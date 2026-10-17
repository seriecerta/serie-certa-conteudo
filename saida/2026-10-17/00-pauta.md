# Pauta: sábado, 2026-10-17 (America/Sao_Paulo)

**Grade:** a grade diária de `08-cronograma.md`: carrossel e Stories às 10h00, Lista da MIA às 12h00 (YouTube 16:9), Short e Reels às 13h30, Reels às 18h30 e Short às 19h00. Blog às 09h, 11h, 14h, 17h e 20h (`11-blog.md`).
**Meta dos 90 dias:** audiência, com orçamento zero (`05`). Reels, Shorts e casal fecham com "Manda pra quem precisa".
**Período de base (14 a 20/10):** grade fixa, sem teste A/B. O registro de `10-experimentos.md` está vazio, então nenhuma peça leva `experimento`.

**O que mudou em relação ao rascunho de ontem** (`saida/2026-10-16/00-pauta.md`):
- **Carrossel:** saiu o pilar 5 ("O que a MIA te pergunta"). Sem crédito, o carrossel e os Stories são as únicas peças de rede com saída garantida. Por isso, este slot vai para a maior tendência confirmada da semana: *A Leste do Éden*, nº 1 global da Netflix entre as séries em inglês e nº 1 em 25 países na semana de 5 a 11/10 (pilar 2). O pilar 5 passa para o Tradutor de domingo.
- **18h30/19h:** sai a peça "órfã" nova. Entra o **casal de 16/10, reaproveitado** ("sexta" vira "sábado"). Ele não foi publicado, já tem roteiro e pôster, e o pilar 3 ainda não teve nenhuma peça na semana. A regra da sexta não foi cumprida ontem, e sábado à noite é o mesmo momento do casal.
- **Lista:** o eixo é **criador** (Mike Flanagan), puxado por *Carrie* (nº 1 global do Prime Video na semana de 5 a 11/10) e pelo mês do Halloween. A Lista de thrillers políticos de 16/10 **não volta**: a versão em texto já saiu no blog (`series-parecidas-com-a-diplomata`), e repetir o tema às 20h quebraria a regra de 60 dias do blog.
- **Selvagens Ep. 03:** fica às 13h30, como estava no rascunho. **Tradutor:** passa para domingo, às 13h30.

## Capacidade e prioridade de narração (ElevenLabs)
Em 16/10 sobraram **29 créditos**, e a primeira fala, de 34, não passou (APRENDIZADOS, 15/10). Não há registro de recarga. **Assuma que nenhum vídeo sai.** Antes de narrar, cheque o saldo: 1 caractere = 1 crédito.

| Ordem | Pasta | Slots que cobre | Narração | Custo estimado |
|---|---|---|---|---|
| **1º** | `05-reels-short-casal-sabado-escolhe-voce` (Reels 18h30 + Short 19h00) | **2** | Ela + Ele, 9 falas, roteiro pronto de 16/10 | **~435 caracteres** |
| **2º** | `04-short-reels-selvagens-ep03-sabado` (Short + Reels 13h30) | **2** | MIA, roteiro pronto de 15/10 | **~505 caracteres** |
| **3º** | `03-lista-da-mia-mike-flanagan` (12h00) | 1 | MIA, 5 séries, ~1 min 45 s | **~1.500 caracteres** |

- **Total:** ~2.440 caracteres. As duas primeiras cobrem 4 slots com ~940.
- **Narre uma pasta por vez, nesta ordem.** Pare no primeiro `quota_exceeded` e não tente de novo (`python scripts/narrar.py saida/2026-10-17/<pasta>`). Nunca use outro voice_id nem outro TTS.
- **Ordem de produção ≠ ordem de narração.** Os roteiros prontos (04 e 05) só precisam da troca de dia e da rechecagem de fatos. O roteiro da Lista é escrito do zero, mas é o último a gastar crédito.
- **Se o saldo ficar entre ~1.150 e ~1.500 depois do 1º e do 2º:** corte o bloco do nº 5 da Lista (*O Clube da Meia-Noite*) antes de narrar. Abaixo de ~1.150, a Lista não é narrada e entra no `99-revisao.md` como slot não cumprido.
- **Sem crédito nenhum:** saem só o carrossel, os Stories e o blog (nada disso gasta crédito). Os roteiros, os `.txt` e os pôsteres ficam prontos.
- **Peças das 10h00:** se não estiverem aprovadas até 9h50, saem às 11h00. Se não estiverem até 10h50, saem às 15h00 (`08`). Registre no `99-revisao.md`.

## Histórico (regra de 30 dias: `historico/publicados.md` + `saida/2026-10-16/99-revisao.md`)
- **16/10 publicou** o carrossel e os Stories "minisséries pro fim de semana" (*A Leste do Éden*, *O Gambito da Rainha*, *Mare of Easttown*, *Chernobyl*) e as 5 matérias do blog. **Não saíram** a Lista de thrillers, o "Qual sexta é você?" e o casal (sem crédito).
- ***A Leste do Éden*** foi indicada em 16/10 com o humor "curiosa" e o gancho "minisséries pro fim de semana". Hoje ela **não é indicada**: aparece só como gancho ("acabou?"), com outro humor (órfã) e outro gancho. O pôster entra no card 1, então ela entra no `"series"` (lição do revisor de 15/10).
- ***Carrie*** foi gancho ou indicação em 13/10 e 15/10. Na Lista de hoje ela é **só gancho** (pôster na abertura, e por isso entra no `"series"`). Não está na contagem.
- ***Residência Hill*** foi citada no gancho do Tradutor de 13/10 e listada no blog de 16/10 (*Profundezas*). Na Lista de hoje, com o eixo "criador" e um gancho novo, ela pode ser a nº 1: o nº 1 dos últimos 30 dias foi *Olhos que Condenam* (14/10).
- ***Sr. e Sra. Smith*** e ***Um Choque de Amor*** nunca foram publicadas. O casal de 09/10 usou *Hotel Assombrado* com o gancho "mão na cara", e o de hoje tem outra série e outro gancho.
- **Eixos da Lista na semana:** 14/10 "acabou X?" (publicada) · 15/10 gênero (não saiu) · 16/10 gênero (não saiu) · **17/10 criador** · 18/10 humor ou plataforma (rascunho abaixo).
- **Matéria do blog com data de 17/10 no `--listar`:** `series-parecidas-com-a-diplomata` é a matéria 05 de **16/10**, publicada às 21h00 de Brasília, que já é 00h00 de 17/10 em UTC. Não é um pacote agendado novo. O tema não se repete hoje.

