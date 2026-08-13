#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara perfis na MESMA fase do ciclo do evento, não na mesma data do calendário.

Comparar um festival que acontece em maio com outro que acontece em novembro pela
data do calendário não diz nada: um está em pré-venda enquanto o outro está dormindo.
Aqui cada perfil é medido na sua própria janela relativa ao evento dele.

Uso:
  janela.py --eventos eventos.json --dados ~/.claude/concorrentes/historico/2026-08-11 --dias 30
  janela.py --eventos eventos.json --dados <pasta> --dias 30 --ate-dia -8

Formato do eventos.json:
  {"festivalcostumegourmet": {"nome": "Festival Costume Gourmet", "data": "2026-09-18",
                              "edicao": "2026", "cidade": "Fortaleza"}, ...}
"""

import argparse
import datetime
import json
import os
import re


def para_data(texto):
    if not texto:
        return None
    texto = re.sub(r"\+0000$", "+00:00", str(texto))
    try:
        return datetime.datetime.fromisoformat(texto)
    except ValueError:
        try:
            return datetime.datetime.strptime(texto[:10], "%Y-%m-%d")
        except ValueError:
            return None


def mediana(valores):
    ordenados = sorted(valores)
    if not ordenados:
        return 0
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2.0


def analisar_janela(retrato, dia_evento, dias, ate_dia):
    """Recorta os posts entre D-dias e D-ate_dia (ate_dia=0 significa o dia do evento)."""
    inicio = dia_evento - datetime.timedelta(days=dias)
    fim = dia_evento + datetime.timedelta(days=ate_dia)
    seguidores = (retrato.get("perfil") or {}).get("seguidores") or 0

    dentro = []
    for post in retrato.get("posts", []):
        quando = para_data(post.get("publicado_em"))
        if not quando:
            continue
        dia = quando.date()
        if inicio <= dia <= fim:
            interacoes = (post.get("curtidas") or 0) + (post.get("comentarios") or 0)
            dentro.append({"interacoes": interacoes, "tipo": post.get("tipo"),
                           "dia": dia, "link": post.get("link"),
                           "legenda": (post.get("legenda") or "")[:100]})

    if not dentro:
        return {"posts": 0, "cobertura": None}

    total = sum(p["interacoes"] for p in dentro)
    formatos = {}
    for post in dentro:
        formatos[post["tipo"]] = formatos.get(post["tipo"], 0) + 1
    campeao = max(dentro, key=lambda p: p["interacoes"])

    return {
        "posts": len(dentro),
        "posts_por_semana": round(len(dentro) / (dias / 7.0), 1),
        "interacoes_totais": total,
        "interacoes_media": round(total / float(len(dentro))),
        "interacoes_mediana": round(mediana([p["interacoes"] for p in dentro])),
        "engajamento_total_sobre_base": (round(100.0 * total / seguidores, 2)
                                         if seguidores else None),
        "engajamento_mediano_por_post": (round(100.0 * mediana([p["interacoes"] for p in dentro])
                                               / seguidores, 3) if seguidores else None),
        "seguidores": seguidores,
        "formatos": formatos,
        "campeao": campeao,
        "cobertura": {"de": inicio.isoformat(), "ate": fim.isoformat()},
        "primeiro_post": min(p["dia"] for p in dentro).isoformat(),
        "ultimo_post": max(p["dia"] for p in dentro).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compara perfis na mesma fase do ciclo do evento")
    parser.add_argument("--eventos", required=True, help="json com data do evento por handle")
    parser.add_argument("--dados", required=True, help="pasta com os retratos gerados por espiar.py")
    parser.add_argument("--dias", type=int, default=30, help="tamanho da janela antes do evento")
    parser.add_argument("--ate-dia", dest="ate_dia", type=int, default=0,
                        help="fim da janela em dias relativos ao evento (0 = dia do evento, "
                             "-8 = para oito dias antes)")
    parser.add_argument("--saida", help="grava o resultado consolidado em json")
    opcoes = parser.parse_args()

    with open(os.path.expanduser(opcoes.eventos), "r", encoding="utf-8") as arquivo:
        eventos = json.load(arquivo)

    pasta = os.path.expanduser(opcoes.dados)
    linhas = []
    for handle, info in eventos.items():
        caminho = os.path.join(pasta, "%s.json" % handle)
        if not os.path.exists(caminho):
            linhas.append({"handle": handle, "info": info, "erro": "sem dados coletados"})
            continue
        with open(caminho, "r", encoding="utf-8") as arquivo:
            retrato = json.load(arquivo)
        if retrato.get("erro"):
            linhas.append({"handle": handle, "info": info, "erro": retrato["erro"][:80]})
            continue
        dia_evento = para_data(info["data"]).date()
        resultado = analisar_janela(retrato, dia_evento, opcoes.dias, opcoes.ate_dia)
        linhas.append({"handle": handle, "info": info, "janela": resultado})

    validos = [l for l in linhas if l.get("janela", {}).get("posts")]
    validos.sort(key=lambda l: -(l["janela"]["interacoes_totais"]))

    print("JANELA: %d dias antes do evento até D%+d\n" % (opcoes.dias, opcoes.ate_dia))
    print("%-30s %-12s %6s %7s %11s %9s" % ("perfil", "evento", "posts", "sem.", "interações", "% base"))
    print("-" * 82)
    for linha in validos:
        j = linha["janela"]
        print("%-30s %-12s %6d %7s %11s %8s%%" % (
            "@" + linha["handle"], linha["info"]["data"], j["posts"], j["posts_por_semana"],
            "{:,}".format(j["interacoes_totais"]).replace(",", "."),
            j["engajamento_total_sobre_base"]))
    faltando = [l for l in linhas if not l.get("janela", {}).get("posts")]
    if faltando:
        print("\nsem dado na janela:")
        for linha in faltando:
            motivo = linha.get("erro") or "nenhum post no período coberto pela coleta"
            print("  @%-28s %s" % (linha["handle"], motivo))

    if opcoes.saida:
        with open(os.path.expanduser(opcoes.saida), "w", encoding="utf-8") as arquivo:
            json.dump(linhas, arquivo, ensure_ascii=False, indent=2, default=str)
        print("\n%s" % opcoes.saida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
