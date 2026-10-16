# Aprendizados — retroalimentação das sessões

Fricções reais que custaram tempo e podem voltar. Leia antes de mexer em scripts, motor, publicação ou configuração.
Regras de como registrar: seção "Fechamento de sessão" do `CLAUDE.md`.
Formato: **sintoma → causa → como resolver/evitar → onde mexer**. Mais recente no topo.

## Blog

### 2026-10-16 — Publicar no blog sem a senha do painel
- **Sintoma:** o pedido veio com login e senha do `/dashboard/blog`. Este repositório é **público** no GitHub, então qualquer senha ou token gravado aqui vaza.
- **Causa:** o CMS autentica pela sessão do Supabase Auth, mas o blog grava nas tabelas `blog_*` do **mesmo** Supabase que as redes já usam (`idbwkhutuomakeptnyia`).
- **Como resolver:** o `blog/publicar_blog.py` grava direto nas tabelas com a `SUPABASE_SERVICE_ROLE_KEY` que já está no ambiente, sobe as imagens no bucket público `blog` e repete as regras do CMS (`lib/blog/salvar.ts` e `conteudo.ts` do repositório `seriecerta/serie-certa`). Nunca grave senha no repositório nem em `saida/`.
- **Efeito colateral:** gravando pelo banco, o `revalidatePath` do CMS não roda. A home e a matéria aparecem pelo ISR em até 5 min e o sitemap em até 1 h. Se precisar na hora, abra e salve a matéria no painel.
- **Onde mexer:** `blog/publicar_blog.py` (protegido em `.claude/settings.json`, como `scripts/`). Se o CMS mudar o formato dos blocos, atualize `ler_materia()`/`normalizar()`.

### 2026-10-16 — Redatores não conseguem abrir o JustWatch nem a Netflix
- **Sintoma:** WebFetch com `ENOTFOUND`/403 do proxy em `justwatch.com`, `netflix.com`, `omelete.com.br` e outros. Toda checagem de "onde assistir" ficou só no resumo da busca, e o revisor teve de cortar séries que não confirmou.
- **Causa:** a rede do ambiente de nuvem é "Custom" e libera só os domínios de `nuvem/dominios-permitidos.txt`.
- **Como resolver:** o Bruno precisa acrescentar no ambiente `serie-certa` (Network access → Allowed domains) as linhas novas de `nuvem/dominios-permitidos.txt` (JustWatch e Netflix). Até lá, série sem confirmação em 2 fontes recentes fica fora da matéria.
- **Onde mexer:** configuração do ambiente em claude.ai/code; `nuvem/dominios-permitidos.txt`.

## Narração e motor

### 2026-10-15 — Créditos da ElevenLabs acabam no meio do pacote
- **Sintoma:** `Erro ElevenLabs 401 ... "code":"quota_exceeded","message":"This request exceeds your quota of 38518. You have 29 credits remaining, while 664 credits are required"`. Em 14/10 caiu o Reels das 19h; em 15/10 caíram a Lista da MIA, o Reels das 18h30 e o Short das 19h; em 16/10 nenhum vídeo saiu (29 créditos, nem a 1ª fala de 34 passou). A cota não reinicia sozinha no meio do ciclo: até a recarga, a pauta deve prever só carrossel + Stories e deixar os roteiros de vídeo prontos.
- **Causa:** a cota mensal da conta (38.518 créditos) acabou. Na grade diária, cerca de 3 mil caracteres de narração por dia (1 crédito por caractere) estouram a cota antes do fim do ciclo.
- **Como evitar:** a pauta ordena as peças de vídeo por prioridade. Narre uma pasta por vez, nessa ordem (`python scripts/narrar.py saida/<data>/<pasta>`), e pare no primeiro `quota_exceeded`, sem repetir. Carrossel e Stories não gastam crédito e saem de qualquer jeito. A solução de verdade é o Bruno ampliar o plano ou recarregar.
- **Onde mexer:** plano da conta ElevenLabs; prioridade na `00-pauta.md`.

### 2026-10-15 — `.esp-s/.esp-m/.esp-g` empilham os elementos da cena
- **Sintoma:** texto e emoji sobrepostos na prévia da cena.
- **Causa:** `.esp-*` são blocos espaçadores de altura fixa, não margens. Usados como classe em texto ou emoji, achatam o elemento.
- **Como evitar:** use `.esp-*` só como `<div>` vazio entre elementos, ou dê `gap` à seção.
- **Onde mexer:** `motor/COMPONENTES.md` (linha "Estrutura") e `cena.html`.

## Painel e ferramentas

### 2026-10-16 — Painel com rolagem lateral no celular
- **Sintoma:** em 390 px o painel inteiro ficava com 510 px de largura e rolava para o lado.
- **Causa:** duas coisas juntas. (1) O `ler_pauta()` lia linhas com vários campos (`- **Pilar:** 1 · **Job:** principal · **Humor:** vários.`) como um campo só, e o filtro "Pilar" ganhava uma opção enorme. (2) A grade `.wrap` não tinha `grid-template-columns: minmax(0, 1fr)`, então o conteúdo mais largo esticava a coluna. Um `max-width` em `%` no `<select>` não adianta: no cálculo de largura mínima o Chrome ignora o percentual.
- **Como evitar:** a pauta pode continuar com vários campos por linha (o painel separa no ` · **`). Em layout novo do painel, grade com `minmax(0, 1fr)` e limites em px. Para conferir: abra `painel/index.html` em 320–430 px e compare `document.documentElement.scrollWidth` com a largura da tela.
- **Onde mexer:** `painel/painel.py` (`ler_pauta`), `painel/modelo.html` (CSS de `.wrap` e `.filtros`).

### 2026-10-13 — Texto de rotina só muda de dentro da própria sessão
- **Sintoma:** `update_trigger: a routine's instructions (its prompt) can be changed only from the conversation or thread the routine posts into`.
- **Causa:** o prompt de uma rotina presa a uma sessão fixa (`persistent_session_id`) só pode ser editado por essa sessão. Nome, horário e liga/desliga podem ser mudados de qualquer sessão.
- **Como evitar:** escreva o prompt das rotinas como "siga o skill X" e ponha os passos no `SKILL.md`, que muda por commit. Para mudar o texto da rotina, peça na sessão dela (ex.: "Série Certa · painel (métricas)").
- **Onde mexer:** `.claude/skills/<skill>/SKILL.md`.
- **Exemplo (2026-10-16):** as rotinas de publicação traziam o comando no próprio texto (`rode python scripts/publicar.py --vencidos` e "publique só pelo scripts/publicar.py"). Por isso, na 1ª tarde do blog, a matéria das 17h não saiu pela rotina das 17h01, mesmo com a skill `/publicar` já atualizada. Ao criar publicador ou rede nova, confira o texto das rotinas com `list_triggers` e peça a mudança na sessão de cada uma (`send_message` para o `persistent_session_id` dela).

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
- **Blog (2026-10-16):** o mesmo aconteceu na revisão do blog (o `revisao.json` recém-escrito e a pauta foram substituídos pela cópia antiga da nuvem). O `blog/publicar_blog.py --simular` agora **não** baixa da nuvem e valida o disco. O `scripts/publicar.py --simular` continua baixando: rode `subir-pacote` antes.
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
