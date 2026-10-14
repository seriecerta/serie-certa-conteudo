# Revisão 2026-10-14

## Notas da fase 2 (cena) para o revisor

### Pôsteres com logo de streaming impresso
O logo foi tirado da arte só com recorte. Nenhum pôster recebeu filtro, tarja ou retoque, e as cores são as originais.
- **VisionQuest** (01, Short 9:16): `.capa` de 470×610 com `object-position: top`. O rodapé ("October 14" + logo Disney+) ficou de fora. Continuam visíveis o crédito do estúdio no topo ("from the studio that brought you WandaVision and Agatha", em letra miúda) e o selo Marvel Television, que não é streaming.
- **Inacreditável / Unbelievable** (02, nº 2): recorte de y 562–1370 px num pôster de 1481 px de altura. Ficam de fora "A NETFLIX LIMITED SERIES" (acima do título) e "SEPT 13 | NETFLIX" (rodapé). O que aparece: o título UNBELIEVABLE, a arte e os nomes do elenco. A capa ficou mais larga que 2:3 (600×485, `.serie-card.largo`). O mesmo recorte vale para o mini-pôster do fecho.
- **Olhos que Condenam / When They See Us** (02, nº 1, fecho e thumb): recorte de y 0–1215 px num pôster de 2000 px de altura. "NETFLIX | NOW STREAMING" fica logo abaixo do título e saiu da arte. O que aparece: a frase do topo, "from director Ava DuVernay", o título e a bandeira. Os rostos dos cinco jovens ficaram quase todos fora. A capa tem 600×540, e na thumb 600×540 inclinada.
- **Uma Advogada Extraordinária**: é o pôster coreano, com o logo do canal de TV ENA (não é streaming) e a data de estreia de 2022 em coreano. Ficou inteiro. Se o revisor entender que o ENA conta como logo, o recorte `object-position` precisa subir (o logo está a ~76% da altura, junto ao título coreano).
- Habeas Corpus, Better Call Saul e O Poder e a Lei não têm logo de streaming.

### Nome de streaming na tela
- **01:** a peça não usa legenda automática. "Disney+" aparece só no selo "onde assistir".
- **02:** a legenda automática fica desligada (`data-legenda="off"`) em todo o gancho (0–17,2 s), onde a fala diz "top dez da Netflix" e "Todas na Netflix". Ela só liga na promessa (17,2–27 s) e na tela da régua do fecho, trechos em que a fala não cita streaming. "Netflix" aparece só no selo brasa `.metas .onde` (gancho e cards). A tela do gancho mostra "liderou o top 10…" sem o nome.

### Técnico
- 01: `video.mp4` com 32,5 s, 1080×1920. A capa fica em 7,8 s (quadro "eu JÁ SEI o que vou ver hoje à noite." com 😎). O relógio fica em 12:00 e passa para 12:01 só em "pela primeira vez".
- 02: `video-16x9.mp4` com ~173 s, 1920×1080. A capa fica em 16,5 s (pôster de Habeas Corpus + "5 séries pra você continuar" + selo). Thumb em `thumb/quadros/01.jpg`.
- O nº 2 (Inacreditável) tem tom sóbrio: sem emoji e sem som de impacto além do whoosh de entrada.

---

# Revisão final (revisor, 14/10, ~07h20 BRT)

## Resultado
| Peça | Status | Horário |
|---|---|---|
| 01-short-relogio-visionquest-hoje-a-noite | **aprovada** | YouTube Short 12h00 |
| 02-lista-da-mia-acabou-habeas-corpus | **aprovada** (capítulos corrigidos) | YouTube 13h30 |
| 03-stories-animada-visionquest | **aprovada** (2º CTA removido, telas re-renderizadas) | Instagram Stories 18h30 |
| 04-reels-qual-quarta-e-voce | **bloqueada** | — |

