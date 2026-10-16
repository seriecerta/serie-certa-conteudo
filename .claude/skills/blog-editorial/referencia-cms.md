# Blog Série Certa — seriecerta.online/blog

Portal editorial do Série Certa: aquisição orgânica, relacionamento (newsletter), retenção (áudio, salvos) e monetização (publicidade própria e de parceiros), com CMS próprio em `/dashboard/blog`.

## 1. Diagnóstico da arquitetura encontrada

- **Stack:** Next.js 16 (App Router, sem Cache Components) + TypeScript, Supabase (Postgres + Auth + Storage, região São Paulo), Netlify, Sentry, PostHog (sem cookies), Resend, Claude API.
- **Identidade:** sistema "Sala Escura" já centralizado em `lib/sc-design.ts`, `app/globals.css` e `app/components/sc/primitives.tsx` (fontes Bricolage Grotesque, Instrument Serif e DM Mono; Brasa `#FF5A36`; 8 pigmentos de humor). O blog **estende** esses tokens — nenhuma cor ou fonte nova.
- **Acesso interno:** o painel `/dashboard` libera só as contas de `DASHBOARD_ADMIN_IDS`. O CMS reaproveita essa regra e soma papéis por pessoa.
- **Não existia:** blog, sitemap, robots, RSS, CMS, armazenamento de mídia editorial.

## 2. Decisões de UX/UI

- **Revista dentro do produto:** mesmo topo, mesma atmosfera e grão do app, com selo "Blog" e uma faixa de categorias logo abaixo (navegação por assunto em 1 toque, também no celular).
- **Home em camadas:** apresentação curta + busca grande → destaque + "Mais lidas" → últimas (com "Carregar mais") → em alta → navegação por assunto (blocos coloridos com os glifos dos humores) → ouça → assista → blocos por categoria → newsletter → chamada para o app.
- **Capas gráficas:** sem imagem, a matéria ganha uma capa gerativa na cor e no glifo do humor escolhido. Evita banco de imagens genérico e risco de direitos autorais.
- **Leitura:** coluna de ~68 caracteres, 18,5 px, contraste alto, índice lateral fixo (no celular, recolhível), barra de progresso, A−/A+, salvamento do ponto do áudio no aparelho.
- **Áudio que acompanha a navegação:** o tocador vive no layout do blog e continua tocando ao trocar de matéria (±15 s, 0,75×–2×, volume, controles da tela de bloqueio).
- **Honestidade nos rankings:** "Mais lidas" só vira ranking com 50+ leituras no período; antes disso aparece "Escolhas da redação", identificado. "Em alta" só aparece quando há aceleração real.
- **Publicidade sem buraco:** posição desligada ou sem campanha não ocupa espaço; todo anúncio tem rótulo; nada de pop-up ou intersticial.

## 3. Rotas

| Rota | O que é | Renderização |
| --- | --- | --- |
| `/blog` | Home editorial | Estática com revalidação a cada 5 min (ISR) + na hora ao publicar |
| `/blog/[slug]` | Matéria | ISR sob demanda; 301 automático quando o slug muda |
| `/blog/categoria/[slug]?pagina=N` | Categoria | Servidor (paginação rastreável) |
| `/blog/tag/[slug]` | Tag (noindex com < 2 matérias) | Servidor |
| `/blog/autor/[slug]` | Autor | Servidor |
| `/blog/busca?q=&categoria=&formato=` | Busca (noindex) | Servidor |
| `/blog/salvos` | Matérias salvas (precisa de conta) | Navegador |
| `/blog/newsletter?acao=confirmar|sair&t=` | Confirmação/descadastro (com clique) | — |
| `/blog/politica-editorial`, `/blog/anuncie` | Institucionais | Estática |
| `/blog/rss.xml` | RSS 2.0 | ISR 10 min |
| `/sitemap.xml`, `/robots.txt` | SEO técnico (site inteiro) | ISR 1 h |
| `/dashboard/blog` e `/dashboard/blog/editor?id=` | CMS | Navegador (APIs protegidas) |

Slugs reservados (nenhuma matéria pode usá-los): `categoria, tag, autor, busca, rss, feed, newsletter, salvos, politica-editorial, anuncie, admin, pagina, api`.

APIs públicas: `/api/blog/sugestoes`, `/api/blog/recentes`, `/api/blog/newsletter`, `/api/blog/salvos`, `/api/blog/anuncio/[id]` (clique), `/api/blog/og/[slug]` (imagem de compartilhamento).
APIs do CMS (todas exigem login + papel): `/api/blog/admin/{painel, materias, materias/[id], taxonomia, anuncios, midias, audio, assistente, distribuicao, verificar, newsletter, equipe}`.

