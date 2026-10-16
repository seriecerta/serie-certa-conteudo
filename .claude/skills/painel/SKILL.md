---
name: painel
description: Gera o painel de conteúdo do Série Certa (backlog, o que saiu, redes, formatos, pilares, desdobramentos, engajamento, cliques na bio e nos links, seguidores e o blog). Use quando o Bruno pedir o painel, os números da semana ou o status do backlog.
---
# Painel

1. Rode `python painel/painel.py --metricas`.
   - Na nuvem, o script baixa do Supabase os textos de todos os dias (pauta, revisão, estado das publicações) e as métricas guardadas, e devolve as métricas atualizadas para `pacotes-redes/painel/metricas.json`.
   - Sem internet ou sem credenciais, rode sem `--metricas`. O painel sai só com backlog e status.
   - A coleta varre a **conta inteira** (Instagram: feed, Reels e os Stories no ar; YouTube: todos os vídeos do canal, inclusive agendados), não só o que saiu pelo `publicar.py`. Na primeira vez, puxa até 2 anos de histórico; depois, atualiza os últimos 30 dias (`--dias`).
   - **Blog:** as matérias de `saida/<data>/blog/` entram no backlog e na seção "Blog". A coleta lê todas as matérias no ar e as leituras por dia direto do banco do blog (mesmo Supabase, sem chave nova). Leitura até 90% e cliques no app vêm do PostHog, se configurado.
   - Publicações do pacote são ligadas às mídias pelo id do `estado-publicacao.json`. Sem id, o painel tenta pela primeira linha da legenda/título e pelo horário e marca como "conciliado". O que está na conta e não veio de nenhum pacote aparece como "fora do pacote".
2. **Atualize sempre o link fixo do Bruno**: https://claude.ai/artifact/PiohAxjUt6LzDvb8s7mT55. Faça isso também na rotina diária, porque é por ele que o Bruno acompanha o painel.
   - Confira que `grep -c "phx_\|access_token" painel/artefato.html` dá 0 (nenhuma chave na página).
   - Ferramenta Artifact: primeiro `action: "read"` com esse `url`; depois publique `file_path: painel/artefato.html` com o mesmo `url`, sem `icon`.
   - Nunca crie um link novo. Se a ferramenta Artifact não existir na sessão, diga isso na resposta.
   - Para ver no computador, `painel/index.html` é a mesma página, completa e offline.
3. Responda em até 5 linhas: publicadas no período (redes e blog), o que está na fila, o que precisa de atenção (bloqueado, erro, perdido, sem registro) e o destaque de envios/alcance.

Regras:
- O painel **só lê**. Não mexa em `revisao.json`, `estado-publicacao.json`, `PAUSAR` nem nos scripts de `scripts/`.
- As fontes que falharem aparecem com bolinha vermelha no topo do painel (passe o mouse para ver o erro). Avise o Bruno se algo estiver faltando: credencial do Instagram ou do YouTube, ou `POSTHOG_API_KEY`/`POSTHOG_PROJECT_ID` para os cliques com UTM.
- Insights de Stories só existem nas 24 h em que eles estão no ar. A rotina das 9h pega os Stories da véspera (publicados às 10h) com cerca de 23 h de vida, ainda no ar, e guarda o número.
- Na rotina da nuvem, não faça commit (as métricas ficam no Supabase).
