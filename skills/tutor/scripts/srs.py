#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de repetição espaçada do AI-TUTOR.

Algoritmo SM-2 enxuto. Decide o que vence hoje e reagenda depois da revisão.
As datas são calculadas aqui, de forma determinística, e nunca estimadas pelo modelo.

Uso:
  srs.py add <arquivo.json> --frente "..." --verso "..." [--topico f1u2]
  srs.py due <arquivo.json> [--limite 10] [--json]
  srs.py revisar <arquivo.json> --id c0003 --nota bom
  srs.py stats <arquivo.json>
  srs.py listar <arquivo.json> [--topico f1u2]

Notas aceitas: errei | dificil | bom | facil
"""

import argparse
import datetime
import json
import os
import sys

NOTAS = {"errei": 0, "dificil": 3, "bom": 4, "facil": 5}
FACILIDADE_MINIMA = 1.3
FACILIDADE_INICIAL = 2.5


def hoje():
    return datetime.date.today()


def para_data(texto):
    return datetime.datetime.strptime(texto, "%Y-%m-%d").date()


def carregar(caminho):
    caminho = os.path.expanduser(caminho)
    if not os.path.exists(caminho):
        return {"cards": []}
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    if "cards" not in dados:
        dados["cards"] = []
    return dados


def salvar(caminho, dados):
    caminho = os.path.expanduser(caminho)
    pasta = os.path.dirname(os.path.abspath(caminho))
    if pasta and not os.path.isdir(pasta):
        os.makedirs(pasta)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)
        arquivo.write("\n")


def proximo_id(dados):
    maior = 0
    for card in dados["cards"]:
        try:
            numero = int(str(card.get("id", "c0"))[1:])
        except ValueError:
            numero = 0
        maior = max(maior, numero)
    return "c%04d" % (maior + 1)


def cmd_add(args):
    dados = carregar(args.arquivo)
    frente = args.frente.strip()
    for card in dados["cards"]:
        if card["frente"].strip().lower() == frente.lower():
            print("já existe um cartão igual a esse: %s" % card["id"])
            return 0
    card = {
        "id": proximo_id(dados),
        "frente": frente,
        "verso": args.verso.strip(),
        "topico": args.topico or "",
        "criado": hoje().isoformat(),
        "due": (hoje() + datetime.timedelta(days=1)).isoformat(),
        "intervalo": 1,
        "facilidade": FACILIDADE_INICIAL,
        "repeticoes": 0,
        "lapsos": 0,
        "historico": [],
    }
    dados["cards"].append(card)
    salvar(args.arquivo, dados)
    print("cartão %s criado, primeira revisão em %s" % (card["id"], card["due"]))
    return 0


def vencidos(dados, limite=None):
    limite_data = hoje()
    pendentes = [c for c in dados["cards"] if para_data(c["due"]) <= limite_data]
    pendentes.sort(key=lambda c: (c["due"], -c.get("lapsos", 0)))
    if limite:
        pendentes = pendentes[:limite]
    return pendentes


def cmd_due(args):
    dados = carregar(args.arquivo)
    pendentes = vencidos(dados, args.limite)
    if args.json:
        print(json.dumps(pendentes, ensure_ascii=False, indent=2))
        return 0
    if not pendentes:
        print("nada vencendo hoje. %d cartões no total." % len(dados["cards"]))
        return 0
    print("%d cartão(ões) para revisar hoje:\n" % len(pendentes))
    for card in pendentes:
        atraso = (hoje() - para_data(card["due"])).days
        selo = "vence hoje" if atraso == 0 else "atrasado %d dia(s)" % atraso
        topico = card.get("topico") or "sem tópico"
        print("[%s] (%s) %s" % (card["id"], topico, selo))
        print("F: %s" % card["frente"])
        print("V: %s\n" % card["verso"])
    return 0


def agendar(card, nota):
    """SM-2 enxuto: recalcula facilidade, intervalo e próxima data do cartão."""
    qualidade = NOTAS[nota]
    facilidade = float(card.get("facilidade", FACILIDADE_INICIAL))
    repeticoes = int(card.get("repeticoes", 0))
    intervalo = int(card.get("intervalo", 1))

    if qualidade < 3:
        repeticoes = 0
        intervalo = 1
        card["lapsos"] = int(card.get("lapsos", 0)) + 1
    else:
        if repeticoes == 0:
            intervalo = 1
        elif repeticoes == 1:
            intervalo = 6
        else:
            fator = 1.2 if qualidade == 3 else facilidade
            intervalo = max(1, int(round(intervalo * fator)))
        repeticoes += 1

    delta = 0.1 - (5 - qualidade) * (0.08 + (5 - qualidade) * 0.02)
    facilidade = max(FACILIDADE_MINIMA, facilidade + delta)

    card["facilidade"] = round(facilidade, 2)
    card["repeticoes"] = repeticoes
    card["intervalo"] = intervalo
    card["due"] = (hoje() + datetime.timedelta(days=intervalo)).isoformat()
    card.setdefault("historico", []).append({"data": hoje().isoformat(), "nota": nota})
    return card


def cmd_revisar(args):
    if args.nota not in NOTAS:
        print("nota inválida. use: %s" % " | ".join(NOTAS))
        return 1
    dados = carregar(args.arquivo)
    for card in dados["cards"]:
        if card["id"] == args.id:
            agendar(card, args.nota)
            salvar(args.arquivo, dados)
            print("%s: %s. próxima revisão em %s (intervalo de %d dia(s))"
                  % (card["id"], args.nota, card["due"], card["intervalo"]))
            return 0
    print("cartão %s não encontrado" % args.id)
    return 1


def cmd_stats(args):
    dados = carregar(args.arquivo)
    cards = dados["cards"]
    if not cards:
        print("nenhum cartão ainda.")
        return 0
    novos = [c for c in cards if not c.get("historico")]
    reaprendendo = [c for c in cards if c.get("historico") and c.get("repeticoes", 0) == 0]
    firmes = [c for c in cards if c.get("repeticoes", 0) >= 3 and c.get("intervalo", 0) >= 21]
    teimosos = [c for c in cards if c.get("lapsos", 0) >= 2]
    print("total: %d" % len(cards))
    print("vencendo hoje: %d" % len(vencidos(dados)))
    print("novos (nunca revisados): %d" % len(novos))
    print("reaprendendo (caíram e voltaram ao início): %d" % len(reaprendendo))
    print("firmes (intervalo de 21 dias ou mais): %d" % len(firmes))
    print("teimosos (2 lapsos ou mais): %d" % len(teimosos))
    print("\npróximos 7 dias:")
    for adiante in range(1, 8):
        dia = hoje() + datetime.timedelta(days=adiante)
        quantos = len([c for c in cards if para_data(c["due"]) == dia])
        if quantos:
            print("  %s: %d" % (dia.isoformat(), quantos))
    if teimosos:
        print("\nos teimosos:")
        for card in teimosos[:10]:
            print("  [%s] %s (%d lapsos)" % (card["id"], card["frente"][:60], card["lapsos"]))
    return 0


def cmd_listar(args):
    dados = carregar(args.arquivo)
    cards = dados["cards"]
    if args.topico:
        cards = [c for c in cards if c.get("topico") == args.topico]
    for card in cards:
        print("[%s] (%s) vence %s | %s" % (card["id"], card.get("topico") or "-",
                                           card["due"], card["frente"][:70]))
    print("\n%d cartão(ões)." % len(cards))
    return 0


def main():
    parser = argparse.ArgumentParser(description="Motor de repetição espaçada do AI-TUTOR")
    sub = parser.add_subparsers(dest="comando")

    p_add = sub.add_parser("add", help="cria um cartão")
    p_add.add_argument("arquivo")
    p_add.add_argument("--frente", required=True)
    p_add.add_argument("--verso", required=True)
    p_add.add_argument("--topico", default="")
    p_add.set_defaults(func=cmd_add)

    p_due = sub.add_parser("due", help="lista o que vence hoje")
    p_due.add_argument("arquivo")
    p_due.add_argument("--limite", type=int, default=None)
    p_due.add_argument("--json", action="store_true")
    p_due.set_defaults(func=cmd_due)

    p_rev = sub.add_parser("revisar", help="registra a resposta e reagenda")
    p_rev.add_argument("arquivo")
    p_rev.add_argument("--id", required=True)
    p_rev.add_argument("--nota", required=True, help="errei | dificil | bom | facil")
    p_rev.set_defaults(func=cmd_revisar)

    p_stats = sub.add_parser("stats", help="resumo do baralho")
    p_stats.add_argument("arquivo")
    p_stats.set_defaults(func=cmd_stats)

    p_list = sub.add_parser("listar", help="lista os cartões")
    p_list.add_argument("arquivo")
    p_list.add_argument("--topico", default=None)
    p_list.set_defaults(func=cmd_listar)

    args = parser.parse_args()
    if not args.comando:
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
