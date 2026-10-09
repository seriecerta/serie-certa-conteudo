#!/usr/bin/env python3
"""Gera MP3 com as vozes do Série Certa na ElevenLabs.

Uso:
  python scripts/narrar.py saida/2026-10-10            # narra todos os narracao*.txt da pasta (recursivo)
  python scripts/narrar.py arquivo.txt --voz mia       # narra um arquivo

Arquivos terminados em -ela.txt / -ele.txt usam as vozes do casal; o resto usa a MIA.
Pula arquivos que já têm .mp3 mais novo que o .txt (rodar de novo não gasta crédito).
Requer ELEVENLABS_API_KEY no ambiente ou no arquivo .env da raiz do projeto.
"""
import argparse
import os
import pathlib
import sys

import requests

VOZES = {
    "mia": "4guCIgdAFz4tp4vfnsk0",  # MIA – Série Certa
    "ela": "1AxHVMpXJZxq6ECdF4Kn",  # Ela – Casal Série Certa
    "ele": "oeBFFQkxcUHweNreD1nw",  # Ele – Casal Série Certa
}
MODELO = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")
AJUSTES = {"stability": 0.45, "similarity_boost": 0.8, "style": 0.25, "use_speaker_boost": True}


def carregar_env():
    env = pathlib.Path(__file__).resolve().parent.parent / ".env"
    if env.exists():
        for linha in env.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def voz_do_arquivo(caminho: pathlib.Path, padrao: str) -> str:
    nome = caminho.stem.lower()
    if nome.endswith("-ela"):
        return "ela"
    if nome.endswith("-ele"):
        return "ele"
    return padrao


def narrar(txt: pathlib.Path, voz: str, chave: str) -> pathlib.Path:
    mp3 = txt.with_suffix(".mp3")
    if mp3.exists() and mp3.stat().st_mtime >= txt.stat().st_mtime:
        print(f"= já existe: {mp3}")
        return mp3
    texto = txt.read_text(encoding="utf-8").strip()
    if not texto:
        print(f"! vazio, pulando: {txt}")
        return mp3
    resp = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOZES[voz]}",
        params={"output_format": "mp3_44100_128"},
        headers={**({"xi-api-key": chave} if chave else {}), "Content-Type": "application/json"},
        json={"text": texto, "model_id": MODELO, "language_code": "pt", "voice_settings": AJUSTES},
        timeout=180,
    )
    if resp.status_code != 200:
        # Sem retry automático: erro de crédito/limite não deve gastar de novo em loop.
        sys.exit(f"Erro ElevenLabs {resp.status_code} em {txt}: {resp.text[:300]}")
    mp3.write_bytes(resp.content)
    print(f"+ {voz}: {mp3}")
    return mp3


def main():
    carregar_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("alvo", help="arquivo .txt ou pasta")
    ap.add_argument("--voz", default="mia", choices=VOZES.keys())
    a = ap.parse_args()
    chave = os.environ.get("ELEVENLABS_API_KEY")
    if not chave and os.environ.get("CLAUDE_CODE_REMOTE") != "true":
        sys.exit("Defina ELEVENLABS_API_KEY no .env")
    # Na nuvem sem chave no ambiente: a "API credential" do ambiente anexa o xi-api-key pelo proxy.
    alvo = pathlib.Path(a.alvo)
    arquivos = sorted(alvo.rglob("narracao*.txt")) if alvo.is_dir() else [alvo]
    if not arquivos:
        sys.exit(f"Nenhum narracao*.txt em {alvo}")
    for txt in arquivos:
        narrar(txt, voz_do_arquivo(txt, a.voz), chave)


if __name__ == "__main__":
    main()
