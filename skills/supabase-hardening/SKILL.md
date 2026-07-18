---
name: supabase-hardening
description: Use SEMPRE que for mexer em segurança do Supabase da Miner (MinerOS frocxapiowyjrdhlirnu ou minercrm): fechar advisor, ligar RLS, revisar verify_jwt de edge function, revogar PAT/chave, ou responder "o Supabase tá seguro?". Dispara com "roda o hardening", "fecha os ERROR do advisor", "essa function tá aberta?", "liga o RLS", "revoga a chave", ou antes de deployar function/tabela nova. Endurece sem derrubar produção: mede antes, muda em lote, confirma byte-idêntico.
---

# supabase-hardening: runbook de segurança do Supabase MinerOS

Runbook que endurece o Supabase sem quebrar o que está no ar, espelhando o hardening de jul/26 no MinerOS (`frocxapiowyjrdhlirnu`): 22 ERROR de advisor viraram 0, todos os endpoints verificados byte-idênticos antes e depois.

## Quando disparar
- Advisor com ERROR, tabela sem RLS, edge function pública sem guard.
- Antes de deployar function ou tabela nova no MinerOS ou minercrm.
- "Fecha os ERROR", "essa function tá aberta?", "revoga a chave".

## Como executar
1. **Mede antes.** `get_advisors` (security + performance) e `get_logs` ANTES de tocar em nada. Fotografa o baseline dos endpoints de produção (portal.minerbz.com.br, normatel/prls/aco .vercel.app).
2. **RLS + REVOKE.** Toda tabela aberta: habilita RLS e `REVOKE ALL` de anon/authenticated. Consumo real passa por edge com `service_role` (policy `service_role ALL`), nunca PostgREST direto no front.
3. **verify_jwt.** Default é `true`. Só deixe `false` em function pública por design (magic link, portal browser) ou webhook com guard próprio: valida `x-miner-webhook-secret` / `x-miner-mcp-secret` / HMAC. Antes de ligar verify_jwt numa function chamada pelo browser, garanta que o front passa a anon key (senão quebra, caso `claude-proxy`/mineraco).
4. **Muda em lote e reconfere.** Após cada lote, `get_advisors` de novo e confirma os endpoints byte-idênticos ao baseline.
5. **Chaves.** Toda chave hardcoded ou já commitada está comprometida ([[varredura-segredos]]): mova pra secret server-side e sinalize rotação. Pendência viva: revogar o PAT `sbp_828e...` (mandado desde jun/26, nunca feito) e criar PAT com expiração.

## Gotchas
- MCP do Supabase às vezes não está exposto: dá pra rodar SQL pela Management API com PAT (`POST /v1/projects/REF/database/query`).
- P0 conhecidos: `portal-upload` (sobrescreve páginas com service_role) e `claude-proxy` (gasta crédito Anthropic aberto).
- No minercrm, quem cuida de org/role/tenant é o [[crm-guard]]: não recrie regra de vínculo aqui.
- Function pública servindo dado de cliente sem auth é caso de [[blindar-portal]] junto.

## O que NÃO fazer
- NÃO mexer sem `get_advisors`/`get_logs` antes (voa às cegas).
- NÃO ligar verify_jwt sem checar o consumidor (derruba portal).
- NÃO achar que mover chave do git resolve: só rotação resolve (e é ação do Gustavo).
