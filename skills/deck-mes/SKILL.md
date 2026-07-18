---
name: deck-mes
description: Use SEMPRE que for virar o mês do deck de relatório de um cliente (Barney's, Estela, Olli's, Normatel, Maresia) ou o Gustavo disser "fecha o mês do <cliente>", "novo mês do deck", "roda o relatório de <mês> do <cliente>", "atualiza o deck do <cliente> pro mês novo", "monta o deck deste mês". Dispara quando o trabalho é "mais um ciclo mensal do deck que já existe", não criar deck do zero. É o wrapper que orquestra estrutura + dados + design num mês só.
---

# deck-mes: vira o mês do deck de um cliente

Todo mês a Miner refaz o mesmo deck de relatório pra cada cliente. Sem trilho, cada virada vira um retrabalho: clona HTML, redigita número, erra delta. Esta skill é o wrapper "novo mês do cliente X": orquestra as skills que já fazem estrutura, dado e visual, garantindo que só o mês mude e o esqueleto fique intacto.

## Quando disparar
- "fecha junho do Barney's", "roda o deck de julho da Estela", "novo mês do Normatel".
- Deck já existe em `~/dev/decks/deck-<cliente>` (barneys, estela, ollis, normatel, maresia) e precisa de mais uma competência.
- NÃO use pra criar deck de cliente que ainda não tem molde (aí é [[deck-kit]]).

## Como executar
1. **Contexto primeiro.** Puxe o cliente e o histórico do deck (memória `feedback_decks_relatorio_padrao`, `barneys-deck-relatorio`). Nunca invente número.
2. **Esqueleto é fixo.** A lógica de slides é SEMPRE a do `~/dev/decks/deck-barneys/junho.html` (regra fixada 09/07: dados mudam, esqueleto não). Clone os componentes da Estela (capa-kv, `.why`, `.adrk`).
3. **Dado separado do esqueleto.** Extraia/atualize os números via [[deck-vivo]] (JSON por competência); delta é calculado, não digitado. Fontes vivas por [[relatorio-vivo]] / [[relatorio-social]] quando o cliente já está ligado.
4. **Números reais, mês explícito.** Regra Normatel: KPI sai do Histórico real, cada card carrega o mês; nunca extrapolar snapshot velho nem rotular dado antigo com mês novo.
5. **Visual Miner.** Capa KV + logo do cliente, `.why` em todo número que cai, favicon do cliente, tudo via [[minerdesign]].
6. **Deploy.** Publique pela rota do [[exporta-deck]] (`vercel --prod` da pasta, da última main).

## Gotchas
- Sem criativo repetido nos slides de Meta Ads (a mesma arte roda em campanhas diferentes no Reportei).
- Sem slide de "plano do mês seguinte" no Barney's; concorrência velha só com rótulo do mês certo.
- Foto grande só com fonte hi-res; thumb pequena em tamanho nativo.

## O que NÃO fazer
- NÃO editar o esqueleto pra "encaixar" o mês.
- NÃO redigitar número que dá pra extrair, nem digitar delta.
- NÃO misturar cliente/competência no mesmo JSON.
