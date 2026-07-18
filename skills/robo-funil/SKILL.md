---
name: robo-funil
description: Use SEMPRE que for automatizar o funil de vendas diário (Aço Cearense e afins) que hoje roda na mão, ou o Gustavo disser "atualiza o funil da Aço", "roda o /funil-aco", "o funil por vendedor", "automatiza o funil diário", "por que o funil não atualizou", "funil sozinho todo dia". Dispara sempre que o /funil-aco for rodado manualmente e ao ligar o cron diário que deveria entregar o funil sozinho.
---

# robo-funil: funil de vendas diário automático

O funil da Aço Cearense (`/funil-aco`) foi rodado 13x na mão entre 10/06 e 18/07: tarefa diária que deveria ser um cron entregando sozinho. Esta skill automatiza o funil diário por vendedor, com a fonte no Salesforce ACCS.

## Quando disparar
- Vai rodar/atualizar o funil da Aço (ou de outro cliente com funil diário).
- "automatiza o funil", "o funil sozinho todo dia", "por que o funil parou".

## Como executar
1. **Regra de ouro: quebra por vendedor.** SEMPRE preencher o array `vendedores` no `FAT_DATA` do `index.html` do repo `~/dev/portal-accs`. Nunca deixar `vendedores:[]` (tira o valor do painel; instrução fixa de 08/07). Estrutura por vendedor: `{ nome, oport, oportClientes, pedidos, recusado, credito, positivado }`. Detalhe do mapeamento em [[funil-vendedor]].
2. **Fonte = Salesforce ACCS.** Leitura do SF alimenta o portal (sync 3x/dia já existe pro ACCS). Confira cada medida contra o KPI-tile correspondente (rótulos de barra têm ±1-3 t de arredondamento).
3. **Automatizar o disparo.** Em vez do comando manual, virar cron diário que lê o SF e reescreve o `FAT_DATA` + deploya. Segue o padrão dos crons Miner e do [[robo-relatorio]] (helper `util.invoke_edge`).
4. **Deploy do portal inteiro.** `portal.minerbz.com.br` é single-file com `/api`: deploy só do `index.html` quebra as rotas; deploya a pasta toda (gotcha ACCS).
5. **Entrega e valida.** Confirme o painel no ar com a quebra por vendedor preenchida.

## Gotchas
- "Volume Total de Oportunidade (t)" no SF é rótulo enganoso: mapeia pra `pedidos`, não pra oportunidade.
- `credito` = 0 quando o gráfico diz "Sem dados do gráfico" (não é erro).
- Relatório mensal/trimestral ACCS é outra entrega ([[relatorio-accs]]); este é o funil diário.

## O que NÃO fazer
- NÃO deixar `vendedores:[]`.
- NÃO deployar só o `index.html` (quebra os `/api`).
- NÃO inventar número de vendedor que não bate com o KPI-tile.
