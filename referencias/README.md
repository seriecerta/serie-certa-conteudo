# Referências — posts do @seriecerta que definem o padrão

**Todo vídeo novo deve parecer da mesma família destes.** Antes de escrever uma cena, abra a folha de quadros
(`quadros/<nome>.jpg`, um quadro a cada 1,5 s) do formato mais próximo e copie a lógica: ritmo, composição,
hierarquia de texto, uso de emoji, efeitos e o fecho. Para ver um instante exato:
`ffmpeg -ss 12 -i referencias/videos/<nome>.mp4 -frames:v 1 /tmp/q.jpg` e abra a imagem.

Os vídeos aqui são cópias leves (540×960) só para consulta. Telas em alta: `telas/`. Narrações originais da MIA: `narracoes/`.

## Padrão comum a todos
- 1080×1920, 30 fps, 30–50 s, −14 LUFS. Narração da MIA entra aos 0,30 s. Trilha "Sala Escura" com ducking + efeitos (pop, carimbo, virada).
- Fundo verde-noite com degradê e granulado. Inter Display Black. Creme (`#F1E8D6`) + **brasa** (`#FF5A36`) para a palavra-chave.
- **Uma ideia por tela**; algo muda a cada frase da MIA (2–3 s no máximo parado).
- Emoji grande como "personagem" da tela (😎 😩 💀 🫂 👀 😴 🙌).
- Interfaces genéricas desenhadas (celular, catálogo, chat, notificação, barra de progresso) — **nunca logo de streaming**.
- Contadores e placares para o absurdo ("TRAILERS 3 × EPISÓDIOS 0", "rolagens: 5", "série assistida: 0 min").
- Carimbos tortos em brasa para as viradas ("JÁ VI", "9 TEMPORADAS?!", "BLOQUEADA", "MUITO.").
- Fecho: pergunta para comentar (com 👇) + promessa de parte 2 + botão brasa ("SEGUE PRA VER A PARTE 2" / "SEGUE PRA NÃO PERDER") + `@seriecerta`.

## 1. `reels-1-almoco` — "Horário de almoço" (35,9 s · formato Relógio)
**Conceito:** a hora livre do almoço inteira gasta escolhendo série; a comida esfria.
**Estrutura:** rótulo "HORÁRIO DE ALMOÇO" + relógio 12:00 → "hora do almoço 🍽️ / **1 hora livre** / bora ver um episódio! 😋" → 12:05 "escolhendo a série…" com celular de catálogo + 🤔 → 12:20 "**AINDA** escolhendo." + chip "a comida esfriando 🥶" → 12:40 "**ACHEI!** 🙌" + botão "▶ DEI PLAY" → "abertura de **2 MINUTOS**" com barra de abertura 0:13/2:00 e 😮‍💨 → 12:58 "tá na hora da **REUNIÃO**" + notificação "📅 Reunião em 2 min" → cupom "RESUMO DO ALMOÇO" (comida **fria** ❄️ · episódio **só a abertura** · tempo livre 60 min · série assistida **0 min** · obrigada pela preferência 🙃) → "comenta 👇 qual série cabe no seu **ALMOÇO?** 🍽️+📺=🤝 · a mais votada vira LISTA AMANHÃ" + botão.
**Recurso-chave:** medidor de rodapé "🍲 temperatura da comida" que vai de QUENTE (brasa) → MORNA → FRIA (azul) ao longo do vídeo.

## 2. `reels-2-tradutor` — "Tradutor oficial de indicação de série" (30,4 s · formato Tradutor)
**Conceito:** o que as pessoas dizem quando indicam uma série × o que isso realmente significa.
**Estrutura:** "**TRADUTOR** OFICIAL de indicação de série" → cabeçalho fixo "🗣️ TRADUTOR DE INDICAÇÃO" + pílula "quem indica → **a verdade**" → 4 itens numerados (1/4…4/4): card escuro "O QUE DIZEM" com a frase entre aspas → seta brasa → card brasa "TRADUÇÃO" → emoji (😩 ⏳ 💀 🫂) → "😂 comenta outra **TRADUÇÃO** 👇 / as melhores entram na **PARTE 2**" + botão.
**Recurso-chave:** cards levemente inclinados em direções opostas; a tradução entra com pop/carimbo e som.
**Cena pronta:** `motor/exemplos/tradutor.html` (recriação fiel deste vídeo).

