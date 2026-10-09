#!/usr/bin/env python3
"""Gera o token do Instagram pedindo explicitamente a permissão de publicar.

Use quando o painel da Meta não mostra instagram_business_content_publish na lista.

Uso: python scripts/gerar_token_instagram.py

Você vai precisar (painel do app → Instagram → Configuração da API com login do Instagram):
  - "ID do app do Instagram" e "Chave secreta do app do Instagram"
    (são diferentes do ID do app do Facebook mostrado no topo do painel)
  - Em "Configurar login do Instagram para empresas", cadastre a URL de redirecionamento:
    https://seriecerta.online/
"""
import datetime as dt
import json
import pathlib
import sys
import urllib.parse
from getpass import getpass
from zoneinfo import ZoneInfo

import requests

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TZ = ZoneInfo("America/Sao_Paulo")
REDIRECT = "https://seriecerta.online/"
ESCOPOS = "instagram_business_basic,instagram_business_content_publish"

app_id = input("ID do app do Instagram: ").strip()
segredo = getpass("Chave secreta do app do Instagram (não aparece ao digitar): ").strip()

url = "https://www.instagram.com/oauth/authorize?" + urllib.parse.urlencode({
    "client_id": app_id, "redirect_uri": REDIRECT, "response_type": "code",
    "scope": ESCOPOS, "force_reauth": "true"})
print("\n1) Abra este link no navegador, entre com o @seriecerta e autorize:\n")
print(url)
print("\n2) Você vai cair no site do Série Certa. Copie o endereço COMPLETO da barra do navegador "
      "(começa com https://seriecerta.online/?code=...)\n")
voltou = input("Cole aqui o endereço: ").strip()
codigo = urllib.parse.parse_qs(urllib.parse.urlparse(voltou).query).get("code", [""])[0].split("#")[0]
if not codigo:
    sys.exit("Não achei o ?code= no endereço colado.")

curto = requests.post("https://api.instagram.com/oauth/access_token", data={
    "client_id": app_id, "client_secret": segredo, "grant_type": "authorization_code",
    "redirect_uri": REDIRECT, "code": codigo}, timeout=30)
if not curto.ok:
    sys.exit(f"Falha ao trocar o código: {curto.text[:300]}")
dados = curto.json()
dados = dados.get("data", [dados])[0] if "data" in dados else dados
permissoes = dados.get("permissions", "")
if "instagram_business_content_publish" not in str(permissoes):
    sys.exit(f"A permissão de publicar não veio. Permissões concedidas: {permissoes}")

longo = requests.get("https://graph.instagram.com/access_token", params={
    "grant_type": "ig_exchange_token", "client_secret": segredo, "access_token": dados["access_token"]},
    timeout=30)
if not longo.ok:
    sys.exit(f"Falha ao gerar token de longa duração: {longo.text[:300]}")
token = longo.json()["access_token"]
expira = dt.datetime.now(TZ) + dt.timedelta(seconds=longo.json().get("expires_in", 5_184_000))

me = requests.get("https://graph.instagram.com/me", params={"fields": "user_id,username",
                                                            "access_token": token}, timeout=30).json()
cred = RAIZ / ".credenciais"
cred.mkdir(exist_ok=True)
(cred / "instagram.json").write_text(json.dumps({
    "ig_user_id": me["user_id"], "username": me.get("username"),
    "access_token": token, "expira_em": expira.isoformat()}, indent=2), encoding="utf-8")
print(f"\nOK: @{me.get('username')} configurado com permissão de publicar. Token até {expira:%d/%m/%Y}.")
