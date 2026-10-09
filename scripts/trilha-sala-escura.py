"""Trilha "Sala Escura" — lo-fi original do Série Certa (composta por código, sem amostras de terceiros).
 
93 BPM, Dó maior, progressão Dm9 – G13 – Cmaj9 – Am9 (um acorde por compasso, ciclo de 4 compassos).
Gera:
  sala-escura-30s.wav   — versão do vídeo "Como funciona" (virada aos 10,3 s, saída aos 27 s)
  sala-escura-loop.wav  — 24 compassos (~62 s) que emendam sem corte, para futuras postagens
"""
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
 
SR = 48000
BPM = 93
BEAT = 60 / BPM
BAR = 4 * BEAT
rng = np.random.default_rng(7)
import os
DEBUG = bool(os.environ.get('DEBUG'))
 
def hz(midi): return 440.0 * 2 ** ((midi - 69) / 12)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x)
 
def adsr(n, a, d, s, r):
    env = np.ones(n) * s
    ai, di, ri = int(a * SR), int(d * SR), int(r * SR)
    ai = min(ai, n); env[:ai] = np.linspace(0, 1, ai, endpoint=False) if ai else env[:ai]
    de = min(n, ai + di); env[ai:de] = np.linspace(1, s, de - ai, endpoint=False)
    if ri: env[max(0, n - ri):] *= np.linspace(1, 0, min(ri, n))
    return env
 
# ── vozes ─────────────────────────────────────────────────────────────────────
def rhodes(f, dur, vel=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    det = 1 + rng.uniform(-0.0015, 0.0015)
    tone = (np.sin(2 * np.pi * f * det * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 6)
            + 0.12 * np.sin(2 * np.pi * 3.01 * f * t) * np.exp(-t * 9))
    env = np.exp(-t * 1.4) * adsr(n, 0.006, 0.05, 1, 0.12)
    trem = 1 + 0.12 * np.sin(2 * np.pi * 4.6 * t)
    return tone * env * trem * vel
 
def pad(f, dur, vel=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * f * (1 + d) * t + p) for d, p in ((-.004, 0), (0, 1.3), (.004, 2.1)))
    x += 0.3 * sum(np.sin(2 * np.pi * 2 * f * (1 + d) * t) for d in (-.003, .003))
    return lp(x, 1800) * adsr(n, 0.9, 0.4, 0.8, 0.9) * vel / 3
 
def bass(f, dur, vel=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)
    return np.tanh(1.4 * x) * adsr(n, 0.01, 0.25, 0.7, 0.08) * vel
 
def kick():
    n = int(0.42 * SR); t = np.arange(n) / SR
    f = 46 + 90 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 7.5) + 0.25 * lp(rng.standard_normal(n), 900) * np.exp(-t * 60)
 
def snare():
    n = int(0.32 * SR); t = np.arange(n) / SR
    noise = bp(rng.standard_normal(n), 900, 6000) * np.exp(-t * 16)
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 22)
    return 0.55 * noise + 0.45 * body
 
def hat(open_=False):
    n = int((0.22 if open_ else 0.07) * SR); t = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7000) * np.exp(-t * (14 if open_ else 70))
 
def bell(f, dur, vel=1.0):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t + 0.8 * np.sin(2 * np.pi * f * 2.0 * t) * np.exp(-t * 3))
    return x * np.exp(-t * 2.6) * adsr(n, 0.004, 0.02, 1, 0.1) * vel
 
# ── harmonia ─────────────────────────────────────────────────────────────────
# notas MIDI (voicing de mão esquerda + direita, estilo neo-soul)
ACORDES = [
    {'nome': 'Dm9',   'raiz': 38, 'voz': [53, 57, 60, 64]},   # F A C E
    {'nome': 'G13',   'raiz': 43, 'voz': [53, 59, 64, 69]},   # F B E A
    {'nome': 'Cmaj9', 'raiz': 36, 'voz': [52, 55, 59, 62]},   # E G B D
    {'nome': 'Am9',   'raiz': 33, 'voz': [55, 60, 64, 71]},   # G C E B
]
# motivo pentatônico (compasso-relativo: tempo em batidas, nota, duração)
MELODIA = [
    [(0.5, 76, 0.5), (1.0, 74, 0.5), (1.5, 72, 1.0), (3.0, 69, 0.75)],
    [(0.5, 74, 0.5), (1.0, 71, 0.5), (2.0, 74, 1.5)],
    [(0.0, 76, 0.75), (1.0, 79, 0.5), (1.5, 76, 0.5), (2.5, 74, 1.25)],
    [(0.5, 72, 0.5), (1.0, 69, 1.0), (2.5, 72, 1.0)],
]
 
