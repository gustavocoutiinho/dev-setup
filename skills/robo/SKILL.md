---
name: robo
description: Use SEMPRE que for armar/ligar/consertar uma automação recorrente da Miner: robô de relatório semanal por cliente, checador diário de "os anúncios estão rodando", funil de vendas diário (Aço Cearense), ingestor do Windsor.ai pro banco, ou emissão recorrente de NF/boleto de mídia. Dispara com "liga o relatório semanal do <cliente>", "arma o robô", "valida se os anúncios estão rodando", "automatiza o funil diário", "roda o /funil-aco", "liga o Windsor", "emite a NF dos anúncios", "desliga o robô do ex-cliente".
---

# robo: automações recorrentes da Miner num trilho só

A Miner tem tarefas que reaparecem toda semana ou todo dia e deveriam ser cron entregando sozinho: relatório semanal, checagem de anúncios, funil da Aço, ingestão de mídia, faturamento. Esta skill arma, liga e conserta essas automações em cima da fundação que já existe no MinerOS (`frocxapiowyjrdhlirnu`), sem criar sistema paralelo. O alerta do resultado é [[monitor]], a narrativa do número é [[relatorio]], o retrato consolidado por cliente é [[cruzar-dados]].

## Modos
- **relatório semanal** (robo-relatorio): liga/desliga cliente na edge `weekly-report-template`, cron seg 09h, grava `miner_reports_log`.
- **checador de anúncios** (robo-anuncios): edge `ads-running-check`, cron 07h, responde "os anúncios estão rodando?".
- **funil diário** (robo-funil): reescreve o `FAT_DATA` (array `vendedores`) do portal ACCS a partir do Salesforce.
- **ingestor Windsor** (windsor-liga): edge `windsor-ingestor` puxa gasto de mídia (52 contas) pro `miner_reports_log`.
- **NF/boleto de mídia** (nfe-automatiza): prepara faturamento recorrente de mídia; emissão e envio por item, com confirmação.

## Quando disparar
- "liga o relatório semanal do <cliente>", "por que o weekly parou", "desliga o robô do <ex-cliente>".
- "os anúncios estão no ar?", "caiu campanha?", "valida se os anúncios estão rodando".
- "automatiza o funil", "roda o /funil-aco", "o funil sozinho todo dia".
- "liga o Windsor", "de onde vem o gasto do relatório", "miner_reports_log vazio/mock".
- "emite a NF/boleto dos anúncios", "faturamento de mídia do mês".

## Como executar
Padrão comum: contexto do cliente no vault primeiro (nunca inventar conta); cron pg_cron chamando a edge via helper SQL `util.invoke_edge(fn_name, payload)`; todos com **cron em UTC** (some 3h do BRT); edge nova segue [[integra]]; e **valide fim a fim (HTTP 200 + linha gravada) antes de dar por ligado**.

- **Relatório semanal:** cada cliente é um cron `miner-weekly-report-<slug>` em `0 12 * * 1` (seg 09h BRT), edge `weekly-report-template` (`verify_jwt=true`) gravando `miner_reports_log`. Existentes: `-stkr-fr`, `-stkr-mm`, `-nmtl`, `-nmpr`. Fonte = Windsor; sem ele, roda em MOCK (não mande mock como se fosse real). **Desligar ex-cliente:** remova `miner-weekly-report-mgtc` (MGTC saiu), senão queima invocação à toa.
- **Checador de anúncios:** edge `ads-running-check` (`verify_jwt=true`), cron `miner-ads-running-check-daily` em `0 10 * * *` (07h BRT), bate Meta API + Google Ads API. Alerta = conta sem campanha ativa, ACTIVE com entrega zerada, ou erro de política (risco WhatsApp Business Hidrotintas). Carteira real em `dossier/24-windsor-carteira-real-midia-paga`. Sinal fora do padrão desce pro [[monitor]].
- **Funil diário:** SEMPRE preencher o array `vendedores` no `FAT_DATA` do `index.html` de `~/dev/portal-accs` (nunca `vendedores:[]`), estrutura `{ nome, oport, oportClientes, pedidos, recusado, credito, positivado }`, fonte Salesforce ACCS ([[salesforce]], sync 3x/dia). Vira cron diário que lê o SF, reescreve o `FAT_DATA` e deploya. Deploy da **pasta inteira** (só o `index.html` quebra os `/api`).
- **Ingestor Windsor:** edge `windsor-ingestor` chama a Windsor API (Facebook + Google Ads) e popula `miner_reports_log` por cliente/semana (spend, clicks, impressions, conversões). Depende de `WINDSOR_API_KEY` (secret/Vault, nunca no source); sem a chave, PARE e registre no [[monitor]] (radar de bloqueios), não simule. Agende o cron semanal para rodar antes dos `miner-weekly-report-*`. ~37 das ~40 contas reais aparecem; marque quem fica de fora.
- **NF/boleto:** levanta o gasto de mídia do período (Windsor/Meta) por cliente, monta a lista com valor e vencimento, **confirma item a item**, emite só o aprovado no Sistema Financeiro (`~/dev/apps/app-financeiro`, Next + Supabase). Envio ao cliente é passo separado, só com ordem explícita por item.

## Gotchas
- `verify_jwt=true` exige o service_role JWT do Vault (`supabase_service_role_jwt`); placeholder derruba a chamada.
- Cron em UTC: `0 12 * * 1` é segunda 09h BRT, não meio-dia.
- A fonte de mídia depende do **token Meta que expira 22/08**; morto, o ingestor cai e o relatório vira mock. O prazo é do [[monitor]].
- Funil: "Volume Total de Oportunidade (t)" no SF mapeia pra `pedidos`, não pra oportunidade; `credito=0` quando o gráfico diz "Sem dados" (não é erro).
- Boleto vencido já apareceu (dLocal LXNT): cheque vencimento e inadimplência antes de reemitir.

## O que NÃO fazer
- NÃO criar repo/sistema novo de automação: ligar na fundação existente.
- NÃO deixar cron de ex-cliente rodando (MGTC) nem faturar quem já saiu ([[cliente]]).
- NÃO reportar número de fonte que não respondeu nem popular `miner_reports_log` com dado inventado.
- NÃO deployar só o `index.html` do portal ACCS (quebra os `/api`).
- NÃO emitir/enviar NF ou boleto em lote sem confirmação por item.
