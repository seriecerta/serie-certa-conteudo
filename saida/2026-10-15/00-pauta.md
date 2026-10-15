# Pauta: quinta-feira, 2026-10-15 (America/Sao_Paulo)

**Grade:** a diária de `08-cronograma.md`, em vigor desde 14/10. Carrossel + Stories às 10h00 · Lista da MIA às 12h00 (YouTube 16:9) · Short + Reels às 13h30 · Reels às 18h30 · Short às 19h00. Não existe mais vídeo longo de quinta.
**Meta dos 90 dias:** audiência, com orçamento zero (`05`). Reels e Shorts fecham com "Manda pra quem precisa".
**Período de base (14–20/10):** a grade fica fixa e sem teste A/B. Nenhuma peça leva `experimento`. O registro de `10-experimentos.md` está vazio.
**Rascunho de 14/10:** foi reencaixado na grade nova e todos os fatos foram rechecados hoje. O que mudou em relação a ele:
- o vídeo longo das 19h saiu;
- a Lista passou para as 12h00;
- *VisionQuest* saiu do carrossel (repetiria série + humor "animado" de 14/10);
- *Profundezas* foi para a Lista, porque virou a nº 1 da Netflix no Brasil;
- *Um Choque de Amor* entrou no Reels das 18h30.

## Capacidade e prioridade de narração (ElevenLabs)
Ontem sobraram **157 créditos**. Não se sabe se houve recarga, então **cheque o saldo antes de narrar**. Estimativa de consumo: 1 caractere = 1 crédito, e cerca de 6 caracteres por palavra em PT-BR.

| Ordem | Peça | Por quê | Narração | Custo estimado |
|---|---|---|---|---|
| **1º** | `04-short-reels-relogio-a-diplomata-voltou` (13h30, YouTube + Instagram) | Estreia de hoje. Um arquivo só cobre 2 slots com o menor custo | ~70 palavras, 25–30 s | ~450 caracteres |
| **2º** | `03-lista-da-mia-terror-de-cidade-pequena` (12h00, YouTube) | Âncora diária, puxada pela nº 1 da Netflix no Brasil | ~280 palavras, **~2 min** (4 séries) | ~1.700 caracteres |
| **3º** | `05-reels-selvagens-do-sofa-ep03-quinta-de-estreia` (18h30, Instagram) | Formato recorrente que gera envio | ~85 palavras, 30–35 s | ~520 caracteres |
| **4º** | `06-short-tradutor-o-que-a-mia-entende` (19h00, YouTube) | O de menor prioridade | ~65 palavras, 25 s | ~400 caracteres |

- **Total do dia:** cerca de 3.100 caracteres. Com os 157 créditos de ontem não sai nenhuma narração.
- **Ordem de produção ≠ ordem de narração:** a Lista vence primeiro (12h00). Se o crédito der para as duas primeiras, narre as duas antes de começar a produzir.
- **Se o crédito só der para uma narração:** sai a 04. A Lista fica sem slot hoje, e isso vai para o `99-revisao.md` como "slot não cumprido (período de base)".
- **Fallback das 19h00:** se o crédito acabar depois da 05, o Short das 19h00 **reaproveita o arquivo do Reels das 18h30** (`05`). São redes diferentes, então não há repetição dentro do mesmo canal. Registre isso no `publicar.json` da 05 como segunda publicação (`YOUTUBE_SHORT`, 19h00). Não use outra voz nem outro TTS (`CLAUDE.md`).
- **Carrossel + Stories (01 e 02) não usam narração nem crédito.** São só imagem (`--imagens`) e saem de qualquer jeito.
- **Peças das 10h00:** se não estiverem aprovadas até 9h50, saem às 11h00. Se não estiverem até 10h50, saem às 15h00 (`08`). Registre a decisão no `99-revisao.md`.

