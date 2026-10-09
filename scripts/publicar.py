#!/usr/bin/env python3
"""Publica no Instagram e no YouTube as peças aprovadas do pacote diário.

Uso:
  python scripts/publicar.py --vencidos            # hoje e ontem (é o que a rotina horária chama)
  python scripts/publicar.py --data 2026-10-10
  python scripts/publicar.py --vencidos --simular  # valida tudo e mostra o que faria, sem publicar

Travas de segurança:
  - Só publica de verdade com PUBLICACAO_AUTOMATICA=true no .env; caso contrário, simula.
  - Pula o dia inteiro se existir o arquivo saida/<data>/PAUSAR.
  - Só publica peças listadas em "aprovadas" de saida/<data>/revisao.json (escrito pelo revisor).
  - Cada publicação acontece uma única vez (estado em <peça>/estado-publicacao.json).
  - Instagram: publica quando chega o horário; se atrasar mais que MAX_ATRASO_HORAS, marca como perdida.
  - YouTube: sobe assim que aprovado e agenda pelo publishAt do próprio YouTube.

Contrato de cada peça: <peça>/publicar.json
{
  "publicacoes": [
    {"id": "ig-reel", "plataforma": "instagram", "tipo": "REELS", "arquivos": ["video.mp4"],
     "legenda": "...", "quando": "2026-10-10T19:00:00-03:00", "capa": "capa.jpg"},
    {"id": "ig-carrossel", "plataforma": "instagram", "tipo": "CAROUSEL", "arquivos": ["cards/01.jpg", "..."],
     "legenda": "...", "quando": "..."},
    {"id": "ig-stories", "plataforma": "instagram", "tipo": "STORIES", "arquivos": ["stories/01.jpg"], "quando": "..."},
    {"id": "yt-short", "plataforma": "youtube", "tipo": "short", "arquivos": ["video.mp4"],
     "titulo": "...", "descricao": "...", "tags": ["..."], "quando": "...", "thumbnail": null, "playlist_id": null}
  ]
}
"""
import argparse
import datetime as dt
import json
import mimetypes
import os
import pathlib
import subprocess
import sys
import time
import uuid
from zoneinfo import ZoneInfo

import requests

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "saida"
CRED = RAIZ / ".credenciais"
TZ = ZoneInfo("America/Sao_Paulo")
AGORA = dt.datetime.now(TZ)


# ---------------------------------------------------------------- utilidades
def carregar_env():
    env = RAIZ / ".env"
    if env.exists():
        for linha in env.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def cfg(nome, padrao=None):
    return os.environ.get(nome, padrao)


def quando(pub) -> dt.datetime:
    q = dt.datetime.fromisoformat(pub["quando"])
    return q if q.tzinfo else q.replace(tzinfo=TZ)


def ler_json(p: pathlib.Path, padrao):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else padrao


def salvar_json(p: pathlib.Path, dados):
    p.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def log(pasta_dia: pathlib.Path, texto: str):
    print(texto)
    with (pasta_dia / "publicacao.log.md").open("a", encoding="utf-8") as f:
        f.write(f"- {dt.datetime.now(TZ):%H:%M} {texto}\n")


def ffprobe(arquivo):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height:format=duration",
                        "-of", "json", str(arquivo)], capture_output=True, text=True)
    return json.loads(r.stdout or "{}")


# ---------------------------------------------------------------- validação
def validar(pub, pasta) -> list:
    erros = []
    arquivos = [pasta / a for a in pub.get("arquivos", [])]
    if not arquivos:
        erros.append("sem arquivos")
    for a in arquivos:
        if not a.exists() or a.stat().st_size == 0:
            erros.append(f"arquivo ausente: {a.name}")
    if "quando" not in pub:
        erros.append("sem 'quando'")
    if pub["plataforma"] == "instagram":
        tipo = pub.get("tipo")
        if tipo not in {"REELS", "IMAGE", "CAROUSEL", "STORIES"}:
            erros.append(f"tipo inválido: {tipo}")
        legenda = pub.get("legenda", "")
        if len(legenda) > 2200:
            erros.append("legenda > 2200 caracteres")
        if legenda.count("#") > 30:
            erros.append("mais de 30 hashtags")
        if tipo == "CAROUSEL" and not 2 <= len(arquivos) <= 10:
            erros.append("carrossel precisa de 2 a 10 itens")
        for a in arquivos:
            if a.suffix.lower() in {".png", ".webp"}:
                erros.append(f"Instagram só aceita imagem JPEG: {a.name}")
        if tipo == "REELS" and arquivos and arquivos[0].exists():
            info = ffprobe(arquivos[0])
            v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
            if v and v.get("width", 0) > v.get("height", 0):
                erros.append("Reels precisa ser vertical")
    elif pub["plataforma"] == "youtube":
        if not pub.get("titulo") or len(pub["titulo"]) > 100:
            erros.append("título vazio ou > 100 caracteres")
        if len(pub.get("descricao", "")) > 5000:
            erros.append("descrição > 5000 caracteres")
        if any(c in pub.get("titulo", "") + pub.get("descricao", "") for c in "<>"):
            erros.append("YouTube não aceita < ou > no título/descrição")
    else:
        erros.append(f"plataforma desconhecida: {pub['plataforma']}")
    return erros


