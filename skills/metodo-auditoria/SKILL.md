---
name: metodo-auditoria
description: Use SEMPRE que o Gustavo for diagnosticar a operação comercial de um cliente (funil de vendas, atendimento WhatsApp, CRM, scripts, conversão travada) com o protocolo próprio da Miner, antes de propor qualquer mudança. Dispara com "faz a auditoria comercial do <cliente>", "por que o funil não converte", "mapeia os gargalos de vendas", "diagnóstico comercial", "auditoria comercial digital", "roda o protocolo do ACCS/Maestria aqui", ou quando entra muito lead e fecha pouco e ninguém sabe onde fura.
---

# metodo-auditoria, Auditoria Comercial Digital (protocolo Miner)

Protocolo proprietário da Miner pra diagnosticar operação de vendas (WhatsApp + CRM) e provar ONDE o funil fura, com hipóteses por impacto. Já rodou no ACCS (funil de 12 etapas, 11 categorias de problema) e na Maestria (1308 deals no HubSpot, `closed_lost` dominante no top de valor, ~1:4). É diagnóstico, não implementação.

## Quando disparar
- "auditoria comercial do <cliente>", "por que não converte", "mapeia os gargalos", "diagnóstico de vendas".
- Cliente com muito lead no topo e pouco fechamento, e ninguém sabe onde perde.
- NÃO é pra mexer no produto, treinar time ou já implementar mudança: isso é fase seguinte.

## Como executar (4 semanas)
1. **Contexto primeiro.** Puxe o cliente no [[obsidianminer]] (stack, CRM, lead Miner, funil já mapeado). Nunca invente número.
2. **Semana 1, imersão.** Leitura no CRM + quantitativo: conversão por etapa, ticket médio, ciclo, no-show, entrada por mês. Inventário de scripts e sequências.
3. **Semana 2, entrevistas.** 1h com 100% dos closers/SDRs, roteiro fixo (rotina, gargalo, conversão percebida, scripts, motivo de perda). Cruze respostas atrás de padrão e contradição.
4. **Semana 3, síntese.** Mapa do funil com volume e taxa por etapa (quebre por vendedor via [[funil-vendedor]]); 3 a 5 gargalos maiores; hipóteses por (impacto x dificuldade); revisão de scripts e automações.
5. **Semana 4, relatório.** Diagnóstico + hipóteses por impacto + recomendações 30-60-90. Apresenta e decide o que entra em execução.

## Gotchas
- **A distribuição de `closed_lost` por motivo é o ouro.** Na Maestria o padrão de perda no top de valor revelou reposicionamento que não chegou à entrada do funil.
- **Filtre agregados da org.** No SF do ACCS a org inteira tem ~22k ops/mês: nunca some sem recortar o escopo auditado.
- **Sem PII em entregável.** Export e entrevista têm dado de cliente: o relatório é interno.

## O que NÃO fazer
- NÃO recomendar mudança sem diagnóstico (mudar sem diagnóstico é cego).
- NÃO virar avaliação individual: é diagnóstico de processo, transparente com o time.
- NÃO opinar só de entrevista, sem a base quantitativa.

A auditoria aplica o [[metodo-smart]] nas dimensões 2, 3, 5, 6, 8 e 9.
