---
name: relatorio
description: Use SEMPRE que o trabalho for relatório de resultado de cliente que se monta com dado vivo, não deck chumbado: ligar um cliente/fonte na fundação de relatórios (app-relatorios/report-data, Meta/Google/GA4/Shopify/Blip), o relatório social mensal (orgânico do Instagram + mídia + posts campeões + análise por IA, no visual do cliente), o relatório mensal/trimestral da Aço Cearense (Meta Ads × Salesforce, prova por linha), o comentário/alerta/resumo executivo por IA sobre os números (ai-json), ou quebrar o funil de vendas por vendedor. Dispara com "monta o relatório do <cliente>", "liga o <cliente> na fundação", "puxa os dados vivos", "liga o Instagram do <cliente>", "relatório com os posts campeões", "comenta o desempenho", "escreve o resumo executivo", "tem alguma anomalia?", "alerta quando o ROAS/CPL sair do padrão", "pergunte aos números", "relatório da ACCS", "cruza os leads com o Salesforce", "quebra o funil por vendedor".
---

# relatorio: relatório de cliente com dado vivo, IA e prova

Substitui os decks feitos à mão por relatório que se atualiza sozinho, lê a narrativa por IA e cruza lead com venda. Fundação única (`~/dev/apps/app-relatorios` + edge `report-data` no MinerOS `frocxapiowyjrdhlirnu`), em vez de mais um sistema paralelo. Quem já tem deck HTML estático é o modo [[deck]]; aqui o dado vem da fonte por edge.

## Modos
- **fundação viva** (relatorio-vivo): liga cliente/fonte no `app-relatorios`/`report-data`, com cron e log de freshness.
- **social** (relatorio-social): relatório mensal rico no visual do CLIENTE, com orgânico do Instagram, posts campeões e IA.
- **ACCS** (relatorio-accs): deck de resultado da Aço Cearense cruzando Meta Ads × Salesforce, com prova por linha.
- **comentário/IA** (relatorio-inteligente): transforma o dump de métricas em texto (comentário, alerta, resumo, Q&A) via ai-json.
- **funil por vendedor** (funil-vendedor): quebra o funil de vendas por pessoa; a regra é sempre preencher o array `vendedores`.

## Quando disparar
- Fundação: "monta/atualiza o relatório do <cliente>", "liga o <cliente> na fundação", relatório parado.
- Social: "liga o Instagram", "posts campeões", "orgânico do IG".
- ACCS: "relatório da ACCS", "atualiza o accs-proposta", "cruza os leads com o Salesforce".
- IA (roda sobre os outros): "comenta o desempenho", "resumo executivo", "tem anomalia?", "pergunte aos números".
- Funil: "quebra o funil por vendedor", "funil do <cliente> por SDR".

## Como executar
**Comum:** leia o vault antes ([[obsidianminer]]: conta, token, fonte, o que já está ligado; `reference_fontes_por_cliente`, `reference_contas_meta_ativas`). Nunca invente conta/ID/número. Slug `tipo-cliente`. Deploy `vercel --prod` da última main ([[deploy]]); editar = deployar, confirmar no ar.

**Fundação viva:** o cliente vira entrada em `report_clients` (nome, seg, slug, deck_url, prio) + `report_accounts` (plataforma meta|google, account_id, N contas/cliente, brutos somados e médias recalculadas). Motor Meta: edge `meta-ingestor` (verify_jwt=false, `?key`=ingest_secret) lê contas, puxa `graph.facebook.com/v21.0/act_X/insights` 4 meses, delete+insert em `miner_reports_log` (source=meta_ads); cron `miner-meta-ingestor-daily` (jobid 13, 6h BRT). Google via `windsor-ingestor` (google_ads/ga4/search_console, WINDSOR_API_KEY no cofre; cron jobid 14). Secrets no Vault do MinerOS (`vault.secrets`, `public.get_secret`): `meta_access_token`, `ingest_secret`, `windsor_api_key`. Leitura: `report-data` (`?cliente=CODE&ym=2026-06`, `?r=<slug>` isolado, `?meta=1` catálogo). Entregue sempre o link isolado `?r=slug`, nunca `?cliente=`.

**Social:** template `~/dev/apps/relatorio-social` (estático, no visual do cliente via `theme_primary` no CSS `:root`; azul Hudson default, Normatel laranja), acabamento KV real (`fonts.css` Behind The Nineties + VisbyCF do deck-barneys) via [[minerdesign]]. Peças MinerOS: `instagram-ingestor` (IG Graph API, token do cofre, cron jobid 15) puxa orgânico + top posts pra `report_top_posts`; `ai-insights` monta o dump e grava 5 blocos em `report_insights`; `report-data v7` serve `top_posts`+`insights`. Vivo por `?r=slug` em `relatorio-social.vercel.app` (piloto Normatel `?r=normatel-12bc61`). Orgânico+campeões+IA hoje só no Normatel; ligar outro = cadastrar IG id em `report_accounts` + rodar os dois ingestores.

