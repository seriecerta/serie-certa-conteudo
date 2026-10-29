#!/usr/bin/env python3
"""Painel de conteúdo do Série Certa: backlog, o que saiu, mix de redes/formatos/pilares,
desdobramentos, engajamento e cliques.

Uso:
  python painel/painel.py               # lê saida/ + historico/ + painel/metricas.json e gera painel/index.html
  python painel/painel.py --metricas    # antes, busca métricas novas (Instagram, YouTube, PostHog)
  python painel/painel.py --metricas --dias 60

Só leitura nas redes: nunca publica, nunca mexe em revisao.json, estado-publicacao.json ou PAUSAR.

De onde vem cada número:
  - Backlog e status: saida/<data>/00-pauta.md (rascunho de amanhã e ideias), revisao.json,
    publicar.json e estado-publicacao.json (escrito pelo publicar.py).
  - Séries: historico/publicados.md (casado por data + gancho).
  - Instagram (todas as publicações da conta, inclusive as que não saíram pelo publicar.py): views, alcance,
    curtidas, comentários, envios, salvamentos, visitas ao perfil, follows. Na 1ª coleta, histórico de até 2 anos.
    Stories só têm insight nas 24 h em que estão no ar: rode --metricas nesse intervalo, o painel guarda o número.
  - Instagram (conta, por dia): cliques no link da bio (website_clicks), visitas ao perfil, alcance, seguidores.
  - YouTube (todos os vídeos do canal, inclusive agendados): views, curtidas, comentários e inscritos.
  - Cliques nos links com UTM: PostHog (opcional; POSTHOG_API_KEY + POSTHOG_PROJECT_ID no .env).
  - Blog: matérias de saida/<data>/blog/ (materia.json, estado-blog.json) + todas as matérias no ar no banco do blog
    (blog_materias) com as leituras por dia (blog_visualizacoes, mesmo Supabase das redes, sem chave nova).
    Leitura até 90% e cliques no app vêm do PostHog (article_scroll_90, platform_cta_click), se configurado.
Na nuvem, baixa do Supabase os textos de todos os dias e guarda as métricas em pacotes-redes/painel/metricas.json.
"""
import argparse
import base64
import datetime as dt
import json
import os
import pathlib
import re
import sys
import unicodedata
from zoneinfo import ZoneInfo

import requests

PAINEL = pathlib.Path(__file__).resolve().parent
RAIZ = PAINEL.parent
SAIDA = RAIZ / "saida"
CRED = RAIZ / ".credenciais"
METRICAS = PAINEL / "metricas.json"
TZ = ZoneInfo("America/Sao_Paulo")
AGORA = dt.datetime.now(TZ)
DATA_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

sys.path.insert(0, str(RAIZ / "scripts"))
import nuvem  # noqa: E402


def ler_json(p: pathlib.Path, padrao):
    try:
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else padrao
    except json.JSONDecodeError:
        return padrao


def normalizar(txt: str) -> str:
    txt = unicodedata.normalize("NFKD", txt.lower())
    return re.sub(r"[^a-z0-9 ]+", "", "".join(c for c in txt if not unicodedata.combining(c))).strip()


def exp_rotulo(exp) -> str:
    """{"id": "gancho-pergunta", "variante": "B"} -> "gancho-pergunta·B" (campo opcional do publicar.json)."""
    return f"{exp.get('id', '')}·{exp.get('variante', '')}" if isinstance(exp, dict) and exp.get("id") else ""


def legivel(slug: str) -> str:
    return re.sub(r"^\d\d-", "", slug).replace("-", " ").capitalize()


# ---------------------------------------------------------------- pauta
CAMPOS = {"formato": "formato", "pilar": "pilar", "pilar / job": "pilar", "job": "job", "humor": "humor",
          "cta / funil": "cta", "horário": "horario", "horários": "horario"}
FUNIS = ("Descoberta", "Consideração", "Conversão", "Retenção")
PILARES = {1: "Série pro seu humor", 2: "Órfã de série", 3: "Dilema do casal", 4: "MIA acertou? / prova",
           5: "Bastidor do produto"}  # estrategia/07-pilares-e-formatos.md
CAMPO_RE = re.compile(r"\*\*([^:*]+):?\*\*:?\s*(.*)")


