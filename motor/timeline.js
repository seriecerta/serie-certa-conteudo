/* ─────────────────────────────────────────────────────────────────────────────
   Motor de tempo do Série Certa. Determinístico: o renderizador chama seek(t)
   para cada quadro e tira um print. Nada depende do relógio real.

   Atributos (em qualquer elemento):
     data-in="2.4" | "@palavra" | "@palavra#2" | "@palavra+0.3" | "@fim"
     data-out="..."                       (mesmo formato; some depois disso)
     data-anim="pop|sobe|desce|fade|esquerda|direita|carimbo|zoom|nada"   (entrada)
     data-loop="treme|pulsa|flutua|pisca|gira"                            (enquanto visível)
     data-dur="0.45"                      (duração da entrada)
     data-conta="0>217" [data-dur]         (número contando; aceita sufixo em data-sufixo)
     data-enche="0>0.8"                   (anima --p de barras de 0 a 0.8)
     data-rola="0>900"                    (anima --rola em px: catálogo rolando)
     data-digita                          (texto aparece letra a letra; data-dur = tempo total)
     data-hora="21:00>23:14"              (relógio avançando)
   <section class="cena" data-in data-out> = troca de tela inteira.
   ───────────────────────────────────────────────────────────────────────────── */
(function () {
  const ALINH = window.__ALINHAMENTO || { palavras: [], duracao: 0 };
  const norm = (s) => (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');

  function tempo(v, padrao) {
    if (v == null || v === '') return padrao;
    v = String(v).trim();
    if (!v.startsWith('@')) return parseFloat(v);
    let m = v.slice(1), extra = 0, n = 1;
    const off = m.match(/([+-]\d*\.?\d+)$/);
    if (off) { extra = parseFloat(off[1]); m = m.slice(0, -off[1].length); }
    const nth = m.match(/#(\d+)$/);
    if (nth) { n = parseInt(nth[1], 10); m = m.slice(0, -nth[0].length); }
    if (m === 'fim') return ALINH.duracao + extra;
    const alvo = norm(m);
    let achou = 0;
    for (const p of ALINH.palavras) {
      if (norm(p.t) === alvo && ++achou === n) return p.i + extra;
    }
    console.warn('palavra não encontrada na narração:', v);
    return padrao;
  }

  const ease = {
    out: (x) => 1 - Math.pow(1 - x, 3),
    back: (x) => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); },
    inout: (x) => (x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
  };
  const clamp = (x) => Math.max(0, Math.min(1, x));
  const lerp = (a, b, k) => a + (b - a) * k;

  let itens = [];
  function preparar() {
    itens = [...document.querySelectorAll('[data-in],[data-out],[data-conta],[data-enche],[data-rola],[data-digita],[data-hora],[data-loop],[data-som]')].map((el) => {
      const sec = el.closest('section.cena');
      const herdado = sec && sec !== el ? tempo(sec.dataset.in, 0) : 0;
      const it = {
        el,
        ini: tempo(el.dataset.in, herdado),
        fim: tempo(el.dataset.out, Infinity),
        anim: el.dataset.anim || (el.matches('section.cena') ? 'nada' : 'pop'),
        dur: parseFloat(el.dataset.dur || (el.dataset.digita != null ? 1.2 : el.dataset.conta || el.dataset.enche || el.dataset.rola || el.dataset.hora ? 1.4 : 0.42)),
        loop: el.dataset.loop,
        // entrada (pop/sobe/…) tem duração própria; data-dur vale para contagem/relógio/digitação quando existem
        durIn: parseFloat(el.dataset.durEntrada || (el.dataset.conta || el.dataset.enche || el.dataset.rola || el.dataset.hora || el.dataset.digita != null ? 0.42 : (el.dataset.dur || 0.42))),
        // contadores/barras/relógio podem aparecer antes e só começar a andar em data-anima-em
        anIni: tempo(el.dataset.animaEm, null),
        texto: el.dataset.digita != null ? el.textContent : null,
      };
      if (it.texto != null) el.textContent = '';
      return it;
    });
  }

  function aplicarEntrada(it, k) {
    const s = it.el.style;
    s.opacity = ''; s.translate = ''; s.scale = ''; s.rotate = '';
    if (k >= 1 || it.anim === 'nada') return;
    const e = ease.out(k), b = ease.back(k);
    switch (it.anim) {
      case 'pop': s.opacity = e; s.scale = lerp(.6, 1, b); break;
      case 'sobe': s.opacity = e; s.translate = `0 ${lerp(80, 0, e)}px`; break;
      case 'desce': s.opacity = e; s.translate = `0 ${lerp(-80, 0, e)}px`; break;
      case 'esquerda': s.opacity = e; s.translate = `${lerp(-500, 0, e)}px 0`; break;
      case 'direita': s.opacity = e; s.translate = `${lerp(500, 0, e)}px 0`; break;
      case 'fade': s.opacity = e; break;
      case 'zoom': s.opacity = e; s.scale = lerp(1.25, 1, e); break;
      case 'carimbo': s.opacity = clamp(k * 3); s.scale = lerp(2.4, 1, ease.out(clamp(k * 1.4))); break;
    }
  }

  function aplicarLoop(it, t) {
    const s = it.el.style, x = t - it.ini;
    switch (it.loop) {
      case 'treme': s.rotate = `${Math.sin(x * 38) * 2.2}deg`; break;
      case 'pulsa': s.scale = String(1 + Math.sin(x * 5) * 0.04); break;
      case 'flutua': s.translate = `0 ${Math.sin(x * 2.4) * 14}px`; break;
      case 'gira': s.rotate = `${x * 120}deg`; break;
      case 'pisca': it.el.style.setProperty('--pisca', Math.floor(x * 2) % 2 ? .15 : 1); break;
    }
  }

  function faixa(str) { const [a, b] = String(str).split('>'); return [parseFloat(a), parseFloat(b)]; }

  window.seek = function (t) {
    for (const it of itens) {
      const vis = t >= it.ini && t < it.fim;
      it.el.style.visibility = vis ? '' : 'hidden';
      if (!vis) continue;
      const k = clamp((t - it.ini) / it.dur);
      const kIn = clamp((t - it.ini) / it.durIn);
      if (it.el.dataset.in != null || it.el.dataset.anim) aplicarEntrada(it, kIn);
      if (it.loop && kIn >= 1) aplicarLoop(it, t);
      const d = it.el.dataset;
      const kk = ease.inout(it.anIni == null ? k : clamp((t - it.anIni) / it.dur));
      if (d.conta) { const [a, b] = faixa(d.conta); it.el.textContent = Math.round(lerp(a, b, kk)).toLocaleString('pt-BR') + (d.sufixo || ''); }
      if (d.enche) { const [a, b] = faixa(d.enche); it.el.style.setProperty('--p', lerp(a, b, kk)); }
      if (d.rola) { const [a, b] = faixa(d.rola); it.el.style.setProperty('--rola', lerp(a, b, kk)); }
      if (d.hora) {
        const [a, b] = d.hora.split('>').map((h) => { const [H, M] = h.split(':').map(Number); return H * 60 + M; });
        const m = Math.round(lerp(a, b, kk));
        it.el.textContent = `${Math.floor(m / 60)}:${String(m % 60).padStart(2, '0')}`;
      }
      if (it.texto != null) it.el.textContent = it.texto.slice(0, Math.round(it.texto.length * k));
    }
    legendaEm(t);
  };

  /* ── legenda automática a partir da narração ─────────────────────────── */
  let grupos = [], caixaLeg = null;
  function montarLegenda() {
    const cfg = document.body.dataset;
    if (cfg.legenda !== 'auto' || !ALINH.palavras.length) return;
    const max = parseInt(cfg.legendaPalavras || '3', 10);
    const destaques = new Set((cfg.destaque || '').split(',').map(norm).filter(Boolean));
    let atual = [];
    const fecha = () => { if (atual.length) grupos.push(atual); atual = []; };
    ALINH.palavras.forEach((p, i) => {
      const prox = ALINH.palavras[i + 1];
      atual.push(p);
      const pausa = prox ? prox.i - p.f : 1;
      if (/[.,!?;:…]$/.test(p.t) || atual.length >= max || pausa > 0.35) fecha();
    });
    fecha();
    grupos = grupos.map((g, gi) => {
      const prox = grupos[gi + 1];
      const fim = prox ? prox[0].i : g[g.length - 1].f + 0.6;
      let marcadas = g.map((p) => destaques.has(norm(p.t)));
      if (!marcadas.some(Boolean) && !destaques.size) {
        // sem lista: destaca a palavra mais longa do grupo (≥4 letras), como nos posts
        let melhor = -1, tam = 3;
        g.forEach((p, k) => { const n = norm(p.t).length; if (n > tam) { tam = n; melhor = k; } });
        marcadas = g.map((_, k) => k === melhor && g.length > 1);
      }
      return { ini: g[0].i, fim, html: g.map((p, k) => `<span class="w${marcadas[k] ? ' b' : ''}">${p.t}</span>`).join(' ') };
    });
    caixaLeg = document.createElement('div');
    caixaLeg.className = 'legenda';
    if (cfg.legendaTop) caixaLeg.style.top = cfg.legendaTop + 'px';
    document.body.appendChild(caixaLeg);
  }
  let ultimo = null;
  function legendaEm(t) {
    if (!caixaLeg) return;
    // uma cena com data-legenda="off" esconde a legenda enquanto estiver na tela
    const off = [...document.querySelectorAll('section.cena[data-legenda="off"]')].some((s) => s.style.visibility !== 'hidden');
    const g = off ? null : grupos.find((x) => t >= x.ini && t < x.fim);
    if (g !== ultimo) { caixaLeg.innerHTML = g ? g.html : ''; ultimo = g; }
    if (g) { const k = clamp((t - g.ini) / 0.16); caixaLeg.style.scale = String(lerp(.9, 1, ease.back(k))); caixaLeg.style.opacity = k; }
  }

  window.__preparar = function () { preparar(); montarLegenda(); window.seek(0); };

  /* efeitos sonoros: data-som="pop|carimbo|whoosh|tick|ding|virada|digita" toca na entrada do elemento */
  window.__eventos = function () {
    return itens.filter((it) => it.el.dataset.som && isFinite(it.ini))
      .map((it) => ({ som: it.el.dataset.som, t: it.ini, vol: parseFloat(it.el.dataset.somVol || '1') }));
  };
})();
