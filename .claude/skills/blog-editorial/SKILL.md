---
name: blog-editorial
description: Gera, revisa e deixa prontas para publicar as 5 matérias diárias do blog seriecerta.online/blog (texto, SEO, pôsteres oficiais e imagem de destaque). O /pacote-diario chama esta skill; use também quando o Bruno pedir matérias do blog ou quiser refazer as de um dia.
---
# Blog editorial — 5 matérias por dia

Data de referência: hoje no fuso America/Sao_Paulo (`TZ=America/Sao_Paulo date +%F`), ou a data pedida.
Regras editoriais e grade: `estrategia/11-blog.md`. Formato do pacote: `blog/README.md`.
Como o site e o CMS funcionam (rotas, blocos, categorias, SEO, analytics): `referencia-cms.md`, nesta pasta.

## Passos
1. **Pauta do blog.** Se `saida/<data>/00-pauta.md` ainda não tem a seção "## Blog", rode `python blog/publicar_blog.py --listar --dias 60` e chame o subagente `estrategista` **colando essa saída no pedido** (ele não tem shell) para completá-la: as 5 matérias da grade (09h, 11h, 14h, 17h, 20h), cada uma com tema, palavra-chave principal, **pergunta-alvo** (GEO, `estrategia/12-geo.md`), categoria, humor, séries, matérias internas para linkar, fontes da tendência e horário.
2. **Redação.** Subagente `redator-blog`, um por matéria (podem rodar em paralelo), cada um na pasta `saida/<data>/blog/<nn>-<slug>/`. Cada um termina com `python blog/publicar_blog.py --verificar <pasta>` e `python blog/verificar_geo.py <pasta>` sem erro.
3. **Revisão.** Subagente `revisor`, que confere as matérias do blog junto com o resto do pacote e escreve as aprovadas em `"blog_aprovadas"` do `saida/<data>/revisao.json`. **Mantenha** `aprovadas` e `bloqueadas` das redes. Se o `revisao.json` já existir, acrescente a chave em vez de reescrever o arquivo.
4. **Histórico.** Uma linha por matéria aprovada em `historico/publicados.md`: `data | blog-<slot> | humor | séries | título`.
5. **Simulação.** `python blog/publicar_blog.py --data <data> --simular` não pode acusar erro nas aprovadas, e `python blog/verificar_geo.py saida/<data>` tem que passar em todas.
6. **Guardar.** Na nuvem: `python scripts/nuvem.py subir-pacote <data>`, que leva também as imagens do blog para a publicação de hora em hora (GitHub Actions). Depois faça commit dos `.md`/`.json` de `saida/<data>/blog/`.

A publicação é feita só pelo `python blog/publicar_blog.py --vencidos`, chamado de hora em hora pelo GitHub Actions `publicar` (`.github/workflows/publicar.yml`). Matéria cujo horário já passou sai na rodada seguinte.

## Se algo falhar
- `--verificar` acusa "sem pôster oficial": rode `scripts/posters.py` na pasta da matéria e use a imagem no texto.
- `[[leia: …]] não é uma matéria no ar`: troque por um slug de `--listar`.
- Sem acesso à web para checar fatos: a matéria fica bloqueada, porque não se publica disponibilidade sem verificação.
- Menos de 5 matérias aprovadas: publique as que passaram e registre o motivo em `99-revisao.md`. Um dia com menos matérias é melhor que uma matéria errada.
