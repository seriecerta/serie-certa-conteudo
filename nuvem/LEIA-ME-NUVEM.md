# Rodando no Claude Code web (nuvem)

Tudo roda na nuvem da Anthropic, **com o computador desligado**. Você acompanha e conversa por claude.ai/code, inclusive no celular (aba Code do app Claude).

## Como as peças se encaixam
| O quê | Onde fica |
|---|---|
| Código, estratégia, roteiros, histórico | Repositório privado no GitHub (cada execução clona do zero) |
| Vídeos, áudios, cards e estado das publicações | Supabase, bucket privado `pacotes-redes` (já criado) |
| Tokens do Instagram e do YouTube | Supabase, bucket privado `credenciais-redes` (já criado) |
| Mídia temporária para o Instagram baixar | Supabase, bucket público `conteudo-redes` (já criado; apagada após cada post) |
| Chaves da ElevenLabs e do Supabase | Ambiente de nuvem do Claude Code (API credentials) |

Os scripts detectam sozinhos que estão na nuvem e fazem o vaivém com o Supabase.

---

## Passo 1 — Subir o kit para o GitHub (~10 min)
O jeito mais fácil, sem terminal, é o **GitHub Desktop** (desktop.github.com):
1. Instale e entre com a conta `seriecerta` do GitHub.
2. **File → Add local repository** → escolha a pasta `serie-certa-conteudo`. Ele vai dizer que não é um repositório: clique em **create a repository** → **Create repository**.
3. Clique em **Publish repository**, deixe **Keep this code private** marcado → **Publish**.

Antes de publicar, coloque na pasta (vão junto para o GitHub):
- `assets/trilha/sala-escura.mp3`, `assets/fontes/marca.ttf` e, se tiver, `assets/templates/card.jpg` e `story.jpg`.

O `.gitignore` já impede que `.env`, `.credenciais/` e vídeos subam.

## Passo 2 — Conectar o GitHub ao Claude Code web (~3 min)
1. Acesse **claude.ai/code**.
2. Siga o onboarding e **autorize o app Claude do GitHub** no repositório `serie-certa-conteudo` (pode escolher "Only select repositories").

## Passo 3 — Criar o ambiente de nuvem (~10 min)
Em claude.ai/code, no seletor de ambiente (ícone de nuvem), crie um ambiente novo chamado `serie-certa`:

1. **Network access → Custom**. Em **Allowed domains**, cole o conteúdo de `nuvem/dominios-permitidos.txt` e marque **Also include default list of common package managers**.
2. **Environment variables**: cole as linhas sem `#` de `nuvem/variaveis-ambiente.txt`.
3. **Setup script**: cole o conteúdo de `nuvem/setup.sh`.
4. Salve. Depois **edite o ambiente de novo** e, em **API credentials** (aparece ao editar, nos planos Pro/Max), adicione:

| Credencial | Host | Header | Prefixo | Valor |
|---|---|---|---|---|
| ElevenLabs | `api.elevenlabs.io` | `xi-api-key` | (vazio) | sua chave da ElevenLabs |
| Supabase | `idbwkhutuomakeptnyia.supabase.co` | `Authorization` | `Bearer` | service role key |
| | | `apikey` (2ª linha de header) | (vazio) | a mesma service role key |

As API credentials ficam fora da máquina da sessão: o Claude usa, mas não consegue ler. Se o seu plano não mostrar essa seção, ponha as duas chaves em **Environment variables** (`ELEVENLABS_API_KEY=` e `SUPABASE_SERVICE_ROLE_KEY=`).

## Passo 4 — Configurar as contas (uma sessão, ~15 min)
Abra uma **nova sessão** em claude.ai/code, com o repositório `serie-certa-conteudo` e o ambiente `serie-certa`.

**YouTube** — antes, envie o JSON do cliente OAuth do Google pelo painel do Supabase: **Storage → `credenciais-redes` → Upload file**, com o nome exato `youtube-client.json`. Depois peça na sessão:
> Rode `python scripts/autorizar_youtube.py --link` e me mostre o link.

Abra o link, entre com a conta do canal e autorize. O navegador vai cair numa página de erro em `http://localhost` (é esperado). Copie o endereço inteiro da barra e mande na sessão:
> Rode `python scripts/autorizar_youtube.py --concluir "COLE_O_ENDEREÇO"`

**Instagram** — peça:
> Rode `python scripts/configurar_instagram.py COLE_O_TOKEN`

