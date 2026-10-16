# Revisão 2026-10-16

## 1ª rodada (revisor, manhã): peças das 10h00

| Peça | Status | Horário |
|---|---|---|
| 01-carrossel-minisseries-pro-fim-de-semana | **aprovada**, com 1 ajuste de texto, comentário fixado refeito e re-render | Instagram Carrossel 10h00 |
| 02-stories-minisseries-pro-fim-de-semana | **aprovada**, com a tela de CTA reescrita e re-render | Instagram Stories 10h00 |
| 03 a 05 (vídeos) | em produção. Ficam fora do `revisao.json` até a 2ª rodada | — |

### Fatos: onde assistir no Brasil (WebSearch em 16/10)
WebFetch e curl caíram em DNS/proxy para justwatch.com, netflix.com, adorocinema.com e soumaispop.com.br. Por isso a checagem foi feita por WebSearch. As 4 séries são **originais da própria plataforma** em que aparecem, e nenhuma fonte aponta saída do catálogo.
- ***A Leste do Éden* (East of Eden, 2026) · Netflix · 7 episódios, todos lançados em 01/10/2026**, com Florence Pugh e criação de Zoe Kazan. Fontes: [Einerd](https://www.einerd.com/a-leste-do-eden-minisserie-com-florence-pugh-ja-esta-na-netflix/), [GameOverDrive](https://gameoverdrive.com.br/a-leste-do-eden-netflix-estreia-horario-episodios-elenco/), [Canaltech](https://canaltech.com.br/entretenimento/a-leste-do-eden-nova-serie-com-florence-pugh-e-grande-aposta-da-netflix-conheca/). ✓
- ***O Gambito da Rainha* · Netflix · minissérie de 7 episódios.** A página da Netflix Brasil ([netflix.com/br/title/80234304](https://www.netflix.com/br/title/80234304)) está indexada com sinopse, elenco e classificação 16. Em fev/2026 a imprensa confirmou que não haverá T2 ([Comentei!](https://comentei.com.br/entretenimento/2026/02/20/a-serie-que-todo-mundo-ama-na-netflix-nao-tera-nova-temporada/)). Original Netflix. ✓
- ***Mare of Easttown* · HBO Max · minissérie de 7 episódios.** A página da HBO Max **Brasil** ([hbomax.com/br/pt/shows/mare-of-easttown](https://www.hbomax.com/br/pt/shows/mare-of-easttown/c1517b80-50ab-4733-8208-ae2c2765c0e7)) está indexada com "1 temporada (7 episódios)". Também aparece no [AdoroCinema](https://www.adorocinema.com/series/serie-24693/) e no [Sitio Andino, 06/08/2026](https://www.sitioandino.com.ar/muchoshow/es-una-las-mejores-miniseries-los-ultimos-tiempos-y-esta-hbo-max-n5660237). A T2 ainda não foi filmada ([Deadline, jan/2026](https://deadline.com/2026/01/kate-winslet-season-2-mare-of-easttown-2027-1236676083/)), então "minissérie de 7 episódios" segue correto. Original HBO. ✓
- ***Chernobyl* · HBO Max · minissérie de 5 episódios.** Aparece no ranking da HBO Max no Brasil em 2026, puxada por *Emergência Radioativa* ([Mais Goiás](https://www.maisgoias.com.br/entretenimento/series/minisserie-de-2019-volta-ao-topo-das-mais-assistidas-apos-buscas-por-cesio-137-em-goiania/); [Omelete, mar/2026](https://www.omelete.com.br/filmes/emergencia-radioativa-filmes-series-desastres-nucleares-streaming)). Os 5 episódios estão no próprio pôster ("A 5-part miniseries"). Original HBO. ✓
- **Ressalva:** catálogo "de hoje" foi confirmado por página oficial indexada e imprensa de 2026, não por acesso direto ao app. Como são 4 originais na plataforma de origem, aprovei. Se a nuvem liberar JustWatch, reconfirmar nas próximas.

### Correções
- **01, card 5 (Chernobyl):** "pra quem não é: quem quer desligar a cabeça: é pesada" tinha dois-pontos duplos. Virou "quem quer desligar a cabeça (é pesada)".
- **01, `comentario-fixado.txt`:** tinha uma pergunta ("Qual dessas você começa hoje?") junto com o CTA e o link. Isso dava dois pedidos, e link em comentário não é clicável. Agora traz só onde assistir cada série, sem pedido, como em 15/10.
- **02, tela 5 (CTA):** "vai ver a dois? 💑" + "a MIA acha a sua pelo seu humor" misturava o modo casal com um texto individual. Também não deu para confirmar que o link da bio leva ao modo casal. Usei o padrão da pauta: 🌙 "qual é a **sua** hoje?" + "a MIA escolhe pelo seu humor." + botão "TESTA GRÁTIS NO LINK DA BIO" + @seriecerta. É um CTA só, de Conversão. `textos.md` atualizado.
- Re-render: `renderizar.py --imagens --formato 4x5` (01, 7 JPGs 1080×1350) e `--imagens` (02, 5 JPGs 1080×1920). Revi todos os quadros depois.

### Checagem visual
- Fundo verde-noite, Inter Black, brasa, emoji grande, botão final + @seriecerta: ✓ nas duas peças.
- **Logos de streaming:** nenhum aparece. O recorte quadrado deixa de fora o rodapé dos pôsteres de *Mare* e *Chernobyl* e qualquer marca da Netflix em *Gambito* e *Leste do Éden*. O nome do streaming só aparece em texto.
- Não há texto cortado, sobreposição nem tela vazia. No pôster de *Chernobyl*, o recorte mostra a metade de cima, com o título inteiro.
- **Pôsteres:** o `posters.json` aponta para East of Eden (#79399, estreia 2026-10-01, não o filme de 1955), The Queen's Gambit (#41428, 2020), Mare of Easttown (#40546, 2021) e Chernobyl (#30770, 2019). Nomes e anos batem.

### Spoiler, voz e CTA
- Spoiler zero. *Gambito* fala de "vício" e *Mare* de "luto", mas os dois temas estão na premissa e na sinopse oficial. Nada de reviravolta ou final.
- A voz está no tom da MIA: frases curtas, humor por card e "pra quem não é" em todas as séries.
- 01: um CTA, "Salva pra hoje à noite" (Consideração). A legenda tem 226 caracteres e 1 emoji. 02: um CTA, "Testa grátis no link da bio" (Conversão).
- **UTM do link da bio (Stories):** `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-16-stories-minisseries-fim-de-semana`. Vai sem `humor=` porque são vários humores. É o mesmo padrão aprovado em 14 e 15/10.

### Técnico
- `publicar.json`: JSON válido, arquivos existem, `quando` = `2026-10-16T10:00:00-03:00`. O `series` está completo: 4 séries no 01 e 3 no 02 (*Chernobyl* fica fora dos Stories, tanto da arte quanto da lista). `validar()` deu **OK** nas duas.
- `publicar.py --data 2026-10-16 --simular` foi rodado em modo local (`CLAUDE_CODE_REMOTE=false MODO_NUVEM=false`) e não deu saída nem erro.
- **Pendente antes das 10h00:** `python scripts/nuvem.py subir-pacote 2026-10-16`. Sem isso, a nuvem publica a versão sem as correções. Também falta trocar o link da bio para a UTM acima.

## Peças de vídeo (03, 04, 05): bloqueadas
Sem narração: a ElevenLabs recusou a primeira fala (`quota_exceeded`, 29 créditos restantes, 34 necessários). Nenhum `.mp3` foi gerado. Roteiros, narrações (.txt) e pôsteres ficam prontos para quando houver recarga. Slots não cumpridos hoje: Lista 12h00, Short+Reels 13h30, Reels 18h30, Short 19h00 (inclui o vídeo do casal da sexta).
