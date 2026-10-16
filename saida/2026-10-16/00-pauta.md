# Pauta: sexta-feira, 2026-10-16 (America/Sao_Paulo)

**Grade:** a diária de `08-cronograma.md`. Carrossel + Stories às 10h00 · Lista da MIA às 12h00 (YouTube 16:9) · Short + Reels às 13h30 · Reels às 18h30 · Short às 19h00.
**Meta dos 90 dias:** audiência, com orçamento zero (`05`). Reels, Shorts e casal fecham com "Manda pra quem precisa".
**Período de base (14–20/10):** grade fixa, sem teste A/B. Nenhuma peça leva `experimento` (registro de `10-experimentos.md` vazio).
**Sexta:** o casal ocupa a noite (Reels 18h30 + Short 19h00, **um arquivo só**).

**O que mudou em relação ao rascunho de ontem** (`saida/2026-10-15/00-pauta.md`):
- **Lista:** saiu a ideia "Prime Video em outubro" / "documentais de música". *Marília Mendonça: Sentimento Louco* estreia hoje, mas **não tem pôster no TVmaze** (revisor, 15/10) e a Lista exige pôster real. Ela também pede peça própria e tom respeitoso (decisão do revisor em 15/10). O tema virou **thriller político puxado por *A Diplomata* T4** (estreou ontem).
- **"Qual sexta é você?":** os 4 tipos foram refeitos. *The Paper* saiu (foi "exausta" no carrossel de 15/10) e entrou *Ninguém Quer*.
- **Carrossel:** continua "minisséries pro fim de semana", mas sem *Sentimento Louco* (sem pôster) e sem *Missa da Meia-Noite* (catálogo 2026 não confirmado, revisor 15/10).
- **Selvagens Ep. 03 e Tradutor** (prontos e não narrados em 15/10) vão para **sábado** (ver rascunho). A Lista "terror de cidade pequena" fica guardada: *Profundezas* entra hoje no "Qual sexta é você?".

## Capacidade e prioridade de narração (ElevenLabs)
Ontem sobraram **29 créditos** (APRENDIZADOS 15/10). Não se sabe se houve recarga. **Cheque o saldo antes de narrar.** Estimativa: 1 caractere = 1 crédito, cerca de 6 caracteres por palavra.

| Ordem | Peça | Slots que cobre | Narração | Custo estimado |
|---|---|---|---|---|
| **1º** | `05-reels-short-casal-sexta-escolhe-voce` (18h30 Reels + 19h00 Short) | **2** (e é o casal obrigatório da sexta) | Ela + Ele, ~85 palavras no total, 25–30 s | ~520 caracteres |
| **2º** | `04-short-reels-qual-sexta-e-voce` (13h30 YouTube + Instagram) | **2** | MIA, ~90 palavras, ~32 s | ~560 caracteres |
| **3º** | `03-lista-da-mia-a-diplomata-thrillers-politicos` (12h00) | 1 | MIA, ~240 palavras, **~1 min 40 s** (4 séries, texto enxuto) | ~1.450 caracteres |

- **Total do dia:** ~2.530 caracteres. A ordem privilegia slots por crédito: as duas primeiras cobrem 4 slots com ~1.080 caracteres.
- **Narre uma pasta por vez, nessa ordem**, e pare no primeiro `quota_exceeded`, sem repetir (`python scripts/narrar.py saida/2026-10-16/<pasta>`). O casal usa `narracao-ela.txt` / `narracao-ele.txt` com as vozes Ela e Ele (`CLAUDE.md`). Nunca outro voice_id nem outro TTS.
- **Ordem de produção ≠ ordem de narração:** produza pela hora (a Lista vence primeiro), mas **gaste o crédito na ordem acima**. Se depois do 1º e do 2º o saldo não cobrir os ~1.450 da Lista, ela não é narrada e vai para o `99-revisao.md` como "slot não cumprido (período de base)". **Não corte a Lista para 3 séries só para caber**: se o saldo ficar entre ~1.100 e ~1.450, aí sim corte o bloco do nº 4 (*O Agente Noturno*) antes de narrar.
- **Se só der para uma narração:** sai a 05 (casal), que cobre a regra da sexta e 2 slots.
- **Carrossel + Stories (01 e 02) não usam crédito.** Saem de qualquer jeito.
- **Peças das 10h00:** se não estiverem aprovadas até 9h50, saem às 11h00; se não até 10h50, às 15h00 (`08`). Registrar no `99-revisao.md`.

