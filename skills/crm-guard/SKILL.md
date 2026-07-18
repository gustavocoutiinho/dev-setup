---
name: crm-guard
description: Use SEMPRE que mexer em acesso, papel, troca de org, desativação de empresa ou isolamento de dados entre clientes no MinerCRM, ou quando aparecer suspeita de vazamento cross-tenant (cliente vendo dado de outro, staff vendo a org errada). Dispara com "um cliente tá vendo dado de outro", "vazou entre tenants", "confere o isolamento", "pode trocar de org?", "desativa a empresa <x>", "por que o staff vê a org errada", "isso respeita RLS?". Multi-tenant, memória do incidente 10/07. NÃO é criar org nova ([[crm-org]]).
---

# crm-guard: tenant guard e RLS multi-org do MinerCRM

Depois do incidente 10/07 (membros da Stalker aparecendo na ForYou), o isolamento entre clientes tem regra fixa. Toda mexida em acesso, papel ou org passa por aqui pra não reabrir buraco cross-tenant. Supabase prod `stpstwsqtuubpxvvexte`.

## Quando disparar
- Suspeita de cliente vendo dado de outro, ou staff vendo a org errada.
- Vai trocar org ativa, mudar papel, desativar empresa ou revisar RLS.

## Como executar
1. **org/role só via service_role**: o trigger `trg_protect_profile_tenant` levanta exceção se `organization_id` ou `role` de `profiles` mudarem fora de service_role. Nunca update direto em `profiles` pelo client.
2. **Trocar org ativa** = `POST /api/admin/switch-org` (staff @minerbz + membership + auditoria `org.switched`). Seletor de org é staff-only (`Layout` `isMinerStaffEmail`). Cliente nunca troca.
3. **Mudar papel** = `/api/admin/users/[id]` (service role).
4. **Desativar empresa** = soft delete (`DELETE /api/admin/organizations/[id]` → `deleted_at` + `pending_deletion`). NUNCA hard delete: dados preservados, reversível. Org @minerbz não desativa.
5. **Isolamento**: `accessible_org_ids()` = super_admin ∪ `miner_assignments` ∪ memberships ativas. Staff @minerbz = transversal (todas as orgs).
6. **Regra de ouro**: `can_access_org` é TRUE pro staff em TODA org; o isolamento por org ativa é responsabilidade da QUERY (`.eq('organization_id', <org ativa>)`) + org na queryKey. A RLS não isola staff.

## Gotchas
- Cross-tenant de CLIENTE já foi fechado (audit jun/26): as 63 tabelas com `organization_id` têm RLS + policy. Rode `docs/security/cross-tenant-isolation.test.sql` após TODA migration.
- O risco vivo é STAFF: leitura direta a serviço sem org ativa vaza (casos Produtos/Equipe 13/07). Sempre filtre por org na query.
- `audit_logs` é append-only: cliente não apaga a própria trilha.

## O que NÃO fazer
- Não hard delete de empresa: só soft delete.
- Não confiar só na RLS pra isolar staff: filtre por org na query.
- Não trocar org por update direto em `profiles`: use `switch-org`.
- Não mexer em banco sem passar pelo hardening ([[supabase-hardening]]).
