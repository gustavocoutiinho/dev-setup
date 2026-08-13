#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Painel de progresso do AI-TUTOR.

Lê os arquivos do curso e gera um painel.html autocontido: árvore de habilidades,
barras de progresso por fase, ofensiva de estudo, estado dos cartões e histórico.

Uso:
  painel.py <pasta-do-curso> [--abrir]

Exemplo:
  python3 painel.py ~/.claude/tutor/estatistica-aplicada --abrir
"""

import argparse
import datetime
import glob
import json
import os
import string
import subprocess
import sys

CLASSE_ESTADO = {
    "concluida": "ok",
    "dispensada": "pulada",
    "em_curso": "agora",
    "revisar": "atencao",
    "pendente": "aberta",
}

ROTULO_ESTADO = {
    "concluida": "concluída",
    "dispensada": "dispensada no diagnóstico",
    "em_curso": "em curso",
    "revisar": "precisa voltar",
    "pendente": "ainda não",
}


def ler_json(caminho, padrao):
    if not os.path.exists(caminho):
        return padrao
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def escapar(texto):
    return (str(texto).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def calcular_ofensiva(sessoes):
    """Dias consecutivos de estudo, contando de hoje (ou de ontem) para trás."""
    dias = set()
    for sessao in sessoes or []:
        try:
            dias.add(datetime.datetime.strptime(sessao["data"], "%Y-%m-%d").date())
        except (KeyError, ValueError, TypeError):
            continue
    if not dias:
        return 0
    hoje = datetime.date.today()
    inicio = hoje if hoje in dias else hoje - datetime.timedelta(days=1)
    if inicio not in dias:
        return 0
    total = 0
    atual = inicio
    while atual in dias:
        total += 1
        atual -= datetime.timedelta(days=1)
    return total


def resumo_cards(cards):
    hoje = datetime.date.today()
    resumo = {"total": len(cards), "vencendo": 0, "firmes": 0, "teimosos": 0}
    for card in cards:
        try:
            due = datetime.datetime.strptime(card["due"], "%Y-%m-%d").date()
        except (KeyError, ValueError, TypeError):
            due = None
        if due and due <= hoje:
            resumo["vencendo"] += 1
        if card.get("repeticoes", 0) >= 3 and card.get("intervalo", 0) >= 21:
            resumo["firmes"] += 1
        if card.get("lapsos", 0) >= 2:
            resumo["teimosos"] += 1
    return resumo


BLOCO_FASE = string.Template("""
        <section class="fase">
          <header>
            <h3>$TITULO</h3>
            $SELO
          </header>
          <div class="barra"><div class="preenchida" style="width:$PCT%"></div></div>
          <p class="contagem">$FEITAS de $TOTAL unidades ($PCT%)</p>
          <ul class="trilha">$NOS</ul>
        </section>""")


def montar_fases(fases):
    blocos = []
    for fase in fases:
        unidades = fase.get("unidades", [])
        feitas = len([u for u in unidades if u.get("status") in ("concluida", "dispensada")])
        pct = int(round(100.0 * feitas / len(unidades))) if unidades else 0

        nos = []
        for unidade in unidades:
            estado = unidade.get("status", "pendente")
            nos.append(
                '<li class="no %s"><span class="bolinha"></span>'
                '<span class="no-txt"><strong>%s</strong><em>%s</em></span></li>'
                % (CLASSE_ESTADO.get(estado, "aberta"),
                   escapar(unidade.get("titulo", unidade.get("id", ""))),
                   ROTULO_ESTADO.get(estado, estado)))

        portao = fase.get("portao") or {}
        estado_portao = portao.get("status", "pendente")
        nota = portao.get("nota")
        complemento = (" com %s%%" % nota) if nota is not None else ""
        if estado_portao == "aprovado":
            selo = '<span class="portao aprovado">portão liberado%s</span>' % complemento
        elif estado_portao == "reprovado":
            selo = '<span class="portao reprovado">portão trancado%s</span>' % complemento
        else:
            selo = '<span class="portao pendente">portão ainda fechado</span>'

        blocos.append(BLOCO_FASE.substitute(
            TITULO=escapar(fase.get("titulo", fase.get("id", "Fase"))),
            SELO=selo, PCT=pct, FEITAS=feitas, TOTAL=len(unidades), NOS="".join(nos)))
    return "".join(blocos)


def montar_historico(pasta):
    linhas = []
    for caminho in sorted(glob.glob(os.path.join(pasta, "aulas", "*.md")), reverse=True)[:8]:
        nome = os.path.basename(caminho)[:-3]
        partes = nome.split("-", 3)
        data = "-".join(partes[:3]) if len(partes) >= 3 else nome
        assunto = partes[3] if len(partes) > 3 else nome
        linhas.append('<li><span class="data">%s</span>%s</li>'
                      % (escapar(data), escapar(assunto.replace("-", " "))))
    return "".join(linhas) or '<li class="vazio">nenhuma aula registrada ainda</li>'


def montar_provas(pasta):
    linhas = []
    for caminho in sorted(glob.glob(os.path.join(pasta, "provas", "*.md")), reverse=True)[:6]:
        nome = os.path.basename(caminho)[:-3]
        linhas.append("<li>%s</li>" % escapar(nome.replace("-", " ")))
    return "".join(linhas) or '<li class="vazio">nenhuma prova aplicada ainda</li>'


PAGINA = string.Template("""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$CURSO | AI-TUTOR</title>
<style>
  :root{
    --fundo:#0b0d12; --cartao:#141822; --borda:#232a38; --texto:#e9ecf4;
    --suave:#9aa4bb; --acento:#7c93ff; --ok:#4ade80; --atencao:#fbbf24; --erro:#f87171;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--fundo);color:var(--texto);
       font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .capa{max-width:1000px;margin:0 auto;padding:40px 20px 80px}
  h1{font-size:30px;margin:0 0 4px;letter-spacing:-.02em}
  .sub{color:var(--suave);margin:0 0 28px;font-size:15px}
  .numeros{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:32px}
  .num{background:var(--cartao);border:1px solid var(--borda);border-radius:14px;padding:16px}
  .num b{display:block;font-size:28px;line-height:1.1;letter-spacing:-.02em}
  .num span{color:var(--suave);font-size:13px}
  .num.destaque b{color:var(--acento)}
  h2{font-size:13px;text-transform:uppercase;letter-spacing:.09em;color:var(--suave);
     margin:34px 0 14px;font-weight:600}
  .fase{background:var(--cartao);border:1px solid var(--borda);border-radius:14px;
        padding:18px;margin-bottom:14px}
  .fase header{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
  .fase h3{margin:0;font-size:17px}
  .portao{font-size:12px;padding:4px 10px;border-radius:999px;border:1px solid var(--borda);white-space:nowrap}
  .portao.aprovado{color:var(--ok);border-color:rgba(74,222,128,.4)}
  .portao.reprovado{color:var(--erro);border-color:rgba(248,113,113,.4)}
  .portao.pendente{color:var(--suave)}
  .barra{height:7px;background:#0a0c11;border-radius:999px;overflow:hidden;margin:14px 0 6px}
  .preenchida{height:100%;background:linear-gradient(90deg,var(--acento),#a5b4fc)}
  .contagem{margin:0 0 12px;color:var(--suave);font-size:13px}
  .trilha{list-style:none;margin:0;padding:0;display:grid;
          grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px}
  .no{display:flex;gap:9px;align-items:flex-start;padding:9px 11px;border-radius:10px;
      background:#0f1219;border:1px solid var(--borda)}
  .bolinha{width:9px;height:9px;border-radius:50%;background:#39415a;margin-top:6px;flex:none}
  .no-txt{display:flex;flex-direction:column;min-width:0}
  .no-txt strong{font-weight:500;font-size:14px}
  .no-txt em{font-style:normal;color:var(--suave);font-size:11.5px}
  .no.ok .bolinha{background:var(--ok)} .no.ok{border-color:rgba(74,222,128,.28)}
  .no.agora .bolinha{background:var(--acento)} .no.agora{border-color:rgba(124,147,255,.4)}
  .no.atencao .bolinha{background:var(--atencao)} .no.atencao{border-color:rgba(251,191,36,.32)}
  .no.pulada .bolinha{background:#4b5468}
  .listas{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
  .lista{background:var(--cartao);border:1px solid var(--borda);border-radius:14px;padding:18px}
  .lista h2{margin-top:0}
  .lista ul{list-style:none;margin:0;padding:0}
  .lista li{padding:7px 0;border-bottom:1px solid #1b2130;font-size:14px}
  .lista li:last-child{border-bottom:0}
  .data{color:var(--acento);font-variant-numeric:tabular-nums;margin-right:8px;font-size:13px}
  .vazio{color:var(--suave)}
  footer{margin-top:40px;color:var(--suave);font-size:12.5px;text-align:center}
  @media (max-width:600px){h1{font-size:24px}.capa{padding:26px 14px 60px}}
</style>
</head>
<body>
<div class="capa">
  <h1>$CURSO</h1>
  <p class="sub">$OBJETIVO</p>

  <div class="numeros">
    <div class="num destaque"><b>$PCT%</b><span>do curso concluído</span></div>
    <div class="num"><b>$OFENSIVA</b><span>dias seguidos estudando</span></div>
    <div class="num"><b>$AULAS</b><span>sessões registradas</span></div>
    <div class="num"><b>$HORAS</b><span>horas de estudo</span></div>
    <div class="num"><b>$CARDS</b><span>cartões no baralho</span></div>
    <div class="num"><b>$VENCENDO</b><span>para revisar hoje</span></div>
  </div>

  <h2>Árvore de habilidades</h2>
  $FASES

  <div class="listas">
    <div class="lista">
      <h2>Últimas aulas</h2>
      <ul>$HISTORICO</ul>
    </div>
    <div class="lista">
      <h2>Provas</h2>
      <ul>$PROVAS</ul>
    </div>
    <div class="lista">
      <h2>Memória</h2>
      <ul>
        <li>$FIRMES cartões já firmes (intervalo de 21 dias ou mais)</li>
        <li>$TEIMOSOS cartões teimosos (errados duas vezes ou mais)</li>
        <li>$VENCENDO vencendo hoje</li>
      </ul>
    </div>
  </div>

  <footer>gerado em $AGORA pelo AI-TUTOR</footer>
</div>
</body>
</html>
""")


def gerar(pasta):
    pasta = os.path.expanduser(pasta)
    progresso = ler_json(os.path.join(pasta, "progresso.json"), {})
    flashcards = ler_json(os.path.join(pasta, "flashcards.json"), {"cards": []})

    fases = progresso.get("fases", [])
    unidades = [u for fase in fases for u in fase.get("unidades", [])]
    feitas = len([u for u in unidades if u.get("status") in ("concluida", "dispensada")])
    pct = int(round(100.0 * feitas / len(unidades))) if unidades else 0

    sessoes = progresso.get("sessoes", [])
    minutos = sum(int(s.get("minutos", 0) or 0) for s in sessoes)
    cards = resumo_cards(flashcards.get("cards", []))

    html = PAGINA.substitute(
        CURSO=escapar(progresso.get("curso", os.path.basename(pasta.rstrip("/")))),
        OBJETIVO=escapar(progresso.get("objetivo", "curso montado pelo AI-TUTOR")),
        PCT=pct,
        OFENSIVA=calcular_ofensiva(sessoes),
        AULAS=len(sessoes),
        HORAS=("%.1f" % (minutos / 60.0)).replace(".", ","),
        CARDS=cards["total"],
        VENCENDO=cards["vencendo"],
        FIRMES=cards["firmes"],
        TEIMOSOS=cards["teimosos"],
        FASES=montar_fases(fases) or '<p class="sub">currículo ainda não montado</p>',
        HISTORICO=montar_historico(pasta),
        PROVAS=montar_provas(pasta),
        AGORA=datetime.datetime.now().strftime("%d/%m/%Y às %H:%M"),
    )

    destino = os.path.join(pasta, "painel.html")
    with open(destino, "w", encoding="utf-8") as arquivo:
        arquivo.write(html)
    return destino


def main():
    parser = argparse.ArgumentParser(description="Gera o painel de progresso do AI-TUTOR")
    parser.add_argument("pasta", help="pasta do curso, por exemplo ~/.claude/tutor/<slug>")
    parser.add_argument("--abrir", action="store_true", help="abre no navegador depois de gerar")
    args = parser.parse_args()

    if not os.path.isdir(os.path.expanduser(args.pasta)):
        print("pasta não encontrada: %s" % args.pasta)
        return 1

    destino = gerar(args.pasta)
    print(destino)
    if args.abrir:
        abridor = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([abridor, destino])
    return 0


if __name__ == "__main__":
    sys.exit(main())
