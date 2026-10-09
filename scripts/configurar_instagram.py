#!/usr/bin/env python3
"""Configura o Instagram uma única vez.

Uso: python scripts/configurar_instagram.py <TOKEN_DE_LONGA_DURACAO>

O token sai do painel do app na Meta (API do Instagram com login do Instagram →
"Gerar token" para a conta @seriecerta). Salva em .credenciais/instagram.json.
"""
import datetime as dt
import json
import pathlib
import sys
from zoneinfo import ZoneInfo

import requests

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TZ = ZoneInfo("America/Sao_Paulo")

if len(sys.argv) != 2:
    sys.exit(__doc__)
token = sys.argv[1].strip()

r = requests.get("https://graph.instagram.com/me", params={"fields": "user_id,username,account_type",
                                                           "access_token": token}, timeout=30)
if not r.ok:
    sys.exit(f"Token recusado: {r.text[:300]}")
me = r.json()

expira = dt.datetime.now(TZ) + dt.timedelta(days=60)
ref = requests.get("https://graph.instagram.com/refresh_access_token",
                   params={"grant_type": "ig_refresh_token", "access_token": token}, timeout=30)
if ref.ok:  # token com mais de 24 h já pode ser renovado
    token = ref.json()["access_token"]
    expira = dt.datetime.now(TZ) + dt.timedelta(seconds=ref.json().get("expires_in", 5_184_000))

cred = RAIZ / ".credenciais"
cred.mkdir(exist_ok=True)
(cred / "instagram.json").write_text(json.dumps({
    "ig_user_id": me["user_id"], "username": me.get("username"),
    "access_token": token, "expira_em": expira.isoformat()}, indent=2), encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import nuvem  # noqa: E402

nuvem.carregar_env()
if nuvem.em_nuvem():
    nuvem.subir_credenciais()  # guarda no bucket privado para as próximas execuções
print(f"OK: @{me.get('username')} ({me.get('account_type')}), token válido até {expira:%d/%m/%Y}. "
      "O publicador renova sozinho antes de vencer.")