## 4. Componentes (`app/blog/_c/`)

`Moldura` (CabecalhoBlog, RodapeBlog) · `Topo` (CampoBusca com sugestões, MenuMobile, BotaoConta, FaixaCategorias) · `Cards` (CardGrade, CardMini, CardDestaque, SeloFormato, RotuloCategoria, SeloPatrocinado) · `Capa` · `Blocos` (renderizador seguro) · `Leitura` (BarraProgresso, RegistroLeitura, IndiceAtivo, AcoesMateria) · `Midia` (ProvedorAudio + mini player, BotaoOuvir, VideoYoutube com carregamento sob clique, VideoArquivo) · `Anuncio` + `VistaAnuncio` · `Newsletter` · `Listas` (MaisLidas, CarregarMais) · `Comum` (TituloSecao, Paginacao, Vazio, JsonLd, ChamadaApp) · `Arquivo` · `Medidor`.

Núcleo em `lib/blog/`: `conteudo.ts` (blocos, formatação segura, slug, índice, importação de Markdown — puro e testado), `dados.ts` (leitura pública), `salvar.ts` (regras editoriais), `admin.ts` + `papeis.ts` (acesso), `voz.ts` (narração), `newsletter.ts`, `site.ts`, `tipos.ts`.

## 5. O que está funcionando (depois da migração aplicada)

- Home, matéria, categoria, tag, autor, busca (sem acento, por prefixo, com filtros), 404, salvos, RSS, sitemap, robots.
- CMS: criar/editar em blocos, colar Markdown, prévia desktop/celular, estados (rascunho → revisão → aprovado → agendado/publicado → arquivado) com permissões por papel, agendamento (o job do banco publica sozinho), duplicar, apagar rascunho, histórico, conflito de edição simultânea, checklist SEO/acessibilidade, verificação de links quebrados e títulos parecidos, categorias/tags/autores (com ordem), biblioteca de mídia com envio direto ao Storage.
- Multimídia: vídeo do YouTube (sem cookies até o clique) ou arquivo próprio com legendas e transcrição; áudio enviado ou **gerado com a voz da MIA** (ElevenLabs), em partes, com transcrição automática; spoilers ficam fora da narração.
- Publicidade: 13 posições ligáveis uma a uma, campanhas com período, prioridade, aparelhos e rótulo; impressões (≥50% visível por 1 s) e cliques contados por dia no banco.
- Newsletter: inscrição com consentimento explícito e prova (texto + data), confirmação dupla, descadastro em 1 clique, envio de matéria para assinantes com teste prévio e List-Unsubscribe.
- IA editorial (Claude Sonnet): títulos, resumo/meta/título SEO, estrutura H2/H3, palavras-chave, links internos (só da lista real de matérias), o que verificar, revisão de texto, adaptação para newsletter/Instagram/TikTok/YouTube/WhatsApp/roteiros — sempre sugestão, nunca publicação automática.
- SEO: metadados por página, canonical, Open Graph com imagem gerada, `BlogPosting` + `BreadcrumbList` + `VideoObject` (só com os campos exigidos) + `Blog`/`WebSite` com busca, `CollectionPage`, `Person`/`Organization` nos autores.
- Analytics (PostHog, sem dado pessoal e sem o termo buscado): `blog_home_view, article_view, article_scroll_50/90, audio_play/complete, video_play/complete, article_share, article_save, blog_search, category_click, related_article_click, newsletter_signup, platform_cta_click, ad_impression, ad_click`.

## 6. Modelo de dados

Migração: `supabase/migrations/20261014200000_blog_editorial.sql` (só cria coisas novas com prefixo `blog_`).
Tabelas: `blog_categorias, blog_tags, blog_autores, blog_materias, blog_materia_tags, blog_midias, blog_redirecionamentos, blog_visualizacoes, blog_anuncio_posicoes, blog_anuncio_campanhas, blog_anuncio_metricas, blog_newsletter, blog_newsletter_envios, blog_equipe, blog_auditoria, blog_distribuicao, blog_salvos`.
Funções: `blog_buscar, blog_mais_lidas, blog_em_alta, blog_total_visualizacoes, blog_registrar_visualizacao, blog_anuncios_ativos, blog_registrar_anuncio` + gatilhos de busca e de formato. Job `blog-publicar-agendadas` (pg_cron, 5 min). Bucket público `blog` (envio só por URL assinada).
RLS: o público só lê o que está no ar; todo o resto passa pelas APIs com chave de serviço.

Conteúdo inicial: `supabase/seed/blog_conteudo_inicial.sql` — 4 matérias perenes publicadas e "7 séries para assistir com sono" **em revisão** (dados de disponibilidade/nota da pesquisa de 05/out; conferir antes de publicar).

