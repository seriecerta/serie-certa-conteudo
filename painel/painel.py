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
  - Instagram (por post): views, alcance, curtidas, comentários, envios, salvamentos, visitas ao perfil, follows.
    Stories só têm insight nas 24 h em que estão no ar: rode --metricas nesse intervalo, o painel guarda o número.
  - Instagram (conta, por dia): cliques no link da bio (website_clicks), visitas ao perfil, alcance, seguidores.
  - YouTube: views, curtidas, comentários por vídeo e inscritos do canal.
  - Cliques nos links com UTM: PostHog (opcional; POSTHOG_API_KEY + POSTHOG_PROJECT_ID no .env).
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


def legivel(slug: str) -> str:
    return re.sub(r"^\d\d-", "", slug).replace("-", " ").capitalize()


# ---------------------------------------------------------------- pauta
CAMPOS = {"formato": "formato", "pilar": "pilar", "pilar / job": "pilar", "job": "job", "humor": "humor",
          "cta / funil": "cta", "horário": "horario", "horários": "horario"}
FUNIS = ("Descoberta", "Consideração", "Conversão", "Retenção")


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
        m = re.match(r"- \*\*([^:*]+):?\*\*:?\s*(.*)", linha)
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
            pil = re.match(r"(\d)\.\s*([^,(/]+)", p.get("pilar", ""))
            p["pilar_n"], p["pilar"] = (int(pil.group(1)), pil.group(2).strip()) if pil else (0, p.get("pilar", ""))
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
           ("youtube", "short"): "Short", ("youtube", "longo"): "Vídeo longo", ("tiktok", "video"): "TikTok"}


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
        for pasta in sorted(p for p in pasta_dia.iterdir() if p.is_dir()):
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


# ---------------------------------------------------------------- métricas
MET_IG = ["views", "reach", "likes", "comments", "shares", "saved", "total_interactions",
          "profile_visits", "follows", "replies", "ig_reels_avg_watch_time"]


def mesclar(antigo: dict, novo: dict) -> dict:
    """Nunca troca número por vazio (o insight dos Stories some depois de 24 h)."""
    return {**antigo, **{k: v for k, v in novo.items() if v is not None}}


class ColetorInstagram:
    def __init__(self):
        c = ler_json(CRED / "instagram.json", None)
        if not c:
            raise RuntimeError("sem .credenciais/instagram.json")
        self.c = c
        self.base = f"https://graph.instagram.com/{os.environ.get('INSTAGRAM_API_VERSION', 'v25.0')}"

    def get(self, caminho, **params):
        r = requests.get(f"{self.base}/{caminho}", params={**params, "access_token": self.c["access_token"]},
                         timeout=60)
        if not r.ok:
            raise RuntimeError(f"{r.status_code} {r.text[:200]}")
        return r.json()

    def insights(self, caminho, metricas, **params):
        """Pede tudo de uma vez; se a API recusar alguma métrica (varia por tipo de mídia), tenta uma por uma."""
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

    def post(self, mid):
        base = self.get(mid, fields="like_count,comments_count")
        ins = self.insights(mid, MET_IG)
        return {**ins, "likes": ins.get("likes", base.get("like_count")),
                "comments": ins.get("comments", base.get("comments_count"))}

    def conta(self, dias, cache):
        uid = self.c["ig_user_id"]
        perfil = self.get(uid, fields="followers_count,media_count")
        hoje = AGORA.date()
        for i in range(dias):
            d = hoje - dt.timedelta(days=i)
            if str(d) in cache and i > 2:
                continue  # dias fechados não mudam; os 3 últimos sempre são relidos
            ini = dt.datetime.combine(d, dt.time(), TZ)
            fim = min(ini + dt.timedelta(days=1), AGORA)
            cache[str(d)] = mesclar(cache.get(str(d), {}), self.insights(
                uid, ["website_clicks", "profile_views", "reach", "accounts_engaged", "views"], period="day",
                metric_type="total_value", since=int(ini.timestamp()), until=int(fim.timestamp())))
        return perfil


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

    def videos(self, ids):
        out = {}
        for i in range(0, len(ids), 50):
            r = self.yt.videos().list(part="statistics", id=",".join(ids[i:i + 50])).execute()
            for v in r.get("items", []):
                s = v.get("statistics", {})
                out[v["id"]] = {"views": int(s.get("viewCount", 0)), "likes": int(s.get("likeCount", 0)),
                                "comments": int(s.get("commentCount", 0))}
        return out

    def inscritos(self):
        r = self.yt.channels().list(part="statistics", mine=True).execute()
        return int((r.get("items") or [{}])[0].get("statistics", {}).get("subscriberCount", 0))


