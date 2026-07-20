---
name: crm
description: "Use SEMPRE que o trabalho for dentro do MinerCRM multi-tenant (Supabase prod stpstwsqtuubpxvvexte): criar org/tenant nova, criar usuário/resetar senha/conferir login, isolar tenant e RLS, ligar/desligar módulo ou menu por empresa, migrar base do RD Station, consertar 'erro ao carregar conversas', ou score/roteamento regional de lead. Dispara com 'cria a org do <cliente> no CRM', 'onboarding do <cliente> no CRM', 'convida <fulano> pro CRM', 'reseta a senha', 'login não funciona', 'login pelo Google caiu', 'vazou entre tenants', 'confere o isolamento', 'esconde o módulo x da empresa y', 'migra da RD pro CRM', 'erro ao carregar conversas', 'pontua o lead por região'."
---

# crm: operação do MinerCRM multi-tenant

O MinerCRM é SaaS multi-tenant (Next.js + Supabase prod `stpstwsqtuubpxvvexte`, prod=main). Cada cliente é uma org (PRLS, ForYou, Hidrotintas, Maresia, Stalker). Esta skill é o trilho das operações que se repetem dentro do CRM: provisionar org, dar acesso, isolar tenant, ligar/desligar módulo, migrar do RD, destravar a inbox e pontuar lead. Nunca invente dado do cliente: puxe o [[obsidianminer]] primeiro.

## Modos
- **criar org**: empresa nova nascendo completa e isolada (org + segment + membership + nav_items + elegibilidade).
- **acesso**: usuário, senha e login (Auth do Supabase); o fluxo repetido umas 8-10 vezes.
- **tenant guard / RLS**: isolamento entre clientes, troca de org, papel e desativação.
- **módulos por empresa**: ligar/desligar item de menu por org (`/admin/empresas`).
- **migrar RD**: trazer o funil do RD Station pelo motor `stalker_*`/`maresia_*`.
- **conserta inbox**: matar "Erro ao carregar conversas" aplicando o schema de mensageria.
- **score regional de lead**: pontuar e rotear lead por região/porte (fluxo HDTS).

## Quando disparar
- "cria/onboarda a org do <cliente>", cliente novo sem `organization_id`.
- "convida <fulano>", "reseta a senha", "fulano não entra", "login do Google caiu".
- "um cliente tá vendo dado de outro", "vazou entre tenants", "desativa a empresa <x>".
- "esconde/liga o módulo <x> da empresa <y>", "matriz de módulos".
- "migra o <cliente> da RD", "o CRM tá com menos deals que o RD".
- "Erro ao carregar conversas", inbox que não abre (ForYou foi o caso).
- "pontua o lead por região", "por que lead da Bahia entrou como quente".

## Como executar
Base: Supabase minercrm `stpstwsqtuubpxvvexte`, prod=main; toda mudança de código deploya pela última main via [[deploy]] (Vercel exige commit verificado). Banco só mexe passando pelo hardening ([[blindar]]).