## Fatos (WebSearch em 14/10; WebFetch, netflix.com, justwatch.com e seriecerta.online bloqueados pelo proxy/DNS)
- **VisionQuest / Disney+:** confirmado no Disney+. A data segue divergente: [Omelete](https://www.omelete.com.br/series-tv/vision-quest-wandavision-estreia-adiantada), [CNN Brasil](https://www.cnnbrasil.com.br/pop/streaming/visionquest-nova-serie-da-marvel-estreia-nesta-terca-13-saiba-tudo/) e [Rolling Stone BR](https://rollingstone.com.br/entretenimento/marvel-divulga-titulos-e-cronograma-de-lancamento-dos-episodios-de-visionquest/) dão 13/10 às 22h; [GameOverDrive](https://gameoverdrive.com.br/visionquest-episodios-calendario-quando-termina/) cita o calendário do Disney+ Brasil com eps. 1 e 2 em 14/10. Nos dois cenários, **"hoje à noite já dá pra ver" é verdade** (Short às 12h e Stories às 18h30). "Os dois primeiros episódios saem juntos": consenso. Total de episódios, data do final e hora não são citados (fontes divergem). Mantido.
- **Netflix Brasil, as 5 da Lista:** *Inacreditável* e *Olhos que Condenam* são originais Netflix ([AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000077798/), [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000040687/)). *O Poder e a Lei* é original Netflix; T4 em 05/02/2026, 5ª confirmada como a última ([Omelete](https://www.omelete.com.br/series-tv/o-poder-e-a-lei-5-temporada-confirmada-como-ultima-da-serie), [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000204670/)). *Better Call Saul* e *Uma Advogada Extraordinária* (licenciadas): fonte de 2026 = [Estado de Minas, abr/2026, "4 séries de advogado na Netflix"](https://www.em.com.br/trends/2026/04/7407127-4-series-de-advogado-na-netflix-para-quem-ama-um-bom-drama-de-tribunal.html) (lista *O Poder e a Lei*, *Better Call Saul* e *Uma Advogada Extraordinária*) + [Space Money, 2026](https://www.spacemoney.com.br/cultura-e-entretenimento/better-call-saul-serie-citada-por-diogo-defante-apos-prisao/). Não deu para abrir o catálogo direto (403). Aceito, com a ressalva: se o Bruno tiver o app aberto antes das 13h30, vale bater o olho nessas duas.
- **Nº de episódios/temporadas citados:** Woo 1 temp./16 eps. ✓ (2ª temporada em produção, sem data; o remake japonês de 18/10 é outra série) · BCS 6 temp. ✓ · O Poder e a Lei 4 temp. + 5ª confirmada ✓ · Inacreditável 8 eps. ✓ · Olhos que Condenam 4 eps. ✓ (AdoroCinema e ficha original; o "5" do Canaltech é erro).
- **Tendência:** *Habeas Corpus* nº 1 entre as séries da Netflix no Brasil na semana 28/09–04/10 e 6º no global de língua não inglesa; matérias de "2ª temporada?" até 07–09/10. A fala diz "liderou o top dez", no passado. Não achei o Top 10 de 05–11/10, então nada de "a mais vista agora". Ok.

## Correções feitas
- **02 — capítulos da descrição estavam ~1 s adiantados** (cada marca caía no fim da série anterior; abri os quadros em 00:26, 00:55, 01:19, 01:47, 02:13 e todos mostravam a série anterior). Recalculei pelo `narracao.json` (+0,30 s de entrada) e pelos cortes de cena (`ffmpeg scene`): **00:28 / 00:57 / 01:21 / 01:49 / 02:14 / 02:38**. Conferi os quadros nesses tempos: nº 5, nº 4, nº 3, nº 2, "nº 1" (pausa de suspense) e fecho. Só `publicar.json`; **sem re-render**.
- **03 — dois CTAs na sequência**: tela 1 pedia "responde no direct numa palavra" e tela 4 "testa grátis no link da bio" (regra 6). Tela 1 virou "QUARTA, FIM DE TARDE · como você tá **hoje?**" (pergunta retórica que puxa a tela 2). Único CTA: "Testa grátis no link da bio" (Conversão, tela diária da grade). **Re-renderizei** as 4 telas com `renderizar.py --imagens` e revi a nova 01. `textos.md` atualizado. Não usa ElevenLabs.

## Decisões sobre os pontos pendentes
- **Pôster coreano de Uma Advogada Extraordinária (logo ENA):** **aceito, sem recorte.** ENA é canal de TV coreano, não streaming; a regra proíbe logo de streaming. É o pôster oficial do TVmaze (#62357, 2022), cores originais. A data em coreano é a da estreia de 2022 na TV, não induz a erro sobre o Brasil.
- **Recorte de When They See Us:** **aceito.** O corte tira "NETFLIX | NOW STREAMING", mantém título, frase oficial, crédito de Ava DuVernay e a arte sem retoque. Conferido no card (02:15), no fecho e na thumb: nenhum resquício do logo. O mesmo vale para *Unbelievable* (conferido em zoom: "A NETFLIX LIMITED SERIES" e "SEPT 13 | NETFLIX" fora).
- **Crédito miúdo no pôster de VisionQuest:** **aceito.** "From the studio that brought you WandaVision and Agatha" + selo Marvel Television são do estúdio, não de streaming; o rodapé com Disney+ e "October 14" está fora do quadro (conferido em 17 s).
- **CTA dos Stories:** a API não publica sticker, então fica **"link da bio"**. Slug `humor=animado` **não confirmado** (seriecerta.online bloqueado pelo proxy) → link da bio **sem humor**: `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-14-stories-animada-visionquest`.

## Checagem por peça
- **01:** 1080×1920, 30 fps, 32,5 s, com áudio; `narracao.mp3` 30,4 s. 14 quadros revistos lado a lado com `quarta-21h-reels.jpg`: mesma família (relógio no topo, Inter Black, brasa, emoji grande, recibo, final com botão "MANDA PRA QUEM PRECISA" + @seriecerta). Nada cortado/sobreposto, sem logo de streaming; "Disney+" só no selo. O contador "episódios de uma vez" passa por 0 em ~13 s (animação 0→2), ok. Capa ok. Spoiler zero; "pra quem não é" ok; 1 CTA; UTM no padrão; 1 emoji no `tiktok.txt`. `series: ["VisionQuest"]` completo (WandaVision é só referência, não indicação).
- **02:** 1920×1080, 30 fps, 173 s, com áudio; `narracao.mp3` 170,9 s. 18 quadros + tempos dos capítulos revistos. Identidade ok (verde-noite, Inter Black, `--curioso`, selo brasa "onde assistir", progresso). A tela escura de ~0,5 s antes do "nº 1" é pausa dramática prevista, não tela vazia. Thumb legível em miniatura ("5 / ACABOU ⚖️ HABEAS CORPUS?"). `series` lista as 5 + Habeas Corpus; `posters.json` aponta para os títulos e anos certos (TVmaze). Spoiler zero; tema sensível do nº 2 com aviso, sem cena. 1 CTA ("Salva pra hoje à noite"); o "onde assistir no comentário fixado" é informação. Título com 64 caracteres. UTM no padrão.
- **03:** 4 JPGs 1080×1920; pôster oficial com rodapé cortado; "Disney+" só no selo de texto. 1 CTA. `series: ["VisionQuest"]`.
- **04 (bloqueada):** sem `narracao.mp3`, sem vídeo, sem `publicar.json` (créditos ElevenLabs: 157 de 254). Não revisei fatos de *The Paper* T2 "amanhã" etc.; se for produzida outro dia, reconfirmar tudo (a frase "chega amanhã" vence hoje).

## Técnico
- `publicar.json` das 3 aprovadas: JSON válido, arquivos existem, `quando` em 14/10 com `-03:00`; `validar()` OK nas três (inclui pôsteres).
- `publicar.py --data 2026-10-14 --simular` rodado **em modo local** (`CLAUDE_CODE_REMOTE=false MODO_NUVEM=false`) para não sobrescrever o `revisao.json` com a cópia da nuvem: "publicaria 01/yt-short 12:00" e "02/yt-lista 13:30"; o Stories não aparece porque o horário (18h30) ainda não chegou.

## Pendências
1. **Subir o pacote para a nuvem** (`python scripts/nuvem.py subir-pacote 2026-10-14`) antes das 12h: o ambiente é nuvem (`CLAUDE_CODE_REMOTE=true`), e o pacote tem `revisao.json` novo, `publicar.json` da 02 corrigido e quadros novos da 03.
2. **Bio do Instagram** trocada para o link acima antes das 18h30 (manual, Bruno). Sem a troca, o link continua levando ao site, só perde a atribuição.
3. Slug `humor=animado`: confirmar com o Bruno para os próximos Stories.
4. Peça 04: só com créditos ElevenLabs; refazer a checagem de fatos no dia.

## Revisão da 04 sem narração (14/10, tarde)
**Resultado: 04-reels-qual-quarta-e-voce aprovada** (Instagram Reels, `quando` 2026-10-14T19:00:00-03:00). A peça saiu **sem narração** pela regra "Sem crédito de voz" do `CLAUDE.md` (ElevenLabs sem créditos). A fala que não foi gravada está em `fala-original-sem-uso.txt`, que não é falha de mídia.

### Fatos (WebSearch em 14/10, à tarde)
- ***The Paper*:** a 2ª temporada chega à HBO Max Brasil em **15/10/2026**. O post sai em 14/10, então "a 2ª temporada chega amanhã" está certo. O Peacock não existe no Brasil. O formato de lançamento (semanal ou temporada inteira) não foi confirmado e não é citado. Fontes: [Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil), [GameOverDrive](https://gameoverdrive.com.br/the-paper-2-temporada-estreia-brasil-hbo-max/), [GameOverDrive, HBO Max 12–18/10](https://gameoverdrive.com.br/hbo-max-lancamentos-semana-12-18-outubro-2026/), [Showmetech](https://www.showmetech.com.br/lancamentos-hbo-max-outubro-2026/), [Einerd](https://www.einerd.com/the-paper-spin-off-de-the-office-ganha-data-de-estreia-da-2a-temporada/).
- ***Habeas Corpus*:** está na Netflix desde 23/09/2026 e é drama jurídico. Fontes: [Netflix About](https://about.netflix.com/pt_br/news/habeas-corpus-sop), [O POVO](https://www.opovo.com.br/vidaearte/2026/09/29/habeas-corpus-justica-e-tema-estrutural-diz-marjorie-estiano.html), [Canaltech](https://canaltech.com.br/entretenimento/habeas-corpus-quem-e-quem-na-nova-serie-juridica-brasileira-da-netflix/).
- ***Profundezas* (Below):** minissérie da Netflix com 6 episódios, todos no ar desde 08/10/2026. A premissa é uma criatura marinha atacando uma vila pesqueira. Não há 2ª temporada anunciada. Fontes: [GameOverDrive](https://gameoverdrive.com.br/profundezas-episodios-duracao/), [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000217242/), [Omelete](https://www.omelete.com.br/series-tv/profundezas-netflix-josh-hartnett-trailer-completo).
- ***Coven Academy*:** está no Disney+ Brasil desde 02/10/2026 com a **temporada inteira**. Fontes: [Showmetech](https://www.showmetech.com.br/lancamentos-do-disney-plus-em-outubro-de-2026/), [Gazeta SP](https://www.gazetasp.com.br/entretenimento/nova-serie-da-disney-acompanha-adolescentes-bruxas-em-academia-cercada-por-misterios-e-forcas-sombrias/), [Salada de Cinema](https://saladadecinema.com.br/coven-academy-supera-american-horror-story-no-ranking-do-disney/). O número de episódios não é citado na peça.
- O texto na tela não precisou de correção.

### Visual (quadros revistos a cada 2 s, comparados com `referencias/quadros/qual-e-voce-4-tipos.jpg`)
- Segue o padrão do formato: cabeçalho "QUAL QUARTA É VOCÊ?" com 4 tracinhos que acendem, número grande com tipo e superpoder, emoji no canto, gag visual e grade final 2×2. Também segue a identidade: verde-noite, Inter Black, brasa, botão "MANDA PRA QUEM PRECISA" e @seriecerta.
- O gancho escrito já está no quadro 1 ("pra amiga que é a Nº 3 toda quarta"). Não há texto cortado, sobreposição nem tela vazia, e não encontrei erro de digitação.
- Tempo de leitura: cada série fica 4,4 s na tela (pôster, onde assistir e chips). A linha "pra quem não é" aparece por 2,4 s, mas tem só 4 ou 5 palavras e é legível. As gags ficam 2,4 a 3 s.
- **Logos:** conferi em zoom 1:1. *The Paper* começa no título "the paper" e não sobrou nada do "peacock ORIGINAL". *Coven Academy* começa no título e não sobrou nada do logo "Disney". Os rodapés dos 4 pôsteres estão limpos. Os nomes dos streamings aparecem só no selo de texto "onde assistir".
- **Pôsteres:** os 4 são oficiais do TVmaze e o `posters.json` bate com o roteiro: The Paper #84611 (2025), Habeas Corpus #93677 (2026), Below #93115 (2026, que é *Profundezas*) e Coven Academy #83159 (2026).
- Capa `capa.jpg` (1080×1920): é a grade final com o nº 3 destacado e o botão. Fica legível em tamanho pequeno.

### Regras e técnico
- Spoiler zero, porque só aparecem as premissas oficiais. Não há diálogo nem letra de música. Cada série tem seu "pra quem não é".
- Há 1 CTA ("Manda pra quem precisa", Descoberta). "Achou a sua?" é retórico.
- A legenda tem 208 caracteres, 1 emoji e 4 hashtags. O `tiktok.txt` também tem 1 emoji. Não há link na peça, então não há UTM a conferir.
- `series` tem as 4 séries indicadas, o que está completo.
- `video.mp4` tem 1080×1920 e 40,6 s, com áudio (trilha e efeitos) a −13,9 LUFS, medidos com ebur128. O `publicar.json` é um JSON válido e o `validar()` deu **OK**. Não rodei `publicar.py` nem `nuvem.py`, como foi pedido.

### Correções
- `roteiro.md`: a nota do topo dizia "capa em 32,8 s". O valor real é `data-capa="38.40"`, a grade final com o botão, e a nota foi corrigida. Não houve re-render.

### Observação (não bloqueia)
- O horário de 19h00 segue a pauta de hoje, mas a grade de `08-cronograma.md` põe o Reels da noite às 18h30 (19h00 é o horário do Short). Mantive o que a pauta definiu. Se o período de base exigir a grade exata, quem decide trocar para 18h30 é o estrategista ou o Bruno.
- **Pendência:** subir o pacote para a nuvem (`python scripts/nuvem.py subir-pacote 2026-10-14`) antes das 19h, porque o `revisao.json` mudou.
