#!/usr/bin/env python3
"""Relatório de desempenho de um período, para a revisão semanal da grade e dos testes A/B.

Uso:
  python painel/relatorio.py --inicio 2026-10-14 --fim 2026-10-20     # escreve historico/relatorios/semana-2026-10-14.md
  python painel/relatorio.py --inicio 2026-10-14 --fim 2026-10-20 --metricas   # coleta números novos antes

Só leitura nas redes. Usa painel/metricas.json (na nuvem, baixado do Supabase) e os pacotes de saida/.

Base de comparação: os números do post em D+1 (primeira foto diária com 12 h ou mais de vida = coleta das 9h da manhã seguinte), para
não comparar um post de 3 dias com um de 3 horas. Quando o post ainda não tem D+1, usa o número atual
e marca com *.
Blog: compara em D+7 (leituras dos dias 0 a 6 desde a publicação), porque a busca demora a trazer leitor.
"""
import argparse
import datetime as dt
import pathlib
import re
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import painel  # noqa: E402

RAIZ = painel.RAIZ
REDE = {"instagram": "Instagram", "youtube": "YouTube", "tiktok": "TikTok"}
SLOT_RE = re.compile(r"^\|\s*(\d{1,2})h(\d{2})\s*\|\s*(Instagram|YouTube)\s*·\s*([^|(]+?)\s*(?:\(|\|)")
FORMATO_SLOT = {"Lista da MIA": "Vídeo longo"}
BLOG_INICIO = dt.date(2026, 10, 16)  # 1º dia do blog na rotina (08-cronograma.md)


def grade():
    """Lê os horários da tabela 'Grade diária' do 08-cronograma.md."""
    slots = []
    for linha in (RAIZ / "estrategia" / "08-cronograma.md").read_text(encoding="utf-8").splitlines():
        m = SLOT_RE.match(linha)
        if m:
            h, mi, rede, fmt = m.groups()
            fmt = fmt.strip()
            slots.append({"hora": f"{int(h):02d}:{mi}", "plataforma": rede.lower(),
                          "formato": FORMATO_SLOT.get(fmt, fmt)})
    return slots


def mediana(vals):
    vals = [v for v in vals if isinstance(v, (int, float))]
    return statistics.median(vals) if vals else None


def fmt(v, pct=False):
    if v is None:
        return "—"
    if pct:
        return f"{v * 100:.1f}%".replace(".", ",")
    return f"{v:,.0f}".replace(",", ".") if abs(v) >= 10 or float(v).is_integer() else f"{v:.1f}".replace(".", ",")


def base(p):
    """Números de comparação (D+1 se houver) + taxas."""
    m, maduro = (p.get("met_d1") or None), True
    if not m:
        m, maduro = (p.get("met") or {}), False
    alc = m.get("reach")
    inter = sum(m.get(k) or 0 for k in ("likes", "comments", "shares", "saved"))
    return {**m, "maduro": maduro, "eng": inter / alc if alc else None,
            "envio_alc": (m.get("shares") or 0) / alc if alc else None}


def tabela(grupos: dict, titulo: str) -> list:
    linhas = [f"### {titulo}", "",
              "| Grupo | n | Views (med.) | Alcance (med.) | Envios (med.) | Salvos (med.) | Envios/alcance | Engaj. |",
              "|---|---|---|---|---|---|---|---|"]
    for nome, pubs in sorted(grupos.items(), key=lambda kv: -(mediana([base(p).get("views") for p in kv[1]]) or 0)):
        b = [base(p) for p in pubs]
        linhas.append(f"| {nome or '—'} | {len(pubs)} | {fmt(mediana([x.get('views') for x in b]))} | "
                      f"{fmt(mediana([x.get('reach') for x in b]))} | {fmt(mediana([x.get('shares') for x in b]))} | "
                      f"{fmt(mediana([x.get('saved') for x in b]))} | {fmt(mediana([x['envio_alc'] for x in b]), True)} | "
                      f"{fmt(mediana([x['eng'] for x in b]), True)} |")
    return linhas + [""]


