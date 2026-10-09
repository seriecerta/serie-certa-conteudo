#!/usr/bin/env python3
"""Renderiza uma peça do Série Certa no padrão visual dos posts (motor HTML → MP4/JPEG).

Uso:
  python scripts/renderizar.py saida/2026-10-10/01-tradutor              # vídeo (Reels/Shorts 9:16)
  python scripts/renderizar.py saida/2026-10-10/05-longo --formato 16x9   # vídeo longo do YouTube
  python scripts/renderizar.py saida/2026-10-10/02-carrossel --imagens    # carrossel/Stories em JPEG
  python scripts/renderizar.py <pasta> --previa 3.5                       # um quadro (para conferir)

Na pasta da peça:
  cena.html             corpo da cena (só o <body>...</body> ou o conteúdo dele) — ver motor/COMPONENTES.md
  narracao*.mp3/.json   gerados por scripts/narrar.py (o .json traz o tempo de cada palavra)
  imagens/              opcional: pôsteres/prints usados na cena (<img src="imagens/x.jpg">)
Saídas: video.mp4 + capa.jpg (modo vídeo) · quadros/01.jpg… (modo imagens) · previa.jpg
"""
import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MOTOR = RAIZ / "motor"
TRILHA = RAIZ / "assets" / "trilha" / "sala-escura.mp3"
FORMATOS = {"9x16": (1080, 1920), "16x9": (1920, 1080), "4x5": (1080, 1350)}
ATRASO_FALA = 0.30  # a fala começa um pouco depois do primeiro quadro


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"falhou: {' '.join(map(str, cmd))[:200]}\n{r.stderr[-1500:]}")
    return r.stdout


def duracao(arq):
    return float(json.loads(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json",
                                str(arq)]))["format"]["duration"])


def juntar_narracao(pasta: pathlib.Path, tmp: pathlib.Path):
    """Concatena narracao*.mp3 (casal: uma fala por arquivo) e une os alinhamentos com o deslocamento certo."""
    mp3s = sorted(pasta.glob("narracao*.mp3"))
    palavras, t0, partes = [], ATRASO_FALA, []
    pausa = 0.25
    for i, mp3 in enumerate(mp3s):
        d = duracao(mp3)
        js = mp3.with_suffix(".json")
        if js.exists():
            for p in json.loads(js.read_text(encoding="utf-8")).get("palavras", []):
                palavras.append({"t": p["t"], "i": round(p["i"] + t0, 3), "f": round(p["f"] + t0, 3)})
        partes.append((mp3, t0))
        t0 += d + (pausa if i < len(mp3s) - 1 else 0)
    fim_fala = t0 if mp3s else 0
    voz = None
    if mp3s:
        voz = tmp / "voz.wav"
        entradas, filtros = [], []
        for k, (mp3, ini) in enumerate(partes):
            entradas += ["-i", str(mp3)]
            filtros.append(f"[{k}:a]aresample=48000,adelay={int(ini * 1000)}:all=1[a{k}]")
        mix = "".join(f"[a{k}]" for k in range(len(partes)))
        sh(["ffmpeg", "-y", *entradas, "-filter_complex",
            ";".join(filtros) + f";{mix}amix=inputs={len(partes)}:normalize=0[o]", "-map", "[o]", str(voz)])
    return voz, {"palavras": palavras, "duracao": round(fim_fala, 3)}


def montar_html(pasta, alinh, w, h, tmp):
    bruto = (pasta / "cena.html").read_text(encoding="utf-8")
    m = re.search(r"<body([^>]*)>(.*)</body>", bruto, re.S | re.I)
    attrs, corpo = (m.group(1), m.group(2)) if m else ("", bruto)
    estilo_extra = "\n".join(re.findall(r"<style[^>]*>.*?</style>", bruto, re.S | re.I))
    doc = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<base href="{pasta.resolve().as_uri()}/">
