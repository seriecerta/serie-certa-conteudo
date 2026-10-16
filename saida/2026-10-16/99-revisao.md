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

## Blog
Revisão das 5 matérias de `blog/` (16/10). JustWatch, Netflix e AdoroCinema não abriram (proxy/DNS), então tudo foi conferido por WebSearch hoje. O `--verificar` passou nas 5, sem erro.

### Aprovadas (5)
- **01 · séries leves para relaxar (17h00).** Ted Lasso T4 (05/08 a 07/10, 10 episódios), Shrinking T3 (11 episódios, 28/01 a 08/04), Only Murders no Disney+ (5 temporadas; a 6ª chega em 08/12 e não foi citada), Heartstopper (3 temporadas + filme de 17/07 na Netflix), Emily em Paris (5 temporadas; a 6ª ainda não estreou, sai em 24/12) e Hacks no HBO Max (5ª e última temporada abr–mai/2026): tudo confirmado. Correção: a palavra-chave entrou no 1º parágrafo e num `##`.
- **02 · estreias da semana (18h00).** Armadilha (Netflix 13/10, 6 episódios, livro de Melanie Raabe), VisionQuest (Disney+ 13/10 às 22h de Brasília, 2 episódios, 8 no total; a matéria não cita a data do final porque as fontes divergem), A Diplomata T4 (Netflix 15/10, 8 episódios), Tulsa King T4 (Paramount+ 16/10, semanal), Crystal Lake (Universal+ 16/10, 8 de uma vez; Peacock nos EUA em 15/10) e Largados e Pelados Brasil T4 (HBO Max/Discovery 18/10, 7 episódios, 2 na estreia): tudo confirmado. Correção: entrou uma fonte com o calendário de VisionQuest.
- **03 · parecidas com Profundezas (19h00).** **Tirei 1899**: não achei nenhuma fonte de 2025 ou 2026 que confirme a série na Netflix BR (só matérias de 2022–2023). Ficam 5 indicações (Mistério no Mar/Prime, Origem/Globoplay T4 completa, Dark/Netflix, Residência Hill/Netflix, Yellowjackets/Paramount+ com a T4 em 20/11 no plano premium). Mudaram junto: título, SEO, resumo, meta e "seis" → "cinco". Saíram o pôster e a fonte de 1899. **Capa refeita**: o leque agora é Residência Hill + Profundezas + Dark. Testei Mistério no Mar e descartei, porque o pôster traz o logo do Prime Video e "New season". O `capa_alt` foi atualizado. Entrou uma fonte de abr/2026 para Dark na Netflix. A palavra-chave foi para o 1º parágrafo e para um `##`.
- **04 · guia Lupin parte 4 (20h00).** A estreia em 23/10, com 8 episódios de uma vez, e as partes 1–3 na Netflix BR estão confirmadas (Einerd e página da Netflix BR indexada com 3 partes). A página da Netflix BR entrou nas fontes. A capa usa o pôster oficial da parte 4, que traz "Only on Netflix" impresso: entra assim mesmo, pela regra nova do `11-blog.md`. A palavra-chave foi para o 1º parágrafo.
- **05 · parecidas com A Diplomata (21h00).** The Americans no Disney+ BR, 6 temporadas e 75 episódios (JustWatch BR e AdoroCinema); Agente Noturno T3 em 19/02/2026; Slow Horses T6 semanal até 21/10; Dia Zero; A Agência T2 em 21/06/2026 com 10 episódios: tudo confirmado. Correção: o texto falava em "Lista da MIA do dia" e "vídeo do dia", mas a Lista de hoje foi bloqueada. Tirei as duas menções. A palavra-chave foi para o 1º parágrafo e para um `##`.

### Também conferido
- Spoiler, diálogo, letra, nota e pirataria: nada. As premissas (pai de Profundezas, filho de Pam em Crystal Lake) são as da sinopse oficial.
- Texto original: busquei uma frase de cada matéria entre aspas e não achei cópia.
- Pôsteres: todos batem com a série certa no `posters.json`. Alguns pôsteres oficiais trazem logo impresso (Crystal Lake/Peacock, VisionQuest/Disney+, A Agência/Paramount+, Shrinking e Ted Lasso/Apple TV). Fora a capa da 04, nenhum deles está nas capas; no corpo, entram como manda a regra.
- A Diplomata aparece na 02 (uma das 6 estreias) e é o tema da 05 (a Lista da MIA em texto pode repetir o tema da Lista). Aceito.
- Os horários (17h a 21h) seguem a exceção de hoje registrada na pauta.

### Pendente
- As pastas `blog/` **não estão no pacote da nuvem**. Antes das 17h00, rode `python scripts/nuvem.py subir-pacote 2026-10-16`. Sem isso, a rotina na nuvem não vê as matérias nem o `blog_aprovadas`.
