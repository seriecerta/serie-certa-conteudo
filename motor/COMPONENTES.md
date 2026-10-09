# Motor de vídeo — como escrever uma cena

Cada peça de vídeo tem um `cena.html` na pasta dela. Você escreve **só o `<body>`** com os componentes abaixo;
o `scripts/renderizar.py` coloca o sistema visual (`motor/base.css`), o motor de tempo (`motor/timeline.js`),
a narração e a trilha, e exporta `video.mp4` (1080×1920, 30 fps, −14 LUFS) + `capa.jpg`.

Antes de escrever, **abra os exemplos** em `motor/exemplos/` — eles reproduzem os posts que já estão no ar:
- `tradutor.html` — formato "Tradutor de indicação" (cards "o que dizem" → card brasa "tradução" + emoji)
- `relogio-catalogo.html` — relógio correndo, celular com catálogo, carimbos sincronizados com a fala, legenda automática
- `carrossel-cupom-e-humores.html` — cupom (recibo) e pílulas de humor, em modo imagens (carrossel/Stories)

## Fluxo
1. `narracao.txt` → `python scripts/narrar.py <pasta>` gera `narracao.mp3` + `narracao.json` (tempo de cada palavra).
2. Escreva `cena.html` usando `@palavra` para sincronizar com a fala.
3. Confira quadros soltos: `python scripts/renderizar.py <pasta> --previa 4.2` → `previa.jpg` (abra a imagem e olhe!).
4. Renderize: `python scripts/renderizar.py <pasta>` (vídeo longo do YouTube: `--formato 16x9`).
5. Carrossel/Stories: cada `<section class="quadro">` vira um JPEG:
   `python scripts/renderizar.py <pasta> --imagens --formato 4x5` (carrossel) ou `--formato 9x16` (Stories).

## Tempo (atributos)
| Atributo | O que faz |
|---|---|
| `data-in="2.4"` / `"@rapidinho"` / `"@ja#2"` / `"@nove+0.3"` / `"@fim"` | quando aparece (segundos, ou a palavra da fala; `#2` = 2ª ocorrência; `+0.3` = atraso) |
| `data-out="..."` | quando some (mesmo formato) |
| `data-anim="pop\|sobe\|desce\|fade\|esquerda\|direita\|carimbo\|zoom\|nada"` | entrada (padrão: pop) |
| `data-loop="treme\|pulsa\|flutua\|pisca\|gira"` | movimento enquanto está na tela |
| `data-dur="0.45"` | duração da entrada / da contagem |
| `data-conta="0>217"` (+ `data-sufixo=" min"`) | número contando |
| `data-enche="0>0.8"` | barra enchendo (`.barra .enche`, `.medidor .enche`) |
| `data-rola="0>900"` | catálogo rolando dentro do `.celular` |
| `data-hora="21:00>23:14"` | relógio avançando |
| `data-anima-em="3"` | o elemento aparece em `data-in`, mas a contagem/relógio só começa aqui |
| `data-digita` | texto aparece letra a letra |
| `data-som="pop\|carimbo\|whoosh\|tick\|ding\|virada\|digita"` (+ `data-som-vol="0.6"`) | efeito sonoro na entrada |
| `<section class="cena" data-in data-out>` | troca de tela inteira (filhos herdam o início) |

No `<body>`:
- `data-legenda="auto"` — legenda grande sincronizada com a fala, em caixa-alta (como em "Selvagens do Sofá" e "Qual é você?").
  `data-destaque="ali,netflix,sofa"` = palavras em brasa (sem lista: a palavra mais longa de cada grupo).
  `data-legenda-palavras="3"`, `data-legenda-top="1300"`. Numa cena com `data-legenda="off"` a legenda some.
- `data-duracao="37.3"` (padrão: fim da fala + 1,8 s) · `data-capa="6.5"` (quadro da capa) · `data-trilha="0.42"` (volume da trilha antes do ducking).
- `class="preto"` — fundo preto (cenas de vinheta, ex.: "A natureza é cruel.").

