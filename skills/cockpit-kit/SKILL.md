---
name: cockpit-kit
description: Use SEMPRE que for criar um cockpit ou dashboard multi-departamento de cliente na Miner (visão de gestor com várias áreas). Dispara com "monta um cockpit pro <cliente>", "dashboard com financeiro, vendas e marca", "painel multi-departamento", "cockpit de gestão do <cliente>", "quero a visão executiva do <cliente>". Diferente de um dashboard rápido de leads: aqui é a casa com nav por departamento.
---

# cockpit-kit: cockpit multi-departamento de cliente

A Miner tem um padrão de cockpit por marca com navegação por departamento: o PRLS OS (/financeiro com DRE/DFC/simuladores, /clientes com 980 customers em 6 tiers RFM, /marca), o pimfood-onboard-zen (3 marcas × meses, funil de mídia, /apresentar) e o cockpitgb (Movimento & Funil + Auditoria + Raio-X, consumindo Omnichat por edge). Esta skill instancia esse padrão.

## Quando disparar
- "monta cockpit/dashboard multi-departamento do <cliente>", visão de gestor com mais de uma área.
- Cliente top que já justifica portal próprio (product-led).

## Como executar
1. **Contexto** do cliente no [[obsidianminer]]: quais departamentos fazem sentido (financeiro, clientes/RFM, mídia, marca, atendimento).
2. **Casca Next 14 + Supabase**, nav lateral por departamento, nome `cockpit-<cliente>` ou `<cliente>-os`.
3. **Cada aba lê dado vivo** ([[dado-vivo]]) da fonte real (Supabase, Bling/Olist, Meta via Windsor), não snapshot.
4. **RFM e base** quando tiver clientes: segmenta com [[base-rfm]] (tiers, ICP, Pareto).
5. **Identidade** KV Miner ou marca do cliente ([[minerdesign]]) + favicon.
6. **Gate** se tem PII ([[blindar-portal]]), domínio ([[dominio-miner]]), deploy e confirma ([[deploy-miner]]).

## Gotchas
- Cockpit é product-led: defina quem opera pós-entrega (cliente ou Miner) e como cobra manutenção, senão vira dependência do time.
- Painel silencioso (aba que nunca carrega dado) é pior que não ter: valide cada fonte antes de entregar.

## O que NÃO fazer
- NÃO montar aba com número inventado ou snapshot manual.
- NÃO duplicar cockpit que já existe pro cliente (cheque com [[faxina-vercel]]).
- NÃO expor financeiro/clientes sem sessão real.