def ler_pauta(pasta_dia: pathlib.Path) -> dict:
    """Peças da pauta por data ({data: {slug: campos}}) + ideias guardadas."""
    arq = pasta_dia / "00-pauta.md"
    pecas, ideias = {}, []
    if not arq.exists():
        return {"pecas": pecas, "ideias": ideias}
    data_atual, atual, secao = pasta_dia.name, None, ""
    for linha in arq.read_text(encoding="utf-8").splitlines():
        if linha.startswith("# "):
            m = DATA_RE.search(linha)
            data_atual = m.group(0) if m else pasta_dia.name
            atual, secao = None, "dia"
            continue
        if linha.startswith("## "):
            m = re.match(r"## (\d\d-[a-z0-9-]+)", linha)
            if m:
                atual = {"slug": m.group(1), "data": data_atual, "texto": ""}
                pecas.setdefault(data_atual, {})[m.group(1)] = atual
                secao = "peca"
            else:
                atual = None
                secao = "ideias" if "ideia" in linha.lower() else "outro"
            continue
        if secao == "ideias" and linha.startswith("- "):
            ideias.append({"texto": re.sub(r"\*\*|`", "", linha[2:]).strip(), "origem": pasta_dia.name})
        if atual is None:
            continue
        atual["texto"] += linha + "\n"
        if not linha.startswith("- **"):
            continue
        # vários campos na mesma linha: "- **Pilar:** 1 · **Job:** principal · **Humor:** vários."
        for parte in re.split(r"\s+·\s+(?=\*\*)", linha[2:]):
            m = CAMPO_RE.match(parte)
            if not m:
                continue
            chave, valor = m.group(1).strip().lower(), m.group(2).strip()
            if chave.startswith("gancho"):
                g = re.search(r'"([^"]+)"', valor)
                atual.setdefault("gancho", g.group(1) if g else valor)
            elif chave in CAMPOS:
                atual[CAMPOS[chave]] = valor
    for dia in pecas.values():
        for p in dia.values():
            m = re.search(r"Formato recorrente:\s*(.+?)\.?\*\*", p.get("formato", ""))
            rec = re.sub(r"\s*(·\s*Ep.*|\(.*)$", "", m.group(1)).strip() if m else ""
            p["recorrente"] = rec
            p["funil"] = next((f for f in FUNIS if f in p.get("cta", "")), "")
            pil = re.match(r"(\d)\b\.?\s*([^,(/·]*)", p.get("pilar", ""))
            if pil and int(pil.group(1)) in PILARES:
                p["pilar_n"] = int(pil.group(1))
                p["pilar"] = pil.group(2).strip().rstrip(".") or PILARES[p["pilar_n"]]
            else:
                p["pilar_n"], p["pilar"] = 0, p.get("pilar", "")
            p["humor"] = re.sub(r"\s*\(.*", "", p.get("humor", "")).strip()
            cta = re.search(r'"([^"]+)"', p.get("cta", ""))
            p["cta"] = cta.group(1) if cta else ""
            p["horarios"] = re.findall(r"(Instagram|YouTube)\s+(\w+)\s+`([^`]+)`", p.get("horario", ""))
    return {"pecas": pecas, "ideias": ideias}


def ler_publicados() -> list:
    arq = RAIZ / "historico" / "publicados.md"
    linhas = []
    if arq.exists():
        for l in arq.read_text(encoding="utf-8").splitlines():
            partes = [c.strip() for c in l.split("|")]
            if len(partes) == 5 and DATA_RE.fullmatch(partes[0]):
                linhas.append(dict(zip(("data", "formato", "humor", "series", "gancho"), partes)))
    return linhas


# ---------------------------------------------------------------- inventário
FORMATO = {("instagram", "REELS"): "Reels", ("instagram", "CAROUSEL"): "Carrossel",
           ("instagram", "STORIES"): "Stories", ("instagram", "IMAGE"): "Feed",
           ("youtube", "short"): "Short", ("youtube", "longo"): "Vídeo longo", ("tiktok", "video"): "TikTok",
           ("blog", "materia"): "Matéria"}
SLOT_BLOG = {"09": "Pelo humor", "11": "Streaming da semana", "14": "Acabou X?", "17": "Guia", "20": "Lista da MIA em texto"}


def status_de(estado, aprovada, bloqueada, pausado, quando):
    st = estado.get("status")
    if st == "agendado" and quando <= AGORA:
        return "publicado"  # o YouTube soltou sozinho no publishAt
    if st in ("publicado", "agendado", "perdido", "invalido", "erro"):
        return st
    if bloqueada:
        return "bloqueado"
    if pausado:
        return "pausado"
    if not aprovada:
        return "revisao"
    # aprovado, horário passou e não há estado: o publicar.py não rodou, ou rodou em simulação
    return "sem-registro" if quando < AGORA - dt.timedelta(hours=1) else "fila"