# ---------------------------------------------------------------- hospedagem temporária (Supabase Storage)
class Hospedagem:
    def __init__(self):
        self.url = cfg("SUPABASE_URL", "").rstrip("/")
        self.chave = cfg("SUPABASE_SERVICE_ROLE_KEY")
        self.bucket = cfg("SUPABASE_BUCKET", "conteudo-redes")
        if not self.url:
            raise RuntimeError("Defina SUPABASE_URL no .env")
        # Sem chave no ambiente: confia na "API credential" da nuvem, que anexa o cabeçalho pelo proxy.
        if not self.chave:
            self.h = {}
        elif self.chave.startswith("sb_"):  # chave nova do Supabase: só no apikey
            self.h = {"apikey": self.chave}
        else:  # chave legada (JWT)
            self.h = {"Authorization": f"Bearer {self.chave}", "apikey": self.chave}
        self.enviados = []

    def subir(self, arquivo: pathlib.Path) -> str:
        caminho = f"{AGORA:%Y-%m-%d}/{uuid.uuid4().hex}/{arquivo.name}"
        tipo = mimetypes.guess_type(arquivo.name)[0] or "application/octet-stream"
        with arquivo.open("rb") as f:
            r = requests.post(f"{self.url}/storage/v1/object/{self.bucket}/{caminho}",
                              headers={**self.h, "Content-Type": tipo, "x-upsert": "true"}, data=f, timeout=600)
        if r.status_code not in (200, 201):
            raise RuntimeError(f"Supabase upload {r.status_code}: {r.text[:200]}")
        self.enviados.append(caminho)
        return f"{self.url}/storage/v1/object/public/{self.bucket}/{caminho}"

    def limpar(self):
        if self.enviados:
            requests.delete(f"{self.url}/storage/v1/object/{self.bucket}", headers=self.h,
                            json={"prefixes": self.enviados}, timeout=60)
            self.enviados = []


