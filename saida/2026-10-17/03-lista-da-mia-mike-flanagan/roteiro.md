# Roteiro: 03-lista-da-mia-mike-flanagan

- **Formato:** Lista da MIA, YouTube 16:9 (1920×1080), narração MIA (eleven_v3), um só texto. Base: `motor/exemplos/lista-da-mia-16x9.html` (`<body class="paisagem" data-legenda="auto" style="--mood:var(--estressado)">`, `.serie-card` com `.capa > img`, `.metas`, `.porque`, `.nao-e`, `.progresso` de 5; `data-legenda="off"` nas telas de série). Render com `--formato 16x9`.
- **Publicação:** YouTube `2026-10-17T12:00:00-03:00` (3º na fila de narração).
- **Pilar:** 1. Série pro seu humor (humor "quero medo bom no fim de semana") · **Eixo:** criador/diretor · **Job:** principal (secundário: emocional 3, quem terminou *Carrie*).
- **CTA único (Consideração):** "Salva esse vídeo pra hoje à noite." "Onde assistir tá no comentário fixado" é informação, não pedido. **Sem pergunta pros comentários** (decisão da pauta, como 14 a 16/10). Botão final: **SALVA PRA HOJE À NOITE** + linha "onde assistir: comentário fixado".
- **Tamanho:** 220 palavras, **1.355 caracteres** (contando quebras de linha). Cerca de 1 min 30 s a 1 min 40 s de fala.
- **Corte previsto (pauta):** se o saldo ficar entre ~1.150 e ~1.355, tire o bloco do nº 5 (*O Clube da Meia-Noite*, 210 caracteres) e troque "mais cinco séries" → "mais quatro séries" e "Cinco séries pra chegar" → "Quatro séries pra chegar" (fica ~1.140). Título passa a "4 séries" e a `.progresso` a 4.
- **Título (≤ 70):** Carrie é do Mike Flanagan: 5 séries dele pra ver até o Halloween (64 caracteres)
- **Thumb (`thumb/cena.html`, modelo `lista-da-mia-thumb.html`):** "5" gigante + "SÉRIES DO MIKE FLANAGAN" + 🕯️ (ou o pôster de *Residência Hill*, nº 1, numa `.capa`: não tem logo).

