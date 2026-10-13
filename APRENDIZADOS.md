# Aprendizados — retroalimentação das sessões

Fricções reais que custaram tempo e podem voltar. Leia antes de mexer em scripts, motor, publicação ou configuração.
Regras de como registrar: seção "Fechamento de sessão" do `CLAUDE.md`.
Formato: **sintoma → causa → como resolver/evitar → onde mexer**. Mais recente no topo.

## Publicação

### 2026-10-13 — `publicar.py --simular` sobrescreve o pacote local com o da nuvem
- **Sintoma:** depois de corrigir `publicar.json` e renderizar `quadros/` de novo, a simulação continuou acusando o erro antigo (`falta o campo "series"`) e as edições locais sumiram.
- **Causa:** na nuvem, o `publicar.py` (mesmo com `--simular`) chama `nuvem.baixar_pacote()` antes de validar, e o download sobrescreve os arquivos locais.
- **Como evitar:** depois de qualquer correção, rode `python scripts/nuvem.py subir-pacote <data>` **antes** de simular ou publicar.
- **Onde mexer:** `scripts/publicar.py` (`main`) e `scripts/nuvem.py`.

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