def agrupar(pubs, chave):
    g = {}
    for p in pubs:
        g.setdefault(chave(p), []).append(p)
    return g


def relatorio(inicio: str, fim: str, m: dict) -> str:
    inv = painel.juntar(painel.inventario(), m)
    a = dt.datetime.fromisoformat(inicio + "T00:00:00-03:00")
    b = dt.datetime.fromisoformat(fim + "T23:59:59-03:00")
    noper = [p for p in inv["publicacoes"] if a <= dt.datetime.fromisoformat(p["quando"]) <= b]
    pub = [p for p in noper if p["status"] == "publicado" and p["plataforma"] in ("instagram", "youtube")]
    dias = (b.date() - a.date()).days + 1
    out = [f"# Relatório {inicio} a {fim}", "",
           f"Gerado em {painel.AGORA:%d/%m/%Y %H:%M} por `painel/relatorio.py`. Métricas coletadas em "
           f"{m.get('coletado_em', 'nunca')[:16]}. Comparação em D+1 (* = post ainda sem D+1).", ""]

    # aderência à grade
    out += ["## Aderência à grade", "", "| Horário | Rede · formato | Dias cumpridos | Atraso médio | Faltou em |", "|---|---|---|---|---|"]
    for s in grade():
        feitos, atrasos, faltas = 0, [], []
        for i in range(dias):
            d = a.date() + dt.timedelta(days=i)
            alvo = dt.datetime.fromisoformat(f"{d}T{s['hora']}:00-03:00")
            achou = [p for p in pub if p["plataforma"] == s["plataforma"] and p["formato"] == s["formato"]
                     and abs(dt.datetime.fromisoformat(p.get("publicado_em") or p["quando"]) - alvo) <= dt.timedelta(hours=3)]
            if achou:
                feitos += 1
                atrasos.append((dt.datetime.fromisoformat(achou[0].get("publicado_em") or achou[0]["quando"]) - alvo).total_seconds() / 60)
            else:
                faltas.append(f"{d:%d/%m}")
        out.append(f"| {s['hora']} | {REDE[s['plataforma']]} · {s['formato']} | {feitos}/{dias} | "
                   f"{fmt(statistics.mean(atrasos)) + ' min' if atrasos else '—'} | {', '.join(faltas) or '—'} |")
    problemas = [p for p in noper if p["status"] in ("bloqueado", "perdido", "invalido", "erro", "sem-registro")]
    out += ["", f"Peças com problema no período: {len(problemas)}."]
    out += [f"- {p['data']} {p['peca']} ({p['plataforma']} {p['formato']}): {p['status']} {p.get('motivo', '')[:120]}"
            for p in problemas]
    out.append("")

    # conta
    seg = sorted((m.get("seguidores") or {}).items())
    def delta(rede):
        v = [(d, o[rede]) for d, o in seg if o.get(rede) is not None and inicio <= d <= fim]
        return f"{v[0][1]} → {v[-1][1]} ({v[-1][1] - v[0][1]:+d})" if len(v) > 1 else (str(v[0][1]) if v else "—")
    conta = {d: o for d, o in (m.get("conta_ig") or {}).items() if inicio <= d <= fim}
    soma = lambda k: sum(o.get(k) or 0 for o in conta.values())
    utm = [c for c in m.get("cliques_utm", []) if inicio <= c["dia"] <= fim]
    out += ["## Conta", "",
            f"- Seguidores Instagram: {delta('instagram')} · Inscritos YouTube: {delta('youtube')}",
            f"- Instagram no período: alcance {fmt(soma('reach'))}, visitas ao perfil {fmt(soma('profile_views'))}, "
            f"cliques no link da bio {fmt(soma('website_clicks'))}",
            f"- Visitas ao site com UTM: {sum(c['cliques'] for c in utm)} "
            f"({', '.join(f'{o}: {n}' for o, n in sorted(agrupar_soma(utm).items()))})", ""]

    out += secao_blog(inv, a, b, dias)

    # comparações
    out += ["## Desempenho por dimensão", ""]
    hora = lambda p: dt.datetime.fromisoformat(p.get("publicado_em") or p["quando"]).strftime("%Hh")
    out += tabela(agrupar(pub, lambda p: f"{REDE[p['plataforma']]} · {p['formato']}"), "Rede e formato")
    out += tabela(agrupar(pub, lambda p: f"{hora(p)} · {REDE[p['plataforma']]} {p['formato']}"), "Horário (hora real de publicação)")
    out += tabela(agrupar([p for p in pub if p.get("pilar_n")], lambda p: f"{p['pilar_n']}. {p['pilar']}"), "Pilar")
    out += tabela(agrupar(pub, lambda p: p.get("recorrente") or ("fora do pacote" if p.get("externa") else "avulso")), "Formato recorrente")
    out += tabela(agrupar([p for p in pub if p.get("funil")], lambda p: p["funil"]), "Estágio do funil (CTA)")

    # ranking
    rank = sorted(pub, key=lambda p: (base(p).get("shares") or 0, base(p).get("reach") or base(p).get("views") or 0), reverse=True)
    linha = lambda p: (f"| {p['data'][5:]} | {REDE[p['plataforma']]} {p['formato']} | {p['titulo'][:60]} | "
                       f"{fmt(base(p).get('views'))}{'' if base(p)['maduro'] else '*'} | {fmt(base(p).get('reach'))} | "
                       f"{fmt(base(p).get('shares'))} | {fmt(base(p).get('saved'))} | {p.get('experimento') or '—'} |")
    cab = ["| Data | Formato | Publicação | Views | Alcance | Envios | Salvos | Teste |", "|---|---|---|---|---|---|---|---|"]
    out += ["## Melhores e piores (por envios, depois alcance)", "", "### Top 5", ""] + cab + [linha(p) for p in rank[:5]]
    out += ["", "### Últimos 5", ""] + cab + [linha(p) for p in rank[-5:][::-1]] + [""]

    # testes A/B
    exps = agrupar([p for p in pub if p.get("experimento")], lambda p: p["experimento"].split("·")[0])
    out += ["## Testes A/B", ""]
    if not exps:
        out += ["Nenhuma publicação marcada com `experimento` no período.", ""]
    for eid, pubs in exps.items():
        out += tabela(agrupar(pubs, lambda p: p["experimento"]), f"Teste `{eid}`")
        var = agrupar(pubs, lambda p: p["experimento"].split("·")[1])
        if len(var) == 2:
            (va, pa), (vb, pb) = sorted(var.items())
            for metrica in ("shares", "views", "reach"):
                ma, mb = mediana([base(p).get(metrica) for p in pa]), mediana([base(p).get(metrica) for p in pb])
                if ma is not None and mb is not None:
                    dif = (mb - ma) / ma if ma else None
                    n_ok = min(len(pa), len(pb)) >= 3
                    sinal = ("inconclusivo (menos de 3 posts por variante)" if not n_ok else
                             f"{vb} à frente" if dif is not None and dif >= 0.2 else
                             f"{va} à frente" if dif is not None and dif <= -0.2 else "empate (diferença < 20%)")
                    out.append(f"- {metrica}: {va} {fmt(ma)} × {vb} {fmt(mb)} "
                               f"({'—' if dif is None else f'{dif * 100:+.0f}%'}) → {sinal}")
            out.append("")
    return "\n".join(out) + "\n"


