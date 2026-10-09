---
name: publicar
description: Publica no Instagram e no YouTube as peças aprovadas cujo horário chegou. É o que a rotina de hora em hora chama; também serve para pausar, retomar ou ver o status das publicações do dia.
---
# Publicar

- **Rodar a fila**: `python scripts/publicar.py --vencidos` e responda em uma linha com o que saiu (links) ou "nada no horário".
  Na nuvem o script baixa sozinho tokens e pacotes do Supabase e guarda o estado de volta — não faça commit nem push nesta rotina.
- **Status**: leia `saida/<data>/publicacao.log.md` e os `estado-publicacao.json` das peças (na nuvem, rode antes `python scripts/nuvem.py baixar-pacote <data>`).
- **Pausar o dia**: crie o arquivo vazio `saida/<data>/PAUSAR` (na nuvem, depois rode `python scripts/nuvem.py subir-pacote <data> --so-texto`). **Retomar**: apague-o.
  Atalho pelo celular: pelo painel do Supabase, envie um arquivo chamado `PAUSAR` para `pacotes-redes/<data>/`.
- **Republicar algo que deu erro**: remova a entrada daquela publicação no `estado-publicacao.json` da peça e rode de novo — confirme antes no Instagram/YouTube que ela não saiu, para não duplicar.

Não edite legendas aqui sem passar pelo revisor.
