---
name: publicar
description: Publica no Instagram, no YouTube e no blog as peças aprovadas cujo horário chegou. A fila de hora em hora roda sozinha no GitHub Actions, sem o Claude; use esta skill para ver o status, pausar, retomar ou fazer uma rodada manual.
---
# Publicar

- **Fila automática (sem Claude, zero token):** `.github/workflows/publicar.yml` roda `python scripts/publicar.py --vencidos` e `python blog/publicar_blog.py --vencidos` de hora em hora das 9h02 às 22h02 (Brasília) e às 13h32 e 18h32. Não existe mais rotina do Claude para isso: não crie uma, porque duas filas ao mesmo tempo podem postar em dobro.
  Cada rodada aparece em github.com/seriecerta/serie-certa-conteudo/actions, com um resumo do que saiu. Rodada manual: aba Actions → `publicar` → **Run workflow** (marcado = só simula).
- **Rodar a fila nesta sessão** (só se o Bruno pedir): `python scripts/publicar.py --vencidos` e depois `python blog/publicar_blog.py --vencidos`. Responda em uma linha com o que saiu (links) ou "nada no horário".
  Na nuvem o script baixa sozinho tokens e pacotes do Supabase e guarda o estado de volta — não faça commit nem push.
- **Status**: leia `saida/<data>/publicacao.log.md` (linhas `[blog]` são do blog), os `estado-publicacao.json` das peças e os `blog/*/estado-blog.json` (na nuvem, rode antes `python scripts/nuvem.py baixar-pacote <data>`).
- **Pausar o dia** (redes e blog): crie o arquivo vazio `saida/<data>/PAUSAR` (na nuvem, depois rode `python scripts/nuvem.py subir-pacote <data> --so-texto`). **Retomar**: apague-o.
  Atalho pelo celular: pelo painel do Supabase, envie um arquivo chamado `PAUSAR` para `pacotes-redes/<data>/`.
  Para desligar tudo de uma vez: no GitHub, Settings → Secrets and variables → Actions → Variables, troque `PUBLICACAO_AUTOMATICA` para `false` (a fila passa a só simular).
- **Republicar algo que deu erro**: remova a entrada daquela publicação no `estado-publicacao.json` da peça e rode de novo — confirme antes no Instagram/YouTube que ela não saiu, para não duplicar.

Não edite legendas aqui sem passar pelo revisor.
