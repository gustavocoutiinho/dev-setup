---
name: blindar
description: Use SEMPRE que houver brecha de segurança num sistema da Miner: portal servindo dado ou PII sem autenticação ou com gate cosmético, segredo/chave/token exposto no front ou .env versionado, Supabase com advisor aberto/RLS desligado/verify_jwt errado/PAT pra revogar, ou endpoint de IA sem cota (abuso de crédito). Dispara ao ver .json/.js de cliente respondendo 200, const X_KEY=/Bearer/sk-/shpat_/service_role no front, .env em git ls-files, advisor ERROR, ou o Gustavo dizer "isso tá exposto", "blinda o portal", "tem chave no código", "varre os segredos", "roda o hardening", "liga o RLS", "revoga a chave", "poe limite na IA", "protege o crédito", "o Supabase tá seguro?". Ação defensiva: fecha sem derrubar o cliente no ar.
---

# blindar: fecha a brecha de segurança sem derrubar o cliente no ar

Fecha vazamento e abuso em sistema da Miner sem tirar o cliente do ar. Quatro frentes que se repetem: portal servindo PII sem auth, segredo no front/git, Supabase com advisor aberto, e endpoint de IA sem cota que torra crédito. É o irmão defensivo do [[conserta-web]]: aqui o foco é fechar a brecha, não melhorar a página.

## Modos
- **portal exposto/PII** (blindar-portal): dado de cliente servível por URL direta, ou gate que só troca badge.
- **segredo no código** (varredura-segredos): chave/token no front ou `.env` versionado; move pra server-side e sinaliza rotação.
- **hardening Supabase** (supabase-hardening): advisors ERROR, RLS desligada, `verify_jwt` errado, PAT pra revogar.
- **cota de IA** (guarda-ia): rate-limit por usuário/dia na frente de qualquer chamada de IA.

## Quando disparar
- `curl https://<portal>/<arquivo>.json` responde 200 com PII (sf-snapshot.json, apollo-enriched.json, data/clientes-*.js, rastreio*.json). Confirmado no portal-accs e no portal-normatel.
- Gate de login que no `!authenticated` só faz `return`/troca classe, sem redirect nem checagem server-side.
- `const X_KEY=`, `Authorization: Bearer <literal>`, `sk-`, `shpat_`, `AIza`, `eyJhbGci`, `service_role` num arquivo do front; `.env` (não `.env.local`) em `git ls-files`.
- Advisor com ERROR, tabela sem RLS, edge function pública sem guard; antes de deployar function ou tabela nova.
- Handler/edge que chama `ai-json` (ou OpenAI/Anthropic) sem contar cota.

## Como executar
Regra comum: **mede antes, muda defensivo (mais restritivo), confirma que o sistema logado ainda sobe, deploya e confirma no ar** ([[deploy]]; editar = deployar).

**Modo portal exposto:**
1. Mapeie o público: `curl -s -o /dev/null -w "%{http_code}"` em cada arquivo de dado. `npx vercel ls <projeto>` pra achar deploy fantasma (`-fix`/`-old`/preview) que vaza o mesmo dado numa URL adivinhável.
2. Front vs backend: `grep -rn "<arquivo>"`. **Só backend** (`require('./x.json')`) → move pra `server/`/`_private/`/`data-internal/`, ajusta o require, adiciona ao `.vercelignore`. **Front consome** (`fetch('/x.json')`) → o dado vai pra trás de uma rota `/api` que valida a sessão.
3. Gate real server-side (cookie HMAC, como portal-accs/financeiro), nunca `if` no JS. `iframe` que renderiza URL do banco → sempre `sandbox`.
4. `git rm --cached <arquivos>` + endurece `.gitignore`/`.vercelignore` (cobre `*-enriched.json`, `sf-snapshot.json`, `rastreio*.json`, `data/*.js`). Verifica: o `curl` passa a 403/404 e o portal logado ainda funciona.

