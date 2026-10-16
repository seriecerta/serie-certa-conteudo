#!/usr/bin/env python3
"""Publica no blog (seriecerta.online/blog) as matérias aprovadas do pacote diário.

Uso:
  python blog/publicar_blog.py --vencidos                  # hoje e ontem (a rotina de hora em hora chama)
  python blog/publicar_blog.py --data 2026-10-16           # um dia específico
  python blog/publicar_blog.py --vencidos --simular        # valida o que está no disco, sem baixar da nuvem nem publicar
  python blog/publicar_blog.py --verificar <pasta>         # checa uma matéria (redator e revisor usam)
  python blog/publicar_blog.py --listar [--dias 60]        # matérias no ar (pauta, repetição e links internos)

Cada matéria fica em saida/<data>/blog/<nn>-<slug>/ com:
  materia.json  metadados (título, slug, categoria, tags, humor, SEO, capa_alt, series, fontes, quando)
  materia.md    texto em Markdown (ver blog/README.md para os atalhos [[app]], [[leia: slug]], :::dica …)
  cena.html     arte da imagem de destaque no motor → quadros/01.jpg (renderizar.py --imagens --formato 16x9)
  imagens/      pôsteres oficiais (scripts/posters.py) usados no texto e na capa

Travas (as mesmas do publicador das redes):
  - Pula o dia inteiro se existir saida/<data>/PAUSAR.
  - Só publica o que o revisor pôs em "blog_aprovadas" de saida/<data>/revisao.json.
  - Só publica depois do "quando" da matéria. Atraso não descarta: matéria de blog pode sair mais tarde.
  - Toda série de "series" precisa do pôster oficial (imagens/posters.json) aparecendo no texto.
  - Sem imagem de destaque (quadros/01.jpg 1920×1080) e texto alternativo, não sai.
  - Cada matéria sai uma vez só (estado-blog.json + checagem do slug no banco).
  - PUBLICACAO_AUTOMATICA diferente de true = só simula.

Grava direto nas tabelas blog_* do Supabase com a chave de serviço (a mesma das redes) e sobe as imagens
para o bucket público "blog". Nenhuma senha do painel é usada. As páginas do blog se atualizam pelo ISR
(home e matéria a cada 5 min; sitemap a cada 1 h).
"""
import argparse
import datetime as dt
import json
import mimetypes
import os
import pathlib
import re
import subprocess
import sys
import unicodedata
from zoneinfo import ZoneInfo

import requests

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "saida"
TZ = ZoneInfo("America/Sao_Paulo")
AGORA = dt.datetime.now(TZ)
BUCKET = "blog"
AUTOR_PADRAO = "redacao"
MIN_PALAVRAS = 600

HUMORES = {"sono", "ansioso", "romantico", "triste", "animado", "estressado", "curioso", "feliz"}
CORES = HUMORES | {"brasa", "papel"}
SLUGS_RESERVADOS = {"categoria", "tag", "autor", "busca", "rss", "rss-xml", "feed", "newsletter", "salvos",
                    "politica-editorial", "anuncie", "admin", "pagina", "api"}
SLUG_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PROIBIDOS = ["você sabia que", "voce sabia que", "fala, galera", "fala galera", "não esquece de curtir"]


# ---------------------------------------------------------------- utilidades
def carregar_env():
    env = RAIZ / ".env"
    if env.exists():
        for linha in env.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def ler_json(p: pathlib.Path, padrao):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else padrao


def salvar_json(p: pathlib.Path, dados):
    p.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def log(pasta_dia: pathlib.Path, texto: str):
    print(texto)
    with (pasta_dia / "publicacao.log.md").open("a", encoding="utf-8") as f:
        f.write(f"- {dt.datetime.now(TZ):%H:%M} [blog] {texto}\n")


def slugificar(s: str, maximo=100) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower().replace("&", " e ")
    return re.sub(r"-+$", "", re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:maximo])


def _slug_serie(t: str) -> str:
    return slugificar(re.sub(r"\s*\(\d{4}\)\s*$", "", t))


def quando(meta) -> dt.datetime:
    q = dt.datetime.fromisoformat(meta["quando"])
    return q if q.tzinfo else q.replace(tzinfo=TZ)


def limpar(v, maximo: int) -> str:
    return v.replace("\x00", "").replace("\r\n", "\n").strip()[:maximo] if isinstance(v, str) else ""