**ACCS (prova por linha):** repo `~/dev/accs-proposta` (pull antes, push depois; `index.html`=mês, `trimestre.html`=trimestre). Mídia via Meta MCP conta `act_1919182935615902` (leads = action `lead`; conversas = `onsite_conversion.messaging_conversation_started_7d`). Leads brutos = export "FORMS B" `~/Downloads/FORMS B - *.csv` (UTF-16, TAB). Base/orçamentos/pedidos via `sf` CLI org `aco-prospec` (Opportunity=orçamento, Order=pedido). Match: `tools/match_accs.py --since --until --ops-until --out` por e-mail/fone/CNPJ. VENDIDO = pedido faturado (`TotalDelivery`/`NotDelivered`/`PartialDelivery`); `Declined`/`InCreditAnalysis` ficam FORA. Gere números por script a partir do dump, nunca à mão. Contexto e ferramenta: [[salesforce]], histórico em `accs-relatorio-jun26`.

**Comentário/IA (ai-json):** `POST https://stpstwsqtuubpxvvexte.supabase.co/functions/v1/ai-json?key=miner_ai_9f2c7b41` corpo `{ system, user:"<dump+pergunta>", model?:"google/gemini-2.5-flash-lite", temperature?:0.2 }`, resposta `{ ok, data }`. 4 saídas: comentário, alerta de anomalia (mande os limiares no user), resumo executivo, "pergunte aos números". A IA só interpreta o dump. Toda leitura de Meta passa pela lente Breakdown Effect ([[midia]]): não recomende cortar segmento por CPA/CPM médio alto.

**Funil por vendedor:** fonte MinerCRM (filtrado pela org, [[crm]]) ou Salesforce. Para a Aço, repo `~/dev/portal-accs` (array `FAT_DATA` + `vendedores` no `index.html`, ver [[robo]]). REGRA: sempre preencher `vendedores`, nunca `[]`. Estrutura `{ nome, oport, oportClientes, pedidos, recusado, credito, positivado }`. Nomes reais da org (NMPR: Alyssa, Natasha, Andriely; PRLS 3 vendedoras). Confira cada soma contra o KPI-tile.

## Gotchas
- **ai-json não é fonte de número:** valor fora do dump não pode ser citado; peça pra sinalizar lacuna. `ok:false`/texto sujo: baixe a temperature e reforce "só JSON". Sem PII no prompt.
- **`--ops-until` = fim real do período** (não a última data do CSV): em jun/26 cortou R$ 201k de 30/06.
- **ACCS match por nome é PROIBIDO** (cada conta tem várias ops/mês). Telefone no SOQL: SF grava `(86)9411-3538`; use `LIKE '%9411-3538'`. CNPJ em `CNPJNUM__c`/`CPFCNPJNUM__c`. Org tem ~22k ops/mês: nunca somar sem filtrar pelas contas casadas.
- **PII:** o CSV "FORMS B" e `app-relatorios`/`relatorio-social` servem a pasta toda. `tools/` e `rastreio*.json` no `.vercelignore`; zero segredo no front (tudo no edge/cofre). Imagem de post: `referrerpolicy=no-referrer`, sem lazy.
- **Token Meta expira 22/08:** o refresh.sh muda o arquivo, não o cofre; re-sincronizar (`ads-mcp-servers-setup`). **Freshness:** fonte sem cron é print, não é vivo. Omnichat congelada em alguns clientes (Normatel só jun/2022): renovar credencial antes de tratar como viva.
- **Paridade de abas** (mensal↔trimestral, ACCS e vivo): slide novo no mensal replica no trimestral, mesma ordem.
- **Rótulo "Volume Total de Oportunidade (t)"** no funil é enganoso: é `pedidos`, não oportunidade.

## O que NÃO fazer
- NÃO criar mais um repo/sistema de relatório: ligar na fundação `app-relatorios`.
- NÃO chumbar token/credencial no front nem reportar número de fonte que não respondeu (marque a fonte sem dado).
- NÃO deixar a IA inventar número ausente, nem recomendar cortar segmento por CPA/CPM médio alto (Breakdown Effect).
- NÃO entregar funil agregado sem quebra por pessoa, nem `vendedores:[]`; nomes vêm do CRM da org, não da lista da Aço.
- NÃO usar emoji nem travessão em texto de cliente; números com máscara pt-BR.
