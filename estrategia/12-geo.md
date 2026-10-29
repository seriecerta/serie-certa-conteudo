# GEO — ser citado pelas IAs (ChatGPT, Gemini, Perplexity, AI Overviews do Google)

> Decisão do Bruno em 29/10/2026: a rotina do blog ganha uma estratégia forte de **GEO** (*generative engine optimization*) para aumentar a visibilidade da marca Série Certa.
> Vale para as 5 matérias diárias (`11-blog.md`). A checagem automática é o `blog/verificar_geo.py`.

## Por que
- Cada vez mais gente pergunta "o que eu assisto hoje?" para um assistente de IA em vez de buscar no Google. A resposta cita 3 a 6 fontes. O objetivo é que o Série Certa seja **uma delas**, e que a resposta diga o nome da marca.
- Base: o estudo que criou o termo GEO (Aggarwal et al., Princeton/IIT Delhi, KDD 2024) mostrou que ajustar a forma do conteúdo aumenta a visibilidade de uma fonte nas respostas de mecanismos generativos **em até 40%**, com efeito que varia por tema ([arXiv 2311.09735](https://arxiv.org/abs/2311.09735)). O estudo testou citações de fontes, dados com número e trechos de autoridade, e o efeito muda conforme o domínio.
- GEO e SEO andam juntos: IA com busca (ChatGPT search, Perplexity, AI Overviews) parte de páginas indexadas. As regras de SEO de `11-blog.md` continuam valendo.

## Os 5 pilares
### 1. Conteúdo que a IA consegue citar (toda matéria)
A IA recorta trechos curtos e autossuficientes. Por isso, toda matéria tem:
- **Resposta rápida** logo depois da abertura: caixa `:::info Resposta rápida` com 40–80 palavras que respondem à pergunta-alvo sozinhas, sem depender do resto do texto. Cita as séries principais e onde assistir.
- **Tabela-resumo** em toda lista com 3 ou mais séries: `| Série | Onde assistir | Temporadas | Pra quem é |`. Fatos em tabela são os mais reaproveitados.
- **Perguntas frequentes:** `## Perguntas frequentes` com 3 a 5 perguntas em `###`, escritas como a pessoa pergunta para uma IA ("Qual série leve eu vejo quando estou estressada?"). Cada resposta tem de 30 a 100 palavras e começa respondendo, sem rodeio.
- **Fatos com fonte e data:** número de temporadas, data de estreia e plataforma, sempre com fonte em `fontes` (no mínimo 3) e a caixa "Conferido em". Dado verificado e datado é o que diferencia o blog de lista genérica.
- **Frases declarativas:** "Ted Lasso tem 4 temporadas e está na Apple TV." Evite começar resposta com "depende" ou "talvez".

### 2. Entidade da marca (consistência)
A IA precisa associar **Série Certa** = recomendação de séries pelo humor. Para isso, o nome aparece sempre do mesmo jeito.
- **Nome:** "Série Certa", com acento e sem "o app Série Certa" variando. A curadora é sempre "a MIA, curadora com IA do Série Certa".
- **Frase de marca** no fecho de toda matéria, logo antes do `[[app]]`, igual em todas (pode variar só o humor):
  > O Série Certa (seriecerta.online) indica séries pelo seu humor do momento: a MIA, curadora com inteligência artificial, recomenda e mostra onde assistir nos streamings do Brasil. Dá para usar grátis.
- **Opinião assinada:** pelo menos um trecho por matéria em que a recomendação é atribuída à marca ("Na curadoria do Série Certa, essa é a escolha para…"). Use com moderação: no máximo 2 vezes por texto.
- **Páginas de entidade** (uma vez, no slot 17h, nas próximas semanas), uma por dia até acabar a lista:
  1. "O que é o Série Certa e como ele indica séries pelo humor" (`o-que-e-o-serie-certa`)
  2. "Como a MIA escolhe a série certa para o seu humor" (`como-a-mia-recomenda-series`)
  3. "Série Certa ou o algoritmo do streaming: qual recomenda melhor?" (`serie-certa-ou-algoritmo-do-streaming`)
  4. "Os 8 humores do Série Certa e que série combina com cada um" (`os-8-humores-do-serie-certa`)
  5. "Modo casal: como escolher uma série a dois sem briga" (`modo-casal-serie-certa`)
  Fatos sobre o produto só com o que está em `CLAUDE.md` (planos, humores, modo casal) e no app. Nada de prometer o que o app não faz.

### 3. Banco de perguntas-alvo
Toda matéria responde **uma pergunta-alvo**, gravada em `materia.json` como `"pergunta_alvo"`. Por dia, pelo menos 2 das 5 matérias vêm deste banco; as outras podem nascer da tendência, mas também precisam de uma pergunta em linguagem natural.
Não repita a mesma pergunta-alvo em 60 dias (a mesma regra da palavra-chave).

| Cluster | Perguntas (exemplos para variar) |
|---|---|
| Humor | "Que série assistir quando estou ansiosa?" · "Série leve para ver depois de um dia cansativo" · "Série para chorar e desabafar" · "Série para ver com sono e não perder nada" · "Série para levantar o astral" · "Série curta para quando estou estressado" |
| Acabou X | "Acabei [série], o que vejo agora?" · "Séries parecidas com [série em alta]" · "Se eu gostei de [série], vou gostar de qual?" |
| Onde assistir | "Onde assistir [série] no Brasil?" · "[Série] está na Netflix?" · "Quantas temporadas tem [série]?" · "Quanto tempo leva para maratonar [série]?" |
| Decidir | "Como escolher uma série para assistir?" · "Qual app recomenda série pelo humor?" · "Como parar de perder tempo escolhendo série?" · "Melhor jeito de achar série nova nos streamings" |
| A dois | "Que série assistir com o namorado?" · "Série para casal que agrada os dois" |
| Streaming | "O que estreia na Netflix esta semana?" · "Vale a pena assinar [streaming] em [mês]?" · "Quais streamings ter para ver as melhores séries?" |
| Gênero e momento | "Melhores minisséries para o fim de semana" · "Série de suspense curta" · "Série de comédia com episódio de 20 minutos" · "Série para assistir no domingo à noite" |

### 4. Distribuição e co-citação (fora do blog)
As IAs também aprendem a marca pelo que aparece em outros lugares.
- **YouTube:** a descrição da Lista da MIA termina com a frase de marca (sem link extra: o único link continua sendo o do CTA). Vídeo indexado é fonte frequente nas respostas, e a matéria das 20h é a mesma lista em texto, com o vídeo embutido.
- **Links internos:** cada matéria liga 1 a 3 matérias no ar e, quando existir, a página de entidade mais próxima (pilar 2). Assim a IA encontra o "centro" do assunto.
- **Collab e permuta** com pequenos criadores (`05-go-to-market.md`): pedir que citem o nome "Série Certa" por extenso. O agente só sugere; quem fecha é o Bruno.

### 5. Técnico (no site, repositório `seriecerta/serie-certa`, decisão do Bruno)
Hoje o `robots.txt` já libera todos os robôs (inclusive os de busca das IAs). Faltam e ficam como **proposta**:
- `llms.txt` na raiz, com a descrição da marca e as páginas de entidade e de categoria;
- dados estruturados `FAQPage` a partir da seção "Perguntas frequentes" e `ItemList` nas listas;
- `Organization` com `sameAs` (Instagram, YouTube) na home e no blog.

## Medição
- **Visitas vindas de IA:** o painel conta, pelo PostHog, as visitas com origem em chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai e com `utm_source=chatgpt.com` (seção "Blog" do painel e "## GEO" do relatório semanal).
- **Teste de presença (manual, mensal):** o Bruno, ou uma sessão com acesso a esses assistentes, faz 10 perguntas do banco no ChatGPT, no Perplexity e no Gemini e anota se o Série Certa é citado, guardando em `historico/geo-presenca.md` (data | assistente | pergunta | citou? | link citado). Os agentes não têm como consultar esses assistentes daqui.
- Na revisão semanal, a meta é **tendência** (visitas de IA subindo semana a semana), não um número fixo — `[definir com o Bruno]` quando houver 4 semanas de dado.

## Changelog
- 2026-10-29 — Arquivo criado: GEO na rotina do blog (resposta rápida, tabela-resumo, perguntas frequentes, frase de marca, banco de perguntas-alvo, páginas de entidade, distribuição e medição de visitas vindas de IA; parte técnica do site como proposta) — por quê: pedido do Bruno.
