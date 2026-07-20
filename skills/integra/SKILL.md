---
name: integra
description: Use SEMPRE que for construir integração/infra no Supabase da Miner: criar MCP server custom multi-tenant (Suri/Omnichat/Blip/ChatGuru/Reportei/API nova), criar edge function (webhook/sync/cron/proxy), criar a edge de IA (proxy ai-json/OpenRouter), ou rotacionar/consertar credencial encriptada {enc}. Dispara com "cria um MCP pro <sistema>", "cria uma edge function", "agenda o sync", "edge de IA", "a integração não conecta", "o token não decripta", "rotaciona a credencial".
---

# integra: integração e infra no Supabase da Miner

Toda integração da Miner (MCP de atendimento, webhook de lead, sync de base, proxy de IA) nasce no mesmo trilho: HTTP no Supabase, multi-tenant por credencial, com guard e observabilidade. Sem trilho, cada uma nasce com auth diferente e vira buraco. Esta skill cobre os quatro casos por modos.

## Modos
- **MCP custom**: server multi-tenant pra uma ferramenta (Suri/Omnichat/Blip/ChatGuru/Reportei ou API nova de cliente).
- **edge function**: webhook, sync, cron ou proxy no Supabase.
- **edge de IA**: o scaffold cru do proxy `ai-json` (OpenRouter).
- **cripto {enc}**: rotacionar/re-encriptar credencial que parou de decriptar.

## Quando disparar
- "cria/endurece um MCP pro <sistema>", "acessa a <API> multi-cliente pelo Claude", MCP dando 401.
- "cria uma edge function", "monta o webhook de <sistema>", "agenda o sync", "roda 1x/dia sozinho".
- "cria uma edge de IA", "scaffold da ai-json", "proxy de IA no Supabase".
- "a integração do <cliente> não conecta", "o token não decripta", "rotaciona a credencial", "conectado mas o sync falha".

## Como executar
Comum: puxe [[obsidianminer]] e a nota miner-automation-infra pro estado real (endpoints, o que já existe). Reuse function/tabela/credencial antes de criar. Valide toda rota no swagger/source oficial, nunca chute (o bug Suri `/users` vs `/contacts` nasceu de chute).

**MCP custom** (MinerOS `frocxapiowyjrdhlirnu`)
- Multi-tenant via `miner_api_credentials`: a tool recebe `{cliente}`, o server lê a credencial daquele tenant. Nada de token hardcoded.
- Secret guard `x-miner-mcp-secret` em toda tool (sem header = 401). Log em `miner_mcp_call_log` com `latency_ms`.
- Registra em `~/.claude.json` com o header. Smoke test: 401 sem header, `initialize` OK, `tools/list` respondendo.
- Já rodam 5 MCPs neste padrão: Suri v4 (13 tools), Omnichat v3 (14), Blip v3 (11), ChatGuru v2 (7), Reportei v1 (6).

**edge function**
- `verify_jwt=true` por padrão. Só `false` quando é chamada por fora sem JWT (webhook, cron), e **aí valida um guard próprio**: `x-miner-webhook-secret` (padrão hdts-lead-scorer), `x-cron-secret`, `?key=<slug>_secret` ou HMAC. Nunca function aberta sem guard.
- Cron chama via `util.invoke_edge(fn, payload)` (pg_net + service_role JWT do Vault) ou `net.http_post` com o header de secret. Agenda com `pg_cron` (UTC; 07h BRT = `0 10 * * *`). Job de fila: **desagende quando terminar** (`cron.unschedule`), senão roda idle pra sempre (caso `foryou-olist-enrich-contacts`).
- Automação de negócio recorrente (funil, anúncio, relatório) é [[robo]]; aqui é só a infra crua.

**edge de IA** (minercrm `stpstwsqtuubpxvvexte`)
- `verify_jwt=false`, auth por `?key=miner_ai_9f2c7b41` na URL (não é segredo). Reusa o secret `OPENROUTER_API_KEY`, não cria chave nova.
- Contrato: `POST {system, user, model?, temperature?}` → `{ok, data, usage}`. Proxy burro de chave, sem lógica de negócio. Default `google/gemini-2.5-flash-lite` (pago, não treina: pode passar dado de cliente).
- Aditivo + dry-run: grava só em coluna jsonb já existente (`ai_meta`/`metadata`). Encaixar IA num produto que já roda é [[ia]].

**cripto {enc}** (minercrm `stpstwsqtuubpxvvexte`)
- `integrations.credentials` guarda `{enc: base64(salt|iv|tag|cipher)}`, AES-256-GCM, chave = `scrypt(INTEGRATIONS_ENCRYPTION_KEY, 'integrations-salt-v1', 32)` (`lib/integrations/encryption.ts`). Teste decrypt local antes de tocar em código.
- Se falha ("Unsupported state or unable to authenticate data"), a chave rotacionou (entre 09/06 e 03/07): blobs antigos são lixo. Regrave com a chave atual (`vercel env pull` + script de ~20 linhas espelhando `encryption.ts` + `UPDATE integrations SET credentials = ...`). Pendentes: ForYou Olist, PRLS Bling, ForYou Suri, Maresia Suri.

## Gotchas
- Credencial `AGUARDANDO_TOKEN` ou começando com `<`: retorne erro claro, não bata 401 cego na API do cliente.
- Endpoint autenticado NUNCA com `Cache-Control` compartilhado (s-maxage): a CDN serve resposta logada pra quem não tem sessão (vazou faturamento na PRLS). Use `private, no-store`.
- `verify_jwt=false` sem guard = qualquer um chama (caso `claude-proxy`/`portal-upload`): endurecer é [[blindar]].
- Modelo de IA pago é o default: NÃO rebaixar pra free com dado de cliente (free pode treinar). Cota e paralelismo com teto ([[ia]]).
- NUNCA troque `INTEGRATIONS_ENCRYPTION_KEY` sem migrar os blobs: foi o que gerou a dor toda. Token que vazou em chat/log: rotacione na origem ([[blindar]]).

## O que NÃO fazer
- NÃO hardcodar token no source: credencial vem por tenant (`miner_api_credentials`) ou do blob `{enc}`.
- NÃO expor tool/function sem guard (`x-miner-mcp-secret` ou secret próprio).
- NÃO cachear resposta autenticada, nem inventar endpoint sem validar no swagger.
- NÃO trocar a chave de encriptação sem plano de migração; sync de base de cliente é [[dados]].
