# Revisão — domingo, 2026-10-18

## 1ª rodada (peças das 10h00) — revisor, ~07h BRT

### Aprovadas
- `01-carrossel-ninguem-quer-volta-quinta` (IG carrossel, 10h00, 7 cards 1080×1350)
- `02-stories-ninguem-quer-volta-quinta` (IG Stories, 10h00, 5 telas 1080×1920)

### Fatos reconferidos hoje (18/10)
- **Ninguém Quer T3 em 22/10 (quinta):** a página da Netflix BR (`netflix.com/br/title/81591296`, user-agent Googlebot) traz o aviso "A temporada 3 estreia quinta-feira". O Omelete e o Critical Hits dão 22/10. Domingo, 18, até quinta, 22, são 4 dias. **"Faltam 4 dias" e "volta quinta" mantidos.** Isso só vale se a peça sair hoje. Se atrasar para amanhã, a contagem fica errada: bloqueie em vez de remarcar.
- **Love:** Netflix BR, 3 temporadas (10/12/12 eps), encerrada (JustWatch BR FLATRATE + página Netflix BR).
- **Modern Love:** Prime Video BR (no JustWatch, "Amor Moderno"), 2 temporadas (JustWatch BR FLATRATE).
- **Master of None:** Netflix BR, 3 temporadas (10/10/5 eps) (JustWatch BR + página Netflix BR).
- *Lovesick* e *Catastrophe* (pauta) não estão na peça. O desdobrador usou a reserva *Master of None*, e o carrossel saiu com 3 séries, como a pauta previa.

### Corrigido pelo revisor (re-render: `--imagens --formato 4x5` no 01; `--imagens` no 02)
- **Modern Love (card 4 e tela 3):** o recorte deixava aparecer uma faixa cortada do logo "prime video" embaixo do pôster. O recorte novo mostra só o "M" e o coração com o elenco, sem logo e sem texto cortado.
- **Master of None (card 5 e tela 4):** o pôster oficial do TVmaze (o da T3, "Moments in Love") aparecia cortado em cima ("presents") e embaixo ("Lena Waithe"), sem o nome da série. O recorte novo mostra "Master of None presents Moments in Love" inteiro e corta antes dos créditos. Os pôsteres de outras temporadas no TVmaze só existem em 210×295 (o original dá 404), pequenos demais.
- **Recibo (card 6):** "amor por episódio" e "Modern Love" ficavam colados na mesma linha, como se fossem uma frase só. O rótulo virou "antologia".
- Abri todos os quadros depois do re-render: 7 do carrossel e 5 dos Stories. Nenhum logo de streaming desenhado por nós, nenhum texto cortado, nenhuma sobreposição. O "A NETFLIX SERIES" pequeno no pôster de *Ninguém Quer* é parte do pôster oficial (`11-blog.md`: o pôster não é editado). O rodapé "ONLY ON NETFLIX | OCTOBER 22" fica fora do recorte.

### Checklist
- Spoiler: zero. Sobre T1/T2 de *Ninguém Quer*, só "volta quinta". Nenhum diálogo, nenhuma letra.
- Voz: ok. Frases curtas, "pra quem não é" nas 3 séries, sem "você sabia".
- CTA: carrossel "salva pra ver até quinta" (Consideração); Stories "testa grátis no link da bio" (Conversão). Um em cada.
- Legenda: 194 caracteres, 1 emoji, 4 hashtags. Comentário fixado só com onde assistir.
- `publicar.json`: `validar()` OK nos dois. `quando` = `2026-10-18T10:00:00-03:00`. Arquivos existem. `series` = as 4 séries com pôster (`posters.json`: TVmaze 77060, 6765 *Love* 2016, 37120, 2761).
- UTM dos Stories (`textos.md`): `https://seriecerta.online/?utm_source=instagram&utm_medium=stories&utm_campaign=2026-10-18-stories-ninguem-quer-volta-quinta`. Vai sem `humor=` porque o slug ainda não foi confirmado (pauta).
- **Pendência manual do Bruno:** trocar o link da bio por essa UTM antes das 10h00.
- `publicar.py --simular` **não** rodou nesta rodada: ele baixa o pacote da nuvem e sobrescreveria o blog que está sendo escrito agora. A validação foi pelo `validar()` (APRENDIZADOS, 13/10). Fica para a rodada final.

### Fora desta rodada (vão no revisao.json na rodada final)
- Blog (5 matérias): em produção.
- 03, 04 e 05 (vídeos): sem narração. Os créditos da ElevenLabs acabaram (29; o Tradutor pedia 179).

## Rodada final — revisor, ~07h–07h30 BRT

### Redes: bloqueadas (não produzidas)
- `03-lista-da-mia-series-sertanejas`, `04-short-reels-tradutor-o-que-a-mia-entende`, `05-reels-short-relogio-domingo-a-noite`: sem narração. A ElevenLabs está sem créditos (29 restantes; o teste de hoje pedia 179, `quota_exceeded`).
- 01 e 02 (carrossel + Stories) seguem aprovadas, sem mudança.