def inventario() -> dict:
    pubs, rascunhos, ideias = [], [], []
    publicados = ler_publicados()
    pautas = {}
    dias = sorted(p for p in SAIDA.iterdir() if p.is_dir() and DATA_RE.fullmatch(p.name)) if SAIDA.exists() else []
    for pasta_dia in dias:
        pauta = ler_pauta(pasta_dia)
        ideias += pauta["ideias"]
        for data, pecas in pauta["pecas"].items():
            for slug, info in pecas.items():
                pautas.setdefault((data, slug), info)
    existentes = {(d.name, p.name) for d in dias for p in d.iterdir() if p.is_dir()}

    for pasta_dia in dias:
        data = pasta_dia.name
        revisao = ler_json(pasta_dia / "revisao.json", {})
        aprovadas = set(revisao.get("aprovadas", []))
        bloqueadas = revisao.get("bloqueadas", {}) or {}
        pausado = (pasta_dia / "PAUSAR").exists()
        pubs += inventario_blog(pasta_dia, revisao, pausado)
        for pasta in sorted(p for p in pasta_dia.iterdir() if p.is_dir() and p.name != "blog"):
            plano = ler_json(pasta / "publicar.json", {})
            estado = ler_json(pasta / "estado-publicacao.json", {})
            info = pautas.get((data, pasta.name), {})
            itens = list(plano.get("publicacoes", []))
            videos = [p for p in itens if any(a.endswith(".mp4") for a in p.get("arquivos", []))]
            if (pasta / "tiktok.txt").exists() and videos:
                itens.append({"id": "tiktok", "plataforma": "tiktok", "tipo": "video", "quando": videos[0]["quando"],
                              "legenda": (pasta / "tiktok.txt").read_text(encoding="utf-8")})
            if not itens:  # peça ainda sem publicar.json: usa os horários da pauta
                for plat, tipo, q in info.get("horarios", []):
                    itens.append({"id": f"{plat.lower()}-{tipo.lower()}", "plataforma": plat.lower(), "tipo": tipo,
                                  "quando": q, "_sem_plano": True})
            titulo, series = "", ""
            for row in publicados:
                g = normalizar(row["gancho"])[:24]
                alvo = normalizar(info.get("texto", "") + " ".join(i.get("legenda", "") + i.get("titulo", "")
                                                                    for i in itens))
                if row["data"] == data and g and g in alvo:
                    titulo, series = row["gancho"], row["series"].replace("—", "").strip()
                    break
            if not series:  # campo "series" do publicar.json (trava do pôster), sem o ano
                nomes = dict.fromkeys(re.sub(r"\s*\(\d{4}\)$", "", n) for i in itens for n in i.get("series") or [])
                series = "; ".join(nomes)
            titulo = (titulo or info.get("gancho") or next((i.get("titulo") or i.get("legenda", "").split("\n")[0]
                                                            for i in itens if i.get("titulo") or i.get("legenda")), "")
                      or legivel(pasta.name))
            for pub in itens:
                q = dt.datetime.fromisoformat(pub["quando"])
                q = q if q.tzinfo else q.replace(tzinfo=TZ)
                est = estado.get(pub["id"], {})
                if pub["plataforma"] == "tiktok":
                    st = "manual"
                elif pub.get("_sem_plano"):
                    st = "producao"
                else:
                    st = status_de(est, pasta.name in aprovadas, pasta.name in bloqueadas, pausado, q)
                campanha = re.search(r"utm_campaign=([\w-]+)", pub.get("descricao", "") + pub.get("legenda", ""))
                motivo = (bloqueadas.get(pasta.name, "") or est.get("erro", "") or "; ".join(est.get("erros", []))
                          or est.get("motivo", ""))
                pubs.append({
                    "chave": f"{data}/{pasta.name}/{pub['id']}", "data": data, "peca": pasta.name,
                    "mae": plano.get("peca_mae", ""), "titulo": titulo, "plataforma": pub["plataforma"],
                    "formato": FORMATO.get((pub["plataforma"], pub.get("tipo")), pub.get("tipo", "")),
                    "quando": q.isoformat(), "status": st, "motivo": str(motivo)[:300],
                    "links": est.get("links", []), "ids": est.get("ids", []),
                    "pilar": info.get("pilar", ""), "pilar_n": info.get("pilar_n", 0), "humor": info.get("humor", ""),
                    "job": info.get("job", ""), "funil": info.get("funil", ""), "cta": info.get("cta", ""),
                    "recorrente": info.get("recorrente", ""), "series": series,
                    "campanha": campanha.group(1) if campanha else f"{data}-{pasta.name[3:]}",
                    "assinatura": normalizar((pub.get("titulo") or pub.get("legenda") or "").split("\n")[0])[:30],
                    "experimento": exp_rotulo(pub.get("experimento") or plano.get("experimento")),
                    "met": None,
                })

    hoje = AGORA.strftime("%Y-%m-%d")
    for (data, slug), info in sorted(pautas.items()):
        if (data, slug) in existentes or data < hoje:
            continue  # já virou pasta, ou o rascunho venceu sem ser produzido
        for plat, tipo, q in info.get("horarios") or [("", "", data + "T00:00:00-03:00")]:
            rascunhos.append({
                "chave": f"{data}/{slug}/{plat.lower()}-{tipo.lower()}", "data": data, "peca": slug,
                "titulo": info.get("gancho") or legivel(slug), "plataforma": plat.lower(),
                "formato": FORMATO.get((plat.lower(), tipo), tipo), "quando": q, "status": "rascunho",
                "pilar": info.get("pilar", ""), "pilar_n": info.get("pilar_n", 0), "humor": info.get("humor", ""),
                "funil": info.get("funil", ""), "cta": info.get("cta", ""), "recorrente": info.get("recorrente", ""),
            })
    return {"publicacoes": pubs, "rascunhos": rascunhos, "ideias": ideias}


def inventario_blog(pasta_dia: pathlib.Path, revisao: dict, pausado: bool) -> list:
    """Matérias do blog do dia (saida/<data>/blog/<nn>-<slug>/), com o status do blog/publicar_blog.py."""
    pasta_blog = pasta_dia / "blog"
    if not pasta_blog.is_dir():
        return []
    aprovadas = set(revisao.get("blog_aprovadas", []))
    bloqueadas = revisao.get("bloqueadas", {}) or {}
    data, saida = pasta_dia.name, []
    for pasta in sorted(p for p in pasta_blog.iterdir() if p.is_dir()):
        meta = ler_json(pasta / "materia.json", {})
        if not meta.get("titulo"):
            continue
        estado = ler_json(pasta / "estado-blog.json", {})
        try:
            q = dt.datetime.fromisoformat(meta["quando"])
            q = q if q.tzinfo else q.replace(tzinfo=TZ)
        except (KeyError, ValueError):
            q = dt.datetime.fromisoformat(f"{data}T00:00:00-03:00")
        slug = meta.get("slug") or re.sub(r"^\d\d-", "", pasta.name)
        chave_bloq = f"blog/{pasta.name}"
        st = status_de(estado, pasta.name in aprovadas, chave_bloq in bloqueadas, pausado, q)
        motivo = bloqueadas.get(chave_bloq, "") or estado.get("erro", "") or "; ".join(estado.get("erros", []))
        saida.append({
            "chave": f"{data}/blog/{pasta.name}", "data": data, "peca": f"blog/{pasta.name}", "mae": "",
            "titulo": meta["titulo"], "plataforma": "blog", "formato": "Matéria",
            "quando": q.isoformat(), "status": st, "motivo": str(motivo)[:300],
            "links": [estado["link"]] if estado.get("link") else [], "ids": [slug],
            "pilar": "", "pilar_n": 0, "humor": meta.get("humor", ""), "job": "", "funil": "Descoberta",
            "cta": "Chamada para o app", "recorrente": SLOT_BLOG.get(f"{q:%H}", ""), "categoria": meta.get("categoria", ""),
            "series": "; ".join(dict.fromkeys(re.sub(r"\s*\(\d{4}\)$", "", n) for n in meta.get("series") or [])),
            "campanha": f"{data}-{slug}", "assinatura": slug, "experimento": exp_rotulo(meta.get("experimento")),
            "met": None,
        })
    return saida


