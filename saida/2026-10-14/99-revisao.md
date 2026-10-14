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
