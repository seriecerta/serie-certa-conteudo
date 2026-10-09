# Pilares e formatos

## Pilares (rotação semanal)
| Pilar | % | Job atendido | Exemplo |
|---|---|---|---|
| 1. Série pro seu humor | 40% | Principal | "3 séries pra quando você tá exausta" |
| 2. Órfã de série | 20% | Emocional 3 | "Acabou Ted Lasso? Vai nessas" |
| 3. Dilema do casal | 15% | Social 1 | Esquete Ela & Ele + modo casal |
| 4. MIA acertou? / prova | 15% | Ansiedade | Demo do app, reações |
| 5. Bastidor do produto | 10% | Atração | "Ensinei a MIA a entender domingo à noite" |

> Percentuais dos pilares **mantidos**: sem métricas em `historico/metricas.md`, não há base para redistribuir.

## Ênfase dos 90 dias (meta: audiência)
Vale até ~jan/2027 (ver `05-go-to-market.md`).
- Reels, Shorts e vídeos do casal fecham com o CTA de Descoberta ("Manda pra quem precisa"), inclusive nos pilares 4 e 5.
- Gancho pensado para **envio**: a pessoa tem que lembrar de alguém específico nos 2 primeiros segundos ("a amiga que acabou de terminar", "o namorado que nunca decide"). Envios pesam no alcance para não seguidores (Mosseri, jan/2025, [Social Media Today](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/)).
- Retenção é o outro sinal: série que combina vem logo depois do gancho; nada de introdução.
- Conversão ("Testa grátis no link") fica nos Stories, como já está na grade.

## Especificações por formato
### Reels / Shorts (9:16, 1080×1920)
- 20–40 s. Gancho falado + texto na tela nos **primeiros 2 s**.
- Estrutura: gancho (dor) → 1 a 3 séries (por que combina + onde assistir) → CTA.
- Entregar: roteiro com tempos, texto na tela por cena, narração (.txt + .mp3), legenda, hashtags (3–5), sugestão de capa.

### Vídeo longo YouTube (16:9)
- Estrutura fixa: 0–20 s dor + promessa → contagem de séries (por que combina, onde assistir, tempo total, pra quem não é) → 15 s de demo do app no meio → fim com link fixado + tela final para o próximo humor.
- Entregar: roteiro completo, narração por bloco, título (3 opções ranqueadas, escolher a 1ª), descrição com capítulos e UTMs, tags, texto da thumb, comentário fixado.

### Carrossel Instagram (1080×1350)
- 7–10 cards. Card 1 = gancho; último = CTA salvar.
- Entregar: `cena.html` com um `section.quadro` por card (motor, `--imagens --formato 4x5`) + legenda.

### Stories (1080×1920)
- Sequência de 3–5: pergunta/enquete → indicação → link de humor → caixinha "MIA acertou?".
- Entregar: texto de cada tela + sticker (enquete, link, caixa) + link com UTM.

### Feed estático
- Só para anúncio de produto/novidade. Texto curto + legenda.

## Changelog
- 2026-10-09 — Adicionada seção "Ênfase dos 90 dias": Reels/Shorts/casal com CTA de Descoberta em todos os pilares, gancho pensado para envio e retenção; percentuais dos pilares e especificações de formato mantidos — por quê: meta dos 90 dias virou audiência (seguidores/alcance); sem métricas, não há base para mexer nos pesos.