# ---------------------------------------------------------------- Supabase
class Banco:
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL", "").rstrip("/")
        if not self.url:
            raise RuntimeError("Defina SUPABASE_URL")
        chave = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
        # Sem chave no ambiente: a "API credential" da nuvem anexa os cabeçalhos pelo proxy.
        self.h = {} if not chave else ({"apikey": chave} if chave.startswith("sb_")
                                       else {"Authorization": f"Bearer {chave}", "apikey": chave})

    def _r(self, metodo, tabela, params=None, corpo=None, prefer=None):
        h = {**self.h, "Content-Type": "application/json"}
        if prefer:
            h["Prefer"] = prefer
        r = requests.request(metodo, f"{self.url}/rest/v1/{tabela}", headers=h, params=params, json=corpo, timeout=60)
        if not r.ok:
            raise RuntimeError(f"Supabase {r.status_code} em {tabela}: {r.text[:300]}")
        return r.json() if r.text else None

    def ler(self, tabela, **params):
        return self._r("GET", tabela, params=params)

    def inserir(self, tabela, corpo):
        return self._r("POST", tabela, corpo=corpo, prefer="return=representation")

    def subir(self, arquivo: pathlib.Path, caminho: str) -> str:
        tipo = mimetypes.guess_type(arquivo.name)[0] or "application/octet-stream"
        with arquivo.open("rb") as f:
            r = requests.post(f"{self.url}/storage/v1/object/{BUCKET}/{caminho}",
                              headers={**self.h, "Content-Type": tipo, "x-upsert": "true",
                                       "Cache-Control": "max-age=31536000"}, data=f, timeout=300)
        if not r.ok:
            raise RuntimeError(f"upload {caminho}: {r.status_code} {r.text[:200]}")
        return f"{self.url}/storage/v1/object/public/{BUCKET}/{caminho}"


# ---------------------------------------------------------------- Markdown → blocos (espelha lib/blog/conteudo.ts)
def ler_materia(pasta: pathlib.Path):
    """Converte materia.md nos blocos do CMS. Imagens locais ficam como 'local:imagens/x.jpg' até o upload.
    Atalhos além do Markdown básico:
      [[app]] / [[app: humor]] / [[app: humor | texto do botão]]  → chamada para o app (o CTA da matéria)
      [[leia: slug-da-materia]]                                   → card "Leia também" (só matéria no ar)
      [[video]]                                                    → vídeo do YouTube da peça "video_da_peca"
      :::dica Título  …  :::   (também :::info e :::atencao)       → caixa de destaque
      ![alt](imagens/x.jpg "legenda")                              → imagem (pôster: crédito automático)
    """
    linhas = (pasta / "materia.md").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    blocos, par, lista, cit, tab = [], [], None, [], []
    caixa = None

    def fechar():
        nonlocal par, lista, cit, tab
        if tab:
            blocos.append({"tipo": "tabela", "cabecalho": tab[0], "linhas": tab[1:]})
            tab = []
        if par:
            blocos.append({"tipo": "paragrafo", "texto": " ".join(par).strip()})
            par = []
        if lista:
            blocos.append({"tipo": "lista", "ordenada": lista[0], "itens": lista[1]})
            lista = None
        if cit:
            blocos.append({"tipo": "citacao", "texto": " ".join(cit).strip()})
            cit = []

    for bruta in linhas:
        l = bruta.strip()
        if caixa is not None:  # dentro de :::dica … :::
            if l == ":::":
                blocos.append({"tipo": "destaque", "variante": caixa[0], "texto": "\n".join(caixa[2]).strip(),
                               **({"titulo": caixa[1]} if caixa[1] else {})})
                caixa = None
            else:
                caixa[2].append(l)
            continue
        if not l:
            fechar()
            continue
        if m := re.match(r"^:::(dica|info|atencao)\s*(.*)$", l):
            fechar()
            caixa = (m.group(1), m.group(2).strip(), [])
            continue
        if re.match(r"^\|.*\|$", l):
            if par or lista or cit:
                t, tab = tab, []
                fechar()
                tab = t
            if not re.match(r"^\|[\s:|-]+\|$", l):
                tab.append([c.strip() for c in l[1:-1].split("|")])
            continue
        if tab:
            fechar()
        if m := re.match(r"^\[\[app(?::\s*([a-z]+))?(?:\s*\|\s*(.+))?\]\]$", l):
            fechar()
            b = {"tipo": "cta_app"}
            if m.group(1) in HUMORES:
                b["humor"] = m.group(1)
            if m.group(2):
                b["texto"] = m.group(2).strip()[:200]
            blocos.append(b)
        elif m := re.match(r"^\[\[leia:\s*([a-z0-9-]+)\s*\]\]$", l):
            fechar()
            blocos.append({"tipo": "leia_tambem", "slug": m.group(1)})
        elif l == "[[video]]":
            fechar()
            blocos.append({"tipo": "video", "url": "peca:"})
        elif m := re.match(r"^(#{1,3})\s+(.+)$", l):
            fechar()
            blocos.append({"tipo": "titulo", "nivel": 3 if len(m.group(1)) == 3 else 2, "texto": m.group(2).strip(),
                           "_h1": len(m.group(1)) == 1})
        elif re.match(r"^(-{3,}|\*{3,}|_{3,})$", l):
            fechar()
            blocos.append({"tipo": "separador"})
        elif m := re.match(r'^!\[([^\]]*)\]\((\S+?)(?:\s+"([^"]*)")?\)$', l):
            fechar()
            url = m.group(2)
            b = {"tipo": "imagem", "url": url if url.startswith("https://") else f"local:{url}", "alt": m.group(1)}
            if m.group(3):
                b["legenda"] = m.group(3)
            blocos.append(b)
        elif m := re.match(r"^[-*•]\s+(.+)$", l):
            if par or cit or (lista and lista[0]):
                fechar()
            lista = lista or (False, [])
            lista[1].append(m.group(1).strip())
        elif m := re.match(r"^\d+[.)]\s+(.+)$", l):
            if par or cit or (lista and not lista[0]):
                fechar()
            lista = lista or (True, [])
            lista[1].append(m.group(1).strip())
        elif m := re.match(r"^>\s?(.*)$", l):
            if par or lista:
                fechar()
            cit.append(m.group(1))
        else:
            if lista or cit:
                fechar()
            par.append(l)
    fechar()
    if caixa is not None:
        blocos.append({"tipo": "_erro", "texto": "caixa :::" + caixa[0] + " sem ::: de fechamento"})
    return blocos