## 7. Integrações e pendências

| Integração | Situação |
| --- | --- |
| Supabase (banco, Storage) | Pronta no código; **aplicar a migração e o seed** |
| Resend (newsletter) | Usa a `RESEND_API_KEY` já existente; remetente `newsletter@seriecerta.online` (domínio já verificado) |
| Claude (assistente) | Usa a `ANTHROPIC_API_KEY` já existente |
| ElevenLabs (voz da MIA) | **Pendente:** `ELEVENLABS_API_KEY` e `ELEVENLABS_VOZ_ID` no Netlify |
| PostHog | Eventos novos no catálogo; criar insights do blog no projeto 640256 |
| Google Search Console | **Pendente:** verificar o domínio e enviar `/sitemap.xml` |
| Google AdSense / Ad Manager | **Não instalado de propósito:** exige conta aprovada e banner de consentimento (LGPD) antes de qualquer script. As posições já existem. |
| Instagram, TikTok, YouTube, WhatsApp | **Pendente:** publicação automática depende das credenciais das redes. Hoje: textos por canal gerados, revisados e aprovados no CMS; o RSS serve de fonte para o agente `serie-certa-conteudo`. |
| Envio de newsletter acima de 400 pessoas | Migrar para Broadcasts da Resend (segmento + contatos) |

## 8. Testes executados

- `npm test` — 15 testes do modelo de conteúdo (XSS em links, URLs de mídia, normalização, âncoras, índice, importação de Markdown e tabelas, YouTube).
- `tsc --noEmit` e `eslint` sem erros.
- `next build` completo (37 páginas).
- Navegador (Chromium) contra um banco simulado com o conteúdo inicial: todas as rotas 200 (404 onde deve), desktop 1366 px e celular 390 px sem rolagem horizontal, tocador persistente entre matérias, A−/A+, sugestões de busca, zero erro no console.
- **Não testado aqui:** APIs do CMS contra o banco real (dependem da migração e da chave de serviço) e envio real de e-mail/voz.

## 9. Problemas conhecidos

- Leitura conta 1 por sessão por matéria após 4 s; robôs que executam JavaScript podem inflar levemente.
- "Mais lidas" de 24 h usa o dia de São Paulo (de 00:00 até agora), não 24 horas corridas.
- Galeria e imagens do corpo usam `<img>` com carregamento preguiçoso (a capa usa a otimização do Next).

## 10. Rodar localmente

```bash
npm ci
# .env.local com NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY,
# DASHBOARD_ADMIN_IDS (seu id) e, se quiser testar, RESEND_API_KEY, ANTHROPIC_API_KEY, ELEVENLABS_*
npm run dev        # http://localhost:3000/blog  ·  CMS: /dashboard/blog
npm test
```

## 11. Publicar em produção

1. Aplicar `supabase/migrations/20261014200000_blog_editorial.sql` e depois `supabase/seed/blog_conteudo_inicial.sql`.
2. No Netlify: `ELEVENLABS_API_KEY`, `ELEVENLABS_VOZ_ID` (voz "MIA – Série Certa"), opcional `NEWSLETTER_REMETENTE`.
3. Merge na `main` (deploy automático).
4. Search Console: enviar `https://seriecerta.online/sitemap.xml`.
5. No CMS: revisar e publicar "7 séries para assistir com sono".

## 12. Variáveis de ambiente

Já existentes e usadas: `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `DASHBOARD_ADMIN_IDS`, `ANTHROPIC_API_KEY`, `RESEND_API_KEY`, `NEXT_PUBLIC_APP_URL`, `NEXT_PUBLIC_POSTHOG_KEY`.
Novas: `ELEVENLABS_API_KEY`, `ELEVENLABS_VOZ_ID`, `ELEVENLABS_MODELO` (opcional, padrão `eleven_multilingual_v2`), `NEWSLETTER_REMETENTE` (opcional).

## 13. Evolução depois do MVP

1. Páginas-pilar por humor ("séries para quando você está ansioso") ligadas ao link profundo `/descobrir?humor=` — o cluster de SEO mais alinhado ao produto.
2. Bloco "ficha da série" no editor puxando TVmaze + disponibilidade (tempo de maratona automático, sem digitação).
3. Publicação automática nas redes via o agente `serie-certa-conteudo`, lendo o RSS e os textos aprovados.
4. Banner de consentimento + AdSense/Ad Manager quando houver tráfego que justifique.
5. Broadcasts da Resend e newsletter semanal automática ("o que assistir no fim de semana").
6. Recomendações de matérias pelo histórico de humor de quem está logado (com consentimento).