def swing(beat_pos):  # colcheias com swing leve (56%)
    inteiro = np.floor(beat_pos); frac = beat_pos - inteiro
    return inteiro + (0.56 if abs(frac - 0.5) < 1e-6 else frac)
 
def render(n_bars, secoes, dur_total=None, fade_out=0.0):
    """secoes(bar) -> dict com níveis {pad, keys, bass, drums, hats, mel} de 0 a 1."""
    total = dur_total or n_bars * BAR + 3.0
    N = int(total * SR)
    trilhas = {k: np.zeros(N + SR * 4) for k in ('pad', 'keys', 'bass', 'kick', 'snare', 'hats', 'mel')}
 
    def put(nome, sinal, t):
        i = max(0, int(t * SR))
        if i >= N: return
        j = min(i + len(sinal), len(trilhas[nome]))
        trilhas[nome][i:j] += sinal[:j - i]
 
    for b in range(n_bars):
        s = secoes(b)
        c = ACORDES[b % 4]; t0 = b * BAR
        if s['pad']:
            for m in c['voz'][:3]:
                put('pad', pad(hz(m - 12), BAR + 0.9, 0.22 * s['pad']), t0)
        if s['keys']:
            # acorde no 1 e "empurrado" antes do 3 (comping)
            for k, m in enumerate(c['voz']):
                put('keys', rhodes(hz(m), BEAT * 1.9, 0.30 * s['keys']), t0 + k * 0.012)
                put('keys', rhodes(hz(m), BEAT * 1.6, 0.22 * s['keys']), t0 + swing(2.5) * BEAT + k * 0.010)
        if s['bass']:
            r = c['raiz']
            for pos, nota, d in ((0, r, 1.4), (1.5, r, 0.4), (2.5, r + 7, 0.9), (3.5, r + 12 if b % 2 else r + 10, 0.4)):
                put('bass', bass(hz(nota), d * BEAT, 0.42 * s['bass']), t0 + swing(pos) * BEAT)
        meio = s.get('meio', False)  # bateria só na 1ª metade do compasso (parada no 3º tempo)
        if s['drums']:
            for pos in ((0,) if meio else (0, 2.5) if b % 2 == 0 else (0, 1.75, 2.5)):
                put('kick', kick() * 0.9 * s['drums'], t0 + swing(pos) * BEAT)
            for pos in ((1,) if meio else (1, 3)):
                put('snare', snare() * 1.7 * s['drums'], t0 + pos * BEAT + 0.018)
        if s['hats']:
            for k in range(4 if meio else 8):
                pos = swing(k * 0.5)
                vel = (0.55 if k % 2 == 0 else 0.34) * s['hats']
                put('hats', hat(open_=(k == 7 and b % 4 == 3)) * vel, t0 + pos * BEAT + rng.uniform(-0.004, 0.004))
        if s['mel']:
            for pos, nota, d in MELODIA[b % 4]:
                put('mel', bell(hz(nota), d * BEAT + 0.9, 0.40 * s['mel']), t0 + swing(pos) * BEAT)
 
    # ── mixagem ──
    kick_env = np.convolve(np.abs(trilhas['kick']), np.ones(int(0.06 * SR)) / int(0.06 * SR), 'same')
    duck = 1 - 0.35 * np.clip(kick_env / (kick_env.max() + 1e-9) * 2.2, 0, 1)
    mix = (trilhas['pad'] * 0.9 + lp(trilhas['keys'], 5200) + trilhas['bass'] * 0.95) * duck
    mix += trilhas['kick'] * 0.95 + lp(trilhas['snare'], 7000) * 0.8 + trilhas['hats'] * 0.55 + trilhas['mel'] * 0.9
 
    # reverb curto (sala escura)
    ir_n = int(1.6 * SR); ti = np.arange(ir_n) / SR
    ir = lp(rng.standard_normal(ir_n), 4500) * np.exp(-ti * 3.6); ir /= np.abs(ir).sum() / 6
    send = trilhas['keys'] * 0.5 + trilhas['mel'] * 0.8 + lp(trilhas['snare'], 5000) * 0.3
    mix = mix + fftconvolve(send, ir)[:len(mix)] * 0.35
 
    mix = mix[:N]
    # textura de vinil: chiado + estalos
    hiss = lp(hp(rng.standard_normal(N), 1500), 6500) * 0.006
    estalos = np.zeros(N); idx = rng.integers(0, N, int(total * 9)); estalos[idx] = rng.uniform(0.05, 0.25, len(idx)) * rng.choice([-1, 1], len(idx))
    mix += hiss + lp(estalos, 3500) * 0.9
 
    # fita: tom mais quente e saturação leve (normaliza antes, para a saturação ser só um toque)
    mix = mix / (np.abs(mix).max() + 1e-9) * 0.6
    if DEBUG:
        for k, v in trilhas.items():
            print(f'  {k:6s} rms {20*np.log10(np.sqrt(np.mean(v[:N]**2))+1e-12):6.1f} dB')
    mix = lp(mix, 10500, 1)
    mix = np.tanh(mix * 1.25) / np.tanh(1.25)
    # wow & flutter discreto
    t = np.arange(N) / SR
    desloc = (0.0009 * np.sin(2 * np.pi * 0.55 * t) + 0.0002 * np.sin(2 * np.pi * 6.1 * t)) * SR
    mix = np.interp(np.arange(N) + desloc, np.arange(N), mix)
 
    mix = np.stack([mix, mix], 1)
    # estéreo: pad e hats um pouco abertos
    largura = np.stack([trilhas['hats'][:N] * 0.10, -trilhas['hats'][:N] * 0.10], 1)
    largura += np.stack([trilhas['pad'][:N] * 0.10, -trilhas['pad'][:N] * 0.10], 1)
    mix += largura
    if fade_out:
        k = int(fade_out * SR); mix[-k:] *= np.linspace(1, 0, k)[:, None] ** 1.5
    mix *= 0.89 / np.abs(mix).max()   # pico a -1 dBFS
    return mix
 