def secao_blog(inv, a, b, dias) -> list:
    """Matérias do blog no período: aderência à grade do blog, desempenho por slot e ranking (D+7)."""
    todas = [p for p in inv["publicacoes"] if p["plataforma"] == "blog"
             and a <= dt.datetime.fromisoformat(p.get("publicado_em") or p["quando"]) <= b]
    pub = [p for p in todas if p["status"] == "publicado"]
    leit = lambda p: ((p.get("met_d7") or {}).get("views"), bool(p.get("met_d7"))) if p.get("met_d7") else ((p.get("met") or {}).get("views"), False)
    out = ["## Blog", "", f"{len(pub)} matérias no ar no período ({sum(1 for p in pub if p.get('externa'))} fora dos pacotes). "
           "Leituras em D+7 (* = matéria ainda sem 7 dias; mostra o total atual).", ""]
    out += ["| Horário | Slot | Dias cumpridos | Faltou em |", "|---|---|---|---|"]
    for h, slot in painel.SLOT_BLOG.items():
        faltas, validos = [], 0
        for i in range(dias):
            d = a.date() + dt.timedelta(days=i)
            if d < BLOG_INICIO:
                continue
            validos += 1
            alvo = dt.datetime.fromisoformat(f"{d}T{h}:00:00-03:00")
            if not any(not p.get("externa") and abs(dt.datetime.fromisoformat(p["quando"]) - alvo) <= dt.timedelta(hours=3) for p in pub):
                faltas.append(f"{d:%d/%m}")
        out.append(f"| {h}h00 | {slot} | {validos - len(faltas)}/{validos} | {', '.join(faltas) or '—'} |")
    out += ["", "| Slot | n | Leituras D+7 (med.) | Leu até 90% (med.) | Cliques no app (soma) |", "|---|---|---|---|---|"]
    for slot, ps in sorted(agrupar(pub, lambda p: p.get("recorrente") or ("fora do pacote" if p.get("externa") else "avulso")).items()):
        out.append(f"| {slot} | {len(ps)} | {fmt(mediana([leit(p)[0] for p in ps]))} | "
                   f"{fmt(mediana([(p.get('met') or {}).get('leituras_90') for p in ps]))} | "
                   f"{fmt(sum((p.get('met') or {}).get('cliques_app') or 0 for p in ps))} |")
    rank = sorted(pub, key=lambda p: leit(p)[0] or 0, reverse=True)
    out += ["", "### Top 5 do blog", "", "| Data | Slot | Matéria | Leituras | Leu até 90% | Cliques no app |", "|---|---|---|---|---|---|"]
    out += [f"| {p['data'][5:]} | {p.get('recorrente') or '—'} | {p['titulo'][:60]} | {fmt(leit(p)[0])}{'' if leit(p)[1] else '*'} | "
            f"{fmt((p.get('met') or {}).get('leituras_90'))} | {fmt((p.get('met') or {}).get('cliques_app'))} |" for p in rank[:5]]
    problemas = [p for p in todas if p["status"] in ("bloqueado", "invalido", "erro", "sem-registro")]
    out += ["", f"Matérias com problema no período: {len(problemas)}."]
    out += [f"- {p['data']} {p['peca']}: {p['status']} {p.get('motivo', '')[:120]}" for p in problemas]
    return out + [""]


def agrupar_soma(utm):
    g = {}
    for c in utm:
        g[c["origem"] or "(sem origem)"] = g.get(c["origem"] or "(sem origem)", 0) + c["cliques"]
    return g


def main():
    painel.nuvem.carregar_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--inicio", required=True)
    ap.add_argument("--fim", required=True)
    ap.add_argument("--metricas", action="store_true", help="coleta números novos antes")
    a = ap.parse_args()
    na_nuvem = painel.nuvem.em_nuvem() and bool(painel.os.environ.get("SUPABASE_URL"))
    if na_nuvem:
        painel.baixar_da_nuvem()
        if a.metricas:
            painel.nuvem.baixar_credenciais()
    m = painel.coletar(30) if a.metricas else painel.ler_json(painel.METRICAS, {})
    if na_nuvem and a.metricas:
        painel.nuvem.subir(painel.nuvem.B_PACOTE, painel.METRICAS, "painel/metricas.json")
        painel.nuvem.subir_credenciais()
    destino = RAIZ / "historico" / "relatorios" / f"semana-{a.inicio}.md"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(relatorio(a.inicio, a.fim, m), encoding="utf-8")
    print(f"✓ {destino.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
