---
name: aniversario-premium
description: Use SEMPRE que o pedido for régua de aniversariantes por WhatsApp cruzada com segmentação de valor (RFM), tipicamente no Normatel Premium. Dispara com "dispara os aniversariantes do dia", "régua de aniversário", "quem faz aniversário hoje", "manda o template de aniversário", "aniversariantes VIP", "felicita a base no aniversário". Também quando o cliente quer parabenizar clientes no dia certo via Suri, priorizando os de maior valor. Cruza data de nascimento + RFM e dispara com ordem por item.
---

# aniversario-premium: régua de aniversariantes + RFM via Suri

O Normatel Premium (CRM Miner pro ARD Grupo: funil, RFM, aniversariantes, Suri) parabeniza clientes no aniversário por WhatsApp. Esta skill monta essa régua: pega quem faz aniversário hoje, cruza com o tier RFM (pra priorizar e ajustar a oferta) e dispara o template Suri. É [[regua-suri]] especializada na data de nascimento.

## Quando disparar
- "aniversariantes do dia", "régua de aniversário", "quem faz aniversário hoje", "aniversariantes VIP".
- Cliente quer felicitar a base no dia certo, com prioridade pra quem vale mais.

## Como executar
1. **Contexto** ([[obsidianminer]]): Normatel Premium mora em `~/Documents/normatel-premium/`, `normatel-premium.vercel.app`, provider Suri (tenant "Normatel Premium"). Confirme a estratégia de PII antes de tocar em dado real.
2. **Aniversariantes de hoje:** filtre `birth_date not null` e case **dia+mês** (não o ano). Foi assim que o widget da ForYou acertou os 4 aniversariantes que a Marina esperava.
3. **Cruze com RFM** ([[base-rfm]]): o tier decide prioridade e se entra brinde/cashback. VIP no aniversário é o disparo de maior retorno.
4. **Dispare via [[regua-suri]]:** template de aniversário aprovado (Meta messageId), `BodyParameters` com o primeiro nome. Dry-run primeiro; envio real só com ordem por item.

## Gotchas
- Base sem `birth_date` preenchido = régua vazia. Se a cobertura estiver baixa (caso Olist ForYou: 90/3796 antes do backfill), rode [[ingere-base]] antes.
- **Tag Suri "não receber disparos"** tira o contato da régua mesmo no aniversário.
- Aniversário casa dia/mês; comparar timestamp cheio perde todo mundo que não nasceu neste ano.

## O que NÃO fazer
- NÃO importar dado de cliente/arquiteto sem confirmar PII (regra do Normatel Premium).
- NÃO disparar sem dry-run aprovado.
- NÃO parabenizar quem pediu pra não receber.