# ---------------------------------------------------------------- Instagram (API com login do Instagram)
class Instagram:
    def __init__(self):
        self.arq = CRED / "instagram.json"
        if not self.arq.exists():
            raise RuntimeError("Rode scripts/configurar_instagram.py primeiro")
        self.c = ler_json(self.arq, {})
        self.base = f"https://graph.instagram.com/{cfg('INSTAGRAM_API_VERSION', 'v25.0')}"
        self.ia = cfg("MARCAR_CONTEUDO_IA", "true").lower() == "true"
        self.renovar_token()

    def renovar_token(self):
        expira = dt.datetime.fromisoformat(self.c["expira_em"])
        if expira - AGORA > dt.timedelta(days=15):
            return
        r = requests.get("https://graph.instagram.com/refresh_access_token",
                         params={"grant_type": "ig_refresh_token", "access_token": self.c["access_token"]}, timeout=30)
        if r.ok:
            d = r.json()
            self.c["access_token"] = d["access_token"]
            self.c["expira_em"] = (AGORA + dt.timedelta(seconds=d.get("expires_in", 5_184_000))).isoformat()
            salvar_json(self.arq, self.c)
        else:
            print(f"! não renovei o token do Instagram ({r.status_code}). Expira em {expira:%d/%m}.")

    def _post(self, caminho, dados):
        r = requests.post(f"{self.base}/{caminho}", data={**dados, "access_token": self.c["access_token"]}, timeout=120)
        if not r.ok:
            raise RuntimeError(f"Instagram {r.status_code}: {r.text[:300]}")
        return r.json()

    def _get(self, caminho, campos):
        r = requests.get(f"{self.base}/{caminho}", params={"fields": campos, "access_token": self.c["access_token"]},
                         timeout=60)
        r.raise_for_status()
        return r.json()

    def _esperar(self, container):
        for _ in range(40):  # até ~10 min
            status = self._get(container, "status_code").get("status_code")
            if status == "FINISHED":
                return
            if status in ("ERROR", "EXPIRED"):
                raise RuntimeError(f"container {container} terminou com {status}")
            time.sleep(15)
        raise RuntimeError(f"container {container} não ficou pronto a tempo")

    def _container(self, url, eh_video, extra):
        dados = {**extra, ("video_url" if eh_video else "image_url"): url}
        cid = self._post(f"{self.c['ig_user_id']}/media", dados)["id"]
        self._esperar(cid)
        return cid

    def _publicar(self, cid):
        mid = self._post(f"{self.c['ig_user_id']}/media_publish", {"creation_id": cid})["id"]
        return mid, self._get(mid, "permalink").get("permalink", "")

    def publicar(self, pub, pasta, host: Hospedagem):
        arquivos = [pasta / a for a in pub["arquivos"]]
        video = lambda a: a.suffix.lower() in {".mp4", ".mov"}
        ia = {"is_ai_generated": "true"} if self.ia else {}
        tipo, legenda = pub["tipo"], pub.get("legenda", "")
        resultados = []
        try:
            if tipo == "REELS":
                extra = {"media_type": "REELS", "caption": legenda, "share_to_feed": "true", **ia}
                if pub.get("capa") and (pasta / pub["capa"]).exists():
                    extra["cover_url"] = host.subir(pasta / pub["capa"])
                resultados.append(self._publicar(self._container(host.subir(arquivos[0]), True, extra)))
            elif tipo == "IMAGE":
                resultados.append(self._publicar(self._container(host.subir(arquivos[0]), False,
                                                                 {"caption": legenda, **ia})))
            elif tipo == "CAROUSEL":
                filhos = []
                for a in arquivos:
                    extra = {"is_carousel_item": "true", **({"media_type": "VIDEO"} if video(a) else {})}
                    filhos.append(self._container(host.subir(a), video(a), extra))
                pai = self._post(f"{self.c['ig_user_id']}/media",
                                 {"media_type": "CAROUSEL", "children": ",".join(filhos), "caption": legenda, **ia})["id"]
                self._esperar(pai)
                resultados.append(self._publicar(pai))
            elif tipo == "STORIES":
                for a in arquivos:  # uma tela por vez, na ordem
                    resultados.append(self._publicar(self._container(host.subir(a), video(a),
                                                                     {"media_type": "STORIES"})))
        finally:
            host.limpar()
        return {"ids": [r[0] for r in resultados], "links": [r[1] for r in resultados if r[1]]}


