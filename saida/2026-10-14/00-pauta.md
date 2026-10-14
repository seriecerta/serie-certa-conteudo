# Pauta: quarta-feira, 2026-10-14 (America/Sao_Paulo)

**Pilar do dia:** 1. Série pro seu humor (`08-cronograma.md`, linha Qua). Grade: Reels 19h · Stories "Indicação + link de humor" · Short 12h · **Lista da MIA 13h30** (todos os dias).
**Meta dos 90 dias:** audiência (seguidores/alcance), orçamento zero (`05-go-to-market.md`). Reels/Shorts fecham com "Manda pra quem precisa".
**Período de base (`10-experimentos.md`):** de 14 a 20/10 a grade roda fixa e sem testes A/B. Nenhuma peça leva `experimento`.
**Capacidade:** 4 peças hoje (Short, Lista da MIA, Stories, Reels). São 3 vídeos com narração ElevenLabs, cena no motor e render, mais os Stories em imagem. A grade de quarta não tem carrossel.

## Decisões de grade
- **Lista da MIA às 13h30, não às 12h00.** O `.claude/agents/estrategista.md` e o skill `pacote-diario` falam em 12h00. O `CLAUDE.md`, o `07-pilares-e-formatos.md` e o `08-cronograma.md` dizem 13h30. Segui a estratégia (13h30). Isso também evita choque com o Short das 12h no mesmo canal do YouTube. **Pendência para o Bruno:** alinhar o agente e o skill para 13h30, ou mudar a estratégia.
- O `estrategista.md` fala em "grade igual todo dia, 7 publicações". O `08-cronograma.md` traz uma grade por dia da semana. Segui o `08`, como pedido.
- Os dois vídeos curtos do dia ficam no pilar 1 porque a grade de quarta pede esse pilar. O agente pede para não repetir pilar nos dois Reels/Shorts do dia, mas aqui a grade manda. Para variar, Short e Reels usam formatos recorrentes, humores e séries diferentes.

## Histórico (`historico/publicados.md`, últimos 30 dias)
Há registros só de 09/10 e 13/10. Nenhuma peça de hoje repete série + humor + gancho:
- *VisionQuest* apareceu em 13/10 no carrossel "órfã de série" com o gancho "Outubro trouxe a herdeira". Hoje ela volta com o humor **animado** e o gancho do Relógio. Série igual, humor e gancho diferentes: permitido.
- Não existe Lista da MIA registrada, então nada se repete em eixo + tema (14 dias) nem em série nº 1 (30 dias).
- *Habeas Corpus*, *Profundezas*, *Coven Academy* e as séries da Lista nunca saíram.
- **Nada de 09/10 e 13/10 foi ao ar**: o `publicar.py` rodou em simulação (`99-revisao.md` de 13/10). Conto as peças mesmo assim, porque estão no histórico.

## Nota de verificação (ler antes de roteirizar)
- Usei só WebSearch. **O WebFetch falha por DNS (ENOTFOUND)** em omelete.com.br, gameoverdrive.com.br e **api.tvmaze.com**. Por isso não conferi nenhum pôster. O `roteirista` roda `scripts/posters.py`. Se uma série ficar sem pôster, entra a **reserva** indicada na peça. Se o TVmaze estiver bloqueado no ambiente, registre no `99-revisao.md`: a Lista não sai sem pôster.
- **Duração de episódio: não confirmada para nenhuma série. Não afirmar.**
- O revisor reconfirma cada "onde assistir" no dia, antes de aprovar.

