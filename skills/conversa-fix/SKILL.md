---
name: conversa-fix
description: Use SEMPRE que uma tela de atendimento/conversas de um CRM Miner mostrar "Erro ao carregar conversas" (ou inbox vazia que deveria ter mensagens), tipicamente na ForYou. Dispara com "conserta o erro ao carregar conversas", "a inbox do <cliente> não abre", "aplica o schema de mensageria", "o /messaging tá quebrado", "aparece erro vermelho no atendimento". Também quando a integração Suri/Omnichat liga a flag de mensageria mas a tabela messaging_* não existe. Aplica a migration que falta e destrava a inbox.
---

# conversa-fix: conserta "Erro ao carregar conversas"

Padrão recorrente no minercrm: a aba Atendimento (`/messaging`) mostra "Erro ao carregar conversas" em vermelho. Quase sempre a causa é a mesma: **o schema de mensageria nunca foi aplicado naquele banco**, então a query bate numa tabela que não existe e devolve 500. Esta skill aplica a migration que falta e destrava a inbox sem quebrar o resto.

## Quando disparar
- "Erro ao carregar conversas", inbox que não abre, "erro vermelho no atendimento" (ForYou foi o caso original).
- Integração `suri`/`omnichat` marcada `connected` liga a flag `hasMessaging`, mas as tabelas `messaging_*` não existem.

## Como executar
1. **Confirme a causa-raiz.** No `stpstwsqtuubpxvvexte` (minercrm), cheque `information_schema.tables like 'messaging%'`. Vazio = schema nunca aplicado (não é bug de API).
2. **Aplique as migrations em ordem:** `supabase/migrations/20260205100000_create_messaging_system.sql` + follow-ups (metrics_columns, voice_calls, fix_reaction_message_trigger). Cria as 6 tabelas `messaging_*` + RLS + triggers; a inbox carrega vazia na hora.
3. **Trigger gotcha:** use `set_updated_at()` (o `update_updated_at_column()` NÃO existe nesse DB).
4. **Coluna faltante:** o select do cliente embute `contacts.ai_paused`; se faltar, adicione (aditiva).
5. **Alinhe antes de mexer no repo** (é do Thales, [[project_nossocrm]]). Migration via MCP Supabase eu aplico; código do provider é PR.

## Gotchas
- SURI liga a flag mas **não tem provider real** em `lib/messaging/providers/` (só serve pra acender `hasMessaging`). O provider `suri.ts` de integração usa `/contacts`, lê `data.items` e pagina por `continuationToken`.
- Ligar a Suri de verdade (tools/credencial) é [[mcp-kit]]; ajustar org/tenant do cliente é [[crm-org]].
- Espelhar WhatsApp ao vivo (Baileys/Evolution) é outra coisa, não faz parte de matar o erro vermelho.

## O que NÃO fazer
- NÃO debugar a API do provider antes de checar se a tabela existe.
- NÃO criar tabela à mão: rode a migration versionada.
- NÃO pushar no main do Thales sem alinhar.
