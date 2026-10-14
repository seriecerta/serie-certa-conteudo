# Aprendizados — retroalimentação das sessões

Fricções reais que custaram tempo e podem voltar. Leia antes de mexer em scripts, motor, publicação ou configuração.
Regras de como registrar: seção "Fechamento de sessão" do `CLAUDE.md`.
Formato: **sintoma → causa → como resolver/evitar → onde mexer**. Mais recente no topo.

## Painel e ferramentas

### 2026-10-13 — Texto de rotina só muda de dentro da própria sessão
- **Sintoma:** `update_trigger: a routine's instructions (its prompt) can be changed only from the conversation or thread the routine posts into`.
- **Causa:** o prompt de uma rotina presa a uma sessão fixa (`persistent_session_id`) só pode ser editado por essa sessão. Nome, horário e liga/desliga podem ser mudados de qualquer sessão.
- **Como evitar:** escreva o prompt das rotinas como "siga o skill X" e ponha os passos no `SKILL.md`, que muda por commit. Para mudar o texto da rotina, peça na sessão dela (ex.: "Série Certa · painel (métricas)").
- **Onde mexer:** `.claude/skills/<skill>/SKILL.md`.

### 2026-10-13 — Script novo não pode ir para `scripts/`
- **Sintoma:** `Write` em `scripts/painel.py` falhou com "File is in a directory that is denied by your permission settings".
- **Causa:** `.claude/settings.json` nega `Edit(scripts/**)` e `Write(scripts/**)` de propósito, para proteger as travas do publicador.
- **Como resolver:** ferramenta nova e só de leitura vive na própria pasta (ex.: `painel/painel.py`, que importa `scripts/nuvem.py` sem alterá-lo). Não contorne o bloqueio com `sed`/`cat >` via Bash.
- **Onde mexer:** `painel/`, permissões em `.claude/settings.json`.

### 2026-10-13 — Playwright do `pip` não acha o Chromium da nuvem
- **Sintoma:** `BrowserType.launch: Executable doesn't exist at /opt/pw-browsers/chromium_headless_shell-1243/...` e o aviso para rodar `playwright install`.
- **Causa:** a versão do pacote `playwright` instalada pelo pip pede uma revisão do navegador diferente da que vem pré-instalada em `/opt/pw-browsers`.
- **Como resolver:** não rode `playwright install`. Lance com `chromium.launch(executable_path="/opt/pw-browsers/chromium")`.
- **Para o `scripts/renderizar.py`:** instale `pip install -q "playwright==1.56.0"` (casa com o Chromium de `/opt/pw-browsers`). Um `pip install playwright` sem versão quebra o renderizador com a mesma mensagem.
- **Onde mexer:** scripts de captura/teste que você escrever.

## Publicação

### 2026-10-14 — Sem crédito na ElevenLabs a peça não precisa ficar bloqueada
- **Sintoma:** Reels do dia bloqueado no `revisao.json` com "créditos ElevenLabs esgotados: 157 de 254 necessários"; sem `narracao.mp3` o roteirista não tinha como escrever a cena (toda sincronizada com `@palavra`).
- **Causa:** o fluxo supunha que todo vídeo tem voz. O `renderizar.py`, porém, já monta vídeo só com trilha e efeitos quando não há `narracao*.mp3`, desde que o `<body>` tenha `data-duracao` e a cena use tempos em segundos.
- **Como resolver:** regra "Sem crédito de voz" do `CLAUDE.md` (decisão do Bruno): refazer a peça com o texto na tela contando tudo e passar pelo revisor normalmente. Exemplo pronto: `saida/2026-10-14/04-reels-qual-quarta-e-voce/` (cena gerada com tempos fixos, 7,4 s por tipo).
- **Armadilha:** deixar o `narracao.txt` na pasta faz o `narrar.py` gerar um áudio que não casa com a cena quando o crédito voltar. Renomeie para `fala-original-sem-uso.txt`.
- **Pegar só uma pasta da nuvem:** pôsteres e vídeos não vão para o git. Para trabalhar numa peça sem o `baixar-pacote` sobrescrever o resto do dia, use `nuvem.baixar(nuvem.B_PACOTE, "<data>/<peça>/imagens/x.jpg", pathlib.Path("saida")/...)` e suba de volta só os arquivos mexidos com `nuvem.subir(...)`. O bucket não apaga arquivo renomeado localmente (o `narracao.txt` antigo continua lá).

