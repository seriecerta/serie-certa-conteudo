# Roteiro: 03-lista-da-mia-a-diplomata-thrillers-politicos

- **Formato:** Lista da MIA, YouTube 16:9 (1920×1080), narração MIA (eleven_v3), um só texto. Base: `motor/exemplos/lista-da-mia-16x9.html` (`<body class="paisagem" data-legenda="auto" style="--mood:var(--estressado)">`, `.serie-card` com `.capa > img`, `.metas`, `.porque`, `.nao-e`, `.progresso` de 4; `data-legenda="off"` nas telas de série). Render com `--formato 16x9`.
- **Publicação:** YouTube 2026-10-16T12:00:00-03:00 (3º na fila de narração).
- **Pilar:** 1. Série pro seu humor (humor "quero tensão política no fim de semana") · **Eixo:** gênero/subgênero com gancho de estreia · **Job:** principal (secundário: emocional 3, quem maratonar a T4).
- **CTA único (Consideração):** "Salva esse vídeo pra hoje à noite." "Onde assistir tá no comentário fixado" é informação, não pedido. **Sem pergunta pros comentários** (decisão da pauta, como 14 e 15/10). Botão final: **SALVA PRA HOJE À NOITE** + linha "onde assistir: comentário fixado".
- **Tamanho:** 217 palavras, **1.339 caracteres**, cerca de 1 min 25 s a 1 min 35 s de fala.
- **Título (≤ 70):** A Diplomata voltou: 4 thrillers políticos pro seu fim de semana (63 caracteres)
- **Thumb (`thumb/cena.html`, modelo `lista-da-mia-thumb.html`):** "4" gigante + "DEPOIS DE A DIPLOMATA" + 🕵️ (ou o pôster de *Dia Zero*, nº 1, numa `.capa`; não tem logo).