## Fonte da tendência
- *Carrie* (Prime Video, criação/showrunner de Mike Flanagan, 8 episódios, todos em 07/10/2026) estreou em **nº 1 do ranking global de séries originais do Prime Video** na semana de 5 a 11/10 ([Selectra](https://selectra.co.uk/tv-broadband/news/prime-video-top-10-carrie-number-one-first-week-kill-jackie); [GameOverDrive, 8 episódios de uma vez](https://gameoverdrive.com.br/carrie-serie-mike-flanagan-estreia-prime-video/); [Omelete](https://www.omelete.com.br/series-tv/carrie-a-estranha-mike-flanagan-primeiras-impressoes)). Outubro = mês do Halloween nos streamings (sinais 2 e 3 da pauta).
- **Na fala:** só "Carrie, no Prime Video". Ranking **não** é dito (economia de caracteres e nada de "mais vista do Brasil").
- **Onde assistir *Carrie* hoje:** JustWatch BR (17/10) → *Carrie: A Estranha* (série 2026) no Amazon Prime Video. TVmaze #45562: 8 episódios.

## Pôsteres (`scripts/posters.py`, TVmaze; conferidos com Read numa folha única em 17/10)
| Arquivo | TVmaze | Estreia | Uso | Observação para a fase 2 |
|---|---|---|---|---|
| `imagens/carrie.jpg` | Carrie #45562 (`--id`, a série, não o filme) | 2026-10-07 | abertura (gancho) | Summer H. Howell com tiara, título "CARRIE"; sem logo visível |
| `imagens/the-midnight-club.jpg` | The Midnight Club #47855 | 2022-10-07 | nº 5 | **rodapé "OCT 7 · NETFLIX" → cortar** (`object-position: top`) |
| `imagens/the-haunting-of-bly-manor.jpg` | The Haunting of Bly Manor #49673 | 2020-10-09 | nº 4 | **rodapé "THIS FALL · NETFLIX" → cortar** |
| `imagens/the-fall-of-the-house-of-usher.jpg` | The Fall of the House of Usher #58166 | 2023-10-12 | nº 3 | sem logo |
| `imagens/midnight-mass.jpg` | Midnight Mass #42840 | 2021-09-24 | nº 2 | **rodapé "SEPT 24 · NETFLIX" → cortar** |
| `imagens/the-haunting-of-hill-house.jpg` | The Haunting of Hill House #29191 | 2018-10-12 | nº 1 + thumb | sem logo |

## Cenas

| Bloco (~tempo) | Fala da MIA (resumo; integral em `narracao.txt`) | Tela | Efeitos |
|---|---|---|---|
| 0:00–0:04 Gancho | "Sabe aquele medo que dá vontade de chorar junto?" | 😢 + 👻 grandes, "medo que dá vontade de **CHORAR JUNTO**" | `whoosh`; legenda auto |
| 0:04–0:09 Tendência | "Se você terminou Carrie, no Prime Video, você conheceu o Mike Flanagan." | pôster de *Carrie* (`.capa`) + chip "Prime Video" + nome **MIKE FLANAGAN** entrando em brasa | `pop` no nome. Nada da trama. |
| 0:09–0:14 Promessa | "E ele tem mais cinco séries te esperando. Todas na Netflix. Sem spoiler." | **5** gigante com carimbo + "séries do Flanagan" + chips "todas na Netflix" · "🚫 spoiler: 0" | `carimbo` no 5 |
| ~0:14 nº 5 | O Clube da Meia-Noite | `.serie-card`: capa + "nº 5 de 5" + h2 + `.metas` [Netflix · 1 temporada · 10 episódios] + `.porque` "jovens contando **histórias de terror à meia-noite**" 🕛 + `.nao-e` "quem odeia ficar sem continuação: foi cancelada" | `progresso` 1/5; `data-legenda="off"` |
| ~0:27 nº 4 | A Maldição da Mansão Bly | metas [Netflix · 1 temporada · 9 episódios] + porque "fantasma que, no fundo, é **uma história de amor**" 🥀 + nao-e "quem quer susto toda hora: é mais melancólica" | progresso 2/5 |
| ~0:40 nº 3 | A Queda da Casa de Usher | metas [Netflix · minissérie · 8 episódios · inspirada em Edgar Allan Poe] + porque "uma família rica **pagando caro** pelas próprias escolhas" 🍷 + nao-e "quem não aguenta sangue" | progresso 3/5 |
| ~0:52 nº 2 | Missa da Meia-Noite | metas [Netflix · minissérie · 7 episódios] + porque "ilha pequena, padre novo e **milagres que ninguém explica**" 🕯️ + nao-e "quem quer ritmo rápido: o terror é conversado" | progresso 4/5 |
| ~1:05 nº 1 | A Maldição da Residência Hill | metas [Netflix · 1 temporada · 10 episódios] + porque "terror e **luto de família** no mesmo episódio" 🏚️ + chip "a série que define o Flanagan" + nao-e "quem quer susto sem drama: aqui o drama pesa" | progresso 5/5; `virada` + `carimbo` "Nº 1" |
| ~1:20 Fecho | "Cinco séries pra chegar no Halloween com o medo certo. Salva esse vídeo…" | grade com as 5 capas + "até o **HALLOWEEN**" 🎃 → botão brasa **SALVA PRA HOJE À NOITE** + "onde assistir: comentário fixado" + @seriecerta | `ding`; 2 s parado |

- **Capítulos da descrição:** calcular na fase 2 pelo `narracao.json` + 0,30 s.
- Fase 2: `.esp-*` só como `<div>` vazio (APRENDIZADOS 15/10). Títulos na tela com o nome da Netflix BR (*Mansão Bly*, *Residência Hill*), não os do JustWatch (que usa "Bly Manor"/"Hill House").

## Descrição YouTube (rascunho; capítulos na fase 2)
Terminou Carrie no Prime Video? Então você conheceu o Mike Flanagan. Aqui estão as 5 séries dele na Netflix pra ver até o Halloween, sem spoiler.
00:00 Abertura · nº 5 O Clube da Meia-Noite · nº 4 A Maldição da Mansão Bly · nº 3 A Queda da Casa de Usher · nº 2 Missa da Meia-Noite · nº 1 A Maldição da Residência Hill
Descubra a série certa pro seu humor: https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-17-lista-da-mia-mike-flanagan
- **Tags:** mike flanagan, carrie, carrie a estranha, residência hill, mansão bly, missa da meia-noite, casa de usher, clube da meia-noite, séries de terror, halloween
- **Comentário fixado:** "Onde assistir: O Clube da Meia-Noite, A Maldição da Mansão Bly, A Queda da Casa de Usher, Missa da Meia-Noite e A Maldição da Residência Hill estão na Netflix. Carrie está no Prime Video."
- **`"series"`:** ["Carrie, a Estranha", "O Clube da Meia-Noite", "A Maldição da Mansão Bly", "A Queda da Casa de Usher", "Missa da Meia-Noite", "A Maldição da Residência Hill"] (*Carrie* entra porque o pôster aparece na abertura)

## Verificação de fatos (2026-10-17)
**Onde assistir — JustWatch BR**, consultado hoje pela API `apis.justwatch.com/graphql` (país BR; o site e a Netflix seguem bloqueados no WebFetch). Todas aparecem em assinatura **Netflix** (padrão e com anúncios), 1 temporada cada. Episódios: JustWatch BR (temporada 1) e TVmaze, que batem.

| Série | Netflix BR hoje | Temporadas / episódios | Fontes extras |
|---|---|---|---|
| O Clube da Meia-Noite (2022) | ✓ JustWatch BR | 1 / 10; cancelada pela Netflix | TVmaze #47855 (10, Ended); [Critical Hits, cancelamento](https://criticalhits.com.br/cinema-e-tv/netflix-cancela-o-clube-da-meia-noite-depois-de-apenas-uma-temporada/); [AdoroCinema](https://www.adorocinema.com/series/serie-26550/) |
| A Maldição da Mansão Bly (2020) | ✓ JustWatch BR | 1 / 9 | TVmaze #49673 (9); página da Netflix BR na busca (2020, 9 episódios, "romance gótico") ([netflix.com/br](https://www.netflix.com/br/title/81237854)); [AdoroCinema, crítica](https://www.adorocinema.com/noticias/filmes/noticia-156227/) |
| A Queda da Casa de Usher (2023) | ✓ JustWatch BR | minissérie / 8, baseada em Edgar Allan Poe | TVmaze #58166 (8); [AdoroCinema](https://www.adorocinema.com/series/serie-30301/); [Netflix, anúncio](https://about.netflix.com/news/netflix-and-intrepid-pictures-announce-new-limited-series-the-fall-of-the) |
| Missa da Meia-Noite (2021) | ✓ JustWatch BR, **pendência de 15/10 resolvida** | minissérie / 7 | TVmaze #42840 (7, Ended); [AdoroCinema](https://www.adorocinema.com/series/serie-25310/) |
| A Maldição da Residência Hill (2018) | ✓ JustWatch BR (também confirmada pelo revisor em 16/10) | 1 / 10 | TVmaze #29191 (10); [AdoroCinema](https://www.adorocinema.com/series/serie-21978/) |

- "Todas na Netflix" na fala = as cinco da contagem (*Carrie* é dita "no Prime Video").
- **Premissas usadas (oficiais, sem spoiler):** jovens que se reúnem à meia-noite pra contar histórias de terror (Clube); fantasma com romance gótico (Bly); família rica dona de farmacêutica (Usher: "pagando caro pelas próprias escolhas" é o tom de Poe, sem evento); ilha isolada + chegada de um padre carismático + acontecimentos "milagrosos" (Missa, sinopse do AdoroCinema); família marcada pela casa (Hill). "Ela foi cancelada" (Clube) é fato de produção, não de trama.
- **Não citados:** duração de episódio, ranking no Brasil, projetos futuros do Flanagan, nada da trama de *Carrie* (nem o baile).
- O revisor pode reconferir no app, mas nenhum item depende mais dele.

## Checagem de regras
- Spoiler zero. Pra quem não é em todas as 5. Um CTA (salvar). Sem pergunta pros comentários.
- Sem logo de streaming na arte (rodapés de Clube, Bly e Missa cortados na fase 2).
- Repetição 30 dias: *Carrie* só como gancho; *Residência Hill* como nº 1 com eixo e gancho novos (pauta); demais inéditas em Lista.