# ---------------------------------------------------------------- métricas
# Métricas aceitas por tipo de mídia (Instagram API com login do Instagram). Se alguma for recusada,
# insights() cai para uma por uma.
MET_IG = {
    "REELS": ["views", "reach", "likes", "comments", "shares", "saved", "total_interactions",
              "ig_reels_avg_watch_time", "ig_reels_video_view_total_time"],
    "FEED": ["views", "reach", "likes", "comments", "shares", "saved", "total_interactions",
             "profile_visits", "follows"],
    "STORY": ["views", "reach", "replies", "shares", "total_interactions", "profile_visits", "follows"],
}
NUMEROS = ("views", "reach", "likes", "comments", "shares", "saved", "total_interactions", "profile_visits",
           "follows", "replies", "ig_reels_video_view_total_time")


def mesclar(antigo: dict, novo: dict) -> dict:
    """Nunca troca número por vazio (o insight dos Stories some depois de 24 h)."""
    return {**antigo, **{k: v for k, v in novo.items() if v is not None}}


def quando_api(ts: str) -> dt.datetime:
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(TZ)


class ColetorInstagram:
    def __init__(self):
        c = ler_json(CRED / "instagram.json", None)
        if not c:
            raise RuntimeError("sem .credenciais/instagram.json")
        self.c = c
        self.uid = c["ig_user_id"]
        self.base = f"https://graph.instagram.com/{os.environ.get('INSTAGRAM_API_VERSION', 'v25.0')}"

    def get(self, caminho, **params):
        r = requests.get(f"{self.base}/{caminho}", params={**params, "access_token": self.c["access_token"]},
                         timeout=60)
        if not r.ok:
            raise RuntimeError(f"{r.status_code} {r.text[:200]}")
        return r.json()

    def insights(self, caminho, metricas, **params):
        """Pede tudo de uma vez; se a API recusar alguma métrica, tenta uma por uma."""
        def ler(dados):
            out = {}
            for d in dados.get("data", []):
                if "total_value" in d:
                    out[d["name"]] = d["total_value"].get("value")
                else:
                    out[d["name"]] = (d.get("values") or [{}])[-1].get("value")
            return out
        try:
            return ler(self.get(f"{caminho}/insights", metric=",".join(metricas), **params))
        except RuntimeError:
            out = {}
            for m in metricas:
                try:
                    out |= ler(self.get(f"{caminho}/insights", metric=m, **params))
                except RuntimeError:
                    pass
            return out

    def midias(self, desde: dt.datetime) -> list:
        """Todas as publicações do feed/Reels desde a data + os Stories que estão no ar agora."""
        campos = "id,caption,media_type,media_product_type,timestamp,permalink,like_count,comments_count"
        out, apos = [], None
        while True:
            d = self.get(f"{self.uid}/media", fields=campos, limit=50, **({"after": apos} if apos else {}))
            itens = d.get("data", [])
            out += [i for i in itens if quando_api(i["timestamp"]) >= desde]
            apos = d.get("paging", {}).get("cursors", {}).get("after")
            if not itens or "next" not in d.get("paging", {}) or quando_api(itens[-1]["timestamp"]) < desde:
                break
        try:
            out += [{**s, "media_product_type": "STORY"} for s in
                    self.get(f"{self.uid}/stories", fields=campos).get("data", [])]
        except RuntimeError:
            pass  # sem Stories no ar
        return out

    def metricas(self, midia) -> dict:
        tipo = midia.get("media_product_type") or "FEED"
        ins = self.insights(midia["id"], MET_IG.get(tipo, MET_IG["FEED"]))
        return {**ins, "likes": ins.get("likes", midia.get("like_count")),
                "comments": ins.get("comments", midia.get("comments_count"))}

    def conta(self, dias, cache):
        perfil = self.get(self.uid, fields="followers_count,media_count")
        hoje = AGORA.date()
        for i in range(dias):
            d = hoje - dt.timedelta(days=i)
            if str(d) in cache and i > 2:
                continue  # dias fechados não mudam; os 3 últimos sempre são relidos
            ini = dt.datetime.combine(d, dt.time(), TZ)
            fim = min(ini + dt.timedelta(days=1), AGORA)
            cache[str(d)] = mesclar(cache.get(str(d), {}), self.insights(
                self.uid, ["website_clicks", "profile_views", "reach", "accounts_engaged", "views"], period="day",
                metric_type="total_value", since=int(ini.timestamp()), until=int(fim.timestamp())))
        return perfil


