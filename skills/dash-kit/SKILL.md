---
name: dash-kit
description: Use SEMPRE que precisar de um dashboard rápido single-file de leads, funil ou kanban na Miner (uma tela pra visualizar dado, sem virar produto). Dispara com "quero um dashboard rápido de leads", "monta um HTML de funil", "uma telinha de kanban dos leads", "dashboard rápido pra ver isso", "board dos leads". Um arquivo, sobe rápido, lê a fonte viva.
---

# dash-kit: dashboard HTML rápido de leads/funil/kanban

Recorrente na Miner: precisar de uma tela pra olhar leads, funil ou kanban sem montar produto inteiro (apareceu várias vezes: HTML lead dashboard, two funnels, lead tracking kanban, dental appointment). Esta skill entrega um dashboard single-file, vivo e descartável, sem overhead.

## Quando disparar
- "quero um dashboard/telinha rápida de leads/funil/kanban", visualização pontual de dado.
- NÃO use quando é pra virar produto multi-departamento (aí é [[cockpit-kit]]).

## Como executar
1. **Fonte do dado** primeiro: de onde vem (Supabase, CRM, Meta/Windsor). Confirme no [[obsidianminer]].
2. **Single-file** HTML+JS, lê a fonte por edge/API ([[dado-vivo]]), nunca dado colado.
3. **Views úteis:** tabela filtrável, funil por etapa, kanban por status. Mantém leve ([[web-enxuta]]).
4. **Se captura contato**, grava de verdade ([[capta-lead]]).
5. **Deploy** na Vercel só se precisar compartilhar; senão roda local. Confirma no ar ([[deploy-miner]]).

## Gotchas
- Dashboard rápido tende a virar snapshot chumbado: já nasce lendo a fonte, senão desatualiza e engana.
- Se serve lead com PII e vai pro ar, precisa de gate ([[blindar-portal]]).

## O que NÃO fazer
- NÃO chumbar o dado no HTML "só pra ver hoje".
- NÃO expor PII de lead num link público sem sessão.
- NÃO transformar em produto sem antes decidir dono e manutenção.