## Fonte da tendência (reconferida em 2026-10-16)
- *A Diplomata* T4 chegou à Netflix na **quinta, 15/10/2026, com 8 episódios de uma vez** ([Omelete](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data); [GameOverDrive, episódios](https://gameoverdrive.com.br/a-diplomata-4-temporada-quantos-episodios/); [GameOverDrive, estreia nesta quinta](https://gameoverdrive.com.br/a-diplomata-4-temporada-horario-estreia-netflix/)). Fala: "voltou esta semana, com os oito episódios de uma vez".
- *Slow Horses* T6 termina na **quarta, 21/10** (sinal 2 da pauta, reconferido abaixo).
- **Não afirmado:** posição em Top 10 no Brasil (não confirmada).

## Pôsteres (`scripts/posters.py`, TVmaze, conferidos com Read em montagem)
| Arquivo | TVmaze | Estreia | Uso | Observação |
|---|---|---|---|---|
| `imagens/the-diplomat.jpg` | The Diplomat #60213 (`--id`) | 2023-04-20 | abertura (gancho) | pôster da T4 com Keri Russell; **cortar rodapé "ONLY ON NETFLIX"** (`object-position: top`) |
| `imagens/the-night-agent.jpg` | The Night Agent #56512 | 2023-03-23 | nº 4 | sem logo visível |
| `imagens/the-americans.jpg` | The Americans #157 | 2013-01-30 | nº 3 | série de 2013 (não confundir); sem logo |
| `imagens/slow-horses.jpg` | Slow Horses #45039 | 2022-04-01 | nº 2 | Gary Oldman, fundo claro; conferir rodapé na prévia |
| `imagens/zero-day.jpg` | Zero Day #65491 | 2025-02-20 | nº 1 + thumb | Read: De Niro, título "ZERO DAY"; sem logo |

## Cenas

| Bloco (~tempo) | Fala da MIA (resumo; integral em `narracao.txt`) | Tela | Efeitos |
|---|---|---|---|
| 0:00–0:06 Gancho | "Sabe aquela tensão boa de série política, que você jura que é só mais um episódio?" | 🕵️ grande + "só mais **UM** episódio" → contador "episódios: 1 → 2 → 3" | `whoosh`; legenda auto |
| 0:06–0:10 Tendência | "A Diplomata voltou esta semana, com os oito episódios de uma vez." | pôster de *A Diplomata* (`.capa`) + chip "voltou esta semana" + chip "8 episódios de uma vez" | `pop` nos chips. Nada da trama. |
| 0:10–0:15 Promessa | "Pra quando acabar, eu separei quatro séries com essa mesma tensão. Sem spoiler." | **4** gigante com carimbo + "thrillers políticos pro fim de semana" + chip "🚫 spoiler: 0" | `carimbo` no 4 |
| ~0:15 nº 4 | O Agente Noturno | `.serie-card`: capa + "nº 4 de 4" + h2 + `.metas` [Netflix · 3 temporadas] + `.porque` "um telefone secreto da Casa Branca e **tudo vira conspiração**" + `.nao-e` "quem quer só política de bastidor: aqui é ação" ☎️ | `progresso` 1/4; `data-legenda="off"` |
| ~0:28 nº 3 | The Americans | metas [Disney+ · 6 temporadas · série encerrada] + porque "espiões fingindo ser **uma família comum**" + chip-ponte "Keri Russell → a própria diplomata" + nao-e "quem quer ritmo rápido: essa cozinha devagar" | progresso 2/4; seta do chip-ponte até a miniatura de *A Diplomata* |
| ~0:45 nº 2 | Slow Horses | metas [Apple TV · 6 temporadas · a 6ª termina qua, 21/10] + porque "espiões rejeitados, chefe insuportável e **humor ácido**" + nao-e "quem não aguenta chefe grosseiro 😤" | progresso 3/4 |
| ~1:00 nº 1 | Dia Zero | metas [Netflix · minissérie · 6 episódios · com Robert De Niro] + porque "um ex-presidente investiga **um ataque hacker**" + chip "dá pra fechar até domingo" + nao-e "quem quer série pra continuar: essa termina ali" | progresso 4/4; `virada` + `carimbo` "Nº 1" |
| ~1:20 Fecho | "Quatro séries pra quem gosta de tensão no fim de semana. Salva esse vídeo…" | grade com as 4 capas + "tensão de **FIM DE SEMANA**" 🛋️ → botão brasa **SALVA PRA HOJE À NOITE** + "onde assistir: comentário fixado" + @seriecerta | `ding`; 2 s parado |

- **Capítulos da descrição:** calcular na fase 2 pelo `narracao.json` + 0,30 s.
- Fase 2: `.esp-*` só como `<div>` vazio (APRENDIZADOS 15/10).

## Descrição YouTube (rascunho; capítulos na fase 2)
A Diplomata voltou esta semana com os 8 episódios de uma vez. Pra quando acabar, 4 thrillers políticos com a mesma tensão, sem spoiler.
00:00 Abertura · nº 4 O Agente Noturno · nº 3 The Americans · nº 2 Slow Horses · nº 1 Dia Zero
Descubra a série certa pro seu humor: https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-16-lista-da-mia-a-diplomata-thrillers-politicos
- **Tags:** a diplomata, the diplomat, keri russell, thriller político, séries de espionagem, o agente noturno, the americans, slow horses, dia zero, robert de niro
- **Comentário fixado:** "Onde assistir: O Agente Noturno (Netflix) · The Americans (Disney+) · Slow Horses (Apple TV) · Dia Zero (Netflix)."
- **`"series"`:** ["A Diplomata", "O Agente Noturno", "The Americans", "Slow Horses", "Dia Zero"] (A Diplomata entra porque o pôster aparece na abertura)

## Verificação de fatos (WebSearch, 2026-10-16)
- **O Agente Noturno:** Netflix; a 3ª temporada saiu inteira em 19/02/2026 ([Einerd](https://www.einerd.com/o-agente-noturno-saiba-o-horario-exato-da-estreia-da-3a-temporada-na-netflix/); [Rolling Stone Brasil](https://rollingstone.com.br/tv/3a-temporada-de-o-agente-noturno-estreia-no-streaming/); [Olhar Digital, 16/02/2026](https://olhardigital.com.br/2026/02/16/cinema-e-streaming/netflix-lancamentos-da-semana-16-a-22-de-fevereiro/)). Nenhuma 4ª temporada nas fontes: **não citada**. "Três temporadas" = as lançadas.
- **The Americans:** 6 temporadas, 75 episódios, série encerrada; AdoroCinema e JustWatch BR apontam Disney+ ([JustWatch BR](https://www.justwatch.com/br/serie/the-americans/temporada-1); [AdoroCinema](https://www.adorocinema.com/series/serie-10790/)). Keri Russell protagoniza as duas séries. ⚠️ **Fontes sem data de 2026 e sem confirmação explícita de todas as temporadas no Disney+ Brasil → revisor confere no app.** Se não estiver, reserva: *Designated Survivor* (Netflix, 3 temporadas; também só com confirmação no app) — refazer o bloco do nº 3 antes de narrar.
- **Slow Horses:** Apple TV; T6 com 6 episódios semanais desde 16/09, **final na quarta, 21/10/2026** ([GameOverDrive](https://gameoverdrive.com.br/slow-horses-6-temporada-data-episodios-elenco-livros/); [Diário do Nordeste](https://diariodonordeste.verdesmares.com.br/verso/slow-horses-lanca-primeiro-episodio-da-6-temporada-veja-livros-que-inspiraram-serie-1.3792012); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/slow-horses-ganha-data-de-estreia-para-a-6a-temporada-e-apresenta-novo-ator-do-elenco/); [Grazia](https://graziadaily.co.uk/life/tv-and-film/slow-horses-season-six-release-date-episode-schedule/)). Renovação para a 7ª ([Omelete](https://www.omelete.com.br/apple-tv/slow-horses-renovada-apple-tv-7a-temporada)) **não citada**. Nada da trama da T6.
- **Dia Zero:** Netflix, minissérie de 6 episódios, estreia 20/02/2025, Robert De Niro como ex-presidente que investiga um ataque cibernético ([Rolling Stone Brasil](https://rollingstone.com.br/cinema/conheca-dia-zero-nova-minisserie-da-netflix-estrelada-por-robert-de-niro/); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000131048/); [Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/dia-zero-robert-de-niro-estreia-na-netflix/)). Sem 2ª temporada anunciada. Duração de episódio **não citada**. ⚠️ Catálogo 2026 sem fonte datada (original Netflix, risco baixo) → revisor confere no app.
- **A Diplomata:** só gancho (fontes na tendência). Nada da T3/T4.

## Checagem de regras
- Spoiler zero: só premissas oficiais; nenhum evento de temporada citado.
- Pra quem não é em todas as 4. Um CTA (salvar). Sem pergunta pros comentários.
- Sem logo de streaming na arte (rodapé de *A Diplomata* cortado).
- Repetição 30 dias: *A Diplomata* só como gancho; nº 1 (*Dia Zero*) inédito em Lista.