def duracao_s(iso: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return ((d * 24 + h) * 60 + mi) * 60 + s


class ColetorYouTube:
    def __init__(self):
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        token = CRED / "youtube-token.json"
        if not token.exists():
            raise RuntimeError("sem .credenciais/youtube-token.json")
        cred = Credentials.from_authorized_user_file(str(token))
        if not cred.valid:
            cred.refresh(Request())
            token.write_text(cred.to_json(), encoding="utf-8")
        self.yt = build("youtube", "v3", credentials=cred, cache_discovery=False)

    def canal(self) -> dict:
        """Inscritos + todos os vídeos enviados (inclui privados e agendados, porque a conta é a dona)."""
        ch = (self.yt.channels().list(part="contentDetails,statistics", mine=True).execute().get("items") or [{}])[0]
        uploads = ch.get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads")
        ids, token = [], None
        while uploads:
            r = self.yt.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=50,
                                             pageToken=token).execute()
            ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
            token = r.get("nextPageToken")
            if not token:
                break
        videos = {}
        for i in range(0, len(ids), 50):
            r = self.yt.videos().list(part="snippet,statistics,contentDetails,status", id=",".join(ids[i:i + 50])).execute()
            for v in r.get("items", []):
                s, st = v.get("statistics", {}), v.get("status", {})
                seg = duracao_s(v.get("contentDetails", {}).get("duration"))
                videos[v["id"]] = {
                    "titulo": v["snippet"]["title"], "timestamp": st.get("publishAt") or v["snippet"]["publishedAt"],
                    "privacidade": st.get("privacyStatus"), "agendado": bool(st.get("publishAt")),
                    "formato": "Short" if 0 < seg <= 180 else "Vídeo longo", "duracao_s": seg,
                    "link": f"https://youtu.be/{v['id']}",
                    "views": int(s.get("viewCount", 0)), "likes": int(s.get("likeCount", 0)),
                    "comments": int(s.get("commentCount", 0)),
                }
        return {"inscritos": int(ch.get("statistics", {}).get("subscriberCount", 0)), "videos": videos}


def coletar_posthog(dias):
    chave, projeto = os.environ.get("POSTHOG_API_KEY"), os.environ.get("POSTHOG_PROJECT_ID")
    if not projeto:
        raise RuntimeError("POSTHOG_PROJECT_ID não definido (opcional)")
    host = os.environ.get("POSTHOG_HOST", "https://us.posthog.com").rstrip("/")
    # Sem chave no ambiente: confia num "Network secret" do ambiente de nuvem, que anexa o cabeçalho pelo proxy.
    cab = {"Authorization": f"Bearer {chave}"} if chave else {}
    sql = f"""SELECT properties.utm_source, properties.utm_medium, properties.utm_campaign, toDate(timestamp),
                     count(), count(DISTINCT person_id)
              FROM events WHERE event = '$pageview' AND properties.utm_medium IN ('organico', 'stories')
                AND timestamp > now() - INTERVAL {int(dias)} DAY
              GROUP BY 1, 2, 3, 4 ORDER BY 4"""
    r = requests.post(f"{host}/api/projects/{projeto}/query/", headers=cab,
                      json={"query": {"kind": "HogQLQuery", "query": sql}}, timeout=120)
    if not r.ok:
        raise RuntimeError(f"PostHog {r.status_code}: {r.text[:200]}")
    return [{"origem": a or "", "meio": b or "", "campanha": c or "", "dia": str(d), "cliques": n, "pessoas": u}
            for a, b, c, d, n, u in r.json().get("results", [])]


def coletar_blog(dias, antigo: dict) -> dict:
    """Todas as matérias no ar (banco do blog) com leituras totais, por dia e em D+7 (dias 0 a 6 desde a publicação)."""
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    if not url:
        raise RuntimeError("SUPABASE_URL não definido")
    cab = nuvem.cabecalhos()

    def ler(tabela, **params):
        linhas, inicio = [], 0
        while True:  # PostgREST devolve no máximo 1000 linhas por pedido
            r = requests.get(f"{url}/rest/v1/{tabela}", headers={**cab, "Range": f"{inicio}-{inicio + 999}"},
                             params=params, timeout=60)
            if not r.ok:
                raise RuntimeError(f"blog {tabela} {r.status_code}: {r.text[:200]}")
            lote = r.json()
            linhas += lote
            if len(lote) < 1000:
                return linhas
            inicio += 1000

    materias = ler("blog_materias", select="id,slug,titulo,publicado_em,status,capa_url,blog_categorias(slug,nome)",
                   status="in.(publicado,agendado)", order="publicado_em.desc")
    por_id = {m["id"]: m for m in materias}
    vistas = ler("blog_visualizacoes", select="materia_id,dia,views", dia=f"gte.{(AGORA - dt.timedelta(days=dias)).date()}")
    out = {}
    for m in materias:
        if not m.get("publicado_em"):
            continue
        anterior = antigo.get(m["slug"], {})
        cat = m.get("blog_categorias") or {}
        out[m["slug"]] = {**anterior, "titulo": m["titulo"], "timestamp": m["publicado_em"], "status": m["status"],
                          "link": f"https://seriecerta.online/blog/{m['slug']}", "categoria": cat.get("nome", ""),
                          "dias": dict(anterior.get("dias", {}))}
    for v in vistas:
        m = por_id.get(v["materia_id"])
        if m and m["slug"] in out:
            out[m["slug"]]["dias"][v["dia"]] = v["views"]
    for md in out.values():
        pub = quando_api(md["timestamp"]).astimezone(TZ).date()
        md["views"] = sum(md["dias"].values())
        if AGORA.date() >= pub + dt.timedelta(days=7):  # D+7 fechado: dias 0 a 6
            md["views_d7"] = sum(n for d, n in md["dias"].items() if dt.date.fromisoformat(d) < pub + dt.timedelta(days=7))
    return out


ORIGENS_IA = {"chatgpt.com": "ChatGPT", "chat.openai.com": "ChatGPT", "perplexity.ai": "Perplexity",
              "www.perplexity.ai": "Perplexity", "gemini.google.com": "Gemini", "copilot.microsoft.com": "Copilot",
              "claude.ai": "Claude"}  # estrategia/12-geo.md → Medição


