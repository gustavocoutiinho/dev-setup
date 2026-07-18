---
name: metodo-mig
description: Use quando o Gustavo for estruturar ou medir uma operação que usa webinar como funil de topo, com o framework proprietário da Miner. Dispara com "estrutura o funil de webinar do <cliente>", "framework MIG", "operação MGTC/Mig-Tech", "medir show-rate e conversão pós-webinar", "por que o webinar não converte", "monta o funil do lançamento", ou quando o canal de captação é webinar/evento e a venda depende de proposta pós-evento.
---

# metodo-mig, MIG Framework (funil de webinar)

Framework proprietário da Miner pra operação que usa webinar como funil de topo. Nasceu na Mig-Tech (MGTC): webinar era a aposta central mas sem medida clara de conversão. MIG estrutura o funil em 4 etapas mensuráveis. Stack de referência MGTC: HubSpot + Kinbox + Meta + Reportei, 4 verticais (medicina/odonto, farma, fisio, credit journey), uma LP por vertical.

## Quando disparar
- "estrutura o funil de webinar do <cliente>", "framework MIG", "operação MGTC", "medir show-rate e conversão pós-webinar".
- Cliente onde webinar (ou evento) é canal de captação e a conversão depende de proposta pós-evento.
- Candidatos além da MGTC: HDTS, Maestria (demo do plugin Word), Stalker franqueado. Varejo B2C puro (PRLS) não é caso.

## Como executar (M-I-G + retenção)
1. **Contexto primeiro.** Puxe o cliente no [[obsidianminer]]. Confirme a stack real (HubSpot/Kinbox/Reportei na MGTC) antes de afirmar métrica.
2. **M (Marketing, topo).** Captação de inscritos: Meta + Google + orgânico + LinkedIn B2B. Métrica-âncora: CPL (custo por lead inscrito). Uma [[lp-kit]] por vertical alimenta esta etapa.
3. **I (Interesse, qualificação).** Confirmação de presença + engajamento no webinar. Métrica-âncora: show-rate + tempo médio assistido. Saída: lead que ficou mais de 30 min.
4. **G (Geração, conversão).** Reunião comercial pós-webinar + proposta. Métrica-âncora: webinar → SQL → venda. O lead tem que chegar com nome correto no Kinbox (gargalo real MGTC).
5. **Retenção (4ª etapa).** Onboarding + expansão + renovação. Métrica-âncora: LTV + churn.

## Gotchas
- **Cada etapa tem UMA métrica-âncora.** Sem CPL, show-rate, conversão e LTV medidos, o funil é opinião.
- **"Lead sem nome no Kinbox" mata a etapa G.** Na MGTC virou a automação `kinbox-name-fix` (webhook HubSpot → enrich → Kinbox API).
- **MIG não substitui o [[metodo-smart]]:** operacionaliza as dimensões 2 (modelo comercial), 3 (jornada) e 8 (indicadores). São complementares.

## O que NÃO fazer
- NÃO aplicar MIG em varejo B2C puro: precisa de webinar + proposta pós-evento.
- NÃO reportar "webinar foi bom" sem show-rate e conversão.
- NÃO inventar CPL/LTV: puxe de HubSpot + Meta + Reportei reais.
