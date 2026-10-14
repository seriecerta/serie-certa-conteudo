# Roteiro: 04-reels-qual-quarta-e-voce

> **Versão no ar: SEM NARRAÇÃO (14/10, ~12h).** Os créditos da ElevenLabs acabaram (157 de 254 caracteres), então a peça foi refeita
> para funcionar só com texto na tela + trilha "Sala Escura" + efeitos (regra "Sem crédito de voz" do `CLAUDE.md`).
> A tabela de cenas mais abaixo é a versão falada original, guardada em `fala-original-sem-uso.txt` (nome fora do padrão `narracao*.txt`
> de propósito, para o `narrar.py` não gerar áudio que não casaria com a cena).
>
> **O que mudou:** cena com tempos fixos em segundos (`data-duracao="40.6"`), sem `@palavra` e sem legenda automática.
> Cada tipo tem 7,4 s: 3 s de cabeçalho + gag visual, 4,4 s de pôster + onde assistir + chips + "pra quem não é" (tempo de leitura).
> Gancho em texto no quadro 1 ("pra amiga que é a Nº 3 toda quarta" + 4 cards). Fecho: grade 2×2 com o nº 3 destacado + botão
> "MANDA PRA QUEM PRECISA" (CTA único de Descoberta). Capa em 38,4 s (grade final com o botão, `data-capa="38.40"`).
> Pôsteres: recorte só por posição (`top` negativo dentro da `.capa`), sem filtro: *The Paper* sem o "peacock ORIGINAL" (corta ~12 px
> do topo de "th"), *Coven Academy* sem o logo "Disney" acima do título, *Habeas Corpus* e *Below* com o título inteiro.
> Arquivo: `video.mp4` 40,6 s, 1080×1920, −13,9 LUFS, com trilha. Horário: Reels 19h00 (pauta de hoje).

- **Formato:** Reels 9:16 (1080×1920), narração MIA (eleven_v3). **Formato recorrente: Qual é você?** Base: folha `referencias/quadros/qual-e-voce-4-tipos.jpg` (cabeçalho "QUAL É VOCÊ?" com 4 tracinhos que acendem na cor de cada tipo, número grande + nome do tipo + "superpoder" + emoji no canto, gag visual no meio, legenda grande sincronizada, grade final com os 4 cards). `data-legenda="auto"`. O mesmo arquivo vai para o TikTok.
- **Plano B da pauta:** `saida/2026-10-14/comentarios.md` não existia às 06h54. Se chegar até 10h, o roteiro muda para "Respondendo seu humor" (não inventar comentário).
- **Pilar:** 1. Série pro seu humor
- **Job:** Principal + social 2 (ser a amiga das indicações)
- **Humores:** 1 exausta `--sono` · 2 curiosa `--curioso` · 3 que quer medo `--estressado` · 4 animada `--animado`
- **CTA único (Descoberta):** "Manda pra quem precisa", falado e no botão brasa. Sem "comenta o número", sem "segue", sem "parte 2". O "Achou a sua?" é retórico, não pede comentário.
- **Tamanho:** 105 palavras, cerca de 38 a 40 s de fala (40 a 42 s de vídeo).

## Pôsteres (`scripts/posters.py`, TVmaze, conferidos)
| Arquivo | TVmaze | Estreia | Tipo |
|---|---|---|---|
| `imagens/the-paper.jpg` | The Paper #84611 | 2025-09-04 | 1 |
| `imagens/habeas-corpus.jpg` | Habeas Corpus #93677 | 2026-09-23 | 2 |
| `imagens/profundezas.jpg` | **Below** #93115 (Netflix) | 2026-10-08 | 3 |
| `imagens/coven-academy.jpg` | Coven Academy #83159 | 2026-10-02 | 4 |

