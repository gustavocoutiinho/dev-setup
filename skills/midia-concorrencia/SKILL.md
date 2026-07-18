---
name: midia-concorrencia
description: Use SEMPRE que precisar montar a análise mensal de concorrência de um cliente, ou o Gustavo disser "análise de concorrência", "o que os concorrentes estão anunciando", "benchmark do <cliente>", "apresentar a concorrência do mês", "ranking de engajamento do mercado", "spia os anúncios do concorrente". Dispara na task recorrente "Apresentar Mensalmente A Análise De Concorrência" (NMTL e outros) e no slide de concorrência dos decks mensais.
---

# midia-concorrencia: análise mensal de concorrência

A análise de concorrência é entrega mensal fixa (task "Apresentar Mensalmente A Análise De Concorrência" no NMTL) e slide obrigatório dos decks. Esta skill monta o benchmark de engajamento do segmento e o retrato dos anúncios que os concorrentes estão rodando.

## Quando disparar
- Task mensal de concorrência de um cliente, ou slide de concorrência num deck do mês.
- "o que o concorrente tá anunciando", "ranking do mercado", "benchmark de engajamento".

## Como executar
1. **Benchmark de engajamento por segmento.** Fonte é o CSV do Social Tracker por vertical (ex.: `..._social_media_tool_Instagram_MODA-...csv` em `~/Downloads`), ranqueado por engajamento total. Referência real: food Fortaleza mai/2026 com 9 marcas (Outback 141.532 no topo; Estela 544 **+66,4%**, Olli's 544 **+41,7%** entre as locais em alta).
2. **Anúncios do concorrente via Ad Library.** Meta Ad Library (site) pra ver quem está no ar, tempo no ar e nº de variações como proxy de performance (a API comercial no BR não dá gasto/impressão). Use o [[spy]] do miner-ads pra puxar os criativos.
3. **Diagnóstico, não só tabela.** O que o líder do segmento faz que o cliente não faz; onde o cliente sobe/cai vs o pelotão local. Leitura de performance pelo [[meta-ads-analyzer]].
4. **Coerência com os insights nativos.** Override do Gustavo: pras marcas que a Miner atende (Barney's/Estela/Olli's), usar Interações totais do Reportei, não o número do Social Tracker; rotular a fonte no slide (metodologia mista) e entregar no visual do cliente com mês explícito.

## Gotchas
- "Engajamento total" do Social Tracker (curtidas+comentários) ≠ "interações totais" do Reportei; são métricas diferentes, rotule qual é qual.
- Ad Library agrupa por anunciante: cada `?id=` devolve o criativo destaque, então saem poucos criativos distintos. Deduplique por md5 do vídeo.
- Sem CSV do mês, NÃO reaproveite o do mês anterior com rótulo novo (regra Normatel); marque a fonte como pendente.

## O que NÃO fazer
- NÃO inventar métrica de concorrente que a fonte não deu.
- NÃO tratar tempo no ar como gasto (Ad Library não expõe verba comercial).
- NÃO misturar segmentos no mesmo ranking.
