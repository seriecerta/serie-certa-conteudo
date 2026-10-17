# Revisão — sábado, 2026-10-17

## 1ª rodada (peças das 10h00), revisada às 09h50–09h57

### Aprovadas
- `01-carrossel-acabou-a-leste-do-eden` (IG carrossel, 10h00)
- `02-stories-acabou-a-leste-do-eden` (IG Stories, 10h00)

### Fatos reconferidos na web hoje (WebSearch; JustWatch, Omelete e Netflix seguem com ENOTFOUND no WebFetch)
- **A Leste do Éden**: minissérie Netflix, 7 episódios, todos em 01/10/2026 ([Canaltech](https://canaltech.com.br/entretenimento/a-leste-do-eden-nova-serie-com-florence-pugh-e-grande-aposta-da-netflix-conheca/); [Einerd](https://www.einerd.com/a-leste-do-eden-minisserie-com-florence-pugh-ja-esta-na-netflix/)). A arte não afirma número nenhum dela.
- **Ripley**: original Netflix, minissérie de 8 episódios em preto e branco, com Andrew Scott ([Netflix About](https://about.netflix.com/news/ripley-starring-andrew-scott-to-premiere-on-netflix); [AdoroCinema](https://www.adorocinema.com/noticias/series/noticia-1000128582/); [PinkNews, 18/03/2026](https://www.thepinknews.com/2026/03/18/andrew-scott-shuts-down-fan-hopes-of-second-season-of-his-spellbinding-netflix-thriller)). Confirmado.
- **Pachinko**: original Apple, no Apple TV. A T3 não foi anunciada ([TVLine](https://tvline.com/news/pachinko-season-3-status-cancelled-renewed-1235474462)). A arte não cita temporadas. Confirmado.
- **Peaky Blinders**: série completa (6 temporadas) na Netflix Brasil, segundo matérias da estreia do filme *O Homem Imortal* em 20/03/2026 ([Rolling Stone Brasil](https://rollingstone.com.br/cinema/peaky-blinders-o-homem-imortal-estreia-na-netflix/); [O Povo, 20/03/2026](https://www.opovo.com.br/vidaearte/2026/03/20/amp/netflix-prime-video-e-hbo-as-estreias-da-semana-16-03-a-22-03.html)). Não achei notícia de saída do catálogo. A arte diz só "Netflix", sem número de temporadas. **Ressalva:** a fonte mais recente é de mar/2026, porque o JustWatch BR está bloqueado. Aceitei porque a Netflix coproduz o filme e a sequência. Se o Bruno puder, vale conferir no app.
- **Succession** já tinha saído do carrossel no desdobramento (sem fonte de 2026 para o HBO Max BR). Ela não aparece em arte, legenda nem `series`.

### Correções feitas
- Carrossel card 3 e Stories tela 2: o rótulo "sem confiar **nela**" ficava em cima do pôster do Tom Ripley e parecia erro. Troquei por "sem confiar **nele**".
- Stories tela 1: "desliza →" virou "toca pra ver →", porque Stories se passa tocando.
- Re-renderizei os dois (`--imagens --formato 4x5` e `--imagens`) e o `validar()` deu OK nos dois.

### Checklist
- Spoiler: nenhum. De A Leste do Éden aparece só a premissa e o pôster oficial.
- Voz: dentro de `06-voz-mia.md`, com "pra quem não é" em todas as séries.
- CTA: o carrossel tem um só ("Salva pra hoje à noite", Consideração). Os Stories também têm um só ("testa grátis no link da bio", Conversão).
- Legenda do carrossel: 198 caracteres e 1 emoji.
- `series` completo nos dois, com 4 séries cada. Os pôsteres do TVmaze batem (East of Eden 2026 #79399, Ripley 2024 #44042, Pachinko #41375, Peaky Blinders #269).
- Olhei todos os quadros (7 + 5): nenhum logo de streaming (o topo do pôster do Pachinko com "Apple TV+" fica fora do recorte), nenhum texto cortado e nenhuma sobreposição.
- O link da bio dos Stories usa `utm_medium=stories` com `utm_campaign`, o mesmo padrão aprovado em 16/10.
- `quando` está em `2026-10-17T10:00:00-03:00` nos dois.

### Fora desta rodada
- Vídeos 03–05 e blog: ficam para a rodada final e estão fora do `revisao.json` por enquanto.

## Rodada final (vídeos 03–05 e blog), revisada às 07h00

### Vídeos bloqueados
- `03-lista-da-mia-mike-flanagan`, `04-short-reels-selvagens-ep03-sabado`, `05-reels-short-casal-sabado-escolhe-voce`: não têm narração, vídeo nem `publicar.json`. A ElevenLabs recusou já a 1ª fala (`quota_exceeded`: 29 créditos, 34 necessários). Os roteiros ficam prontos para quando o Bruno recarregar.

### Blog: as 5 aprovadas
Fatos reconferidos hoje pela API GraphQL do JustWatch BR (ofertas `FLATRATE`, temporadas e episódios), pela página da Netflix BR (curl com UA Googlebot), pela API do TVmaze (durações) e por WebSearch. Para conferir se o texto é original, busquei 5 frases entre aspas e nenhuma apareceu em outro site. As 5 passam no `--verificar`.

- **01 · triste (09h).** As 6 séries conferem no JustWatch (5 na Netflix, Fleabag no Prime). Temporadas e episódios batem.
  - Corrigi *Pousando no Amor*: o texto dizia que os episódios "passam de uma hora e meia", mas a média é de 85 min.
  - Tirei "na reta final, por doença" de *Disque Amiga para Matar*, porque é um ponto de trama da 3ª temporada (spoiler).
  - **O CVV (188) fica.** É uma linha de cuidado, não é CTA, e segue a boa prática de falar de tristeza sem romantizar.
  - Na capa, o "ONLY ON NETFLIX" do pôster de *Dead to Me* aparece pela metade. Todos os pôsteres oficiais candidatos têm logo impresso (Fleabag, Atypical, Eu Nunca...). Aceitei pela regra do `11-blog.md`: o pôster não é editado, e a regra vale para o que a gente desenha.
- **02 · estreias de 19 a 25/10 (11h).**
  - **Georgie e Mandy T3 saiu.** Não achei confirmação na HBO Max BR; o JustWatch BR não mostra oferta para a T3. Ajustei a contagem para 4 estreias em 2 streamings (subtítulo, resumo, abertura, "como escolher", `series`, `fontes`, pôster).
  - *Ninguém Quer* sai em 22/10, data da Netflix Brasil (Omelete, Critical Hits).
  - *Lupin* P4 sai em 23/10 com 8 episódios. *Cyberpunk* T2 sai em 20/10 com 10. *A Lista Terminal* T2 sai em 21/10 com 8, todos de uma vez.
  - Tirei "classificação 16 anos" de *A Lista Terminal*, porque o JustWatch BR diz 18.
  - Acrescentei o "por que combina" que faltava em *Lupin*.
- **03 · parecidas com A Leste do Éden (14h).**
  - **Succession fica.** O JustWatch BR mostra hoje a série no HBO Max (e no canal HBO Max do Prime). A Oficina da Net a lista no catálogo em abr/2026. As 4 temporadas e os 39 episódios conferem.
  - Tirei a classificação "16 anos" de *Objetos Cortantes* (o JustWatch diz 18).
  - O aviso de autolesão e abuso fica como está: o tom é direto e acolhedor, sem detalhe de cena.
  - Durações e episódios de todas conferidos no TVmaze.
- **04 · Slow Horses (17h).**
  - JustWatch: 6 temporadas de 6 episódios, eps. 1–5 da T6 no ar e o último em 21/10.
  - Somei de novo os tempos do TVmaze e a tabela bate.
  - Corrigi a contradição "exclusiva do Apple TV" × "canal no Prime". A série está nos dois, e o JustWatch confirma o canal Apple TV no Prime.
  - Acrescentei que, no horário de Brasília, os episódios têm aparecido já na noite de terça.
- **05 · Mike Flanagan (20h).**
  - **A premissa de O Clube da Meia-Noite foi confirmada** pela sinopse da Netflix BR ("clínica para adolescentes em estado terminal", "clube secreto") e pelo AdoroCinema (encontros à meia-noite para contar histórias, livro de Christopher Pike). Reescrevi a frase com essa base.
  - Corrigi "Flanagan é o criador e o diretor" para "criou e dirige parte dos episódios".
  - Troquei "ambientada nos dias de hoje" (sem fonte) por "versão atualizada".
  - **Tirei o `[[video]]` e o `video_da_peca`**, porque a Lista 03 está bloqueada. Nada no texto promete vídeo.
  - As 5 séries estão na Netflix BR e *Carrie* no Prime (JustWatch). Os tempos batem com o TVmaze.
- **Pôsteres:** os `posters.json` batem com nome e ano de todas as séries indicadas. Nenhuma capa tem texto cortado. Os logos que aparecem vêm impressos nos pôsteres oficiais.
- **Observação de SEO, sem bloquear:** nas matérias 02, 03 e 04 a palavra-chave aparece no título em variação ("Acabou A Leste do Éden? 5 séries parecidas", "quantas temporadas"). A forma exata está no `seo_titulo` e na meta.
- **Simulação:** às 07h03 o `publicar_blog.py --data 2026-10-17 --simular` não acusou nada, porque todas as matérias ainda estão no futuro. A validação equivalente (`--verificar`) passou nas 5.
