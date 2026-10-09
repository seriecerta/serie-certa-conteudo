#!/usr/bin/env python3
"""Gera MP3 com as vozes do Série Certa na ElevenLabs.

Uso:
  python scripts/narrar.py saida/2026-10-10            # narra todos os narracao*.txt da pasta (recursivo)
  python scripts/narrar.py arquivo.txt --voz mia       # narra um arquivo

Arquivos terminados em -ela.txt / -ele.txt usam as vozes do casal; o resto usa a MIA.
Pula arquivos que já têm .mp3 mais novo que o .txt (rodar de novo não gasta crédito).
Gera também narracao*.json com o tempo de cada palavra (legendas e cenas sincronizadas com a fala).
Requer ELEVENLABS_API_KEY no ambiente ou no arquivo .env da raiz do projeto.
"""
import argparse
import base64
import json
import os
import pathlib
import sys

import requests

VOZES = {
    "mia": "4guCIgdAFz4tp4vfnsk0",  # MIA – Série Certa
    "ela": "1AxHVMpXJZxq6ECdF4Kn",  # Ela – Casal Série Certa
    "ele": "oeBFFQkxcUHweNreD1nw",  # Ele – Casal Série Certa
}
# eleven_v3: o mesmo modelo dos posts; aceita tags de emoção no texto, ex.: [rindo baixinho], [sussurrando]
MODELO = os.environ.get("ELEVENLABS_MODEL", "eleven_v3")
AJUSTES = {"stability": 0.5, "similarity_boost": 0.8}
API = "https://api.elevenlabs.io/v1"


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
    h = {"xi-api-key": chave} if chave else {}
    corpo = {"text": texto, "model_id": MODELO, "voice_settings": AJUSTES}
    # 1ª opção: áudio + tempo de cada letra num pedido só
    resp = requests.post(f"{API}/text-to-speech/{VOZES[voz]}/with-timestamps", params={"output_format": "mp3_44100_128"},
                         headers={**h, "Content-Type": "application/json"}, json=corpo, timeout=240)
    if resp.status_code == 200:
        dados = resp.json()
        mp3.write_bytes(base64.b64decode(dados["audio_base64"]))
        lista = palavras_de_letras(dados.get("alignment") or dados.get("normalized_alignment") or {})
    elif resp.status_code in (400, 422):
        # o modelo não devolveu tempos: gera o áudio normal e tira os tempos com a transcrição (Scribe)
        r = requests.post(f"{API}/text-to-speech/{VOZES[voz]}", params={"output_format": "mp3_44100_128"},
                          headers={**h, "Content-Type": "application/json"}, json=corpo, timeout=240)
        if r.status_code != 200:
            sys.exit(f"Erro ElevenLabs {r.status_code} em {txt}: {r.text[:300]}")
        mp3.write_bytes(r.content)
        lista = transcrever(mp3, h)
    else:
        # Sem retry automático: erro de crédito/limite não deve gastar de novo em loop.
        sys.exit(f"Erro ElevenLabs {resp.status_code} em {txt}: {resp.text[:300]}")
    txt.with_suffix(".json").write_text(json.dumps({"palavras": sem_tags(lista)}, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
    print(f"+ {voz}: {mp3} ({len(lista)} palavras com tempo)")
    return mp3


def transcrever(mp3: pathlib.Path, h: dict) -> list:
    with mp3.open("rb") as f:
        r = requests.post(f"{API}/speech-to-text", headers=h, timeout=240,
                          data={"model_id": "scribe_v1", "language_code": "por", "timestamps_granularity": "word",
                                "tag_audio_events": "false"},
                          files={"file": (mp3.name, f, "audio/mpeg")})
    if r.status_code != 200:
        print(f"! sem tempos por palavra ({r.status_code}); a legenda automática fica desligada")
        return []
    return [{"t": w["text"].strip(), "i": round(w["start"], 3), "f": round(w["end"], 3)}
            for w in r.json().get("words", []) if w.get("type") == "word" and w["text"].strip()]


def sem_tags(lista: list) -> list:
    """Tira as tags de emoção do v3 ([rindo baixinho]) — elas não são faladas nem vão para a legenda."""
    saida, dentro = [], False
    for p in lista:
        t = p["t"]
        if t.startswith("["):
            dentro = True
        if not dentro:
            saida.append(p)
        if t.endswith("]"):
            dentro = False
    return saida


def palavras_de_letras(alinh: dict) -> list:
    """Transforma o alinhamento por letra da ElevenLabs em palavras com início/fim (segundos)."""
    letras = alinh.get("characters", [])
    ini, fim = alinh.get("character_start_times_seconds", []), alinh.get("character_end_times_seconds", [])
    saida, atual, t0, t1 = [], "", None, None
    for c, a, b in zip(letras, ini, fim):
        if c.isspace():
            if atual:
                saida.append({"t": atual, "i": round(t0, 3), "f": round(t1, 3)})
            atual, t0 = "", None
            continue
        if t0 is None:
            t0 = a
        atual += c
        t1 = b
    if atual:
        saida.append({"t": atual, "i": round(t0, 3), "f": round(t1, 3)})
    return saida


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
