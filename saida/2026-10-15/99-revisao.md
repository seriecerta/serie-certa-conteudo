# Revisão 2026-10-15

## 1ª rodada (revisor, ~06h50 BRT): peças das 10h00

| Peça | Status | Horário |
|---|---|---|
| 01-carrossel-quinta-de-estreia-por-humor | **aprovada**, com o card 5 (Sentimento Louco) trocado e re-render | Instagram Carrossel 10h00 |
| 02-stories-quinta-de-estreia | **aprovada**, com ajuste de texto e re-render | Instagram Stories 10h00 |
| 03 a 06 (vídeos) | ainda em produção. Ficam fora do `revisao.json` até a 2ª rodada | — |

### Fatos (WebSearch em 15/10; WebFetch caiu em DNS para showmetech.com.br e gameoverdrive.com.br)
- **The Paper T2 / HBO Max:** a estreia no Brasil em 15/10 aparece em várias fontes: [Omelete](https://www.omelete.com.br/series-tv/the-paper-2a-temporada-spin-off-the-office-data-estreia-brasil), [GameOverDrive](https://gameoverdrive.com.br/the-paper-2-temporada-estreia-brasil-hbo-max/), [Upnerd, que cita o site da HBO Max](https://www.upnerd.com.br/2026/09/the-paper-2-temporada-ganha-data-de.html) e [semana 12–18/10](https://gameoverdrive.com.br/hbo-max-lancamentos-semana-12-18-outubro-2026/). No TVmaze, a T2 saiu no Peacock (EUA) em 09/09, com 10 episódios de uma vez. A lista da [Showmetech](https://www.showmetech.com.br/lancamentos-hbo-max-outubro-2026/) que fala em "fim de temporada" não abriu, e a busca não confirma essa versão. Também não está confirmado se no Brasil sai inteira ou semanal. **Por isso a arte só diz "Leve, no HBO Max"**, sem número de episódios, sem formato de lançamento e sem "estreia hoje". A afirmação é verdadeira em qualquer cenário. Mantido.
- **A Diplomata T4 / Netflix:** sai em 15/10, com 8 episódios de uma vez ([Omelete](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data), [GameOverDrive](https://gameoverdrive.com.br/a-diplomata-4-temporada-quantos-episodios/)). O TVmaze confirma: T4 com estreia em 2026-10-15 e 8 episódios. A arte não cita hora. "Na Netflix desde hoje" ✓.
- **Carrie, a Estranha / Prime Video:** 8 episódios, todos em 07/10, com Mike Flanagan como showrunner ([GameOverDrive](https://gameoverdrive.com.br/carrie-serie-mike-flanagan-estreia-prime-video/), [TecMundo](https://www.tecmundo.com.br/minha-serie/604301-carrie-nova-adaptacao-do-prime-video-ganha-trailer-e-data-de-estreia.htm)). No TVmaze, #45562 tem Prime Video e 8 episódios em 2026-10-07. ✓
- **Marília Mendonça: Sentimento Louco / Prime Video:** série documental de 4 episódios. **Chega só amanhã, 16/10** ([GameOverDrive](https://gameoverdrive.com.br/marilia-mendonca-sentimento-louco-episodios/), [Omelete](https://www.omelete.com.br/series-tv/marilia-mendonca-sentimento-louco-documentario-critica)). O card dizia "No Prime Video" sem a data, num carrossel que fecha com "salva pra hoje à noite". Isso estava **errado hoje** (ver abaixo).

### Decisão sobre o card 5 (Sentimento Louco, `.capa.gerada`)
**O card saiu do carrossel.** Os motivos:
1. **Contorno da trava.** A série era indicada na arte e na legenda, mas o desdobrador tirou o nome dela do `"series"` do `publicar.json`. Com isso, a trava do pôster oficial (regra 3) deixava de pegar o card. Não aceito tirar a série da lista para a peça passar.
2. **Fato errado para hoje.** A série só estreia em 16/10, e o CTA da peça é "salva pra hoje à noite".
3. **Tom.** Uma tela de "saudade" com a Marília no meio de um carrossel de estreias leves pede um cuidado que uma capa gerada não dá.

O pôster não existe no TVmaze: a busca por "Sentimento Louco" e "Marília Mendonça" voltou vazia. Se ela entrar outro dia, que seja numa peça própria e com tom respeitoso. Pela regra, a capa gerada pode entrar, mas com a série no `"series"` e registro neste arquivo.

**Substituto** para manter os 7 cards: o card 5 virou **"o mapa da quinta"**, um cupom/recibo do motor (formato que já está no ar). Ele lista humor → série → streaming das 3 séries com pôster: The Paper · HBO Max, A Diplomata · Netflix, Carrie · Prime Video. O card não indica série nova e serve ao "salvar".

### Outras correções
- **01, card 1 e card 7:** "4 séries" virou "3 séries novas" e "quatro estreias" virou "três séries novas". *Carrie* é de 07/10, então "estreia" não valia para ela.
- **01 e 02, card *The Paper*:** "pra quem não é: quem quer The Office igualzinho, ~~o elenco é outro~~". Cortei o fim porque o Oscar Nuñez volta no spin-off, então o elenco não é todo outro.
- **01 e 02, pôster de *Carrie*:** o `object-position` passou de 50% 40% para 50% 75%. O título "CARRIE" do pôster aparecia cortado pela metade. Agora está inteiro e a tiara continua na arte.
- **01, legenda:** saiu a linha da Marília. A legenda ficou com 275 caracteres, 1 emoji e 1 CTA ("Salva pra hoje à noite").
- **01, `comentario-fixado.txt`:** tinha um 2º CTA, de outro estágio do funil ("Testa a MIA grátis: link"), num carrossel de Consideração. Agora traz só onde assistir cada série, sem pedido.
- Re-render: `renderizar.py --imagens --formato 4x5` (01, 7 JPGs 1080×1350) e `--imagens` (02, 5 JPGs 1080×1920). Revi todos os quadros.

### Checagem visual
- Fundo verde-noite, Inter Black, brasa, emoji grande, botão final + @seriecerta: ✓ nas duas peças.
- **Logos de streaming:** o "peacock ORIGINAL" (topo do pôster de *The Paper*) e o "ONLY ON NETFLIX | OCTOBER 15" (rodapé de *The Diplomat*) ficam fora do recorte, conferidos em zoom. *Carrie* não tem logo. O nome do streaming aparece só em texto.
- Nada de texto cortado, sobreposto ou tela vazia. As letras do título "the paper" encostam na borda superior da capa, mas estão legíveis. Esse é o preço de esconder o logo do Peacock.
- Pôsteres: `posters.json` aponta para The Paper (#84611, 2025), The Diplomat (#60213, 2023) e Carrie (#45562, 2026, não o filme). Nomes e anos batem.

### Spoiler, voz e CTA
- Spoiler zero. Nada do final da T3 de *A Diplomata*, e *Carrie* aparece só como gênero.
- A voz está no tom da MIA: frases curtas, opinião segura e "pra quem não é" em cada série.
- 01: um CTA ("salva pra hoje à noite", Consideração). 02: um CTA ("testa grátis no link da bio", Conversão). A tela 1 tem uma pergunta retórica, sem pedir resposta.
- UTM do Stories (link da bio): `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-15-stories-quinta-de-estreia`. Vai sem `humor=` porque nenhum slug está confirmado e são vários humores. Segue o mesmo padrão aprovado em 14/10.

### Técnico
- `publicar.json`: JSON válido, todos os arquivos existem, `quando` = `2026-10-15T10:00:00-03:00`, `series` completo (as 3 séries indicadas). `validar()` deu **OK** nas duas.
- `publicar.py --data 2026-10-15 --simular`, rodado em modo local (`CLAUDE_CODE_REMOTE=false MODO_NUVEM=false`): sem saída. O Instagram com `quando` no futuro é pulado antes de validar (APRENDIZADOS 13/10), por isso conferi direto pelo `validar()`.
- **Pendente antes das 10h00:** subir o pacote corrigido com `python scripts/nuvem.py subir-pacote 2026-10-15`. Sem isso, o publicador da nuvem baixa a versão antiga, que ainda tem o card da Marília e o `revisao.json` sem as aprovações. Também falta trocar o link da bio para a UTM acima.

## 2ª rodada (revisor, 15/10 manhã): vídeos

| Peça | Status | Horário |
|---|---|---|
| 01 e 02 | **aprovadas na 1ª rodada**, mantidas sem reabrir | 10h00 |
| 04-short-reels-relogio-a-diplomata-voltou | **aprovada**, sem correção e sem re-render | YouTube Short + Instagram Reels 13h30 |
| 03-lista-da-mia-terror-de-cidade-pequena | **bloqueada**: sem narração, vídeo e `publicar.json` | 12h00 não cumprido |
| 05-reels-selvagens-do-sofa-ep03-quinta-de-estreia | **bloqueada**: sem narração, vídeo e `publicar.json` | 18h30 não cumprido |
| 06-short-tradutor-o-que-a-mia-entende | **bloqueada**: sem narração, vídeo e `publicar.json` | 19h00 não cumprido |

### 04: o que foi conferido
- **Fatos (WebSearch, 15/10):** A Diplomata T4 na Netflix desde 15/10, com os 8 episódios de uma vez, e sem anúncio de parte 2 ([Omelete](https://www.omelete.com.br/series-tv/a-diplomata-netflix-4a-temporada-primeiro-trailer-data), [GameOverDrive: 8 episódios](https://gameoverdrive.com.br/a-diplomata-4-temporada-quantos-episodios/), [GameOverDrive: estreia nesta quinta](https://gameoverdrive.com.br/a-diplomata-4-temporada-horario-estreia-netflix/)). As fontes não divergem. A previsão de liberação é por volta das 4h, então o título já está no ar às 13h30. A peça não cita horário nem duração. ✓
- **Spoiler:** zero. Nada da T3 nem da trama da T4 aparece na fala, na arte, na legenda ou na descrição. ✓
- **Voz:** frases curtas, gancho de envio ("pra amiga que tá contando os dias"), opinião segura e "pra quem não é" (quem nunca viu as outras, começa pela 1ª). O texto do `narracao.json` (timings do mp3) bate com o `narracao.txt`. ✓
- **CTA:** um só, de Descoberta: "Manda pra quem precisa", falado e no botão. A linha "manda pra amiga que contou os dias" acima do botão é o mesmo pedido. Não tem "segue", "comenta" nem "parte 2". ✓
- **UTM (descrição do YouTube):** `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=2026-10-15-short-relogio-a-diplomata-voltou`, no padrão do `05`. A legenda do Instagram vai sem link. ✓
- **publicar.json:** JSON válido. `validar()` deu **OK** nas duas publicações (yt-short e ig-reel). `quando` = `2026-10-15T13:30:00-03:00`. Legenda do IG com 245 caracteres e descrição do YT com 427. `series` = ["The Diplomat (2023)"], a única série indicada. ✓
- **Pôster:** `posters.json` → The Diplomat, TVmaze #60213, estreia 2023. É o pôster da T4, com cores originais. ✓
- **Mídia:** `video.mp4` tem 1080×1920 e 24,2 s, com áudio. `narracao.mp3` tem 22,3 s. `capa.jpg` tem 1080×1920. ✓
- **Visual:** conferi a folha de 6 quadros, uma folha de 2 quadros/s (48 quadros) e a capa, comparando com `referencias/quadros/quarta-21h-reels.jpg`. Está tudo no padrão: relógio no topo, fundo verde-noite, Inter Black, carimbos brasa, emoji grande e botão final com @seriecerta. O "ONLY ON NETFLIX | OCTOBER 15" do rodapé do pôster fica fora do recorte (`object-position: top`) na cena e na capa, e o nome Netflix aparece só no selo em texto. Não achei texto cortado, sobreposição nem palavra errada. As telas parcialmente vazias aparecem só durante a entrada das animações. A capa (contador "8" + "DE UMA VEZ." + pôster) fica legível em tamanho pequeno.
- **Observação, sem bloqueio:** a 2ª linha do gancho ("PRA A DIPLOMATA VOLTAR") entra por volta de 2,5 s, sincronizada com a fala. A 1ª linha está na tela desde o quadro 0.

### Simulação
- `CLAUDE_CODE_REMOTE=false MODO_NUVEM=false python3 -B scripts/publicar.py --data 2026-10-15 --simular`: sem saída, código 0. O Instagram com `quando` no futuro é pulado antes de validar (APRENDIZADOS 13/10), por isso conferi direto pelo `validar()`.

### Pendências do Bruno
1. **Créditos ElevenLabs esgotados:** sobraram 29 créditos, e só a Lista pedia 664. Por isso 03, 05 e 06 não têm narração nem vídeo e ficam bloqueadas. Hoje três slots não são cumpridos (Lista 12h00, Reels 18h30, Short 19h00), em pleno período de base. **É preciso recarregar o plano** antes da rotina de amanhã, ou o mesmo vai acontecer. Ontem o Reels "Qual quarta é você?" também caiu por crédito. A regra proíbe outra voz ou outro TTS.
2. **Subir o pacote** com `python scripts/nuvem.py subir-pacote 2026-10-15` antes das 13h30, para o publicador da nuvem receber o `revisao.json` com a 04 aprovada. O pendente da 1ª rodada (subir antes das 10h00 e trocar o link da bio) continua valendo se ainda não foi feito.
