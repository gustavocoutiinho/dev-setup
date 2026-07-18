---
name: crm-acesso
description: Use SEMPRE que precisar criar usuário, resetar senha ou conferir login de alguém no MinerCRM (time Miner ou pessoa do cliente). Dispara com "cria o acesso da <pessoa> no CRM", "convida <fulano> pro CRM", "reseta a senha do <cliente>", "fulano não consegue entrar", "o login do CRM caiu", "login pelo Google não funciona", "confere o acesso da <pessoa>". É o fluxo de Auth do Supabase, repetido umas 8-10 vezes igual. NÃO é criar a org inteira (isso é [[crm-org]]).
---

# crm-acesso: usuário, senha e login no MinerCRM

Toda semana entra gente nova no MinerCRM (time Miner ou vendedor do cliente) e às vezes o login cai. É sempre o mesmo fluxo no Supabase Auth do projeto prod `stpstwsqtuubpxvvexte`. Esta skill é o trilho pra não redescobrir do zero toda vez.

## Quando disparar
- "Cria/convida acesso", "reseta senha", "fulano não entra", "login do CRM caiu", "Google não funciona".
- NÃO use pra provisionar a empresa inteira (aí é [[crm-org]]).

## Como executar
1. **Login sempre @minerbz** pro time (gustavo@minerbz.com.br), nunca gmail.
2. **Usuário do cliente** = convite em `organization_invites` (role, `invited_name`), link `/join?token=...`. Repasse manual (Resend em sandbox só entrega pro Gustavo).
3. **Time Miner entra sozinho**: qualquer @minerbz é transversal a todas as orgs pelo e-mail, sem convite por org.
4. **Confirmação/senha**: `mailer_autoconfirm` depende de SMTP; sem SMTP, confirme manual. Ex real: Ana Cláudia (anaalbuquerque@stalker.com.br), último mile foi a confirmação de e-mail.
5. **Conferir login**: seletor de org (OrgSwitcher) é staff-only.

## Gotchas
- **Login Google caindo**: 1º suspeito é o toggle "Enable Sign in with Google" DESLIGADO no Supabase (Authentication → Sign In / Providers → Google). Sintoma no log auth: `/authorize → 400 "provider is not enabled"`. Fix: religar + Save. Teste: `curl -I ".../auth/v1/authorize?provider=google"` tem que dar 302 pra accounts.google.com, não 400.
- 2º suspeito: `site_url`/`uri_allow_list`. Se voltarem pra `localhost`, o OAuth cai em localhost pra todo mundo. `site_url=https://minercrm.vercel.app`.
- O código está certo (`app/login/page.tsx`, `app/auth/callback/route.ts`); quando o Google cai, suspeite da config do Supabase, não do código.
- daviribeiro100@gmail.com ainda acessa a PRLS por gmail: migrar pra davi@minerbz.com.br.

## O que NÃO fazer
- Não usar gmail pro time Miner (padrão gustavo@minerbz.com.br).
- Não trocar `profiles.organization_id`/`role` direto no client: o guard bloqueia ([[crm-guard]]).
- Não mexer no código antes de checar toggle/allowlist do Supabase Auth.
