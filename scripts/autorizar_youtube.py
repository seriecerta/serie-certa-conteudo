#!/usr/bin/env python3
"""Autoriza o YouTube uma única vez.

Antes: o JSON do cliente OAuth ("App para computador") precisa estar em .credenciais/youtube-client.json
(no modo nuvem, suba esse arquivo no bucket privado credenciais-redes pelo painel do Supabase).

No computador (abre o navegador sozinho):
  python scripts/autorizar_youtube.py

Na nuvem (Claude Code web), em duas etapas:
  python scripts/autorizar_youtube.py --link
      -> mostra um link; abra, autorize; o navegador vai para http://localhost/... e dá erro de conexão.
         Isso é esperado: copie o endereço inteiro da barra.
  python scripts/autorizar_youtube.py --concluir "http://localhost/?state=...&code=..."
"""
import json
import os
import pathlib
import sys

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CRED = RAIZ / ".credenciais"
CLIENTE = CRED / "youtube-client.json"
PENDENTE = CRED / "_oauth_pendente.json"
TOKEN = CRED / "youtube-token.json"
ESCOPOS = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]
REDIRECT = "http://localhost"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import nuvem  # noqa: E402

nuvem.carregar_env()
if nuvem.em_nuvem():
    nuvem.baixar_credenciais()
if not CLIENTE.exists():
    sys.exit(f"Falta {CLIENTE.name}: baixe do Google Cloud (Credenciais) e coloque em .credenciais/ "
             "ou, na nuvem, no bucket credenciais-redes do Supabase.")


def concluir(cred):
    TOKEN.write_text(cred.to_json(), encoding="utf-8")
    PENDENTE.unlink(missing_ok=True)
    canal = build("youtube", "v3", credentials=cred, cache_discovery=False).channels().list(
        part="snippet", mine=True).execute()
    nome = canal["items"][0]["snippet"]["title"] if canal.get("items") else "?"
    if nuvem.em_nuvem():
        nuvem.subir_credenciais()
    print(f"OK: autorizado no canal '{nome}'.")


args = sys.argv[1:]
if not args:
    concluir(InstalledAppFlow.from_client_secrets_file(str(CLIENTE), ESCOPOS).run_local_server(port=0))
elif args[0] == "--link":
    flow = Flow.from_client_secrets_file(str(CLIENTE), ESCOPOS, redirect_uri=REDIRECT,
                                         autogenerate_code_verifier=True)
    url, state = flow.authorization_url(access_type="offline", prompt="consent")
    PENDENTE.write_text(json.dumps({"state": state, "code_verifier": flow.code_verifier}), encoding="utf-8")
    if nuvem.em_nuvem():
        nuvem.subir_credenciais()
    print("Abra este link, entre com a conta do canal e autorize:\n")
    print(url)
    print("\nO navegador vai cair numa página de erro em http://localhost — copie o endereço inteiro da barra "
          "e rode:  python scripts/autorizar_youtube.py --concluir \"ENDEREÇO\"")
elif args[0] == "--concluir" and len(args) == 2:
    if not PENDENTE.exists():
        sys.exit("Rode primeiro com --link.")
    p = json.loads(PENDENTE.read_text(encoding="utf-8"))
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # o retorno é http://localhost, sem servidor real
    flow = Flow.from_client_secrets_file(str(CLIENTE), ESCOPOS, redirect_uri=REDIRECT, state=p["state"])
    flow.code_verifier = p["code_verifier"]
    flow.fetch_token(authorization_response=args[1])
    concluir(flow.credentials)
else:
    sys.exit(__doc__)
