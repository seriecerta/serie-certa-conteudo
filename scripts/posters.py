#!/usr/bin/env python3
"""Baixa o pôster oficial de cada série citada numa peça (mesma fonte do app: TVmaze, sem chave).

Uso:
  python scripts/posters.py saida/2026-10-13/05-lista-com-sono "Ted Lasso" "Only Murders in the Building (2021)"
  python scripts/posters.py <pasta> --id 44458 "Ted Lasso"      # força o ID do TVmaze quando o nome é ambíguo

Salva em <pasta>/imagens/<slug>.jpg (use na cena: <div class="capa"><img src="imagens/ted-lasso.jpg"></div>)
e registra a origem em <pasta>/imagens/posters.json (título encontrado, ano, id e URL do TVmaze).
Ano entre parênteses no nome ajuda a desambiguar ("The Office (2005)").
Sai com código 2 se alguma série ficar sem pôster — aí a cena usa .capa.gerada e o revisor é avisado.
"""
import json
import pathlib
import re
import subprocess
import sys
import unicodedata

import requests

API = "https://api.tvmaze.com"
MIN_ALTURA = 500  # px — abaixo disso o pôster fica borrado no vídeo


def slug(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def buscar(nome: str, show_id: int | None = None) -> dict | None:
    if show_id:
        r = requests.get(f"{API}/shows/{show_id}", timeout=20)
        return r.json() if r.ok else None
    m = re.match(r"^(.*?)\s*\((\d{4})\)\s*$", nome)
    titulo, ano = (m.group(1), int(m.group(2))) if m else (nome, None)
    r = requests.get(f"{API}/search/shows", params={"q": titulo}, timeout=20)
    if not r.ok:
        return None
    candidatos = [c["show"] for c in r.json() if c.get("show", {}).get("image")]
    if ano:
        candidatos = [s for s in candidatos if (s.get("premiered") or "")[:4] == str(ano)] or candidatos
    return candidatos[0] if candidatos else None


def altura(arq: pathlib.Path) -> int:
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=height",
                              "-of", "csv=p=0", str(arq)], capture_output=True, text=True).stdout.strip()
        return int(out or 0)
    except Exception:
        return 0


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit(__doc__)
    pasta = pathlib.Path(args.pop(0))
    destino = pasta / "imagens"
    destino.mkdir(parents=True, exist_ok=True)
    registro_arq = destino / "posters.json"
    registro = json.loads(registro_arq.read_text(encoding="utf-8")) if registro_arq.exists() else {}

    faltando, forcar_id = [], None
    for a in args:
        if a == "--id":
            forcar_id = -1
            continue
        if forcar_id == -1:
            forcar_id = int(a)
            continue
        show = buscar(a, forcar_id)
        forcar_id = None
        arq = destino / f"{slug(re.sub(r'\s*\(\d{4}\)\s*$', '', a))}.jpg"
        url = ((show or {}).get("image") or {}).get("original")
        if not url:
            print(f"✗ sem pôster: {a}")
            faltando.append(a)
            continue
        img = requests.get(url, timeout=60)
        if not img.ok:
            print(f"✗ falha ao baixar pôster de {a} ({img.status_code})")
            faltando.append(a)
            continue
        arq.write_bytes(img.content)
        h = altura(arq)
        if h and h < MIN_ALTURA:
            print(f"! pôster de {a} pequeno ({h}px) — vai ficar borrado")
        registro[arq.name] = {"pedido": a, "encontrado": show.get("name"), "estreia": show.get("premiered"),
                              "tvmaze_id": show.get("id"), "pagina": show.get("url"), "imagem": url}
        aviso = "" if slug(show.get("name", "")) in slug(a) else f"  ⚠ confira: achou '{show.get('name')}'"
        print(f"+ {arq.name} ← {show.get('name')} ({(show.get('premiered') or '????')[:4]}){aviso}")

    registro_arq.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    if faltando:
        print("Sem pôster (use .capa.gerada e registre no 99-revisao.md): " + "; ".join(faltando))
        sys.exit(2)


if __name__ == "__main__":
    main()
