#!/usr/bin/env python3
"""Guarda e recupera, no Supabase Storage privado, o que precisa sobreviver entre execuções na nuvem.

No Claude Code web cada execução começa do zero (clone novo do GitHub). Por isso:
  - tokens (.credenciais/)           -> bucket privado credenciais-redes
  - pacote do dia (saida/<data>/)    -> bucket privado pacotes-redes/<data>/
    (vídeos, áudios, cards, publicar.json, revisao.json, estado-publicacao.json, logs)

Uso:
  python scripts/nuvem.py baixar-credenciais
  python scripts/nuvem.py subir-credenciais
  python scripts/nuvem.py baixar-pacote 2026-10-10
  python scripts/nuvem.py subir-pacote 2026-10-10            # tudo
  python scripts/nuvem.py subir-pacote 2026-10-10 --so-texto # só .json/.md/.txt (rápido; usado de hora em hora)

Autenticação: usa SUPABASE_SERVICE_ROLE_KEY do ambiente. Se ela não estiver definida, não envia
cabeçalho de autenticação, para funcionar com uma "API credential" do ambiente de nuvem (o proxy anexa).
"""
import mimetypes
import os
import pathlib
import sys
import urllib.parse

import requests

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CRED = RAIZ / ".credenciais"
SAIDA = RAIZ / "saida"
B_CRED = "credenciais-redes"
B_PACOTE = "pacotes-redes"
TEXTO = {".json", ".md", ".txt"}


def carregar_env():
    env = RAIZ / ".env"
    if env.exists():
        for linha in env.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def em_nuvem() -> bool:
    return os.environ.get("CLAUDE_CODE_REMOTE") == "true" or os.environ.get("MODO_NUVEM") == "true"


def base():
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    if not url:
        sys.exit("Defina SUPABASE_URL")
    return f"{url}/storage/v1"


def cabecalhos(extra=None):
    h = dict(extra or {})
    chave = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if chave:
        h |= {"Authorization": f"Bearer {chave}", "apikey": chave}
    return h


def listar(bucket, prefixo):
    """Lista recursivamente os arquivos sob um prefixo."""
    arquivos, pendentes = [], [prefixo.rstrip("/")]
    while pendentes:
        p = pendentes.pop()
        r = requests.post(f"{base()}/object/list/{bucket}", headers=cabecalhos(),
                          json={"prefix": p, "limit": 1000, "offset": 0}, timeout=60)
        r.raise_for_status()
        for item in r.json():
            caminho = f"{p}/{item['name']}" if p else item["name"]
            if item.get("id") is None:  # pasta
                pendentes.append(caminho)
            else:
                arquivos.append(caminho)
    return arquivos


def baixar(bucket, remoto, local: pathlib.Path):
    r = requests.get(f"{base()}/object/{bucket}/{urllib.parse.quote(remoto)}", headers=cabecalhos(), timeout=600)
    if r.status_code == 200:
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(r.content)
        return True
    return False


def subir(bucket, local: pathlib.Path, remoto):
    tipo = mimetypes.guess_type(local.name)[0] or "application/octet-stream"
    with local.open("rb") as f:
        r = requests.post(f"{base()}/object/{bucket}/{urllib.parse.quote(remoto)}",
                          headers=cabecalhos({"Content-Type": tipo, "x-upsert": "true"}), data=f, timeout=900)
    if r.status_code not in (200, 201):
        print(f"! não subiu {remoto}: {r.status_code} {r.text[:150]}")
        return False
    return True


def baixar_credenciais():
    n = sum(baixar(B_CRED, nome, CRED / nome) for nome in
            ("instagram.json", "youtube-client.json", "youtube-token.json", "_oauth_pendente.json"))
    print(f"= {n} credenciais baixadas")


def subir_credenciais():
    n = sum(subir(B_CRED, p, p.name) for p in CRED.glob("*.json")) if CRED.exists() else 0
    print(f"+ {n} credenciais salvas")


def baixar_pacote(data):
    arquivos = listar(B_PACOTE, data)
    for remoto in arquivos:
        local = SAIDA / remoto
        # Textos (estado, revisão, logs) sempre vêm do Supabase, que é a fonte da verdade;
        # mídia só é baixada se ainda não existir.
        if local.suffix.lower() in TEXTO or not local.exists():
            baixar(B_PACOTE, remoto, local)
    print(f"= pacote {data}: {len(arquivos)} arquivos")


def subir_pacote(data, so_texto=False):
    pasta = SAIDA / data
    if not pasta.exists():
        print(f"! sem pasta {pasta}")
        return
    n = 0
    for p in sorted(pasta.rglob("*")):
        if p.is_file() and (not so_texto or p.suffix.lower() in TEXTO):
            n += subir(B_PACOTE, p, str(p.relative_to(SAIDA)))
    print(f"+ pacote {data}: {n} arquivos salvos")


def main():
    carregar_env()
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "baixar-credenciais":
        baixar_credenciais()
    elif cmd == "subir-credenciais":
        subir_credenciais()
    elif cmd == "baixar-pacote" and args:
        baixar_pacote(args[0])
    elif cmd == "subir-pacote" and args:
        subir_pacote(args[0], "--so-texto" in args)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
