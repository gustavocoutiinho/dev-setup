---
name: base-rfm
description: Use SEMPRE que for segmentar uma base de clientes em RFM, ICP ou Pareto pra um cliente Miner (PRLS, ForYou, Normatel). Dispara com "segmenta a base em RFM", "quem são os VIP", "monta os tiers de cliente", "curva de Pareto da base", "clientes por recência/frequência/valor", "quem tá sumido pra reativar", "define o ICP". Também quando uma régua ou cockpit precisa de segmento por valor. Gera os tiers a partir de recência, frequência e valor, pra alimentar régua e painel.
---

# base-rfm: segmentação RFM / ICP / Pareto

Segmentar a base por valor é o que faz régua e cockpit valerem: sem tier, dispara-se igual pra todo mundo. Esta skill corta a base em RFM (recência, frequência, valor), marca o ICP e monta a curva de Pareto. Já foi feito na PRLS OS (980 customers, 6 tiers RFM, ICP 3,8%, Pareto em heat-map), na ForYou e no Normatel.

## Quando disparar
- "segmenta a base em RFM", "quem são os VIP", "tiers de cliente", "curva de Pareto", "clientes sumidos pra reativar", "define o ICP".
- Uma régua ([[regua-suri]], [[aniversario-premium]]) ou cockpit ([[cockpit-kit]]) precisa de segmento por valor.

## Como executar
1. **Contexto + dado de compra** ([[obsidianminer]]): sem histórico de pedido não há RFM. A ForYou só teve RFM depois do sync de vendas (ticket médio ~R$9.966, 1.135 compradores).
2. **Calcule R/F/V:** recência (dias desde a última compra), frequência (nº de pedidos), valor (`total_value`/LTV). Combine nos tiers (a PRLS usa 6).
3. **Segmentos acionáveis, formato do CRM:** `[{op, field, value}]` com `logic: AND`. Ex ForYou: "VIP alto valor (R$50k+)", "VIP inativos p/ reativar (R$50k+, 120d+)", "Recorrentes (R$20k+)", "Compraram últimos 90 dias", "Sumidos há 6+ meses".
4. **ICP + Pareto:** marque o perfil ideal (% da base) e a curva (quantos % dos clientes fazem 80% do valor) pra priorizar carteira.
5. **Entregue pro consumo:** o segmento vira público de régua ou linha de cockpit.

## Gotchas
- Base sem `total_value`/vendas = só dá pra segmentar por cadastro, não por valor. Rode [[ingere-base]] antes.
- Snapshot velho mente: use o histórico vivo (Bling/Olist), não um número congelado ([[feedback_normatel_numeros_reais_historico]]).
- Tier não é fim: existe pra virar ação (disparo, oferta, priorização), senão é slide morto.

## O que NÃO fazer
- NÃO fabricar RFM sem dado de compra real.
- NÃO cravar corte de tier sem olhar a distribuição real da base.
- NÃO deixar o segmento sem uso (régua/cockpit).
