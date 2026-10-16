# Melhoria contínua e testes A/B

> Ciclo definido pelo Bruno em 13/10/2026: a grade de `08-cronograma.md` roda **fixa de 14 a 20/10** (período de base).
> Depois, toda semana os agentes analisam os resultados, propõem melhorias em tudo (grade, formatos, ganchos, CTAs, pilares)
> e testam as mudanças com testes A/B antes de adotar.

## Calendário
| Quando | O quê |
|---|---|
| 14 a 20/10 | **Período de base.** Grade fixa, sem testes. Serve de referência para tudo que vem depois. |
| Qua, 21/10, 18h17 | **1ª revisão semanal** (rotina "Série Certa · revisão semanal", skill `/revisao-semanal`): relatório de 14–20/10, propostas e os primeiros testes. |
| Toda quarta, 18h17 | Revisão da semana anterior (quarta a terça): fecha os testes que atingiram o tamanho, adota vencedores, abre os próximos testes. |
| Todo dia, 9h00 | Coleta de métricas e atualização do link do painel (rotina do painel). Guarda uma foto diária dos números de cada post. |

A revisão roda na quarta à noite: a coleta das 9h de quarta já traz o D+1 dos posts de terça, o último dia da semana analisada. As mudanças valem a partir do pacote da manhã seguinte.

## Como medir
- **Relatório:** `python painel/relatorio.py --inicio <AAAA-MM-DD> --fim <AAAA-MM-DD>` gera `historico/relatorios/semana-<inicio>.md`.
- **Base de comparação: D+1.** São os números do post na primeira foto diária com 12 h ou mais de vida, ou seja, na coleta das 9h da manhã seguinte. Com isso, um post de 3 dias não é comparado com um de 3 horas.
- **Métrica principal por formato** (meta dos 90 dias = audiência, `05-go-to-market.md`):

| Formato | Métrica principal | Secundárias |
|---|---|---|
| Reels | envios ÷ alcance | alcance, views, follows |
| Short | views em D+1 | curtidas, comentários |
| Lista da MIA | views em D+1 | curtidas, comentários, cliques UTM |
| Carrossel | salvos ÷ alcance | envios, alcance |
| Stories | alcance da 1ª tela | respostas, visitas ao perfil, cliques no link da bio |
| Matéria do blog | visualizações em D+7 (`article_view`, PostHog) | leitura até 90%, cliques no app (`platform_cta_click`) |

## Regras dos testes A/B
1. **Uma variável por teste.** Exemplos: horário de um slot, tipo de gancho (pergunta × afirmação × "pra amiga que..."), duração, formato recorrente, texto do CTA (dentro do mesmo estágio do funil), capa, primeira tela do carrossel, título do Short.
2. **No máximo 2 testes ao mesmo tempo**, em slots diferentes, para um não contaminar o outro.
3. **Hipótese escrita antes**, com a métrica principal declarada no registro abaixo. Nada de escolher a métrica depois de ver o resultado.
4. **Alocação:** alterne a variante por dia (A em dias pares, B em dias ímpares) no mesmo slot. Quando o teste não depende do horário (gancho, capa, CTA), também vale A e B no mesmo dia em slots equivalentes (Reels 13h30 × Reels 18h30), trocando a ordem no dia seguinte.
5. **Tamanho mínimo:** 3 posts por variante (de preferência 7 dias, uma semana inteira).
6. **Decisão** (o relatório calcula):
   - Diferença ≥ 20% na mediana da métrica principal, com ≥ 3 posts por variante, e a secundária mais importante não piorando mais de 20% → a vencedora é adotada.
   - Diferença menor que 20% → empate: mantém a atual (A) e fecha o teste.
   - Menos de 3 posts por variante → estende 1 semana. Se ainda faltar, encerra como inconclusivo.
   - Com a conta pequena, um único post viral distorce a mediana. Se um post sozinho tiver mais que o dobro da soma dos outros da variante, registre e estenda o teste.
7. **Marcação:** toda peça de teste leva no `publicar.json` (topo ou na publicação) `"experimento": {"id": "<id-do-teste>", "variante": "A"}`. O publicador ignora esse campo; o painel e o relatório leem.
8. **As regras invioláveis do `CLAUDE.md` não entram em teste:** fatos, spoiler, pôster oficial, 1 CTA, voz da MIA, revisor e publicador.

## O que os agentes mudam sozinhos e o que propõem ao Bruno
**Mudam sozinhos** (com registro no changelog do arquivo e no resumo da revisão):
- Abrir e fechar testes A/B dentro das regras acima.
- Adotar o vencedor de um teste: horário de um slot (entre 8h e 22h), qual formato ocupa um slot que já existe, ganchos, durações, formatos recorrentes, capas, títulos, hashtags, texto do CTA dentro do estágio do funil.
- Ajustar os pesos dos pilares em até 10 pontos por semana, quando houver dado de pelo menos 2 semanas.

**Só propõem** (seção "Propostas para o Bruno" do relatório; o Bruno decide e eles aplicam depois):
- Mudar a quantidade de publicações por dia, incluir ou tirar uma rede, criar ou remover um slot da grade.
- Tirar a Lista da MIA ou voltar o vídeo longo semanal.
- Mudar a meta dos 90 dias, o orçamento, o posicionamento, o ICP, a voz da MIA ou as vozes.
- Qualquer coisa que toque as regras invioláveis do `CLAUDE.md`.

## Registro de testes
| ID | Período | Slot | Variável | A (atual) | B (desafiante) | Métrica principal | Resultado | Decisão |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

## Changelog
- 2026-10-16 — Métrica do blog (views D+7) incluída. Ainda não é coletada pelo `painel/relatorio.py`, então até lá ela é lida no PostHog — por quê: blog entrou na rotina.
- 2026-10-13 — Coleta diária passa de 17h47 para 9h00 e o D+1 passa a ser a foto da manhã seguinte (12 h ou mais de vida) — por quê: Bruno quer o painel atualizado de manhã.
- 2026-10-13 — Arquivo criado: ciclo de 7 dias de base (14–20/10) + revisão semanal às quartas com testes A/B, métrica em D+1 e limites do que os agentes mudam sozinhos — por quê: pedido do Bruno de melhoria contínua com testes A/B depois da primeira semana da grade diária.
