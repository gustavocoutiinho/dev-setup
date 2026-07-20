---
name: midia
description: "Use SEMPRE que o trabalho for mídia paga (Meta Ads, Google Ads): analisar/diagnosticar performance de campanha (ROAS, CPA, breakdown effect), definir estratégia e estrutura de campanha (público, criativo, copy, budget, Pixel, negativas), montar o mapa de investimento/distribuição de verba por canal e região, a análise mensal de concorrência (Ad Library) ou executar/publicar campanha via AdKit. Dispara com 'analisa a campanha', 'diagnostica o Meta Ads', 'por que o ROAS caiu', 'estratégia de mídia', 'estrutura de campanha', 'monta o mapa de investimento', 'distribui a verba', 'análise de concorrência', 'o que o concorrente tá anunciando', 'cria/sobe a campanha no Meta ou Google'."
---

# midia: mídia paga da Miner (Meta + Google), da estratégia à concorrência

Mídia paga é entrega recorrente em quase todo cliente Miner. Esta skill cobre o ciclo inteiro: diagnosticar performance (com o Breakdown Effect), desenhar estratégia e estrutura de campanha, montar o mapa de investimento, a análise mensal de concorrência e executar via AdKit. Tudo ancorado no gasto real do Windsor (cobre 37 contas Meta + 6 Google Ads), nunca em chute.

## Modos
- **análise/diagnóstico Meta**: interpretar performance, achar causa-raiz e recomendar, com foco no Breakdown Effect (custo marginal, não médio).
- **estratégia Meta**: estrutura de campanha, criativo, copy, público, budget e Pixel para Facebook/Instagram.
- **estratégia Google**: Search Ads, keyword mining, estrutura de conta, negativas, RSA e smart bidding.
- **mapa de investimento**: distribuir verba por canal, região, categoria e campanha, amarrado ao objetivo do contrato.
- **concorrência**: benchmark mensal de engajamento por segmento + anúncios no ar via Ad Library.
- **execução (AdKit)**: criar/publicar campanha, ad set/group e anúncio; draft-first.

## Quando disparar
- "analisa/diagnostica a campanha", "por que o ROAS/CPA piorou", "o Meta Ads tá ruim".
- "estratégia de mídia", "estrutura de campanha", "como estruturar o Google Ads".
- "monta o mapa de investimento", "distribui a verba", "planejamento de investimento de mídia" (tasks NMTL, OTRH e cia).
- "análise de concorrência", "o que o concorrente tá anunciando", "benchmark do mês".
- "cria/sobe a campanha", quando o AdKit está conectado e é hora de publicar.

## Como executar
Sempre: puxe o cliente no [[obsidianminer]] e o gasto/resultado real do Windsor (janela dos últimos 30 dias). Nunca invente verba. Entregue no visual do cliente com mês explícito (slide de metas no [[deck]], card no portal, ou planilha); a leitura em texto dos números sai pelo [[relatorio]] e a automação recorrente pelo [[robo]].

- **Análise Meta:** primeiro identifique o nível de avaliação correto (Advantage+/CBO = campanha; placements automáticos sem CBO = ad set; vários anúncios num ad set = ad set) para não cair no Breakdown Effect. Cheque learning phase (~50 eventos). Analise custo **marginal**, não média. Interprete tudo pela lente do Breakdown Effect e alinhe com `get_recommendations` antes de divergir. Nomeie métrica certo: "Clicks (all)" vs "Link Clicks"; público é "Accounts Center accounts", nunca "people".
- **Estratégia Meta:** criativo é a alavanca nº 1 (auction = Bid x Estimated Action Rate x Ad Quality); targeting broad; Pixel antes de tudo; objetivo **Sales** em ~90% (nunca Tráfego). Conta nova: warmup $2-5/dia por uns dias, depois escala 10-20% a cada 48h.
- **Estratégia Google:** relevância keyword→anúncio→LP vence (Ad Strength é vaidade); campanhas por intenção, ad groups por tema; arquitetura de negativas ANTES de subir; conversion tracking antes de smart bidding; Search Term Report semanal por 60 dias.
- **Mapa de investimento:** use o molde canônico da ACCS (`Mapa de investimento - Aço Cearense.xlsx`, divide por região P1/P2/P3 e produto). Cada fatia tem objetivo + o que mede + onde chegou. Verba por marca vive em `investmentPlan` no pimfood.
- **Concorrência:** benchmark de engajamento por segmento via CSV do Social Tracker; Ad Library (site) pra ver quem está no ar, tempo no ar e nº de variações. Override do Gustavo: pras marcas que a Miner atende (Barney's/Estela/Olli's), usar "Interações totais" do Reportei, não o Social Tracker, e rotular a fonte. Benchmarks reais: food Fortaleza mai/2026, Estela **+66,4%**, Olli's **+41,7%** entre as locais em alta.
- **Execução AdKit:** cheque `adkit status`; se conectado, use MCP/CLI; senão, faça pela UI nativa. Draft-first sempre.

## Gotchas
- **Breakdown Effect:** NUNCA recomende pausar/cortar um segmento só por CPA/CPM médio mais alto. Média mais alta não é performance ruim; cortar pode subir o custo total. Enquadre como hipótese testável.
- Cliente que roda mídia por agência (Hidrotintas via Mulato) não expõe API direta do Meta: o número vem do Windsor ou da planilha CSV.
- Gasto do Windsor é dos últimos 30 dias: confira a janela antes de projetar.
- "Engajamento total" (Social Tracker) ≠ "Interações totais" (Reportei): rotule qual é qual no slide.
- Ad Library agrupa por anunciante e devolve o criativo destaque: deduplique por md5 do vídeo.
- Conta Meta nova sem warmup dispara detecção de fraude e BANE.

## O que NÃO fazer
- NÃO propor distribuição nem recomendação sem ancorar no gasto/resultado real.
- NÃO extrapolar ritmo de amostra parcial pro mês inteiro (regra Normatel).
- NÃO reaproveitar CSV do mês anterior com rótulo novo; sem dado do mês, marque a fonte como pendente.
- NÃO usar objetivo Tráfego; não misturar segmentos no mesmo ranking de concorrência.
- NÃO publicar campanha pelo AdKit sem aprovação explícita do Gustavo.
- NÃO inventar métrica de concorrente que a fonte não deu (Ad Library não expõe verba comercial).
