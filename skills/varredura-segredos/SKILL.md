---
name: varredura-segredos
description: Use quando houver risco de segredo exposto em código da Miner: chave/token hardcoded no front, `.env` versionado no git, API key paga num bundle, ou service_role em client. Dispara ao ver `const X_KEY=`, `Authorization: Bearer <literal>`, `sk-`, `shpat_`, `AIza`, `eyJhbGci`, `.env` em `git ls-files`, ou quando o Gustavo disser "tem chave exposta?", "varre os segredos", "isso pode estar no git", "audita as chaves". Move o segredo pra server-side e sinaliza rotação. Anda junto com [[blindar-portal]].
---

# varredura-segredos

Acha segredo que não devia estar no front ou no git, move pra o lugar certo e sinaliza rotação. O que já apareceu na Miner: chave `acsc_preorc_...` hardcoded no `index.html` do portal-accs, `.env` versionado no portal-hub, `APOLLO_API_KEY` num deploy da Normatel, 17 segredos convivendo com dados públicos no portal-accs.

## Quando disparar
- Chave/token literal em arquivo do front (`.html`, `.tsx`, `.js` client).
- `.env` (não `.env.local`) aparecendo em `git ls-files`.
- Endpoint que usa API key paga sem ela estar em env/secret server-side.

## Como executar
1. **Varra.** No repo:
   `grep -rnE "sk-[a-zA-Z0-9]|shpat_|AIza[0-9A-Za-z_-]{20}|eyJhbGciOi|service_role|_KEY\s*=\s*[\"'][^\"']{12}|Bearer [A-Za-z0-9._-]{20}" --include=*.{html,ts,tsx,js,jsx} .`
   e `git ls-files | grep -E "(^|/)\.env($|\.)"`.
2. **Classifique cada achado:**
   - **Anon/publishable key do Supabase, VITE_* públicas** → ok no front, não é vazamento. Ignore.
   - **service_role, API key paga (OpenAI/Anthropic/Apollo/Meta/Shopify shpat_), SMTP_PASS, secret de gate** → NÃO pode ir ao front nem ao git.
3. **Mova o segredo.** Tira do código: vira env/secret server-side (Vercel env, Supabase Edge secret). O front passa a chamar uma rota `/api/...` que usa o segredo do lado do servidor. Se a IA era o motivo, migre pra o proxy `ai-json` ([[ia-unificada]]) e o problema some (sem chave nova).
4. **Endureça o `.gitignore`.** Cubra `.env`, `.env.*` (menos `.env.example`), e os arquivos de dado sensível.
5. **Sinalize rotação.** Toda chave que JÁ foi commitada ou servida ao front está **comprometida**: só mover não resolve, tem que **girar** a chave na origem. Isso é ação do Gustavo (ele tem acesso aos provedores); a skill lista exatamente quais girar e onde. Registra no [[radar-bloqueios]].

## Gotchas
- Mover o arquivo **não limpa o histórico do git**: a chave antiga continua recuperável no history → rotação é obrigatória, não opcional.
- Nem todo `KEY=` é segredo: `VITE_SUPABASE_PUBLISHABLE_KEY` e project id são públicos por design.
- Chave paga hardcoded no front = qualquer visitante gasta o crédito: prioridade alta.

## O que NÃO fazer
- Não girar a chave sozinho (é do Gustavo, e girar sem coordenar derruba o que a usa). Prepare e liste.
- Não tratar anon key como incidente (barulho falso).
- Não achar que `.gitignore` conserta um segredo que já subiu: só a rotação conserta.
