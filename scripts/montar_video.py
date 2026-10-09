#!/usr/bin/env python3
"""Monta o vídeo de uma peça: imagens + narração (MIA/casal) + trilha da marca.

Uso:
  python scripts/montar_video.py saida/2026-10-10/01-cansada --formato 9x16
  python scripts/montar_video.py saida/2026-10-10/05-longo-sono --formato 16x9

Na pasta da peça:
  narracao*.mp3       -> concatenados em ordem (narracao.mp3 ou narracao-01-ela.mp3, narracao-02-ele.mp3...)
  imagens/*.png|jpg   -> slides em ordem alfabética, tempo dividido igualmente (opcional)
  telas.txt           -> uma linha por cena com o texto na tela, usado quando não há imagens (opcional)
Trilha: assets/trilha/sala-escura.mp3 (se existir), em volume baixo.
Saída: video.mp4 na pasta da peça.
"""
import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import textwrap

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FORMATOS = {"9x16": (1080, 1920), "16x9": (1920, 1080), "4x5": (1080, 1350)}
COR_FUNDO = "0x14101F"  # roxo escuro; troque pela cor do design system
FONTE = RAIZ / "assets" / "fontes" / "marca.ttf"


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffmpeg falhou:\n{' '.join(map(str, cmd))}\n{r.stderr[-1500:]}")
    return r.stdout


def duracao(arquivo) -> float:
    out = sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(arquivo)])
    return float(json.loads(out)["format"]["duration"])


def juntar_audios(mp3s, destino):
    lista = destino.parent / "lista_audio.txt"
    lista.write_text("".join(f"file '{m.resolve()}'\n" for m in mp3s), encoding="utf-8")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lista), "-c:a", "libmp3lame", "-q:a", "2", str(destino)])


def slides_de_texto(telas, tmp, w, h):
    imgs = []
    for i, texto in enumerate(telas):
        arq_txt = tmp / f"t{i}.txt"
        arq_txt.write_text("\n".join(textwrap.wrap(texto, 22 if w < h else 40)), encoding="utf-8")
        fonte = f":fontfile='{FONTE}'" if FONTE.exists() else ""
        img = tmp / f"s{i:02d}.png"
        sh(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c={COR_FUNDO}:s={w}x{h}", "-frames:v", "1", "-vf",
            f"drawtext=textfile='{arq_txt}'{fonte}:fontcolor=white:fontsize={int(w/14)}:line_spacing=18:"
            f"x=(w-text_w)/2:y=(h-text_h)/2", str(img)])
        imgs.append(img)
    return imgs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--formato", default="9x16", choices=FORMATOS.keys())
    a = ap.parse_args()
    pasta = pathlib.Path(a.pasta)
    w, h = FORMATOS[a.formato]

    mp3s = sorted(pasta.glob("narracao*.mp3"))
    if not mp3s:
        sys.exit(f"Sem narração em {pasta}. Rode scripts/narrar.py antes.")

    with tempfile.TemporaryDirectory() as t:
        tmp = pathlib.Path(t)
        voz = tmp / "voz.mp3"
        juntar_audios(mp3s, voz)
        total = duracao(voz) + 0.8

        imgs = sorted([*pasta.glob("imagens/*.png"), *pasta.glob("imagens/*.jpg")])
        if not imgs:
            telas_arq = pasta / "telas.txt"
            telas = [l.strip() for l in telas_arq.read_text(encoding="utf-8").splitlines() if l.strip()] \
                if telas_arq.exists() else ["Série Certa", "seriecerta.online"]
            imgs = slides_de_texto(telas, tmp, w, h)

        por_img = total / len(imgs)
        lista = tmp / "lista_img.txt"
        lista.write_text("".join(f"file '{i.resolve()}'\nduration {por_img:.3f}\n" for i in imgs)
                         + f"file '{imgs[-1].resolve()}'\n", encoding="utf-8")

        trilha = RAIZ / "assets" / "trilha" / "sala-escura.mp3"
        entradas = ["-f", "concat", "-safe", "0", "-i", str(lista), "-i", str(voz)]
        filtro_v = (f"[0:v]scale={w}:{h}:force_original_aspect_ratio=decrease,"
                    f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color={COR_FUNDO},fps=30,format=yuv420p[v]")
        if trilha.exists():
            entradas += ["-stream_loop", "-1", "-i", str(trilha)]
            filtro_a = "[2:a]volume=0.12[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]"
        else:
            filtro_a = "[1:a]anull[a]"

        saida = pasta / "video.mp4"
        sh(["ffmpeg", "-y", *entradas, "-filter_complex", f"{filtro_v};{filtro_a}",
            "-map", "[v]", "-map", "[a]", "-t", f"{total:.2f}",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", str(saida)])
    print(f"+ vídeo: {saida} ({total:.1f}s, {w}x{h})")


if __name__ == "__main__":
    if not shutil.which("ffmpeg"):
        sys.exit("Instale o ffmpeg (Mac: brew install ffmpeg | Windows: winget install ffmpeg)")
    main()
