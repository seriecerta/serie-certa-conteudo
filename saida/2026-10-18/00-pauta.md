# Pauta: domingo, 2026-10-18 (America/Sao_Paulo)

**Grade:** a grade diária de `08-cronograma.md`: carrossel e Stories às 10h00, Lista da MIA às 12h00 (YouTube 16:9), Short e Reels às 13h30, Reels às 18h30 e Short às 19h00. Blog às 09h, 11h, 14h, 17h e 20h (`11-blog.md`).
**Meta dos 90 dias:** audiência, com orçamento zero (`05`). Reels, Shorts e casal fecham com "Manda pra quem precisa".
**Período de base (14 a 20/10):** grade fixa, sem teste A/B. O registro de `10-experimentos.md` está vazio, então nenhuma peça leva `experimento`.
**Domingo:** o Reels das 18h30 conversa com "domingo à noite" (`08`). Pilar 1, porque o pilar 4 depende de demo do app.

**O que mudou em relação ao rascunho de ontem** (`saida/2026-10-17/00-pauta.md`):
- **Lista da MIA:** sai o eixo "humor/plataforma" genérico. Entra a maior tendência **brasileira** da semana: a série documental ***Marília Mendonça: Sentimento Louco*** (Prime Video, 4 episódios, todos em 16/10). O eixo é **gênero** ("séries sobre o mundo sertanejo"). É o primeiro eixo de gênero que pode ir ao ar, porque as Listas de gênero de 15 e 16/10 não saíram.
- **Blog 11h:** o rascunho falava de "Halloween nos streamings" ou "o que sai do catálogo". Não há fonte de saídas do catálogo, e o terror de outubro tem poucas séries novas (as estreias são filmes). Entra **"lançamentos HBO Max outubro 2026"**, com as fontes do dia.
- **Blog 14h:** "Acabou *Crystal Lake*?" fica, como estava no rascunho.
- O resto segue o rascunho: carrossel de *Ninguém Quer*, Tradutor reaproveitado às 13h30 e Relógio "Domingo, 21h" às 18h30/19h.

## Capacidade e prioridade de narração (ElevenLabs)
Saldo conhecido: **29 créditos** (APRENDIZADOS, 15/10). Não há registro de recarga. **Assuma que nenhum vídeo sai.** Antes de narrar, cheque o saldo. 1 caractere custa 1 crédito.

| Ordem | Pasta | Slots que cobre | Narração | Custo estimado |
|---|---|---|---|---|
| **1º** | `05-reels-short-relogio-domingo-a-noite` (Reels 18h30 + Short 19h00) | **2** | MIA, roteiro novo, ~75 palavras | **~450 caracteres** |
| **2º** | `04-short-reels-tradutor-o-que-a-mia-entende` (Short + Reels 13h30) | **2** | MIA, roteiro pronto de 15/10 | **~469 caracteres** |
| **3º** | `03-lista-da-mia-series-sertanejas` (12h00) | 1 | MIA, 5 séries, ~1 min 45 s | **~1.450 caracteres** |

- **Total:** ~2.370 caracteres. As duas primeiras cobrem 4 slots com ~920.
- O 05 vem antes do Tradutor por causa da regra de domingo e porque o gancho de envio é mais forte. Os dois custam quase o mesmo.
- **Narre uma pasta por vez, nesta ordem.** Pare no primeiro `quota_exceeded` e não tente de novo (`python scripts/narrar.py saida/2026-10-18/<pasta>`). Nunca use outro voice_id nem outro TTS.
- **Se sobrarem entre ~1.150 e ~1.450 créditos depois do 1º e do 2º:** corte o bloco do nº 5 da Lista antes de narrar. Abaixo de ~1.150, a Lista não é narrada e entra no `99-revisao.md` como slot não cumprido.
- **Sem crédito:** saem o carrossel, os Stories e o blog (nenhum gasta crédito). Os roteiros, os `.txt` e os pôsteres ficam prontos.
- **Roteiros de 15 a 17/10 que não foram narrados:**
  - O casal (`saida/2026-10-17/05-reels-short-casal-sabado-escolhe-voce`) fica para **sexta, 23/10**, a noite do casal (`08`).
  - O *Selvagens* Ep. 03 (sábado das estreias) e o "Qual sexta é você?" dependem do dia da semana. O "Qual é você?" pode virar "Qual segunda é você?" amanhã (veja o rascunho).
  - A Lista do Flanagan e a de "terror de cidade pequena" ficam para a semana do Halloween. A versão em texto do Flanagan já saiu no blog em 17/10, então essa Lista não volta como matéria.
- **Peças das 10h00:** se não estiverem aprovadas até 9h50, saem às 11h00. Se não estiverem até 10h50, saem às 15h00 (`08`). Registre no `99-revisao.md`.

## Histórico (regra de 30 dias: `historico/publicados.md` + `saida/2026-10-17/99-revisao.md`)
- **17/10 publicou** o carrossel e os Stories "Acabou A Leste do Éden?" (*Ripley*, *Pachinko*, *Peaky Blinders*) e as 5 matérias do blog. **Não saíram** a Lista do Flanagan, o *Selvagens* Ep. 03 e o casal (ElevenLabs recusou a 1ª fala).
- **Nenhuma série de hoje foi indicada nos últimos 30 dias**, com uma exceção: *Ninguém Quer* aparece no "Qual sexta é você?" de 16/10, que não foi publicado. O carrossel de hoje usa a série só como gancho (pôster no card 1).
- **Lista:** o nº 1 de hoje (*As Aventuras de José & Durval*) nunca foi usado. Nos últimos 30 dias, os nº 1 foram *Olhos que Condenam* (14/10, publicada) e *Residência Hill* (17/10, não publicada).
- **Eixos da Lista:** 14/10 "acabou X?" (publicada) · 15/10 gênero (não saiu) · 16/10 gênero (não saiu) · 17/10 criador (não saiu) · **18/10 gênero (sertanejo)**. Não repete eixo + tema em 14 dias, porque o tema é novo.

