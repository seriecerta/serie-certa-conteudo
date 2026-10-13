---
name: painel
description: Gera o painel de conteúdo do Série Certa (backlog, o que saiu, redes, formatos, pilares, desdobramentos, engajamento, cliques na bio e nos links, seguidores). Use quando o Bruno pedir o painel, os números da semana ou o status do backlog.
---
# Painel

1. Rode `python painel/painel.py --metricas`.
   - Na nuvem, o script baixa do Supabase os textos de todos os dias (pauta, revisão, estado das publicações) e as métricas guardadas, e devolve as métricas atualizadas para `pacotes-redes/painel/metricas.json`.
   - Sem internet ou sem credenciais, rode sem `--metricas`. O painel sai só com backlog e status.
2. Abra `painel/index.html` (arquivo único, funciona offline). Se o Bruno quiser um link, publique esse arquivo como artefato.
3. Responda em até 5 linhas: publicadas no período, o que está na fila, o que precisa de atenção (bloqueado, erro, perdido, sem registro) e o destaque de envios/alcance.

Regras:
- O painel **só lê**. Não mexa em `revisao.json`, `estado-publicacao.json`, `PAUSAR` nem nos scripts de `scripts/`.
- As fontes que falharem aparecem com bolinha vermelha no topo do painel (passe o mouse para ver o erro). Avise o Bruno se algo estiver faltando: credencial do Instagram ou do YouTube, ou `POSTHOG_API_KEY`/`POSTHOG_PROJECT_ID` para os cliques com UTM.
- Insights de Stories só existem nas 24 h em que eles estão no ar. Rodar o painel à noite, depois dos Stories, garante que esse número fique guardado.
- Na rotina da nuvem, não faça commit (as métricas ficam no Supabase).
