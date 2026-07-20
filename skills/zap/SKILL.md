---
name: zap
description: Use SEMPRE que o trabalho for disparo/régua de WhatsApp via Suri (ou Blip) pra base de cliente: carrinho abandonado, boas-vindas, reativação de inativos, ou régua de aniversariantes cruzada com RFM (Normatel Premium). Dispara com "monta a régua do <cliente>", "dispara o template x pra base", "campanha de WhatsApp", "régua de reativação", "dispara os aniversariantes", "quem faz aniversário hoje".
---

# zap: régua de disparo WhatsApp via Suri

A Suri (e o Blip) é o canal de WhatsApp de vários clientes Miner (PRLS, Normatel Premium, Stalker, Maresia). Esta skill monta e dispara a régua: escolhe o template aprovado, monta o payload certo, filtra o público e respeita quem pediu pra não receber. Envio real tem efeito colateral: só acontece com ordem do Gustavo item a item.

## Modos
- **régua/campanha**: carrinho abandonado, boas-vindas, reativação, pós-venda pra uma base filtrada por canal e segmento.
- **aniversariantes + RFM**: quem faz aniversário hoje cruzado com o tier de valor (padrão Normatel Premium), pra priorizar VIP.

## Quando disparar
- "monta/dispara a régua do <cliente>", "manda o template <X> pra base", "campanha de WhatsApp da PRLS/Maresia", "régua de reativação".
- "aniversariantes do dia", "quem faz aniversário hoje", "aniversariantes VIP", "manda o template de aniversário".
- Qualquer pedido de enviar template Meta em massa por WhatsApp.

## Como executar
1. **Contexto + credencial** ([[obsidianminer]], nota miner-automation-infra): endpoint e token do tenant vivem em `miner_api_credentials`. PRLS tenant `cb55561066`, canais Varejo `wp683764354811896` + Atacado `wp685312314657220`. Normatel Premium em `normatel-premium.vercel.app`, provider Suri (tenant "Normatel Premium").
2. **Template aprovado, não texto livre.** POST `/messages/send` com `{userId, message: {templateId, BodyParameters: [...]}}` (PascalCase). O `templateId` é o **messageId do Meta/Gupshup**, não o id interno da Suri. A PRLS tem 51 templates aprovados (ex: `carrinho_abandonado_04_utilidade`).
3. **Público certo:** filtre a base pelo canal (varejo × atacado) e pela régua. Segmente por valor/recência com [[dados]] (RFM).
4. **Aniversariantes:** filtre `birth_date not null` e case **dia+mês** (nunca o ano). Foi assim que o widget da ForYou acertou os 4 aniversariantes que a Marina esperava. Cruze com o tier RFM ([[dados]]) pra decidir prioridade e brinde/cashback.
5. **Dry-run sempre:** liste quem receberia e qual template, mostre pro Gustavo, e só dispare com o ok dele item a item.

## Gotchas
- **Respeite a tag Suri "não receber disparos"**: quem tem essa tag fica FORA da régua, sempre, mesmo no aniversário. Opt-out é lei.
- STKR e MRSA têm base na Suri mas **inativas pra disparo**: confirme antes de mandar.
- `templateId` errado (id interno em vez do Meta messageId) = a Suri aceita e não entrega. Use o messageId aprovado.
- Base sem `birth_date` ou sem histórico de compra = régua vazia ou sem tier. Se a cobertura estiver baixa (Olist ForYou tinha 90/3796 antes do backfill), rode a ingestão em [[dados]] antes.
- Inbox do CRM com "erro ao carregar conversas" é problema de CRM ([[crm]]), não da régua.

## O que NÃO fazer
- NÃO disparar sem dry-run aprovado e ordem por item (envio real).
- NÃO mandar texto livre fora de janela: WhatsApp exige template aprovado.
- NÃO ignorar a tag de opt-out, nem no aniversário.
- NÃO importar dado de cliente/arquiteto sem confirmar PII (regra do Normatel Premium).
