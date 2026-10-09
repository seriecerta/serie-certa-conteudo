# Agente de Conteúdo Série Certa — Claude Code

Todo dia de manhã o Claude Code cria a pauta, os roteiros, a narração com a voz da MIA, os vídeos, os carrosséis e os Stories. Um revisor independente aprova ou bloqueia cada peça, e o que foi aprovado vai ao ar **sozinho** no Instagram e no YouTube, nos horários do cronograma. Você não copia nem cola nada.

> **Vai usar o Claude Code web (nuvem)?** Siga o guia `nuvem/LEIA-ME-NUVEM.md`. Este README descreve a instalação no computador.

## Como funciona
```
06:40  tarefa "pacote-diario"  →  pauta → roteiro → MP3 (MIA) → vídeo → cards → revisão
                                  → YouTube: sobe e agenda (publishAt nativo do YouTube)
de hora em hora  tarefa "publicar"  →  Instagram: publica o que chegou no horário
```
Travas de segurança (todas em `scripts/publicar.py`):
- Só vai ao ar o que o `revisor` colocou em `saida/<data>/revisao.json` → `aprovadas`.
- `PUBLICACAO_AUTOMATICA=false` no `.env` = só simula. Comece assim.
- Criar o arquivo `saida/<data>/PAUSAR` segura o dia inteiro (dá pra fazer pelo celular se a pasta estiver no Drive/iCloud).
- Cada post sai uma vez só; erro no YouTube não é repetido sozinho (evita vídeo duplicado).
- Se o computador dormiu e o horário do Instagram passou há mais de 4 h, o post é descartado em vez de sair de madrugada.
- Vídeos marcados como conteúdo com IA (`is_ai_generated` no Instagram, `containsSyntheticMedia` no YouTube). Dá pra desligar em `MARCAR_CONTEUDO_IA`.

## Estrutura
```
CLAUDE.md                      regras, produto, vozes, time
estrategia/                    TAM-SAM-SOM, ICP, JTBD, posicionamento, proposta de valor, GTM, voz, pilares, cronograma
.claude/agents/                estrategista, roteirista, desdobrador, revisor
.claude/skills/                /pacote-diario, /publicar, /estrategia
scripts/narrar.py              ElevenLabs (MIA, Ela, Ele)
scripts/montar_video.py        vídeo 9:16 / 16:9 com trilha Sala Escura
scripts/renderizar_cards.py    carrossel e Stories em JPEG
scripts/publicar.py            Instagram + YouTube
scripts/configurar_instagram.py / autorizar_youtube.py   configuração única das contas
.credenciais/                  tokens (fora do Git)
historico/                     publicados e métricas
assets/                        posters/, trilha/, fontes/, templates/card.jpg e story.jpg (fundos com a marca)
```

## Instalação (uma vez)

### 1. Base (~10 min)
1. Ponha a pasta dentro do Google Drive/iCloud (para ver tudo no celular) e abra no **Claude Code Desktop**.
2. Instale Python 3 e ffmpeg (`brew install ffmpeg` no Mac), depois `pip install -r requirements.txt`.
3. `cp .env.example .env` e cole a chave da ElevenLabs.
4. Copie a trilha para `assets/trilha/sala-escura.mp3`, a fonte para `assets/fontes/marca.ttf` e, se quiser, fundos com a marca em `assets/templates/card.jpg` (1080×1350) e `story.jpg` (1080×1920).

### 2. Supabase — hospedagem temporária para o Instagram (~3 min)
O Instagram só aceita mídia por URL pública. O publicador sobe o arquivo no seu Supabase, o Instagram baixa e o arquivo é apagado logo depois.
1. Bucket `conteudo-redes` já criado (público, até 50 MB, só MP4 e JPEG).
2. No `.env`: `SUPABASE_URL` e `SUPABASE_SERVICE_ROLE_KEY` (Project Settings → API).

### 3. Instagram (~15 min)
Requisito: @seriecerta como **conta profissional** (Criador de conteúdo ou Empresa).
1. Em developers.facebook.com: **Criar app → caso de uso "Gerenciar mensagens e conteúdo no Instagram"** (API do Instagram com login do Instagram).
2. Em **Funções do app**, adicione @seriecerta como testador do Instagram e aceite o convite no app do Instagram (Configurações → Apps e sites).
3. Na configuração da API, clique em **Gerar token** para @seriecerta com as permissões `instagram_business_basic` e `instagram_business_content_publish`.
4. Rode `python scripts/configurar_instagram.py SEU_TOKEN`. O token dura 60 dias e o publicador renova sozinho.

Como é um app só para a sua conta, não precisa de revisão da Meta.

### 4. YouTube (~15 min)
1. No console.cloud.google.com: crie um projeto e ative a **YouTube Data API v3**.
2. Em **Tela de consentimento OAuth**: tipo Externo, adicione seu e-mail e clique em **Publicar app (Em produção)**. Se ficar em "Teste", o acesso expira em 7 dias e a automação para.
3. Em **Credenciais → Criar ID do cliente OAuth → App para computador**. Baixe o JSON como `.credenciais/youtube-client.json`.
4. Rode `python scripts/autorizar_youtube.py` e entre com a conta do canal. O Google vai avisar "app não verificado"; é o seu próprio app, então clique em Avançado → Continuar.

### 5. Teste e liga
1. Rode `/estrategia` (preenche TAM/SAM/SOM e faz até 5 perguntas).
2. Rode `/pacote-diario` com `PUBLICACAO_AUTOMATICA=false` e aprove as permissões com "sempre permitir". Confira `saida/<data>/` e a simulação no fim.
3. Gostou? Troque para `PUBLICACAO_AUTOMATICA=true`.

### 6. As duas tarefas agendadas (Claude Code Desktop → Code → Routines → New routine → Local)
| Nome | Agenda | Instrução |
|---|---|---|
| `pacote-diario-serie-certa` | Daily, 6:40 | `Rode /pacote-diario para hoje.` |
| `publicar-serie-certa` | Hourly | `Rode /publicar.` |

Ligue **Keep computer awake** em Configurações → Desktop app → General. Clique **Run now** em cada uma na primeira vez e marque "sempre permitir".

## Sua rotina
- **Diária: nenhuma.** Se quiser, abra `saida/<data>/README.md` (o que vai ao ar) e `publicacao.log.md` (os links do que saiu).
- **Segunda**: cole os números em `historico/metricas.md` e rode `/estrategia`.
- **Até quarta**: coloque os pôsteres do vídeo longo em `assets/posters/`.
- **Emergência**: crie `saida/<data>/PAUSAR`.

## Limites das plataformas
- **Stories pela API saem sem stickers** (enquete, link, caixinha). O CTA vai escrito na arte, apontando para o link da bio. Stories com sticker continuam manuais, se você quiser.
- **TikTok** não está no publicador. A legenda fica pronta em `tiktok.txt`.
- **Música do Instagram/YouTube** não entra por API. Por isso a trilha é a Sala Escura, embutida no vídeo.
- **Thumbnail personalizada** no YouTube exige canal verificado por telefone. Sem isso, o vídeo sobe sem ela.
- O Instagram limita posts por API a um teto por 24 h (100 segundo a documentação atual; a seção de carrossel cita 50). O cronograma usa bem menos.