O token vai aparecer no histórico dessa sessão. Quando terminar, arquive-a (ou apague) em claude.ai/code. Os tokens ficam guardados no bucket privado e o publicador renova o do Instagram sozinho.

## Passo 5 — Primeiro teste
Na mesma sessão, ou numa nova:
> Rode /estrategia

Responda às perguntas. Depois:
> Rode /pacote-diario

Confira o resumo final. Os vídeos ficam no Supabase (**Storage → `pacotes-redes` → data de hoje**); dá para abrir e assistir pelo painel. Com `PUBLICACAO_AUTOMATICA=false`, nada vai ao ar: ele só mostra a simulação.

Gostou? Edite o ambiente e troque para `PUBLICACAO_AUTOMATICA=true`.

## Passo 6 — Rotinas: só o que precisa de IA fica no Claude
A publicação não precisa de IA: é rodar dois scripts no horário. Por isso ela roda no **GitHub Actions** (`.github/workflows/publicar.yml`), que é grátis e **não gasta o limite do plano** do Claude. No Claude ficam só as rotinas que criam ou analisam conteúdo.

| Rotina | Onde roda | Agenda |
|---|---|---|
| Pacote diário (`/pacote-diario`) | Claude, sessão nova a cada dia | 6h41 |
| Painel (métricas) | Claude | 9h |
| Revisão semanal | Claude | quarta, 18h17 |
| **Publicar** (Instagram, YouTube e blog) | **GitHub Actions, sem Claude** | de hora em hora das 9h02 às 22h02 + 13h32 e 18h32 |

### Ligar o GitHub Actions (uma vez, ~3 min)
1. O arquivo `.github/workflows/publicar.yml` precisa estar na branch **main** (o GitHub só roda agendamentos da main).
2. No GitHub: **Settings → Secrets and variables → Actions**.
   - Aba **Secrets** → **New repository secret**: nome `SUPABASE_SERVICE_ROLE_KEY`, valor = a service role key do Supabase. (Secret fica cifrado; não aparece nos logs nem para quem vê o repositório.)
   - Aba **Variables** → **New repository variable**: nome `PUBLICACAO_AUTOMATICA`, valor `true`.
3. Teste: aba **Actions** → `publicar` → **Run workflow**, deixando "Só simular" marcado. O resumo mostra o que sairia.
4. Deu certo? **Desative as rotinas antigas de publicação** em claude.ai/code/routines ("Série Certa · publicar (fila do dia)", "publicar (horários e meia)" e "publicar blog"). Elas e o Actions juntos podem postar em dobro.

Para pausar tudo: troque a variável `PUBLICACAO_AUTOMATICA` para `false` (só simula), ou use o `PAUSAR` do dia como antes.

Em **Connectors** de cada rotina do Claude, **remova todos**: o kit não precisa deles, e assim a rotina não tem acesso ao que não deve.

## No dia a dia
- **Ver o que saiu**: `pacotes-redes/<data>/…/publicacao.log.md` no Supabase, ou pergunte numa sessão: "o que foi publicado hoje?"
- **Pausar o dia pelo celular**: no painel do Supabase, envie um arquivo qualquer com o nome `PAUSAR` para `pacotes-redes/<data>/`.
- **Mudar estratégia, voz, horários**: abra uma sessão e peça. Ele edita e faz push na main, e vale a partir da próxima rotina.
- **Segunda**: abra uma sessão, cole os números da semana e peça `/estrategia`.
- **Uma rotina falhou?** Em claude.ai/code/routines, abra a execução e leia o que aconteceu. "Verde" só significa que a sessão rodou; confira o resumo. Erro `403 host_not_allowed` = falta liberar um domínio no ambiente.

## Limites deste modo
- Arquivos acima do limite de upload do seu projeto Supabase (50 MB no plano gratuito) não são guardados no pacote. Isso só afeta o vídeo longo, que já sobe direto para o YouTube na rotina da manhã.
- Rotinas são *research preview* na Anthropic: o comportamento pode mudar. As execuções contam no seu limite de uso do plano (por isso a publicação foi para o GitHub Actions).
- O GitHub desliga agendamentos de repositório **público** depois de 60 dias sem nenhum commit. O commit diário do pacote evita isso; se a fila parar, reative em Actions → `publicar` → **Enable workflow**.
- Rodadas agendadas do GitHub podem atrasar alguns minutos (às vezes mais em horário de pico). O Instagram só descarta um post depois de 4 h de atraso.