def sem_marcas(s: str) -> str:
    s = re.sub(r"\[([^\]\n]{1,200})\]\(([^)\s]{1,600})\)", r"\1", s or "")
    s = re.sub(r"\*\*([^*\n](?:[^\n]*?[^*\n])?)\*\*", r"\1", s)
    return re.sub(r"\*([^*\s](?:[^*\n]*?[^*\s])?)\*", r"\1", s)


def normalizar(blocos):
    """Mesmos limites de normalizarUm() do CMS; descarta o que o site não renderiza."""
    saida = []
    for b in blocos:
        t = b["tipo"]
        if t == "paragrafo" and (x := limpar(b["texto"], 6000)):
            saida.append({"tipo": t, "texto": x})
        elif t == "titulo" and (x := limpar(b["texto"], 200).replace("\n", " ")):
            saida.append({"tipo": t, "nivel": b["nivel"], "texto": x})
        elif t == "lista":
            itens = [limpar(i, 1200) for i in b["itens"] if limpar(i, 1200)][:60]
            if itens:
                saida.append({"tipo": t, "ordenada": b["ordenada"], "itens": itens})
        elif t == "citacao" and (x := limpar(b["texto"], 1500)):
            saida.append({"tipo": t, "texto": x})
        elif t == "imagem":
            o = {"tipo": t, "url": b["url"], "alt": limpar(b.get("alt"), 250)}
            for k, mx in (("legenda", 300), ("credito", 200)):
                if limpar(b.get(k), mx):
                    o[k] = limpar(b[k], mx)
            saida.append(o)
        elif t == "destaque" and (x := limpar(b["texto"], 3000)):
            saida.append({"tipo": t, "variante": b["variante"], "texto": x,
                          **({"titulo": limpar(b["titulo"], 120)} if b.get("titulo") else {})})
        elif t == "tabela":
            cab = [limpar(c, 120) for c in b["cabecalho"]][:8]
            linhas = [[limpar(l[i] if i < len(l) else "", 400) for i in range(len(cab))] for l in b["linhas"]]
            linhas = [l for l in linhas if any(l)][:80]
            if cab and linhas:
                saida.append({"tipo": t, "cabecalho": cab, "linhas": linhas})
        elif t in ("leia_tambem", "cta_app", "separador", "video"):
            saida.append(b)
    return saida[:400]


