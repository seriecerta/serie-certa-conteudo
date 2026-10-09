# TAM, SAM e SOM — Série Certa

> Status: **revisado em 2026-10-09** com fontes públicas. TAM tem fonte oficial; SAM mistura fonte + estimativa; SOM é **cenário**, não meta.
> Regra: todo número aqui precisa de fonte e data. Sem fonte, fica marcado como **estimativa** com a conta usada.
> Observação de método: Cetic.br, IBGE, DataReportal, Nexus e NapoleonCat bloquearam acesso direto nesta revisão; os números abaixo foram conferidos nas páginas oficiais indexadas e em reportagens que citam a fonte. Reconferir no PDF original na próxima revisão.

## Lógica de cálculo (bottom-up)

**TAM — todo mundo no Brasil que assiste séries em streaming por assinatura**
- Usuários de internet no Brasil: **168,7 milhões** de pessoas com 10 anos ou mais (90,5% dessa população), 4º tri de 2025. Fonte: IBGE, PNAD Contínua TIC 2025, divulgada em 02/07/2026 ([Agência IBGE](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/47410-internet-chega-a-95-de-domicilios-do-pais-em-2025); [Mercado & Consumo, 02/07/2026](https://mercadoeconsumo.com.br/02/07/2026/tecnologia/brasil-tinha-168-milhoes-de-usuarios-de-internet-em-2025-afirma-ibge/)).
  - Referências cruzadas: TIC Domicílios 2025 (Cetic.br/CGI.br, coleta mar–ago/2025) = 157 mi usuários, 85% da população 10+ ([principais resultados](https://cetic.br/media/analises/tic_domicilios_2025_principais_resultados.pdf)); DataReportal Digital 2026 = 185 mi (todas as idades, fim de 2025) ([Digital 2026: Brazil](https://datareportal.com/reports/digital-2026-brazil)). Usamos o IBGE por ser a maior amostra e o dado oficial mais recente.
- % que usa streaming de vídeo por assinatura: **44,4%** dos domicílios com TV tinham serviço **pago** de streaming de vídeo em 2025 (33,4 milhões de domicílios; eram 43,4% em 2024). Fonte: IBGE, PNAD Contínua TIC 2025, 02/07/2026 ([Agência IBGE](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/47410-internet-chega-a-95-de-domicilios-do-pais-em-2025)).
  - **Estimativa de conversão domicílio → pessoa:** o IBGE mede lares, não pessoas. Usamos os 44,4% como proxy da % de internautas com acesso a streaming pago (quem mora num lar assinante tem acesso, mesmo sem ser o titular).
  - Checagem de sanidade: Comscore (4ª edição do estudo de TV conectada, campo set–out/2025, divulgado jun/2026) estima **88 milhões** de pessoas (67% da população online) consumindo conteúdo digital pela TV conectada — inclui serviços grátis, então é teto, não base ([Mercado & Consumo, 14/06/2026](https://mercadoeconsumo.com.br/14/06/2026/economia/uso-de-streaming-pela-tv-conectada-avanca-e-chega-a-88-milhoes-de-pessoas-no-brasil/)).
- **TAM (pessoas) = 168,7 mi × 44,4% ≈ 74,9 milhões** (estimativa sobre fonte oficial).
- TAM (R$/ano) = TAM pessoas × ticket anual. **Pressuposto:** ticket de R$ 58,80/ano (Plus, R$ 4,90 × 12) a R$ 118,80/ano (Max, R$ 9,90 × 12), como se 100% pagassem. É teto teórico, não receita possível.
  - 74,9 mi × R$ 58,80 ≈ **R$ 4,40 bi/ano**; 74,9 mi × R$ 118,80 ≈ **R$ 8,90 bi/ano**.

**SAM — quem tem a dor que o Série Certa resolve e está ao alcance de Instagram/YouTube**
- Filtro 1: assina 2+ streamings → **62,5% dos assinantes**. Fonte: Nexus (FSB), pesquisa com 1.000 pessoas de 16+ das classes A, B e C, campo 14–20/07/2025, margem 3 p.p.: 27% assinam 1 serviço, 26% assinam 2–3 e 19% assinam 4+ ([IstoÉ](https://istoe.com.br/netflix-domina-servico-de-streaming-no-brasil-aponta-pesquisa-da-nexus); [Fast Company Brasil](https://fastcompanybrasil.com/money/72-dos-brasileiros-das-classes-abc-usam-streaming-veja-os-mais-populares/)).
  - Conta: (26% + 19%) ÷ (27% + 26% + 19%) = 45% ÷ 72% = 62,5% de quem assina tem 2 ou mais. Ressalva: amostra só classes ABC; a base de pagantes do IBGE também concentra renda mais alta (renda per capita dos lares com streaming pago = R$ 2.950 vs. R$ 1.390 sem, PNAD TIC 2024), então o viés é aceitável.
  - Reforço: Comscore (campo set–out/2025) aponta média de **4,6 serviços pagos** por domicílio entre usuários de TV conectada ([O Hoje, 22/06/2026](https://ohoje.com/2026/06/22/brasileiro-assina-quase-nove-servicos-de-streaming-por-mes-aponta-pesquisa/)).
- Filtro 2: 18–40 anos, usuário ativo de Instagram/YouTube → **40% × 94% = 37,6%**.
  - **18–40 anos = 40% (estimativa, sem fonte direta).** Conta: idade mediana do Brasil é 35 anos e 19,8% da população tem até 14 anos (IBGE, Censo 2022, [Agência IBGE](https://agenciadenoticias.ibge.gov.br/media/com_mediaibge/arquivos/ca93b770f7ef3931bd425cdea60c8b5c.pdf)) → abaixo de 18 ≈ 25% (estimativa) → 18–35 ≈ 50% − 25% = 25%; 35–40 ≈ 7% (estimativa, ~1,4 p.p. por ano de idade) → 18–40 ≈ 32% da população. Ajustamos para 40% entre assinantes porque jovens adultos sobre-indexam em internet (TIC 2025: ~95% de uso nas faixas 16–34 vs. 54% em 60+) e em streaming (Nexus 2025: jovens normalizam mais a maratona). **Faixa plausível: 32–45%.** Trocar por dado real quando houver tabela etária de assinantes.
  - **Usa rede social = 94%**: usuários de internet de 25–34 anos que usaram redes sociais (16–24 anos: 93%). Fonte: TIC Domicílios 2025, tabela C5 ([Cetic.br](https://cetic.br/en/tics/domicilios/2025/individuos/C5/)). Não há recorte público por Instagram/YouTube nessa fonte; referência de escala: NapoleonCat estima 163,8 mi de usuários endereçáveis do Instagram no Brasil em abr/2026, com 25–34 anos como maior faixa (~51,6 mi) ([NapoleonCat](https://stats.napoleoncat.com/instagram-users-in-brazil/2026/04/)).
- Filtro 3: consome conteúdo de recomendação de séries (perfis/canais de nicho) → **30% (estimativa, sem fonte)**. Conta: não há pesquisa pública sobre consumo de perfis de recomendação. Indícios de que a dor é comum: tempo médio de 13,6 min para decidir o que assistir (Comscore, via [O Hoje, 22/06/2026](https://ohoje.com/2026/06/22/brasileiro-assina-quase-nove-servicos-de-streaming-por-mes-aponta-pesquisa/)) e 51% já viraram a madrugada vendo série (Nexus, campo jul/2025, [Viva](https://viva.com.br/cultura-e-lazer/estudo-revela-que-sacrificios-maratonar-series.html)). **Faixa plausível: 20–40%.** É o filtro mais frágil do cálculo.
- **SAM = 74,9 mi × 62,5% × 40% × 94% × 30% ≈ 5,3 milhões de pessoas** (faixa com os extremos dos filtros 2 e 3: ~2,8 a ~7,9 mi).
- SAM (R$/ano), mesmo pressuposto de ticket: 5,3 mi × R$ 58,80 ≈ **R$ 310 mi**; × R$ 118,80 ≈ **R$ 627 mi**.

**SOM — o que dá para capturar em 12 meses só com orgânico (orçamento zero)**
> **Cenário, não meta.** O alcance mensal ainda não tem dado (`historico/metricas.md` vazio). As metas reais ficam `[definir com o Bruno]` em `05-go-to-market.md`.

Fórmula: contas alcançadas/mês × taxa de clique no link × taxa de cadastro × taxa de conversão para pago.

| Taxa | Valor usado | Base |
|---|---|---|
| Clique no link / alcance | 1% | **estimativa**. Único número achado é 1–3% de CTR em link de Stories, de blog sem fonte primária ([influencerfee](https://influencerfee.com/blog/instagram-story-swipe-up-rates/)); usamos o piso porque o alcance total inclui Reels sem link clicável |
| Cadastro / clique | 6,6% | mediana de conversão de landing pages, todas as indústrias — Unbounce Conversion Benchmark Report 2024, 41 mil+ páginas ([Unbounce](https://unbounce.com/landing-page-articles/what-is-a-good-conversion-rate/)) |
| Pago / cadastro (12 m) | 3% | **estimativa**: referência de SaaS freemium 3–5% e 2,6% freemium→pago citados pela [Crazy Egg](https://www.crazyegg.com/blog/free-to-paid-conversion-rate/) (sem fonte primária de app de consumo) |

| Cenário (alcance/mês, **hipótese**) | Cliques/mês | Cadastros 12 m | Pagantes ao fim de 12 m | Receita anualizada (R$ 58,80–118,80/pagante) |
|---|---|---|---|---|
| Conservador — 50 mil | 500 | ~396 | ~12 | R$ 706 – R$ 1.426 |
| Base — 200 mil | 2.000 | ~1.584 | ~48 | R$ 2.822 – R$ 5.702 |
| Otimista — 500 mil | 5.000 | ~3.960 | ~119 | R$ 6.997 – R$ 14.137 |

- Pressupostos: alcance constante no mês (sem crescimento), sem churn, todo pagante no Plus (piso) ou no Max (teto). Alcance mensal conta contas únicas por mês; a soma de 12 meses ignora sobreposição de público, então superestima.
- Leitura: mesmo no cenário otimista o SOM é <0,1% do SAM. Isso confirma a decisão do Bruno de focar **audiência** nos 90 dias — o gargalo é alcance, não conversão.

## Tabela de trabalho
| Camada | Pessoas | R$/ano (ticket R$ 58,80–118,80) | Fonte | Data |
|---|---|---|---|---|
| TAM | ~74,9 mi | R$ 4,40 bi – R$ 8,90 bi (teto teórico) | IBGE PNAD Contínua TIC 2025 (168,7 mi internautas × 44,4% lares com streaming pago); conversão lar→pessoa é estimativa | dados 2025, divulgação 02/07/2026 |
| SAM | ~5,3 mi (faixa 2,8–7,9 mi) | R$ 310 mi – R$ 627 mi | TAM × Nexus 2025 (62,5% com 2+ streamings) × estimativa 18–40 (40%) × TIC Domicílios 2025 (94% em redes) × estimativa nicho (30%) | Nexus jul/2025; TIC 2025; estimativas 2026-10-09 |
| SOM 12m | cenário base ~1.584 cadastros / ~48 pagantes (faixa 396–3.960 / 12–119) | R$ 2,8 mil – R$ 5,7 mil anualizado (faixa R$ 0,7 mil – R$ 14,1 mil) | cenário: alcance hipotético × CTR 1% (estimativa) × cadastro 6,6% (Unbounce 2024) × pago 3% (estimativa) | 2026-10-09 |

## Lacunas abertas
- Penetração de streaming pago **por pessoa** (só existe por domicílio).
- Distribuição etária de assinantes de streaming no Brasil.
- % do público que consome perfis/canais de recomendação de séries (sem pesquisa pública).
- CTR de link em Stories e conversão freemium→pago de app de consumo no Brasil (só benchmarks genéricos).
- Dados próprios (PostHog, Insights) — não puxados nesta revisão por decisão do Bruno.

## O que isso muda no conteúdo
- O conteúdo fala com o **SAM**, não com o TAM: quem já assina 2+ streamings e trava na hora de escolher.
- Cada peça deve servir a um humor/contexto — é assim que o SAM se reconhece ("eu, toda noite").
- Com SOM limitado por alcance, a prioridade dos 90 dias é **ser compartilhado** pelo SAM (ver `05-go-to-market.md`).

## Changelog
- 2026-10-09 — Trocados todos os `[validar]` por número + fonte + data (IBGE PNAD TIC 2025, TIC Domicílios 2025, Nexus jul/2025, Comscore 2025/26, Unbounce 2024); filtros sem fonte marcados como estimativa com a conta; tabela preenchida; SOM refeito como cenário de funil orgânico com orçamento zero; seção de lacunas criada — por quê: revisão `/estrategia` pedida pelo Bruno, meta dos 90 dias passou a ser audiência e o orçamento é zero.
