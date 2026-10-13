# Vai ao ar hoje: terça, 2026-10-13

| Horário | Plataforma | Peça | Pasta |
|---|---|---|---|
| 13h30 | Instagram (carrossel) | Órfã de série: as herdeiras de outubro | 01-carrossel-orfa-herdeiras-outubro |
| 18h00 | YouTube (Short) | Tradutor da órfã de terror (Carrie, a Estranha) | 02-short-tradutor-orfa-residencia-hill |
| 19h30 | Instagram (Stories, 4 telas) | MIA acertou? | 03-stories-mia-acertou |
| 20h00 | Instagram (Reels) | Selvagens do Sofá Ep. 02 (The Paper) | 04-reels-selvagens-ep02-orfa-the-office |

- TikTok (manual, não está no publicador automático): `tiktok.txt` das pastas 02 e 04, mesmo vídeo.
- O Short 02 não vai como Reels no Instagram, porque a pauta prevê só YouTube (e TikTok).
- Comentários fixados sugeridos (não são publicados automaticamente): `comentario-fixado.txt` nas pastas 01, 02 e 04.

## Bio
A bio **não muda hoje**. Os Stories de hoje (MIA acertou?) não têm link, e o CTA é por direct.

## Atenção
- `revisao.json` ainda lista só as peças 01 e 03. Sem as peças 02 e 04 lá, o `publicar.py` não publica o Reels das 20h (e o Short). Falta a segunda rodada do revisor.
- Conferir que o pacote foi enviado à nuvem (`python scripts/nuvem.py subir-pacote 2026-10-13`) antes das 13h30.
- Numeração "Ep. 02" de Selvagens do Sofá: confirmar e registrar em `historico/publicados.md`.
