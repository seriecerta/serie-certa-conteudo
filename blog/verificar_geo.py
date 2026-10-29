#!/usr/bin/env python3
"""Confere se uma matéria do blog segue a estratégia de GEO (estrategia/12-geo.md). Só lê; não publica.

Uso:
  python blog/verificar_geo.py saida/<data>/blog/<nn>-<slug>          # uma matéria
  python blog/verificar_geo.py saida/<data>                           # todas as matérias do dia

Sai com código 1 se alguma matéria falhar. O redator roda antes de entregar; o revisor roda antes de aprovar.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import publicar_blog as pb  # noqa: E402  (só as funções de leitura: ler_materia, normalizar, sem_marcas)

FRASE_MARCA = "O Série Certa (seriecerta.online) indica séries pelo seu humor do momento"
VARIANTES_ERRADAS = [r"\bSerie Certa\b", r"\bSérie certa\b", r"\bSeriecerta\b(?!\.online)", r"\bSérieCerta\b"]


def palavras(s: str) -> int:
    return len(re.findall(r"[^\W_]+", pb.sem_marcas(s or "")))


def checar(pasta: pathlib.Path) -> list:
    meta = pb.ler_json(pasta / "materia.json", None)
    if meta is None or not (pasta / "materia.md").exists():
        return ["falta materia.json ou materia.md"]
    blocos = pb.normalizar(pb.ler_materia(pasta))
    md = (pasta / "materia.md").read_text(encoding="utf-8")
    erros = []

    # pergunta-alvo
    pergunta = (meta.get("pergunta_alvo") or "").strip()
    if not pergunta.endswith("?") or palavras(pergunta) < 4:
        erros.append('falta "pergunta_alvo" no materia.json (pergunta em linguagem natural, terminando em "?")')

    # 1. resposta rápida logo no começo
    rr = next((i for i, b in enumerate(blocos) if b["tipo"] == "destaque" and
               (b.get("titulo") or "").lower().startswith("resposta rápida")), None)
    if rr is None:
        erros.append("falta a caixa ':::info Resposta rápida' (40–80 palavras, logo depois da abertura)")
    else:
        if rr > 5:
            erros.append(f"a Resposta rápida está no bloco {rr + 1}: ponha logo depois da abertura (até o 5º bloco)")
        n = palavras(blocos[rr]["texto"])
        if not 40 <= n <= 80:
            erros.append(f"Resposta rápida com {n} palavras (use 40–80)")
        chave = (meta.get("palavra_chave") or "").lower()
        termos = [t for t in re.findall(r"[^\W_]{4,}", chave)]
        if termos and not any(t in blocos[rr]["texto"].lower() for t in termos):
            erros.append("a Resposta rápida não usa a palavra-chave principal")

    # 2. tabela-resumo em lista com 3+ séries
    if len(meta.get("series") or []) >= 3 and not any(b["tipo"] == "tabela" for b in blocos):
        erros.append("lista com 3+ séries sem tabela-resumo (| Série | Onde assistir | Temporadas | Pra quem é |)")

    # 3. perguntas frequentes
    try:
        ini = next(i for i, b in enumerate(blocos) if b["tipo"] == "titulo" and b["nivel"] == 2
                   and b["texto"].lower().startswith("perguntas frequentes"))
    except StopIteration:
        erros.append("falta a seção '## Perguntas frequentes'")
    else:
        perguntas, atual = [], None
        for b in blocos[ini + 1:]:
            if b["tipo"] == "titulo" and b["nivel"] == 2:
                break
            if b["tipo"] == "titulo" and b["nivel"] == 3:
                atual = [b["texto"], 0]
                perguntas.append(atual)
            elif atual and b["tipo"] in ("paragrafo", "lista"):
                atual[1] += palavras(b.get("texto") or " ".join(b.get("itens", [])))
        if not 3 <= len(perguntas) <= 6:
            erros.append(f"Perguntas frequentes com {len(perguntas)} perguntas (use 3 a 5, em '###')")
        for texto, n in perguntas:
            if not texto.strip().endswith("?"):
                erros.append(f"pergunta sem '?': {texto[:50]}")
            if not 25 <= n <= 110:
                erros.append(f"resposta com {n} palavras em '{texto[:40]}' (use 30–100)")

    # 4. fatos com fonte e data
    fontes = [f for f in meta.get("fontes", []) if f.get("url")]
    if len(fontes) < 3:
        erros.append(f"só {len(fontes)} fontes com link (mínimo 3)")
    if meta.get("series") and "conferido em" not in md.lower():
        erros.append("falta a caixa ':::info Conferido em DD/MM/AAAA'")

    # 5. entidade da marca
    if FRASE_MARCA not in md:
        erros.append(f"falta a frase de marca antes do [[app]] (começa com \"{FRASE_MARCA}\")")
    for padrao in VARIANTES_ERRADAS:
        if re.search(padrao, md):
            erros.append(f"nome da marca escrito errado ({padrao}); use sempre \"Série Certa\"")
    return erros


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    alvo = pathlib.Path(sys.argv[1])
    pastas = [alvo] if (alvo / "materia.json").exists() else sorted(p for p in (alvo / "blog").glob("*/") if (p / "materia.json").exists())
    if not pastas:
        sys.exit(f"nenhuma matéria em {alvo}")
    falhou = False
    for p in pastas:
        erros = checar(p)
        falhou |= bool(erros)
        print(f"{p.name}: " + ("✓ GEO ok" if not erros else f"{len(erros)} pendência(s)"))
        for e in erros:
            print(f"  ✗ {e}")
    sys.exit(1 if falhou else 0)


if __name__ == "__main__":
    main()
