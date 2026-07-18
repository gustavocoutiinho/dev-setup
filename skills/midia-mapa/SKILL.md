---
name: midia-mapa
description: Use SEMPRE que precisar montar ou atualizar o mapa de investimento / distribuição de verba de mídia de um cliente, ou o Gustavo disser "monta o mapa de investimento do <cliente>", "distribuição de verba", "como dividir a verba", "planejamento de investimento de mídia", "compartilhar a estratégia de investimento". Dispara nas tasks recorrentes tipo "Mapa de investimento", "Distribuição de verba" e "Compartilhar Planejamento e Distribuição da Estratégia de Investimento de Mídia" (NMTL, OTRH e outros).
---

# midia-mapa: mapa de investimento e distribuição de verba

Distribuir verba por canal, categoria, região e campanha é task recorrente em quase todo cliente Miner (aparece como "Mapa de investimento", "Distribuição de verba", "Planejamento da Estratégia de Investimento de Mídia" no Asana de NMTL, OTRH e cia). Esta skill monta esse mapa ancorado no gasto real, não em chute.

## Quando disparar
- Task de "mapa/distribuição/planejamento de investimento de mídia" de um cliente.
- Vai definir quanto de verba vai pra Meta × Google, por categoria de produto ou por região.
- Fechamento de mês pede o plano do mês seguinte por objetivo.

## Como executar
1. **Contexto e gasto real primeiro.** Puxe o cliente no vault e o gasto real do [[windsor-liga]] (Windsor cobre 37 contas Meta + 6 Google Ads; carteira em `dossier/24-windsor-carteira-real-midia-paga`). Nunca inventar verba.
2. **Use o documento canônico como molde.** ACCS tem o padrão de referência: `Mapa de investimento - Aço Cearense.xlsx` divide por região e produto (P1 Nordeste, P2 Norte, P3 Sudeste; tubos, telha, metalon, perfis, chapas). Replique a lógica pro cliente do momento.
3. **Amarre no objetivo do contrato.** Cada fatia de verba tem objetivo, o que mede e onde chegou (padrão dos decks: iFood/Cardápio/Branding/Suri no Barney's). Verba por marca vive em `investmentPlan` no pimfood pra quem usa portal.
4. **Estratégia por trás dos números** vem do [[meta-ads-strategy]] (estrutura de campanha, público, budget). Concorrência que justifica a fatia sai do [[midia-concorrencia]].
5. **Entregue no formato do cliente** (slide de metas no deck, card de plano no portal, ou planilha), mês explícito.

## Gotchas
- Alguns clientes rodam mídia por agência (Hidrotintas via Mulato) e a conta não expõe API direta; o número vem do Windsor ou da planilha, não do Meta.
- Gasto do Windsor é dos últimos 30 dias; confira a janela antes de projetar.

## O que NÃO fazer
- NÃO propor distribuição sem ancorar no gasto/resultado real.
- NÃO extrapolar ritmo de amostra parcial pro mês inteiro (regra Normatel).
- NÃO deixar fatia de verba sem objetivo e sem métrica.
