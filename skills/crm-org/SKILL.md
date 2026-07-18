---
name: crm-org
description: Use SEMPRE que for criar uma org/tenant nova no MinerCRM (cliente novo virando empresa no CRM, como PRLS, ForYou, Hidrotintas, Maresia, Stalker). Dispara com "cria a org do <cliente> no CRM", "novo tenant no minercrm", "coloca o <cliente> no CRM", "onboarding do <cliente> no CRM", "provisiona a empresa <cliente>", ou quando um cliente vai começar a usar o MinerCRM e ainda não tem organization_id, segment nem membership. NÃO é criar usuário avulso (isso é [[crm-acesso]]).
---

# crm-org: empresa nova no MinerCRM nascendo completa

O MinerCRM é multi-tenant: cada cliente é uma org (PRLS, ForYou, Hidrotintas, Maresia, Stalker). Provisionar na mão sempre esquece um pedaço (segment, membership do dono, nav_items, régua de elegibilidade). Esta skill faz a org nascer inteira e isolada, no Supabase prod `stpstwsqtuubpxvvexte`.

## Quando disparar
- "Cria a org / coloca o <cliente> no CRM", cliente novo sem organization_id.
- Vai clonar o onboarding de uma org existente pra um cliente novo.
- NÃO use pra criar só um usuário ou resetar senha (aí é [[crm-acesso]]).

## Como executar
1. **Contexto primeiro** via [[obsidianminer]]: quem é o cliente, varejo ou B2B, lead Miner. Nunca invente.
2. **Cria a org**: RPC `create_org_with_invite('Nome','slug','active','<email-dono>',7)` com contexto JWT do super_admin. Slug no padrão `tipo-cliente`.
3. **Memberships**: o time @minerbz entra sozinho (transversal pelo e-mail); o dono/gerente do cliente vai por convite em `organization_invites` (role admin). Cliente só na PRÓPRIA org.
4. **`organizations.segment`** = varejo | b2b | ambos. B2B usa `feature_overrides.account_person_type` = pf (Stalker, comprador pessoa física) | pj (Hidrotintas, Maresia). Varejo: ForYou, PRLS.
5. **nav_items por org** (o que aparece no menu), pela matriz de [[crm-modulos]].
6. **Régua `<cliente>_apply_eligibility`** no motor, com o foco geográfico próprio do cliente.
7. **RLS por membership**: `accessible_org_ids()` já isola; confirme cross-tenant com [[crm-guard]].

## Gotchas
- `create_org_with_invite` precisa de `set_config('request.jwt.claims', ...)` na mesma statement (auth.uid() vem nulo no MCP).
- Coluna de ordem dos stages é `"order"`, não `position`; não existe tabela `stages`.
- Resend em sandbox só entrega pra gustavo@minerbz.com.br: repasse o link `/join` manualmente.
- Incidente Marina→Hidrotintas: cliente NUNCA tem membership em outra org nem na org interna Miner (`56459edd-2bec-4e0e-8e0b-822658216587`).

## O que NÃO fazer
- Não criar org sem segment (vira meio-termo que não serve varejo nem B2B).
- Não dar membership de cliente fora da própria org.
- Não pular a régua de elegibilidade quando o cliente tem foco geográfico.
- Não inventar dado do cliente: puxe o vault antes.