### VisionQuest: a data de estreia segue sem fechar (por isso o gancho mudou)
- **14/10 (hoje):** página Disney+ Brasil citada pelo [GameOverDrive](https://gameoverdrive.com.br/visionquest-horario-episodios-o-que-assistir-antes/), [TechTudo](https://www.techtudo.com.br/noticias/2026/10/quando-estreia-visionquest-veja-datas-episodios-e-entrevista-exclusiva.ghtml), [Guia Disney+ Brasil](https://disneyplusbrasil.com.br/visionquest-veja-as-datas-e-horarios-de-lancamento-de-todos-os-episodios/) (22h) e [Wikipedia](https://en.wikipedia.org/wiki/VisionQuest).
- **13/10, 22h (antecipada):** [O Tempo, 13/10](https://www.otempo.com.br/entretenimento/filmes-e-series/2026/10/13/disney-visionquest-estreia-com-dois-episodios-na-semana), [Omelete](https://www.omelete.com.br/series-tv/vision-quest-wandavision-estreia-adiantada) (cita post da Marvel Studios, "6PM PT") e [Observatório do Cinema](https://observatoriodocinema.com.br/series/visionquest-que-horas-estreia-a-serie-do-visao-no-disney/).
- **Consenso:** Disney+. Os 2 primeiros episódios saem juntos. As fontes divergem sobre o calendário completo (o [Einerd](https://www.einerd.com/visionquest-veja-o-cronograma-de-estreia-de-todos-os-episodios-no-disney/) dá outro final), então não citar o total de episódios nem a data do final.
- **Decisão:** sai o gancho "VisionQuest estreia hoje". Entra **"hoje à noite já dá pra ver"**, que vale nos dois cenários: se estreou ontem às 22h, já está no ar; se estreia hoje às 22h, estará à noite. **Proibido** dizer "estreia hoje", "estreou ontem", a hora exata, o número total de episódios ou a data do final.

---

# HOJE: 2026-10-14

## 01-short-relogio-visionquest-hoje-a-noite (YouTube Short)
- **Formato:** Short 9:16, 25–30 s, narração MIA (eleven_v3). **Formato recorrente: Relógio / ritual**, com fecho em **Recibo/placar** (`09`). Base: `motor/exemplos/relogio-catalogo.html` + folha de quadros do "Quarta, 21h" em `referencias/`.
- **Pilar:** 1. Série pro seu humor
- **Job:** Principal (indicação certeira, com onde assistir, sem rolar catálogo)
- **Humor:** animado (`--animado`)
- **Gancho (0–2 s, fala + tela):** "Pra amiga que até hoje fala de WandaVision." O relógio abre em **12:00**: "quarta, meio-dia… e eu JÁ SEI o que vou ver hoje à noite." Virada: "pela primeira vez na vida." Faz eco do "Quarta, 21h" (07/10), só que agora ela acerta.
- **Série:** **VisionQuest**, no **Disney+**. Spin-off de *WandaVision*. "Hoje à noite já dá pra ver." Dá para citar "os dois primeiros episódios saem juntos". Pra quem não é: quem nunca viu nada da Marvel. Pôster: TVmaze #64950, já baixado em 13/10 (`saida/2026-10-13/01-carrossel-orfa-herdeiras-outubro/imagens/`). Rodar `posters.py` de novo na pasta.
- **Recibo final:** "séries escolhidas antes das 21h: 1 · recorde pessoal".
- **Fecho / CTA:** botão brasa "MANDA PRA QUEM PRECISA" + @seriecerta. Funil: Descoberta. Um CTA só.
- **Spoiler:** zero. Só premissa e ligação com *WandaVision*, nada do final de *WandaVision*.
- **Fatos para o revisor verificar:** Disney+ Brasil e "hoje à noite" (ver nota acima). Se uma fonte oficial do Disney+ Brasil der estreia **depois** de hoje, troque "hoje à noite" por "esta semana".
- **UTM da descrição:** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-14-short-relogio-visionquest-hoje-a-noite`
- **Horário:** YouTube short `2026-10-14T12:00:00-03:00` · TikTok: mesmo arquivo + `tiktok.txt`

## 02-lista-da-mia-acabou-habeas-corpus (YouTube, Lista da MIA 16:9)
- **Formato:** Lista da MIA, 1920×1080, 3–5 min, contagem regressiva de 5 séries (nº 1 por último). Motor em paisagem (`motor/exemplos/lista-da-mia-16x9.html`), `<body class="paisagem" style="--mood:var(--curioso)">`. Thumb: `motor/exemplos/lista-da-mia-thumb.html` com **"5"** gigante + "ACABOU HABEAS CORPUS?" + ⚖️.
- **Pilar:** 2. Órfã de série (o eixo "acabou X?")
- **Job:** Emocional 3 (acabei uma série que amei e quero algo com a mesma sensação)
- **Humor / `--mood`:** curioso (`--curioso`, #43D2E0). É a vontade de entender o caso e torcer pela virada.
- **Eixo:** "acabou X?". **Tema:** depois de *Habeas Corpus* (Netflix), 5 séries sobre justiça, advogado e erro judicial.
- **Por que é tendência (3 sinais):**
  1. **Top 10:** *Habeas Corpus* foi a **nº 1 entre as séries da Netflix no Brasil** na semana de 28/09 a 04/10 ([Netflix Tudum, Top 10 Brasil](https://www.netflix.com/tudum/top10/brazil/tv); [Exame](https://exame.com/pop/top-10-da-netflix-serie-habeas-corpus-domina-ranking-de-mais-vistas-no-brasil/); [Trecobox](https://trecobox.com.br/habeas-corpus-top-1-netflix-conheca-serie/)). É o primeiro drama jurídico brasileiro da Netflix: estreou em 23/09, tem 8 episódios e é inspirado no Innocence Project Brasil ([Netflix About](https://about.netflix.com/pt_br/news/marjorie-estiano-and-any-gabrielly-fight-for-justice-and-redress-habeas-corpus-netflix-brazils-first-legal-drama-premiering-september-23)).
  2. **Público que terminou e procura a próxima:** há matérias "terá 2ª temporada? o que sabemos após o final" ([GameOverDrive](https://gameoverdrive.com.br/habeas-corpus-2-temporada-netflix/), que registra que até 07/10 não houve renovação) e "Gostou de Habeas Corpus? 7 séries e filmes jurídicos" ([Einerd](https://www.einerd.com/gostou-de-habeas-corpus-conheca-mais-7-series-e-filmes-juridicos-para-ver/)). Também há cobertura do elenco em 09/10 ([O Liberal](https://www.oliberal.com/cultura/any-gabrielly-e-marjorie-estiano-protagonizam-s%C3%A9rie-jur%C3%ADdica-da-netflix-1.1174849)).
  3. **Repercussão fora do Brasil:** [Screen Rant](https://screenrant.com/habeas-corpus-netflix-new-legal-drama/) e [What's on Netflix](https://www.whats-on-netflix.com/what-to-watch/habeas-corpus-netflix-review-brazilian-legal-drama/). A série entrou no Top 10 de 7 países.
  - **Lacuna:** não confirmei sinal direto de redes (Google Trends, X, TikTok). A busca não trouxe nada e o WebFetch está bloqueado. O tema se sustenta pelo Top 10 e pela demanda editorial.
  - **Ressalva:** não achei o Top 10 da semana de 05 a 11/10. Na pauta, o "nº 1" vale para a semana de 28/09 a 04/10. **Na peça, não dizer "a mais vista agora".** Dizer "a série brasileira que liderou a Netflix".
- **Título (≤ 70):** **"Acabou Habeas Corpus? 5 séries sobre justiça pra ver na Netflix"** (64 caracteres)
- **Gancho (0–15 s):** "Acabou *Habeas Corpus* e ficou com aquela sensação de que a justiça te deve uma resposta? Eu separei cinco séries pra você continuar." Sem nada do final de *Habeas Corpus*.
- **Séries (todas na Netflix. Esse foco é coerente com o eixo, já que quem viu *Habeas Corpus* tem Netflix):**
  5. **Uma Advogada Extraordinária**: Netflix, 1 temporada, 16 episódios ([netflix.com/br/title/81518991](https://www.netflix.com/br/title/81518991)). Por que combina: tribunal com coração, um caso por episódio. Pra quem não é: quem quer o tom pesado de *Habeas Corpus*, porque essa é leve. ⚠️ A fonte de 2026 é fraca (só a página da Netflix indexada). **O revisor confirma.**
  4. **Better Call Saul**: Netflix, 6 temporadas ([Space Money, 2026](https://www.spacemoney.com.br/cultura-e-entretenimento/better-call-saul-serie-citada-por-diogo-defante-apos-prisao/); [JustWatch BR](https://www.justwatch.com/br/serie/better-call-saul/temporada-4)). Por que combina: um advogado que conhece o sistema por dentro. Pra quem não é: quem não tem paciência pra começo lento. **Não citar** o caso Diogo Defante, que não está confirmado.
  3. **O Poder e a Lei**: Netflix, 4 temporadas. A T4 saiu em 05/02/2026, com 10 episódios, e a série foi renovada para a T5 ([Olhar Digital, fev/2026](https://olhardigital.com.br/2026/02/02/cinema-e-streaming/netflix-lancamentos-da-semana-2-a-8-de-fevereiro/); [Omelete](https://www.omelete.com.br/series-tv/o-poder-e-a-lei-renovada-5a-temporada-netflix); [netflix.com/br/title/81303831](https://www.netflix.com/br/title/81303831)). Por que combina: defesa criminal e julgamento, temporada a temporada. Pra quem não é: quem quer realismo brasileiro, porque é procedural americano.
  2. **Inacreditável**: Netflix, minissérie ([Einerd, lista pós-Habeas Corpus](https://www.einerd.com/gostou-de-habeas-corpus-conheca-mais-7-series-e-filmes-juridicos-para-ver/)). Por que combina: a vítima em quem ninguém acreditou e duas investigadoras que não desistem. Pra quem não é: quem está sensível a temas de violência sexual. Dizer só isso, sem descrever cenas. Não citar número de episódios, que não foi confirmado.
  1. **Olhos que Condenam**: Netflix, minissérie de 4 episódios, de Ava DuVernay ([Einerd](https://www.einerd.com/gostou-de-habeas-corpus-conheca-mais-7-series-e-filmes-juridicos-para-ver/); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000040687/)). Por que combina: é a mais próxima do tema, sobre jovens condenados por engano e o peso de um erro judicial. Pra quem não é: quem quer algo leve hoje.
  - **Reservas (se faltar pôster ou o revisor não confirmar):** *Anatomia de um Escândalo* (Netflix, minissérie de 6 episódios, fonte só de 2022, [AdoroCinema](https://www.adorocinema.com/series/serie-26636/)). *Acima de Qualquer Suspeita* fica fora: é Apple TV, a T2 não tem data e não confirmei a T1 no catálogo em 2026.
  - **Pôster:** `python scripts/posters.py <pasta> "Uma Advogada Extraordinária" "Better Call Saul" "The Lincoln Lawyer" "Unbelievable" "When They See Us"`. Use os nomes originais no TVmaze e confira o ano. *Habeas Corpus* aparece só como série de origem. Se tiver pôster no TVmaze, pode entrar na abertura. Se não tiver, a abertura fica só no texto, sem capa gerada.
- **Demo do app:** opcional. Só entra se houver gravação em `assets/demo/`.
- **Fim e CTA único:** "Salva pra hoje à noite" (Consideração, vídeo longo YouTube, conforme o `05`) + link fixado. O `07` prevê "pergunta pros comentários" no fim da Lista, mas isso seria um segundo CTA (regra 6). **Decisão:** sem pergunta. O comentário fixado só lista onde assistir cada série, sem pedido. Se o Bruno preferir a pergunta, ela substitui o "salva" e não se soma a ele.
- **Spoiler:** zero, em *Habeas Corpus* e nas 5 séries. Só premissa.
- **Descrição:** capítulos (00:00 abertura, depois um capítulo por série), onde assistir de cada série e a UTM `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-14-lista-da-mia-acabou-habeas-corpus`.
- **Tags:** habeas corpus, séries jurídicas, o que assistir netflix, séries de tribunal, marjorie estiano, olhos que condenam, o poder e a lei
- **Horário:** YouTube `2026-10-14T13:30:00-03:00`

## 03-stories-animada-visionquest (Stories)
- **Formato:** Stories, 4 telas 1080×1920, em imagem (`--imagens`). Como a API não publica stickers, a resposta é pedida por direct e o link vai na bio, tudo escrito na arte.
- **Pilar:** 1. Série pro seu humor
- **Job:** Principal
- **Humor:** animado (`--animado`)
- **Telas:**
  1. "Como você tá hoje? Responde no direct numa palavra."
  2. "Animada e sem paciência pra escolher?"
  3. Indicação com pôster: *VisionQuest*, Disney+. "Hoje à noite já dá pra ver." Pra quem não é: quem nunca viu Marvel. **Não dizer "estreou hoje".**
  4. "A MIA acha a sua pelo seu humor. Testa grátis no link da bio."
- **CTA / funil:** "Testa grátis no link" (Conversão), a tela diária de conversão da grade. Um CTA só.
- **Link da bio:** `https://seriecerta.online/descobrir?humor=animado&utm_source=instagram&utm_medium=stories`. ⚠️ **O slug `animado` não está confirmado.** O único slug já usado foi `medo` (09/10), e ele nem é uma das 8 cores. Se o Bruno não confirmar, use `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-14-stories-animada-visionquest`.
- **Horário:** Instagram STORIES `2026-10-14T18:30:00-03:00` (meia hora antes do Reels)

## 04-reels-qual-quarta-e-voce (Reels)
- **Situação:** o rascunho de ontem previa "Respondendo seu humor (parte 2)" com comentários reais em `saida/2026-10-14/comentarios.md` até 10h. **A pasta estava vazia quando escrevi a pauta.** Por isso vale o **plano B**. Se o arquivo aparecer até 10h, o roteirista troca para o formato Respondendo seu humor e mantém as mesmas séries quando o humor bater. **Não inventar comentário.**
- **Formato:** Reels 9:16, 35–40 s, narração MIA. **Formato recorrente: Qual é você?** (`09`): 4 tipos numerados, cada um com uma cor de humor, um "superpoder" e uma série. A tela final mostra os 4 cards e "manda pra amiga que é a nº __".
- **Pilar:** 1. Série pro seu humor
- **Job:** Principal + social 2 (ser a amiga das indicações)
- **Humor:** "qual quarta é você" (4 humores)
- **Gancho (0–2 s):** "Pra amiga que é a número 3 toda quarta." Na tela: "QUAL QUARTA É VOCÊ?"
- **Tipos (todos com pôster):**
  1. **A exausta** (`--sono`): "superpoder: dormir no episódio 1". Série: **The Paper**, HBO Max. A T1 está no catálogo e "a segunda temporada chega amanhã" (15/10) ([Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil); [GameOverDrive, semana 12–18/10](https://gameoverdrive.com.br/hbo-max-lancamentos-semana-12-18-outubro-2026/); [O Tempo, 13/10](https://www.otempo.com.br/entretenimento/filmes-e-series/2026/10/13/netflix-hbo-max-disney-e-prime-video-recebem-novos-filmes-e-series-nesta-semana)). Pra quem não é: quem quer *The Office* igualzinho. Não dizer se a T2 sai inteira ou semanal, porque isso não foi confirmado. A série já saiu no Reels de 13/10, mas com outro humor e outro gancho, então é permitido. O roteirista não reaproveita a piada do documentário.
  2. **A curiosa** (`--curioso`): "superpoder: 'só mais um episódio' às 2h". Série: **Habeas Corpus**, Netflix, 8 episódios, desde 23/09 ([Netflix About](https://about.netflix.com/pt_br/news/marjorie-estiano-and-any-gabrielly-fight-for-justice-and-redress-habeas-corpus-netflix-brazils-first-legal-drama-premiering-september-23); [Canaltech](https://canaltech.com.br/entretenimento/habeas-corpus-quem-e-quem-na-nova-serie-juridica-brasileira-da-netflix/)). Pra quem não é: quem quer série leve. Conversa com a Lista das 13h30: aqui é para quem ainda não viu.
  3. **A que quer medo** (`--estressado`): "superpoder: ver terror com a luz acesa". Série: **Profundezas**, Netflix, minissérie de 6 episódios, todos lançados em 08/10/2026 ([GameOverDrive](https://gameoverdrive.com.br/profundezas-episodios-duracao/); [Canaltech](https://canaltech.com.br/entretenimento/nova-serie-de-terror-da-netflix-tem-astro-de-stranger-things-e-monstro-marinho/)). Pra quem não é: quem tem medo de mar. Dizer só isso, sem descrever o monstro além da premissa oficial.
  4. **A animada** (`--animado`): "superpoder: começar 3 séries no mesmo dia". Série: **Coven Academy**, Disney+, temporada inteira desde 02/10 ([Gazeta SP](https://www.gazetasp.com.br/entretenimento/nova-serie-da-disney-acompanha-adolescentes-bruxas-em-academia-cercada-por-misterios-e-forcas-sombrias/); [ARY News](https://arynews.tv/disney-unveils-first-trailer-for-coven-academy-a-new-supernatural-teen-series)). Pra quem não é: quem quer terror pesado, porque é teen. **Não citar** "21 episódios" nem "curtos": o revisor de 13/10 não confirmou.
- **Fecho / CTA:** botão brasa "MANDA PRA QUEM PRECISA" + @seriecerta (Descoberta). Sem "comenta o número" e sem "segue pra parte 2", para manter um CTA só, conforme a decisão registrada em 13/10.
- **Legenda:** gancho + "1 The Paper (HBO Max) · 2 Habeas Corpus (Netflix) · 3 Profundezas (Netflix) · 4 Coven Academy (Disney+)" + "Manda pra quem precisa." No máximo 2 emojis. Hashtags: #seriecerta #oqueassistir #dicadeserie #quarta
- **Capa:** os 4 números coloridos com "QUAL QUARTA É VOCÊ?".
- **Pôsteres:** `python scripts/posters.py <pasta> "The Paper (2025)" "Habeas Corpus" "Profundezas" "Coven Academy"`. Para *Profundezas*, buscar também pelo título original em inglês e conferir o ano (2026) e o elenco (Josh Hartnett). **Reserva**, se faltar algum pôster: *VisionQuest* para a animada (pôster já baixado), avisando que repete a série do Short.
- **Horário:** Instagram REELS `2026-10-14T19:00:00-03:00` · TikTok: mesmo arquivo + `tiktok.txt`

---

# RASCUNHO DE AMANHÃ: quinta-feira, 2026-10-15
> Pilar: 5. Bastidor / vídeo longo. Grade: Carrossel 12h + Reels 20h · Stories Bastidor · **Vídeo longo 19h** + Short 12h · **Lista da MIA 13h30**. Pasta: `saida/2026-10-15/`. A rotina de amanhã **revalida cada fato na web** antes de produzir.
> **Capacidade:** amanhã a grade tem 6 peças, incluindo 2 vídeos longos 16:9 (Lista + vídeo longo semanal). Proposta realista: produzir Short, Lista, carrossel (imagem), Stories e Reels. O **vídeo longo das 19h fica condicionado**: só sai se o pacote da manhã fechar as outras peças até 14h. Se não sair, o caso entra como "slot não cumprido" no período de base (`10-experimentos.md`). Quem decide se pula o slot ou adia para sábado é o Bruno, porque remover ou criar slot só o Bruno decide.

## 01-short-relogio-a-diplomata-voltou (YouTube Short, 12h)
- Formato Relógio. Pilar 2. Órfã (resgatada). Job emocional 3. Humor: estressado (`--estressado`).
- Série: **A Diplomata T4**, Netflix, 15/10 ([Omelete](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data); [Tecmundo](https://www.tecmundo.com.br/minha-serie/602304-a-diplomata-vai-ter-4-temporada-confira-o-que-diz-a-netflix.htm)). O número de episódios não foi confirmado. **Zero spoiler da T3**: não citar o gancho final (a arma, Hal, Grace Penn).
- Gancho: "Pra amiga que tá esperando a Kate Wyler desde o ano passado." CTA: Manda pra quem precisa.

## 02-lista-da-mia-<tema> (YouTube 13h30)
- **Eixo diferente de hoje** (hoje foi "acabou X?"). Proposta: **gênero, com "terror de outubro"**: o terror novo do mês nos streamings. Candidatas: *Carrie, a Estranha* (Prime Video, 8 episódios, 07/10), *Profundezas* (Netflix, 08/10), *Coven Academy* (Disney+, 02/10, teen), *True Blood* T1 (Prime Video desde 05/10), *VisionQuest* não (não é terror). `--mood`: estressado. A nº 1 não pode ser a mesma de outra Lista em 30 dias. Não há conflito.
- Alternativa, se amanhã aparecer sinal mais forte: atriz/ator em evidência na semana (ex.: Keri Russell com *A Diplomata*), desde que todas as séries tenham onde assistir confirmado no Brasil.
- A rotina de amanhã refaz a pesquisa de tendência (3 sinais) antes de fechar o tema.

## 03-carrossel-lancamentos-da-semana-por-humor (Carrossel 12h)
- 7 cards: capa "Os lançamentos da semana, pelo seu humor" → *The Paper* T2 (HBO Max, 15/10; exausta) → *A Diplomata* T4 (Netflix, 15/10; estressada) → *VisionQuest* (Disney+; animada) → *Marília Mendonça: Sentimento Louco* (Prime Video, **16/10**, 4 episódios de uma vez; triste/saudade; [GameOverDrive](https://gameoverdrive.com.br/marilia-mendonca-sentimento-louco-episodios/); [Omelete](https://www.omelete.com.br/series-tv/marilia-mendonca-sentimento-louco-documentario-critica)) → *Profundezas* (Netflix; medo) → CTA "Salva pra hoje à noite".
- Pilar 1. Job principal. Consideração. O doc da Marília pede tom respeitoso: sem piada, sem falar da morte, só "a trajetória contada com arquivo pessoal".

## 04-stories-bastidor (Stories)
- "Como a MIA decide a série pelo seu humor": 4 telas de bastidor. Pilar 5, força Atração. CTA: "Testa grátis no link". Só com tela real do app se houver gravação em `assets/demo/`. Sem isso, as telas ficam só em texto, sem prometer o que o app não faz.

## 05-reels-<bastidor> (Reels 20h)
- Pilar 5. Proposta: **Selvagens do Sofá · Ep. 03**, com o "brasileiro adulto na quinta de lançamento" (3 estreias no mesmo dia, nenhuma escolhida). A virada indica 1 série. CTA: Manda pra quem precisa. Revalidar a numeração do episódio com o `publicados.md`.

## 06-video-longo-<humor> (YouTube 19h): condicional
- Proposta: "7 séries pra quando você tá ansiosa" (`--ansioso`), estrutura fixa do `07`. Não pode repetir séries da Lista de amanhã. Só produzir se a capacidade permitir (ver acima).

---

## Ideias guardadas
- *Ninguém Quer* T3 (Netflix, 22/10, revalidar): Órfã da terça 20/10.
- *Lupin* parte 4 (Netflix, 23/10, revalidar).
- *Marília Mendonça: Sentimento Louco* (Prime Video, 16/10): Lista da MIA de sexta ou sábado, com eixo "música brasileira em série". Tom respeitoso.
- *Casamento às Cegas Brasil*: a 6ª temporada só vem em 2027 ([DOL](https://dol.com.br/entretenimento/963667/nova-temporada-de-casamento-as-cegas-brasil-estreia-em-2027)). A "nova temporada" listada nesta semana é a de outro país. Não pautar como brasileira.

## Pendências para o Bruno
1. **Horário da Lista da MIA:** a estratégia diz 13h30, o agente e o skill dizem 12h00. Usei 13h30. Alinhar os arquivos.
2. **`comentarios.md`** do "Quarta, 21h": não chegou. Hoje sai o plano B ("Qual quarta é você?"). A parte 2 prometida continua em aberto.
3. **Slug `humor=animado`** no app: confirmar. Se não confirmar, o link vai sem humor.
4. **Domínios bloqueados (DNS):** omelete.com.br, gameoverdrive.com.br e **api.tvmaze.com**, este último crítico para os pôsteres. Se `posters.py` falhar, a Lista não sai.
5. `PUBLICACAO_AUTOMATICA` segue desligada? Nada de 09 e 13/10 foi ao ar.
6. Vídeo longo de quinta: aceita condicionar ou pular o slot nesta semana de base?
7. `historico/metricas.md` segue sem números, então horários e pilares continuam como hipótese.