def coletar_posthog(dias):
    chave, projeto = os.environ.get("POSTHOG_API_KEY"), os.environ.get("POSTHOG_PROJECT_ID")
    if not (chave and projeto):
        raise RuntimeError("POSTHOG_API_KEY e POSTHOG_PROJECT_ID não definidos (opcional)")
    host = os.environ.get("POSTHOG_HOST", "https://us.posthog.com").rstrip("/")
    sql = f"""SELECT properties.utm_source, properties.utm_medium, properties.utm_campaign, toDate(timestamp),
                     count(), count(DISTINCT person_id)
              FROM events WHERE event = '$pageview' AND properties.utm_medium IN ('organico', 'stories')
                AND timestamp > now() - INTERVAL {int(dias)} DAY
              GROUP BY 1, 2, 3, 4 ORDER BY 4"""
    r = requests.post(f"{host}/api/projects/{projeto}/query/", headers={"Authorization": f"Bearer {chave}"},
                      json={"query": {"kind": "HogQLQuery", "query": sql}}, timeout=120)
    if not r.ok:
        raise RuntimeError(f"PostHog {r.status_code}: {r.text[:200]}")
    return [{"origem": a or "", "meio": b or "", "campanha": c or "", "dia": str(d), "cliques": n, "pessoas": u}
            for a, b, c, d, n, u in r.json().get("results", [])]


def coletar(inv, dias):
    m = ler_json(METRICAS, {})
    for k in ("posts", "conta_ig", "seguidores"):
        m.setdefault(k, {})
    erros = {}
    pubs = [p for p in inv["publicacoes"] if p["ids"] and p["status"] == "publicado"]
    limite = (AGORA - dt.timedelta(days=dias)).isoformat()
    hoje = str(AGORA.date())

    try:
        ig = ColetorInstagram()
        for p in (p for p in pubs if p["plataforma"] == "instagram" and p["quando"] >= limite):
            soma = {}
            for mid in p["ids"]:  # Stories têm um id por tela: soma as telas
                for k, v in ig.post(mid).items():
                    if isinstance(v, (int, float)):
                        soma[k] = soma.get(k, 0) + v
            m["posts"][p["chave"]] = mesclar(m["posts"].get(p["chave"], {}), {**soma, "em": AGORA.isoformat()})
        perfil = ig.conta(min(dias, 90), m["conta_ig"])
        m["seguidores"].setdefault(hoje, {})["instagram"] = perfil.get("followers_count")
    except Exception as e:
        erros["instagram"] = str(e)[:300]

    try:
        yt = ColetorYouTube()
        ids = {i: p["chave"] for p in pubs if p["plataforma"] == "youtube" for i in p["ids"]}
        for vid, dados in yt.videos(list(ids)).items():
            m["posts"][ids[vid]] = mesclar(m["posts"].get(ids[vid], {}), {**dados, "em": AGORA.isoformat()})
        m["seguidores"].setdefault(hoje, {})["youtube"] = yt.inscritos()
    except Exception as e:
        erros["youtube"] = str(e)[:300]

    try:
        m["cliques_utm"] = coletar_posthog(dias)
    except Exception as e:
        erros["posthog"] = str(e)[:300]

    m["coletado_em"] = AGORA.isoformat()
    m["erros"] = erros
    METRICAS.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    for fonte, erro in erros.items():
        print(f"! {fonte}: {erro}")
    return m


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
    metricas = coletar(inv, a.dias) if a.metricas else ler_json(METRICAS, {})
    if na_nuvem and a.metricas:
        nuvem.subir(nuvem.B_PACOTE, METRICAS, "painel/metricas.json")
        nuvem.subir_credenciais()  # o token do YouTube pode ter sido renovado
    destino = gerar_html(inv, metricas)
    print(f"✓ {destino.relative_to(RAIZ)}: {len(inv['publicacoes'])} publicações, {len(inv['rascunhos'])} rascunhos, "
          f"{len(inv['ideias'])} ideias, métricas de {len(metricas.get('posts', {}))} posts")


if __name__ == "__main__":
    main()