## Nota de verificação
- **WebFetch caiu em DNS** (ENOTFOUND) em opovo.com.br. Tudo foi checado por WebSearch em 18/10, perto das 06h45.
- **Não há Top 10 semanal da Netflix nem do Prime Video do Brasil** nas buscas de hoje. Nenhuma peça afirma posição em ranking.
- ⚠️ = o redator ou o roteirista confere **no dia** pela API GraphQL do JustWatch BR (`popularTitles(country:BR…)`, ofertas `FLATRATE`, temporadas e episódios) e pela `netflix.com/br/title/<id>` com user-agent de Googlebot (APRENDIZADOS, 17/10). O revisor confirma. Série sem confirmação sai e a reserva entra.
- **Não afirmar** duração de episódio, nº de temporadas nem horário de estreia marcados com ⚠️ sem essa confirmação.

---

# HOJE: 2026-10-18

## 01-carrossel-ninguem-quer-volta-quinta (Instagram · Carrossel · 10h00)
- **Formato:** 7 cards de 1080×1350 (`--imagens --formato 4x5`), um `section.quadro` por card. Sem narração.
- **Pilar:** 2. Órfã de série (na versão "esperando a volta") · **Job:** emocional 3 (quero algo com a mesma sensação enquanto a minha série não volta) · **Humor:** romântico (`--romantico` no card 1; a cor de cada série nos seguintes).
- **Estágio / CTA:** Consideração · "**Salva pra ver até quinta.**" (um só).
- **Formato de referência:** card de indicação com selo "onde assistir" + recibo (`saida/2026-10-17/01-carrossel-acabou-a-leste-do-eden/`).
- **Gancho (card 1):** "*Ninguém Quer* volta quinta. E até lá?" Subtítulo: "4 comédias românticas de gente grande pra segurar a ansiedade." Pôster de *Ninguém Quer* + 🫶.
- **Por que agora:** a 3ª temporada chega à Netflix na **quinta, 22/10**, com trailer novo ([Omelete, data](https://www.omelete.com.br/series-tv/ninguem-quer-3a-temporada-data-estreia-netflix); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/netflix-divulga-data-de-estreia-e-primeiras-imagens-da-3a-temporada-de-ninguem-quer/); [Einerd, trailer](https://www.einerd.com/ninguem-quer-3a-temporada-ganha-trailer-com-joanne-e-noah-morando-juntos/)). **Não citar o nº de episódios** da T3 (nenhuma fonte traz). Spoiler zero sobre as temporadas 1 e 2: só "o casal volta".
- **Cards** (todas originais das plataformas; ⚠️ em todas, conferir no JustWatch BR):
  2. ***Love*** · Netflix · 3 temporadas, encerrada (2016–2018), de Judd Apatow. Por que combina: casal adulto, desajeitado e real, com humor. Pra quem não é: quem quer casal fofo desde o 1º episódio (os dois são difíceis).
  3. ***Lovesick*** · Netflix · 3 temporadas, comédia britânica. Por que combina: amizade que vira romance devagar, episódios curtos. Pra quem não é: quem não curte história contada fora de ordem.
  4. ***Modern Love*** · Prime Video · antologia, cada episódio um casal. Por que combina: dá pra ver um por noite, sem compromisso. Pra quem não é: quem quer acompanhar o mesmo casal.
  5. ***Catastrophe*** · Prime Video · 4 temporadas de episódios curtos. Por que combina: casal que se mete numa vida a dois sem planejar, com humor ácido. Pra quem não é: quem não gosta de comédia de palavrão.
  - **Reserva:** *Master of None* (Netflix, original). Se faltarem duas, o carrossel fica com 3 séries + recibo + CTA (6 cards).
  6. **Recibo "contagem até quinta"** (cupom do motor): série → streaming das que ficaram. Não indica série nova.
  7. **CTA:** "Salva pra ver até quinta." + @seriecerta.
- **Legenda:** gancho + "Love (Netflix) · Lovesick (Netflix) · Modern Love (Prime Video) · Catastrophe (Prime Video)" + "Salva pra ver até quinta." No máximo 2 emojis. Hashtags: #seriecerta #oqueassistir #ninguemquer #comediaromantica.
- **Comentário fixado:** só onde assistir cada série, sem pedido (o padrão de 15 a 17/10).
- **Pôsteres:** `python scripts/posters.py <pasta> "Nobody Wants This" "Love (2016)" "Lovesick" "Modern Love" "Catastrophe (2015)"`. *Nobody Wants This* é o TVmaze #77060, já baixado em `saida/2026-10-16/04-short-reels-qual-sexta-e-voce/imagens/nobody-wants-this.jpg`. **Corte o rodapé "ONLY ON NETFLIX | OCTOBER 22"** com `object-position: top`. *Love* é a da Netflix (2016), não outra com o mesmo nome. Logos de streaming ficam fora do recorte.
- **`"series"`:** ["Ninguém Quer", "Love", "Lovesick", "Modern Love", "Catastrophe"] (tire a que sair).
- **Horário:** Instagram CAROUSEL `2026-10-18T10:00:00-03:00` (se atrasar, 11h00 e depois 15h00).

## 02-stories-ninguem-quer-volta-quinta (Instagram · Stories · 10h00)
- **Formato:** o carrossel 01 em 9:16 (1080×1920), **4 telas + 1 de CTA**. Pode usar `"peca_mae": "01-carrossel-ninguem-quer-volta-quinta"`. Sem narração.
- **Pilar:** 2 · **Job:** emocional 3 · **Humor:** romântico.
- **Telas:** 1. "*Ninguém Quer* volta quinta. E até lá?" (pôster) · 2. *Love* · 3. *Modern Love* · 4. *Catastrophe* (ou a que sobrar) · 5. CTA. "Toca pra ver →" na tela 1 (correção do revisor de 17/10).
- **CTA / funil:** Conversão, um só: "**A MIA acha a próxima pelo seu humor. Testa grátis no link da bio.**"
- **Link da bio:** `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-18-stories-ninguem-quer-volta-quinta` (sem `humor=`, porque o slug não está confirmado).
- **`"series"`:** as séries das telas.
- **Horário:** Instagram STORIES `2026-10-18T10:00:00-03:00` (mesmo plano de atraso do 01).

## 03-lista-da-mia-series-sertanejas (YouTube · Lista da MIA 16:9 · 12h00)
- **Formato:** Lista da MIA em 1920×1080, **~1 min 45 s**, contagem regressiva de **5 séries** (a nº 1 por último). Vídeo: `motor/exemplos/lista-da-mia-16x9.html` com `<body class="paisagem" style="--mood:var(--romantico)">`. Thumb: `motor/exemplos/lista-da-mia-thumb.html` com o **"5"** gigante, "SÉRIES PRA QUEM AMA SERTANEJO" e 🤠.
- **Pilar:** 2. Órfã de série (para quem terminou o doc no fim de semana; o tema vem da tendência) · **Job:** emocional 3 · **`--mood`:** romântico (a sofrência).
- **Eixo:** **gênero/subgênero**: séries sobre o mundo sertanejo, entre ficção e documentário.
- **Tema:** "Viu o doc da Marília Mendonça? 5 séries pra continuar no sertanejo".
- **Por que é tendência (3 sinais):**
  1. **Estreia brasileira da semana:** *Marília Mendonça: Sentimento Louco* (Prime Video) estreou na **sexta, 16/10, com os 4 episódios de uma vez**. A direção é de Susanna Lira, e a série tem acervo da família, com mais de 530 mil imagens e 50 mil vídeos ([TNH1](https://www.tnh1.com.br/noticia/nid/serie-documental-sobre-marilia-mendonca-estreia-nesta-sexta-veja-onde-assistir/); [Jornal Opção](https://www.jornalopcao.com.br/entretenimento/marilia-mendonca-serie-documental-prime-video-879083/); [GameOverDrive, episódios](https://gameoverdrive.com.br/marilia-mendonca-sentimento-louco-episodios/)).
  2. **Imprensa de cultura pop:** crítica e entrevista com a diretora no Omelete ([crítica](https://www.omelete.com.br/series-tv/marilia-mendonca-sentimento-louco-documentario-critica); [entrevista](https://www.omelete.com.br/series-tv/marilia-mendonca-sentimento-louco-entrevista-documentario)). O Vida&Arte (O Povo) põe a série entre os destaques da semana, ao lado de *VisionQuest* ([O Povo, 16/10](https://www.opovo.com.br/vidaearte/2026/10/16/disney-prime-video-e-netflix-confira-as-estreias-da-semana-12-10-a-18-10.html)).
  3. **Conversa fora da tela:** a exposição *Marília* fica no MIS de São Paulo de 09/10 a 29/11, e o filme de ficção sobre ela está previsto para 2027 ([Omelete, trailer e exposição](https://www.omelete.com.br/series-tv/marilia-mendonca-doc-prime-video-trailer-data-exposicao); [TNH1](https://www.tnh1.com.br/noticia/nid/serie-documental-sobre-marilia-mendonca-estreia-nesta-sexta-veja-onde-assistir/)).
  - **Lacuna:** não há Top 10 do Prime Video Brasil nem sinal direto de Google Trends ou X. **Não diga "a mais vista".** Diga "estreou na sexta".
- **Título (≤ 70):** **"Viu o doc da Marília Mendonça? 5 séries pra continuar no sertanejo"** (66 caracteres).
- **Gancho (0–15 s):** "Terminou *Sentimento Louco* com o coração apertado? Então você não quer largar esse mundo agora. Tenho cinco séries pra você continuar nele." Pôster de *Sentimento Louco* na abertura.
- **Cuidado de tom (obrigatório):** acolhedor e respeitoso. Nada de piada com a morte da cantora, nada sobre o acidente, nada de "chorei horrores" como riso. **Zero letra de música** (`CLAUDE.md`, regra 3): título de canção pode aparecer, verso não.
- **Séries (contagem regressiva; ⚠️ em todas: o roteirista confere o catálogo de hoje no JustWatch BR; Globoplay e Prime são catálogos próprios, risco médio):**
  5. ***Em Casa com os Gil*** · Prime Video · série documental de **5 episódios** (24/06/2022), sobre a família de Gilberto Gil preparando a turnê dos 80 anos dele ([O Imparcial](https://oimparcial.com.br/noticias/2022/06/com-intimismo-e-toques-de-reality-em-casa-com-os-gil-estreia-no-prime-video/); [O Povo+](https://mais.opovo.com.br/jornal/vidaearte/2022/06/20/em-casa-com-os-gil-reality-reune-familia-gil-em-preparacao-para-turne.html)). Por que combina: é o mesmo jeito de ver família e música por dentro, sem a dor. Pra quem não é: quem quer sertanejo (é MPB).
  4. ***Só Se For Por Amor*** · Netflix · ficção, **1 temporada de 6 episódios** (set/2022), passada em Goiás, com sertanejo e sofrência, e com Lucy Alves, Filipe Bragança e Agnes Nunes ([Netflix About](https://about.netflix.com/pt_br/news/so-se-for-por-amor-sertanejo-sofrencia-music-is-the-chosen-tune-for-netflixs); [O Popular](https://opopular.com.br/magazine/nova-serie-da-netflix-e-ambientada-em-goias-ao-som-de-sertanejo-e-sofrencia-1.2347937)). Por que combina: banda, amor e carreira solo puxando para lados opostos. Pra quem não é: quem não gosta de série musical (tem número cantado).
  3. ***Sandy & Junior: A História*** · Globoplay · série documental de **7 episódios** de cerca de 1 hora (10/07/2020) ([Guia da Semana](https://www.guiadasemana.com.br/filmes-e-series/noticia/serie-sandy-e-junior-a-historia-estreia-dia-10-de-julho-no-globoplay); [Oficina da Net](https://www.oficinadanet.com.br/entretenimento/31819-sandy-e-junior-a-historia-serie-ja-esta-disponivel-no-globoplay)). Por que combina: acervo pessoal, fama desde criança e o peso de ser ídolo. E os dois são filhos do Xororó, o elo com o nº 1. Pra quem não é: quem não tem paciência para episódio de uma hora.
  2. ***Rensga Hits!*** · Globoplay · ficção, **3 temporadas** (2022, 2024 e 2025; a T3 tem 8 episódios), passada no mercado sertanejo de Goiânia ([Canaltech](https://canaltech.com.br/entretenimento/rensga-hits-vai-ter-segunda-temporada-224769/); [Billboard Brasil, T2](https://billboard.com.br/segunda-temporada-rensga-hits-ganha-data-estreia/); [Señal News, T3](https://senalnews.com/es/digital/globoplay-estrenara-la-tercera-temporada-de-rensga-hits/amp)). Por que combina: mulheres compositoras tentando o lugar delas no sertanejo, a mesma estrada que o doc mostra. Pra quem não é: quem quer documentário (é ficção, com humor).
  1. ***As Aventuras de José & Durval*** · Globoplay · ficção, **8 episódios de 45 min** (ago/2023), sobre a origem de Chitãozinho & Xororó, com Rodrigo e Felipe Simas ([Canaltech](https://canaltech.com.br/entretenimento/as-aventuras-de-jose-e-durval-conheca-a-serie-sobre-chitaozinho-e-xororo-259384/); [AdoroCinema](https://www.adorocinema.com/series/serie-31483/)). Por que combina: a estrada, a família e o começo de tudo no sertanejo, com emoção do começo ao fim. Pra quem não é: quem quer só fatos (mistura história real com ficção, e a série diz isso).
  - **Reservas:** *Clube do Araújo* (Globoplay, 10 episódios, documental) e *Anitta: Made in Honório* (Netflix, documental). Ambas ⚠️.
  - **Pôster:** se o TVmaze não tiver o pôster de uma série brasileira, **troque pela reserva**. Não use capa gerada na Lista (`07`). Se ficarem só 3, a Lista sai com 3 (é o mínimo) e o título passa a "3 séries".
- **Pôsteres:** `python scripts/posters.py <pasta> "Marília Mendonça: Sentimento Louco" "Em Casa com os Gil" "Só Se For Por Amor" "Sandy & Junior: A História" "Rensga Hits!" "As Aventuras de José & Durval"`. Confira nome e ano em `posters.json`. Corte os logos de streaming.
- **Demo do app:** não entra (`assets/demo/` vazio).
- **Fim e CTA único:** "**Salva pra hoje à noite**" (Consideração) + link fixado. Sem pergunta para os comentários (o padrão de 14 a 17/10). O comentário fixado lista onde assistir cada série.
- **Descrição:** capítulos (00:00 abertura e um por série, calculados pelo `narracao.json` + 0,30 s), onde assistir cada uma e a UTM `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-18-lista-da-mia-series-sertanejas`.
- **Tags:** marília mendonça, sentimento louco, sertanejo, séries sertanejas, rensga hits, chitãozinho e xororó, josé e durval, sandy e junior, só se for por amor, globoplay.
- **`"series"`:** ["Marília Mendonça: Sentimento Louco", "Em Casa com os Gil", "Só Se For Por Amor", "Sandy & Junior: A História", "Rensga Hits!", "As Aventuras de José & Durval"]. *Sentimento Louco* entra porque o pôster aparece na abertura.
- **Horário:** YouTube `2026-10-18T12:00:00-03:00` (3º na fila de narração).

## 04-short-reels-tradutor-o-que-a-mia-entende (YouTube Short + Instagram Reels · 13h30 · **o mesmo vídeo**)
- **Decisão:** um arquivo 9:16, publicado duas vezes no `publicar.json` (`YOUTUBE_SHORT` + `REELS`), ambas em `2026-10-18T13:30:00-03:00`. TikTok: o mesmo arquivo.
- **Reaproveitamento:** copie `saida/2026-10-15/06-short-tradutor-o-que-a-mia-entende/`. O texto não cita dia da semana. **Troque só as UTMs** (`utm_campaign=2026-10-18-short-tradutor-o-que-a-mia-entende`) e o `quando`.
- **Formato:** Tradutor de indicação (`09`). Base: `referencias/quadros/reels-2-tradutor.jpg`.
- **Pilar:** 5. Bastidor do produto · **Força:** Atração · **Humor:** vários (4 cores).
- **Gancho:** "Pra amiga que pede indicação e responde 'qualquer coisa'." Não repete o Tradutor de 13/10, que era "órfã de terror" com *Residência Hill* e *Carrie*.
- **CTA:** "Manda pra quem precisa" (Descoberta), falado e no botão. Um só.
- **`"series"`:** [] (nenhuma série indicada, sem pôster).
- **Custo:** 469 caracteres. 2º na fila de narração.

## 05-reels-short-relogio-domingo-a-noite (Instagram Reels 18h30 + YouTube Short 19h00 · **o mesmo vídeo**)
- **Decisão:** um arquivo 9:16, publicado duas vezes: `REELS` em `2026-10-18T18:30:00-03:00` e `YOUTUBE_SHORT` em `2026-10-18T19:00:00-03:00`. TikTok: o mesmo arquivo.
- **Formato:** Relógio / ritual (`09`): relógio no topo correndo enquanto a MIA narra. Abra a folha de quadros do "Quarta, 21h" em `referencias/` antes de montar.
- **Pilar:** 1. Série pro seu humor · **Job:** emocional 2 (quando estou ansiosa, quero algo previsível e confortável, para desligar a cabeça) · **Humor:** ansioso (`--ansioso`).
- **Regra de domingo:** cumprida (Reels 18h30 sobre "domingo à noite").
- **Gancho (0–2 s, falado + tela):** "Pra amiga que fica ansiosa domingo à noite." Tela: relógio **"DOM · 21:00"**.
- **Roteiro (~75 palavras, ~450 caracteres; o roteirista escreve a versão final, uma só):** 21:00 a cabeça já está na segunda (lista de tarefas aparecendo em carimbos genéricos) → 21:40 abre três séries pesadas e fecha → a MIA corta: "Domingo à noite não é dia de série nova e tensa. É dia de série que abraça." → a série → CTA. Virada leve no fim: "segunda que lute" (sem deboche de quem tem ansiedade).
- **Série:** ***Abbott Elementary*** · Disney+ · comédia de escola em formato de documentário, com episódios curtos. A Omelete (ago/2026) diz que as temporadas estão no Disney+ e que a T6 estreou nos EUA em 07/10 ([Omelete, T6](https://www.omelete.com.br/series-tv/abott-elementary-6a-temporada-anuncio-miranda-cosgrove-edi-patterson-ali-wong); [Omelete, imagens da T6](https://www.omelete.com.br/series-tv/elenco-de-abbott-elementary-primeiras-imagens-6-temporada)). ⚠️ **Não citar** nº de temporadas, a T6 nem a duração sem conferir no JustWatch BR. A fala pode dizer "episódio de vinte minutinhos" só se o TVmaze confirmar. Por que combina: gente boa tentando, sem surpresa ruim, risada fácil. Pra quem não é: quem não curte humor de "falso documentário".
  - **Reserva** (se o Disney+ BR não confirmar): *Modern Family* (Disney+), ⚠️.
- **CTA:** botão brasa "**MANDA PRA QUEM PRECISA**" + @seriecerta (Descoberta), falado e na tela. Um só.
- **Legenda IG:** "Pra amiga que fica ansiosa domingo à noite 🫂" + "Abbott Elementary (Disney+)" + "Manda pra quem precisa." #seriecerta #domingoanoite #oqueassistir #abbottelementary. **Título YT:** "Domingo, 21h: a série certa pra ansiedade de domingo".
- **UTM (descrição YT):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-18-short-relogio-domingo-a-noite`.
- **Pôster:** `python scripts/posters.py <pasta> "Abbott Elementary"`.
- **`"series"`:** ["Abbott Elementary"].
- **Custo:** ~450 caracteres. 1º na fila de narração.

**Pilares de hoje:** 2 (carrossel, Stories e Lista), 5 (13h30) e 1 (18h30/19h). Reels: 5 × 1 ✓. Shorts: 5 × 1 ✓.
**Semana, contando só o que foi ao ar de 14 a 17/10:** o pilar 1 domina, o 2 veio no carrossel de 17/10 e os pilares 3, 4 e 5 seguem em zero. Hoje o 5 entra, se houver crédito. O 3 volta na sexta (23/10). O 4 segue travado sem demo.

---

# RASCUNHO DE AMANHÃ: segunda, 2026-10-19
> A rotina de amanhã refaz a pesquisa de tendência e **revalida todos os fatos**. Pasta: `saida/2026-10-19/`.

## 01-carrossel + 02-stories (10h00)
- **Pilar 1.** Proposta: "Segunda-feira: séries de episódio curto que cabem na semana" (humor sono/cansada), com séries novas no histórico. Não usar *Abbott Elementary* (Reels de hoje).
- Stories: o carrossel em 9:16 + CTA de Conversão.

## 03-lista-da-mia (12h00)
- **Eixo diferente de gênero:** ator/atriz ou plataforma. Candidatos:
  - Chris Pratt, porque *A Lista Terminal* T2 chega na quarta (21/10).
  - George Kay, criador de *Lupin* (parte 4 em 23/10) e de *Guerra* (HBO Max).
  - O que sair no Top 10 da Netflix de terça.
- O nº 1 não pode ser *As Aventuras de José & Durval*, *Olhos que Condenam* nem *Residência Hill*.

## 04-short-reels-qual-segunda-e-voce (13h30, YouTube + Instagram, mesmo vídeo)
- **Reaproveitar** `saida/2026-10-16/04-short-reels-qual-sexta-e-voce/` (pilar 1, ~651 caracteres), trocando "sexta" por "segunda" e rechecando as 4 séries. O tipo 3 ("quer medo") pode ficar, porque é outubro. Se *Ninguém Quer* estiver no roteiro, mantenha só se a fala não repetir o gancho do carrossel de hoje.

## 05-reels-short (18h30 + 19h00, mesmo vídeo)
- **Pilar 2 ou 5**, sem repetir o pilar do 04. Ideia: Relógio "Segunda, 21h: a série acabou e a segunda começou" (órfã), com 1 série checada no dia.
- **Prioridade de crédito:** 05 → 04 → Lista.

## Blog de segunda (rascunho)
- **09h, humor `feliz`.** O humor não se repete em 7 dias: 14/10 sono, 16/10 estressado, 17/10 triste e 18/10 ansioso. Palavra-chave: "séries para começar a semana de bom humor".
- **11h:** *Cyberpunk: Mercenários* T2 chega na terça (20/10, já na matéria de 19 a 25/10). Melhor: "Globoplay em outubro 2026", só com fonte do dia.
- **14h:** "Acabou *Carrie*?" com séries que não sejam do Flanagan (não repetir a lista de 17/10).
- **17h:** guia "*A Lista Terminal* 2ª temporada: como rever a 1ª antes de quarta".
- **20h:** a Lista de segunda em texto.

---

## Ideias guardadas (revalidar antes de usar)
- *Slow Horses* T6 termina na quarta (21/10): pilar 2 "acabou Slow Horses?" na quinta (22/10).
- *Guerra* (*War*, HBO Max): 8 episódios semanais às quintas, com final previsto para 19/11 ([GameOverDrive](https://gameoverdrive.com.br/guerra-hbo-max-episodios-calendario/)). Dá um "acabou Guerra?" em 20/11.
- Casal de 17/10 (*Sr. e Sra. Smith*): sexta, 23/10, com fatos rechecados.
- Lista "terror de cidade pequena" (15/10) e Lista do Flanagan (17/10): semana do Halloween (até 31/10).

## Pendências para o Bruno
1. **Créditos da ElevenLabs:** quinto dia sem recarga. O dia pede ~2.370 caracteres. Sem crédito, saem só o carrossel, os Stories e o blog. Já são 5 dias do período de base sem vídeo, o que deixa a revisão de 21/10 sem base de Reels, Shorts e Lista.
2. **Bio do Instagram:** trocar para a UTM do Stories de hoje antes das 10h00 (troca manual).
3. **Domínios** (`nuvem/dominios-permitidos.txt`): JustWatch, Netflix, FlixPatrol e O Povo seguem sem WebFetch.
4. **Slug `humor=<humor>`** e link do modo casal no app: ainda sem confirmação, então os links vão sem humor.
5. **Demo do app** em `assets/demo/`: sem ela, o pilar 4 (15%) não sai.

---

## Blog
> Grade e padrão: `estrategia/11-blog.md` · pacote e publicação: `blog/README.md`. Pastas: `saida/2026-10-18/blog/<nn>-<slug>/`.
> **No ar (60 dias, `--listar` colado no pedido):** `series-de-mike-flanagan`, `slow-horses-temporadas-guia`, `series-parecidas-com-a-leste-do-eden`, `estreias-streaming-semana-19-a-25-outubro-2026`, `series-para-quando-voce-esta-triste`, `series-parecidas-com-a-diplomata`, `lupin-parte-4-guia`, `series-parecidas-com-profundezas`, `estreias-streaming-semana-12-a-18-outubro-2026`, `series-leves-para-relaxar`, `series-para-assistir-com-sono`, `como-escolher-serie-pelo-humor`, `como-calcular-tempo-de-maratona`, `minisseries-e-series-curtas` e `como-organizar-assinaturas-de-streaming`. **Nenhuma palavra-chave nem lista de séries de hoje repete essas matérias.** A matéria de estreias de 19 a 25/10 saiu ontem, por isso a 02 de hoje é um recorte por plataforma (HBO Max no mês), não a semana.
> **Destaque único no dia:** nenhuma série é destaque em duas matérias. A das 20h repete a Lista, como manda a regra. A 01 não usa *Abbott Elementary* (Reels de hoje) e a 04 não repete as comédias do carrossel.
> **Verificação:** tudo foi conferido por WebSearch em 18/10. Onde há ⚠️, o redator confere no JustWatch BR (API GraphQL) e na Netflix BR (curl), e o revisor confirma. Sem confirmação, a série sai. Toda matéria com disponibilidade leva `:::info Conferido em 18/10/2026`.
> **Lista de 14/10 (`series-para-assistir-com-sono`):** o redator abre a matéria no ar e confirma que a 01 não repete mais de 2 séries dela.

### 01 · 09h00 · Pelo humor
- **Título provisório:** 7 séries para quando você está ansiosa (e precisa de algo previsível)
- **Palavra-chave principal:** séries para quando você está ansiosa
- **Slug:** `series-para-quando-voce-esta-ansiosa` · **Categoria:** `o-que-assistir` · **Humor:** `ansioso` (CTA `[[app: ansioso]]`). O humor não se repete no slot em 7 dias (14/10 sono, 16/10 estressado, 17/10 triste).
- **Job:** emocional 2 (quando estou ansiosa, quero algo previsível e confortável, para desligar a cabeça).
- **Gancho de abertura:** o domingo à noite (a matéria sai num domingo), mas o texto é perene, para qualquer dia.
- **Séries (⚠️ em todas: o redator confere no JustWatch BR, com temporadas e episódios; sai a que não confirmar):**
  1. ***The Good Place*** · Netflix ⚠️ · comédia de episódios curtos, 4 temporadas, encerrada. Pra quem não é: quem não curte comédia com filosofia.
  2. ***Queer Eye*** · Netflix ⚠️ · reality de transformação, gentil e previsível. Pra quem não é: quem não gosta de reality.
  3. ***Modern Family*** · Disney+ ⚠️ · sitcom familiar, 11 temporadas, para ver em qualquer ordem. Pra quem não é: quem já viu e quer novidade.
  4. ***Gilmore Girls*** · ⚠️ confirmar o streaming (Netflix ou HBO Max). Ritmo de conversa, cidade pequena, zero susto. Pra quem não é: quem se cansa de diálogo rápido.
  5. ***Brooklyn Nine-Nine*** · ⚠️ confirmar o streaming. Comédia policial sem tensão de verdade. Pra quem não é: quem quer crime sério.
  6. ***Mestres da Confeitaria*** (*The Great British Bake Off*) · Netflix ⚠️ · competição em que ninguém é cruel. Pra quem não é: quem quer drama de reality.
  7. ***Parks and Recreation*** · ⚠️ confirmar o streaming. Gente otimista e episódios de 20 minutos. Pra quem não é: quem não curte o estilo "falso documentário".
  - **Reserva:** *Schitt's Creek* ⚠️. Não usar *Ted Lasso*, *Only Murders*, *Heartstopper*, *Hacks*, *Emily em Paris* nem *Falando a Real* (matéria de 16/10). Se ficarem só 5, a matéria sai com 5 e o título muda.
- **Cuidado de tom:** acolher sem diagnosticar. Nada de "cura", "tratamento" nem conselho de saúde. Uma linha de cuidado (CVV 188) só se o texto falar de crise. É ansiedade do dia a dia, não transtorno.
- **Linkar:** `[[leia: como-escolher-serie-pelo-humor]]`, `[[leia: series-leves-para-relaxar]]`, `[[leia: series-para-assistir-com-sono]]`.
- **Link do app:** `https://seriecerta.online/descobrir?humor=ansioso&utm_source=blog&utm_medium=organico&utm_campaign=2026-10-18-series-para-quando-voce-esta-ansiosa`.

### 02 · 11h00 · Streaming da semana
- **Título provisório:** Lançamentos HBO Max outubro 2026: Guerra, The Paper, Largados e Pelados Brasil e o que ainda vem
- **Palavra-chave principal:** lançamentos HBO Max outubro 2026
- **Slug:** `lancamentos-hbo-max-outubro-2026` (com data, porque o tema é datado) · **Categoria:** `streaming` · **Humor:** `animado` (CTA `[[app: animado]]`).
- **Job:** principal (saber o que vale ver no streaming que já assina).
- **Por que é tendência / fontes:**
  - Hoje, 18/10, estreia a T4 de *Largados e Pelados Brasil*.
  - *Guerra* está no meio da temporada.
  - Ainda vêm *A Promessa* (19/10) e *O Colombiano de Keko* (22/10).
  - Fontes: [Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/), [Oficina da Net](https://www.oficinadanet.com.br/hbo-max/73209-hbo-max-lancamentos-outubro-2026) e [Showmetech](https://www.showmetech.com.br/lancamentos-hbo-max-outubro-2026/).
- **Séries (em ordem de data):**
  1. ***Guerra*** (*War*) · HBO Max · desde 01/10, **8 episódios semanais às quintas**, com final previsto para 19/11. Drama jurídico sobre um divórcio bilionário, com Sienna Miller e Dominic West, criado por George Kay (de *Lupin*). Já tem 2ª temporada encomendada ([GameOverDrive, calendário](https://gameoverdrive.com.br/guerra-hbo-max-episodios-calendario/); [Omelete, trailer](https://www.omelete.com.br/series-tv/war-hbo-serie-criador-de-lupin-trailer); [Einerd](https://www.einerd.com/war-hbo-divulga-trailer-do-drama-juridico-com-dominic-west-e-sienna-miller/)). ⚠️ O redator confere no JustWatch o horário e se o final é mesmo em 19/11 (é projeção do calendário).
  2. ***Get Jiro*** · HBO Max · 04/10, animação baseada em quadrinhos ([Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/)). ⚠️ Fonte única: confirme em uma segunda fonte ou o item sai.
  3. ***The Paper*** T2 · HBO Max · 15/10 ([Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/)). ⚠️ O redator confere se os episódios saíram todos juntos ou se são semanais.
  4. ***Largados e Pelados Brasil*** T4 · HBO Max · **hoje, 18/10** ([Itatiaia](https://www.itatiaia.com.br/entretenimento/veja-os-lancamentos-de-series-e-filmes-da-hbo-max-para-outubro-de-2026/); [Oficina da Net](https://www.oficinadanet.com.br/hbo-max/73209-hbo-max-lancamentos-outubro-2026)). Já apareceu na matéria de 12 a 18/10. Aqui entra em um parágrafo curto, com `[[leia: estreias-streaming-semana-12-a-18-outubro-2026]]`.
  5. ***A Promessa*** · HBO Max · 19/10 ⚠️ (sem sinopse confiável no dia: o redator busca; sem sinopse, o item sai).
  6. ***O Colombiano de Keko*** · HBO Max · 22/10 ⚠️ (idem).
  - **Fora:** *Estado de Fúria* e *Masterchef Profissionais* T6 (09/10), só se o redator achar o formato e a sinopse com fonte. Se a matéria ficar com menos de 5 itens confirmados, complete com um `##` "O que vale começar agora no HBO Max", sem indicar série nova sem fonte. O título acompanha o que ficar.
- **Linkar:** `[[leia: estreias-streaming-semana-12-a-18-outubro-2026]]`, `[[leia: estreias-streaming-semana-19-a-25-outubro-2026]]`, `[[leia: como-organizar-assinaturas-de-streaming]]`.

### 03 · 14h00 · Acabou X?
- **Título provisório:** Acabou Crystal Lake? 6 séries de terror slasher para continuar no clima
- **Palavra-chave principal:** séries parecidas com Crystal Lake
- **Slug:** `series-parecidas-com-crystal-lake` · **Categoria:** `series` · **Humor:** `curioso` (CTA `[[app: curioso]]`).
- **Job:** emocional 3.
- ***Crystal Lake*** (gancho, com pôster no topo e no `"series"`): prelúdio de *Sexta-Feira 13*, **8 episódios, todos em 16/10, no Universal+**. O Universal+ é assinatura própria e também é vendido como canal em parceiros, como o Prime Video. **Não diga que está "no Prime Video"**: o pacote básico não inclui ([GameOverDrive, onde assistir](https://gameoverdrive.com.br/crystal-lake-onde-assistir-brasil/); [Legião dos Heróis](https://www.legiaodosherois.com.br/2026/crystal-lake-onde-assistir-a-serie-prequel-de-sexta-feira-13-aqui-no-brasil.html); [BNews](https://www.bnewssaopaulo.com.br/noticias/entretenimento/crystal-lake-onde-assistir-a-serie-de-sexta-feira-13-no-brasil.html)). Spoiler zero.
- **Por que é tendência:**
  - Estreou na sexta, com 79% de aprovação no Rotten Tomatoes ([GameOverDrive](https://gameoverdrive.com.br/crystal-lake-aprovacao-rotten-tomatoes-estreia/)).
  - É o mês do Halloween: a Netflix pôs 22 filmes de terror no catálogo de outubro ([GameOverDrive](https://gameoverdrive.com.br/filmes-terror-netflix-outubro-2026-halloween/)).
  - A temporada saiu inteira de uma vez, então quem maratonou no fim de semana já terminou.
  - Não há ranking brasileiro: não afirme posição.
- **Séries (⚠️ em todas: o redator confere no JustWatch BR; sai a que não confirmar):**
  1. ***American Horror Story: 1984*** (9ª temporada) · Disney+ ⚠️ · acampamento de verão e assassino mascarado, a homenagem mais direta a *Sexta-Feira 13*. Pra quem não é: quem não quer ver as outras temporadas fora de ordem (cada uma é independente, então pode).
  2. ***Bates Motel*** · ⚠️ confirmar o streaming · também é prelúdio de um clássico do terror (*Psicose*). Pra quem não é: quem quer susto rápido (é drama lento).
  3. ***Scream Queens*** · ⚠️ confirmar o streaming · slasher com comédia. Pra quem não é: quem quer terror sério.
  4. ***Chucky*** · ⚠️ confirmar o streaming · série da franquia do boneco. Pra quem não é: quem não aguenta sangue.
  5. ***Yellowjackets*** · ⚠️ confirmar o streaming (ela já foi listada na matéria de *Profundezas*, mas aqui a lista é outra) · sobrevivência na floresta e o passado que volta. Pra quem não é: quem não aguenta violência gráfica.
  6. ***Slasher*** · ⚠️ confirmar o streaming · antologia de assassino mascarado. Pra quem não é: quem não aguenta violência gráfica.
  - **Reserva:** *Pânico* (a série) ⚠️. Não usar *Carrie* nem as séries do Flanagan (matéria de 17/10). Se ficarem só 4, a matéria sai com 4 e o título muda.
- **Linkar:** `[[leia: series-de-mike-flanagan]]`, `[[leia: series-parecidas-com-profundezas]]`.

### 04 · 17h00 · Guia
- **Título provisório:** Ninguém Quer 3ª temporada: quando estreia, onde ver e como rever as duas primeiras
- **Palavra-chave principal:** Ninguém Quer 3ª temporada
- **Slug:** `ninguem-quer-3-temporada-guia` · **Categoria:** `guias` · **Humor:** `romantico` (CTA `[[app: romantico]]`).
- **Job:** principal (o que ver, em que ordem e quanto tempo leva). Secundário: emocional 3.
- **Série (1):** ***Ninguém Quer*** · Netflix · T3 em **22/10** ([Omelete](https://www.omelete.com.br/series-tv/ninguem-quer-3a-temporada-data-estreia-netflix); [Critical Hits](https://criticalhits.com.br/cinema-e-tv/netflix-divulga-data-de-estreia-e-primeiras-imagens-da-3a-temporada-de-ninguem-quer/); [Einerd, trailer](https://www.einerd.com/ninguem-quer-3a-temporada-ganha-trailer-com-joanne-e-noah-morando-juntos/)).
  - O guia traz:
    - a premissa da T1 (podcaster e rabino);
    - quantos episódios e quanto tempo têm a T1 e a T2 (⚠️ o redator confirma no JustWatch/TVmaze antes de somar);
    - a conta do tempo de maratona (como **estimativa**, pelo método de `como-calcular-tempo-de-maratona`);
    - o que a Netflix já mostrou da T3: "Joanne e Noah morando juntos", que está no trailer oficial (só isso);
    - pra quem não é.
  - **Não citar** o nº de episódios da T3 (nenhuma fonte traz) nem horário de estreia sem fonte.
  - **Spoiler zero:** nada do fim da T1 nem da T2 além do que a sinopse oficial da T3 já diz. Se o redator achar que "morando juntos" entrega o fim da T2, escreva só "o casal volta".
- **Linkar:** `[[leia: estreias-streaming-semana-19-a-25-outubro-2026]]`, `[[leia: como-calcular-tempo-de-maratona]]`.

### 05 · 20h00 · Lista da MIA em texto
- **Título provisório:** Viu o doc da Marília Mendonça? 5 séries sobre sertanejo para continuar nesse mundo
- **Palavra-chave principal:** séries sobre sertanejo
- **Slug:** `series-sobre-sertanejo` · **Categoria:** `o-que-assistir` · **Humor:** `romantico` (CTA `[[app: romantico]]`). Repetir o humor da 04 é permitido (uma `[[app]]` por matéria).
- **Job:** emocional 3.
- **Base:** a Lista do dia (`03-lista-da-mia-series-sertanejas/roteiro.md`), com as mesmas fontes, a mesma ordem (5 → 1) e as mesmas trocas, se alguma série cair na checagem.
  - **Se o vídeo sair:** entram `video_da_peca` e `[[video]]`.
  - **Se a Lista for bloqueada** (sem crédito): a matéria sai sem vídeo e sem dizer "vídeo do dia" (correção do revisor de 16/10).
- ***Marília Mendonça: Sentimento Louco*** entra como seção de abertura: Prime Video, série documental de 4 episódios, todos em 16/10, direção de Susanna Lira (fontes da Lista). Somada às 5 da contagem, a matéria fica com 6 séries.
- **Tom:** respeitoso, sem detalhes do acidente, sem letra de música (título de canção pode aparecer, verso não). Nada de fofoca de família ou de bastidor (anti-ICP).
- **Linkar:** `[[leia: minisseries-e-series-curtas]]`, `[[leia: series-para-quando-voce-esta-triste]]`.

**Checagem do dia (blog):**
- Palavras-chave novas nos 60 dias ✓.
- Nenhuma série é destaque em duas matérias ✓. *Largados e Pelados Brasil* entra na 02 só como parágrafo com link.
- Humores: ansioso (09h), animado (11h), curioso (14h), romântico (17h) e romântico (20h), com uma `[[app]]` por matéria.
- `destaque: true` só na 05 (é a maior tendência brasileira do dia). Se a 05 cair, o destaque vai para a 03.
