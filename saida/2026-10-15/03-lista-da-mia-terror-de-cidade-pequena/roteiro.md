# Roteiro: 03-lista-da-mia-terror-de-cidade-pequena

- **Formato:** Lista da MIA, YouTube 16:9 (1920×1080), narração MIA (eleven_v3), um só texto. Base: `motor/exemplos/lista-da-mia-16x9.html` (`<body class="paisagem" data-legenda="auto" style="--mood:var(--estressado)">`, `.serie-card` com `.capa > img`, `.metas`, `.porque`, `.nao-e`, `.progresso` de 4; `data-legenda="off"` nas telas de série). Render com `--formato 16x9`.
- **Pilar:** 1. Série pro seu humor (humor "com vontade de medo"; tema puxado pela tendência) · **Eixo:** gênero/subgênero · **Job:** principal.
- **Humor / mood:** estressado (`--estressado`).
- **Tamanho:** 283 palavras, 1.716 caracteres, cerca de 1 min 55 s a 2 min 05 s de fala.
- **CTA único (Consideração):** "Salva esse vídeo pra hoje à noite." O "onde assistir tá no comentário fixado" é informação, não pedido. **Sem pergunta pros comentários** (decisão da pauta, regra 6). Botão final: "SALVA PRA HOJE À NOITE"; linha de apoio "onde assistir: comentário fixado".
- **Título (≤ 70):** Profundezas e mais 3 séries de terror de cidade pequena (55 caracteres)
- **Thumb (`thumb/cena.html`, modelo `lista-da-mia-thumb.html`):** "4" gigante + "TERROR DE CIDADE PEQUENA" + 🌊. Se usar pôster, o de *Profundezas* (`imagens/below.jpg`, não tem logo de streaming).