def salvar(nome, x):
    from scipy.io import wavfile
    wavfile.write(nome, SR, (x * 32767).astype(np.int16))
 
# ── versão do vídeo (30 s): roteiro musical casado com as cenas ───────────────
# compasso 0 (0–2,6 s) abertura: só pad + vinil · 1–3 (2,6–10,3 s) entra o app: keys, baixo, chimbal
# 4–9 (10,3–25,8 s) recomendações: batida completa + melodia · 10 (25,8 s+) encerramento: só keys e pad
def secoes_video(b):
    if b == 0:  return dict(pad=1, keys=0.0, bass=0, drums=0, hats=0, mel=0)
    if b <= 3:  return dict(pad=1, keys=0.8, bass=0.8, drums=0, hats=0.7, mel=0)
    if b <= 9:  return dict(pad=0.8, keys=1, bass=1, drums=1, hats=1, mel=1 if b >= 5 else 0.0)
    if b == 10: return dict(pad=1, keys=0.9, bass=0.7, drums=1, hats=1, mel=0, meio=True)  # para aos 27,1 s
    return dict(pad=1, keys=0.9, bass=0.5, drums=0, hats=0, mel=0)
 
video = render(12, secoes_video, dur_total=30.0, fade_out=2.2)
salvar('sala-escura-30s.wav', video)
 
# ── versão em loop (24 compassos ≈ 62 s): mesmo nível do começo ao fim para emendar ──
def secoes_loop(b):
    return dict(pad=0.8, keys=1, bass=1, drums=1, hats=1, mel=1 if (b // 4) % 2 == 1 else 0)
n = 24
longa = render(n + 2, secoes_loop, dur_total=(n + 2) * BAR)
# emenda: cauda dos 2 compassos extras volta para o começo (crossfade de 1 compasso)
L = int(n * BAR * SR); cf = int(BAR * SR)
loop = longa[:L].copy()
cauda = longa[L:L + cf]
rampa = np.linspace(0, 1, cf)[:, None]
loop[:cf] = loop[:cf] * rampa + cauda * (1 - rampa)
loop *= 0.89 / np.abs(loop).max()
salvar('sala-escura-loop.wav', loop)
print('ok', video.shape[0] / SR, loop.shape[0] / SR, 'BPM', BPM, 'compasso', round(BAR, 4))