## 3. `quarta-21h-reels` — "Quarta, 21h" (37,3 s · formato Relógio)
Ficha de produção completa em `estrategia/09-identidade-visual-e-formatos.md`.
**Recurso-chave:** relógio correndo de 21:00 a 23:14; carimbos sobre o catálogo; virada meta "fui procurar indicação num vídeo curtinho… e tô aqui **ATÉ AGORA.** 👀 (sim, nesse aqui)"; final com 6 chips de humor.
**Cena de base:** `motor/exemplos/relogio-catalogo.html`.

## 4. `selvagens-do-sofa-ep01-final` — "Selvagens do Sofá · Ep. 01" (46,4 s · formato Documentário)
**Conceito:** documentário de natureza narrando o "brasileiro adulto" no habitat natural, o sofá.
**Estrutura:** "🤫 **SILÊNCIO.**" → binóculo (dois círculos) com 🧔 no sofá 🛋️ e celular + "REGISTRO DE CAMPO Nº 01 · ESPÉCIE: brasileiro adulto · HABITAT: o sofá." → celular com catálogo "ABRIU: Netflix" e chip "rolagens: 0→5" com 👆 rolando → 3 trailers com barras enchendo + placar "trailers vistos 3 / séries assistidas **0**" → dois celulares "ANTES / AGORA" + carimbo "MESMOS MOVIMENTOS" → binóculo com 🧐 "REGISTRO Nº 02 · COMPORTAMENTO: repetido · MOTIVO: desconhecido" → relógio analógico "12 min → 40 min depois" com 🍕 e termômetro esfriando → contagem regressiva "COMPORTAMENTO PREVISÍVEL EM… 3, 2, 1" → card de TV "THE OFFICE ▶ continuar assistindo" + "REPRISE Nº 11 → **12**" com confete → tela preta com serifa itálica "*A natureza é cruel.*" → "RESPONDE AÍ 👇" + campo de comentário digitando "já perdi a conta 😅" + "*eu não julgo.*" + carimbo "**MUITO.**"
**Recurso-chave:** cabeçalho de série fixo ("● SELVAGENS DO SOFÁ · EP. 01 … @seriecerta") + **legenda grande sincronizada com a fala** (2–3 palavras, palavra-chave em brasa) — use `data-legenda="auto"`.

## 5. `qual-e-voce-4-tipos` — "Os 4 tipos de pessoa escolhendo série" (50,6 s · formato Qual é você?)
**Conceito:** 4 perfis identificáveis; o público comenta o número com que se identifica.
**Estrutura:** "OS **4** TIPOS DE PESSOA ESCOLHENDO SÉRIE" com 4 cards coloridos (azul 😴 1, amarelo 🔁 2, verde 🙋 3, rosa 🤐 4) caindo → para cada tipo: número grande na cor + "A QUE DESISTE / superpoder: abrir 4 streamings em 2 min" + emoji no canto e um gag visual (barras "catálogo 20 min × série 0 min"; contador "217 → 1000 SÉRIES NOVAS"; card dourado "EP. 1 DE NOVO 🔁" + carimbo "7ª VEZ"; chat de grupo "família 🏠" com 40 respostas + carimbo "ASSISTIDAS: 0"; fita "⚠ PERIGO ⚠" + chat do spoiler + carimbo "🚫 BLOQUEADA") → grade final com os 4 tipos, "**QUAL É VOCÊ?** · COMENTA O NÚMERO 👇" e o card do número 3 destacado.
**Recurso-chave:** cabeçalho "QUAL É VOCÊ?" com 4 tracinhos de progresso que acendem na cor de cada tipo + legenda sincronizada.

## Como usar nas próximas peças
- Escolha o formato mais próximo da pauta e **reaproveite a estrutura**, trocando o tema (outro horário, outras traduções, novo episódio de Selvagens, novos 4 tipos).
- Séries recorrentes ganham número de episódio e parte 2 — mantenha a numeração em `historico/publicados.md`.
- Pode criar formatos novos, mas sempre com os elementos do "Padrão comum" acima.
