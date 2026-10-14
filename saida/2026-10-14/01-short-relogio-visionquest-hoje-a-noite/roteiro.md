# Roteiro: 01-short-relogio-visionquest-hoje-a-noite

- **Formato:** YouTube Short 9:16 (1080×1920), narração MIA (eleven_v3). **Formato recorrente: Relógio / ritual**, com fecho em **Recibo/placar**. Base: `motor/exemplos/relogio-catalogo.html` + folha `referencias/quadros/quarta-21h-reels.jpg`. É o espelho do "Quarta, 21h" (07/10): lá ela não escolhia nada; aqui, ao meio-dia, ela já escolheu. O mesmo arquivo vai para o TikTok.
- **Pilar:** 1. Série pro seu humor
- **Job:** Principal (indicação certeira, com onde assistir, sem rolar catálogo)
- **Humor:** animado (`--mood: var(--animado)`)
- **CTA único (Descoberta):** "Manda pra quem precisa", falado e no botão brasa. Sem "comenta", sem "segue", sem "parte 2".
- **Tamanho:** 77 palavras, cerca de 29 a 31 s de fala (31 a 33 s de vídeo com entrada aos 0,30 s e respiro final).
- **Pôster:** `imagens/visionquest.jpg` (TVmaze #64950, "VisionQuest", estreia 2026-10-13 no registro do TVmaze, canal Disney+). Conferido visualmente: é o pôster da série (Visão no trono). **Atenção fase 2:** o pôster oficial traz no rodapé "October 14" e o logo do Disney+. Enquadre a `.capa` cortando o rodapé (ex.: `object-fit: cover; object-position: top` com altura menor) para não mostrar logo de streaming nem data de estreia na arte.

## Cenas

| ~Tempo | Fala da MIA | Texto na tela | Visual / efeito |
|---|---|---|---|
| 0,3–2,5 s | Pra amiga que até hoje fala de WandaVision. | **PRA AMIGA QUE ATÉ HOJE FALA DE** **WANDAVISION** (brasa) | Texto já no quadro 1. Emoji 📺 grande com `pulsa`. Som `whoosh`. Relógio no topo já visível: rótulo "QUARTA-FEIRA" + **12:00**. |
| 2,5–4,5 s | Quarta-feira, meio-dia. | "eu, ao meio-dia:" (igual ao "eu, às 21h:" da referência) | Relógio 12:00 com o ponto piscando. Emoji 🍽️ pequeno. |
| 4,5–7 s | E eu já sei o que vou ver hoje à noite. | "eu **JÁ SEI** o que vou ver hoje à noite." (JÁ SEI em brasa, carimbo) | `carimbo` + som `carimbo` no "já sei". Emoji 😎 (eco do "RAPIDINHO" de 07/10). |
| 7–9 s | [rindo baixinho] Pela primeira vez na vida. | "pela primeira vez na vida." + rodapé pequeno "— eu, chocada" | Emoji 🤯 com `treme`. Relógio avança 12:00 → 12:01. |
| 9–12 s | VisionQuest. No Disney Plus. | Nome **VISIONQUEST** + selo "onde assistir: Disney+" (texto, sem logo) | Pôster oficial entra com `esquerda` + som `virada`. `.capa > img` cortada (sem rodapé do pôster). |
| 12–15 s | A série nova do Visão, que vem de WandaVision. | chip "spin-off de WandaVision" | Pôster segue em cena, leve zoom. |
| 15–19 s | Os dois primeiros episódios saem juntos... e hoje à noite já dá pra ver. | "**2 episódios** de uma vez" → "hoje à noite **JÁ DÁ PRA VER**" | Contador "episódios: 0 → 2" (`data-conta`). `pop` no "já dá pra ver". Emoji 🍿. |
| 19–22 s | Pra quem não é? Quem nunca viu nada da Marvel. | Chip escuro "PRA QUEM NÃO É:" + "quem nunca viu nada da Marvel" | Emoji 🤷 com `treme`. |
| 22–27 s | Séries escolhidas antes das nove da noite: uma. Recorde pessoal. | **Recibo/cupom** "RESUMO DA QUARTA": séries escolhidas antes das 21h **1** · catálogo rolado **0 min** · trailers vistos **0** · **RECORDE PESSOAL** (carimbo brasa) | Cupom desce (`sobe`), linhas entram uma a uma. Carimbo "RECORDE PESSOAL" com som `carimbo`. Confete leve. Emoji 🏆. |
| 27–30,5 s | Manda pra quem precisa. | 🫂 + **manda pra ela** / botão brasa **MANDA PRA QUEM PRECISA** + @seriecerta | `ding` no botão. 1,5 s parado no fim. |

- **Relógio:** fica fixo em 12:00/12:01 o vídeo inteiro (a piada é que ela não precisou de horas). Não mostrar 22:00 nem nenhum horário de estreia.
- **Capa sugerida (`data-capa`):** o quadro "eu **JÁ SEI** o que vou ver hoje à noite." com o 😎 e o relógio 12:00. Alternativa: o recibo com "RECORDE PESSOAL".
- **Recibo:** "catálogo rolado 0 min" e "trailers vistos 0" são piada de comportamento, não dado.

## Legenda (YouTube / TikTok)
Pra amiga que até hoje fala de WandaVision 📺
VisionQuest está no Disney+: os dois primeiros episódios saem juntos e hoje à noite já dá pra ver. Se você nunca viu nada da Marvel, não é essa.
Manda pra quem precisa.
#seriecerta #visionquest #wandavision #marvel #oqueassistir

- **Comentário fixado:** "VisionQuest está no Disney+. Os dois primeiros episódios saem juntos."
- **UTM da descrição:** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-14-short-relogio-visionquest-hoje-a-noite`

## Verificação de fatos (WebSearch, 2026-10-14)
WebFetch segue bloqueado; checagem por resultado de busca. TVmaze respondeu via `scripts/posters.py`.
- **Onde assistir:** Disney+ Brasil. Fontes: [GameOverDrive, horário e episódios](https://gameoverdrive.com.br/visionquest-horario-episodios-o-que-assistir-antes/), [GameOverDrive, estreias Disney+ 12–18/10](https://gameoverdrive.com.br/disney-plus-lancamentos-semana-12-18-outubro-2026/), [Showmetech, Disney+ outubro 2026](https://www.showmetech.com.br/lancamentos-do-disney-plus-em-outubro-de-2026/), [Omelete, estreia adiantada](https://www.omelete.com.br/series-tv/vision-quest-wandavision-estreia-adiantada). TVmaze registra o canal Disney+.
- **Dois primeiros episódios juntos:** consenso entre as fontes acima.
- **Data/hora de estreia:** segue divergente (13/10 22h antecipada pelo Omelete × 14/10 22h no calendário do Disney+ Brasil citado pelo GameOverDrive). Por isso a fala diz só "hoje à noite já dá pra ver", que vale nos dois cenários. **Não citados:** data, hora, total de episódios, data do final (o GameOverDrive fala em 8 episódios até 11/11; não usado).
- **Spin-off de WandaVision:** consenso das matérias (o "Visão" é o protagonista). Nada do final de *WandaVision* é mencionado.
- **Para o revisor:** confirme no app do Disney+ Brasil que VisionQuest aparece no catálogo (ou com estreia marcada para hoje à noite). Se a estreia oficial for depois de hoje, troque "hoje à noite já dá pra ver" por "esta semana já dá pra ver".

## Checagem de regras
- Um CTA só. Pra quem não é dito. Sem spoiler, sem diálogo, sem logo na arte (rodapé do pôster cortado).
- Nenhuma frase diz "estreia hoje" ou "estreou ontem".