### Blog: as 5 aprovadas
Fatos reconferidos hoje: API GraphQL do JustWatch BR (ofertas FLATRATE, temporadas, episódios), `netflix.com/br/title` com UA Googlebot e `api.tvmaze.com` (datas, runtimes, pôsteres), mais busca na web para datas de estreia. Todas passam em `publicar_blog.py --verificar`. Originalidade: frases buscadas entre aspas sem resultado. Um `[[app]]` em cada, caixa "Conferido em 18/10/2026", "pra quem não é" em toda série, links internos de matérias no ar.

- **01 (09h) ansiosa:** as 7 séries batem com o JustWatch BR (Queer Eye 10 temp. Netflix; Gilmore Girls 7 temp./153 eps HBO Max, Disney+ e Prime Video; Brooklyn Nine-Nine 8 temp./153 eps Netflix; Monk 8 temp. Prime Video; Mandou Bem 7 temp. Netflix; Grace e Frankie 7 temp./94 eps Netflix; Somebody Feed Phil 8 temp. Netflix). Brooklyn Nine-Nine repete só como uma série de outra lista. Palavra-chave e lista diferentes: liberada. Capa ok. Sem mudança. Aprovada primeiro e subida antes das 09h.
- **02 (11h) HBO Max outubro:** o calendário de *Guerra* foi confirmado no TVmaze (8 eps, quintas, 1/10 a 19/11), no Einerd/Gameoverdrive e pelo criador George Kay (Lupin). *The Torment* (Zmora): 6 eps às sextas, Małecki, Cielecka e Toruń confirmados em mais de um veículo polonês, e o JustWatch BR põe a série no HBO Max. *Get Jiro* no BR em 4/10 (Showmetech/Itatiaia). *The Paper* T2 no BR em 15/10 (Omelete/Gameoverdrive; JustWatch: HBO Max, 2 temp.). *Largados e Pelados Brasil* T4 hoje, com 7 eps.
  - Corrigido: a duração de *Guerra* passou de "cerca de 50 min" para "de 50 min a 1 hora" (TVmaze 51–60), e a de *Lanternas* para "cerca de uma hora". *Largados* agora diz "hoje à noite, com dois episódios" e que depois sai um a cada domingo.
  - Selos nos pôsteres (HBO Max no *Zmora*, Peacock no *The Paper*, DC Studios/adult swim): são os pôsteres oficiais e não foram editados (`11-blog.md`). Na capa (leque) só aparecem DC Studios e adult swim, que não são streaming.
- **03 (14h) Crystal Lake:** Universal+ (canal Amazon e assinatura direta), 8 eps, no BR em 16/10, confirmados no JustWatch BR e em 3 veículos. Slasher tem 3 temporadas na Netflix BR (página da Netflix: "3 temporadas").
  - **Pôsteres trocados:** *American Horror Story* saiu da T13 para o pôster oficial da T9, *1984* (TVmaze, temporada 9). *Slasher* saiu da T5, *Ripper* (que não está na Netflix BR), para o pôster da T2, *Guilty Party* / *Os Culpados*, a temporada que o texto recomenda (TVmaze, temporada 2). O `posters.json` foi atualizado, os alt/legendas dizem a temporada e a capa foi renderizada de novo.
  - Duração de AHS 1984 e de Chucky passou para "menos de 1 hora". Ponto final que faltava no item do Prime.
  - O selo "Peacock Original" no pôster de *Crystal Lake* fica: os dois pôsteres oficiais do TVmaze trazem o selo, e a legenda diz Universal+.
- **04 (17h) Ninguém Quer T3:** **erro corrigido.** 22/10/2026 é **quinta**, e a matéria dizia "quarta" em 9 lugares e no subtítulo. A data foi confirmada no TVmaze, no What's on Netflix, no TVLine e na Netflix BR ("estreia quinta-feira"). O plano de maratona foi refeito para domingo a quarta. Agora a matéria diz 10 eps na T3 (What's on Netflix + TVmaze + JustWatch). Saíram duas datas sem confirmação: renovação em "novembro de 2025" e anúncio "em setembro". Elenco novo (Silverman, Rannells) confirmado na Netflix Tudum. Spoiler zero de T1/T2.
- **05 (20h) sertanejo:** *Sentimento Louco* (Prime Video, 16/10, 4 eps, direção de Susanna Lira) está só como contexto: é o gancho de quem já viu, sem seção e sem recomendação. Cortei a frase que avaliava o doc ("contado com respeito"), e ele ficou fora do `series` (o TVmaze não tem pôster). Tom respeitoso, sem acidente e sem letra. Nada promete vídeo, porque a Lista foi bloqueada.
  - Corrigido: *Rensga Hits!* dizia "casamento que não deu certo" e passou para "noivado" (ela larga o noivo no altar). *Só Se For Por Amor* dizia "sem continuação" e passou para "por enquanto, é uma só" (o TVmaze diz "TBD").

### Atenção: `publicar.py --simular` desfez as correções locais
Depois do `subir-pacote`, o `scripts/publicar.py --simular` baixou da nuvem uma cópia antiga dos `.json`/`.md` (resposta do storage com `cf-cache-status: HIT`) e desfez todas as correções do blog e o `revisao.json`. Refiz tudo, subi de novo e conferi pelo `object/info` (tamanho/etag), sem baixar.
