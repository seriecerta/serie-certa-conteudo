# Revisão de 2026-10-13

> **Revisão parcial, feita às ~11h BRT.** Cobre só as peças sem vídeo (01 e 03). As peças 02 e 04 (vídeos) ainda estão em produção e entram numa segunda rodada. Elas ainda **não** constam no `revisao.json`.

## Resultado
| Peça | Status | Horário |
|---|---|---|
| 01-carrossel-orfa-herdeiras-outubro | **aprovada** (com correções) | 13/10 13h30 |
| 03-stories-mia-acertou | **aprovada** | 13/10 19h30 |
| 02-short-tradutor-orfa-residencia-hill | pendente (em produção) | — |
| 04-reels-selvagens-ep02-orfa-the-office | pendente (em produção) | — |

## 01 — Carrossel "herdeiras de outubro"
Fatos rechecados com WebSearch em 13/10. O WebFetch segue bloqueado, então nada foi conferido direto nos apps.
- **The Paper / HBO Max, T2 em 15/10: confirmado** ([Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil), [GameOverDrive](https://gameoverdrive.com.br/the-paper-2-temporada-estreia-brasil-hbo-max/), [Einerd](https://www.einerd.com/the-paper-spin-off-de-the-office-ganha-data-de-estreia-da-2a-temporada/)). T1 com 10 episódios na HBO Max ([Rolling Stone BR](https://rollingstone.com.br/?p=260936)). A fonte é de 2025, mas a chegada da T2 na mesma plataforma sustenta a informação.
- **VisionQuest / Disney+: data NÃO fecha.** Rolling Stone BR, UpNerd e ComicBook.com dizem que a estreia foi **antecipada para hoje, 13/10, às 22h**. Variety, Omelete e a página da Marvel ainda dão 14/10. "Estreia amanhã, 14/10" pode estar errado já hoje à noite. **Corrigido:** saíram a data, a contagem de episódios e o ritmo de lançamento. Card: "o spin-off de WandaVision. Estreia esta semana." Legenda: "O spin-off estreia esta semana." A frase vale nas duas versões.
- **Carrie, a Estranha / Prime Video: confirmado.** São 8 episódios, todos em 07/10, com Mike Flanagan como showrunner ([GameOverDrive](https://gameoverdrive.com.br/carrie-serie-mike-flanagan-estreia-prime-video/), [Legião dos Heróis](https://www.legiaodosherois.com.br/2026/carrie-a-estranha-nova-adaptacao-ganha-data-de-estreia.html)). O texto dizia "mesmo criador", o que é impreciso, porque a obra é de Stephen King. **Corrigido:** card "Do Mike Flanagan", legenda "com Mike Flanagan no comando, o mesmo de Residência Hill".
- **Coven Academy / Disney+: estreia em 02/10 com a temporada inteira de uma vez confirmada. "21 episódios" NÃO confirmado.** Uma listagem (Flicks) sugere 10 episódios com entradas duplicadas. "Curtos" também não tem fonte, e a regra proíbe afirmar duração. **Corrigido:** "Temporada inteira no ar (desde 02/10)", sem contagem e sem "curtos".
- **True Blood / Prime Video, só T1 desde 05/10: confirmado** ([Fast Company Brasil](https://fastcompanybrasil.com/tech/prime-video-chega-catalogo-outubro-2026/), [Oficina da Net](https://www.oficinadanet.com.br/amazon-prime-video/73210-lancamentos-prime-video-outubro-2026)).
- As correções foram aplicadas em `cena.html`, `legenda.txt` e `publicar.json`. Os cards foram re-renderizados com `renderizar.py --imagens --formato 4x5`. Revi os 7 cards depois da renderização: nada cortado ou sobreposto, sem logo de streaming, identidade "Sala Escura" mantida, botão "salva pra hoje à noite" e @seriecerta no fim.
- **Spoiler:** nenhum, só premissa. **Voz:** ok, todo par traz "pra quem não é". **CTA:** um só, "Salva pra hoje à noite" (Consideração, carrossel). **Emojis na legenda:** 1. **Hashtags:** 4. **Legenda:** 713 caracteres. Não há link, então não há UTM a conferir.
- O `comentario-fixado.txt` só lista onde assistir, sem data ou contagem. Está ok e não é publicado pelo script.

## 03 — Stories "MIA acertou?"
- Como as peças de 09/10 não foram ao ar, a versão já é a genérica ("a última série que a MIA te indicou..."), sem citar *Hotel Assombrado*. Não há fatos a checar.
- Visual: 4 telas 1080×1920 ok. Fundo verde-noite, brasa, emoji grande, botão + @seriecerta. Nada cortado.
- **CTA:** um só, "Me conta se acertou" (Retenção), com resposta por direct. Não há link. A promessa "o que a MIA erra, ela aprende" bate com o 👍/👎 do app (`04-proposta-de-valor.md`).

## Checagens técnicas
- `publicar.json` das duas peças: JSON válido, todos os arquivos existem, `quando` em 13/10 com `-03:00`, e o `validar()` do `publicar.py` retorna OK nas duas.
- `python scripts/publicar.py --data 2026-10-13 --simular`: sem erro. O script não listou as peças porque os horários do Instagram ainda estão no futuro, então ele não as valida antes da hora. Por isso rodei o `validar()` direto.
- **Atenção:** a simulação rodou em modo nuvem e mostrou `= pacote 2026-10-13: 0 arquivos` no bucket `pacotes-redes`. A rotina horária na nuvem baixa o pacote do Supabase. **Se o pacote de hoje, com este `revisao.json` e os quadros re-renderizados, não for enviado (`python scripts/nuvem.py subir-pacote 2026-10-13`) antes das 13h30, o carrossel não sai.**

## Para a segunda rodada (02 e 04)
- O Short 02 cita Carrie: use "do Mike Flanagan", não "mesmo criador", e mantenha os 8 episódios no Prime Video.
- O Reels 04 cita The Paper com T2 na quinta, 15/10, o que está confirmado.
- O rascunho de amanhã (Short "VisionQuest estreia hoje", 14/10) pode ficar errado se a estreia de fato foi antecipada para 13/10. Reconfirme amanhã.
