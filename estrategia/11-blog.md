# Blog — seriecerta.online/blog

> Decisão do Bruno em 16/10/2026: o blog entra na rotina diária com **5 matérias por dia**, cada uma com imagem de destaque que contextualize o conteúdo, feitas pelo mesmo time de agentes das redes.
> CMS e arquitetura do site: `.claude/skills/blog-editorial/referencia-cms.md`. Como o pacote é montado e publicado: `blog/README.md`.

## Papel no funil
| Estágio | O que o blog faz | Métrica |
|---|---|---|
| Descoberta | Busca orgânica (Google): quem pesquisa "séries para quando…", "acabou X, o que ver", "vale a pena Y" | visualizações em D+1 e D+7, % vindo de busca |
| Consideração | Leitura longa, salvos, newsletter | tempo de leitura (scroll 90%), salvos |
| Conversão | Bloco "Chamada para o app" com o humor da matéria (`/descobrir?humor=`) | `platform_cta_click` (PostHog) |

A meta dos 90 dias continua sendo **audiência** (`05-go-to-market.md`). No blog, isso é tráfego de busca, que cresce devagar. Por isso o blog privilegia temas que as pessoas **pesquisam** (perenes) e temas em alta, que pegam busca no mesmo dia.

## Grade diária (todos os dias, fuso America/Sao_Paulo)
| Horário | Slot | Categoria | O que é |
|---|---|---|---|
| 09h00 | **Pelo humor** | O que assistir | Lista perene por humor/contexto ("séries para quando você está ansiosa", "séries para ver no domingo à noite"). Cluster de SEO ligado a `/descobrir?humor=`. |
| 11h00 | **Streaming da semana** | Streaming | O que chegou ou sai dos streamings no Brasil, estreias e novas temporadas da semana. Tudo verificado no dia. |
| 14h00 | **Acabou X?** | Séries | Série em alta (top 10, final de temporada) → "acabou X? N séries com a mesma sensação". |
| 17h00 | **Guia** | Guias (ou Cultura pop) | Guia sem spoiler: "vale a pena?", tempo de maratona, ordem para assistir, por onde começar uma franquia, quem é o elenco/criador em alta. |
| 20h00 | **Lista da MIA em texto** | O que assistir (ou a categoria do tema) | A Lista da MIA do dia em texto, com o vídeo do YouTube embutido (`[[video]]`) quando ele estiver no ar. Se a Lista do dia foi bloqueada, a matéria sai assim mesmo, sem vídeo. |

- As matérias são feitas na rotina da manhã. Matéria aprovada depois do horário sai na próxima rodada de hora em hora do GitHub Actions `publicar` (blog não perde horário).
- Num dia, não repita a mesma série como destaque em duas matérias. A matéria das 20h pode repetir as séries da Lista da MIA (é o mesmo tema em outro formato).
- Repetição: nenhuma matéria com a mesma palavra-chave principal ou a mesma lista de séries de uma matéria dos últimos **60 dias** (`python blog/publicar_blog.py --listar --dias 60`).

## Padrão de cada matéria
- **Tamanho:** 900–1.600 palavras (o publicador recusa menos de 600). Lista: 5 a 10 séries.
- **Estrutura:** abertura de 2–3 parágrafos que começa pelo sentimento/situação (como a MIA) e diz o que a pessoa vai encontrar → `##` a cada 150–300 palavras → fecho curto → **um** `[[app: <humor>]]`.
- **Cada série indicada:** `## Nome da série` + pôster oficial (`![Pôster de …](imagens/…)`) + onde assistir no Brasil + temporadas/episódios/duração + por que combina + **pra quem não é**. Conferido na web no dia, com a fonte em `fontes`.
- **Caixa de data:** toda matéria com disponibilidade traz `:::info Conferido em DD/MM/AAAA` explicando que catálogo muda.
- **Links internos:** 1 a 3 `[[leia: slug]]` de matérias que já estão no ar. Links para o app com UTM: `https://seriecerta.online/descobrir?humor=<humor>&utm_source=blog&utm_medium=organico&utm_campaign=<AAAA-MM-DD>-<slug>`.
- **SEO:** palavra-chave principal no título, no `seo_titulo` (≤ 60 caracteres de preferência, máx. 90), na `meta_descricao` (140–160 caracteres), no 1º parágrafo e em um `##`. Slug curto, sem data e sem ano, a não ser que o tema seja datado ("estreias-netflix-outubro-2026").
- **Imagem de destaque:** arte do motor 1920×1080 (`motor/exemplos/blog-capa-16x9.html`): leque com os pôsteres oficiais das séries principais, ou emoji grande quando a matéria não indica série. Chamada de 3–7 palavras, cor do humor/assunto. `capa_alt` descreve o que a imagem mostra. No leque, prefira pôsteres sem logo de streaming impresso. Se o único pôster oficial da série traz o logo, ele entra assim mesmo: o pôster não é editado, e a regra "sem logo na arte" vale para os elementos que a gente desenha.
- **Voz:** escrita da "Redação Série Certa", com o jeito da MIA (`06-voz-mia.md`): "você", frases curtas, opinião segura, honestidade sobre pra quem não é. Sem "você sabia que…?", sem emoji no texto corrido.
- **Nunca:** spoiler (nem dentro de caixa de spoiler), trecho de diálogo/roteiro, letra de música, cena descrita quadro a quadro, nota/estrela, pirataria ou "onde assistir de graça" ilegal, fofoca de elenco (anti-ICP).

## Medição
- Painel (`/painel`, seção "Blog") e relatório semanal (seção "## Blog"): leituras por matéria da tabela `blog_visualizacoes` do banco do blog, leitura até 90% e cliques no app do PostHog. Search Console quando for verificado.
- Na revisão semanal, a métrica principal do blog é **visualizações em D+7** (busca demora a indexar; D+1 só mostra o efeito do dia).

## Changelog
- 2026-10-16 — Arquivo criado: blog na rotina diária com 5 matérias (09h, 11h, 14h, 17h, 20h), padrão de matéria, imagem de destaque no motor e trava de pôster oficial — por quê: pedido do Bruno.
