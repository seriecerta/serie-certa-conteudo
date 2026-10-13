# Revisão de 2026-10-13

> 1ª rodada (~11h BRT): peças 01 e 03. 2ª rodada (~11h20 BRT): vídeos 02 e 04. As quatro estão aprovadas no `revisao.json` **local**.

## Resultado
| Peça | Status | Horário |
|---|---|---|
| 01-carrossel-orfa-herdeiras-outubro | **aprovada** (com correções) | 13/10 13h30 |
| 03-stories-mia-acertou | **aprovada** | 13/10 19h30 |
| 02-short-tradutor-orfa-residencia-hill | **aprovada** (UTM ajustada) | 13/10 18h (YouTube) |
| 04-reels-selvagens-ep02-orfa-the-office | **aprovada** (cena corrigida e re-renderizada) | 13/10 20h (Instagram) |

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

---

# 2ª rodada: vídeos 02 e 04

## Fatos (WebSearch refeito em 13/10; WebFetch segue bloqueado)
- **Carrie, a Estranha:** está no Prime Video desde 07/10, com os 8 episódios lançados de uma vez. Mike Flanagan é showrunner, roteirista, produtor executivo e diretor de 4 episódios. Confirmado em [Tecmundo](https://www.tecmundo.com.br/minha-serie/604301-carrie-nova-adaptacao-do-prime-video-ganha-trailer-e-data-de-estreia.htm), [Gazeta SP](https://www.gazetasp.com.br/entretenimento/carrie-a-estranha-ganha-nova-serie-de-terror-no-prime-video-veja-quando-estreia/) e [Omelete](https://www.omelete.com.br/series-tv/carrie-a-estranha-prime-video-mike-flanagan-data-lancamento-outubro). As peças usam "do Mike Flanagan", não "mesmo criador".
- **The Paper:** a T1 está na HBO Max e a T2 chega em 15/10 (quinta), segundo [Omelete, 17/09/2026, citando o site da HBO Max](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil), [Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/), [Showmetech](https://www.showmetech.com.br/lancamentos-hbo-max-outubro-2026/) e [GameOverDrive](https://gameoverdrive.com.br/the-paper-2-temporada-estreia-brasil-hbo-max/). As matérias de "adiamento" e "sem data no Brasil" falam da T1, em 2025. Não houve adiamento da T2. O formato de lançamento (semanal ou tudo de uma vez) segue sem confirmação, e a peça não fala disso.
- *Residência Hill* e *The Office* aparecem só como referência. Nenhuma das peças diz onde assistir a elas.

## 02: Short "Tradutor da órfã de terror" (aprovado)
- **Mídia:** 1080×1920, 30 fps, 36,2 s, com áudio. `narracao.txt` tem `.mp3` (34,1 s). Fala, tela e roteiro batem.
- **Visual:** revi os quadros a cada 2 s e os pontos de virada. Está na identidade (verde-noite, Inter Black, cards brasa, emoji grande), e o final tem botão "MANDA PRA QUEM PRECISA" + @seriecerta. Nada cortado, nada sobreposto, nenhum logo. "Prime Video" não aparece na arte. Há meio segundo de tela só com o cabeçalho, em 6,5 s, enquanto entra o card 1/4. É transição, não tela vazia.
- **Spoiler/diálogo:** nenhum. As frases entre aspas são da fã, inventadas. *Carrie* aparece só com nome, número de episódios e Flanagan.
- **Voz e CTA:** a peça tem "pra quem não é" (quem quer susto de pular do sofá) e um único CTA, "Manda pra quem precisa", de Descoberta.
- **Corrigido:** a UTM de `publicar.json` (`utm_campaign=2026-10-13-short-tradutor-orfa`) estava diferente da do roteiro. Agora as duas usam `2026-10-13-short-tradutor-orfa-residencia-hill`, no padrão `<AAAA-MM-DD>-<peça>`.
- `validar()` dá OK. O título tem menos de 100 caracteres, a descrição não tem `<` nem `>` e traz 5 hashtags. O `tiktok.txt` tem 1 emoji.

## 04: Reels "Selvagens do Sofá · Ep. 02" (aprovado)
- **Mídia:** 1080×1920, 30 fps, 40,0 s (39,98 s), −14,2 LUFS. `narracao.txt` tem `.mp3` (37,9 s).
- **Duração:** 40,0 s fica dentro do limite de 20–40 s do 07, no teto. Aceito.
- **Numeração Ep. 02:** `referencias/README.md` registra só o Ep. 01 no ar, e não existe outro Selvagens em `saida/` nem em `referencias/`. Ep. 02 está correto. **Pendente para o Bruno:** registrar o Ep. 01 e o Ep. 02 em `historico/publicados.md`. O agente não edita `historico/`.
- **Legenda automática com "HBO MAX": desligada nesse trecho.** Decisão: a regra escrita do 09 e do `motor/COMPONENTES.md` diz "sem logos/nomes de streaming na arte". O "ABRIU: Netflix" do Ep. 01 é um precedente que fere a regra, não um padrão a seguir. O Short 02 de hoje também deixa o nome do streaming só na fala, então os dois ficam coerentes. Como corrigi: dividi a cena da herdeira em 3 (`@o`→`@ta#2` com legenda; `@ta#2`→`@e#3` com `data-legenda="off"`; `@e#3`→`@se` com legenda), deixando card, confete e chip "T1 no catálogo" estáticos para não piscar. Em 26–31 s a tela mostra "THE PAPER." → (sem legenda) → "E A SEGUNDA / TEMPORADA CHEGA QUINTA.". **Re-renderizei** com `renderizar.py`, revi os quadros e a capa (10,4 s, igual). "HBO Max" segue na fala e na legenda do post. A narração não mudou.
- **Visual:** está no padrão do Ep. 01: cabeçalho fixo, binóculo, registro de campo, legenda grande, vinheta "A natureza se adapta." em serifa itálica, final com botão + @seriecerta. Nada cortado nem sobreposto, e nenhum logo.
- **Spoiler:** nenhum. De *The Paper* só aparece a premissa oficial.
- **Voz e CTA:** a peça tem "pra quem não é" (quem quer *The Office* igualzinho), não julga quem revê e tem um único CTA, "Manda pra quem precisa". A legenda tem 1 emoji, 5 hashtags e 202 caracteres. "Segunda temporada chega quinta" vale para hoje (terça). Se o TikTok sair depois de quinta, troque por "Segunda temporada já chegou".

## Checagens técnicas (2ª rodada)
- `validar()` dá OK em 02/yt-short e 04/ig-reel.
- **O `publicar.py --simular` em modo nuvem SOBRESCREVE o `revisao.json` local** com a cópia do Supabase. É o `baixar_pacote`, que sempre baixa os textos (.json, .md, .txt). Na 1ª execução ele trouxe de volta a versão só com 01 e 03. Reescrevi o `revisao.json` e simulei localmente (`CLAUDE_CODE_REMOTE=false MODO_NUVEM=false`), com o resultado "publicaria 02/yt-short para 13/10 18:00". O 04 não aparece porque o horário ainda não chegou, e o validar direto deu OK.
- **O pacote na nuvem (32 arquivos) não tem as pastas 02 e 04 e tem o `revisao.json` antigo.** Antes das 18h é preciso rodar `python scripts/nuvem.py subir-pacote 2026-10-13`. Sem isso, a rotina horária não publica o Reels das 20h. Também não rode `--simular` em modo nuvem antes de subir, porque ele desfaz o `revisao.json` local de novo.

## Fechamento do pacote (2026-10-13, ~11h20)
- Pacote completo subido para a nuvem (43 arquivos), com `revisao.json` final (4 aprovadas, 0 bloqueadas).
- `publicar.py --data 2026-10-13` rodou em **simulação**: `PUBLICACAO_AUTOMATICA` não está `true` no `.env`. Nada vai ao ar até o Bruno ligar a trava (o agente não altera). Primeira postagem prevista: carrossel às 13h30.
- Peças de 09/10 também não foram ao ar (mesma trava).
- Atenção para o fluxo: em modo nuvem, o `publicar.py` baixa o pacote e sobrescreve `.json/.md/.txt` locais. Sempre rodar `nuvem.py subir-pacote` **antes** do `publicar.py`, senão o `revisao.json` local volta para a cópia antiga da nuvem.
- Ambiente: o pacote `playwright` do pip precisou ser fixado em 1.56.0 para casar com o Chromium instalado (1194). Vale fixar no `requirements.txt` ou no setup da nuvem.

---

# 3ª rodada (13/10, ~15h55): carrossel 01 com pôsteres oficiais
- **Pôsteres:** os 10 itens de `imagens/posters.json` apontam para a série certa no TVmaze: The Office (2005, #526), The Paper (2025, #84611), WandaVision (2021, #41748), VisionQuest (#64950), The Haunting of Hill House (2018, #29191), Carrie (2026-10-07, #45562, a série do Flanagan com Summer H. Howell), Wednesday (2022, #53647), Coven Academy (2026-10-02, #83159), The Vampire Diaries (2009, #63) e True Blood (2008, #22). Abri os 7 JPGs (1080×1350). Os pôsteres aparecem nos cards 2–6, com a órfã pequena e a herdeira grande de borda brasa. Nada está cortado ou sobreposto, e a capa e o CTA seguem iguais.
- **Logos impressos nos pôsteres:** Disney+ (WandaVision e VisionQuest), Disney (Coven Academy), "peacock ORIGINAL" (The Paper) e KTLA/CW (TVD). Aceitei com base na regra 3 do CLAUDE.md: pôster oficial real, com cores originais e sem filtro. A regra "sem logo de streaming" do 09 vale para a arte da marca, não para o pôster oficial. **Pendente para o Bruno:** o selo Peacock aparece na mesma peça que diz "HBO Max". É fato (a série é original Peacock), mas, se incomodar, a regra precisa dizer se o pôster pode ser recortado.
- **Pôster de True Blood:** é key art de temporada posterior (a da lágrima de sangue), e a legenda fala só da T1. É a série certa, então não bloqueei.
- **Cosmético:** a seta entre os pôsteres saiu fina e cinza, não a seta brasa de 90 px do `<style>`. Alguma classe do motor sobrescreve. Não bloqueia.
- **Fatos (WebSearch, 13/10):**
  - VisionQuest estreia no Disney+ Brasil em **14/10** (2 episódios, 22h de Brasília), e "estreia esta semana" está correto ([GameOverDrive](https://gameoverdrive.com.br/visionquest-horario-episodios-o-que-assistir-antes/), [Showmetech](https://www.showmetech.com.br/lancamentos-do-disney-plus-em-outubro-de-2026/)).
  - The Paper T2 chega à HBO Max em 15/10 ([Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil), [Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/)).
  - Carrie tem 8 episódios, todos no Prime Video desde 07/10 ([GameOverDrive](https://gameoverdrive.com.br/carrie-serie-mike-flanagan-estreia-prime-video-2/)).
  - Coven Academy está inteira no Disney+ desde 02/10 ([Omelete](https://www.omelete.com.br/series-tv/coven-academy-serie-disney-plus-trailer)).
  - True Blood T1 está no Prime Video desde 05/10 ([Oficina da Net](https://www.oficinadanet.com.br/amazon-prime-video/73210-lancamentos-prime-video-outubro-2026), [Fast Company Brasil](https://fastcompanybrasil.com/tech/prime-video-chega-catalogo-outubro-2026/)).
- **Técnico:** chamei `validar()` direto (sem rodar `publicar.py`), e voltou `[]`. A legenda tem 713 caracteres e é igual à de `legenda.txt`. O `quando` é 13:30 −03:00, e com `MAX_ATRASO_HORAS=4` a janela fecha às **17h30**. Depois disso a peça vira "perdido". O `estado-publicacao.json` ainda diz "invalido" (falta de `series`), o que não trava, porque o publicador revalida.
- **Veredito:** 01 **segue aprovado**.

## Correção das 19h: pôster oficial

- **03-stories-mia-acertou:** confirmei no `cena.html` que nenhuma das 4 telas indica série. Elas só perguntam "a última série que a MIA te indicou... acertou?", então `"series": []` está correto. `validar()` voltou `[]`. **Segue aprovada.**
- **04-reels-selvagens-ep02-orfa-the-office:**
  - **Pôster:** `imagens/posters.json` aponta para o TVmaze 84611, "The Paper", com estreia em 04/09/2025. É o spin-off de The Office (Domhnall Gleeson, Oscar Nuñez), ou seja, a série do roteiro, não uma homônima. É o pôster oficial com as cores originais.
  - **Encaixe:** extraí os quadros de 26 s a 31,5 s. O pôster aparece inteiro dentro da "TV", à esquerda de "THE PAPER", sem corte e sem sobreposição. O chip "T2 · quinta, 15/10" sobrepõe o "T1 no catálogo" só durante a animação de carimbo (menos de 0,3 s) e depois assenta lado a lado. Não precisa corrigir.
  - **Marca no pôster:** o "peacock ORIGINAL" impresso no pôster fica ilegível no tamanho da cena (cerca de 250 px). Aceitei pela regra do pôster oficial (CLAUDE.md, regra 3).
  - **Vídeo e capa:** `video.mp4` tem 1080×1920, 39,98 s, com áudio. A `capa.jpg` é o quadro "ÓRFÃO DE ESCRITÓRIO", sem mudança e dentro da identidade.
  - **Validação:** `"series": ["The Paper (2025)"]` cobre a única série indicada. `validar()` voltou `[]`.
  - **Decisão:** **segue aprovada.**
- Não rodei `publicar.py` nem `nuvem.py`. Fatos, voz e legenda não foram rechecados porque não mudaram desde a revisão da manhã.
