#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrai o retrato público de perfis concorrentes no Instagram.

Duas fontes, em cascata automática:
  1. graph   Instagram Graph API, endpoint business_discovery (oficial, estável).
             Exige token Meta com instagram_basic + instagram_manage_insights +
             pages_read_engagement, e que o alvo seja conta Business ou Creator.
  2. publico Endpoint público que o site do Instagram usa para montar o perfil.
             Não precisa de token. Não é documentado e quebra em algumas contas.

Só coleta o que é público: seguidores, contagem de posts, curtidas, comentários e
views. Alcance, impressões, salvamentos, stories e demografia não existem para
terceiros em nenhuma fonte.

Uso:
  espiar.py leroymerlinbrasil outbackbrasil
  espiar.py --arquivo handles.txt --saida ~/Documents/benchmark
  espiar.py leroymerlinbrasil --fonte publico --posts 12
  espiar.py --cliente NMTL          (lê os handles de concorrentes.json do motor de decks)
"""

import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

TOKEN_PADRAO = os.path.expanduser("~/.meta-ads/current_token.txt")
CLIENTES_PADRAO = os.path.expanduser("~/dev/decks/deck-normatel-junho/_src/clients.json")
CONCORRENTES_PADRAO = os.path.expanduser("~/dev/decks/deck-normatel-junho/_src/concorrentes.json")
SAIDA_PADRAO = os.path.expanduser("~/.claude/concorrentes")
VERSAO_GRAPH = "v21.0"
APP_ID_WEB = "936619743392459"
UA_WEB = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
          "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")

TIPO_POR_PRODUCT = {"clips": "reels", "igtv": "video", "feed": "post", "ad": "anuncio"}


USO_APP = {"call_count": 0}


def buscar(url, cabecalhos=None, tempo=25):
    """GET que devolve JSON. Em erro HTTP, lê o corpo: a causa real vem nele.
    Guarda o medidor x-app-usage da Meta, que diz o quanto do limite já foi gasto."""
    pedido = urllib.request.Request(url, headers=cabecalhos or {})
    try:
        with urllib.request.urlopen(pedido, timeout=tempo) as resposta:
            medidor = resposta.headers.get("x-app-usage")
            if medidor:
                try:
                    USO_APP.update(json.loads(medidor))
                except ValueError:
                    pass
            return json.loads(resposta.read().decode("utf-8"))
    except urllib.error.HTTPError as falha:
        corpo = ""
        try:
            corpo = falha.read().decode("utf-8", "replace")
        except Exception:
            pass
        detalhe = ""
        try:
            dados = json.loads(corpo)
            detalhe = (dados.get("message")
                       or (dados.get("error") or {}).get("message")
                       or corpo[:200])
        except ValueError:
            detalhe = corpo[:200]
        raise RuntimeError("HTTP %s: %s" % (falha.code, detalhe.strip() or "sem detalhe"))


def ler_token(caminho):
    caminho = os.path.expanduser(caminho)
    if not os.path.exists(caminho):
        return None
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read().strip()


def limpar_handle(bruto):
    bruto = bruto.strip()
    if bruto.startswith("http"):
        bruto = urllib.parse.urlparse(bruto).path
    return bruto.strip("/").lstrip("@").split("/")[0].split("?")[0]


# --------------------------------------------------------------- fonte propria

def contas_do_token(token):
    """Contas Instagram que o token administra. É por aqui que a casa entra no
    benchmark: perfil próprio não depende do endpoint público nem de permissão
    extra para trazer curtidas e comentários."""
    if not token:
        return {}
    url = "https://graph.facebook.com/%s/me/accounts?%s" % (
        VERSAO_GRAPH, urllib.parse.urlencode({
            "fields": "instagram_business_account{id,username}",
            "limit": 200, "access_token": token}))
    try:
        dados = buscar(url)
    except (RuntimeError, urllib.error.URLError, ValueError):
        return {}
    mapa = {}
    for pagina in dados.get("data", []):
        conta = pagina.get("instagram_business_account") or {}
        if conta.get("username") and conta.get("id"):
            mapa[conta["username"].lower()] = conta["id"]
    return mapa


def via_propria(handle, ig_id, token, quantos):
    perfil_url = "https://graph.facebook.com/%s/%s?%s" % (
        VERSAO_GRAPH, ig_id, urllib.parse.urlencode({
            "fields": "username,name,followers_count,follows_count,media_count,"
                      "biography,website,profile_picture_url",
            "access_token": token}))
    bruto = buscar(perfil_url)
    if "error" in bruto:
        raise RuntimeError("propria: %s" % bruto["error"].get("message", "")[:160])

    campos = ("id,caption,media_type,media_product_type,timestamp,permalink,"
              "like_count,comments_count")
    # Insights só voltam com instagram_manage_insights. Sem ela, seguimos sem.
    for tentativa in (campos + ",insights.metric(reach,saved,shares,views)", campos):
        try:
            midia = buscar("https://graph.facebook.com/%s/%s/media?%s" % (
                VERSAO_GRAPH, ig_id, urllib.parse.urlencode({
                    "fields": tentativa, "limit": quantos, "access_token": token})))
            if "error" not in midia:
                break
        except RuntimeError:
            midia = None
    if not midia or "error" in (midia or {}):
        raise RuntimeError("propria: não consegui listar a mídia")

    posts = []
    for item in midia.get("data", []):
        tipo = TIPO_POR_PRODUCT.get((item.get("media_product_type") or "").lower())
        if not tipo:
            tipo = {"VIDEO": "video", "CAROUSEL_ALBUM": "carrossel",
                    "IMAGE": "post"}.get(item.get("media_type", ""), "post")
        medidas = {}
        for medida in (item.get("insights") or {}).get("data", []):
            valores = medida.get("values") or [{}]
            medidas[medida.get("name")] = valores[0].get("value")
        posts.append({
            "id": item.get("id"),
            "link": item.get("permalink"),
            "tipo": tipo,
            "publicado_em": item.get("timestamp"),
            "legenda": (item.get("caption") or "")[:400],
            "curtidas": item.get("like_count"),
            "comentarios": item.get("comments_count"),
            "views": medidas.get("views"),
            "alcance": medidas.get("reach"),
            "salvamentos": medidas.get("saved"),
            "compartilhamentos": medidas.get("shares"),
        })
    perfil = {
        "nome": bruto.get("name"),
        "seguidores": bruto.get("followers_count"),
        "segue": bruto.get("follows_count"),
        "posts_total": bruto.get("media_count"),
        "bio": bruto.get("biography"),
        "site": bruto.get("website"),
        "foto": bruto.get("profile_picture_url"),
    }
    return perfil, posts


# ------------------------------------------------------------ histórico fundo

def id_publico(handle):
    dados = buscar("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"
                   % urllib.parse.quote(handle),
                   {"User-Agent": UA_WEB, "X-IG-App-ID": APP_ID_WEB})
    usuario = (dados.get("data") or {}).get("user") or {}
    if not usuario.get("id"):
        raise RuntimeError("não achei o id numérico do perfil")
    return usuario["id"], usuario


def historico_publico(handle, teto, pausa, avisar=None):
    """Pagina o feed público até o teto de posts (0 = até acabar).
    12 posts por página. Perfil com milhares de posts leva minutos."""
    user_id, usuario = id_publico(handle)
    posts = []
    cursor = None
    paginas = 0
    while True:
        url = "https://i.instagram.com/api/v1/feed/user/%s/?count=50" % user_id
        if cursor:
            url += "&max_id=%s" % urllib.parse.quote(cursor)
        # O Instagram devolve 401 "wait a few minutes" quando a paginação
        # acelera. Não adianta insistir na hora: espera e tenta de novo.
        pagina = None
        for espera in (0, 90, 180, 300):
            if espera:
                if avisar:
                    avisar("  limite do Instagram, esperando %ds (tenho %d posts)"
                           % (espera, len(posts)))
                time.sleep(espera)
            try:
                pagina = buscar(url, {"User-Agent": UA_WEB, "X-IG-App-ID": APP_ID_WEB})
                break
            except RuntimeError as falha:
                texto = str(falha)
                if "401" not in texto and "429" not in texto:
                    if not posts:
                        raise
                    if avisar:
                        avisar("  parei em %d posts: %s" % (len(posts), texto[:80]))
                    pagina = None
                    break
        if pagina is None:
            if not posts:
                raise RuntimeError("publico: limite de requisições do Instagram")
            if avisar:
                avisar("  parei em %d posts por limite de requisições" % len(posts))
            break
        itens = pagina.get("items") or []
        if not itens:
            break
        for item in itens:
            carimbo = item.get("taken_at")
            produto = (item.get("product_type") or "").lower()
            tipo = TIPO_POR_PRODUCT.get(produto)
            if not tipo:
                tipo = {8: "carrossel", 2: "video", 1: "post"}.get(item.get("media_type"), "post")
            legenda = ((item.get("caption") or {}) or {}).get("text") or ""
            posts.append({
                "id": item.get("pk") or item.get("id"),
                "link": ("https://www.instagram.com/p/%s/" % item["code"]) if item.get("code") else None,
                "tipo": tipo,
                "publicado_em": (datetime.datetime.utcfromtimestamp(carimbo).isoformat() + "+0000"
                                 if carimbo else None),
                "legenda": legenda[:400],
                "curtidas": item.get("like_count"),
                "comentarios": item.get("comment_count"),
                "views": item.get("play_count") or item.get("view_count"),
            })
        paginas += 1
        if avisar and paginas % 10 == 0:
            avisar("  ... %d posts varridos" % len(posts))
        if teto and len(posts) >= teto:
            posts = posts[:teto]
            break
        if not pagina.get("more_available") or not pagina.get("next_max_id"):
            break
        cursor = str(pagina["next_max_id"])
        time.sleep(pausa)
    return usuario, posts


def historico_graph(handle, ig_user_id, token, teto, pausa, avisar=None, parar_antes_de=None):
    """Varre o histórico do concorrente pela via oficial (business_discovery).
    Pagina com cursores, sem o bloqueio agressivo do endpoint público.

    parar_antes_de encerra a varredura quando a página já ficou mais antiga que a
    data pedida. Para analisar a janela de um evento, não faz sentido (nem cabe na
    cota da Meta) baixar sete anos de perfil para usar trinta dias."""
    posts = []
    perfil = None
    cursor = None
    while True:
        recorte = "media.limit(50)" + (".after(%s)" % cursor if cursor else "")
        campos = ("business_discovery.username(%s){username,name,followers_count,"
                  "follows_count,media_count,biography,website,profile_picture_url,"
                  "%s{id,caption,like_count,comments_count,media_type,"
                  "media_product_type,timestamp,permalink}}" % (handle, recorte))
        dados = buscar("https://graph.facebook.com/%s/%s?%s" % (
            VERSAO_GRAPH, ig_user_id,
            urllib.parse.urlencode({"fields": campos, "access_token": token})))
        if "error" in dados:
            raise RuntimeError("graph %s: %s" % (dados["error"].get("code"),
                                                 dados["error"].get("message", "")[:160]))
        bruto = dados.get("business_discovery") or {}
        if not bruto:
            raise RuntimeError("graph: resposta sem business_discovery")
        if perfil is None:
            perfil = {
                "nome": bruto.get("name"),
                "seguidores": bruto.get("followers_count"),
                "segue": bruto.get("follows_count"),
                "posts_total": bruto.get("media_count"),
                "bio": bruto.get("biography"),
                "site": bruto.get("website"),
                "foto": bruto.get("profile_picture_url"),
            }
        midia = bruto.get("media") or {}
        itens = midia.get("data") or []
        if not itens:
            break
        for item in itens:
            tipo = TIPO_POR_PRODUCT.get((item.get("media_product_type") or "").lower())
            if not tipo:
                tipo = {"VIDEO": "video", "CAROUSEL_ALBUM": "carrossel",
                        "IMAGE": "post"}.get(item.get("media_type", ""), "post")
            posts.append({
                "id": item.get("id"),
                "link": item.get("permalink"),
                "tipo": tipo,
                "publicado_em": item.get("timestamp"),
                "legenda": (item.get("caption") or "")[:400],
                "curtidas": item.get("like_count"),
                "comentarios": item.get("comments_count"),
                "views": None,
            })
        if avisar and len(posts) % 200 < 50:
            avisar("  ... %d posts varridos (uso do app: %s%%)"
                   % (len(posts), USO_APP.get("call_count")))
        if parar_antes_de and posts:
            mais_antigo = (posts[-1].get("publicado_em") or "")[:10]
            if mais_antigo and mais_antigo < parar_antes_de:
                if avisar:
                    avisar("  cheguei em %s, que é antes de %s: paro aqui"
                           % (mais_antigo, parar_antes_de))
                break
        if teto and len(posts) >= teto:
            posts = posts[:teto]
            break
        # O business_discovery devolve o cursor "after" mas nem sempre o "next":
        # exigir os dois faz a varredura parar na primeira página.
        anterior = cursor
        cursor = ((midia.get("paging") or {}).get("cursors") or {}).get("after")
        if not cursor or cursor == anterior:
            break
        # O limite do app é por hora. Chegar em 100% derruba tudo com erro #4,
        # então freia antes em vez de bater no muro e perder a varredura.
        if USO_APP.get("call_count", 0) >= 60:
            if avisar:
                avisar("  uso do app em %s%%, pausando 15 min para não estourar"
                       % USO_APP.get("call_count"))
            time.sleep(900)
        else:
            time.sleep(pausa)
    return perfil, posts


def historico_proprio(ig_id, token, teto, pausa, avisar=None):
    """Pagina /media da conta própria. Aqui o histórico é completo de verdade."""
    campos = ("id,caption,media_type,media_product_type,timestamp,permalink,"
              "like_count,comments_count")
    url = "https://graph.facebook.com/%s/%s/media?%s" % (
        VERSAO_GRAPH, ig_id, urllib.parse.urlencode({
            "fields": campos, "limit": 100, "access_token": token}))
    posts = []
    while url:
        pagina = buscar(url)
        if "error" in pagina:
            raise RuntimeError("propria: %s" % pagina["error"].get("message", "")[:160])
        for item in pagina.get("data", []):
            tipo = TIPO_POR_PRODUCT.get((item.get("media_product_type") or "").lower())
            if not tipo:
                tipo = {"VIDEO": "video", "CAROUSEL_ALBUM": "carrossel",
                        "IMAGE": "post"}.get(item.get("media_type", ""), "post")
            posts.append({
                "id": item.get("id"),
                "link": item.get("permalink"),
                "tipo": tipo,
                "publicado_em": item.get("timestamp"),
                "legenda": (item.get("caption") or "")[:400],
                "curtidas": item.get("like_count"),
                "comentarios": item.get("comments_count"),
                "views": None,
            })
        if avisar and len(posts) % 300 < 100:
            avisar("  ... %d posts varridos" % len(posts))
        if teto and len(posts) >= teto:
            posts = posts[:teto]
            break
        url = (pagina.get("paging") or {}).get("next")
        if url:
            time.sleep(pausa)
    return posts


# ---------------------------------------------------------------- fonte graph

def via_graph(handle, ig_user_id, token, quantos):
    campos = (
        "business_discovery.username(%s){username,name,followers_count,follows_count,"
        "media_count,biography,website,profile_picture_url,"
        "media.limit(%d){id,caption,like_count,comments_count,media_type,"
        "media_product_type,timestamp,permalink}}" % (handle, quantos))
    url = "https://graph.facebook.com/%s/%s?%s" % (
        VERSAO_GRAPH, ig_user_id,
        urllib.parse.urlencode({"fields": campos, "access_token": token}))
    dados = buscar(url)
    if "error" in dados:
        erro = dados["error"]
        raise RuntimeError("graph %s: %s" % (erro.get("code"), erro.get("message", "")[:160]))
    bruto = dados.get("business_discovery") or {}
    if not bruto:
        raise RuntimeError("graph: resposta sem business_discovery")

    posts = []
    for item in (bruto.get("media") or {}).get("data", []):
        tipo = TIPO_POR_PRODUCT.get((item.get("media_product_type") or "").lower())
        if not tipo:
            tipo = {"VIDEO": "video", "CAROUSEL_ALBUM": "carrossel",
                    "IMAGE": "post"}.get(item.get("media_type", ""), "post")
        posts.append({
            "id": item.get("id"),
            "link": item.get("permalink"),
            "tipo": tipo,
            "publicado_em": item.get("timestamp"),
            "legenda": (item.get("caption") or "")[:400],
            "curtidas": item.get("like_count"),
            "comentarios": item.get("comments_count"),
            "views": None,
        })
    perfil = {
        "nome": bruto.get("name"),
        "seguidores": bruto.get("followers_count"),
        "segue": bruto.get("follows_count"),
        "posts_total": bruto.get("media_count"),
        "bio": bruto.get("biography"),
        "site": bruto.get("website"),
        "foto": bruto.get("profile_picture_url"),
    }
    return perfil, posts


# -------------------------------------------------------------- fonte publica

def via_publico(handle, quantos):
    url = ("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"
           % urllib.parse.quote(handle))
    dados = buscar(url, {"User-Agent": UA_WEB, "X-IG-App-ID": APP_ID_WEB})
    if dados.get("message"):
        raise RuntimeError("publico: %s" % str(dados["message"])[:160])
    usuario = (dados.get("data") or {}).get("user")
    if not usuario:
        raise RuntimeError("publico: perfil vazio, privado ou inexistente")

    posts = []
    grade = (usuario.get("edge_owner_to_timeline_media") or {}).get("edges", [])
    for aresta in grade[:quantos]:
        no = aresta.get("node", {})
        tipo = TIPO_POR_PRODUCT.get((no.get("product_type") or "").lower())
        if not tipo:
            tipo = {"GraphSidecar": "carrossel", "GraphVideo": "video",
                    "GraphImage": "post"}.get(no.get("__typename", ""), "post")
        legenda = ""
        legendas = (no.get("edge_media_to_caption") or {}).get("edges", [])
        if legendas:
            legenda = legendas[0].get("node", {}).get("text", "")
        carimbo = no.get("taken_at_timestamp")
        posts.append({
            "id": no.get("id"),
            "link": "https://www.instagram.com/p/%s/" % no.get("shortcode") if no.get("shortcode") else None,
            "tipo": tipo,
            "publicado_em": (datetime.datetime.utcfromtimestamp(carimbo).isoformat() + "+0000"
                             if carimbo else None),
            "legenda": legenda[:400],
            "curtidas": (no.get("edge_liked_by") or {}).get("count"),
            "comentarios": (no.get("edge_media_to_comment") or {}).get("count"),
            "views": no.get("video_view_count"),
        })
    perfil = {
        "nome": usuario.get("full_name"),
        "seguidores": (usuario.get("edge_followed_by") or {}).get("count"),
        "segue": (usuario.get("edge_follow") or {}).get("count"),
        "posts_total": (usuario.get("edge_owner_to_timeline_media") or {}).get("count"),
        "bio": usuario.get("biography"),
        "site": usuario.get("external_url"),
        "foto": usuario.get("profile_pic_url_hd") or usuario.get("profile_pic_url"),
        "verificado": usuario.get("is_verified"),
        "conta_business": usuario.get("is_business_account"),
        "categoria": usuario.get("category_name"),
    }
    return perfil, posts


# ------------------------------------------------------------------- análise

DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]


def mediana(valores):
    ordenados = sorted(valores)
    if not ordenados:
        return 0
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2.0


def para_data(texto):
    if not texto:
        return None
    texto = re.sub(r"\+0000$", "+00:00", texto)
    try:
        return datetime.datetime.fromisoformat(texto)
    except ValueError:
        return None


def analisar(perfil, posts, fuso_horas, quantos_top=3):
    seguidores = perfil.get("seguidores") or 0
    formatos = {}
    por_dia = {}
    por_hora = {}
    datas = []

    for post in posts:
        interacoes = (post.get("curtidas") or 0) + (post.get("comentarios") or 0)
        post["interacoes"] = interacoes
        post["taxa_engajamento"] = (round(100.0 * interacoes / seguidores, 2)
                                    if seguidores else None)
        formatos[post["tipo"]] = formatos.get(post["tipo"], 0) + 1
        quando = para_data(post.get("publicado_em"))
        if quando:
            local = quando + datetime.timedelta(hours=fuso_horas)
            post["publicado_local"] = local.strftime("%Y-%m-%d %H:%M")
            datas.append(local)
            dia = DIAS[local.weekday()]
            por_dia[dia] = por_dia.get(dia, 0) + 1
            por_hora[local.hour] = por_hora.get(local.hour, 0) + 1

    resumo = {
        "posts_analisados": len(posts),
        "mix_formatos": formatos,
        "publicacoes_por_dia_da_semana": por_dia,
        "publicacoes_por_hora": por_hora,
    }

    if datas:
        datas.sort()
        resumo["periodo_analisado"] = {"de": datas[0].strftime("%Y-%m-%d"),
                                       "ate": datas[-1].strftime("%Y-%m-%d")}
        intervalo = (datas[-1] - datas[0]).days or 1
        resumo["cadencia_posts_por_semana"] = round(len(datas) / (intervalo / 7.0), 1)
        resumo["cadencia_posts_por_mes"] = round(len(datas) / (intervalo / 30.0), 1)

    com_taxa = [p for p in posts if p.get("taxa_engajamento") is not None]
    if com_taxa:
        media = sum(p["taxa_engajamento"] for p in com_taxa) / len(com_taxa)
        resumo["taxa_engajamento_media"] = round(media, 2)
        resumo["taxa_engajamento_mediana"] = mediana(
            [p["taxa_engajamento"] for p in com_taxa])
        resumo["interacoes_media_por_post"] = round(
            sum(p["interacoes"] for p in com_taxa) / float(len(com_taxa)))
        resumo["interacoes_mediana_por_post"] = round(
            mediana([p["interacoes"] for p in com_taxa]))
        # Um viral sozinho puxa a média e faz o perfil parecer melhor do que é.
        # A mediana é a leitura honesta do dia a dia; o aviso marca a distorção.
        if resumo["interacoes_mediana_por_post"]:
            razao = resumo["interacoes_media_por_post"] / float(resumo["interacoes_mediana_por_post"])
            if razao >= 3:
                resumo["aviso_outlier"] = (
                    "a média é %.1f vezes a mediana: existe post viral distorcendo. "
                    "Use a mediana para comparar o dia a dia." % razao)
        campeoes = sorted(com_taxa, key=lambda p: p["interacoes"], reverse=True)[:quantos_top]
        resumo["top_posts"] = [
            {"posicao": i + 1, "link": p["link"], "tipo": p["tipo"],
             "interacoes": p["interacoes"], "curtidas": p.get("curtidas"),
             "comentarios": p.get("comentarios"), "views": p.get("views"),
             "taxa_engajamento": p["taxa_engajamento"],
             "publicado": p.get("publicado_local"),
             "legenda": (p.get("legenda") or "")[:160]}
            for i, p in enumerate(campeoes)]
    return resumo


# ------------------------------------------------------------------ execução

def coletar(handle, opcoes, ig_user_id, token, minhas_contas=None):
    minhas_contas = minhas_contas or {}
    meu_id = minhas_contas.get(handle.lower())

    tentativas = []
    if meu_id and opcoes.fonte in ("auto", "propria") and token:
        tentativas.append("propria")
    if opcoes.fonte in ("auto", "graph") and ig_user_id and token:
        tentativas.append("graph")
    if opcoes.fonte in ("auto", "publico"):
        tentativas.append("publico")
    if not tentativas:
        return {"handle": handle, "erro": "nenhuma fonte disponível para a opção escolhida"}

    erros = []
    for fonte in tentativas:
        try:
            if opcoes.historico is not None and fonte in ("propria", "graph", "publico"):
                aviso = (lambda t: print(t)) if not opcoes.silencioso else None
                if fonte == "graph":
                    perfil, posts = historico_graph(handle, ig_user_id, token,
                                                    opcoes.historico, opcoes.pausa_pagina, aviso,
                                                    opcoes.ate_data)
                elif fonte == "propria":
                    posts = historico_proprio(meu_id, token, opcoes.historico,
                                              opcoes.pausa_pagina, aviso)
                    perfil, _ = via_propria(handle, meu_id, token, 1)
                else:
                    usuario, posts = historico_publico(handle, opcoes.historico,
                                                       opcoes.pausa_pagina, aviso)
                    perfil = {
                        "nome": usuario.get("full_name"),
                        "seguidores": (usuario.get("edge_followed_by") or {}).get("count"),
                        "segue": (usuario.get("edge_follow") or {}).get("count"),
                        "posts_total": (usuario.get("edge_owner_to_timeline_media") or {}).get("count"),
                        "bio": usuario.get("biography"),
                        "site": usuario.get("external_url"),
                        "verificado": usuario.get("is_verified"),
                        "conta_business": usuario.get("is_business_account"),
                    }
            elif fonte == "propria":
                perfil, posts = via_propria(handle, meu_id, token, opcoes.posts)
            elif fonte == "graph":
                perfil, posts = via_graph(handle, ig_user_id, token, opcoes.posts)
            else:
                perfil, posts = via_publico(handle, opcoes.posts)
            return {
                "handle": handle,
                "url": "https://www.instagram.com/%s" % handle,
                "fonte": fonte,
                "coletado_em": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "perfil": perfil,
                "resumo": analisar(perfil, posts, opcoes.fuso, opcoes.top),
                "posts": posts,
            }
        except (RuntimeError, urllib.error.URLError, urllib.error.HTTPError,
                ValueError, KeyError) as falha:
            erros.append("%s: %s" % (fonte, falha))
    return {"handle": handle, "erro": " | ".join(erros)}


def imprimir(retrato):
    if retrato.get("erro"):
        print("\n%-22s NÃO COLETADO" % ("@" + retrato["handle"]))
        print("  motivo: %s" % retrato["erro"])
        return
    perfil = retrato["perfil"]
    resumo = retrato["resumo"]
    print("\n@%s (%s) via %s" % (retrato["handle"], perfil.get("nome") or "sem nome", retrato["fonte"]))
    print("  seguidores: %s | posts no perfil: %s" % (
        "{:,}".format(perfil["seguidores"]).replace(",", ".") if perfil.get("seguidores") else "?",
        perfil.get("posts_total") or "?"))
    if resumo.get("cadencia_posts_por_mes"):
        print("  cadência: %s posts por mês (%s por semana)" % (
            resumo["cadencia_posts_por_mes"], resumo["cadencia_posts_por_semana"]))
    if resumo.get("taxa_engajamento_media") is not None:
        print("  engajamento: mediana %s%% (%s interações) | média %s%% (%s interações)" % (
            resumo.get("taxa_engajamento_mediana"), resumo.get("interacoes_mediana_por_post"),
            resumo["taxa_engajamento_media"], resumo.get("interacoes_media_por_post")))
    if resumo.get("aviso_outlier"):
        print("  atenção: %s" % resumo["aviso_outlier"])
    if resumo.get("mix_formatos"):
        print("  formatos: %s" % ", ".join("%s %d" % (k, v) for k, v in
                                           sorted(resumo["mix_formatos"].items(),
                                                  key=lambda x: -x[1])))
    campeoes = resumo.get("top_posts", [])
    if campeoes:
        print("  campeões (%d de %d posts varridos):" % (len(campeoes), resumo["posts_analisados"]))
        for post in campeoes:
            print("   %2d. %7s interações (%s%%) %-9s %s  %s" % (
                post["posicao"], "{:,}".format(post["interacoes"]).replace(",", "."),
                post["taxa_engajamento"], post["tipo"], post.get("publicado") or "",
                post["link"] or ""))


def carregar_handles(opcoes):
    handles = [limpar_handle(h) for h in opcoes.handles]
    if opcoes.arquivo:
        with open(os.path.expanduser(opcoes.arquivo), "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha and not linha.startswith("#"):
                    handles.append(limpar_handle(linha))
    if opcoes.cliente:
        caminho = os.path.expanduser(opcoes.concorrentes)
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as arquivo:
                mapa = json.load(arquivo)
            for handle in mapa.get(opcoes.cliente.upper(), []):
                handles.append(limpar_handle(handle))
        else:
            print("aviso: %s não encontrado" % caminho)
    vistos = set()
    unicos = []
    for handle in handles:
        if handle and handle.lower() not in vistos:
            vistos.add(handle.lower())
            unicos.append(handle)
    return unicos


def descobrir_ig_user_id(opcoes):
    if opcoes.ig_user_id:
        return opcoes.ig_user_id
    caminho = os.path.expanduser(opcoes.clientes)
    if not os.path.exists(caminho):
        return None
    with open(caminho, "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)
    alvo = (opcoes.cliente or "").upper()
    if alvo and isinstance(clientes.get(alvo), dict):
        candidato = str(clientes[alvo].get("ig_user_id") or "")
        if candidato.isdigit():
            return candidato
    for dados in clientes.values():
        if isinstance(dados, dict) and str(dados.get("ig_user_id") or "").isdigit():
            return str(dados["ig_user_id"])
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Extrai o retrato público de concorrentes no Instagram")
    parser.add_argument("handles", nargs="*", help="@ dos concorrentes (com ou sem @, aceita URL)")
    parser.add_argument("--arquivo", help="arquivo texto com um handle por linha")
    parser.add_argument("--cliente", help="código do cliente para ler o concorrentes.json do motor de decks")
    parser.add_argument("--fonte", choices=["auto", "propria", "graph", "publico"], default="auto")
    parser.add_argument("--posts", type=int, default=25, help="quantos posts recentes analisar")
    parser.add_argument("--fuso", type=float, default=-3.0, help="fuso do cliente em horas (padrão -3)")
    parser.add_argument("--saida", default=SAIDA_PADRAO, help="pasta onde gravar os JSON")
    parser.add_argument("--token", default=TOKEN_PADRAO)
    parser.add_argument("--ig-user-id", dest="ig_user_id")
    parser.add_argument("--clientes", default=CLIENTES_PADRAO)
    parser.add_argument("--concorrentes", default=CONCORRENTES_PADRAO)
    parser.add_argument("--pausa", type=float, default=2.0, help="segundos entre perfis")
    parser.add_argument("--historico", type=int, nargs="?", const=0, default=None,
                        help="varre o histórico do perfil; sem número = até o fim, "
                             "com número = teto de posts (ex: --historico 600)")
    parser.add_argument("--top", type=int, default=3, help="quantos posts campeões listar")
    parser.add_argument("--pausa-pagina", dest="pausa_pagina", type=float, default=1.2,
                        help="segundos entre páginas do histórico")
    parser.add_argument("--ate-data", dest="ate_data", default=None,
                        help="para de varrer ao passar desta data (AAAA-MM-DD). "
                             "Use a borda da janela que você vai analisar.")
    parser.add_argument("--silencioso", action="store_true")
    opcoes = parser.parse_args()

    handles = carregar_handles(opcoes)
    if not handles:
        parser.print_help()
        return 1

    token = ler_token(opcoes.token)
    ig_user_id = descobrir_ig_user_id(opcoes)
    if opcoes.fonte in ("auto", "graph") and not (token and ig_user_id):
        print("aviso: sem token ou ig_user_id, indo direto para a fonte pública")

    pasta = os.path.join(os.path.expanduser(opcoes.saida),
                         datetime.date.today().isoformat())
    if not os.path.isdir(pasta):
        os.makedirs(pasta)

    minhas_contas = contas_do_token(token) if opcoes.fonte in ("auto", "propria") else {}
    minhas_na_lista = [h for h in handles if h.lower() in minhas_contas]
    if minhas_na_lista:
        print("contas próprias reconhecidas (vão pela via oficial): %s" %
              ", ".join("@" + h for h in minhas_na_lista))

    retratos = []
    for indice, handle in enumerate(handles):
        retrato = coletar(handle, opcoes, ig_user_id, token, minhas_contas)
        retratos.append(retrato)
        imprimir(retrato)
        destino = os.path.join(pasta, "%s.json" % handle)
        with open(destino, "w", encoding="utf-8") as arquivo:
            json.dump(retrato, arquivo, ensure_ascii=False, indent=2)
        if indice < len(handles) - 1:
            time.sleep(opcoes.pausa)

    consolidado = os.path.join(pasta, "_consolidado.json")
    with open(consolidado, "w", encoding="utf-8") as arquivo:
        json.dump(retratos, arquivo, ensure_ascii=False, indent=2)

    falhas = len([r for r in retratos if r.get("erro")])
    print("\n%d perfil(is) coletado(s), %d falha(s). Arquivos em %s" %
          (len(retratos) - falhas, falhas, pasta))
    return 0


if __name__ == "__main__":
    sys.exit(main())
