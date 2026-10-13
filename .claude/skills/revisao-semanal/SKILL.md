---
name: revisao-semanal
description: Revisão semanal de desempenho do Série Certa — gera o relatório da semana, fecha e abre testes A/B, adota vencedores e propõe melhorias na grade, formatos, ganchos, CTAs e pilares. É o que a rotina de quarta à noite chama; use também quando o Bruno pedir a análise da semana.
---
# Revisão semanal

Regras do ciclo: `estrategia/10-experimentos.md` (leia inteiro antes de começar). Fuso America/Sao_Paulo.

1. **Período:** semana anterior, de quarta a terça (início = hoje − 7 dias, fim = ontem). Antes de 21/10/2026 é período de base: responda "período de base, sem revisão até 21/10" e pare.
2. **Dados:** `python painel/relatorio.py --inicio <início> --fim <fim> --metricas` → `historico/relatorios/semana-<início>.md`. Se alguma fonte falhar (veja `painel/metricas.json` → `erros`), registre no relatório e siga com o que houver. Não invente número.
3. **Análise** (subagente `estrategista`, com o relatório + `estrategia/` + `historico/publicados.md`). Acrescente ao fim do relatório:
   - **Leitura da semana:** 5 a 8 linhas. O que funcionou e o que não funcionou, por formato, horário, pilar, gancho e formato recorrente. Considere o tamanho da amostra: uma diferença com n < 3 é indício, não conclusão.
   - **Testes encerrados:** aplique a regra de decisão de `10-experimentos.md` e escreva o resultado e a decisão no registro de testes.
   - **Mudanças adotadas** (só as que os agentes podem fazer sozinhos): edite os arquivos de `estrategia/` (`08`, `07` etc.) com changelog datado e o "por quê" com o número do relatório.
   - **Novos testes:** no máximo 2 ativos ao mesmo tempo. Escolha os de maior potencial para a métrica principal da meta (envios e alcance). Para cada um: hipótese, slot, variável, A, B, métrica, alocação e período. Registre na tabela de `10-experimentos.md`.
   - **Propostas para o Bruno:** o que exige decisão dele (lista em `10-experimentos.md`), com o dado que sustenta cada proposta e o que você recomendaria.
4. **Aplicação nos pacotes:** o `estrategista` lê os testes ativos de `10-experimentos.md` toda manhã e marca as peças de teste na pauta; o `desdobrador` põe o campo `"experimento"` no `publicar.json`. Nada a fazer aqui além de deixar o registro claro.
5. **Guardar:** commit de `historico/relatorios/` e `estrategia/` com a mensagem `revisão semanal <início>`. **Faça push direto na `main`.**
6. **Aviso final ao Bruno**, em até 8 linhas:
   - os 3 números da semana: alcance, envios e seguidores ganhos;
   - o que mudou na grade ou nos formatos;
   - os testes abertos e os encerrados;
   - as propostas que esperam a decisão dele;
   - o caminho do relatório.

Proibido: publicar, editar `scripts/`, mexer em `revisao.json`, `estado-publicacao.json` ou `PAUSAR`, mudar regras invioláveis do `CLAUDE.md`.