## Histórico (regra de 30 dias, `historico/publicados.md` + `saida/2026-10-14/`)
- **14/10 publicou** (agendados): Short *VisionQuest* (animado), Lista "Acabou Habeas Corpus?" (eixo "acabou X?", nº 1 *Olhos que Condenam*) e Stories *VisionQuest*. O Reels "Qual quarta é você?" **não saiu**: ficou bloqueado por falta de crédito. Ele não vai para hoje, porque é de quarta. O roteiro pode virar "Qual sexta é você?" amanhã (ver rascunho).
- **Lista de hoje:** o eixo é **gênero/subgênero** (ontem foi "acabou X?"). Nenhuma das 4 séries foi nº 1 de Lista. *Profundezas* e *Missa da Meia-Noite* nunca saíram. *Stranger Things* e *IT: Bem-vindos a Derry* também não.
- ***Carrie, a Estranha*** saiu em 13/10 (Short Tradutor, humor "órfã de terror", gancho Residência Hill). Hoje ela entra no carrossel com outro humor ("com vontade de medo") e outro gancho ("quinta de estreia"). É permitido. Na Lista ela fica **só de reserva**.
- ***The Paper*** saiu em 13/10 (Reels Selvagens Ep. 02, humor "órfão/reprise", gancho The Office). Hoje entra só no carrossel, com humor "exausta" e o gancho da T2. É permitido. **Não usar a piada do The Office de novo.**
- ***Hotel Assombrado*** (09/10): fora hoje.
- **Selvagens do Sofá:** o Ep. 02 saiu em 13/10, então hoje é o **Ep. 03**.

## Nota de verificação
- **WebFetch falhou por DNS (ENOTFOUND)** em netflix.com, flixpatrol.com, revistabula.com e gameoverdrive.com.br. Tudo foi checado por WebSearch. **Os pôsteres não foram baixados**: este agente não tem shell. Quem roda `python scripts/posters.py` é o `roteirista`. Sem pôster, entra a reserva indicada em cada peça.
- **Duração de episódio:** não foi confirmada para nenhuma série. **Não afirmar.**
- **Horário de estreia:** nenhum foi confirmado oficialmente (o "4h" de *A Diplomata* é previsão de site). **Não afirmar hora.**
- O `revisor` reconfirma cada "onde assistir" no dia.

---

# HOJE: 2026-10-15