- *Profundezas* não foi achada pelo nome em português. O título original é **Below** ([Einerd](https://www.einerd.com/profundezas-below-netflix-charlie-heaton/)); baixado com `--id 93115` (Netflix, 08/10/2026). Conferido com Read: pôster com Josh Hartnett num barco, título "BELOW". Sem troca de série.
- **Alerta para a fase 2:** o pôster de *The Paper* tem "peacock ORIGINAL" no topo e o de *Coven Academy* tem o logo "Disney" acima do título. Cortar topo/rodapé com `object-position` quando der; se não der sem perder o título, registrar no `99-revisao.md`.

## Cenas

| ~Tempo | Fala da MIA | Tela | Visual / efeito |
|---|---|---|---|
| 0,3–2,5 s | Pra amiga que é a número três toda quarta. | "PRA AMIGA QUE É A **Nº 3** TODA QUARTA" + 4 cards coloridos (😴 1 azul, 🤔 2 ciano, 😱 3 vermelho/estressado, 🤩 4 laranja/animado) já no quadro 1, o 3 destacado e tremendo | Texto já no quadro 1. `whoosh`. Cards caem como na referência. |
| 2,5–4 s | Qual quarta é você? | **QUAL QUARTA É VOCÊ?** (QUARTA em brasa) | `carimbo` + som. Cabeçalho fixo entra: "QUAL QUARTA É VOCÊ? — — — —" + @seriecerta. |
| 4–7 s | Um: a exausta. Superpoder: dormir no episódio um. | **1** grande azul + "A EXAUSTA" + "superpoder: dormir no episódio 1" + 😴 no canto | Tracinho 1 acende. Gag: barra "episódio 1" enchendo até 40% e 💤 caindo. |
| 7–11 s | The Paper, na HBO Max. A segunda temporada chega amanhã. Não é The Office igualzinho. | Pôster *The Paper* (`.capa`) + chip "HBO Max" + chip "T2 chega amanhã" + `.nao-e` "não é The Office igualzinho" | Capa entra com `esquerda` + `virada`. |
| 11–14 s | Dois: a curiosa. Superpoder: "só mais um" às duas da manhã. | **2** ciano + "A CURIOSA" + "superpoder: 'só mais um' às 2h" + 🤔 | Tracinho 2. Gag: relógio 02:00 + contador "só mais um: 1 → 4". |
| 14–17 s | Habeas Corpus, na Netflix. Drama jurídico. Leve, não é. | Pôster *Habeas Corpus* + chip "Netflix" + chip "drama jurídico" + `.nao-e` "não é leve" | `pop`. Emoji ⚖️. |
| 17–20 s | Três: a que quer medo. Superpoder: terror de luz acesa. | **3** vermelho + "A QUE QUER MEDO" + "superpoder: terror de luz acesa" + 😱 | Tracinho 3. Gag: 💡 aceso com chip "luz: LIGADA" e carimbo "TODAS". |
| 20–24 s | Profundezas, na Netflix. Uma criatura no mar. Medo de mar? Pula essa. | Pôster *Profundezas* + chip "Netflix" + chip "minissérie" + `.nao-e` "medo de mar? pula" | Capa com `treme` leve. Emoji 🌊. |
| 24–27 s | Quatro: a animada. Superpoder: começar três séries num dia só. | **4** laranja + "A ANIMADA" + "superpoder: começar 3 séries no mesmo dia" + 🤩 | Tracinho 4. Gag: contador "séries começadas hoje: 1 → 3" com 3 barras de progresso em 5%. |
| 27–31 s | Coven Academy, no Disney Plus. Bruxas adolescentes. Terror pesado? Não é aqui. | Pôster *Coven Academy* + chip "Disney+" + chip "temporada inteira" + `.nao-e` "terror pesado? não é aqui" | `pop`. Emoji 🔮. |
| 31–35 s | [rindo baixinho] Achou a sua? Manda pra quem precisa. | Grade final 2×2 com os 4 cards (número + tipo + mini pôster), o nº 3 destacado → botão brasa **MANDA PRA QUEM PRECISA** + @seriecerta | `ding` no botão. 1,5 s parado. |

- **Capa (`data-capa`):** a grade final com os 4 números coloridos e "QUAL QUARTA É VOCÊ?" no topo (como pede a pauta).
- O chip "temporada inteira" de *Coven Academy* e "minissérie" de *Profundezas* aparecem só na tela (fala enxugada para caber em 40 s). Não citar "21 episódios" nem "curtos".

## Legenda (Instagram / TikTok)
Pra amiga que é a nº 3 toda quarta 😱
1 The Paper (HBO Max) · 2 Habeas Corpus (Netflix) · 3 Profundezas (Netflix) · 4 Coven Academy (Disney+)
Manda pra quem precisa.
#seriecerta #oqueassistir #dicadeserie #quarta

## Verificação de fatos (WebSearch, 2026-10-14)
- ***The Paper*:** T1 na HBO Max; **T2 estreia na HBO Max Brasil em 15/10/2026** ([Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil); [GameOverDrive, HBO Max 12–18/10](https://gameoverdrive.com.br/hbo-max-lancamentos-semana-12-18-outubro-2026/); [GameOverDrive, T2 no Brasil](https://gameoverdrive.com.br/the-paper-2-temporada-estreia-brasil-hbo-max/); [Showmetech](https://www.showmetech.com.br/lancamentos-hbo-max-outubro-2026/)). O Reels sai em 14/10 às 19h, então "chega amanhã" vale. Formato de lançamento (semanal × inteira) diverge entre fontes: **não citado**.
- ***Habeas Corpus*:** Netflix, desde 23/09/2026, 8 episódios ([Netflix About](https://about.netflix.com/pt_br/news/marjorie-estiano-and-any-gabrielly-fight-for-justice-and-redress-habeas-corpus-netflix-brazils-first-legal-drama-premiering-september-23); [GameOverDrive](https://gameoverdrive.com.br/habeas-corpus-quantos-episodios/)). A fala só diz "drama jurídico".
- ***Profundezas* (Below):** Netflix, minissérie de 6 episódios, todos desde 08/10/2026; premissa oficial: criatura marinha aterrorizando uma cidade costeira ([GameOverDrive](https://gameoverdrive.com.br/profundezas-episodios-duracao/); [GameOverDrive, estreia e elenco](https://gameoverdrive.com.br/profundezas-netflix-quando-estreia-episodios-elenco/); [Omelete](https://www.omelete.com.br/series-tv/profundezas-netflix-josh-hartnett-serie-teaser-trailer)). A fala diz só "uma criatura no mar".
- ***Coven Academy*:** Disney+ Brasil, temporada inteira desde 02/10/2026; bruxas adolescentes num internato em Nova Orleans ([Gazeta SP](https://www.gazetasp.com.br/entretenimento/nova-serie-da-disney-acompanha-adolescentes-bruxas-em-academia-cercada-por-misterios-e-forcas-sombrias/); [Showmetech](https://www.showmetech.com.br/lancamentos-do-disney-plus-em-outubro-de-2026/); [Salada de Cinema](https://saladadecinema.com.br/coven-academy-supera-american-horror-story-no-ranking-do-disney/)). Número de episódios **não citado** (fontes falam em 21, não confirmado pelo revisor de 13/10).
- **Duração de episódio:** não citada em nenhuma.

## Checagem de regras
- Um CTA. Pra quem não é em todas as 4. Sem spoiler (só premissas), sem diálogo, sem logo de streaming na arte (nomes só em chip de texto; logos dos pôsteres cortados ou registrados).
- *The Paper* já saiu em 13/10 com outro humor e gancho; piada do documentário não reaproveitada.