def coletar_posthog_ia(dias):
    """Visitas ao site vindas de assistentes de IA (referência ou utm_source), por dia, origem e página."""
    chave, projeto = os.environ.get("POSTHOG_API_KEY"), os.environ.get("POSTHOG_PROJECT_ID")
    if not projeto:
        raise RuntimeError("POSTHOG_PROJECT_ID não definido (opcional)")
    host = os.environ.get("POSTHOG_HOST", "https://us.posthog.com").rstrip("/")
    cab = {"Authorization": f"Bearer {chave}"} if chave else {}
    dominios = ", ".join(f"'{d}'" for d in ORIGENS_IA)
    sql = f"""SELECT toDate(timestamp), if(properties.$referring_domain IN ({dominios}), properties.$referring_domain,
                     properties.utm_source), properties.$pathname, count(), count(DISTINCT person_id)
              FROM events WHERE event = '$pageview' AND timestamp > now() - INTERVAL {int(dias)} DAY
                AND (properties.$referring_domain IN ({dominios}) OR properties.utm_source IN ({dominios}))
              GROUP BY 1, 2, 3 ORDER BY 1"""
    r = requests.post(f"{host}/api/projects/{projeto}/query/", headers=cab,
                      json={"query": {"kind": "HogQLQuery", "query": sql}}, timeout=120)
    if not r.ok:
        raise RuntimeError(f"PostHog {r.status_code}: {r.text[:200]}")
    return [{"dia": str(d), "origem": ORIGENS_IA.get(o or "", o or "?"), "pagina": c or "/", "visitas": n, "pessoas": u}
            for d, o, c, n, u in r.json().get("results", [])]


def coletar_posthog_blog(dias):
    """Leitura até 90% e cliques no app por matéria (eventos do blog no PostHog)."""
    chave, projeto = os.environ.get("POSTHOG_API_KEY"), os.environ.get("POSTHOG_PROJECT_ID")
    if not projeto:
        raise RuntimeError("POSTHOG_PROJECT_ID não definido (opcional)")
    host = os.environ.get("POSTHOG_HOST", "https://us.posthog.com").rstrip("/")
    cab = {"Authorization": f"Bearer {chave}"} if chave else {}
    sql = f"""SELECT if(event = 'article_scroll_90', properties.slug, replaceOne(properties.origem, 'materia:', '')), event, count()
              FROM events WHERE timestamp > now() - INTERVAL {int(dias)} DAY AND (event = 'article_scroll_90'
                OR (event = 'platform_cta_click' AND startsWith(properties.origem, 'materia:')))
              GROUP BY 1, 2"""
    r = requests.post(f"{host}/api/projects/{projeto}/query/", headers=cab,
                      json={"query": {"kind": "HogQLQuery", "query": sql}}, timeout=120)
    if not r.ok:
        raise RuntimeError(f"PostHog {r.status_code}: {r.text[:200]}")
    out = {}
    for slug, evento, n in r.json().get("results", []):
        out.setdefault(slug or "", {})["leituras_90" if evento == "article_scroll_90" else "cliques_app"] = n
    return out


def fotografar(md: dict) -> dict:
    """Guarda a foto do dia dos números (com a idade do post em horas), para comparar posts na mesma idade."""
    if not md.get("timestamp"):
        return md
    foto = {"d": str(AGORA.date()), "h": round((AGORA - quando_api(md["timestamp"])).total_seconds() / 3600, 1),
            **{k: md[k] for k in NUMEROS if isinstance(md.get(k), (int, float))}}
    md["serie"] = [f for f in md.get("serie", []) if f.get("d") != foto["d"]] + [foto]
    return md


def coletar(dias):
    """Varre a conta inteira (não só o que saiu pelo publicar.py) e guarda por id de mídia."""
    m = ler_json(METRICAS, {})
    for k in ("ig_midias", "yt_videos", "conta_ig", "seguidores"):
        m.setdefault(k, {})
    erros = {}
    hoje = str(AGORA.date())
    recente = AGORA - dt.timedelta(days=dias)

    try:
        ig = ColetorInstagram()
        # 1ª coleta: histórico inteiro (até 2 anos); depois, só a janela + o que ainda não tem número
        desde = recente if m["ig_midias"] else AGORA - dt.timedelta(days=730)
        for md in ig.midias(desde):
            antigo = m["ig_midias"].get(md["id"], {})
            info = {"timestamp": md["timestamp"], "tipo": md.get("media_product_type") or "FEED",
                    "media_type": md.get("media_type"), "permalink": md.get("permalink"),
                    "legenda": (md.get("caption") or "")[:300]}
            if not antigo.get("em") or quando_api(md["timestamp"]) >= recente:
                info |= ig.metricas(md) | {"em": AGORA.isoformat()}
            m["ig_midias"][md["id"]] = mesclar(antigo, info)
            if "em" in info:
                fotografar(m["ig_midias"][md["id"]])
        perfil = ig.conta(min(dias, 90), m["conta_ig"])
        m["seguidores"].setdefault(hoje, {})["instagram"] = perfil.get("followers_count")
    except Exception as e:
        erros["instagram"] = str(e)[:300]

    try:
        canal = ColetorYouTube().canal()
        for vid, dados in canal["videos"].items():
            m["yt_videos"][vid] = fotografar(mesclar(m["yt_videos"].get(vid, {}), {**dados, "em": AGORA.isoformat()}))
        m["seguidores"].setdefault(hoje, {})["youtube"] = canal["inscritos"]
    except Exception as e:
        erros["youtube"] = str(e)[:300]

    try:
        m["cliques_utm"] = coletar_posthog(max(dias, 90))
    except Exception as e:
        erros["posthog"] = str(e)[:300]

    try:
        m["blog_materias"] = coletar_blog(max(dias, 90), m.get("blog_materias") or {})
        try:
            for slug, nums in coletar_posthog_blog(max(dias, 90)).items():
                if slug in m["blog_materias"]:
                    m["blog_materias"][slug] |= nums
        except Exception as e:
            erros["posthog_blog"] = str(e)[:300]
    except Exception as e:
        erros["blog"] = str(e)[:300]

    try:
        m["visitas_ia"] = coletar_posthog_ia(max(dias, 90))
    except Exception as e:
        erros["posthog_ia"] = str(e)[:300]

    m.pop("posts", None)  # formato antigo (por publicação); agora tudo é por id de mídia
    m["coletado_em"] = AGORA.isoformat()
    m["erros"] = erros
    METRICAS.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    for fonte, erro in erros.items():
        print(f"! {fonte}: {erro}")
    return m