**Modo segredo:**
1. `grep -rnE "sk-[a-zA-Z0-9]|shpat_|AIza[0-9A-Za-z_-]{20}|eyJhbGciOi|service_role|_KEY\s*=\s*[\"'][^\"']{12}|Bearer [A-Za-z0-9._-]{20}" --include=*.{html,ts,tsx,js,jsx} .` e `git ls-files | grep -E "(^|/)\.env($|\.)"`.
2. Classifica: anon/publishable key, `VITE_*` e project id são **públicos** (ignora). `service_role`, API key paga (OpenAI/Anthropic/Apollo/Meta/`shpat_`), `SMTP_PASS`, secret de gate → NUNCA no front nem no git.
3. Move pra env/secret server-side (Vercel env, Supabase Edge secret); o front passa a chamar uma rota `/api`. Se a IA era o motivo, migra pro proxy `ai-json` ([[integra]]) e o problema some sem chave nova.
4. Toda chave já commitada ou servida ao front está comprometida: `.gitignore` não limpa o history → **rotação obrigatória** (ação do Gustavo; a skill lista qual girar e onde).

**Modo hardening Supabase** (MinerOS `frocxapiowyjrdhlirnu` / minercrm `stpstwsqtuubpxvvexte`):
1. `get_advisors` (security + performance) e `get_logs` ANTES de tocar em nada; fotografa o baseline dos endpoints de produção.
2. RLS + `REVOKE ALL` de anon/authenticated em toda tabela aberta; consumo por edge com `service_role`, nunca PostgREST direto no front.
3. `verify_jwt` default `true`. `false` só em function pública por design (magic link, portal browser) ou webhook com guard próprio (`x-miner-webhook-secret` / `x-miner-mcp-secret` / HMAC). Antes de ligar numa function chamada pelo browser, garanta que o front passa a anon key.
4. Muda em lote, reconfere `get_advisors` e confirma os endpoints byte-idênticos ao baseline (jul/26: 22 ERROR viraram 0). Se o MCP não está exposto, roda SQL pela Management API (`POST /v1/projects/REF/database/query` com PAT).

**Modo cota de IA** (`ai-json` no minercrm):
1. `grep -rniE "ai-json|openai\.com|anthropic\.com|functions/v1"` e ache quem não checa cota antes.
2. Tabela aditiva `ai_usage_daily` (`user_id`, `dia`, `used`), RLS ligada, escrita só via service_role. Limite `AI_DAILY_LIMIT` (default 50) via env, ajustável sem deploy.
3. RPC `ai_bump_usage` (upsert `used = used + 1`, `security definer`, atômico); o envelope incrementa ANTES de chamar o modelo e, ao passar do teto, devolve HTTP 429 `{ok:false, error:"limite_diario"}`. Chama o `ai-json` só depois (POST `.../functions/v1/ai-json?key=miner_ai_9f2c7b41`).
4. Identifica o usuário por JWT/`auth.uid()`, nunca id vindo do client. Dia em `America/Sao_Paulo`. Testa com `AI_DAILY_LIMIT=2` antes de subir.

## Gotchas
- Bloquear arquivo que o FRONT consome derruba a tela do cliente: cheque o consumo (`grep`) antes.
- `.gitignore`/`.vercelignore` NÃO apaga o git history: chave já commitada continua recuperável → rotação obrigatória, não opcional.
- Anon key do Supabase no front é esperada, não é vazamento; o problema é `service_role` e dado servido sem auth.
- Deploy fantasma (`<projeto>-fix`/`-old`/preview) vaza o mesmo dado numa URL adivinhável: ache TODOS os deploys.
- `verify_jwt`: ligar numa function chamada pelo browser sem o front passar anon key derruba o portal (caso `claude-proxy`/mineraco).
- P0 vivos: `portal-upload` (sobrescreve páginas com service_role) e `claude-proxy` (gasta crédito Anthropic aberto). PAT `sbp_828e...` a revogar (mandado desde jun/26, nunca feito). No minercrm, org/role/tenant é o [[crm]], não recrie regra de vínculo aqui.
- Cota de IA: incremente ANTES de chamar o modelo (ou atômico), senão duas abas passam juntas; nunca conte no client (burla em 1 F5).

## O que NÃO fazer
- NÃO confiar em gate client-side como proteção.
- NÃO deletar deploy/projeto sem o ok do Gustavo (delete é irreversível): despublica/protege primeiro.
- NÃO girar chave sozinho (é do Gustavo, e girar sem coordenar derruba quem usa): prepara e lista.
- NÃO mexer no Supabase sem `get_advisors`/`get_logs` antes (voa às cegas).
- NÃO ligar `verify_jwt` sem checar o consumidor (derruba portal).
- NÃO hardcodar o limite de IA nem contar cota no client; bloqueio nunca silencioso (sempre devolve `limite_diario` e o teto).