def texto_plano(blocos) -> str:
    partes = []
    for b in blocos:
        t = b["tipo"]
        if t in ("paragrafo", "titulo"):
            partes.append(sem_marcas(b["texto"]))
        elif t == "lista":
            partes.append("\n".join(sem_marcas(i) for i in b["itens"]))
        elif t == "citacao":
            partes.append(sem_marcas(b["texto"]))
        elif t == "destaque":
            partes.append(". ".join(x for x in (b.get("titulo"), sem_marcas(b["texto"])) if x))
        elif t == "tabela":
            partes.append("\n".join([" | ".join(b["cabecalho"])] + [" | ".join(l) for l in b["linhas"]]))
        elif t == "imagem" and b.get("legenda"):
            partes.append(b["legenda"])
    return "\n\n".join(p for p in partes if p)


def tempo_leitura(texto: str) -> int:
    return min(240, max(1, -(-len(re.findall(r"[^\W_]+", texto)) // 200)))


# ---------------------------------------------------------------- validação
def dimensoes(arquivo: pathlib.Path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                        "-of", "json", str(arquivo)], capture_output=True, text=True)
    s = (json.loads(r.stdout or "{}").get("streams") or [{}])[0]
    return s.get("width", 0), s.get("height", 0)


def validar(pasta: pathlib.Path, banco: Banco | None = None, taxonomia=None) -> list:
    erros = []
    meta = ler_json(pasta / "materia.json", None)
    if meta is None:
        return ["falta materia.json"]
    if not (pasta / "materia.md").exists():
        return ["falta materia.md"]
    titulo = meta.get("titulo", "")
    if not 3 <= len(titulo) <= 160:
        erros.append("título precisa de 3 a 160 caracteres")
    slug = meta.get("slug") or slugificar(titulo)
    if not SLUG_VALIDO.match(slug) or len(slug) > 120 or slug in SLUGS_RESERVADOS:
        erros.append(f"slug inválido ou reservado: {slug}")
    for campo, mx in (("subtitulo", 300), ("resumo", 400), ("seo_titulo", 90), ("meta_descricao", 200),
                      ("palavra_chave", 80), ("capa_alt", 250), ("capa_legenda", 300)):
        if len(meta.get(campo) or "") > mx:
            erros.append(f"{campo} > {mx} caracteres")
    for campo in ("resumo", "meta_descricao", "capa_alt", "categoria"):
        if not meta.get(campo):
            erros.append(f"falta '{campo}'")
    if meta.get("humor") and meta["humor"] not in CORES:
        erros.append(f"humor inválido: {meta['humor']} (use {', '.join(sorted(CORES))})")
    try:
        quando(meta)
    except Exception:
        erros.append("'quando' ausente ou inválido (ex.: 2026-10-16T09:00:00-03:00)")
    for f in meta.get("fontes", []):
        if f.get("url") and not re.match(r"^https?://\S+$", f["url"]):
            erros.append(f"fonte com link inválido: {f.get('titulo')}")

    blocos = ler_materia(pasta)
    erros += [b["texto"] for b in blocos if b["tipo"] == "_erro"]
    if any(b.get("_h1") for b in blocos):
        erros.append("use ## e ### no texto: o título (H1) já vem do materia.json")
    norm = normalizar(blocos)
    plano = texto_plano(norm)
    palavras = len(re.findall(r"[^\W_]+", plano))
    if palavras < MIN_PALAVRAS:
        erros.append(f"texto curto: {palavras} palavras (mínimo {MIN_PALAVRAS})")
    ctas = sum(1 for b in norm if b["tipo"] == "cta_app")
    if ctas != 1:
        erros.append(f"precisa de exatamente 1 [[app]] (CTA único); tem {ctas}")
    baixo = (titulo + "\n" + plano).lower()
    erros += [f"expressão proibida pela voz: '{p}'" for p in PROIBIDOS if p in baixo]

    # imagens locais existem
    for b in norm:
        if b["tipo"] == "imagem":
            if b["url"].startswith("local:") and not (pasta / b["url"][6:]).exists():
                erros.append(f"imagem ausente: {b['url'][6:]}")
            if not b.get("alt"):
                erros.append(f"imagem sem texto alternativo: {b['url'].removeprefix('local:')}")

    # imagem de destaque
    capa = pasta / "quadros" / "01.jpg"
    if not capa.exists() or capa.stat().st_size == 0:
        erros.append("sem imagem de destaque (renderize cena.html: --imagens --formato 16x9 → quadros/01.jpg)")
    elif dimensoes(capa) != (1920, 1080):
        erros.append(f"imagem de destaque precisa ser 1920×1080 (está {dimensoes(capa)})")

    # pôster oficial de toda série indicada (mesma regra do publicar.py)
    if "series" not in meta:
        erros.append('falta o campo "series" (lista das séries indicadas; [] se nenhuma)')
    registro = ler_json(pasta / "imagens" / "posters.json", {})
    md = (pasta / "materia.md").read_text(encoding="utf-8")
    for nome in meta.get("series") or []:
        alvo = _slug_serie(nome)
        arq = next((k for k, v in registro.items()
                    if alvo and alvo in {_slug_serie(v.get("pedido", "")), _slug_serie(v.get("encontrado", "")),
                                         _slug_serie(k[:-4])}), None)
        if not arq or not (pasta / "imagens" / arq).exists():
            erros.append(f"sem pôster oficial de '{nome}' (rode scripts/posters.py {pasta} \"{nome}\")")
        elif f"(imagens/{arq}" not in md:
            erros.append(f"pôster de '{nome}' não aparece no texto (use ![Pôster de {nome}](imagens/{arq}))")

    # banco: categoria existe e links internos apontam para matéria no ar
    if banco and taxonomia is not None:
        if meta.get("categoria") and meta["categoria"] not in taxonomia["categorias"]:
            erros.append(f"categoria inexistente: {meta['categoria']} (use {', '.join(taxonomia['categorias'])})")
        for b in norm:
            if b["tipo"] == "leia_tambem" and b["slug"] not in taxonomia["no_ar"]:
                erros.append(f"[[leia: {b['slug']}]] não é uma matéria no ar")
        if slug in taxonomia["no_ar"] and taxonomia["no_ar"][slug] != titulo:
            erros.append(f"já existe outra matéria em /blog/{slug}: escolha outro slug")
    return erros


def carregar_taxonomia(banco: Banco):
    cats = {c["slug"]: c for c in banco.ler("blog_categorias", select="id,slug,nome", ativa="eq.true")}
    no_ar = {m["slug"]: m["titulo"] for m in banco.ler("blog_materias", select="slug,titulo",
                                                         status="in.(publicado,agendado)", limit="2000")}
    autores = {a["slug"]: a for a in banco.ler("blog_autores", select="id,slug,nome")}
    return {"categorias": cats, "no_ar": no_ar, "autores": autores}


# ---------------------------------------------------------------- publicação
def link_da_peca(pasta_dia: pathlib.Path, peca: str | None) -> str | None:
    """Link do YouTube da peça do dia, se já estiver público (para o atalho [[video]])."""
    if not peca:
        return None
    for v in ler_json(pasta_dia / peca / "estado-publicacao.json", {}).values():
        links = [l for l in v.get("links", []) if "youtu" in l]
        if not links:
            continue
        if v.get("status") == "publicado":
            return links[0]
        ag = v.get("agendado_para")
        if v.get("status") == "agendado" and ag and dt.datetime.fromisoformat(ag.replace("Z", "+00:00")) <= AGORA:
            return links[0]
    return None


def credito_poster(pasta: pathlib.Path, arquivo: str) -> str | None:
    registro = ler_json(pasta / "imagens" / "posters.json", {})
    return "Pôster: divulgação (via TVmaze)" if arquivo in registro else None


def publicar(pasta: pathlib.Path, pasta_dia: pathlib.Path, banco: Banco, tax) -> str:
    meta = ler_json(pasta / "materia.json", {})
    slug = meta.get("slug") or slugificar(meta["titulo"])
    base = f"materias/{slug}"

    blocos = []
    for b in normalizar(ler_materia(pasta)):
        if b["tipo"] == "imagem" and b["url"].startswith("local:"):
            rel = b["url"][6:]
            arq = rel.split("/")[-1]
            b["url"] = banco.subir(pasta / rel, f"{base}/{arq}")
            if (cred := credito_poster(pasta, arq)) and "credito" not in b:
                b["credito"] = cred
        elif b["tipo"] == "video":
            url = link_da_peca(pasta_dia, meta.get("video_da_peca"))
            if not url:
                continue  # vídeo ainda não está no ar: a matéria sai sem ele
            b = {"tipo": "video", "url": url, **({"titulo": meta["video_titulo"]} if meta.get("video_titulo") else {})}
        blocos.append(b)
    capa_url = banco.subir(pasta / "quadros" / "01.jpg", f"{base}/capa-{AGORA:%Y%m%d}.jpg")

    cat = tax["categorias"][meta["categoria"]]
    autor = tax["autores"].get(meta.get("autor", AUTOR_PADRAO)) or tax["autores"].get(AUTOR_PADRAO)
    tags = [t for t in dict.fromkeys(limpar(t, 60) for t in meta.get("tags", [])) if len(t) >= 2][:20]
    plano = texto_plano(blocos)
    agora = dt.datetime.now(dt.timezone.utc).isoformat()
    registro = {
        "titulo": meta["titulo"], "slug": slug,
        "subtitulo": meta.get("subtitulo") or None, "resumo": meta["resumo"],
        "conteudo": blocos, "texto_plano": plano,
        "termos": " ".join([cat["nome"], *( [autor["nome"]] if autor else []), *tags])[:2000],
        "tempo_leitura": tempo_leitura(plano),
        "categoria_id": cat["id"], "autor_id": autor["id"] if autor else None,
        "status": "publicado", "publicado_em": agora, "atualizado_em": agora,
        "capa_url": capa_url, "capa_alt": meta["capa_alt"],
        "capa_credito": meta.get("capa_credito") or ("Arte: Série Certa · pôsteres: divulgação" if meta.get("series")
                                                     else "Arte: Série Certa"),
        "capa_legenda": meta.get("capa_legenda") or None,
        "capa_cor": meta.get("humor") if meta.get("humor") in CORES else "brasa",
        "seo_titulo": meta.get("seo_titulo") or None, "meta_descricao": meta["meta_descricao"],
        "palavra_chave": meta.get("palavra_chave") or None,
        "indexar": True, "destaque": bool(meta.get("destaque")), "prioridade": 0,
        "fontes": [{"titulo": limpar(f["titulo"], 200), "url": limpar(f.get("url", ""), 600)}
                   for f in meta.get("fontes", []) if f.get("titulo")][:30],
    }
    m = banco.inserir("blog_materias", registro)[0]

    if tags:
        existentes = {t["slug"]: t["id"] for t in banco.ler("blog_tags", select="id,slug",
                                                             slug=f"in.({','.join(slugificar(t, 60) for t in tags)})")}
        novas = [{"slug": slugificar(t, 60), "nome": t} for t in tags if slugificar(t, 60) not in existentes]
        if novas:
            for t in banco.inserir("blog_tags", novas):
                existentes[t["slug"]] = t["id"]
        ids = list(dict.fromkeys(existentes[slugificar(t, 60)] for t in tags if slugificar(t, 60) in existentes))
        if ids:
            banco.inserir("blog_materia_tags", [{"materia_id": m["id"], "tag_id": i} for i in ids])
    try:
        banco.inserir("blog_auditoria", {"entidade": "materia", "entidade_id": m["id"], "acao": "criar",
                                         "detalhes": {"titulo": meta["titulo"], "slug": slug,
                                                      "origem": "agente serie-certa-conteudo",
                                                      "pacote": f"{pasta_dia.name}/blog/{pasta.name}"}})
    except Exception as e:  # auditoria não segura a publicação
        print(f"! auditoria não registrada: {e}")
    return f"https://seriecerta.online/blog/{slug}"


def processar_dia(data: str, simular: bool, banco: Banco):
    pasta_dia = SAIDA / data
    pasta_blog = pasta_dia / "blog"
    if not pasta_blog.exists():
        return
    if (pasta_dia / "PAUSAR").exists():
        print(f"{data}: PAUSAR encontrado, nada do blog será publicado.")
        return
    revisao = ler_json(pasta_dia / "revisao.json", None)
    if revisao is None:
        print(f"{data}: sem revisao.json — o revisor ainda não aprovou nada.")
        return
    aprovadas = set(revisao.get("blog_aprovadas", []))
    tax = None
    for pasta in sorted(p for p in pasta_blog.iterdir() if p.is_dir() and p.name in aprovadas):
        estado_arq = pasta / "estado-blog.json"
        estado = ler_json(estado_arq, {})
        if estado.get("status") == "publicado" or estado.get("tentativas", 0) >= 2:
            continue
        meta = ler_json(pasta / "materia.json", {})
        try:
            if quando(meta) > AGORA:
                continue
        except Exception:
            pass  # o validar() acusa
        tax = tax or carregar_taxonomia(banco)
        slug = meta.get("slug") or slugificar(meta.get("titulo", ""))
        # Já está no ar com o mesmo título (ex.: o estado não chegou a ser salvo na rodada anterior)
        if tax["no_ar"].get(slug) == meta.get("titulo"):
            if not simular:
                estado = {"status": "publicado", "em": AGORA.isoformat(), "link": f"https://seriecerta.online/blog/{slug}"}
                salvar_json(estado_arq, estado)
            continue
        erros = validar(pasta, banco, tax)
        if erros:
            msg = f"✗ {pasta.name}: {'; '.join(erros)}"
            if simular:
                print(f"[simulação] {msg}")
            elif estado.get("erros") != erros:
                salvar_json(estado_arq, {"status": "invalido", "erros": erros})
                log(pasta_dia, msg)
            continue
        if simular:
            print(f"[simulação] publicaria {pasta.name} em https://seriecerta.online/blog/{slug}")
            continue
        try:
            link = publicar(pasta, pasta_dia, banco, tax)
            salvar_json(estado_arq, {"status": "publicado", "em": AGORA.isoformat(), "link": link})
            tax["no_ar"][slug] = meta["titulo"]
            log(pasta_dia, f"✓ {pasta.name} publicado: {link}")
        except Exception as e:
            salvar_json(estado_arq, {"status": "erro", "tentativas": estado.get("tentativas", 0) + 1, "erro": str(e)[:500]})
            log(pasta_dia, f"✗ {pasta.name}: {str(e)[:200]}")


def listar(banco: Banco, dias: int):
    desde = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=dias)).isoformat()
    linhas = banco.ler("blog_materias", select="slug,titulo,publicado_em,blog_categorias(slug)",
                       status="in.(publicado,agendado)", publicado_em=f"gte.{desde}", order="publicado_em.desc",
                       limit="1000")
    for m in linhas:
        cat = (m.get("blog_categorias") or {}).get("slug", "-")
        print(f"{(m['publicado_em'] or '')[:10]} | {cat} | {m['slug']} | {m['titulo']}")
    print(f"= {len(linhas)} matérias no ar nos últimos {dias} dias")