# ---------------------------------------------------------------- juntar pacotes + conta
FORMATO_IG = {"REELS": "Reels", "STORY": "Stories", ("FEED", "CAROUSEL_ALBUM"): "Carrossel",
              ("FEED", "IMAGE"): "Feed", ("FEED", "VIDEO"): "Feed (vídeo)"}


def formato_ig(md):
    return FORMATO_IG.get(md.get("tipo")) or FORMATO_IG.get((md.get("tipo"), md.get("media_type")), "Feed")


def somar(midias: list) -> dict:
    out = {}
    for md in midias:
        for k in NUMEROS:
            if isinstance(md.get(k), (int, float)):
                out[k] = out.get(k, 0) + md[k]
    if any(isinstance(md.get("ig_reels_avg_watch_time"), (int, float)) for md in midias):
        out["ig_reels_avg_watch_time"] = max(md.get("ig_reels_avg_watch_time") or 0 for md in midias)
    return out or None


def d1(md: dict) -> dict:
    """Números na primeira foto com 12 h ou mais de vida: com a coleta das 9h, é a manhã seguinte para qualquer
    post do dia anterior (10h → 23 h de vida; 19h → 14 h). Base justa para comparar posts."""
    fotos = [f for f in md.get("serie", []) if f.get("h", 0) >= 12]
    return min(fotos, key=lambda f: f["h"]) if fotos else {}


def juntar(inv, m):
    """Liga cada publicação do pacote às mídias da conta e acrescenta o que saiu por fora do publicador.

    Liga pelo id gravado no estado-publicacao.json; sem id (estado perdido, post manual), tenta pela
    primeira linha da legenda/título e pelo horário (até 6 h de diferença; Stories até 2 h)."""
    ig = m.get("ig_midias", {})
    yt = m.get("yt_videos", {})
    blog = m.get("blog_materias", {})
    usados = set()
    for p in inv["publicacoes"]:
        if p["plataforma"] == "blog":
            md = blog.get(p["ids"][0]) if p["ids"] else None
            if md:
                usados.add(p["ids"][0])
                p |= met_blog(md)
                p["links"] = p["links"] or [md["link"]]
                if p["status"] in ("sem-registro", "fila", "erro", "invalido", "pausado"):
                    p["status"] = "publicado"  # está no ar (publicada pelo painel ou numa rodada sem estado)
            continue
        if p["plataforma"] not in ("instagram", "youtube"):
            continue
        fonte = ig if p["plataforma"] == "instagram" else yt
        ids = [i for i in p["ids"] if i in fonte]
        if not ids and p["status"] not in ("bloqueado", "revisao", "producao"):
            q = dt.datetime.fromisoformat(p["quando"])
            for i, md in fonte.items():
                if i in usados:
                    continue
                perto = abs(quando_api(md["timestamp"]) - q) <= dt.timedelta(hours=2 if p["formato"] == "Stories" else 6)
                if p["plataforma"] == "instagram":
                    mesmo = formato_ig(md) == p["formato"] and (
                        p["formato"] == "Stories" or (p["assinatura"] and
                                                      normalizar(md.get("legenda", "")).startswith(p["assinatura"])))
                else:
                    mesmo = bool(p["assinatura"]) and normalizar(md.get("titulo", "")).startswith(p["assinatura"])
                if perto and mesmo:
                    ids.append(i)
            if ids:
                p["conciliado"] = True
        usados.update(ids)
        if ids:
            midias = [fonte[i] for i in ids]
            p["ids"] = ids
            p["met"] = somar(midias)
            p["met_d1"] = somar([d1(md) for md in midias])
            p["publicado_em"] = min(quando_api(md["timestamp"]) for md in midias).isoformat()
            p["links"] = p["links"] or list(dict.fromkeys(md.get("permalink") or md.get("link") for md in midias if
                                                          md.get("permalink") or md.get("link")))
            if p["status"] in ("sem-registro", "fila", "erro", "perdido", "invalido", "pausado"):
                agendado = p["plataforma"] == "youtube" and any(md.get("privacidade") == "private" and md.get("agendado")
                                                                 and quando_api(md["timestamp"]) > AGORA for md in midias)
                p["status"] = "agendado" if agendado else "publicado"

    # o que está na conta e não veio de nenhum pacote: Stories agrupados por dia, o resto um por um
    grupos = {}
    for i, md in ig.items():
        if i in usados:
            continue
        q = quando_api(md["timestamp"])
        chave = f"ig/stories/{q.date()}" if md.get("tipo") == "STORY" else f"ig/{i}"
        grupos.setdefault(chave, ("instagram", []))[1].append((i, md))
    for i, md in yt.items():
        if i not in usados:
            grupos[f"yt/{i}"] = ("youtube", [(i, md)])
    for slug, md in blog.items():
        if slug in usados:
            continue
        q = quando_api(md["timestamp"]).astimezone(TZ)
        inv["publicacoes"].append({
            "chave": f"blog/{slug}", "data": str(q.date()), "peca": "", "mae": "", "titulo": md["titulo"][:140],
            "plataforma": "blog", "formato": "Matéria", "quando": q.isoformat(),
            "status": "agendado" if q > AGORA else "publicado", "motivo": "", "links": [md["link"]], "ids": [slug],
            "externa": True, "pilar": "", "pilar_n": 0, "humor": "", "job": "", "funil": "", "cta": "",
            "recorrente": "", "categoria": md.get("categoria", ""), "series": "", "campanha": "", "assinatura": slug,
            "experimento": "", **met_blog(md),
        })
    for chave, (plat, itens) in grupos.items():
        itens.sort(key=lambda x: x[1]["timestamp"])
        i0, md0 = itens[0]
        q = quando_api(md0["timestamp"])
        if plat == "instagram":
            formato = formato_ig(md0)
            titulo = (md0.get("legenda") or "").split("\n")[0].strip() or f"{formato} de {q:%d/%m}"
            if formato == "Stories":
                titulo = f"Stories de {q:%d/%m} ({len(itens)} {'tela' if len(itens) == 1 else 'telas'})"
            status = "publicado"
        else:
            formato, titulo = md0["formato"], md0.get("titulo", "")
            status = ("agendado" if md0.get("agendado") and q > AGORA else
                      "publicado" if md0.get("privacidade") == "public" else "privado")
        inv["publicacoes"].append({
            "chave": chave, "data": str(q.date()), "peca": "", "mae": "", "titulo": titulo[:140], "plataforma": plat,
            "formato": formato, "quando": q.isoformat(), "status": status, "motivo": "",
            "links": [md.get("permalink") or md.get("link") for _, md in itens if md.get("permalink") or md.get("link")][:1],
            "ids": [i for i, _ in itens], "met": somar([md for _, md in itens]), "externa": True,
            "met_d1": somar([d1(md) for _, md in itens]), "publicado_em": q.isoformat(),
            "pilar": "", "pilar_n": 0, "humor": "", "job": "", "funil": "", "cta": "", "recorrente": "", "series": "",
            "campanha": "", "assinatura": "", "experimento": "",
        })
    return inv