# ---------------------------------------------------------------- YouTube
class YouTube:
    ESCOPOS = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]

    def __init__(self):
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        token = CRED / "youtube-token.json"
        if not token.exists():
            raise RuntimeError("Rode scripts/autorizar_youtube.py primeiro")
        cred = Credentials.from_authorized_user_file(str(token), self.ESCOPOS)
        if not cred.valid:
            cred.refresh(Request())
            token.write_text(cred.to_json(), encoding="utf-8")
        self.yt = build("youtube", "v3", credentials=cred, cache_discovery=False)

    def publicar(self, pub, pasta, _host=None):
        from googleapiclient.http import MediaFileUpload
        titulo = pub["titulo"]
        descricao = pub.get("descricao", "")
        if pub.get("tipo") == "short" and "#shorts" not in (titulo + descricao).lower():
            descricao = (descricao + "\n\n#Shorts").strip()
        quando_pub = quando(pub)
        status = {"selfDeclaredMadeForKids": False,
                  "containsSyntheticMedia": cfg("MARCAR_CONTEUDO_IA", "true").lower() == "true"}
        if quando_pub > AGORA + dt.timedelta(minutes=15):
            status |= {"privacyStatus": "private",
                       "publishAt": quando_pub.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        else:
            status["privacyStatus"] = "public"
        corpo = {"snippet": {"title": titulo, "description": descricao, "tags": pub.get("tags", []),
                             "categoryId": pub.get("categoria", "24"),  # 24 = Entretenimento
                             "defaultLanguage": "pt-BR", "defaultAudioLanguage": "pt-BR"},
                 "status": status}
        midia = MediaFileUpload(str(pasta / pub["arquivos"][0]), mimetype="video/mp4", chunksize=8 * 1024 * 1024,
                                resumable=True)
        req = self.yt.videos().insert(part="snippet,status", body=corpo, media_body=midia)
        resp = None
        while resp is None:
            _, resp = req.next_chunk()
        vid = resp["id"]
        if pub.get("thumbnail") and (pasta / pub["thumbnail"]).exists():
            try:
                self.yt.thumbnails().set(videoId=vid, media_body=MediaFileUpload(str(pasta / pub["thumbnail"]))).execute()
            except Exception as e:  # thumbnail personalizada exige canal verificado
                print(f"! thumbnail não aplicada: {e}")
        if pub.get("playlist_id"):
            self.yt.playlistItems().insert(part="snippet", body={"snippet": {
                "playlistId": pub["playlist_id"], "resourceId": {"kind": "youtube#video", "videoId": vid}}}).execute()
        link = f"https://youtu.be/{vid}"
        return {"ids": [vid], "links": [link], "agendado_para": status.get("publishAt")}


# ---------------------------------------------------------------- orquestração
def processar_dia(data: str, simular: bool):
    pasta_dia = SAIDA / data
    if not pasta_dia.exists():
        return
    if (pasta_dia / "PAUSAR").exists():
        print(f"{data}: PAUSAR encontrado, nada será publicado.")
        return
    revisao = ler_json(pasta_dia / "revisao.json", None)
    if revisao is None:
        print(f"{data}: sem revisao.json — o revisor ainda não aprovou nada.")
        return
    aprovadas = set(revisao.get("aprovadas", []))
    max_atraso = dt.timedelta(hours=float(cfg("MAX_ATRASO_HORAS", "4")))
    clientes, host = {}, None

    for pasta in sorted(p for p in pasta_dia.iterdir() if p.is_dir() and p.name in aprovadas):
        plano = ler_json(pasta / "publicar.json", None)
        if not plano:
            continue
        estado_arq = pasta / "estado-publicacao.json"
        estado = ler_json(estado_arq, {})
        for pub in plano.get("publicacoes", []):
            chave = pub["id"]
            atual = estado.get(chave, {})
            if atual.get("status") in ("publicado", "agendado", "perdido", "invalido"):
                continue
            if atual.get("tentativas", 0) >= (1 if pub["plataforma"] == "youtube" else 2):
                continue  # não insiste: evita post duplicado
            q = quando(pub)
            if pub["plataforma"] == "instagram":
                if q > AGORA:
                    continue
                if AGORA - q > max_atraso:
                    msg = f"⏭ {pasta.name}/{chave}: horário passou há mais de {max_atraso}, não publiquei"
                    if simular:
                        print(f"[simulação] {msg}")
                    else:
                        estado[chave] = {"status": "perdido", "motivo": f"atraso de {AGORA - q}"}
                        log(pasta_dia, msg)
                        salvar_json(estado_arq, estado)
                    continue
            erros = validar(pub, pasta)
            if erros:
                msg = f"✗ {pasta.name}/{chave}: {'; '.join(erros)}"
                if simular:
                    print(f"[simulação] {msg}")
                else:
                    estado[chave] = {"status": "invalido", "erros": erros}
                    log(pasta_dia, msg)
                    salvar_json(estado_arq, estado)
                continue
            if simular:
                print(f"[simulação] publicaria {pasta.name}/{chave} ({pub['plataforma']} {pub.get('tipo')}) "
                      f"para {q:%d/%m %H:%M}")
                continue
            try:
                if pub["plataforma"] not in clientes:
                    clientes[pub["plataforma"]] = Instagram() if pub["plataforma"] == "instagram" else YouTube()
                if pub["plataforma"] == "instagram" and host is None:
                    host = Hospedagem()
                res = clientes[pub["plataforma"]].publicar(pub, pasta, host)
                st = "agendado" if res.get("agendado_para") else "publicado"
                estado[chave] = {"status": st, "em": AGORA.isoformat(), **res}
                log(pasta_dia, f"✓ {pasta.name}/{chave} {st}: {' '.join(res['links'])}")
            except Exception as e:
                estado[chave] = {"status": "erro", "tentativas": atual.get("tentativas", 0) + 1, "erro": str(e)[:500]}
                log(pasta_dia, f"✗ {pasta.name}/{chave}: {str(e)[:200]}")
            salvar_json(estado_arq, estado)


def main():
    carregar_env()
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--data")
    g.add_argument("--vencidos", action="store_true")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    simular = a.simular or cfg("PUBLICACAO_AUTOMATICA", "false").lower() != "true"
    if simular and not a.simular:
        print("PUBLICACAO_AUTOMATICA não está true no .env — rodando em simulação.")
    datas = [a.data] if a.data else [(AGORA - dt.timedelta(days=1)).strftime("%Y-%m-%d"), AGORA.strftime("%Y-%m-%d")]

    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import nuvem
    na_nuvem = nuvem.em_nuvem()
    if na_nuvem:  # execução na nuvem começa vazia: traz tokens e pacotes do Supabase
        nuvem.baixar_credenciais()
        for d in datas:
            nuvem.baixar_pacote(d)
    try:
        for d in datas:
            processar_dia(d, simular)
    finally:
        if na_nuvem and not simular:  # guarda estado das publicações e token renovado
            for d in datas:
                nuvem.subir_pacote(d, so_texto=True)
            nuvem.subir_credenciais()


if __name__ == "__main__":
    main()
