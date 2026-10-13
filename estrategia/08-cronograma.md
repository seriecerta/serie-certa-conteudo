# Cronograma de publicações

> Vale a partir de **quarta, 14/10/2026** (decisão do Bruno em 13/10). Mesma grade **todos os dias**, inclusive fim de semana.
> Fuso: America/Sao_Paulo. Horários são o que vai no `quando` do `publicar.json`.

## Grade diária
| Horário | Rede | Peça | Pilar |
|---|---|---|---|
| 10h00 | Instagram · Carrossel | definida pelo `estrategista` | definido pelo `estrategista` |
| 10h00 | Instagram · Stories | o carrossel do dia em Stories (ver abaixo) | o mesmo do carrossel |
| 12h00 | YouTube · Lista da MIA (16:9) | definida pelo `estrategista` | **definido pela tendência do dia** |
| 13h30 | YouTube · Short | definida pelo `estrategista` | definido pelo `estrategista` |
| 13h30 | Instagram · Reels | definida pelo `estrategista` | definido pelo `estrategista` |
| 18h30 | Instagram · Reels | definida pelo `estrategista` | definido pelo `estrategista` |
| 19h00 | YouTube · Short | definida pelo `estrategista` | definido pelo `estrategista` |

Por dia: 1 carrossel + 1 sequência de Stories + 1 Lista da MIA + 2 Shorts + 2 Reels.

## Como o `estrategista` escolhe peça e pilar
- **Pilares:** distribua as peças da semana perto dos pesos de `07-pilares-e-formatos.md` (40 / 20 / 15 / 15 / 10). Num dia, não repita o mesmo pilar nos dois Reels nem nos dois Shorts.
- **Dilema do casal:** pelo menos 1 peça de vídeo do casal na sexta à noite (Reels das 18h30 ou Short das 19h).
- **Domingo à noite:** o Reels das 18h30 conversa com "domingo à noite" (pilar 4, prova, ou pilar 1).
- **Short e Reels no mesmo horário (13h30):** podem ser o mesmo vídeo 9:16 (um arquivo, duas redes) ou peças diferentes. O `estrategista` decide e registra na pauta.
- **Lista da MIA:** o tema vem do que está em alta no dia. As regras estão em `07-pilares-e-formatos.md` → Lista da MIA e em `.claude/agents/estrategista.md`.
- **Repetição:** continua a regra de 30 dias (série + humor + gancho) de `historico/publicados.md`.

## Stories das 10h00
- Os cards do carrossel do dia adaptados para 9:16 (1080×1920), 3 a 5 telas, mais **uma** tela final de CTA.
- O CTA segue `05-go-to-market.md`. Na maioria dos dias é a tela de Conversão ("Testa grátis no link", com o link de humor na bio). Em alguns dias pode ser Retenção ("MIA acertou?"). Um só por sequência.
- A API publica sem stickers, então o CTA vai escrito na arte (ver `.claude/agents/desdobrador.md`).
- No `publicar.json`, é uma publicação `STORIES` própria, com `quadros/` 9:16. O desdobrador pode usar a mesma pasta do carrossel (com `"peca_mae"`) ou uma pasta separada.

## Pacote diário
- A rotina da manhã (6h41) entrega as peças do **dia** + o rascunho das peças do **dia seguinte**.
- As peças das 10h00 são as mais apertadas. Se não estiverem aprovadas até 9h50, vão para 11h00. Se não estiverem até 10h50, saem às 15h00 ou ficam para o dia seguinte (a pauta registra a decisão).
- Rascunhos de amanhã escritos antes desta grade (ex.: o de 14/10, feito em 13/10) **seguem a grade nova**: a rotina da manhã reencaixa as peças nos horários acima.

## Publicação
- YouTube: sobe e agenda na hora exata (publishAt do YouTube).
- Instagram: a rotina de publicação roda de hora em hora no minuto :01 e também às 13h31 e 18h31, para os horários "e meia" não atrasarem 30 min.

## Changelog
- 2026-10-13 — Grade semanal (horários diferentes por dia, vídeo longo de quinta às 19h) trocada por **grade diária única**: carrossel + Stories 10h, Lista da MIA 12h, Short + Reels 13h30, Reels 18h30, Short 19h. O vídeo longo semanal sai da grade (a Lista da MIA diária ocupa o espaço de vídeo 16:9). Pilares continuam escolhidos pelo agente com os pesos de `07` — por quê: decisão do Bruno, válida a partir de 14/10.