### 2026-10-13 — `publicar.py --simular` não valida post do Instagram antes do horário
- **Sintoma:** a simulação não acusa nada numa peça que vai ser recusada (ex.: sem o campo `"series"`), e o erro só aparece no log depois do horário marcado.
- **Causa:** o `processar_dia` pula publicações do Instagram com `quando` no futuro antes de chamar `validar()`.
- **Como conferir antes:** `python3 -B -c "import sys,json,pathlib; sys.path.insert(0,'scripts'); import publicar; p=pathlib.Path('saida/<data>/<peça>'); [print(x['id'], publicar.validar(x, p) or 'OK') for x in json.loads((p/'publicar.json').read_text())['publicacoes']]"` (o `-B` evita gravar `__pycache__` em `scripts/`).
- **Onde mexer:** nada no script; use o comando acima ao corrigir uma peça.

### 2026-10-13 — `publicar.py --simular` sobrescreve o pacote local com o da nuvem
- **Sintoma:** depois de corrigir `publicar.json` e renderizar `quadros/` de novo, a simulação continuou acusando o erro antigo (`falta o campo "series"`) e as edições locais sumiram.
- **Causa:** na nuvem, o `publicar.py` (mesmo com `--simular`) chama `nuvem.baixar_pacote()` antes de validar, e o download sobrescreve os arquivos locais.
- **Como evitar:** depois de qualquer correção, rode `python scripts/nuvem.py subir-pacote <data>` **antes** de simular ou publicar.
- **Onde mexer:** `scripts/publicar.py` (`main`) e `scripts/nuvem.py`.
- **Vale também para o painel:** `python painel/painel.py` na nuvem baixa os `.md`/`.json` de todos os dias e sobrescreve os locais. Antes de commitar depois de rodar o painel, confira `git status` e não suba arquivos de `saida/` que você não editou (`git checkout -- <arquivo>`).

### 2026-10-13 — Pacote gerado antes da trava do pôster é recusado
- **Sintoma:** `✗ .../ig-carrossel: falta o campo "series" no publicar.json`.
- **Causa:** o pacote foi montado num branch atrás do `main`; a rotina de hora em hora já usa o `publicar.py` novo.
- **Como resolver:** `scripts/posters.py <pasta> "Série (ano)" ...`, colocar `<div class="capa"><img src="imagens/...">` na cena, renderizar, preencher `"series"` e passar pelo revisor. Ver também "Branch de trabalho atrás do main".

### 2026-10-13 — Instagram responde `API access blocked` (OAuthException, code 200)
- **Sintoma:** `Instagram 400: {"error":{"message":"API access blocked.","type":"OAuthException","code":200}}` na 1ª tentativa do carrossel (~16h); a mesma peça publicou ~50 min depois sem mudar nada.
- **Causa:** bloqueio passageiro do lado da Meta. Não era token (válido), convite de testador (aceito em 9/10), app em Desenvolvimento, marcação de IA nem a URL do Supabase — tudo isso foi testado e funcionou.
- **Como diagnosticar sem gastar tentativa:** `GET graph.instagram.com/v25.0/me` (lê a conta) e `POST /<ig_user_id>/media` com uma `image_url` pública (cria rascunho que não vai ao ar e expira em 24 h). Se ambos dão 200, só tente de novo.
- **Atenção:** cada peça do Instagram tem só 2 tentativas no `publicar.py`; não gaste a segunda antes desse teste.

## Git e branches

### 2026-10-13 — Branch de trabalho atrás do `main` depois do merge
- **Sintoma:** o branch `claude/...` estava "em dia com o remoto", mas o `main` tinha 3 commits a mais (Lista da MIA, trava do pôster oficial, permissões do kit). Um pacote gerado ali sairia sem a trava do pôster.
- **Causa:** o PR do branch já tinha sido mergeado e o `main` andou depois; "sincronizado com origin/<branch>" não quer dizer "sincronizado com o main".
- **Como evitar:** no início da sessão, `git fetch origin main` e compare `git log --oneline HEAD..origin/main`. Se o branch não tiver commits fora do `main`, atualize com `git merge --ff-only origin/main`.
- **Armadilha:** `git checkout -B <branch> origin/main` é bloqueado pelo modo automático como ação destrutiva, mesmo com o branch limpo. Use o `merge --ff-only`, que faz o mesmo sem reescrever nada.