## Componentes (classes)
**Estrutura:** `.cena` (tela; `.centro` centraliza; `.topo-livre` começa abaixo do cabeçalho) · `.abs` · `.linha` · `.col` · `.esp-s/.esp-m/.esp-g`
**Texto:** `.titulo` · `.titulo-g` · `.frase` · `.frase-p` · `.apoio` · `.rotulo` · `.rotulo-p` · `.serif` (Instrument itálico) · `.caixa` (caixa-alta) · `.b`/`.brasa` · `.m` (cor do humor via `--mood`) · `.cinza`
**Emoji:** `.emoji` (200px) · `.emoji-m` · `.emoji-p` (dentro do texto)
**Cabeçalho de série:** `<div class="topo"><div class="serie">Selvagens do sofá <span class="ep">· ep. 01</span></div><div class="arroba">@seriecerta</div></div>`
  com passos: `<div class="serie sem-ponto">qual é você? <span class="passos"><i class="on"></i><i></i><i></i><i></i></span></div>`
**Relógio:** `<div class="relogio"><div class="dia">quarta-feira</div><div class="hora" data-hora="21:00>23:12">21:00</div></div>` (`.hora.alerta` = brasa)
**Cards:** `.card` (+ `.inclina-e`/`.inclina-d`, `.brasa-bg`, `.contorno`; texto grande em `.grande`) · `.seta` (↓ brasa) · `.par` (pílula "quem indica → a verdade")
**Cupom/recibo:** `.cupom` com `.item` (`<span>rótulo</span><b>valor</b>`), `<hr>`, `.rodape`
**Humores:** `.pilulas` > `.pilula style="--c:var(--sono)"` (cores: `--sono --ansioso --romantico --triste --animado --estressado --curioso --feliz`)
**Chamada final:** `.botao` (brasa) + `.arroba-final`
**Carimbo:** `.carimbo` (use `data-anim="carimbo" data-som="carimbo"`) · **Chip:** `.chip`, `.chip.escuro`, `.chip.azul`
**Barras:** `.barra` (`.nome`, `.trilho > .enche style="--c:..."`, `.valor`; `.alerta`) · `.medidor` (barra de rodapé, ex.: temperatura da comida)
**Celular:** `.celular` > `.app` + `.catalogo` (grade de `<i style="--c1:..;--c2:..">`) ou `.lista` (itens `.it > i + span`)
**Chat:** `.chat` > `.cab` + `.msg` (`.eu`, `.caixa-alta`, `<small>nome</small>`)
**Comentário:** `.campo` com `<small>você · agora</small>` + texto `data-digita` + `<span class="cursor" data-loop="pisca">`
**Número:** `.numero` (`<small>min</small>`) · **Tipos:** `.tipos > .tipo style="--c:.."` (`.n`, `.t`, `.sel`)
**Documentário:** `.binoculo`, `.registro` (`.rotulo-p` + `<b>ESPÉCIE:</b> ...`) · **Perigo:** `.fita > span` · **Confete:** `.confete > i`

Pode criar estilos próprios num `<style>` dentro do `cena.html` quando a ideia pedir (o renderizador inclui).

## Regras de ouro (tiradas dos posts que funcionaram)
- Uma ideia por tela. Cada frase da MIA troca ou acrescenta algo visual — nada fica parado mais de ~2,5 s.
- Topo seguro: nada importante acima de 130 px nem abaixo de 1650 px (interface do Instagram).
- Sem logos ou nomes de streaming na arte (use cards e ícones genéricos); pôster só se o Bruno colocar em `assets/posters/`.
- Final sempre com pergunta para comentar + `.botao` ("SEGUE PRA VER A PARTE 2" ou "SEGUE PRA NÃO PERDER") + `@seriecerta`.
- Depois de renderizar, gere 3 prévias (início, meio, fim) e olhe. Texto cortado, sobreposição ou tela vazia = corrigir antes de seguir.
