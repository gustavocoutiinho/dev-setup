---
name: mcp-kit
description: Use SEMPRE que for criar ou endurecer um MCP server custom da Miner pra uma ferramenta de atendimento/dado multi-tenant (Suri, Omnichat, Blip, ChatGuru, Reportei ou uma API nova de cliente). Dispara com "cria um MCP pro <sistema>", "quero acessar a <API> multi-cliente pelo Claude", "adiciona tools de <ferramenta>", "endurece o MCP", "por que o MCP dá 401", "registra o MCP no Claude". Também quando a integração precisa falar com N clientes por uma credencial só. Nasce no padrão (HTTP no Supabase + secret guard + miner_api_credentials + log), nunca script solto.
---

# mcp-kit: MCP custom multi-tenant no padrão Miner

A Miner já tem 5 MCP servers custom de atendimento/dado, 51 tools no total: Suri v4 (13), Omnichat v3 (14), Blip v3 (11), ChatGuru v2 (7), Reportei v1 (6). Todos no mesmo trilho. Esta skill nasce um MCP novo (ou endurece um) nesse padrão: server HTTP no Supabase, multi-tenant por credencial, com secret guard e observabilidade.

## Quando disparar
- "cria/endurece um MCP pro <sistema>", "acessa a <API> multi-cliente pelo Claude", "adiciona tools de <ferramenta>".
- MCP dando 401, handshake falhando, ou precisa registrar no Claude.
- Uma API de cliente precisa ser falada por N tenants com uma credencial só.

## Como executar
1. **Contexto primeiro** ([[obsidianminer]]): a nota [[miner-automation-infra]] tem os endpoints e o estado de cada MCP. Não invente path.
2. **Paths por fonte oficial.** Valide cada rota no swagger/source oficial (OmniChat API-Public-Swagger, LIME Templates do Blip, `suri.ts` do minercrm), nunca chute. O bug Suri `/users` vs `/contacts` nasceu de chute.
3. **Multi-tenant via `miner_api_credentials`** (MinerOS `frocxapiowyjrdhlirnu`): a tool recebe `{cliente}`, o server lê a credencial daquele tenant. Nada de token hardcoded no source.
4. **Secret guard `x-miner-mcp-secret`** em toda tool: sem header = 401. É a porta.
5. **Log em `miner_mcp_call_log`** com `latency_ms` (observability).
6. **Registro em `~/.claude.json`** com o header `x-miner-mcp-secret`. Smoke test: 401 sem header, `initialize` OK, `tools/list` retornando, `*_list_clientes` sem erro.

## Gotchas
- Credencial `AGUARDANDO_TOKEN` ou começando com `<`: retorne erro claro, não bata 401 cego na API do cliente.
- Blob `{enc}` que não decripta = chave rotacionada, é caso de [[cripto-integra]], não de código do MCP.
- Cron/webhook que alimenta o mesmo dado é [[edge-kit]]; "erro ao carregar conversas" no CRM é [[conversa-fix]].

## O que NÃO fazer
- NÃO hardcodar token no source: credencial vem de `miner_api_credentials` por tenant.
- NÃO expor tool sem `x-miner-mcp-secret`.
- NÃO inventar endpoint: valide no swagger/source oficial antes.
