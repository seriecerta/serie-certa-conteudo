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
# Sistema visual "Sala Escura" do app (app/globals.css)
COR_FUNDO = "0x0B1410"    # --noite-900
COR_TITULO = "0xF1E8D6"   # --papel
COR_TEXTO = "0xB7BDA8"    # --papel-2
COR_DESTAQUE = "0xFF5A36"  # --brasa
COR_RODAPE = "0x7F8E80"   # --musgo
FONTE = RAIZ / "assets" / "fontes" / "marca.ttf"


def esc(p):  # caminho seguro dentro do filtro do ffmpeg
    return str(p).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def render(destino, w, h, blocos, fundo):
    """blocos: [(texto, tamanho_fonte, caracteres_por_linha, cor)] — alinhados à esquerda, com barra brasa no topo."""
    fonte = f":fontfile='{esc(FONTE)}'" if FONTE.exists() else ""
    margem = int(w * 0.09)
    y = int(h * 0.22)
    filtros = [f"drawbox=x={margem}:y={y - 60}:w=120:h=12:color={COR_DESTAQUE}:t=fill"]
    with tempfile.TemporaryDirectory() as t:
        for i, (texto, tamanho, largura, cor) in enumerate(blocos):
            if not texto:
                continue
            linhas = textwrap.wrap(texto, largura)
            arq = pathlib.Path(t) / f"b{i}.txt"
            arq.write_text("\n".join(linhas), encoding="utf-8")
            espaco = int(tamanho * 0.25)
            filtros.append(f"drawtext=textfile='{esc(arq)}'{fonte}:fontcolor={cor}:fontsize={tamanho}:"
                           f"line_spacing={espaco}:x={margem}:y={y}")
            y += len(linhas) * (tamanho + espaco) + int(tamanho * 0.9)
        rod = pathlib.Path(t) / "rodape.txt"
        rod.write_text("seriecerta.online", encoding="utf-8")
        filtros.append(f"drawtext=textfile='{esc(rod)}'{fonte}:fontcolor={COR_RODAPE}:fontsize={int(w / 30)}:"
                       f"x={margem}:y=h-{int(h * 0.07)}")
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
                   [(c.get("titulo", ""), 84, 19, COR_TITULO), (c.get("texto", ""), 46, 34, COR_TEXTO)],
                   RAIZ / "assets" / "templates" / "card.jpg")
            feitos += 1
    sto = pasta / "stories.json"
    if sto.exists():
        (pasta / "stories").mkdir(exist_ok=True)
        for i, s in enumerate(json.loads(sto.read_text(encoding="utf-8"))["telas"], 1):
            render(pasta / "stories" / f"{i:02d}.jpg", 1080, 1920,
                   [(s.get("texto", ""), 84, 19, COR_TITULO), (s.get("rodape", ""), 46, 32, COR_DESTAQUE)],
                   RAIZ / "assets" / "templates" / "story.jpg")
            feitos += 1
    print(f"+ {feitos} imagens em {pasta}")


if __name__ == "__main__":
    main()
