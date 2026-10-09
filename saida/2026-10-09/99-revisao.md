# Revisão: 2026-10-09 (sexta), feita às ~18h30

## Resultado
| Peça | Status | Horário |
|---|---|---|
| 02-stories-dilema-casal | **aprovada** | IG Stories 19h45 |
| 01-casal-terror-ou-risada | **aprovada** | IG Reels 20h, YT Short 20h30 |

`publicar.py --data 2026-10-09 --simular`: sem erros. O Short já aparece como pronto para 20h30. Os itens do Instagram ainda não aparecem porque o horário deles não chegou. Rodei o `validar()` do script direto nos três itens e ele não apontou nenhum erro. Arquivos, `quando` com `-03:00`, legenda com 333 caracteres e capa: tudo ok.

## Fatos (refeitos por WebSearch hoje)
- **Hotel Assombrado:** original Netflix. A T2 estreou hoje, 09/10/2026, segundo o Netflix Tudum e o What's on Netflix (2026 confirmado). A T1 segue no catálogo. As peças só afirmam "na Netflix", então isso está **confirmado**.
- **Wandinha:** original Netflix. Matérias de 2026 (Omelete, fim das filmagens da T3) tratam a série como Netflix. A T3 não tem data. As peças só afirmam "na Netflix", então isso também está **confirmado**.
- Nenhuma peça cita temporada, número de episódios, duração ou estreia. Por isso não houve correção de fato.

## O que corrigi
1. **Narração `01-casal-terror-ou-risada/narracao-07-ela.txt`.** A fala "Mas a gente sabe que você não quer." virou "Hoje é terror de mão dada." O "a gente sabe" soava como a marca debochando de quem tem medo, e essa pessoa é justamente quem recebe o envio. A nova fala mantém a provocação carinhosa do casal. Atualizei também a cena 25–34 s do `roteiro.md`. O texto na tela (`telas.txt`) não muda.
   **Precisa regenerar** `narracao-07-ela.mp3` (voz Ela) e o `video.mp4`. O YouTube sobe o vídeo na primeira rodada do `publicar.py` depois da aprovação, então regenere e suba o pacote **antes** da próxima rodada. Se não der tempo, o vídeo atual com a fala antiga ainda é publicável. A troca é uma melhoria de tom, não um bloqueio.
2. **Título do Short.** "a série pros dois" virou "as séries pros dois", porque são duas séries.
3. **Story 04.** "O modo casal da MIA escolhe pelos dois. Testa grátis..." virou "A MIA tem modo casal pra escolher pelos dois. Testa a MIA grátis no link da bio." O texto antigo prometia o modo casal grátis, e não consegui confirmar em qual plano ele está. Tirei também o rodapé "link na bio", que repetia o CTA. Renderizei de novo com `scripts/renderizar_cards.py`.

## Checagens sem problema
- Spoiler, diálogo e letra de terceiros: nenhum. Pôster: nenhum (`assets/posters/` não existe). Tudo é tipografia da marca.
- CTA: o Reels, o Short e o TikTok têm só "Manda pra quem precisa" (Descoberta). Os Stories têm só "Testa grátis no link" (Conversão).
- Emojis: 1 na legenda do Reels e 1 no TikTok.
- Mídia: o `video.mp4` tem 1080×1920 e 34,2 s, com áudio. Os 7 `narracao*.txt` têm `.mp3`. A `capa.jpg` e os `stories/01-04.jpg` são JPEG 1080×1920.
- UTM do Short: `utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-09-casal-terror-ou-risada`, no padrão.

## Pendências para o Bruno
1. **Bio antes das 19h45:** `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-09-stories-casal`. Depois do dia, volte a bio ao padrão.
2. **Modo casal:** confirmar se existe deep link. Se existir, troque a bio pelo deep link com os mesmos UTM. Confirmar também em qual plano ele está, para os próximos Stories poderem dizer "grátis" (ou não).
3. **Domínios bloqueados no proxy (WebFetch, EGRESS_BLOCKED):** oficinadanet.com.br, ovicio.com.br, olhardigital.com.br, justwatch.com, netflix.com. **seriecerta.online** também está bloqueado (curl retorna 403 no CONNECT), e o revisor não conseguiu checar planos nem o modo casal no próprio site. Liberar esses domínios.
4. **Nuvem:** o `--simular` baixou 0 arquivos do Supabase para 2026-10-09. Se a rotina horária roda na nuvem, rode `python scripts/nuvem.py subir-pacote 2026-10-09` (completo, com vídeo e JPGs) depois de regenerar o áudio e o vídeo, ou nada será publicado.

## Fontes
- [Netflix Tudum: Haunted Hotel](https://www.netflix.com/tudum/articles/haunted-hotel)
- [What's on Netflix: data da T2](https://www.whats-on-netflix.com/news/haunted-hotel-season-2-netflix-release-date/)
- [Einerd: T2 ganha data](https://www.einerd.com/hotel-assombrado-segunda-temporada-ganha-data-de-estreia-e-trailer-assista/)
- [Omelete: Wandinha T3, fim das filmagens](https://www.omelete.com.br/series-tv/wandinha-netflix-3a-temporada-fim-filmagens-nova-foto-jenna-ortega)

## Publicação (rodada da tarde, 2026-10-09)
- `publicar.py --data 2026-10-09` rodou em **simulação**: `PUBLICACAO_AUTOMATICA` não está `true` no `.env`. Nada foi publicado nem agendado. Para ir ao ar, o Bruno precisa ligar a trava no `.env` do ambiente (o agente não altera essa trava).
- Pacote completo (com vídeo e áudio) subido para a nuvem: 30 arquivos.