## 01-carrossel-quinta-de-estreia-por-humor (Instagram · Carrossel · 10h00)
- **Formato:** carrossel com 7 cards de 1080×1350 (`--imagens --formato 4x5`), um `section.quadro` por card. Não tem narração.
- **Pilar:** 1. Série pro seu humor · **Job:** principal (indicação certeira com onde assistir) · **Humor:** vários, cada card com a sua cor.
- **Formato recorrente de referência:** card de indicação com selo "onde assistir", como o carrossel de 13/10 (`saida/2026-10-13/01-carrossel-orfa-herdeiras-outubro/`).
- **Gancho (card 1):** "Quinta de estreia. Qual é o seu humor hoje?" Subtítulo: "4 séries novas, uma pra cada jeito de chegar em casa."
- **Cards:**
  1. Capa (texto acima, emoji 🍿).
  2. **Exausta** (`--sono`): ***The Paper*, 2ª temporada**, HBO Max, **chega hoje (15/10)**. Por que combina: comédia de escritório, sem esforço. Pra quem não é: quem quer *The Office* igualzinho. **Não dizer** número de episódios nem se a temporada sai inteira ou semanal (não confirmado no Brasil).
     - Fontes: [Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil), [Einerd](https://www.einerd.com/the-paper-spin-off-de-the-office-ganha-data-de-estreia-da-2a-temporada/), [GameOverDrive](https://gameoverdrive.com.br/the-paper-2-temporada-estreia-brasil-hbo-max/), [Itatiaia, outubro na HBO Max](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/).
     - ⚠️ Uma lista da [Showmetech](https://www.showmetech.com.br/lancamentos-hbo-max-outubro-2026/) trata 15/10 como "fim" da temporada. A maioria das fontes diz estreia. O revisor confere no app ou no site da HBO Max. Se não confirmar, o card diz "a 2ª temporada chegou ao HBO Max".
  3. **Tensa / querendo adrenalina** (`--estressado`): ***A Diplomata*, 4ª temporada**, Netflix, **hoje (15/10), 8 episódios de uma vez**. Por que combina: thriller político que não deixa largar. Pra quem não é: quem nunca viu as temporadas anteriores, porque é pra começar da 1ª.
     - Fontes: [Omelete](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data), [GameOverDrive (8 episódios)](https://gameoverdrive.com.br/a-diplomata-4-temporada-quantos-episodios/), [GameOverDrive (estreia nesta quinta)](https://gameoverdrive.com.br/a-diplomata-4-temporada-horario-estreia-netflix/), [What's on Netflix](https://www.whats-on-netflix.com/news/keri-russell-confirms-the-diplomat-season-4-is-set-for-netflix-release-in-october-2026/).
     - **Zero spoiler da T3:** nada do gancho final (arma, Hal, Grace Penn).
  4. **Com vontade de medo** (`--estressado` ou `--ansioso`): ***Carrie, a Estranha***, Prime Video, **8 episódios, todos desde 07/10**, de Mike Flanagan. Pra quem não é: quem não aguenta terror adolescente intenso.
     - Fontes: [GameOverDrive](https://gameoverdrive.com.br/carrie-serie-mike-flanagan-estreia-prime-video/), [Omelete](https://www.omelete.com.br/series-tv/carrie-a-estranha-prime-video-mike-flanagan-data-lancamento-outubro), [Tecmundo](https://www.tecmundo.com.br/minha-serie/604301-carrie-nova-adaptacao-do-prime-video-ganha-trailer-e-data-de-estreia.htm).
  5. **Com saudade** (`--triste`): ***Marília Mendonça: Sentimento Louco***, Prime Video, **chega amanhã (16/10)**, série documental de 4 episódios. **Tom respeitoso:** sem piada, sem falar da morte, só "a trajetória dela contada com o arquivo pessoal". Pra quem não é: quem não quer chorar hoje.
     - Fontes: [Omelete (crítica)](https://www.omelete.com.br/series-tv/marilia-mendonca-sentimento-louco-documentario-critica), [Omelete (trailer e data)](https://www.omelete.com.br/series-tv/marilia-mendonca-doc-prime-video-trailer-data-exposicao), [Super Rádio Tupi](https://www.tupi.fm/?p=2437729).
  6. "A regra da MIA: escolhe pelo humor, não pelo hype." Este card é texto, sem série.
  7. **CTA:** "**Salva pra hoje à noite.**" (Consideração). Um CTA só.
- **Legenda:** gancho + "The Paper T2 (HBO Max) · A Diplomata T4 (Netflix) · Carrie (Prime Video) · Marília Mendonça: Sentimento Louco (Prime Video, sexta)" + "Salva pra hoje à noite." No máximo 2 emojis. Hashtags: #seriecerta #oqueassistir #lancamentosdasemana #dicadeserie.
- **Pôsteres:** `python scripts/posters.py <pasta> "The Paper (2025)" "The Diplomat" "Carrie (2026)" "Marília Mendonça: Sentimento Louco"`.
  - Para *Carrie*, conferir o ano (2026) e o criador (Flanagan). Não pode vir o filme nem o remake de 2002.
  - *Sentimento Louco* pode não estar no TVmaze. Se não estiver, use a capa gerada (`.capa.gerada`) **só para ela** e registre no `99-revisao.md`. Se o revisor preferir, o card 5 sai e o carrossel fica com 6 cards: no mínimo 7 pela regra do `07`, então troque por um card-texto "e amanhã chega…".
- **`"series"`:** ["The Paper", "A Diplomata", "Carrie, a Estranha", "Marília Mendonça: Sentimento Louco"].
- **Horário:** Instagram CAROUSEL `2026-10-15T10:00:00-03:00` (fallback: 11h00 e depois 15h00).

## 02-stories-quinta-de-estreia (Instagram · Stories · 10h00)
- **Formato:** o carrossel 01 em 9:16 (1080×1920), em **4 telas + 1 tela de CTA**. Pode usar `"peca_mae": "01-carrossel-quinta-de-estreia-por-humor"`. Não tem narração.
- **Pilar:** 1 · **Job:** principal · **Humor:** vários.
- **Telas:**
  1. "Quinta de estreia. Como você chegou hoje?"
  2. Exausta → *The Paper* T2 (HBO Max).
  3. Tensa → *A Diplomata* T4 (Netflix).
  4. Medo → *Carrie* (Prime Video).
  5. CTA: "A MIA acha a sua pelo seu humor. **Testa grátis no link da bio.**"
  - O card da Marília fica fora dos Stories, para não misturar tom de saudade com tela de venda.
- **CTA / funil:** Conversão, um só. A arte não tem enquete nem caixinha. A pergunta da tela 1 é retórica (lição do revisor em 14/10: não pedir "responde no direct").
- **Link da bio:** `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-15-stories-quinta-de-estreia`. O slug de humor ainda não foi confirmado, então o link vai sem humor.
- **`"series"`:** ["The Paper", "A Diplomata", "Carrie, a Estranha"].
- **Horário:** Instagram STORIES `2026-10-15T10:00:00-03:00` (mesmo fallback do 01).

## 03-lista-da-mia-terror-de-cidade-pequena (YouTube · Lista da MIA 16:9 · 12h00)
- **Formato:** Lista da MIA, 1920×1080, **~2 min**, contagem regressiva de **4 séries** (nº 1 por último).
  - Vídeo: `motor/exemplos/lista-da-mia-16x9.html`, `<body class="paisagem" style="--mood:var(--estressado)">`.
  - Thumb: `motor/exemplos/lista-da-mia-thumb.html` com **"4"** gigante + "TERROR DE CIDADE PEQUENA" + 🌊.
- **Pilar:** 1. Série pro seu humor (o humor é "com vontade de medo"; o tema veio da tendência) · **Job:** principal · **Humor / `--mood`:** estressado (a cor de medo/tensão, a mesma usada para terror em 14/10).
- **Eixo:** **gênero/subgênero.** **Tema:** terror de cidade pequena, puxado por *Profundezas*.
- **Por que é tendência (3 sinais):**
  1. **Top 10 Brasil:** *Profundezas* foi a **série mais vista da Netflix no Brasil na semana de 5 a 11/10**, à frente de *Percy Jackson*, *A Leste do Éden*, *Um Choque de Amor* e *Habeas Corpus* ([Revista Bula](https://www.revistabula.com/169299-5-series-mais-vistas-netflix-brasil-outubro-2026/); [Oficina da Net](https://www.oficinadanet.com.br/lancamentos-netflix/73295-essa-serie-lidera-top-10-semana-netflix-veja-trailer)).
  2. **Topo mundial:** 17 milhões de visualizações no mundo em 5–11/10, número global ([A Tarde](https://atarde.com.br/cineinsite/minisserie-da-netflix-bate-recorde-mundial-com-17-milhoes-de-views-1405738); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000227377/); [Einerd](https://www.einerd.com/profundezas-below-serie-terror-netflix/)).
  3. **Conversa e demanda:** a Omelete publicou "final explicado" ([Omelete](https://www.omelete.com.br/series-tv/profundezas-final-explicado-como-termina-serie-netflix)), sinal de público terminando a série e procurando mais. Há também a crítica ([Omelete](https://www.omelete.com.br/series-tv/criticas/profundezas-boa-serie-netflix-critica)) e a comparação com Stephen King ([AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000217242/)). Some-se o **mês do Halloween**, com 22 filmes de terror entrando na Netflix em outubro ([GameOverDrive](https://gameoverdrive.com.br/filmes-terror-netflix-outubro-2026-halloween/)).
  - **Lacuna:** não há sinal direto de Google Trends, X ou TikTok (busca vazia, WebFetch bloqueado). Também não achei o Top 10 de 12–18/10, que ainda não fechou.
  - **Na peça, dizer "liderou a Netflix no Brasil na semana passada".** Não dizer "a mais vista agora".
- **Título (≤ 70):** **"Profundezas e mais 3 séries de terror de cidade pequena"** (55 caracteres).
- **Gancho (0–15 s):** "Sabe aquele medo que começa quando a cidade é pequena demais pra alguém fugir? *Profundezas* liderou a Netflix no Brasil na semana passada. Eu separei mais três com esse mesmo arrepio." Sem nada do final de *Profundezas*.
- **Séries (contagem regressiva):**
  4. ***IT: Bem-vindos a Derry***: HBO Max, 1ª temporada com 8 episódios. Renovada para a 2ª, ainda sem data.
     - Fontes: [Omelete](https://www.omelete.com.br/series-tv/it-bem-vindos-a-derry-renovacao-2a-temporada-teaser), [Diário do Nordeste, ago/2026](https://diariodonordeste.verdesmares.com.br/entretenimento/zoeira/it-bem-vindos-a-derry-e-renovada-para-2-temporada-pela-hbo-max-confira-as-novidades-1.3784767).
     - Por que combina: uma cidade inteira escondendo um medo antigo. Pra quem não é: quem não aguenta violência explícita nem palhaço.
  3. ***Missa da Meia-Noite***: Netflix, minissérie de 7 episódios, de Mike Flanagan.
     - Fontes: [AdoroCinema](https://www.adorocinema.com/series/serie-25310/), [A Tarde](https://atarde.com.br/cineinsite/so-7-episodios-a-serie-de-terror-da-netflix-ideal-para-sua-segunda-1384677).
     - Por que combina: uma ilha isolada e uma comunidade que muda devagar. Pra quem não é: quem quer susto rápido, porque ela é lenta e fala muito de fé.
     - ⚠️ Não há fonte de catálogo de 2026, só a de que é original Netflix. **O revisor confirma.**
  2. ***Stranger Things***: Netflix, 5 temporadas, série encerrada (o final saiu em 31/12/2025, [Times Brasil](https://timesbrasil.com.br/brasil/stranger-things-5-a-que-horas-estreia-o-episodio-final-na-netflix/)).
     - Ponte com a tendência: Charlie Heaton, o Jonathan, está em *Profundezas* ([Einerd](https://www.einerd.com/profundezas-below-netflix-charlie-heaton/)).
     - Por que combina: cidade pequena, um mistério e amizade no meio do medo. Pra quem não é: quem não quer começar uma série de 5 temporadas hoje.
  1. ***Profundezas***: Netflix, minissérie de 6 episódios, todos desde 08/10/2026, com Josh Hartnett. Título original: *Below*.
     - Fontes: [GameOverDrive](https://gameoverdrive.com.br/profundezas-netflix-quando-estreia-episodios-elenco/), [Einerd](https://www.einerd.com/profundezas-below-serie-terror-netflix/), [Omelete](https://www.omelete.com.br/series-tv/profundezas-netflix-josh-hartnett-serie-teaser-trailer).
     - Por que combina: um pescador protegendo a família numa vila no Canadá quando algo do mar começa a atacar. É só a premissa oficial; sem descrever o monstro.
     - Pra quem não é: quem tem medo de mar.
  - **Reservas** (se faltar pôster ou confirmação): *Carrie, a Estranha* (Prime Video, 8 episódios, 07/10; fontes no card 4 do carrossel) e *Hotel Assombrado* (Netflix; a T2 foi anunciada para 09/10 ([Einerd](https://www.einerd.com/hotel-assombrado-segunda-temporada-ganha-data-de-estreia-e-trailer-assista/)), mas o lançamento não foi confirmado, então só citar a T1, e o tom é de comédia).
- **Pôsteres:** `python scripts/posters.py <pasta> "Below (2026)" "Stranger Things" "Midnight Mass" "IT: Welcome to Derry"`. Em *Below*, conferir o ano 2026 e o elenco (Josh Hartnett). Recortar logo de streaming se houver, sem filtro (como em 14/10).
- **Demo do app:** não entra (`assets/demo/` está vazio).
- **Fim e CTA único:** "**Salva pra hoje à noite**" (Consideração) + link fixado. Sem pergunta pros comentários, seguindo a mesma decisão de 14/10 (regra 6). O comentário fixado lista onde assistir cada série, sem pedido.
- **Spoiler:** zero, em todas.
- **Descrição:** capítulos (00:00 abertura, depois um capítulo por série; calcular pelo `narracao.json` + 0,30 s, lição de 14/10), onde assistir de cada série e a UTM `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-15-lista-da-mia-terror-de-cidade-pequena`.
- **Tags:** profundezas, below netflix, séries de terror, terror netflix, stranger things, missa da meia-noite, it bem-vindos a derry, josh hartnett, halloween.
- **`"series"`:** ["Profundezas", "Stranger Things", "Missa da Meia-Noite", "IT: Bem-vindos a Derry"].
- **Horário:** YouTube `2026-10-15T12:00:00-03:00`.

## 04-short-reels-relogio-a-diplomata-voltou (YouTube Short + Instagram Reels · 13h30 · **o mesmo vídeo**)
- **Decisão:** é um arquivo 9:16 só, publicado nas duas redes. O `publicar.json` tem duas publicações (`YOUTUBE_SHORT` + `REELS`), ambas com `quando` às 13h30.
- **Formato:** 9:16, 25–30 s, narração da MIA. **Formato recorrente: Relógio / ritual** (`09`). Antes de criar, abrir `motor/exemplos/relogio-catalogo.html` e a folha de quadros do "Quarta, 21h" em `referencias/`. Não copiar o fecho de recibo do Short de 14/10.
- **Pilar:** 2. Órfã de série (a série que ela esperava voltou) · **Job:** emocional 3 · **Humor:** estressado / adrenalina (`--estressado`).
- **Gancho (0–2 s, fala + tela):** "**Pra amiga que tá contando os dias pra *A Diplomata* voltar.**" O relógio abre em 13:30: "quinta, hora do almoço… e eu já sei o que vou ver hoje à noite." Virada: "voltou. Oito episódios. De uma vez." (contador 0→8).
- **Série:** ***A Diplomata*, 4ª temporada**, **Netflix**, **hoje, 8 episódios de uma vez** (fontes no card 3 do carrossel). Pra quem não é: quem nunca viu as temporadas anteriores.
  - **Proibido:** citar hora de estreia; dizer "desde o ano passado" (a data da T3 não foi checada hoje); qualquer coisa do final da T3 (arma, Hal, Grace Penn).
- **Fecho / CTA:** botão brasa "**MANDA PRA QUEM PRECISA**" + @seriecerta (Descoberta). Um só.
- **Legenda IG:** gancho + "A Diplomata T4, Netflix, 8 episódios de uma vez." + "Manda pra quem precisa." Hashtags: #adiplomata #seriecerta #oqueassistir #netflix. **Título YT Short:** "A Diplomata voltou: 8 episódios de uma vez".
- **Capa:** o quadro do contador "8".
- **Pôster:** `python scripts/posters.py <pasta> "The Diplomat"`. Recortar o logo Netflix se houver.
- **`"series"`:** ["A Diplomata"].
- **UTM (descrição YT):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-15-short-relogio-a-diplomata-voltou`.
- **Horários:** YouTube Short `2026-10-15T13:30:00-03:00` · Instagram REELS `2026-10-15T13:30:00-03:00` · TikTok: mesmo arquivo + `tiktok.txt`.

## 05-reels-selvagens-do-sofa-ep03-quinta-de-estreia (Instagram Reels · 18h30)
- **Formato:** 9:16, 30–35 s, narração da MIA em tom de documentário. **Formato recorrente: Selvagens do Sofá, Ep. 03** (`09`): binóculo, registro de campo, legenda grande sincronizada. Base: a folha de quadros do Selvagens em `referencias/` e o Ep. 02 (`saida/2026-10-13/`). Não repetir piada do Ep. 02.
- **Pilar:** 1. Série pro seu humor (diferente do pilar 2 do Reels das 13h30) · **Job:** principal · **Humor:** romântico / leve (`--romantico`).
- **Gancho (0–2 s):** "**Pro amigo que abre três estreias na quinta e assiste zero.**" Registro de campo: "quinta-feira, 21h. O brasileiro adulto detecta três estreias. Abre todas. Assiste aos trailers. Nenhum episódio." Isso é situação, sem citar séries da concorrência.
- **Virada / indicação:** "Quando o cansaço vence o hype, a natureza pede algo leve." Série: ***Um Choque de Amor***, Netflix, dorama de comédia romântica, **10 episódios, todos desde 09/10**. Esteve no Top 10 do Brasil em 5–11/10 (4º lugar segundo a [Revista Bula](https://www.revistabula.com/169299-5-series-mais-vistas-netflix-brasil-outubro-2026/)).
  - Fontes: [GameOverDrive](https://gameoverdrive.com.br/um-choque-de-amor-historia-elenco-serie-netflix/), [A Crítica](https://acritica.net/entretenimento/um-choque-de-amor-netflix/), [Omelete](https://www.omelete.com.br/korea/um-choque-de-amor-dorama-netflix-trailer).
  - ⚠️ Uma fonte anterior à estreia falava em 12 episódios. **O revisor confirma "10" ou a fala não cita o número.**
  - Pra quem não é: quem quer algo tenso hoje.
- **Fecho / CTA:** "MANDA PRA QUEM PRECISA" + @seriecerta (Descoberta). Um só.
- **Pôster:** `python scripts/posters.py <pasta> "Um Choque de Amor"`. Se não achar, buscar "Take Charge of My Heart" ([What's on Netflix](https://www.whats-on-netflix.com/news/k-dramas/take-charge-of-my-heart-netflix-release-date-october-2026/)) ou "Charge Me Up" ([Khan](https://sports.khan.co.kr/en/article/202609100923007)), e conferir 2026, Kim Young-kwang e Chae Soo-bin.
  - **Reserva** sem pôster: *The Paper* T2 (HBO Max, com o humor "exausto"; sem a piada do The Office).
- **`"series"`:** ["Um Choque de Amor"].
- **Legenda:** gancho + "Um Choque de Amor, Netflix." + "Manda pra quem precisa." Hashtags: #selvagensdosofa #seriecerta #dorama #oqueassistir.
- **Horário:** Instagram REELS `2026-10-15T18:30:00-03:00` · TikTok: mesmo arquivo.
- **Fallback 19h00:** se a 06 não for narrada, este arquivo vai também como YouTube Short às `2026-10-15T19:00:00-03:00`, com UTM `utm_campaign=2026-10-15-short-selvagens-ep03` (ver "Capacidade").

## 06-short-tradutor-o-que-a-mia-entende (YouTube Short · 19h00)
- **Formato:** 9:16, ~25 s, narração da MIA. **Formato recorrente: Tradutor de indicação** (`09`): "o que você diz" → seta → "o que a MIA entende" (card brasa) + emoji, em 4 itens. Base: `referencias/` (Tradutor) e o Short de 13/10.
- **Pilar:** 5. Bastidor do produto (diferente do pilar 2 do Short das 13h30) · **Job / força:** Atração (nova solução) · **Humor:** vários (4 cores).
- **Gancho (0–2 s):** "**Pra amiga que pede indicação e responde 'qualquer coisa'.**"
- **Traduções (só o que o app faz, segundo `04-proposta-de-valor.md`):**
  1. "qualquer coisa" → "tô cansada, quero leve" (`--sono`).
  2. "nada muito pesado" → "hoje eu tô ansiosa" (`--ansioso`).
  3. "algo tipo aquela que acabou" → "tô órfã" (`--triste`).
  4. "tanto faz, você escolhe" → "quero acertar de primeira" (`--feliz`).
  - Fecho: "A MIA começa pelo seu humor, diz onde assistir e avisa pra quem não é."
  - **Não prometer** o que o app não faz: nada de "lê sua mente", nada de "assiste com você", nada de números de uso.
- **Séries:** nenhuma indicação → `"series": []`, sem pôster.
- **Fecho / CTA:** "MANDA PRA QUEM PRECISA" + @seriecerta (Descoberta). Um só. Sem "comenta mais traduções", para não somar um 2º CTA.
- **Título YT:** "Tradutor oficial: o que você quer dizer quando pede série".
- **UTM:** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-15-short-tradutor-o-que-a-mia-entende`.
- **Horário:** YouTube Short `2026-10-15T19:00:00-03:00` (4º na fila de narração; ver o fallback acima).

**Pilares de hoje:** 1 (carrossel, Stories, Lista, Reels 18h30), 2 (Short/Reels 13h30) e 5 (Short 19h).
- Não há pilar repetido nos dois Reels (2 × 1) nem nos dois Shorts (2 × 5).
- Se a 06 cair no fallback, os Shorts ficam 2 × 1, que continua sem repetição.
- Na semana, os pilares 3 (casal) e 4 (prova) entram a partir de sexta.

---

# RASCUNHO DE AMANHÃ: sexta-feira, 2026-10-16
> Grade diária. **Casal obrigatório na sexta à noite** (`08`). A rotina de amanhã refaz a pesquisa de tendência e **revalida todos os fatos**. Pasta: `saida/2026-10-16/`.
> **Capacidade:** para economizar crédito, o vídeo do casal ocupa os dois slots da noite (Reels 18h30 + Short 19h00, um arquivo, redes diferentes).

## 01-carrossel-<sexta> (10h00) + 02-stories (10h00)
- **Pilar 4 (prova)** ou **pilar 1**. Proposta: "Minisséries pra terminar no fim de semana" (6 episódios ou menos), humor "quero fechar algo".
- Candidatas a revalidar: *Sentimento Louco* (4 episódios, Prime Video, estreia 16/10), *Missa da Meia-Noite* (só se não for usada na Lista de hoje; **é usada**, então fora) e outras a pesquisar.
- **Stories:** o carrossel em 9:16 + CTA de Conversão ligado ao **modo casal**: "Testa o modo casal grátis no link da bio". Se o modo casal não estiver confirmado na bio/link, usar o CTA padrão.

## 03-lista-da-mia-<tema> (12h00)
- **Eixo diferente de ontem e de hoje** (foram "acabou X?" e gênero). Propostas:
  - **(a) plataforma/momento:** "o melhor que chegou no Prime Video em outubro" (*Sentimento Louco* 16/10, *Carrie* 07/10, *True Blood* desde 05/10; revalidar todas);
  - **(b) por pessoa/estreia:** *Marília Mendonça: Sentimento Louco* como gancho de "séries documentais sobre música brasileira". Só se houver de 3 a 7 séries com onde assistir confirmado no Brasil hoje. Tom respeitoso.
- `--mood`: triste (b) ou curioso (a). A nº 1 não pode ser *Olhos que Condenam* nem *Profundezas*.

## 04-short-reels-qual-sexta-e-voce (13h30, YouTube + Instagram, mesmo vídeo)
- Adaptação do Reels bloqueado de 14/10 ("Qual quarta é você?"). Formato **Qual é você?**, pilar 1, CTA "Manda pra quem precisa".
- **Refazer os 4 tipos e as séries** sem repetir série + humor das peças de 15/10. Exemplo: a exausta → *The Paper* T2 já foi usada no carrossel de hoje com "exausta", então trocar.
- Reconfirmar todos os fatos (o roteiro de 14/10 tem frases que já venceram, como "chega amanhã").

## 05-reels-casal-<tema> (18h30 Reels + 19h00 Short, mesmo arquivo)
- **Pilar 3. Dilema do casal** · Job social 1 · vozes Ela (`1AxHVMpXJZxq6ECdF4Kn`) e Ele (`oeBFFQkxcUHweNreD1nw`).
- Esquete "sexta à noite, o que a gente vê?". Uma série que agrade os dois, por exemplo um thriller com romance, a escolher amanhã.
- Não repetir *Hotel Assombrado* nem o gancho "mão na cara" de 09/10.
- CTA: "Manda pra quem precisa" (Descoberta), um só.

---

## Ideias guardadas (revalidar antes de usar)
- *Ninguém Quer* T3 (Netflix, 22/10): pilar 2 na semana que vem.
- *Lupin* parte 4 (Netflix, 23/10, [Showmetech](https://www.showmetech.com.br/lancamentos-da-netflix-em-outubro-de-2026/)).
- *Largados e Pelados Brasil* T4 (HBO Max, 18/10, [Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/)): reality, só se casar com um humor.
- *A Leste do Éden* (Netflix, 01/10, Florence Pugh), 3ª no Top 10 de 5–11/10: possível Lista por atriz.
- *Percy Jackson* (2ª no Top 10 de 5–11/10): conferir se é série ou filme e o que está na Netflix BR.

## Pendências para o Bruno
1. **Créditos ElevenLabs:** confirmar a recarga. O dia todo pede ~3.100 caracteres. Sem crédito, só saem carrossel + Stories.
2. **Slug `humor=<humor>`** no app: segue sem confirmação. Os links vão sem humor.
3. **DNS/proxy:** netflix.com, flixpatrol.com, revistabula.com e gameoverdrive.com.br falham no WebFetch, então não dá para conferir catálogo direto. Vale bater o olho no app em *Missa da Meia-Noite* (Netflix), *IT: Bem-vindos a Derry* (HBO Max) e *The Paper* T2 (HBO Max, hoje).
4. **Bio do Instagram:** trocar para o link do Stories de hoje antes das 10h00. É manual.
5. **"Respondendo seu humor (parte 2)":** a promessa do "Quarta, 21h" continua em aberto. Não chegou `comentarios.md`.
