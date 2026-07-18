---
name: monitor-saude
description: Use SEMPRE que precisar saber se os portais, edge functions, MCPs e o login continuam de pé, ou quando algo pode ter caído sem ninguém perceber. Pinga os endpoints de produção, faz smoke test dos MCPs e do login do MinerCRM e roda os advisors do Supabase, avisando quando algo sai do baseline (foi assim que o login Google do MinerCRM ficou fora no ar sem alarme). Dispara com "tá tudo no ar?", "algum portal caiu?", "o login tá funcionando?", "health check", "os MCPs respondem?", "checa a saúde dos sistemas", "algo quebrou?".
---

# monitor-saude: health check dos portais, edges, MCPs e login

São **35 projetos Vercel**, **6+ edge functions** no MinerOS, **5 MCPs custom** (51 tools) e o login do MinerCRM, e nada avisa quando um cai. No incidente de **15/06** ninguém entrava pelo Google no MinerCRM porque o toggle "Enable Sign in with Google" tinha sido desligado no Supabase Auth, e só se descobriu quando reclamaram. Esta skill pinga, testa e avisa quando algo sai do baseline. Ela detecta, não conserta.

## Quando disparar
- Rotina de checagem (encaixa no daily-briefing) ou "tá tudo no ar / algum portal caiu?".
- Após deploy, mudança de config ou hardening.
- Gustavo pediu health check, "o login funciona?", "os MCPs respondem?".

## Como executar
1. **Pinga produção** esperando 200: `portal.minerbz.com.br`, `normatel.vercel.app`, `prls.vercel.app`, `miner-aco-cearense.vercel.app`, `app-relatorios.vercel.app`. Um timeout isolado não é queda: reintente antes de alarmar.
2. **Edge functions** do MinerOS (`frocxapiowyjrdhlirnu`): confirme status ACTIVE das de produção (`report-data`, `meta-ingestor`, `windsor-ingestor`, `portal-mslz`, etc).
3. **Smoke test dos 5 MCPs** (Suri, Omnichat, Chat.guru, Blip, Reportei): handshake `initialize` OK e o secret guard `x-miner-mcp-secret` barrando (401 sem header).
4. **Login MinerCRM** (`stpstwsqtuubpxvvexte`): `curl -I ".../auth/v1/authorize?provider=google"` tem que dar **302** pra accounts.google.com, não 400 ("provider is not enabled").
5. **Advisors do Supabase** (`get_advisors`): ERROR deve ser **0** (baseline do hardening, ver [[supabase-hardening]]). ERROR>0 = regressão de segurança.
6. **Avise** o que saiu do baseline (Slack/WhatsApp/daily-brief) e registre no vault.

## Gotchas
- **302 vs 400 no authorize** é o sintoma do toggle Google (incidente 15/06); o fix é religar + Save, mas quem faz é o Gustavo.
- **Portal stale ≠ portal caído:** dado velho é problema de ingestão, não de disponibilidade; separe os dois avisos.
- Endpoints de produção têm baseline byte-idêntico do hardening: mudança inesperada é sinal, não ruído.

## O que NÃO fazer
- NÃO religar toggle, redeployar nem mexer em RLS sozinho sem ok do Gustavo.
- NÃO alarmar por um timeout único: reintente primeiro.
- NÃO confundir custo com saúde: gasto é [[monitor-custo]].