## Histórico (regra de 30 dias: `historico/publicados.md` + `saida/2026-10-15/`)
- **15/10 publicou:** carrossel + Stories "quinta de estreia" (*The Paper*, *A Diplomata*, *Carrie*) e Short + Reels Relógio *A Diplomata* ("contando os dias pra voltar"). **Não saíram:** Lista "terror de cidade pequena", Selvagens Ep. 03, Tradutor (sem crédito).
- ***A Diplomata*** já saiu 2× (15/10). Hoje ela **não é indicada** em nenhuma peça: aparece só como gancho de tendência na abertura da Lista, com humor ("tensão política pro fim de semana") e gancho diferentes. Pôster dela na abertura → entra no `"series"` da Lista (trava do pôster; não tirar a série da lista para passar, lição do revisor de 15/10).
- ***Carrie*** (13 e 15/10) e ***The Paper*** (13 e 15/10): **fora hoje**, para não cansar.
- ***Profundezas***, ***Habeas Corpus***, ***Coven Academy***: nunca foram indicadas em peça publicada com esses humores. *Habeas Corpus* foi só gancho da Lista de 14/10 ("Acabou Habeas Corpus?"); hoje entra com humor "curiosa" e gancho "Qual sexta". *Coven Academy* saiu no carrossel de 13/10 com humor "órfã"; hoje é "animada". Permitido.
- **Casal:** 09/10 foi *Hotel Assombrado* + gancho "mão na cara". Hoje: outra série, outro gancho.
- **Lista, nº 1 em 30 dias:** *Olhos que Condenam* (14/10). Hoje o nº 1 é *Dia Zero*. ✓
- **Eixos da Lista na semana:** 14/10 "acabou X?" (publicada) · 15/10 gênero (não publicada) · **16/10 gênero/subgênero com gancho de estreia** (thriller político) · sábado: plataforma/momento ou pessoa (ver rascunho).

## Nota de verificação
- **WebFetch caiu em DNS (ENOTFOUND)** em gameoverdrive.com.br, oficinadanet.com.br e **api.tvmaze.com**. Tudo foi checado por WebSearch. **Pôsteres não foram baixados**: quem roda `python scripts/posters.py` é o `roteirista`. Sem pôster → reserva indicada na peça.
- **Top 10 da Netflix Brasil de 5–11/10 não foi reconfirmado hoje** (a busca não trouxe o ranking; ontem o revisor também não confirmou). **Não afirmar posição no Brasil** em nenhuma peça.
- **Duração de episódio e horário de estreia:** não afirmar em nenhuma peça.
- Catálogo de títulos antigos (*The Americans*, *Dia Zero*, *O Gambito da Rainha*, *Chernobyl*, *Mare of Easttown*) só tem fonte sem data de 2026 ou de meses atrás. **O revisor confirma no app ou no JustWatch BR** antes de aprovar.

---

# HOJE: 2026-10-16

