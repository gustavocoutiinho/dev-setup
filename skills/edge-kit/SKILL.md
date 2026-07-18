---
name: edge-kit
description: Use SEMPRE que for criar uma edge function nova no Supabase da Miner (webhook, sync, cron, proxy) ou agendar uma pra rodar sozinha. Dispara com "cria uma edge function pra <X>", "monta o webhook de <sistema>", "agenda o sync do <cliente>", "roda isso 1x/dia sozinho", "edge function com cron", "por que a function dá 401". Também quando um cron precisa chamar uma function com service_role. Nasce no padrão (verify_jwt certo + guard + invoke_edge + pg_cron), nunca improvisado.
---

# edge-kit: edge function Supabase no padrão Miner

A Miner roda dezenas de edge functions (webhook de lead, sync de Suri/Olist, cron de relatório) no MinerOS (`frocxapiowyjrdhlirnu`) e no minercrm. Sem trilho, cada uma nasce com auth diferente e vira buraco de segurança. Esta skill scaffolda a function certa: `verify_jwt` no valor correto, guard próprio quando é pública, e agendamento por cron real.

## Quando disparar
- "cria uma edge function pra <X>", "monta o webhook de <sistema>", "agenda o sync do <cliente>", "roda 1x/dia sozinho".
- Cron que precisa chamar uma function com service_role.

## Como executar
1. **Contexto** ([[obsidianminer]], [[miner-automation-infra]]): reuse function/tabela que já exista pro cliente antes de criar.
2. **`verify_jwt=true` por padrão.** Só use `verify_jwt=false` quando a rota é chamada por fora sem JWT (webhook, cron via `net.http_post`) e **aí ela valida um guard próprio**: `x-miner-webhook-secret` (padrão hdts-lead-scorer), `x-cron-secret`, `?key=<slug>_secret`, ou HMAC. Nunca function aberta sem guard.
3. **Cron chama via `util.invoke_edge(fn, payload)`** (pg_net + service_role JWT do Vault) quando quer JWT válido; ou `net.http_post` com o header de secret quando é `verify_jwt=false`.
4. **Agende com `pg_cron`** (horários em UTC; 07h BRT = `0 10 * * *`). Chunked + time-budget pra job longo.
5. **Deploy + smoke test:** 401 sem guard, 200 com. Confirme no log.

## Gotchas
- Job que drena uma fila: **desagende quando terminar** (`cron.unschedule`), senão roda idle pra sempre (caso `foryou-olist-enrich-contacts`).
- Endpoint autenticado NUNCA com `Cache-Control` compartilhado (s-maxage): a CDN serve a resposta logada pra quem não tem sessão (vazou faturamento na PRLS). Use `private, no-store`.
- `verify_jwt=false` sem guard = qualquer um chama (caso `claude-proxy`/`portal-upload`): endurecer é [[supabase-hardening]].
- Ligar fonte de dado de relatório (Windsor) é [[windsor-liga]]; IA dentro da edge é [[edge-ia]].

## O que NÃO fazer
- NÃO deixar function pública sem guard.
- NÃO cachear resposta autenticada.
- NÃO esquecer de desagendar cron de fila terminada.
