---
name: funil-vendedor
description: Use SEMPRE que o Gustavo quiser o funil de vendas quebrado por vendedor de qualquer cliente com CRM (não só a Aço Cearense). Dispara com "quebra o funil por vendedor", "funil por vendedor do <cliente>", "o funil do <cliente> por SDR/vendedora", "abre o funil por pessoa", "como cada vendedor tá no funil". Generaliza o /funil-aco; a regra é sempre preencher o array `vendedores`, nunca deixar vazio.
---

# funil-vendedor: funil de vendas quebrado por vendedor

Generaliza o `/funil-aco` (hoje só Aço Cearense) pra qualquer cliente com CRM. O Gustavo usa a visão de funil por vendedor: deixar o array `vendedores` vazio tira todo o valor do painel. Fonte é o MinerCRM (por org) ou o Salesforce do cliente.

## Quando disparar
- "quebra o funil por vendedor", "funil do <cliente> por SDR/vendedora", "abre o funil por pessoa".
- Qualquer cliente com CRM: ACCS via Salesforce, PRLS/NMPR via MinerCRM.

## Como executar
1. **Contexto.** Cliente e fonte via [[obsidianminer]]. Para a Aço, o fluxo canônico é [[relatorio-accs]] + [[robo-funil]] (repo `~/dev/portal-accs`, array `FAT_DATA` + `vendedores` no `index.html`).
2. **Puxe o funil por vendedor** da fonte: MinerCRM (filtrado pela org) ou Salesforce. Por vendedor: oportunidades, pedidos, recusado, crédito, positivado.
3. **REGRA: sempre preencher o array `vendedores`.** Nunca `vendedores:[]`. Estrutura ACCS: `{ nome, oport, oportClientes, pedidos, recusado, credito, positivado }`.
4. **Nomes reais da org.** Ex: PRLS 3 vendedoras; NMPR 3 (Alyssa, Natasha, Andriely). Confirme no CRM da org, não assuma.
5. **Confira cada soma** contra o KPI-tile correspondente (rótulos de barra têm ±1-3 de arredondamento).
6. **Deploy** só conta no ar: editar = deployar, confirmar a URL respondendo.

## Gotchas
- Feedback de 08/07 (`feedback_funil_aco_quebra_vendedor`): nunca deixar `vendedores` vazio, mesmo que o runbook antigo permitisse.
- Rótulo "Volume Total de Oportunidade (t)" é enganoso: é `pedidos`, não oportunidade. Ler os gráficos de baixo do Salesforce.
- Cada cliente tem vendedores diferentes: puxe da org, não reuse a lista da Aço.

## O que NÃO fazer
- Não entregar funil agregado sem a quebra por pessoa.
- Não inventar vendedor: o nome vem do CRM da org.
- Não reportar número sem bater com o KPI-tile da fonte.