## Nota de verificação
- **WebFetch caiu em DNS** (ENOTFOUND) em flixpatrol.com e whats-on-netflix.com, então tudo foi checado por WebSearch em 17/10.
- **Não há Top 10 da Netflix Brasil desta semana** nas buscas. Nenhuma peça afirma posição no ranking **brasileiro**. Dá para dizer "nº 1 da Netflix no mundo entre as séries em inglês" (*A Leste do Éden*) e "nº 1 do Prime Video no mundo" (*Carrie*), sempre com fonte.
- **Não afirmar** duração de episódio, horário de estreia nem nº de temporadas que esteja marcado com ⚠️, a não ser que o revisor confirme.
- Os títulos antigos e não originais da plataforma ficam com ⚠️. **O revisor confirma no app ou no JustWatch BR antes de aprovar.** Série sem confirmação sai e a reserva entra.

---

# HOJE: 2026-10-17

## 01-carrossel-acabou-a-leste-do-eden (Instagram · Carrossel · 10h00)
- **Formato:** 7 cards de 1080×1350 (`--imagens --formato 4x5`), um `section.quadro` por card. Sem narração.
- **Pilar:** 2. Órfã de série · **Job:** emocional 3 (acabei uma série que amei e quero a mesma sensação) · **Humor:** órfã, com `--triste` no card 1 e a cor de cada série nos cards seguintes.
- **Estágio / CTA:** Consideração · "**Salva pra hoje à noite.**" (um só).
- **Formato de referência:** card de indicação com selo "onde assistir" + recibo (`saida/2026-10-16/01-carrossel-minisseries-pro-fim-de-semana/`).
- **Gancho (card 1):** "Terminou *A Leste do Éden* e ficou com aquele vazio?" Subtítulo: "4 séries pra continuar sentindo a mesma coisa." Pôster de *A Leste do Éden* + 🫠.
- **Por que agora:** a minissérie (7 episódios, todos desde 01/10) foi nº 1 da Netflix no mundo entre as séries em inglês na estreia, com 6,5 mi de visualizações. Na semana de 5 a 11/10 chegou a 12,6 mi e ficou em nº 1 em 25 países ([Mac Observer](https://www.macobserver.com/entertainment/east-of-eden-is-netflixs-no-1-show-how-florence-pughs-cathy-ames-drama-reached-6-5-million-views/); [Selectra, Top 10 do Reino Unido](https://selectra.co.uk/tv-broadband/news/netflix-uk-top-10-week-below-east-of-eden-animals-ice-age); [Canaltech](https://canaltech.com.br/entretenimento/a-leste-do-eden-nova-serie-com-florence-pugh-e-grande-aposta-da-netflix-conheca/)). Não há Top 10 brasileiro: **não dizer "a mais vista do Brasil"**. O primeiro fim de semana depois de duas semanas no topo é a hora do "e agora?".
- **Cards:**
  2. ***Ripley*** · Netflix · minissérie de 8 episódios (abr/2024), com Andrew Scott. **Não terá 2ª temporada** ([Netflix About](https://about.netflix.com/news/ripley-starring-andrew-scott-to-premiere-on-netflix); [AdoroCinema, 29/05/2026](https://www.adorocinema.com/noticias/series/noticia-1000128582/)). Por que combina: adaptação de romance clássico, protagonista que você não consegue largar mesmo sem confiar nela. Pra quem não é: quem quer ritmo rápido (é lenta e em preto e branco). `--curioso`.
  3. ***Pachinko*** · Apple TV · saga de uma família coreana ao longo de gerações, baseada no romance de Min Jin Lee ([Omelete, crítica da T2](https://www.omelete.com.br/series-tv/criticas/pachinko-2a-temporada-apple-tv); [Apple TV Press](https://apple.com/tv-pr/news/2024/07/apple-tv-debuts-trailer-for-highly-anticipated-second-season-of-its-critically-acclaimed-drama-pachinko-premiering-friday-august-23)). Por que combina: legado de família e escolhas que atravessam décadas. Pra quem não é: quem não curte legenda (tem coreano, japonês e inglês). ⚠️ **Não citar nº de temporadas** sem o revisor confirmar se há T3. É original Apple, então o risco de catálogo é baixo. `--romantico`.
  4. ***Peaky Blinders*** · Netflix · 6 temporadas, e o filme *O Homem Imortal* chegou à Netflix em 20/03/2026 ([Diário do Pará](https://diariodopara.com.br/cinema/peaky-blinders-ganha-filme-epico-veja-onde-assistir/); [Sopa Cultural](https://sopacultural.com/peaky-blinders-o-homem-imortal-ganha-data-de-estreia-na-netflix-para-marco-de-2026/)). Por que combina: irmãos, poder e família no começo do século 20. Pra quem não é: quem não aguenta violência. ⚠️ O revisor confere as 6 temporadas na Netflix BR. `--estressado`.
  5. ***Succession*** · HBO Max · 4 temporadas, série encerrada ([Omelete](https://www.omelete.com.br/series-tv/com-familia-dividida-succession-retorna-afiada-para-sua-despedida); [Claro](https://www.claro.com.br/amp/stories/tv/assistir-succession)). Por que combina: irmãos disputando a herança de um pai difícil. Pra quem não é: quem quer gostar de alguém (ninguém presta). ⚠️ **Não há fonte de 2026 para o HBO Max BR.** O revisor confirma. Se não confirmar, o card sai e o carrossel fica com 3 séries + recibo + CTA (6 cards). `--animado`.
  6. **Recibo "o mapa do órfão"** (cupom do motor): série → streaming das que ficaram. Não indica série nova.
  7. **CTA:** "Salva pra hoje à noite." + @seriecerta.
- **Spoiler zero:** de *A Leste do Éden*, só a premissa (família, irmãos, "uma mulher que ninguém consegue decifrar"). Nada da Cathy além disso, nada do final.
- **Legenda:** gancho + "Ripley (Netflix) · Pachinko (Apple TV) · Peaky Blinders (Netflix) · Succession (HBO Max)" + "Salva pra hoje à noite." No máximo 2 emojis. Hashtags: #seriecerta #oqueassistir #alestedoeden #dicadeserie.
- **Comentário fixado:** só onde assistir cada série, sem pedido (padrão de 15 e 16/10).
- **Pôsteres:** `python scripts/posters.py <pasta> "East of Eden (2026)" "Ripley" "Pachinko" "Peaky Blinders" "Succession"`. *East of Eden* = TVmaze #79399 (já conferido pelo revisor em 16/10; dá para copiar de `saida/2026-10-16/01-.../imagens/east-of-eden.jpg`). *Ripley* é a de 2024 com Andrew Scott, não outra. Logos de streaming ficam fora do recorte.
- **`"series"`:** ["A Leste do Éden", "Ripley", "Pachinko", "Peaky Blinders", "Succession"] (tirar *Succession* se o card sair).
- **Horário:** Instagram CAROUSEL `2026-10-17T10:00:00-03:00` (se atrasar, 11h00 e depois 15h00).

## 02-stories-acabou-a-leste-do-eden (Instagram · Stories · 10h00)
- **Formato:** o carrossel 01 em 9:16 (1080×1920), **4 telas + 1 de CTA**. Pode usar `"peca_mae": "01-carrossel-acabou-a-leste-do-eden"`. Sem narração.
- **Pilar:** 2 · **Job:** emocional 3 · **Humor:** órfã.
- **Telas:** 1. "Terminou *A Leste do Éden*?" (pôster) · 2. *Ripley* (Netflix) · 3. *Pachinko* (Apple TV) · 4. *Peaky Blinders* (Netflix) · 5. CTA.
- **CTA / funil:** Conversão, um só: "**A MIA acha a próxima pelo seu humor. Testa grátis no link da bio.**" Sem enquete e sem "responde no direct".
- **Link da bio:** `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-17-stories-acabou-a-leste-do-eden` (sem `humor=`, porque o slug não está confirmado).
- **`"series"`:** ["A Leste do Éden", "Ripley", "Pachinko", "Peaky Blinders"].
- **Horário:** Instagram STORIES `2026-10-17T10:00:00-03:00` (mesmo plano de atraso do 01).

## 03-lista-da-mia-mike-flanagan (YouTube · Lista da MIA 16:9 · 12h00)
- **Formato:** Lista da MIA em 1920×1080, **~1 min 45 s**, contagem regressiva de **5 séries** (a nº 1 por último). Vídeo: `motor/exemplos/lista-da-mia-16x9.html` com `<body class="paisagem" style="--mood:var(--estressado)">`. Thumb: `motor/exemplos/lista-da-mia-thumb.html` com o **"5"** gigante, "SÉRIES DO MIKE FLANAGAN" e 🕯️.
- **Pilar:** 1. Série pro seu humor (humor "quero medo bom no fim de semana"; o tema vem da tendência) · **Job:** principal (secundário: emocional 3, para quem terminou *Carrie*) · **`--mood`:** estressado (medo e tensão).
- **Eixo:** **criador/diretor**, pela primeira vez na semana. **Tema:** "*Carrie* é do Mike Flanagan: as séries dele pra ver até o Halloween".
- **Por que é tendência (3 sinais):**
  1. **Estreia em alta:** *Carrie* (Prime Video, 8 episódios, todos em 07/10, criação de Mike Flanagan) estreou em **nº 1 no ranking global de séries originais do Prime Video** na semana de 5 a 11/10, no ranking divulgado pela Amazon em 14/10 ([Selectra](https://selectra.co.uk/tv-broadband/news/prime-video-top-10-carrie-number-one-first-week-kill-jackie); [ozap, FlixPatrol no dia seguinte](https://www.ozap.com/actu/prime-video-24-heures-apres-sa-sortie-cette-serie-de-science-fiction-epoustouflante-simpose-au-sommet-du-top-mondial-et-detrone-neagler-et-reacher/657377); [Omelete, crítica de 02/10](https://www.omelete.com.br/series-tv/criticas/carrie-acerta-ao-atualizar-classico-de-stephen-king-com-a-assinatura-de-mike-flanagan)).
  2. **Mês do terror nos streamings:** a Netflix Brasil pôs 22 filmes de terror no catálogo entre 2 e 23/10 por causa do Halloween ([GameOverDrive](https://gameoverdrive.com.br/filmes-terror-netflix-outubro-2026-halloween/)). *Crystal Lake* estreou na sexta (16/10) no Universal+, e *American Horror Story* 13 tem episódios semanais no Disney+ até o fim do mês ([Canaltech](https://canaltech.com.br/entretenimento/lancamentos-do-disney-em-outubro-mes-tem-serie-do-visao-e-terror-para-o-halloween/); [Oficina da Net](https://www.oficinadanet.com.br/disney-plus/73211-lancamentos-disney-plus-outubro-2026)).
  3. **Conversa sobre o Flanagan:** a imprensa trata *Carrie* como a série que está "empolgando o público" no Prime Video ([kino.de](https://www.kino.de/serie/carrie--01KXJ4J1JKTRW6487Z1FPJQ76Y/news/)). Há listas fixas no Brasil de "séries do Mike Flanagan" ([Canaltech](https://canaltech.com.br/entretenimento/melhores-filmes-e-series-de-mike-flanagan/); [Olhar Digital](https://olhardigital.com.br/2023/10/21/cinema-e-streaming/gostou-de-a-queda-da-casa-de-usher-veja-estes-5-filmes-e-series-do-diretor-mike-flanagan/)): é a busca natural de quem terminou *Carrie*.
  - **Lacuna:** não há sinal direto de Google Trends, X ou TikTok no Brasil (buscas vazias, FlixPatrol bloqueado), nem Top 10 brasileiro do Prime Video. **Na peça, diga "nº 1 do Prime Video no mundo na semana de estreia". Não diga "a mais vista do Brasil".**
- **Título (≤ 70):** **"Carrie é do Mike Flanagan: 5 séries dele pra ver até o Halloween"** (64 caracteres).
- **Gancho (0–15 s):** "Sabe aquele medo que dá vontade de chorar junto? Se você terminou *Carrie*, você conheceu o Mike Flanagan. E ele tem mais cinco esperando por você." Pôster de *Carrie* na abertura. Spoiler zero: de *Carrie*, só que é a nova versão do clássico de Stephen King.
- **Séries (contagem regressiva; todas Netflix, originais da plataforma; fonte do conjunto: [Canaltech](https://canaltech.com.br/entretenimento/melhores-filmes-e-series-de-mike-flanagan/), [Olhar Digital](https://olhardigital.com.br/2023/10/21/cinema-e-streaming/gostou-de-a-queda-da-casa-de-usher-veja-estes-5-filmes-e-series-do-diretor-mike-flanagan/) e a coleção Flanagan da Netflix com as 5 séries de 2018 a 2023, citada pela busca a partir da Netflix Portugal):**
  5. ***O Clube da Meia-Noite*** · Netflix · 1 temporada (2022), cancelada. Por que combina: jovens contando histórias de terror à noite, é o Flanagan mais leve. Pra quem não é: quem odeia final em aberto (a série acabou sem continuação). ⚠️ O revisor confirma o catálogo e o nº de episódios.
  4. ***A Maldição da Mansão Bly*** · Netflix · 1 temporada (2020). Por que combina: história de fantasma que é, no fundo, história de amor. Pra quem não é: quem quer susto a cada cena (é mais melancólica que assustadora). ⚠️ O revisor confirma.
  3. ***A Queda da Casa de Usher*** · Netflix · minissérie de 8 episódios (2023), inspirada em Edgar Allan Poe ([Olhar Digital](https://olhardigital.com.br/2023/10/21/cinema-e-streaming/gostou-de-a-queda-da-casa-de-usher-veja-estes-5-filmes-e-series-do-diretor-mike-flanagan/)). Por que combina: uma família rica pagando o preço das escolhas. Pra quem não é: quem não aguenta sangue. ⚠️ O revisor confirma.
  2. ***Missa da Meia-Noite*** · Netflix · minissérie de 7 episódios (2021) ([AdoroCinema](https://www.adorocinema.com/series/serie-25310/); [AdoroCinema, notícia](https://www.adorocinema.com/noticias/series/noticia-1000067179/)). Por que combina: uma ilhazinha, um padre novo e milagres que ninguém explica. Pra quem não é: quem quer ritmo rápido (é um terror falado, de monólogos). ⚠️ **O revisor de 15/10 não confirmou o catálogo de 2026.** Se não confirmar hoje, sai, a nº 3 sobe e a Lista fica com 4 (o título passa a "4 séries").
  1. ***A Maldição da Residência Hill*** · Netflix · 1 temporada de 10 episódios (2018) ([AdoroCinema](https://www.adorocinema.com/series/serie-21978/); confirmada na Netflix BR pelo revisor em 16/10, no blog de *Profundezas*). Por que combina: é a obra que define o Flanagan, terror e luto de família no mesmo episódio. Pra quem não é: quem quer susto sem drama.
  - **Reserva:** nenhuma série do Flanagan fora da Netflix e do Prime. Se faltarem duas, a Lista sai com 3 (é o mínimo).
- **Pôsteres:** `python scripts/posters.py <pasta> "Carrie (2026)" "The Midnight Club" "The Haunting of Bly Manor" "The Fall of the House of Usher" "Midnight Mass" "The Haunting of Hill House"`. *Carrie* = TVmaze #45562 (a série de 2026, não o filme). Corte os logos de streaming.
- **Demo do app:** não entra (`assets/demo/` vazio).
- **Fim e CTA único:** "**Salva pra hoje à noite**" (Consideração) + link fixado. Sem pergunta para os comentários (mesmo padrão de 14 a 16/10). O comentário fixado lista onde assistir cada série.
- **Descrição:** capítulos (00:00 abertura e um por série, calculados pelo `narracao.json` + 0,30 s), onde assistir cada uma e a UTM `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-17-lista-da-mia-mike-flanagan`.
- **Tags:** mike flanagan, carrie, carrie a estranha, residência hill, mansão bly, missa da meia-noite, casa de usher, clube da meia-noite, séries de terror, halloween.
- **`"series"`:** ["Carrie, a Estranha", "O Clube da Meia-Noite", "A Maldição da Mansão Bly", "A Queda da Casa de Usher", "Missa da Meia-Noite", "A Maldição da Residência Hill"] (*Carrie* entra porque o pôster aparece na abertura).
- **Horário:** YouTube `2026-10-17T12:00:00-03:00` (3º na fila de narração).

## 04-short-reels-selvagens-ep03-sabado (YouTube Short + Instagram Reels · 13h30 · **o mesmo vídeo**)
- **Decisão:** um arquivo 9:16, publicado duas vezes no `publicar.json` (`YOUTUBE_SHORT` + `REELS`), ambas em `2026-10-17T13:30:00-03:00`. TikTok: o mesmo arquivo.
- **Reaproveitamento:** use o roteiro de `saida/2026-10-15/05-reels-selvagens-do-sofa-ep03-quinta-de-estreia/roteiro.md`, com o pôster TVmaze #90007 já baixado. **Trocas obrigatórias:** "quinta" vira "sábado" na fala do gancho ("Pro amigo que abre três estreias no sábado... e assiste zero."), no registro de campo ("SÁBADO, 21H") e na legenda. O resto da piada é genérico e fica igual. Não nomeie as "3 estreias".
- **Formato:** Selvagens do Sofá, Ep. 03 (`09`). Base: `referencias/quadros/selvagens-do-sofa-ep01-final.jpg`.
- **Pilar:** 1. Série pro seu humor · **Job:** principal · **Humor:** romântico/leve (`--romantico`).
- **Série:** ***Um Choque de Amor*** · Netflix · dorama de comédia romântica, **10 episódios, desde 09/10** (fonte do dia da estreia: [Rolling Stone Brasil](https://rollingstone.com.br/entretenimento/um-choque-de-amor-nova-comedia-romantica-coreana-ganha-trailer/); [BNews](https://www.bnewssaopaulo.com.br/noticias/entretenimento/um-choque-de-amor-conheca-a-historia-do-novo-dorama-da-netflix.html); [Omelete](https://www.omelete.com.br/korea/um-choque-de-amor-dorama-netflix-trailer)). Uma nota antiga falava em 12 episódios. O número 10 vem da matéria do dia da estreia e da fonte coreana de 15/10. ⚠️ O revisor confirma no app; se não confirmar, **tire o "10 episódios"** da fala e da tela (a piada não depende dele). Pra quem não é: quem quer algo tenso hoje.
- **CTA:** "Manda pra quem precisa" (Descoberta), falado e no botão. Um só.
- **Legenda IG:** "Pro amigo que abre três estreias no sábado e assiste zero 🔭" + linha da série + "Manda pra quem precisa." + #selvagensdosofa #seriecerta #dorama #oqueassistir. **Título YT:** "Selvagens do Sofá, Ep. 03: o sábado das 3 estreias".
- **UTM (descrição YT):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-17-short-selvagens-ep03`.
- **`"series"`:** ["Um Choque de Amor"].
- **Horário:** 2º na fila de narração.

## 05-reels-short-casal-sabado-escolhe-voce (Instagram Reels 18h30 + YouTube Short 19h00 · **o mesmo vídeo**)
- **Decisão:** um arquivo 9:16, publicado duas vezes: `REELS` em `2026-10-17T18:30:00-03:00` e `YOUTUBE_SHORT` em `2026-10-17T19:00:00-03:00`. TikTok: o mesmo arquivo.
- **Reaproveitamento:** roteiro, 9 falas e pôster de `saida/2026-10-16/05-reels-short-casal-sexta-escolhe-voce/`. **Trocas obrigatórias:** fala 01 (Ela) "Pro casal que passa **o sábado** inteiro no 'escolhe você'."; texto de tela igual; relógio "SÁB · 21:00"; legenda com #sabadou no lugar de #sextou; título YT "Sábado à noite: quem escolhe a série?". As outras 8 falas não mudam.
- **Vozes:** Ela (`1AxHVMpXJZxq6ECdF4Kn`) e Ele (`oeBFFQkxcUHweNreD1nw`), um arquivo `narracao-NN-ela/ele.txt` por fala. A MIA aparece só como texto no celular.
- **Pilar:** 3. Dilema do casal · **Job:** social 1 · **Humor:** romântico + adrenalina (`--romantico`).
- **Série:** ***Sr. e Sra. Smith*** · Prime Video · 1ª temporada de 8 episódios, lançados de uma vez em 02/02/2024, com Donald Glover e Maya Erskine ([About Amazon](https://aboutamazon.com/news/entertainment/mr-and-mrs-smith-prime-video); [Canaltech](https://canaltech.com.br/series/sr-e-sra-smith-o-que-esperar-do-reboot-do-prime-video-277705)). É original Amazon. ⚠️ Não há fonte de 2026 para o catálogo do Prime BR: o revisor confirma no app. **Não citar a 2ª temporada** (renovada, sem data, com elenco novo).
  - **Reserva** (se não confirmar): nenhuma pronta. A peça cai e vai para o `99-revisao.md`; não monte outra série às pressas.
- **CTA:** botão brasa "**MANDA PRA QUEM PRECISA**" + @seriecerta (Descoberta). Um só.
- **UTM (descrição YT):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-17-short-casal-sabado-escolhe-voce`.
- **`"series"`:** ["Sr. e Sra. Smith"].
- **Horário:** 1º na fila de narração.

**Pilares de hoje:** 2 (carrossel e Stories), 1 (Lista e 13h30) e 3 (18h30/19h). Reels: 1 × 3 ✓. Shorts: 1 × 3 ✓.
**Semana até aqui (14 a 16/10, só o que foi publicado no feed e em vídeo):** pilar 1 em 4 peças, pilar 2 em 2, pilares 3, 4 e 5 em zero. Hoje entram 2 e 3. Domingo entra o 5 (Tradutor). O pilar 4 (prova) segue travado sem demo em `assets/demo/`.

---

# RASCUNHO DE AMANHÃ: domingo, 2026-10-18
> A rotina de amanhã refaz a pesquisa de tendência e **revalida todos os fatos**. Pasta: `saida/2026-10-18/`.

## 01-carrossel + 02-stories (10h00)
- **Pilar 2 ou 1**, conforme a tendência. Proposta: "*Ninguém Quer* volta quinta (22/10): 4 comédias românticas pra esperar". A data da T3 está confirmada ([Omelete](https://www.omelete.com.br/series-tv/ninguem-quer-3a-temporada-data-estreia-netflix); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/netflix-divulga-data-de-estreia-e-primeiras-imagens-da-3a-temporada-de-ninguem-quer/)); o nº de episódios **não** está. Fica de fora *Sr. e Sra. Smith* (casal de sábado).
- Stories: o carrossel em 9:16 + CTA de Conversão.

## 03-lista-da-mia (12h00)
- **Eixo diferente de criador e de gênero:** humor ("ansiedade de domingo à noite") ou plataforma ("o melhor que chegou no HBO Max em outubro": *The Paper* T2, *Largados e Pelados Brasil* T4 em 18/10, *Lanternas*). O nº 1 não pode ser *Residência Hill* nem *Olhos que Condenam*.

## 04-short-reels-tradutor-o-que-a-mia-entende (13h30, YouTube + Instagram, mesmo vídeo)
- **Reaproveitar** `saida/2026-10-15/06-short-tradutor-o-que-a-mia-entende/` (pilar 5, sem séries, ~470 caracteres, `"series": []`). O texto não cita dia da semana; só confira as UTMs (data 18/10).

## 05-reels-short-domingo-a-noite (Reels 18h30 + Short 19h00, mesmo vídeo)
- **Regra de domingo:** o Reels das 18h30 fala de "domingo à noite". **Pilar 1** (o pilar 4 depende de demo). Formato Relógio ("Domingo, 21h"), gancho de envio ("pra amiga que fica ansiosa domingo à noite"), 1 série leve e curta, com fatos checados no dia. Cerca de 75 palavras (~450 caracteres).
- **Prioridade de crédito de domingo:** 05 (domingo à noite, 2 slots) → 04 Tradutor (2 slots) → Lista. Total aproximado: ~450 + ~470 + ~1.450.

## Blog de domingo (rascunho)
- 09h **ansioso** ("séries para ansiedade de domingo à noite"; o humor não se repete em 7 dias: 14/10 sono, 16/10 estressado, 17/10 triste) · 11h "Halloween nos streamings: séries de terror que chegaram em outubro" ou "o que sai do catálogo no fim de outubro" (só com fonte do dia) · 14h "Acabou *Crystal Lake*?" (8 episódios em 16/10, Universal+) · 17h guia "*Ninguém Quer* 3ª temporada: quando estreia e como rever as 2 primeiras" · 20h a Lista de domingo em texto.

---

## Ideias guardadas (revalidar antes de usar)
- *Slow Horses* T6 termina na quarta (21/10): pilar 2 "acabou Slow Horses?" na quinta (22/10).
- *A Lista Terminal* T2 (Prime Video, 21/10, 8 episódios de uma vez) ([Omelete](https://www.omelete.com.br/series-tv/a-lista-terminal-chris-pratt-2-temporada-trailer-data)).
- *Lupin* parte 4 (Netflix, 23/10).
- *Dom de Iludir* (Netflix, 28/10, ainda sem confirmação da data).
- Lista "terror de cidade pequena" (`saida/2026-10-15/03-...`, não narrada): fica para o Halloween (sábado, 31/10). Não repete séries do Flanagan; *Carrie* aparece lá como nº 3, então nesse dia ela não é gancho de outra peça.

## Pendências para o Bruno
1. **Créditos da ElevenLabs:** quarto dia sem recarga. O dia pede ~2.440 caracteres. Sem crédito, saem só o carrossel, os Stories e o blog, e 5 slots de vídeo ficam vazios em pleno período de base (isso distorce a referência da revisão de 21/10).
2. **Bio do Instagram:** trocar para a UTM do Stories de hoje antes das 10h00 (troca manual).
3. **Domínios** (`nuvem/dominios-permitidos.txt`): JustWatch, Netflix, FlixPatrol e What's on Netflix seguem bloqueados. Vale bater o olho no app em *Succession* (HBO Max), *Sr. e Sra. Smith* (Prime Video) e *Missa da Meia-Noite* (Netflix).
4. **Slug `humor=<humor>`** e link do modo casal no app: ainda sem confirmação, então os links vão sem humor.
5. **Demo do app** em `assets/demo/`: sem ela, o pilar 4 (15%) não sai.

---

## Blog
> Grade e padrão: `estrategia/11-blog.md` · pacote e publicação: `blog/README.md`. Pastas: `saida/2026-10-17/blog/<nn>-<slug>/`. Horários da grade normal: 09h, 11h, 14h, 17h e 20h.
> **No ar (60 dias, `--listar` colado no pedido):** `series-parecidas-com-a-diplomata` (16/10 às 21h; aparece como 17/10 por causa do UTC), `lupin-parte-4-guia`, `series-parecidas-com-profundezas`, `estreias-streaming-semana-12-a-18-outubro-2026`, `series-leves-para-relaxar`, `series-para-assistir-com-sono`, `como-escolher-serie-pelo-humor`, `como-calcular-tempo-de-maratona`, `minisseries-e-series-curtas` e `como-organizar-assinaturas-de-streaming`. Nenhuma palavra-chave nem lista de séries de hoje repete essas matérias.
> **Destaque único no dia:** nenhuma série é destaque em duas matérias. A das 20h repete a Lista, como manda a regra. As séries das redes de hoje (*Um Choque de Amor*, *Sr. e Sra. Smith*) ficam fora do blog. As do carrossel 01 são a base da matéria das 14h: é o mesmo tema em outro canal, e dentro do blog não há repetição.
> **Verificação:** tudo foi conferido por WebSearch em 17/10. Onde há ⚠️, o revisor confirma no app ou no JustWatch BR; sem confirmação, a série sai. Toda matéria com disponibilidade leva `:::info Conferido em 17/10/2026`.

### 01 · 09h00 · Pelo humor
- **Título provisório:** 6 séries para quando você está triste (e quer companhia, não mais tristeza)
- **Palavra-chave principal:** séries para quando você está triste
- **Slug:** `series-para-quando-voce-esta-triste` · **Categoria:** `o-que-assistir` · **Humor:** `triste` (CTA `[[app: triste]]`). O humor não se repete no slot em 7 dias (14/10 sono, 16/10 estressado).
- **Job:** emocional 1 (quando estou mal, quero uma série que acolha sem piorar).
- **Séries:**
  1. ***After Life*** · Netflix · 3 temporadas de 6 episódios, encerrada em 2022, de e com Ricky Gervais ([Folha Vitória](https://www.folhavitoria.com.br/cultura/after-life-traz-ricky-gervais-como-viuvo-que-nao-supera-a-morte-de-sua-mulher/); [Variety](https://variety.com/2020/tv/news/after-life-renewed-for-season-3-ricky-gervais-netflix-overall-deal-1234599578)). Luto com humor. Pra quem não é: quem está num luto muito recente (o tema é direto). ⚠️ O revisor confirma a Netflix BR (original da Netflix, risco baixo).
  2. ***Disque Amiga para Matar*** · Netflix · 3 temporadas, encerrada ([Netflix BR](https://www.netflix.com/br/title/80219707); [Canaltech](https://canaltech.com.br/series/critica-disque-amiga-para-matar-temporada-3-230551/)). Amizade que nasce num grupo de luto, com comédia. Pra quem não é: quem quer evitar o tema doença (a reta final passa por ele; dizer só isso, sem detalhe).
  3. ***Fleabag*** · Prime Video · 2 temporadas, encerrada. ⚠️ Sem fonte de 2026 nesta pauta: o redator busca e o revisor confirma (é original Amazon, risco baixo). Pra quem não é: quem não curte quebra da quarta parede.
  4. ***Eu Nunca...*** · Netflix · 4 temporadas, encerrada. ⚠️ O redator busca a fonte. Luto adolescente com comédia leve. Pra quem não é: quem não tem paciência com drama de escola.
  5. ***Atypical*** · Netflix · 4 temporadas, encerrada. ⚠️ O redator busca a fonte. Família acolhedora, humor gentil. Pra quem não é: quem quer história com tensão.
  6. ***Pousando no Amor*** · Netflix · dorama de 16 episódios. ⚠️ O redator busca a fonte. Romance que abraça. Pra quem não é: quem não tem tempo para episódio longo.
  - **Reserva:** *Uma Advogada Extraordinária* foi usada na Lista de 14/10, então não entra. Se faltar série, a matéria fica com 5.
- **Linkar:** `[[leia: como-escolher-serie-pelo-humor]]`, `[[leia: series-leves-para-relaxar]]`.
- **Link do app:** `https://seriecerta.online/descobrir?humor=triste&utm_source=blog&utm_medium=organico&utm_campaign=2026-10-17-series-para-quando-voce-esta-triste`.
- **Cuidado de tom:** acolher sem diagnosticar. Nada de "cura" nem de conselho de saúde.

### 02 · 11h00 · Streaming da semana
- **Título provisório:** Estreias da próxima semana nos streamings: Ninguém Quer, Lupin, A Lista Terminal e mais (19 a 25/10)
- **Palavra-chave principal:** estreias da próxima semana streaming
- **Slug:** `estreias-streaming-semana-19-a-25-outubro-2026` (com data, porque o tema é datado) · **Categoria:** `streaming` · **Humor:** `animado` (CTA `[[app: animado]]`).
- **Job:** principal (já saber, no fim de semana, o que vem e onde).
- **Por que é tendência:** 3 séries grandes em 3 dias, cada uma num serviço diferente, sendo duas aguardadas há anos (Lupin, 3 anos; Lista Terminal, 4 anos). As fontes estão em cada item. Também trazem a data: [Showmetech, Netflix outubro](https://www.showmetech.com.br/lancamentos-da-netflix-em-outubro-de-2026/), [Oficina da Net, Prime Video outubro](https://www.oficinadanet.com.br/amazon-prime-video/73210-lancamentos-prime-video-outubro-2026), [Oficina da Net, HBO Max outubro](https://www.oficinadanet.com.br/hbo-max/73209-hbo-max-lancamentos-outubro-2026) e [Oficina da Net, Disney+ outubro](https://www.oficinadanet.com.br/disney-plus/73211-lancamentos-disney-plus-outubro-2026).
- **Séries (em ordem de data):**
  1. ***A Lista Terminal*** T2 · Prime Video · **21/10, 8 episódios de uma vez**, com Chris Pratt ([Omelete](https://www.omelete.com.br/series-tv/a-lista-terminal-chris-pratt-2-temporada-trailer-data); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/2a-temporada-de-a-lista-terminal-ganha-data-de-estreia-com-chris-pratt-em-thriller-de-espionagem/)). Não confundir com o derivado *Dark Wolf*. Pra quem não é: quem não curte violência e ação militar.
  2. ***Ninguém Quer*** T3 · Netflix · **22/10** ([Omelete](https://www.omelete.com.br/series-tv/ninguem-quer-3a-temporada-data-estreia-netflix); [Einerd, trailer](https://www.einerd.com/ninguem-quer-3a-temporada-ganha-trailer-com-joanne-e-noah-morando-juntos/)). **Não citar o nº de episódios** (nenhuma fonte traz). Spoiler zero sobre as temporadas 1 e 2: só "o casal volta".
  3. ***Lupin*** parte 4 · Netflix · **23/10, 8 episódios de uma vez** (já conferido em 16/10; reconfirme). Aqui entra só um parágrafo com `[[leia: lupin-parte-4-guia]]`: o destaque completo já está no guia.
  4. ***Georgie & Mandy: Seu Primeiro Casamento*** (nova temporada) · HBO Max · 22/10 ([Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/); [Oficina da Net](https://www.oficinadanet.com.br/hbo-max/73209-hbo-max-lancamentos-outubro-2026)). ⚠️ O revisor confirma o nº da temporada.
  5. ***Cyberpunk: Mercenários*** T2 · Netflix · 20/10, segundo a [Oficina da Net](https://www.oficinadanet.com.br/netflix/72900-lancamentos-netflix-outubro-2026). ⚠️ Fonte única: o redator confirma em uma segunda fonte, ou o item sai.
  6. ***American Horror Story*** 13 · Disney+ · episódio semanal em 22/10 ([Canaltech](https://canaltech.com.br/entretenimento/lancamentos-do-disney-em-outubro-mes-tem-serie-do-visao-e-terror-para-o-halloween/)). **Não citar a data do final** (as fontes divergem: 29 × 30/10).
  - **Fora:** *Slow Horses* (é o guia das 17h). *Fingida* (Disney+, 20/10) e *O Colombiano de Keko* (HBO Max, 22/10) não têm sinopse confiável. *Largados e Pelados Brasil* já saiu na matéria de 12 a 18/10.
- **Linkar:** `[[leia: lupin-parte-4-guia]]`, `[[leia: estreias-streaming-semana-12-a-18-outubro-2026]]`, `[[leia: como-organizar-assinaturas-de-streaming]]`.

### 03 · 14h00 · Acabou X?
- **Título provisório:** Acabou A Leste do Éden? 5 séries parecidas para não ficar órfã
- **Palavra-chave principal:** séries parecidas com A Leste do Éden
- **Slug:** `series-parecidas-com-a-leste-do-eden` · **Categoria:** `series` · **Humor:** `curioso` (CTA `[[app: curioso]]`) · `destaque: true` (é a série mais forte da semana nos rankings).
- **Job:** emocional 3.
- ***A Leste do Éden*** (gancho, com pôster no topo e no `"series"`): Netflix, minissérie de 7 episódios, todos desde 01/10, com Florence Pugh, criação de Zoe Kazan e base no romance de John Steinbeck ([Canaltech](https://canaltech.com.br/entretenimento/a-leste-do-eden-nova-serie-com-florence-pugh-e-grande-aposta-da-netflix-conheca/); [Omelete](https://www.omelete.com.br/series-tv/a-leste-do-eden-serie-da-netflix-com-florence-pugh-ganha-novo-trailer-e-data)). Sem 2ª temporada confirmada ([BNews](https://www.bnewssaopaulo.com.br/noticias/entretenimento/a-leste-do-eden-vai-ter-2-temporada-na-netflix-entenda-o-futuro-da-serie.html)). Spoiler zero.
- **Por que é tendência:** nº 1 global da Netflix entre as séries em inglês na estreia (6,5 mi) e 12,6 mi de visualizações na semana de 5 a 11/10, em nº 1 em 25 países ([Mac Observer](https://www.macobserver.com/entertainment/east-of-eden-is-netflixs-no-1-show-how-florence-pughs-cathy-ames-drama-reached-6-5-million-views/); [Selectra](https://selectra.co.uk/tv-broadband/news/netflix-uk-top-10-week-below-east-of-eden-animals-ice-age)). Não há posição no Brasil, então escreva "entre as mais vistas da Netflix no mundo".
- **Séries:** as do carrossel 01 (fontes acima), mais *Objetos Cortantes*:
  1. ***Ripley*** · Netflix · minissérie de 8 episódios, sem T2.
  2. ***Pachinko*** · Apple TV. ⚠️ Nº de temporadas só com confirmação.
  3. ***Peaky Blinders*** · Netflix · 6 temporadas + o filme *O Homem Imortal* (20/03/2026). ⚠️
  4. ***Objetos Cortantes*** · HBO Max · minissérie de 8 episódios (2018), com Amy Adams, baseada no livro de Gillian Flynn. Uma matéria de set/2026 a lista na HBO Max ([AdoroCinema](https://www.adorocinema.com/series/serie-20322/); [Observatório do Cinema](https://observatoriodocinema.com.br/indicacoes/mais-pesada-que-euphoria-drama-psicologico-da-hbo-max-explora-relacoes-toxicas-e-segredos-perturbadores/amp/)). Mãe difícil e cidade natal que sufoca. **Pra quem não é:** quem quer evitar temas de autolesão e abuso. Escreva isso com clareza, sem detalhe.
  5. ***Succession*** · HBO Max · 4 temporadas. ⚠️ Sem fonte de 2026: sai se o revisor não confirmar.
  - **Reserva:** *Mare of Easttown* não entra (foi destaque no carrossel de 16/10). Se faltarem duas, a matéria fica com as 4 confirmadas + um `##` "Se quiser o livro", sem indicar série.
- **Linkar:** `[[leia: minisseries-e-series-curtas]]`, `[[leia: series-parecidas-com-profundezas]]`.

### 04 · 17h00 · Guia
- **Título provisório:** Slow Horses: quantas temporadas, ordem e onde assistir antes do final da 6ª (21/10)
- **Palavra-chave principal:** Slow Horses temporadas
- **Slug:** `slow-horses-temporadas-guia` · **Categoria:** `guias` · **Humor:** `estressado` (CTA `[[app: estressado]]`).
- **Job:** principal (como começar, em que ordem e quanto tempo leva). Secundário: emocional 3, para quem vai terminar na quarta.
- **Série (1):** ***Slow Horses*** · Apple TV · 6 temporadas. A 6ª tem 6 episódios semanais, de 16/09 a **21/10**, e adapta *Joe Country* e *Slough House*, de Mick Herron ([GameOverDrive](https://gameoverdrive.com.br/slow-horses-6-temporada-data-episodios-elenco-livros/); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/slow-horses-ganha-data-de-estreia-para-a-6a-temporada-e-apresenta-novo-ator-do-elenco/); [Diário do Nordeste](https://diariodonordeste.verdesmares.com.br/verso/slow-horses-lanca-primeiro-episodio-da-6-temporada-veja-livros-que-inspiraram-serie-1.3792012)). Renovada para a 7ª temporada ([Omelete](https://www.omelete.com.br/apple-tv/slow-horses-renovada-apple-tv-7a-temporada)). A notícia de renovação até a 8ª tem uma fonte só: **não citar**.
  - O guia traz: ordem (T1 → T6), quantos episódios por temporada (⚠️ o redator confirma que todas têm 6 antes de somar), quanto tempo para ver tudo (a conta vai como **estimativa**, pelo método de `como-calcular-tempo-de-maratona`, sem afirmar duração que o revisor não confirmar), quem é Gary Oldman e qual é a premissa da T1 (sem spoiler), qual livro cada temporada adapta (só se houver fonte) e pra quem não é.
  - **Spoiler zero:** nada do que acontece da T2 à T6. Nenhuma morte de personagem.
- **Linkar:** `[[leia: como-calcular-tempo-de-maratona]]`, `[[leia: series-parecidas-com-a-diplomata]]` (onde *Slow Horses* já aparece).

### 05 · 20h00 · Lista da MIA em texto
- **Título provisório:** Séries de Mike Flanagan: as 5 para ver depois de Carrie (e antes do Halloween)
- **Palavra-chave principal:** séries de Mike Flanagan
- **Slug:** `series-de-mike-flanagan` · **Categoria:** `o-que-assistir` · **Humor:** `curioso` (CTA `[[app: curioso]]`). O `--mood` do vídeo é `estressado`, mas a 04 já usa `estressado` no blog. A regra é uma `[[app]]` por matéria, e a repetição de humor entre matérias é permitida (a 03 também é `curioso`).
- **Job:** principal (secundário: emocional 3, para quem terminou *Carrie*).
- **Base:** a Lista do dia (`03-lista-da-mia-mike-flanagan/roteiro.md`), com as mesmas fontes e a mesma ordem (5 → 1). **Se o vídeo sair**, entram `video_da_peca` e `[[video]]`. **Se a Lista for bloqueada** (sem crédito), a matéria sai sem vídeo e sem dizer "vídeo do dia" (correção do revisor de 16/10).
- ***Carrie*** entra como seção de abertura ("a mais nova do Flanagan"): Prime Video, 8 episódios, todos em 07/10, nº 1 do Prime Video no mundo na semana de estreia (fontes da Lista). Spoiler zero, nem a cena do baile. Somada às 5 da contagem, a matéria fica com 6 séries.
- **Se *Missa da Meia-Noite* cair na revisão,** a matéria fica com 5 (*Carrie* + 4) e o título passa a "as 4".
- **Linkar:** `[[leia: series-parecidas-com-profundezas]]`, `[[leia: minisseries-e-series-curtas]]`.

**Checagem do dia (blog):** palavras-chave novas nos 60 dias ✓. Nenhuma série é destaque em duas matérias: *Lupin* aparece na 02 só como parágrafo com link para o guia de 16/10, e *Slow Horses* fica fora da 02. Humores: triste (09h), animado (11h), curioso (14h), estressado (17h) e curioso (20h), com uma `[[app]]` por matéria. `destaque: true` só na 03.
