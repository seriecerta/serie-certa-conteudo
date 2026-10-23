# Blog — formato do pacote e publicação

Estratégia, grade e padrão editorial: `estrategia/11-blog.md`. Fluxo do dia: `/blog-editorial` (`.claude/skills/blog-editorial/SKILL.md`).

## Pasta de cada matéria
```
saida/<data>/blog/<nn>-<slug>/
  materia.json     metadados (abaixo)
  materia.md       o texto
  cena.html        arte da imagem de destaque (motor, 1 section.quadro)
  quadros/01.jpg   imagem de destaque 1920×1080 (renderizada)
  imagens/         pôsteres oficiais + posters.json (scripts/posters.py)
  estado-blog.json escrito pelo publicador (não edite)
```
`<nn>` = ordem do dia (`01` a `05`). A pasta `blog/` fica dentro do dia, então o `scripts/publicar.py` das redes não a enxerga.

## materia.json
```json
{
  "titulo": "7 séries para ver quando você está ansiosa (e precisa desligar a cabeça)",
  "slug": "series-para-ver-ansiosa",
  "subtitulo": "Histórias previsíveis no melhor sentido: episódios curtos, conflito leve e final que acolhe.",
  "resumo": "Até 400 caracteres. Aparece nos cards e no topo da matéria.",
  "categoria": "o-que-assistir",
  "tags": ["Ansiedade", "Séries de conforto", "Comédia"],
  "humor": "ansioso",
  "seo_titulo": "Séries para ver quando você está ansiosa",
  "meta_descricao": "140 a 160 caracteres com a palavra-chave.",
  "palavra_chave": "séries para ansiedade",
  "capa_alt": "Pôsteres de Ted Lasso, Abbott Elementary e Schitt's Creek em leque sobre fundo verde-noite, com o texto 'séries pra desligar a cabeça'.",
  "series": ["Ted Lasso", "Abbott Elementary", "Schitt's Creek"],
  "fontes": [{"titulo": "JustWatch — Ted Lasso", "url": "https://www.justwatch.com/br/serie/ted-lasso"}],
  "quando": "2026-10-17T09:00:00-03:00",
  "video_da_peca": "03-lista-da-mia-…",
  "destaque": false
}
```
- `categoria`: slug de uma categoria ativa (`series`, `filmes`, `o-que-assistir`, `streaming`, `cultura-pop`, `guias`).
- `humor`: uma das 8 cores do app (`sono ansioso romantico triste animado estressado curioso feliz`) ou `brasa`. Vira a cor da capa gerativa e do CTA.
- `series`: **toda** série indicada (igual ao nome usado no `posters.py`); `[]` se nenhuma. Cada uma precisa do pôster no texto.
- `video_da_peca` (opcional): pasta da peça do dia no YouTube. O `[[video]]` do texto vira o vídeo dela quando já estiver público.
- `destaque`: `true` só para a matéria que deve disputar o topo da home (no máximo 1 por dia).
- `autor` (opcional): slug do autor; padrão `redacao`.

## materia.md
Markdown básico (o mesmo que o CMS aceita colar): `##`/`###` (nunca `#`: o título vem do JSON), parágrafos, `- ` e `1. ` listas, `> ` citação, tabelas `| a | b |`, `---`, **negrito**, *itálico*, [links](https://…).
Atalhos do Série Certa:
| Escreva | Vira |
|---|---|
| `![Pôster de Ted Lasso](imagens/ted-lasso.jpg "Ted Lasso · Apple TV+")` | imagem (sobe para o bucket `blog`; pôster ganha o crédito "divulgação (via TVmaze)") |
| `:::info Conferido em 16/10/2026` … `:::` | caixa de destaque (`dica`, `info` ou `atencao`) |
| `[[leia: slug-de-materia-no-ar]]` | card "Leia também" |
| `[[app: ansioso]]` ou `[[app: ansioso \| Descobrir minha série]]` | chamada para o app — **exatamente uma** por matéria |
| `[[video]]` | vídeo do YouTube de `video_da_peca` (some se ainda não estiver no ar) |

## Imagem de destaque
Copie `motor/exemplos/blog-capa-16x9.html` para `cena.html` (variação A com pôsteres ou B com emoji), ajuste chapéu, chamada e `--mood` e renderize:
```
python scripts/renderizar.py saida/<data>/blog/<nn>-<slug> --imagens --formato 16x9
```
Abra `quadros/01.jpg` e confira.

## Comandos
```
python blog/publicar_blog.py --listar --dias 60        # o que já está no ar (repetição e links internos)
python blog/publicar_blog.py --verificar <pasta>       # checa uma matéria antes do revisor
python blog/publicar_blog.py --data <data> --simular   # o que sairia
python blog/publicar_blog.py --vencidos                # publica o que chegou no horário (GitHub Actions de hora em hora)
```
Aprovação: o revisor lista as pastas em `"blog_aprovadas"` do `saida/<data>/revisao.json`.
O publicador grava direto nas tabelas `blog_*` do Supabase com a chave de serviço e sobe as imagens no bucket público `blog` (`materias/<slug>/`). Não usa login nem senha do painel.
Para tirar uma matéria do ar: no painel (`seriecerta.online/dashboard/blog`), mude para "Arquivado".
