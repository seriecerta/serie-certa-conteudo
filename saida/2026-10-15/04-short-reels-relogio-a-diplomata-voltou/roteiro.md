# Roteiro: 04-short-reels-relogio-a-diplomata-voltou

- **Formato:** 9:16 (1080×1920), um arquivo só para YouTube Short + Instagram Reels às 13h30 (e TikTok). Narração MIA (eleven_v3). **Formato recorrente: Relógio / ritual.** Base: `motor/exemplos/relogio-catalogo.html` + folha `referencias/quadros/quarta-21h-reels.jpg` (rótulo do dia + relógio grande no topo, uma ideia por tela, carimbo brasa na virada). Fecho **sem recibo** (o recibo foi o fecho de 14/10): o fecho é o contador "8" + botão.
- **Pilar:** 2. Órfã de série (a série que ela esperava voltou) · **Job:** emocional 3 · **Humor:** adrenalina (`--mood: var(--estressado)`).
- **CTA único (Descoberta):** "Manda pra quem precisa", falado e no botão brasa. Sem "comenta", sem "segue", sem "parte 2".
- **Tamanho:** 57 palavras, 328 caracteres, cerca de 22–25 s de fala (≈ 26 s de vídeo com entrada aos 0,30 s e respiro final).
- **Pôster:** `imagens/the-diplomat.jpg` (TVmaze #60213, "The Diplomat", estreia 2023-04-20). Conferido visualmente: é o pôster da T4 (Keri Russell, Rufus Sewell, Allison Janney, Bradley Whitford). **Atenção fase 2:** o rodapé traz "ONLY ON NETFLIX | OCTOBER 15" — enquadre a `.capa` cortando o rodapé (`object-fit: cover; object-position: top`, altura menor) para não mostrar logo de streaming.

## Cenas

| ~Tempo | Fala da MIA | Texto na tela | Visual / efeito |
|---|---|---|---|
| 0,3–3 s | Pra amiga que tá contando os dias pra A Diplomata voltar. | **PRA AMIGA QUE TÁ CONTANDO OS DIAS** pra **A DIPLOMATA** (brasa) voltar | Texto já no 1º quadro. Relógio no topo: rótulo "QUINTA-FEIRA" + **13:30**. Emoji 🗓️ com `pulsa`; chip "dias contados: ✓✓✓✓" riscando. Som `whoosh`. |
| 3–7 s | Quinta, hora do almoço... e eu já sei o que vou ver hoje à noite. | "eu, na hora do almoço:" → "eu **JÁ SEI** o que vou ver hoje à noite." | Relógio 13:30 com ponto piscando. Carimbo brasa "JÁ SEI" + som `carimbo`. Emoji 😎 (eco do "RAPIDINHO"). |
| 7–9,5 s | A Diplomata voltou. Na Netflix. | **A DIPLOMATA** + carimbo "VOLTOU." + selo "onde assistir: Netflix" (texto, sem logo) | Pôster oficial entra com `esquerda` + som `virada`. `.capa > img` com rodapé cortado. |
| 9,5–13 s | Quarta temporada. Oito episódios. De uma vez. | chip "4ª temporada" → contador grande **episódios: 0 → 8** → "**DE UMA VEZ.**" | `data-conta` 0→8 sincronizado com "Oito"; `pop` + som no "De uma vez". **Quadro da capa.** |
| 13–15 s | [rindo baixinho] Adeus, sono. | "adeus, **SONO.**" | Relógio do topo dispara 13:30 → 03:00 (piada visual: a madrugada que vem). Emoji 😴 → 🫣 com `treme`. |
| 15–19 s | Pra quem não é? Quem nunca viu as outras. Começa pela primeira. | Chip escuro "PRA QUEM NÃO É:" + "quem nunca viu as outras" → "começa pela **1ª**" | Emoji 🤚. Três tracinhos "T1 · T2 · T3" acendendo, seta para T1. |
| 19–22 s | Manda pra quem precisa. | 🫂 + "manda pra ela" / botão brasa **MANDA PRA QUEM PRECISA** + @seriecerta | `ding` no botão. 1,5 s parado no fim. |

- **Relógio:** começa em 13:30 e só "dispara" para 03:00 no "adeus, sono" (é piada de maratona, não horário de estreia). Não mostrar nenhuma hora de lançamento.
- **Capa sugerida (`data-capa`):** o quadro do contador **"8"** com "DE UMA VEZ." e o pôster ao lado.
- Nenhuma imagem ou texto sobre a trama: nem da T3, nem da T4.

## Legenda (Instagram / TikTok)
Pra amiga que tá contando os dias pra A Diplomata voltar 🗓️
A Diplomata T4, Netflix, 8 episódios de uma vez. Se você nunca viu as outras, começa pela primeira.
Manda pra quem precisa.
#adiplomata #seriecerta #oqueassistir #netflix

- **Título YT Short:** "A Diplomata voltou: 8 episódios de uma vez"
- **Descrição YT:** legenda acima + `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-15-short-relogio-a-diplomata-voltou`
- **`"series"`:** ["A Diplomata"]

## Verificação de fatos (WebSearch, 2026-10-15)
WebFetch segue bloqueado; checagem por resultado de busca. TVmaze respondeu via `scripts/posters.py`.
- **Onde assistir / data / episódios:** Netflix, 4ª temporada em 15/10/2026, 8 episódios de uma vez. Fontes: [Omelete, trailer e data](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data), [GameOverDrive, 8 episódios](https://gameoverdrive.com.br/a-diplomata-4-temporada-quantos-episodios/), [GameOverDrive, estreia nesta quinta](https://gameoverdrive.com.br/a-diplomata-4-temporada-horario-estreia-netflix/), [GameOverDrive, Netflix 12–18/10](https://gameoverdrive.com.br/netflix-lancamentos-semana-12-18-outubro-2026/). O próprio pôster oficial traz "October 15". Nenhuma fonte de adiamento.
- **Não citados:** horário de estreia (o "4h" é previsão de site), duração de episódio, data da T3, total de episódios da série.
- **Spoiler:** zero. A fala não diz nada da trama; "pra quem não é" só pede para começar pela T1.
- **Para o revisor:** conferir no app da Netflix que a T4 está no ar antes das 13h30.

## Checagem de regras
- Um CTA só. Pra quem não é dito. Sem spoiler, sem diálogo, sem logo na arte (rodapé do pôster cortado).
