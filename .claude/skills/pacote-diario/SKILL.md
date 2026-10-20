---
name: pacote-diario
description: Gera o pacote diário de conteúdo do Série Certa (pauta, roteiros, narração com a voz da MIA, vídeos, cards, legendas, publicar.json e as 5 matérias do blog), revisa e agenda/publica no Instagram, YouTube e blog. Use quando pedirem o conteúdo do dia ou quando a rotina da manhã rodar.
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
2. **Roteiros (fase 1)** — subagente `roteirista`: `roteiro.md` + `narracao.txt` de cada peça de vídeo, **incluindo a Lista da MIA do dia** (YouTube 12h00, 16:9), e os pôsteres oficiais (`scripts/posters.py`) de toda série citada.
3. **Narração** — `python scripts/narrar.py saida/<data>` (MIA, eleven_v3; `-ela`/`-ele` usam as vozes do casal). Gera `.mp3` + `.json` com o tempo de cada palavra.
4. **Cenas (fase 2)** — subagente `roteirista`: `cena.html` de cada peça no motor de vídeo (`motor/COMPONENTES.md`), sincronizada com a fala, conferida com prévias.
5. **Vídeos** — para cada pasta com `cena.html` e narração: `python scripts/renderizar.py saida/<data>/<nn>-<slug>` (Lista da MIA e vídeo longo do YouTube: `--formato 16x9` → `video-16x9.mp4`; thumbnail: `python scripts/renderizar.py <pasta>/thumb --imagens --formato 16x9`). Sai `video.mp4`/`video-16x9.mp4` + `capa.jpg`.
6. **Desdobramento** — subagente `desdobrador`: legendas, `publicar.json` e as artes de carrossel/Stories (`cena.html` com `section.quadro`, renderizadas com `--imagens`).
6b. **Blog** — siga `.claude/skills/blog-editorial/SKILL.md`, passos 1 e 2: a seção "## Blog" da pauta e as 5 matérias em `saida/<data>/blog/` (`redator-blog`, uma por matéria, em paralelo). Não gasta crédito da ElevenLabs: sai mesmo quando os vídeos caem.
7. **Revisão** — subagente `revisor` (olha os quadros dos vídeos, as imagens e as matérias do blog, gera `revisao.json` com `aprovadas` e `blog_aprovadas`). Se ele mudou narração ou cena, rode de novo os passos 3–5 só para aquela peça.
8. **Histórico** — acrescente em `historico/publicados.md` uma linha por peça aprovada: data | formato | humor | séries | gancho (matéria do blog: `data | blog-<slot> | humor | séries | título`).
9. **Publicação** — `python scripts/publicar.py --data <data>`. Sobe e agenda os vídeos do YouTube e publica no Instagram o que já estiver no horário; o resto do Instagram sai pelo GitHub Actions de hora em hora. Em seguida, `python blog/publicar_blog.py --data <data>` (publica as matérias cujo horário já passou; as outras saem de hora em hora).
10. **Guardar** —
    - Na nuvem: `python scripts/nuvem.py subir-pacote <data>` (tudo, inclusive vídeos — a rotina horária depende disso).
    - Faça commit de `estrategia/`, `historico/` e dos `.md`/`.json` de `saida/<data>/` e **dê push direto na branch `main`** (não crie branch `claude/`). Mensagem: `pacote <data>`.
11. **Aviso final** — 3 linhas: quantas peças aprovadas/bloqueadas (redes e blog), horário da primeira postagem, pendências do `99-revisao.md`.

## Se algo falhar
- Sem acesso à ElevenLabs: siga sem áudio/vídeo; peças sem vídeo ficam fora de `aprovadas`.
- `renderizar.py` acusa "palavra não encontrada na narração": troque o `@palavra` da cena pela grafia que está em `narracao.json`.
- `publicar.py` acusa "sem pôster oficial" ou "pôster não aparece na cena": baixe com `scripts/posters.py`, coloque na cena com `.capa > img`, renderize de novo e rode o revisor. A peça volta a valer sozinha na próxima rodada.
- `posters.py` sem acesso (403 ou erro de rede): o domínio `api.tvmaze.com`/`static.tvmaze.com` precisa estar liberado no ambiente; registre em `99-revisao.md`. Sem pôster, a peça de lista não sai.
- Chromium ausente (erro do Playwright): rode `python -m playwright install --with-deps chromium` uma vez e tente de novo.
- Erro de crédito na ElevenLabs ou de API das redes: não repita em loop; registre em `99-revisao.md`.
- Nunca chame `publicar.py` sem `revisao.json` escrito pelo revisor.
- Na nuvem, se um domínio for bloqueado (`403 host_not_allowed`), registre qual foi em `99-revisao.md` — o Bruno precisa liberar no ambiente.
