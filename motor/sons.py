"""Efeitos sonoros sintetizados (sem amostras de terceiros) usados pelo motor.

Na cena: data-som="pop|carimbo|whoosh|tick|ding|virada|digita" em qualquer elemento → toca quando ele entra.
"""
import pathlib
import wave

import numpy as np

SR = 48000
PASTA = pathlib.Path(__file__).resolve().parent / "sons"
_rng = np.random.default_rng(3)


def _env(n, ataque=0.003, decai=8.0):
    t = np.arange(n) / SR
    a = np.clip(t / ataque, 0, 1)
    return a * np.exp(-t * decai)


def _ruido(n):
    return _rng.uniform(-1, 1, n)


def _passa_baixa(x, corte):
    # filtro de 1 polo simples (suficiente para efeitos)
    a = np.exp(-2 * np.pi * corte / SR)
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = (1 - a) * x[i] + a * y[i - 1]
    return y


def pop():
    n = int(0.12 * SR); t = np.arange(n) / SR
    f = 950 * np.exp(-t * 18) + 260
    return 0.55 * np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, 0.002, 28)


def carimbo():
    n = int(0.32 * SR); t = np.arange(n) / SR
    baque = np.sin(2 * np.pi * (70 + 90 * np.exp(-t * 30)) * t) * _env(n, 0.001, 14)
    estalo = _passa_baixa(_ruido(n), 2500) * _env(n, 0.0005, 45)
    return 0.9 * baque + 1.4 * estalo


def whoosh():
    n = int(0.38 * SR); t = np.arange(n) / SR
    x = _passa_baixa(_ruido(n), 1800) - _passa_baixa(_ruido(n), 300)
    forma = np.sin(np.pi * t / t[-1]) ** 2
    return 0.9 * x * forma


def tick():
    n = int(0.05 * SR); t = np.arange(n) / SR
    return 0.45 * (np.sin(2 * np.pi * 2200 * t) + 0.5 * np.sin(2 * np.pi * 1100 * t)) * _env(n, 0.0005, 120)


def ding():
    n = int(0.9 * SR); t = np.arange(n) / SR
    return 0.32 * (np.sin(2 * np.pi * 1320 * t) + 0.5 * np.sin(2 * np.pi * 1980 * t)) * _env(n, 0.002, 5)


def virada():
    # relógio virando: dois ticks + whoosh curto
    a, b = tick(), tick()
    out = np.zeros(int(0.3 * SR))
    out[: len(a)] += a
    out[int(0.07 * SR): int(0.07 * SR) + len(b)] += b * 0.8
    w = whoosh()[: len(out)] * 0.4
    out[: len(w)] += w
    return out


def digita():
    out = np.zeros(int(0.6 * SR))
    for k in range(6):
        c = tick() * 0.5
        i = int(k * 0.09 * SR)
        out[i: i + len(c)] += c
    return out


GERADORES = {"pop": pop, "carimbo": carimbo, "whoosh": whoosh, "tick": tick, "ding": ding, "virada": virada,
             "digita": digita}


def arquivo(nome: str) -> pathlib.Path | None:
    if nome not in GERADORES:
        return None
    PASTA.mkdir(exist_ok=True)
    p = PASTA / f"{nome}.wav"
    if not p.exists():
        x = GERADORES[nome]()
        x = (np.clip(x / max(1e-9, np.abs(x).max()) * 0.8, -1, 1) * 32767).astype(np.int16)
        with wave.open(str(p), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(x.tobytes())
    return p