## Fonte da tendência (reconferida em 2026-10-15)
- **Confirmado hoje:** *Profundezas* (*Below*) chegou ao 1º lugar entre as séries mais populares da Netflix **no mundo** dois dias depois da estreia ([Einerd](https://www.einerd.com/profundezas-below-serie-terror-netflix/)); 17 milhões de visualizações em 5–11/10, segundo a pauta ([A Tarde](https://atarde.com.br/cineinsite/minisserie-da-netflix-bate-recorde-mundial-com-17-milhoes-de-views-1405738); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000227377/)).
- **Não reconfirmado hoje:** o 1º lugar **no Brasil** em 5–11/10 (a pauta cita [Revista Bula](https://www.revistabula.com/169299-5-series-mais-vistas-netflix-brasil-outubro-2026/) e [Oficina da Net](https://www.oficinadanet.com.br/lancamentos-netflix/73295-essa-serie-lidera-top-10-semana-netflix-veja-trailer); a busca de hoje não trouxe o ranking brasileiro). **Por isso a fala diz "chegou ao topo da Netflix no mundo"**, não "liderou no Brasil". Na tela: "nº 1 da Netflix no mundo" (sem número de views).
- Conversa: crítica e "final explicado" na Omelete ([crítica](https://www.omelete.com.br/series-tv/criticas/profundezas-boa-serie-netflix-critica)), comparação com *Stranger Things* ([AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000215824/)), mês do Halloween.

## Troca em relação à pauta
- **Nº 3: *Missa da Meia-Noite* saiu, entrou a reserva *Carrie, a Estranha*.** Motivo: nenhuma fonte de 2026 confirma *Missa da Meia-Noite* no catálogo da Netflix Brasil (só páginas de 2021–2022 e listas sem data). Regra 2/8: não afirmar. *Carrie* tem fontes de outubro/2026 (Prime Video, 8 episódios, 07/10) e pôster.
- **Repetição (30 dias):** *Carrie* saiu em 13/10 (Short Tradutor, humor "órfã de terror", gancho Residência Hill) e entra hoje no carrossel (humor "medo", gancho "quinta de estreia"). Aqui o gancho é outro (cidade pequena / Profundezas). Série + humor + gancho não se repetem juntos, mas é a 2ª peça do dia com Carrie: **o revisor decide**; se vetar, a reserva 2 da pauta (*Hotel Assombrado*) não serve (tom de comédia, e só T1 confirmada), então a Lista fica com 3 séries (corta-se o bloco do nº 3 da narração antes de narrar).

## Pôsteres (`scripts/posters.py`, TVmaze, conferidos visualmente)
| Arquivo | TVmaze | Estreia | Uso | Observação |
|---|---|---|---|---|
| `imagens/below.jpg` | Below #93115 (via `--id`) | 2026-10-08 (canal Netflix) | nº 1 + abertura + thumb | Josh Hartnett no barco; sem logo |
| `imagens/stranger-things.jpg` | Stranger Things #2993 | 2016-07-15 | nº 2 | pôster da T5; **logo Netflix e datas no rodapé** → cortar com `object-position: top` |
| `imagens/carrie.jpg` | Carrie #45562 | 2026-10-07 | nº 3 | série de 2026 (não é filme nem remake de 2002); sem logo |
| `imagens/it-welcome-to-derry.jpg` | IT: Welcome to Derry #61324 | 2025-10-26 | nº 4 | sem logo |
- `midnight-mass.jpg` foi baixado e apagado (série trocada).

## Cenas

| Bloco (~tempo) | Fala da MIA (resumo; texto integral em `narracao.txt`) | Tela | Efeitos |
|---|---|---|---|
| 0:00–0:06 Gancho | "Sabe aquele medo que começa quando a cidade é pequena demais pra alguém fugir?" | placa de estrada "BEM-VINDO · população: 312" (genérica) + emoji 🏚️ → "pequena demais pra **FUGIR**" | `whoosh`; carimbo em "FUGIR". Legenda auto. |
| 0:06–0:12 Tendência | "Profundezas chegou ao topo da Netflix no mundo. E quem terminou tá procurando o próximo arrepio." | pôster de *Profundezas* (`.capa`) + chip "nº 1 da Netflix no mundo" → "o próximo **ARREPIO**" 🥶 | `pop` no chip. |
| 0:12–0:18 Promessa | "Então eu separei quatro séries… Sem spoiler nenhum. Do número quatro ao número um." | **4** gigante com carimbo + "séries de terror de cidade pequena" + chip "🚫 spoiler: 0" | `carimbo` no 4. |
| ~0:18 nº 4 | IT: Bem-vindos a Derry | `.serie-card`: capa + "nº 4 de 4" + h2 + `.metas` [HBO Max · 1 temporada · 8 episódios · 2ª confirmada] + `.porque` "um **medo antigo** que a cidade inteira finge não ver" + `.nao-e` "quem não aguenta violência explícita (nem palhaço 🎈)" | `progresso` 1/4. `data-legenda="off"`. |
| ~0:42 nº 3 | Carrie, a Estranha | metas [Prime Video · 8 episódios · todos disponíveis · de Mike Flanagan] + porque "o terror é **o olhar dos outros**" + nao-e "quem não quer terror adolescente pesado hoje" | progresso 2/4. |
| ~1:02 nº 2 | Stranger Things | metas [Netflix · 5 temporadas · série encerrada] + porque "cidadezinha, um sumiço e **amizade no meio do medo**" + chip-ponte "Charlie Heaton → também em *Profundezas*" + nao-e "quem não quer começar 5 temporadas hoje" | progresso 3/4. Seta animada ligando o chip ao nº 1 (sem pôster de *Profundezas* ainda). |
| ~1:24 nº 1 | Profundezas | metas [Netflix · minissérie · 6 episódios · com Josh Hartnett] + porque "um pescador protegendo a família quando **algo vem do mar**" + chip "dá pra terminar no fim de semana" + nao-e "quem tem medo de mar 🌊" | progresso 4/4; `virada` + `carimbo` "Nº 1". Nada de descrever a criatura. |
| ~1:50 Fecho | "Quatro séries pra quem gosta de medo com CEP. Salva esse vídeo pra hoje à noite. Onde assistir…" | grade com as 4 capas + "medo com **CEP**" 📍 → botão brasa **SALVA PRA HOJE À NOITE** + "onde assistir: comentário fixado" + @seriecerta | `ding` no botão; 2 s parado. |

- **Capítulos da descrição:** calcular na fase 2 pelo `narracao.json` + 0,30 s (lição de 14/10).

## Descrição YouTube (rascunho; capítulos na fase 2)
Profundezas chegou ao topo da Netflix no mundo. Se você terminou e quer o próximo arrepio, aqui vão 4 séries de terror de cidade pequena, sem spoiler.
00:00 Abertura · nº 4 IT: Bem-vindos a Derry · nº 3 Carrie, a Estranha · nº 2 Stranger Things · nº 1 Profundezas
Descubra a série certa pro seu humor: https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-15-lista-da-mia-terror-de-cidade-pequena
- **Tags:** profundezas, below netflix, séries de terror, terror netflix, stranger things, carrie a estranha, it bem-vindos a derry, josh hartnett, halloween.
- **Comentário fixado:** "Onde assistir: IT: Bem-vindos a Derry (HBO Max) · Carrie, a Estranha (Prime Video) · Stranger Things (Netflix) · Profundezas (Netflix)."
- **`"series"`:** ["Profundezas", "Stranger Things", "Carrie, a Estranha", "IT: Bem-vindos a Derry"]

## Verificação de fatos (WebSearch, 2026-10-15; WebFetch segue bloqueado)
- **Profundezas:** Netflix, minissérie de 6 episódios, todos desde 08/10/2026, com Josh Hartnett, Mackenzie Davis e Charlie Heaton; pescador em Terra Nova, Canadá. [GameOverDrive, episódios](https://gameoverdrive.com.br/profundezas-episodios-duracao/), [GameOverDrive, elenco](https://gameoverdrive.com.br/profundezas-netflix-quando-estreia-episodios-elenco/), [Canaltech](https://canaltech.com.br/entretenimento/nova-serie-de-terror-da-netflix-tem-astro-de-stranger-things-e-monstro-marinho/). TVmaze: canal Netflix. Sem 2ª temporada anunciada (não citado). "Dá pra terminar num fim de semana" é opinião sobre 6 episódios; a duração (37–47 min, ~4 h) **não** é citada.
- **Stranger Things:** Netflix, 5 temporadas, encerrada (final em 31/12/2025). [Omelete, calendário da T5](https://www.omelete.com.br/series-tv/stranger-things-5-calendario-episodios-data-horario-netflix), [Times Brasil](https://timesbrasil.com.br/brasil/stranger-things-5-a-que-horas-estreia-o-episodio-final-na-netflix/). Charlie Heaton em ambas: [Canaltech](https://canaltech.com.br/entretenimento/nova-serie-de-terror-da-netflix-tem-astro-de-stranger-things-e-monstro-marinho/), [Einerd](https://www.einerd.com/profundezas-below-netflix-charlie-heaton/).
- **Carrie, a Estranha:** Prime Video, 8 episódios de uma vez em 07/10/2026, criada por Mike Flanagan. [TecMundo](https://www.tecmundo.com.br/minha-serie/604301-carrie-nova-adaptacao-do-prime-video-ganha-trailer-e-data-de-estreia.htm), [Omelete](https://www.omelete.com.br/series-tv/carrie-a-estranha-prime-video-mike-flanagan-data-lancamento-outubro), [Gazeta SP](https://www.gazetasp.com.br/entretenimento/carrie-a-estranha-ganha-nova-serie-de-terror-no-prime-video-veja-quando-estreia/). TVmaze: estreia 2026-10-07.
- **IT: Bem-vindos a Derry:** HBO Max, T1 com 8 episódios; 2ª temporada confirmada em 17/08/2026, sem data. [Diário do Nordeste](https://diariodonordeste.verdesmares.com.br/entretenimento/zoeira/it-bem-vindos-a-derry-e-renovada-para-2-temporada-pela-hbo-max-confira-as-novidades-1.3784767), [Omelete](https://www.omelete.com.br/series-tv/it-bem-vindos-a-derry-renovacao-2a-temporada-teaser), [Rolling Stone Brasil](https://rollingstone.com.br/entretenimento/tudo-o-que-sabemos-sobre-a-segunda-temporada-de-it-bem-vindos-a-derry/).
- **Para o revisor:** conferir no app que *IT: Bem-vindos a Derry* segue no HBO Max e *Carrie* no Prime Video; decidir sobre a 2ª aparição de *Carrie* no dia.

## Checagem de regras
- Spoiler zero: só premissas oficiais; nada do final de *Profundezas*, *Stranger Things* ou *IT*; a criatura não é descrita.
- Um CTA só (salvar). Pra quem não é em todas. Sem logo de streaming na arte (rodapé de *Stranger Things* cortado).