- **Criar org:** RPC `create_org_with_invite('Nome','slug','active','<email-dono>',7)` com contexto JWT do super_admin. `organizations.segment` = varejo | b2b | ambos; B2B usa `feature_overrides.account_person_type` = pf (Stalker) | pj (Hidrotintas, Maresia). Defina `nav_items` (modo módulos) e a régua `<cliente>_apply_eligibility` com o foco geográfico próprio. Time @minerbz entra sozinho pelo e-mail; dono do cliente vai por `organization_invites` (role admin), só na PRÓPRIA org.
- **Acesso:** time sempre @minerbz (gustavo@minerbz.com.br), nunca gmail. Cliente = `organization_invites` + link `/join?token=...` (Resend em sandbox só entrega pro Gustavo, repasse manual). Login Google caindo: 1º suspeito é o toggle "Enable Sign in with Google" DESLIGADO no Supabase Auth (sintoma: `/authorize → 400 "provider is not enabled"`); 2º é `site_url` voltar pra localhost (`site_url=https://minercrm.vercel.app`). O código está certo, suspeite da config.
- **Guard/RLS:** `organization_id`/`role` só mudam via service_role (trigger `trg_protect_profile_tenant`), nunca update direto em `profiles`. Trocar org = `POST /api/admin/switch-org` (staff-only + auditoria `org.switched`). Desativar empresa = soft delete (`deleted_at` + `pending_deletion`), NUNCA hard delete. `accessible_org_ids()` isola cliente, mas staff @minerbz é transversal: o isolamento de staff é da QUERY (`.eq('organization_id', <org ativa>)` + org na queryKey). Rode `docs/security/cross-tenant-isolation.test.sql` após TODA migration.
- **Módulos:** `org_nav_modules.nav_items jsonb` = mapa `id → false` (ausência = ligado, 100% retrocompatível). Fonte única `lib/nav/managedNavItems.ts`; `Configurações`/`Perfil` são `core`, não desligáveis. UI na aba **Módulos** de `app/admin/empresas/EmpresasClient.tsx`; backend `PATCH /api/admin/organizations/[id]/modules` (auditado). Desligar só some do menu, não trava a rota.
- **Migrar RD:** credenciais = token da conta + pipeline id + responsável (Stalker: token `68ed0b11e131910020b18ed5`, pipeline `68ef8dfb75222800145ef320`). Edge `stalker-rd-sync` → `stalker_load_rd_batch` grava `deals` + `contacts`, cron 15 min (`?key=stkr_sync_7f3a9c2e`). Traz TODOS os campos; casa por `deals.external_id` + telefone E.164. A régua `<cliente>_apply_eligibility` projeta `raw_meta` → `contacts.status`/`stage`. Confira a dimensão (deals RD × deals entrados). Base fora do RD entra por [[dados]].
- **Conserta inbox:** cheque `information_schema.tables like 'messaging%'`; vazio = schema nunca aplicado (não é bug de API). Aplique `supabase/migrations/20260205100000_create_messaging_system.sql` + follow-ups → 6 tabelas `messaging_*` + RLS; a inbox carrega vazia na hora. Ligar a Suri de verdade é [[integra]]; espelhar WhatsApp ao vivo é [[zap]].
- **Score regional:** ingestão idempotente por `external_id` (`hdts-leads-sync`); enriqueça por CNPJ (Apollo). Edge `hdts-lead-scorer` no Supabase MinerOS `frocxapiowyjrdhlirnu` (`verify_jwt=false` + header `x-miner-webhook-secret`) grava em `hdts_lead_scores`. Regra HDTS: **BA/PA/SE/MA/PE/AM = frio**. Score vira temperatura e distribui round-robin entre `profiles` role `vendedor` (gerente não recebe). Volume semanal via [[robo]]; falta de secret/chave Apollo, PARE e registre no [[monitor]].

## Gotchas
- `create_org_with_invite` precisa de `set_config('request.jwt.claims', ...)` na MESMA statement (`auth.uid()` vem nulo via MCP). Coluna de ordem dos stages é `"order"`, não `position`; não existe tabela `stages`.
- Cliente NUNCA tem membership em outra org nem na org interna Miner (`56459edd-2bec-4e0e-8e0b-822658216587`): incidente Marina→Hidrotintas. Incidente 10/07: Stalker aparecendo na ForYou.
- Correção por UPDATE direto em `contacts` é REVERTIDA pelo cron em ≤15 min: mexa no motor (função + eligibility), nunca nos dados. Perda no RD = `win=false` + motivo, NÃO a etapa "Base Perdida".
- Migration de mensageria usa `set_updated_at()` (o `update_updated_at_column()` NÃO existe nesse DB). Suri acende a flag `hasMessaging` mas não tem provider real.
- `verify_jwt=false` só é seguro porque valida `x-miner-webhook-secret`: sem header, a função recusa.

## O que NÃO fazer
- NÃO criar org sem segment, nem dar membership de cliente fora da própria org.
- NÃO fazer update direto em `profiles` (o guard bloqueia); troca de org só via `switch-org`.
- NÃO hard delete de empresa: só soft delete. Não confiar só na RLS pra isolar staff.
- NÃO sanear dado na mão na migração (o cron desfaz); não copiar a régua da Stalker pra outro cliente (foco geográfico difere); `stalker_*` e `maresia_*` são separados.
- NÃO debugar a API do provider antes de checar se a tabela `messaging_*` existe.
- NÃO usar gmail pro time; não pushar no main do Thales sem alinhar.
- NÃO mandar lead pro vendedor sem passar pelo score; não deixar webhook aberto sem o secret.
