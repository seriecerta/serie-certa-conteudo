---
name: pacote-diario
description: Gera o pacote diário de conteúdo do Série Certa (pauta, roteiros, narração com a voz da MIA, vídeos, cards, legendas e publicar.json), revisa e agenda/publica no Instagram e YouTube. Use quando pedirem o conteúdo do dia ou quando a rotina da manhã rodar.
---
# Pacote diário

Data de referência: hoje no fuso America/Sao_Paulo (`TZ=America/Sao_Paulo date +%F`).

## 0. Na nuvem (Claude Code web / rotina cloud)
Se `CLAUDE_CODE_REMOTE=true`:
- `python scripts/nuvem.py baixar-credenciais`
- `python scripts/nuvem.py baixar-pacote <data>` — se já vier `revisao.json`, o pacote de hoje já existe: pule para o passo 9.

Fora da nuvem: se `saida/<data>/revisao.json` já existir, pule para o passo 9.

## Passos
1. **Pauta** — subagente `estrategista` → `saida/<data>/00-pauta.md` (peças de hoje + rascunho de amanhã).
2. **Roteiros** — subagente `roteirista` para cada peça de vídeo.
3. **Narração** — `python scripts/narrar.py saida/<data>` (MIA por padrão; `-ela`/`-ele` usam as vozes do casal).
4. **Vídeos** — para cada pasta com narração: `python scripts/montar_video.py saida/<data>/<nn>-<slug> --formato 9x16` (longo do YouTube: `--formato 16x9`).
5. **Desdobramento** — subagente `desdobrador` (gera `publicar.json`, `carrossel.json`, `stories.json`).
6. **Cards e Stories** — para cada pasta com `carrossel.json` ou `stories.json`: `python scripts/renderizar_cards.py saida/<data>/<nn>-<slug>`.
7. **Revisão** — subagente `revisor` (gera `revisao.json`). Se ele mudou narração, rode o passo 3 e o 4 de novo só para aquela peça.
8. **Histórico** — acrescente em `historico/publicados.md` uma linha por peça aprovada: data | formato | humor | séries | gancho.
9. **Publicação** — `python scripts/publicar.py --data <data>`. Sobe e agenda os vídeos do YouTube e publica no Instagram o que já estiver no horário; o resto do Instagram sai pela rotina de hora em hora.
10. **Guardar** —
    - Na nuvem: `python scripts/nuvem.py subir-pacote <data>` (tudo, inclusive vídeos — a rotina horária depende disso).
    - Faça commit de `estrategia/`, `historico/` e dos `.md`/`.json` de `saida/<data>/` e **dê push direto na branch `main`** (não crie branch `claude/`). Mensagem: `pacote <data>`.
11. **Aviso final** — 3 linhas: quantas peças aprovadas/bloqueadas, horário da primeira postagem, pendências do `99-revisao.md`.

## Se algo falhar
- Sem acesso à ElevenLabs: siga sem áudio/vídeo; peças sem vídeo ficam fora de `aprovadas`.
- Erro de crédito na ElevenLabs ou de API das redes: não repita em loop; registre em `99-revisao.md`.
- Nunca chame `publicar.py` sem `revisao.json` escrito pelo revisor.
- Na nuvem, se um domínio for bloqueado (`403 host_not_allowed`), registre qual foi em `99-revisao.md` — o Bruno precisa liberar no ambiente.
