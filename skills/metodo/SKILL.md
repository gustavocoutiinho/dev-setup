---
name: metodo
description: Use SEMPRE que o Gustavo for aplicar uma metodologia proprietária da Miner pra diagnosticar/estruturar a operação de um cliente: auditoria comercial digital (funil, atendimento, conversão travada), Smart Company Method (maturidade em ~10 dimensões, o que trava o crescimento), ou o MIG Framework (operação com webinar como funil de topo). Dispara com 'faz a auditoria comercial do <cliente>', 'por que o funil não converte', 'diagnóstico de maturidade', 'smart company method', 'estrutura a operação do <cliente>', 'framework MIG', 'funil de webinar'.
---

# metodo: metodologias proprietárias de diagnóstico da Miner

Três protocolos proprietários que o Gustavo aplica pra diagnosticar e estruturar a operação de um cliente antes de propor mudança: a Auditoria Comercial Digital (onde o funil fura), o Smart Company Method (o que trava o crescimento) e o MIG Framework (operação com webinar no topo). Princípio central do Gustavo: negócio digital não cresce com ferramenta, cresce com estrutura. Todos partem do contexto real do cliente no vault, nunca de memória. É diagnóstico, não implementação.

## Modos
- **auditoria** (Auditoria Comercial Digital): diagnóstico de 4 semanas do funil de vendas (WhatsApp + CRM), prova ONDE fura com hipóteses por impacto.
- **smart** (Smart Company Method): maturidade da operação em 10 dimensões, acha a dimensão-âncora frágil que trava tudo.
- **mig** (MIG Framework): estrutura operação com webinar como funil de topo em 4 etapas mensuráveis.

## Quando disparar
- "faz a auditoria comercial do <cliente>", "por que o funil não converte", "mapeia os gargalos de vendas", "roda o protocolo do ACCS/Maestria" → **auditoria**.
- "estrutura a operação do <cliente>", "por que o cliente não escala", "o que trava o crescimento", "diagnóstico de maturidade", "smart company method", "quais dimensões estão fracas" → **smart**.
- "estrutura o funil de webinar do <cliente>", "framework MIG", "operação MGTC/Mig-Tech", "medir show-rate e conversão pós-webinar" → **mig**.

## Como executar
**Comum:** puxe o cliente no [[obsidianminer]] (stack, CRM, lead Miner, o que já existe). Nunca opine número ou dimensão sem ler a nota. Saída é diagnóstico com recomendação priorizada, entregue no molde de [[relatorio]].

- **auditoria (4 semanas):** S1 imersão (quantitativo no CRM: conversão por etapa, ticket, ciclo, no-show, entrada/mês + inventário de scripts). S2 entrevistas 1h com 100% dos closers/SDRs, roteiro fixo, cruze atrás de padrão e contradição. S3 síntese: mapa do funil com volume e taxa por etapa (quebre por vendedor via [[crm]]), 3-5 gargalos, hipóteses por impacto × dificuldade. S4 relatório 30-60-90, apresenta e decide o que entra em execução. Rodou no ACCS (funil 12 etapas, 11 categorias de problema) e na Maestria (1308 deals no HubSpot, `closed_lost` dominante no top de valor, ~1:4). Aprofunda as dimensões 2, 3, 5, 6, 8 e 9 do modo smart.
- **smart:** rode as 10 dimensões uma a uma, sinal de saúde × sinal de doença: 1 Posicionamento, 2 Modelo Comercial, 3 Jornada do Cliente, 4 CRM, 5 Processos, 6 Automação, 7 Operação Digital, 8 Indicadores, 9 Governança, 10 Tomada de Decisão. Ache a UMA dimensão-âncora frágil (é onde o crescimento trava), priorize por gargalo (a fraca puxa as fortes pra baixo), ligue cada dimensão a um sprint ou SOP. Já mapeou 8 clientes (Normatel, Maestria, ACCS, Mig-Tech, HDTS, MSLZ, Stalker, DLT), cada um com a âncora frágil apontada.
- **mig (M-I-G + retenção):** M Marketing/topo, âncora CPL, uma LP por vertical via [[criar-web]]. I Interesse/qualificação, âncora show-rate + tempo assistido (saída: lead que ficou >30 min). G Geração/conversão, âncora webinar → SQL → venda, lead tem que chegar com nome certo no Kinbox. Retenção, âncora LTV + churn. Stack de referência MGTC: HubSpot + Kinbox + Meta + Reportei, 4 verticais. Operacionaliza as dimensões 2, 3 e 8 do modo smart.

## Gotchas
- **auditoria:** a distribuição de `closed_lost` por motivo é o ouro (na Maestria revelou reposicionamento que não chegou à entrada do funil). Filtre agregados da org (o SF do ACCS tem ~22k ops/mês, nunca some sem recortar o escopo auditado). Export e entrevista têm PII: o relatório é interno.
- **smart:** 9 dimensões boas não salvam 1 ruim. Sinal de doença é observável ("cliente confunde sua oferta com a do concorrente"), não achismo. Cada cliente tem UMA âncora frágil, documentada com evidência do vault.
- **mig:** cada etapa tem UMA métrica-âncora, sem elas o funil é opinião. "Lead sem nome no Kinbox" mata a etapa G (virou a automação `kinbox-name-fix`: webhook HubSpot → enrich → Kinbox API). Não aplicar em varejo B2C puro (PRLS não é caso); candidatos além da MGTC: HDTS, Maestria, Stalker franqueado.

## O que NÃO fazer
- NÃO recomendar mudança sem diagnóstico, nem opinar só de entrevista sem base quantitativa.
- NÃO vender ferramenta como solução (fere o princípio central), nem diagnosticar de memória.
- NÃO tratar as 10 dimensões como checklist de peso igual: priorize a que trava.
- NÃO reportar "webinar foi bom" ou inventar CPL/LTV: puxe de HubSpot + Meta + Reportei reais.