## 01-carrossel-minisseries-pro-fim-de-semana (Instagram · Carrossel · 10h00)
- **Formato:** 7 cards 1080×1350 (`--imagens --formato 4x5`), um `section.quadro` por card. Sem narração.
- **Pilar:** 1. Série pro seu humor · **Job:** principal (indicação certeira com onde assistir) · **Humor:** "quero fechar algo" — cada card na cor de um humor.
- **Estágio / CTA:** Consideração · "**Salva pra hoje à noite.**" (um só).
- **Formato recorrente de referência:** card de indicação com selo "onde assistir" + recibo/cupom (como o carrossel de 15/10, `saida/2026-10-15/01-carrossel-quinta-de-estreia-por-humor/`).
- **Gancho (card 1):** "Sexta. Começa hoje, termina domingo." Subtítulo: "4 minisséries pra fechar no fim de semana — uma pra cada humor." Emoji 🛋️.
- **Cards:**
  2. **Curiosa** (`--curioso`): ***A Leste do Éden***, Netflix, **minissérie de 7 episódios, todos desde 01/10**, com Florence Pugh. Por que combina: drama de família com uma vilã que você não consegue largar. Pra quem não é: quem quer algo leve hoje.
     - Fontes: [Einerd](https://www.einerd.com/a-leste-do-eden-minisserie-com-florence-pugh-ja-esta-na-netflix/), [Omelete](https://www.omelete.com.br/netflix/a-leste-do-eden-netflix-florence-pugh-trailer), [Canaltech](https://canaltech.com.br/entretenimento/a-leste-do-eden-nova-serie-com-florence-pugh-e-grande-aposta-da-netflix-conheca/).
  3. **Focada / querendo se inspirar** (`--feliz`): ***O Gambito da Rainha***, Netflix, **minissérie de 7 episódios**. Por que combina: uma prodígio do xadrez, e você torce a cada partida. Pra quem não é: quem não quer tocar em vício (é tema da série).
     - Fontes: [Netflix BR (página do título)](https://www.netflix.com/br/title/80234304), [Jovem Pan](https://jovempan.com.br/entretenimento/tv-e-cinema/o-gambito-da-rainha-saiba-detalhes-da-serie-limitada-mais-assistida-da-netflix.html). ⚠️ Fonte de catálogo sem data de 2026: **revisor confirma**.
  4. **Tensa** (`--estressado`): ***Mare of Easttown***, HBO Max, **minissérie de 7 episódios**, com Kate Winslet. Por que combina: investigação numa cidadezinha, um episódio puxa o outro. Pra quem não é: quem quer história sem luto.
     - Fontes: [Sitio Andino, 06/08/2026 (disponível na HBO Max)](https://www.sitioandino.com.ar/muchoshow/es-una-las-mejores-miniseries-los-ultimos-tiempos-y-esta-hbo-max-n5660237). ⚠️ Fonte argentina: **revisor confirma no HBO Max Brasil**.
  5. **Com vontade de algo forte** (`--triste`): ***Chernobyl***, HBO Max, **minissérie de 5 episódios**. Por que combina: a mais curta da lista e uma das mais impactantes. Pra quem não é: quem quer desligar a cabeça — é pesada.
     - Fontes: [Omelete, lista de mar/2026 (HBO Max)](https://www.omelete.com.br/filmes/emergencia-radioativa-filmes-series-desastres-nucleares-streaming), [A Tarde (5 episódios)](https://atarde.com.br/cineinsite/essa-serie-baseada-em-fatos-e-considerada-uma-das-melhores-da-historia-1350881), [Xataka](https://www.xataka.com.br/diversos/dura-apenas-5-horas-e-uma-das-melhores-minisseries-da-historia-e-voce-pode-assistir-em-streaming).
  6. **Recibo "o mapa do fim de semana"** (cupom do motor): humor → série → streaming → nº de episódios, das 4. Não indica série nova.
  7. **CTA:** "Salva pra hoje à noite." + @seriecerta.
  - **Reservas** (sem pôster ou sem confirmação): *Dia Zero* não (está na Lista); *Profundezas* não (está no 04). Use ***Olhos que Condenam*** **só se** precisar e com outro humor (Netflix, minissérie de 4 episódios; foi nº 1 da Lista de 14/10 com humor "justiça" — aqui seria "quero fechar algo"; o revisor decide) ou fique com 3 séries + card-texto "a regra da MIA: minissérie é série que respeita seu domingo".
- **Legenda:** gancho + "A Leste do Éden (Netflix) · O Gambito da Rainha (Netflix) · Mare of Easttown (HBO Max) · Chernobyl (HBO Max)" + "Salva pra hoje à noite." Máx. 2 emojis. Hashtags: #seriecerta #oqueassistir #minisserie #dicadeserie.
- **Pôsteres:** `python scripts/posters.py <pasta> "East of Eden (2026)" "The Queen's Gambit" "Mare of Easttown" "Chernobyl"`. Em *East of Eden*, conferir 2026 + Florence Pugh (não o filme de 1955 nem a minissérie de 1981). Cortar logos de streaming do pôster.
- **`"series"`:** ["A Leste do Éden", "O Gambito da Rainha", "Mare of Easttown", "Chernobyl"].
- **Horário:** Instagram CAROUSEL `2026-10-16T10:00:00-03:00` (fallback 11h00 → 15h00).

## 02-stories-minisseries-pro-fim-de-semana (Instagram · Stories · 10h00)
- **Formato:** o carrossel 01 em 9:16 (1080×1920), **4 telas + 1 de CTA**. Pode usar `"peca_mae": "01-carrossel-minisseries-pro-fim-de-semana"`. Sem narração.
- **Pilar:** 1 · **Job:** principal + social 1 (sexta a dois) · **Humor:** vários.
- **Telas:** 1 "Sexta. Começa hoje, termina domingo." · 2 *A Leste do Éden* (Netflix) · 3 *Mare of Easttown* (HBO Max) · 4 *O Gambito da Rainha* (Netflix) · 5 CTA.
  - *Chernobyl* fica fora dos Stories (tom pesado ao lado de tela de venda).
- **CTA / funil:** Conversão, um só: "**Vai ver a dois? Testa o modo casal grátis no link da bio.**" (modo casal está no ar, `CLAUDE.md`; casa com a sexta). Se o revisor não confirmar que o link da bio leva a um lugar onde o modo casal aparece, use o padrão: "A MIA acha a sua pelo seu humor. Testa grátis no link da bio." Sem enquete, sem "responde no direct".
- **Link da bio:** `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-16-stories-minisseries-fim-de-semana` (sem `humor=`: slug não confirmado).
- **`"series"`:** ["A Leste do Éden", "Mare of Easttown", "O Gambito da Rainha"].
- **Horário:** Instagram STORIES `2026-10-16T10:00:00-03:00` (mesmo fallback do 01).

## 03-lista-da-mia-a-diplomata-thrillers-politicos (YouTube · Lista da MIA 16:9 · 12h00)
- **Formato:** Lista da MIA 1920×1080, **~1 min 40 s**, contagem regressiva de **4 séries** (nº 1 por último). Vídeo: `motor/exemplos/lista-da-mia-16x9.html`, `<body class="paisagem" style="--mood:var(--estressado)">`. Thumb: `motor/exemplos/lista-da-mia-thumb.html` com **"4"** gigante + "DEPOIS DE A DIPLOMATA" + 🕵️.
- **Pilar:** 1. Série pro seu humor (humor "quero tensão política no fim de semana"; tema pela tendência) · **Job:** principal (secundário: emocional 3, para quem maratonar a T4) · **`--mood`:** estressado (tensão).
- **Eixo:** **gênero/subgênero** (thriller político), com gancho na estreia da semana. **Tema:** "A Diplomata voltou: thrillers políticos pro fim de semana".
- **Por que é tendência (3 sinais):**
  1. **Estreia da semana:** *A Diplomata* T4 chegou à Netflix em **15/10, com 8 episódios de uma vez** ([Omelete](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data); [Omelete, trailer completo](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-trailer-completo); [What's on Netflix](https://www.whats-on-netflix.com/news/keri-russell-confirms-the-diplomat-season-4-is-set-for-netflix-release-in-october-2026/); TVmaze conferido pelo revisor em 15/10). É a maior estreia de série da Netflix nesta semana no Brasil ([Oficina da Net, lançamentos de outubro](https://www.oficinadanet.com.br/netflix/72900-lancamentos-netflix-outubro-2026): 12/10 *Fire Spike*, 13/10 *Armadilha*, 15/10 *A Diplomata* T4; próximas só em 22/10).
  2. **Reta final de outra série do gênero:** *Slow Horses* T6 termina na **quarta, 21/10** (episódios semanais desde 16/09) ([Ovicio](https://ovicio.com.br/slow-horses-ganha-teaser-e-data-de-estreia-oficial-para-a-6a-temporada/); [T2 Online](https://t2online.in/screen/streaming/apple-tv-s-slow-horses-season-six-sends-the-misfits-of-mi5-underground-from-september-16/2007344)).
  3. **Demanda de busca "parecidas com A Diplomata":** há listas fixas sobre isso em sites BR ([Canaltech](https://canaltech.com.br/series/10-series-de-suspense-e-drama-politico-como-a-diplomata-disponiveis-em-streaming/); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000021278/)), sinal de que quem termina procura a próxima. Fim de semana logo após um lançamento de 8 episódios de uma vez = maratona.
  - **Lacuna:** sem sinal direto de Google Trends, X ou TikTok (buscas vazias, WebFetch bloqueado). Top 10 BR da semana não confirmado. **Na peça, dizer "voltou ontem/esta semana com os 8 episódios"; não dizer "a mais vista".**
- **Título (≤ 70):** **"A Diplomata voltou: 4 thrillers políticos pro seu fim de semana"** (63 caracteres).
- **Gancho (0–15 s):** "Sabe aquela tensão boa de série política, que você jura que é só mais um episódio? *A Diplomata* voltou esta semana com os oito de uma vez. Pra quando acabar, eu separei quatro com essa mesma tensão." Pôster de *A Diplomata* na abertura.
  - **Spoiler zero:** nada da T3 nem da trama da T4 (nada de arma, Hal, Grace Penn). A abertura cita só que voltou.
- **Séries (contagem regressiva):**
  4. ***O Agente Noturno***: Netflix, 3 temporadas; a 3ª saiu em 19/02/2026 com 10 episódios de uma vez ([Einerd](https://www.einerd.com/o-agente-noturno-saiba-o-horario-exato-da-estreia-da-3a-temporada-na-netflix/); [Rolling Stone Brasil](https://rollingstone.com.br/tv/netflix-data-de-estreia-temporada-3-o-agente-noturno/)). Por que combina: um agente atende um telefone secreto da Casa Branca e tudo vira conspiração. Pra quem não é: quem quer política de bastidor, sem tiroteio — essa é ação. **Não afirmar 4ª temporada** (não anunciada nas fontes).
  3. ***The Americans***: Disney+, 6 temporadas (série encerrada), com **Keri Russell, a Kate de *A Diplomata*** (ponte com a tendência) ([JustWatch BR](https://www.justwatch.com/br/serie/the-americans); [Disney+](https://www.disneyplus.com/browse/entity-6deba130-65fb-4816-acb1-aea5eb940f0f)). Por que combina: espiões soviéticos fingindo ser uma família comum nos EUA. Pra quem não é: quem quer ritmo rápido — é slow burn. ⚠️ **Revisor confirma no Disney+ Brasil** (fontes sem data).
  2. ***Slow Horses***: Apple TV, 6 temporadas; **a 6ª termina na quarta, 21/10** (fontes no sinal 2). Por que combina: espiões rejeitados do MI5 e um chefe insuportável, com humor ácido. Pra quem não é: quem não aguenta sotaque britânico carregado e chefe grosseiro. **Não citar** o que acontece na T6.
  1. ***Dia Zero***: Netflix, **minissérie de 6 episódios** (2025), com Robert De Niro ([Netflix BR](https://www.netflix.com/br/title/81598435); [TecMundo](https://www.tecmundo.com.br/minha-serie/600770-dia-zero-tem-quantos-episodios-veja-notas-e-quanto-tempo-demora-para-maratonar.htm); [Rolling Stone Brasil](https://rollingstone.com.br/cinema/conheca-dia-zero-nova-minisserie-da-netflix-estrelada-por-robert-de-niro/)). Por que combina: um ex-presidente investiga um ataque cibernético; dá pra fechar até domingo. Pra quem não é: quem quer final aberto pra continuar (é minissérie fechada). **Não citar duração** (fontes divergem).
  - **Reserva:** ***Designated Survivor*** (Netflix, 3 temporadas; a Netflix disse que manteria as 3 "por anos" ([Netflix About](https://about.netflix.com/news/netflix-to-bring-designated-survivor-to-viewers-around-the-world-as-a-global-original-series)); confirmação 2026 fraca → revisor confirma no app).
- **Pôsteres:** `python scripts/posters.py <pasta> "The Diplomat" "The Night Agent" "The Americans" "Slow Horses" "Zero Day"`. *The Diplomat* = TVmaze #60213 (pôster da T4, conferido pelo revisor em 15/10; cortar "ONLY ON NETFLIX" do rodapé). *Zero Day*: conferir 2025 + De Niro. *The Americans*: 2013 (não confundir). Cortar logos de streaming.
- **Demo do app:** não entra (`assets/demo/` vazio).
- **Fim e CTA único:** "**Salva pra hoje à noite**" (Consideração) + link fixado. Sem pergunta pros comentários (mesma decisão de 14 e 15/10). Comentário fixado lista onde assistir cada série, sem pedido.
- **Descrição:** capítulos (00:00 abertura; um por série, calculados pelo `narracao.json` + 0,30 s), onde assistir de cada uma e UTM `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-16-lista-da-mia-a-diplomata-thrillers-politicos`.
- **Tags:** a diplomata, the diplomat, keri russell, thriller político, séries de espionagem, o agente noturno, the americans, slow horses, dia zero, robert de niro.
- **`"series"`:** ["A Diplomata", "O Agente Noturno", "The Americans", "Slow Horses", "Dia Zero"] (A Diplomata entra porque o pôster aparece na abertura).
- **Horário:** YouTube `2026-10-16T12:00:00-03:00` (3º na fila de narração).

## 04-short-reels-qual-sexta-e-voce (YouTube Short + Instagram Reels · 13h30 · **o mesmo vídeo**)
- **Decisão:** um arquivo 9:16, duas publicações no `publicar.json` (`YOUTUBE_SHORT` + `REELS`), ambas `2026-10-16T13:30:00-03:00`. TikTok: mesmo arquivo + `tiktok.txt`.
- **Formato:** 9:16, ~32–35 s, narração da MIA. **Formato recorrente: Qual é você?** (`09`). Base: `referencias/quadros/qual-e-voce-4-tipos.jpg` e o roteiro de 14/10 (`saida/2026-10-14/04-reels-qual-quarta-e-voce/roteiro.md`), que **não foi publicado**. Reaproveitar a estrutura, **reescrever as falas** (as de 14/10 têm "chega amanhã" vencido).
- **Pilar:** 1. Série pro seu humor · **Job:** principal + social 2 (ser a amiga das indicações) · **Humores:** 1 exausta `--sono` · 2 curiosa `--curioso` · 3 que quer medo `--estressado` · 4 animada `--animado`.
- **Gancho (0–2 s, fala + tela):** "**Pra amiga que é a número três toda sexta.**" → "Qual sexta é você?"
- **Tipos e séries** (fala enxuta: tipo + superpoder + série + streaming + pra quem não é):
  1. **A exausta** — superpoder: dormir no episódio 1 → ***Ninguém Quer***, Netflix, comédia romântica leve; **a 3ª temporada chega dia 22/10** ([Omelete, lançamentos de outubro](https://www.omelete.com.br/series-tv/netflix-lancamentos-outubro-2026); [Oficina da Net](https://www.oficinadanet.com.br/netflix/72900-lancamentos-netflix-outubro-2026)). Pra quem não é: quem quer tensão. Na tela: "dá tempo de ver as 2 primeiras antes do dia 22". ⚠️ Revisor confirma que T1 e T2 estão na Netflix BR e a data da T3.
  2. **A curiosa** — superpoder: "só mais um" às 2h → ***Habeas Corpus***, Netflix, drama jurídico brasileiro, 8 episódios, desde 23/09 ([Netflix About](https://about.netflix.com/pt_br/news/netflix-unveils-the-first-images-and-the-poster-for-habeas-corpus-a-series-featuring-marjorie-estiano-and-any-gabrielly-which-premieres-september-23); [Canaltech](https://canaltech.com.br/entretenimento/habeas-corpus-quem-e-quem-na-nova-serie-juridica-brasileira-da-netflix/)). Pra quem não é: quem quer algo leve.
  3. **A que quer medo** — superpoder: terror de luz acesa → ***Profundezas***, Netflix, minissérie de 6 episódios, desde 08/10 ([Einerd](https://www.einerd.com/profundezas-below-serie-terror-netflix/); [GameOverDrive](https://gameoverdrive.com.br/profundezas-episodios-duracao/)). Pra quem não é: quem tem medo de mar. Só a premissa ("algo vem do mar"); nada do final.
  4. **A animada** — superpoder: começar 3 séries no mesmo dia → ***Coven Academy***, Disney+, temporada inteira desde 02/10, bruxas adolescentes em Nova Orleans ([Disney Blog](https://disneyblog.com/news/coven-academy-premieres-october-1-on-freeform-streams-next-day/); [Showmetech](https://www.showmetech.com.br/lancamentos-do-disney-plus-em-outubro-de-2026/)). Pra quem não é: quem quer terror pesado. **Não citar nº de episódios** (21 não confirmado).
- **Fecho / CTA:** "[rindo baixinho] Achou a sua? Manda pra quem precisa." + botão brasa **MANDA PRA QUEM PRECISA** + @seriecerta (Descoberta). Um só: sem "comenta o número".
- **Capa:** grade final com os 4 números coloridos e "QUAL SEXTA É VOCÊ?".
- **Legenda IG:** "Pra amiga que é a nº 3 toda sexta" + "1 Ninguém Quer (Netflix) · 2 Habeas Corpus (Netflix) · 3 Profundezas (Netflix) · 4 Coven Academy (Disney+)" + "Manda pra quem precisa." Hashtags: #seriecerta #oqueassistir #dicadeserie #sextou. **Título YT:** "Qual sexta é você? 4 tipos, 4 séries".
- **Pôsteres:** reaproveitar de `saida/2026-10-14/04-reels-qual-quarta-e-voce/imagens/` (*Habeas Corpus* #93677, *Below* #93115, *Coven Academy* #83159; logo "Disney" do pôster de *Coven Academy* → cortar ou registrar) + `python scripts/posters.py <pasta> "Nobody Wants This"` (2024, Kristen Bell / Adam Brody).
- **`"series"`:** ["Ninguém Quer", "Habeas Corpus", "Profundezas", "Coven Academy"].
- **UTM (descrição YT):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-16-short-qual-sexta-e-voce`.
- **Horários:** YouTube Short + Instagram REELS `2026-10-16T13:30:00-03:00` (2º na fila de narração).

## 05-reels-short-casal-sexta-escolhe-voce (Instagram Reels 18h30 + YouTube Short 19h00 · **o mesmo vídeo**)
- **Decisão:** um arquivo 9:16, duas publicações: `REELS` `2026-10-16T18:30:00-03:00` e `YOUTUBE_SHORT` `2026-10-16T19:00:00-03:00`. Redes diferentes, sem repetição no mesmo canal. TikTok: mesmo arquivo.
- **Formato:** 9:16, 25–30 s, **esquete Ela & Ele** com as vozes Ela (`1AxHVMpXJZxq6ECdF4Kn`) e Ele (`oeBFFQkxcUHweNreD1nw`), arquivos `narracao-ela.txt` / `narracao-ele.txt`. Sem voz da MIA (economia de crédito): a MIA aparece como **texto na tela do celular** (genérico, sem logo). Base: o vídeo do casal de 09/10 (`referencias/`), sem repetir o gancho "mão na cara".
- **Pilar:** 3. Dilema do casal · **Job:** social 1 (escolha que agrade os dois) · **Humor:** romântico + adrenalina (`--romantico`).
- **Gancho (0–2 s, fala + tela):** "**Pro casal que passa a sexta inteira no 'escolhe você'.**"
- **Esquete (situação, sem diálogo de série):** sexta, 21h, sofá. Ele: "Escolhe você." Ela escolhe; ele veta. Ele escolhe; ela veta. Inversão do clichê: **ela quer ação, ele quer romance**. Placar na tela "vetos: 4 × séries vistas: 0". Ele abre a MIA no modo casal (texto na tela: "ela: ação · ele: romance") → resposta.
- **Série:** ***Sr. e Sra. Smith***, Prime Video, **1ª temporada com 8 episódios** (fev/2024), com Donald Glover e Maya Erskine: dois espiões que precisam fingir ser casados — ação pra um, romance pro outro ([AdoroCinema](https://www.adorocinema.com/noticias/filmes/noticia-1000067155/); [CNN Brasil](https://www.cnnbrasil.com.br/pop/sr-e-sra-smith-nova-serie-ganha-fotos-e-data-de-estreia-veja/); [Canaltech](https://canaltech.com.br/series/sr-e-sra-smith-o-que-esperar-do-reboot-do-prime-video-277705)). Pra quem não é (tela): "quem quer comédia romântica levinha".
  - **Não afirmar** nada sobre a 2ª temporada (renovada em 2024; elenco e data não confirmados). ⚠️ Original Prime Video; fontes de 2024 → **revisor confirma no app**.
  - **Reserva** (sem pôster ou sem confirmação): ***Um Choque de Amor*** (Netflix, dorama de comédia romântica, 10 episódios desde 09/10, [Einerd](https://www.einerd.com/um-choque-de-amor-o-k-drama-em-que-o-toque-e-questao-de-vida-ou-morte/)) — mas aí o Selvagens Ep. 03 de sábado precisa trocar de série.
- **Fecho / CTA:** botão brasa "**MANDA PRA QUEM PRECISA**" + @seriecerta (Descoberta). Um só. Na tela acima: "manda pro seu 'escolhe você'".
- **Legenda:** gancho + "Sr. e Sra. Smith, Prime Video: ação pra um, romance pro outro." + "Manda pra quem precisa." Hashtags: #seriecerta #casal #oqueassistir #sextou. **Título YT:** "Sexta à noite: quem escolhe a série?".
- **Pôster:** `python scripts/posters.py <pasta> "Mr. & Mrs. Smith (2024)"` (série, não o filme de 2005). Cortar logo Prime Video se houver.
- **`"series"`:** ["Sr. e Sra. Smith"].
- **UTM (descrição YT):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-16-short-casal-sexta-escolhe-voce`.
- **Horários:** 1º na fila de narração.

**Pilares de hoje:** 1 (carrossel, Stories, Lista, 13h30) e 3 (casal 18h30/19h). Reels: 1 × 3 ✓. Shorts: 1 × 3 ✓. Casal na sexta à noite ✓.
**Semana até aqui (14–16/10, só peças de feed/vídeo):** pilar 1 dominante, 2 em 15/10, 3 hoje, 5 planejado e não publicado. Pilar 4 (prova) segue sem peça: falta demo em `assets/demo/` (pendência para o Bruno). Sábado puxa 2 e 5.

---

# RASCUNHO DE AMANHÃ: sábado, 2026-10-17
> A rotina de amanhã refaz a pesquisa de tendência e **revalida todos os fatos**. Pasta: `saida/2026-10-17/`. Foco em reaproveitar roteiros prontos e não narrados (economia de crédito).

## 01-carrossel-<sábado> + 02-stories (10h00)
- **Pilar 5. Bastidor do produto** (o mais atrasado na semana) · Job: Atração. Proposta: "**O que a MIA te pergunta antes de indicar**" — humor → contexto (sozinha / a dois / quanto tempo) → onde assistir → pra quem não é. Pode ter 1 série-exemplo com pôster. **Não prometer** o que o app não faz (`04`).
- Stories: as telas + CTA Conversão "Testa grátis no link da bio".

## 03-lista-da-mia-<tema> (12h00)
- **Eixo diferente de gênero e de "acabou X?"**: (a) **plataforma/momento** "o melhor que chegou no Prime Video em outubro" (*Carrie* 07/10 — só se o revisor aceitar a 3ª aparição em 5 dias, senão fora; *Rainha Vermelha* T2 02/10 — data BR não confirmada; *Prefiro a Morte* 02/10; *True Blood* 05/10; *Sentimento Louco* só se o pôster existir no TVmaze); ou (b) **por atriz** se surgir sinal (ex.: Florence Pugh / *A Leste do Éden* no Top 10). Nº 1 não pode ser *Olhos que Condenam* nem *Dia Zero*.
- **Sentimento Louco:** se o pôster aparecer no TVmaze e houver repercussão do fim de semana, pode virar peça própria, tom respeitoso, sem piada, sem falar da morte.

## 04-short-reels-selvagens-do-sofa-ep03 (13h30, YouTube + Instagram, mesmo vídeo)
- **Reaproveitar** o roteiro pronto de `saida/2026-10-15/05-reels-selvagens-do-sofa-ep03-quinta-de-estreia/` (*Um Choque de Amor*, 504 caracteres). Trocar "quinta" por "sábado" no registro de campo; o resto da piada (3 estreias, zero episódios) segue genérico. Pôster TVmaze #90007 já baixado. Pilar 1, CTA "Manda pra quem precisa". Revalidar 10 episódios / Netflix.

## 05-reels-<órfã> (18h30)
- **Pilar 2. Órfã de série**. Candidatas: quem maratonou *A Diplomata* T4 no fim de semana (sem spoiler; série + humor + gancho diferentes de 15/10) ou *A Leste do Éden*. Formato Relógio ou Tradutor. CTA Descoberta.

## 06-short-tradutor-o-que-a-mia-entende (19h00)
- **Reaproveitar** o roteiro pronto de `saida/2026-10-15/06-short-tradutor-o-que-a-mia-entende/` (pilar 5, sem séries, ~400 caracteres). Shorts do dia: 1 × 5 ✓.
- **Crédito previsto de sábado:** ~504 + ~400 + Lista (~1.450) + órfã (~450) ≈ 2.800 caracteres. Prioridade de sábado: 04 (2 slots, já roteirizado) → 06 (já roteirizado) → Lista → 05. Se faltar crédito, o 05 cai (o arquivo do 13h30 já está no Instagram, então não serve de reaproveitamento) e vai para o `99-revisao.md`.

---

## Ideias guardadas (revalidar antes de usar)
- *Ninguém Quer* T3 (Netflix, 22/10): pilar 2 na quinta 22/10.
- *Lupin* parte 4 (Netflix, 23/10).
- *A Lista Terminal* T2 (Prime Video, 21/10).
- *Slow Horses* T6, final em 21/10: pilar 2 ("acabou Slow Horses?") em 22/10.
- *Dom de Iludir* (Netflix, série brasileira, **28/10**, Marieta Severo, Alice Wegmann, Nanda Costa, 10 episódios) ([Netflix About](https://about.netflix.com/pt_br/news/netflix-unveils-main-trailer-and-release-date-for-the-gift-of-deceit-new-melodrama-starring-marieta-severo-alice-wegmann-and-nanda-costta)).
- *Largados e Pelados Brasil* T4 (HBO Max, 18/10): reality, só se casar com um humor.
- Lista "terror de cidade pequena" (pronta em `saida/2026-10-15/03-...`, não narrada): reaproveitar perto do Halloween (sáb 31/10), com fatos rechecados e sem repetir *Profundezas* como série-chave se ela já tiver saído.

## Pendências para o Bruno
1. **Créditos ElevenLabs:** confirmar recarga. O dia pede ~2.530 caracteres. Sem crédito, só saem carrossel + Stories; o casal obrigatório da sexta cai.
2. **Pôster de *Marília Mendonça: Sentimento Louco*:** não existe no TVmaze (15/10). Sem ele a série não entra em Lista; se quiser uma peça sobre o doc, decidir se aceita capa gerada (regra 3, com registro).
3. **Slug `humor=<humor>`** e **link do modo casal** no app: seguem sem confirmação; links vão sem humor.
4. **Bio do Instagram:** trocar para a UTM do Stories de hoje antes das 10h00 (manual).
5. **DNS/proxy:** WebFetch falha em gameoverdrive, oficinadanet e **api.tvmaze.com**. Catálogo de títulos antigos depende de busca; vale bater o olho no app em *The Americans* (Disney+), *Mare of Easttown* e *Chernobyl* (HBO Max), *Sr. e Sra. Smith* (Prime Video).
6. **Demo do app** em `assets/demo/`: sem ela, o pilar 4 (prova, 15%) não sai.
7. **"Respondendo seu humor (parte 2)":** promessa do "Quarta, 21h" segue em aberto (sem `comentarios.md`).
