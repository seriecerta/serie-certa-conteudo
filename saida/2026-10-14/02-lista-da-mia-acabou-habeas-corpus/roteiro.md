# Roteiro: 02-lista-da-mia-acabou-habeas-corpus

- **Formato:** Lista da MIA, YouTube 16:9 (1920×1080), narração MIA (eleven_v3), um só texto. Base: `motor/exemplos/lista-da-mia-16x9.html` (`<body class="paisagem" data-legenda="auto" style="--mood:var(--curioso)">`, `.serie-card` com `.capa > img`, `.metas`, `.porque`, `.nao-e`, `.progresso` de 5; `data-legenda="off"` nas telas de série). Render com `--formato 16x9`.
- **Pilar:** 2. Órfã de série (eixo "acabou X?")
- **Job:** Emocional 3 (acabei uma série que amei e quero algo com a mesma sensação)
- **Humor / mood:** curioso (`--curioso`, #43D2E0)
- **Tamanho:** 429 palavras, cerca de 3 min a 3 min 10 s de fala.
- **CTA único (Consideração):** "Salva esse vídeo pra hoje à noite." O "onde assistir tá no comentário fixado" é informação, não pedido. **Sem pergunta pros comentários** (decisão da pauta, regra 6). Botão final: "SALVA PRA HOJE À NOITE"; linha de apoio "onde assistir: comentário fixado".
- **Título (≤ 70):** Acabou Habeas Corpus? 5 séries sobre justiça pra ver na Netflix (64 caracteres)
- **Thumb (`thumb/cena.html`, modelo `lista-da-mia-thumb.html`):** "5" gigante + "ACABOU HABEAS CORPUS?" + ⚖️. Se usar pôster, usar o de *Olhos que Condenam* (nº 1) **recortado sem o logo Netflix** (ver alerta abaixo); senão fica só o emoji.

## Fonte da tendência (da pauta, reconferida em 2026-10-14)
- *Habeas Corpus* foi nº 1 entre as séries da Netflix no Brasil na semana de 28/09 a 04/10 ([Netflix Tudum Top 10 Brasil](https://www.netflix.com/tudum/top10/brazil/tv); [Exame](https://exame.com/pop/top-10-da-netflix-serie-habeas-corpus-domina-ranking-de-mais-vistas-no-brasil/)). Primeiro drama jurídico brasileiro da Netflix, estreou em 23/09 ([Netflix About](https://about.netflix.com/pt_br/news/marjorie-estiano-and-any-gabrielly-fight-for-justice-and-redress-habeas-corpus-netflix-brazils-first-legal-drama-premiering-september-23)).
- Busca de hoje: sem anúncio de 2ª temporada até 07/10 ([GameOverDrive](https://gameoverdrive.com.br/habeas-corpus-2-temporada-netflix/)); matérias de "o que ver depois" ([Einerd](https://www.einerd.com/gostou-de-habeas-corpus-conheca-mais-7-series-e-filmes-juridicos-para-ver/)).
- A fala diz "liderou o top dez da Netflix", no passado. **Não** diz "a mais vista agora". Não fala de renovação nem do final.

## Pôsteres (`scripts/posters.py`, TVmaze, todos conferidos por título e ano)
| Arquivo | TVmaze | Estreia | Uso |
|---|---|---|---|
| `imagens/habeas-corpus.jpg` | Habeas Corpus #93677 | 2026-09-23 | abertura (série de origem) |
| `imagens/extraordinary-attorney-woo.jpg` | Extraordinary Attorney Woo #62357 | 2022-06-29 | nº 5 |
| `imagens/better-call-saul.jpg` | Better Call Saul #618 | 2015-02-08 | nº 4 |
| `imagens/the-lincoln-lawyer.jpg` | The Lincoln Lawyer #52910 | 2022-05-13 | nº 3 |
| `imagens/unbelievable.jpg` | Unbelievable #34526 | 2019-09-13 | nº 2 |
| `imagens/when-they-see-us.jpg` | When They See Us #30202 | 2019-05-31 | nº 1 |
| `imagens/anatomy-of-a-scandal.jpg` | Anatomy of a Scandal #48241 | 2022-04-15 | reserva, não usada |

- Nenhuma troca: as 5 séries da pauta têm pôster.
- **Alerta para a fase 2 e o revisor:** os pôsteres de *Unbelievable* ("SEPT 13 | NETFLIX" no rodapé) e *When They See Us* ("NETFLIX | NOW STREAMING" no meio) trazem o **logo da Netflix**. O de *Extraordinary Attorney Woo* é o pôster coreano (título em coreano, logo do canal ENA). Para *Unbelievable*, cortar o rodapé com `object-position: top`. Para *When They See Us*, o logo fica na altura do título; se o corte não esconder sem perder o título, registrar no `99-revisao.md` para o revisor decidir (pôster oficial é regra do Bruno; logo de streaming na arte é proibido).

## Cenas

| Bloco (~tempo) | Fala da MIA (resumo; texto integral em `narracao.txt`) | Tela | Efeitos |
|---|---|---|---|
| 0:00–0:15 Gancho | "Acabou Habeas Corpus... justiça ainda te deve uma resposta? Eu te entendo. A série brasileira que liderou o top dez da Netflix deixou um vazio. Então eu separei cinco séries pra você continuar. Todas na Netflix." | Pôster de *Habeas Corpus* à esquerda (`.capa`), à direita "acabou **HABEAS CORPUS**?" → "a justiça ainda te deve uma resposta" ⚖️ → número **5** com carimbo + "séries pra continuar" | `whoosh` na capa, `carimbo` no 5. Legenda auto ligada. |
| 0:15–0:22 Promessa | "Sem spoiler nenhum... Do número cinco ao número um. E a número um é a que mais se parece com ela." | Chip "🚫 spoiler: 0" + "do nº 5 ao nº 1" | `pop` no chip. |
| 0:22 nº 5 | Uma Advogada Extraordinária | `.serie-card`: capa + "nº 5 de 5" + h2 + `.metas` [Netflix · 1 temporada · 16 episódios] + `.porque` "**tribunal com coração**: um caso por episódio" + `.nao-e` "quem quer o tom pesado de Habeas Corpus" | `progresso` 1/5. `data-legenda="off"`. |
| ~0:52 nº 4 | Better Call Saul | metas [Netflix · 6 temporadas] + porque "um advogado que conhece **o sistema por dentro**" + nao-e "quem não tem paciência pra começo lento" | progresso 2/5. Emoji 😏 pequeno no "você não larga". |
| ~1:22 nº 3 | O Poder e a Lei | metas [Netflix · 4 temporadas · 5ª confirmada] + porque "**julgamento de roer as unhas**, um caso por temporada" + nao-e "quem quer realismo brasileiro" | progresso 3/5. |
| ~1:55 nº 2 | Inacreditável | metas [Netflix · minissérie · 8 episódios · fatos reais] + porque "**insistir na verdade** quando o sistema já desistiu" + nao-e "quem tá sensível a temas de violência sexual" | progresso 4/5. Tom sóbrio: sem emoji, sem som de impacto. |
| ~2:25 nº 1 | Olhos que Condenam | Pausa antes ("E o número um...") com tela escura + "nº 1" em carimbo; depois card: metas [Netflix · minissérie · 4 episódios · Ava DuVernay] + porque "**o peso de um erro judicial**" + nao-e "quem quer algo leve hoje" | `carimbo` + som `carimbo` no h2. progresso 5/5. Sem confete (tema pesado). |
| ~2:55 Fecho | "Cinco séries pra você não ficar órfã de tribunal. Da mais leve à mais pesada... Salva esse vídeo pra hoje à noite. Onde assistir cada uma tá no comentário fixado." | Grade com os 5 pôsteres pequenos em ordem (5→1, faixa "leve → pesada" embaixo) → "**salva** pra hoje à noite 🔖" + `.botao` "SALVA PRA HOJE À NOITE" + apoio "onde assistir: comentário fixado" + seriecerta.online | `ding` no botão. |

- **Demo do app:** não entra (sem gravação em `assets/demo/`).
- **Capa (`data-capa`):** o quadro do gancho com o pôster de *Habeas Corpus* e o 5 carimbado.
- **Spoiler:** zero. *Habeas Corpus* só como sensação ("a justiça te deve uma resposta"). As 5 séries só com premissa oficial. *Better Call Saul* sem citar *Breaking Bad* nem o destino de ninguém.

## Descrição (rascunho para o desdobrador)
Acabou Habeas Corpus e ficou órfã de tribunal? A MIA separou 5 séries sobre justiça, advogados e erro judicial, todas na Netflix. Sem spoiler.
00:00 Acabou Habeas Corpus?
00:22 5. Uma Advogada Extraordinária
00:52 4. Better Call Saul
01:22 3. O Poder e a Lei
01:55 2. Inacreditável
02:25 1. Olhos que Condenam
(ajustar os tempos pelo `narracao.json`)
A série certa pro seu humor: https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-14-lista-da-mia-acabou-habeas-corpus
- **Comentário fixado:** "Onde assistir: 5. Uma Advogada Extraordinária (Netflix) · 4. Better Call Saul (Netflix) · 3. O Poder e a Lei (Netflix) · 2. Inacreditável (Netflix) · 1. Olhos que Condenam (Netflix)". Sem pedido.
- **Tags:** habeas corpus, séries jurídicas, o que assistir netflix, séries de tribunal, marjorie estiano, olhos que condenam, o poder e a lei

## Verificação de fatos (WebSearch, 2026-10-14)
WebFetch bloqueado; checagem por resultado de busca. **Nenhuma fonte de 2026 confirma o catálogo atual da Netflix Brasil para os títulos antigos: o revisor confirma cada um no app/site da Netflix antes de aprovar.**
- **nº 5 Uma Advogada Extraordinária:** Netflix ([netflix.com/br/title/81518991](https://www.netflix.com/br/title/81518991); [Canaltech](https://canaltech.com.br/series/uma-advogada-extraordinaria-5-motivos-para-assistir-a-serie-da-netflix/)). 16 episódios na 1ª temporada ([AdoroCinema](https://www.adorocinema.com/series/serie-31134/)). A 2ª temporada ainda está em produção, sem data (Purepeople, 30/09/2026, via busca). Por isso "uma temporada". ⚠️ Não confundir com o remake japonês que entra na Netflix em 18/10. **Fonte fraca para 2026.**
- **nº 4 Better Call Saul:** Netflix, 6 temporadas ([JustWatch BR](https://www.justwatch.com/br/serie/better-call-saul/temporada-4); [Canaltech, T6 na Netflix](https://canaltech.com.br/entretenimento/better-call-saul-temporad-6-quando-estreia-213806/); [Space Money, 2026](https://www.spacemoney.com.br/cultura-e-entretenimento/better-call-saul-serie-citada-por-diogo-defante-apos-prisao/)). **Fonte fraca para 2026** (JustWatch sem data).
- **nº 3 O Poder e a Lei:** Netflix, 4 temporadas (T4 em 05/02/2026), 5ª confirmada e anunciada como a última, ainda sem data ([Omelete](https://www.omelete.com.br/series-tv/o-poder-e-a-lei-renovada-5a-temporada-netflix); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/netflix-confirma-que-o-poder-e-a-lei-sera-finalizada-na-5a-temporada/); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000204670/)). A fala diz só "a quinta já tá confirmada".
- **nº 2 Inacreditável:** Netflix, minissérie de 8 episódios, baseada em fatos reais ([netflix.com/br/title/80153467](https://www.netflix.com/br/title/80153467); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000077798/); [AdoroCinema, ficha](https://www.adorocinema.com/series/serie-23246/)). Os 8 episódios agora têm fonte (a pauta não tinha). Duração de episódio não citada.
- **nº 1 Olhos que Condenam:** Netflix, minissérie de 4 episódios, de Ava DuVernay ([AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000040687/); [ficha AdoroCinema](https://www.adorocinema.com/series/serie-23908/); [Correio Braziliense](https://blogs.correiobraziliense.com.br/proximocapitulo/critica-olhos-que-condenam-da-netflix/)). Divergência: o Canaltech fala em 5 episódios; a maioria e a estrutura original dão 4. Mantido "quatro". **Revisor confirma.**
- **Não citado em nenhuma:** duração de episódio, horas de maratona, notas.
- **Reserva:** *Anatomia de um Escândalo* (pôster baixado). Entra no lugar de qualquer série que o revisor não confirmar na Netflix Brasil; fala e card precisam ser reescritos (minissérie de 6 episódios, fonte só de 2022, reconfirmar).

## Checagem de regras
- Um CTA (salvar). Pra quem não é em todas as 5. Sem spoiler, sem diálogo, sem letra.
- Tema sensível (nº 2): aviso direto, sem descrever cenas.