<link rel="stylesheet" href="{(MOTOR / 'base.css').resolve().as_uri()}">
<style>html,body{{width:{w}px;height:{h}px}}</style>{estilo_extra}
<script>window.__ALINHAMENTO={json.dumps(alinh, ensure_ascii=False)};</script>
<script src="{(MOTOR / 'timeline.js').resolve().as_uri()}"></script>
</head><body{attrs}>{corpo}</body></html>"""
    arq = tmp / "cena.html"
    arq.write_text(doc, encoding="utf-8")
    return arq


def mixar_audio(mudo, voz, eventos, total, corpo, sem_trilha, saida):
    sys.path.insert(0, str(MOTOR))
    import sons

    entradas, filtros, rotulos = [], [], []
    k = 1  # entrada 0 é o vídeo mudo
    T = f"{total:.3f}"
    if voz:
        entradas += ["-i", str(voz)]
        filtros.append(f"[{k}:a]aresample=48000,apad,atrim=0:{T},asplit=2[v][vsc]")
        rotulos.append("[v]")
        k += 1
    if TRILHA.exists() and not sem_trilha:
        vol = corpo.get("trilha", "0.42")
        entradas += ["-stream_loop", "-1", "-i", str(TRILHA)]
        base = (f"[{k}:a]aresample=48000,atrim=0:{T},volume={vol},afade=t=in:d=0.4,"
                f"afade=t=out:st={max(0, total - 1.4):.3f}:d=1.4")
        if voz:  # ducking: a trilha cai quando há fala
            filtros.append(base + "[mraw]")
            filtros.append("[mraw][vsc]sidechaincompress=threshold=0.015:ratio=9:attack=20:release=380:makeup=1[m]")
        else:
            filtros.append(base + "[m]")
        rotulos.append("[m]")
        k += 1
    elif voz:
        filtros.append("[vsc]anullsink")
    for ev in eventos:
        arq = sons.arquivo(ev["som"])
        if not arq or ev["t"] >= total:
            continue
        entradas += ["-i", str(arq)]
        filtros.append(f"[{k}:a]aresample=48000,adelay={int(ev['t'] * 1000)}:all=1,"
                       f"volume={0.55 * ev.get('vol', 1):.2f}[s{k}]")
        rotulos.append(f"[s{k}]")
        k += 1
    if not rotulos:
        shutil.copy(mudo, saida)
        return
    fc = ";".join(filtros) + f";{''.join(rotulos)}amix=inputs={len(rotulos)}:normalize=0:duration=longest," \
                             f"atrim=0:{T},loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    sh(["ffmpeg", "-y", "-i", str(mudo), *entradas, "-filter_complex", fc, "-map", "0:v", "-map", "[a]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", T, "-movflags", "+faststart", str(saida)])


def abrir(pw, arq, w, h):
    nav = pw.chromium.launch(args=["--allow-file-access-from-files", "--font-render-hinting=none"])
    pg = nav.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
    avisos = []
    pg.on("console", lambda m: avisos.append(m.text) if m.type in ("warning", "error") else None)
    pg.goto(arq.as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    pg.evaluate("window.__preparar()")
    return nav, pg, avisos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--formato", default="9x16", choices=FORMATOS)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--imagens", action="store_true", help="cada <section class='quadro'> vira um JPEG")
    ap.add_argument("--previa", type=float, help="gera só previa.jpg no instante indicado")
    ap.add_argument("--sem-trilha", action="store_true")
    a = ap.parse_args()

    from playwright.sync_api import sync_playwright

    pasta = pathlib.Path(a.pasta)
    if not (pasta / "cena.html").exists():
        sys.exit(f"Falta {pasta}/cena.html")
    w, h = FORMATOS[a.formato]  # carrossel: --formato 4x5 · Stories: 9x16

    with tempfile.TemporaryDirectory() as t, sync_playwright() as pw:
        tmp = pathlib.Path(t)
        voz, alinh = (None, {"palavras": [], "duracao": 0}) if a.imagens else juntar_narracao(pasta, tmp)
        arq = montar_html(pasta, alinh, w, h, tmp)
        nav, pg, avisos = abrir(pw, arq, w, h)

        if a.previa is not None:
            pg.evaluate(f"seek({a.previa})")
            pg.screenshot(path=str(pasta / "previa.jpg"), type="jpeg", quality=90)
            print(f"+ prévia: {pasta / 'previa.jpg'}")
        elif a.imagens:
            n = pg.evaluate("document.querySelectorAll('section.quadro').length")
            saida = pasta / "quadros"
            shutil.rmtree(saida, ignore_errors=True)
            saida.mkdir()
            for i in range(n):
                pg.evaluate(f"""document.querySelectorAll('section.quadro').forEach((s,k)=>s.style.display=k=={i}?'':'none');
                               seek(99)""")
                pg.screenshot(path=str(saida / f"{i + 1:02d}.jpg"), type="jpeg", quality=93)
            print(f"+ {n} imagens em {saida}")
        else:
            corpo = pg.evaluate("document.body.dataset")
            total = float(corpo.get("duracao") or (alinh["duracao"] + float(corpo.get("final", 1.8))))
            n = int(total * a.fps)
            mudo = tmp / "mudo.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(a.fps),
                                   "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                                   "-pix_fmt", "yuv420p", str(mudo)], stdin=subprocess.PIPE)
            for i in range(n):
                pg.evaluate(f"seek({i / a.fps:.4f})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
                if i % (a.fps * 5) == 0:
                    print(f"  quadro {i}/{n}", flush=True)
            ff.stdin.close()
            if ff.wait():
                sys.exit("ffmpeg falhou ao montar o vídeo")
            capa_t = float(corpo.get("capa", min(1.5, total / 2)))
            pg.evaluate(f"seek({capa_t})")
            pg.screenshot(path=str(pasta / "capa.jpg"), type="jpeg", quality=92)

            # áudio: fala + trilha com ducking (abaixa quando a MIA fala) + efeitos, normalizado em −14 LUFS
            eventos = pg.evaluate("window.__eventos ? window.__eventos() : []")
            saida = pasta / ("video-16x9.mp4" if a.formato == "16x9" else "video.mp4")
            mixar_audio(mudo, voz, eventos, total, corpo, a.sem_trilha, saida)
            print(f"+ vídeo: {saida} ({total:.1f}s, {w}x{h}) · capa: {pasta / 'capa.jpg'}")

        for av in dict.fromkeys(avisos):
            print(f"! aviso da cena: {av}")
        nav.close()


if __name__ == "__main__":
    main()