def main():
    carregar_env()
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--data")
    g.add_argument("--vencidos", action="store_true")
    g.add_argument("--verificar", metavar="PASTA")
    g.add_argument("--listar", action="store_true")
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--dias", type=int, default=60)
    a = ap.parse_args()
    banco = Banco()

    if a.listar:
        return listar(banco, a.dias)
    if a.verificar:
        pasta = pathlib.Path(a.verificar)
        erros = validar(pasta, banco, carregar_taxonomia(banco))
        plano = texto_plano(normalizar(ler_materia(pasta))) if (pasta / "materia.md").exists() else ""
        print(f"{pasta.name}: {len(re.findall(r'[^\W_]+', plano))} palavras, {tempo_leitura(plano)} min de leitura")
        print("\n".join(f"✗ {e}" for e in erros) or "✓ pronta para o revisor")
        sys.exit(1 if erros else 0)

    simular = a.simular or os.environ.get("PUBLICACAO_AUTOMATICA", "false").lower() != "true"
    if simular and not a.simular:
        print("PUBLICACAO_AUTOMATICA não está true — rodando em simulação.")
    datas = [a.data] if a.data else [(AGORA - dt.timedelta(days=1)).strftime("%Y-%m-%d"), AGORA.strftime("%Y-%m-%d")]

    sys.path.insert(0, str(RAIZ / "scripts"))
    sys.dont_write_bytecode = True
    import nuvem
    na_nuvem = nuvem.em_nuvem()
    # Simulação valida o que está no disco: baixar da nuvem sobrescreveria revisao.json/pauta locais recém-editados.
    if na_nuvem and not simular:
        for d in datas:
            nuvem.baixar_pacote(d)
    try:
        for d in datas:
            processar_dia(d, simular, banco)
    finally:
        if na_nuvem and not simular:
            for d in datas:
                nuvem.subir_pacote(d, so_texto=True)


if __name__ == "__main__":
    main()
