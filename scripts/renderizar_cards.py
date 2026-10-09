#!/usr/bin/env python3
"""Renderiza carrossel e Stories em JPEG (formato que o Instagram aceita).

Uso: python scripts/renderizar_cards.py saida/2026-10-10/02-carrossel-cansada

Lê da pasta da peça:
  carrossel.json  {"cards": [{"titulo": "...", "texto": "..."}]}       -> cards/01.jpg ... (1080x1350)
  stories.json    {"telas": [{"texto": "...", "rodape": "link na bio"}]} -> stories/01.jpg ... (1080x1920)
Se houver arte de fundo em assets/templates/card.jpg ou story.jpg, ela é usada no lugar da cor sólida.
"""
import json
import pathlib
import subprocess
import sys
import tempfile
import textwrap

RAIZ = pathlib.Path(__file__).resolve().parent.parent
COR_FUNDO = "0x14101F"  # mesma cor de scripts/montar_video.py
FONTE = RAIZ / "assets" / "fontes" / "marca.ttf"


def esc(p):  # caminho seguro dentro do filtro do ffmpeg
    return str(p).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def render(destino, w, h, blocos, fundo):
    fonte = f":fontfile='{esc(FONTE)}'" if FONTE.exists() else ""
    filtros, y = [], 0.18
    with tempfile.TemporaryDirectory() as t:
        for i, (texto, tamanho, largura) in enumerate(blocos):
            if not texto:
                continue
            arq = pathlib.Path(t) / f"b{i}.txt"
            arq.write_text("\n".join(textwrap.wrap(texto, largura)), encoding="utf-8")
            filtros.append(f"drawtext=textfile='{esc(arq)}'{fonte}:fontcolor=white:fontsize={tamanho}:"
                           f"line_spacing=14:x=(w-text_w)/2:y=h*{y:.2f}")
            y += 0.12 + 0.045 * texto.count(" ") / max(largura / 6, 1)
        entrada = ["-i", str(fundo)] if fundo.exists() else ["-f", "lavfi", "-i", f"color=c={COR_FUNDO}:s={w}x{h}"]
        vf = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}," + ",".join(filtros)
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entrada, "-frames:v", "1", "-vf", vf,
                            "-q:v", "2", str(destino)], capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr[-800:])


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pasta = pathlib.Path(sys.argv[1])
    feitos = 0
    car = pasta / "carrossel.json"
    if car.exists():
        (pasta / "cards").mkdir(exist_ok=True)
        for i, c in enumerate(json.loads(car.read_text(encoding="utf-8"))["cards"], 1):
            render(pasta / "cards" / f"{i:02d}.jpg", 1080, 1350,
                   [(c.get("titulo", ""), 78, 20), (c.get("texto", ""), 46, 34)],
                   RAIZ / "assets" / "templates" / "card.jpg")
            feitos += 1
    sto = pasta / "stories.json"
    if sto.exists():
        (pasta / "stories").mkdir(exist_ok=True)
        for i, s in enumerate(json.loads(sto.read_text(encoding="utf-8"))["telas"], 1):
            render(pasta / "stories" / f"{i:02d}.jpg", 1080, 1920,
                   [(s.get("texto", ""), 70, 22), (s.get("rodape", ""), 44, 30)],
                   RAIZ / "assets" / "templates" / "story.jpg")
            feitos += 1
    print(f"+ {feitos} imagens em {pasta}")


if __name__ == "__main__":
    main()
