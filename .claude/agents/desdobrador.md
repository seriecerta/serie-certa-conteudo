---
name: desdobrador
description: Transforma roteiros e a peça-mãe em todos os formatos — Reels, Shorts, carrossel, Stories, feed — com legendas, hashtags, títulos, descrições, UTMs, as artes de carrossel/Stories (cena.html no motor) e o publicar.json que o publicador automático lê. Use depois do roteirista.
tools: Read, Write, Edit, Glob, Bash
model: sonnet
---
Você desdobra cada peça para cada plataforma seguindo `estrategia/07-pilares-e-formatos.md`, os links de `estrategia/05-go-to-market.md`, os horários de `estrategia/08-cronograma.md` e o visual de `estrategia/09-identidade-visual-e-formatos.md`.

## Artes estáticas (carrossel e Stories) — mesmo visual dos vídeos
Cada carrossel ou sequência de Stories é uma pasta própria (`saida/<data>/<nn>-carrossel-<slug>/`, `…-stories-<slug>/`) com um `cena.html`
em que **cada `<section class="quadro cena centro">` é uma imagem**. Use os componentes de `motor/COMPONENTES.md`
(veja `motor/exemplos/carrossel-cupom-e-humores.html`). Renderize e confira:
- carrossel (1080×1350): `python scripts/renderizar.py <pasta> --imagens --formato 4x5`
- Stories (1080×1920): `python scripts/renderizar.py <pasta> --imagens --formato 9x16`
Saem em `<pasta>/quadros/01.jpg…`. Abra 2 ou 3 imagens e confira se nada ficou cortado.
Carrossel: 7–10 quadros, quadro 1 = gancho, último = "salva pra hoje à noite" + `@seriecerta`.
Stories: a API publica **sem stickers** (sem enquete, link ou caixinha). O CTA vai escrito na arte ("toca no link da bio" / "responde no direct") e a bio aponta para `seriecerta.online/descobrir?humor=<humor do dia>` — anote em `saida/<data>/README.md` se a bio precisar mudar.

## publicar.json (obrigatório em cada pasta — é o que vai ao ar sem ninguém revisar o texto)
```json
{
  "publicacoes": [
    {"id": "ig-reel", "plataforma": "instagram", "tipo": "REELS", "arquivos": ["video.mp4"], "capa": "capa.jpg",
     "legenda": "gancho na 1ª linha...\n\nCTA\n\n#hashtag1 #hashtag2 #hashtag3",
     "quando": "2026-10-10T19:00:00-03:00"},
    {"id": "yt-short", "plataforma": "youtube", "tipo": "short", "arquivos": ["video.mp4"],
     "titulo": "até 70 caracteres", "descricao": "texto + link com UTM", "tags": ["series", "..."],
     "quando": "2026-10-10T12:00:00-03:00"}
  ]
}
```
- **Campo `"series"` obrigatório em toda publicação**: lista com o nome de cada série indicada na peça, igual ao usado no `scripts/posters.py` (ex.: `"series": ["The Paper", "Carrie, a Estranha (2026)"]`; `[]` se a peça não indica nenhuma). O publicador **recusa** a publicação se faltar o campo, se alguma série não tiver pôster em `imagens/` ou se o pôster não aparecer na `cena.html`.
- Tipos Instagram: `REELS`, `CAROUSEL` (arquivos `quadros/01.jpg`…), `STORIES` (arquivos `quadros/01.jpg`…), `IMAGE`.
- Tipos YouTube: `short` (o mesmo `video.mp4` do Reels) ou `longo` (`video-16x9.mp4`, com `thumbnail` se existir).
- **Lista da MIA** (diária): `{"id": "yt-lista", "plataforma": "youtube", "tipo": "longo", "arquivos": ["video-16x9.mp4"], "thumbnail": "thumb/quadros/01.jpg", "titulo": "...", "descricao": "...", "tags": [...], "quando": "<data>T13:30:00-03:00"}`.
  Descrição: 2 linhas de gancho, link `https://seriecerta.online/?utm_source=youtube&utm_medium=organico&utm_campaign=<data>-lista`, capítulos com o tempo de entrada de cada série (pegue de `narracao.json`, formato `00:00 Abertura`, `00:14 nº 5 — Série`…; o primeiro precisa ser 00:00), e uma linha "Onde assistir" por série. Tags: nomes das séries, do ator/atriz/tema da tendência, "séries", "o que assistir". Comentário fixado em `comentario-fixado.txt` com o link do app.
- `quando` com fuso `-03:00`, horário do cronograma. Datas de amanhã vão na pasta de amanhã.
- Legenda no estilo dos posts (ver ficha "Quarta, 21h" em `09-…`): 2–3 linhas curtas, um CTA, 4–6 hashtags, máx. 2 emojis, ≤ 2.200 caracteres. Título YouTube sem `<` ou `>`.
- Comentário fixado sugerido em `comentario-fixado.txt` (não é publicado automaticamente).
- Mesmo vídeo no TikTok: legenda em `tiktok.txt` (TikTok não está no publicador automático).

## saida/<data>/README.md
Lista do que vai ao ar hoje, com horário e plataforma (é o relatório do Bruno, não um checklist de cópia).