def met_blog(md: dict) -> dict:
    """Números de uma matéria no formato das outras publicações (met = atual, met_d7 = dias 0 a 6)."""
    met = {k: md[k] for k in ("views", "leituras_90", "cliques_app") if isinstance(md.get(k), (int, float))}
    return {"met": met or None, "met_d7": {"views": md["views_d7"]} if "views_d7" in md else None,
            "publicado_em": quando_api(md["timestamp"]).isoformat()}


# ---------------------------------------------------------------- nuvem
def baixar_da_nuvem():
    """Traz só os textos (pauta, revisão, estado, logs, PAUSAR) de todos os dias + métricas guardadas."""
    r = requests.post(f"{nuvem.base()}/object/list/{nuvem.B_PACOTE}", headers=nuvem.cabecalhos(),
                      json={"prefix": "", "limit": 1000, "offset": 0}, timeout=60)
    r.raise_for_status()
    datas = sorted(i["name"] for i in r.json() if DATA_RE.fullmatch(i["name"]))
    for d in datas:
        for remoto in nuvem.listar(nuvem.B_PACOTE, d):
            p = pathlib.Path(remoto)
            if p.suffix.lower() in nuvem.TEXTO or p.name == "PAUSAR":
                nuvem.baixar(nuvem.B_PACOTE, remoto, SAIDA / remoto)
    nuvem.baixar(nuvem.B_PACOTE, "painel/metricas.json", METRICAS)
    print(f"= nuvem: textos de {len(datas)} dias")


# ---------------------------------------------------------------- HTML
def gerar_html(inv, metricas):
    modelo = (PAINEL / "modelo.html").read_text(encoding="utf-8")
    fonte = RAIZ / "motor" / "fontes" / "inter-latin-opsz-normal.woff2"
    fonte_b64 = base64.b64encode(fonte.read_bytes()).decode() if fonte.exists() else ""
    dados = {"gerado_em": AGORA.isoformat(), **inv, "metricas": metricas,
             "metas_pilar": {"1": 40, "2": 20, "3": 15, "4": 15, "5": 10}}
    js = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    corpo = modelo.replace("/*__DADOS__*/null", js).replace("__FONTE_B64__", fonte_b64)
    destino = PAINEL / "index.html"
    destino.write_text('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8">'
                       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                       f"</head><body>\n{corpo}\n</body></html>\n", encoding="utf-8")
    # mesma página sem o esqueleto <html>/<head>, no formato que a publicação como artefato do claude.ai espera
    (PAINEL / "artefato.html").write_text(corpo + "\n", encoding="utf-8")
    return destino


def main():
    nuvem.carregar_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--metricas", action="store_true", help="busca métricas novas nas redes e no PostHog")
    ap.add_argument("--dias", type=int, default=30, help="janela de coleta de métricas (padrão 30)")
    a = ap.parse_args()

    na_nuvem = nuvem.em_nuvem() and bool(os.environ.get("SUPABASE_URL"))
    if na_nuvem:
        baixar_da_nuvem()
        if a.metricas:
            nuvem.baixar_credenciais()
    inv = inventario()
    metricas = coletar(a.dias) if a.metricas else ler_json(METRICAS, {})
    inv = juntar(inv, metricas)
    if na_nuvem and a.metricas:
        nuvem.subir(nuvem.B_PACOTE, METRICAS, "painel/metricas.json")
        nuvem.subir_credenciais()  # o token do YouTube pode ter sido renovado
    destino = gerar_html(inv, metricas)
    print(f"✓ {destino.relative_to(RAIZ)}: {len(inv['publicacoes'])} publicações, {len(inv['rascunhos'])} rascunhos, "
          f"{len(inv['ideias'])} ideias, {sum(1 for p in inv['publicacoes'] if p.get('met'))} com métricas "
          f"({sum(1 for p in inv['publicacoes'] if p.get('externa'))} fora dos pacotes)")


if __name__ == "__main__":
    main()
