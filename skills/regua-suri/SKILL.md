---
name: regua-suri
description: Use SEMPRE que for montar ou disparar uma régua/campanha de WhatsApp via Suri (ou Blip) pra base de um cliente Miner (carrinho abandonado, boas-vindas, reativação, pós-venda). Dispara com "monta a régua do <cliente>", "dispara o template <X> pra base", "campanha de WhatsApp da PRLS/Maresia", "manda o carrinho abandonado", "régua de reativação", "quais templates aprovados tem". Também quando o pedido envolve enviar template Meta em massa por WhatsApp. Respeita opt-out e só dispara com ordem por item.
---

# regua-suri: régua de disparo WhatsApp via Suri

A Suri é o canal de WhatsApp de vários clientes Miner (PRLS, Normatel Premium, Stalker, Maresia). Esta skill monta a régua: escolhe o template aprovado, monta o payload certo e respeita quem pediu pra não receber. Envio real é ação com efeito colateral: só com ordem do Gustavo item a item ([[feedback_sem_envio_so_leitura]]).

## Quando disparar
- "monta/dispara a régua do <cliente>", "manda o template <X> pra base", "campanha WhatsApp da PRLS/Maresia".
- Carrinho abandonado, boas-vindas, reativação, pós-venda (aniversário é [[aniversario-premium]]).

## Como executar
1. **Contexto + credencial** ([[obsidianminer]], [[miner-automation-infra]]): endpoint e token do tenant vivem em `miner_api_credentials`. PRLS tenant `cb55561066`, canais Varejo `wp683764354811896` + Atacado `wp685312314657220`.
2. **Template aprovado, não texto livre.** POST `/messages/send` com `{userId, message: {templateId, BodyParameters: [...]}}` (PascalCase). O `templateId` é o **messageId do Meta/Gupshup**, não id interno da Suri. A PRLS tem 51 templates aprovados (ex: `carrinho_abandonado_04_utilidade`).
3. **Público certo:** filtre a base pelo canal (varejo × atacado) e pela régua. Segmente por valor/recência com [[base-rfm]].
4. **Dry-run:** liste quem receberia e qual template, mostre pro Gustavo, só dispare com o ok dele.

## Gotchas
- **Respeite a tag Suri "não receber disparos"** ([[miner-operacao-scan-log]]): quem tem essa tag fica FORA da régua, sempre. Opt-out é lei.
- STKR e MRSA têm base na Suri mas **inativas pra disparo**: confirme antes de mandar.
- `templateId` errado (id interno em vez do Meta messageId) = a Suri aceita e não entrega. Use o messageId aprovado.
- Inbox do CRM com "erro ao carregar conversas" é [[conversa-fix]], não problema de régua.

## O que NÃO fazer
- NÃO disparar sem ordem por item do Gustavo (envio real).
- NÃO mandar texto livre fora de janela: WhatsApp exige template aprovado.
- NÃO ignorar a tag de opt-out.
