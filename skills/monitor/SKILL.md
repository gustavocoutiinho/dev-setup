---
name: monitor
description: Use SEMPRE que precisar vigiar e ser avisado antes de virar incidente: saúde de portais/edges/MCPs/login, custo de MCPs/Vercel/Supabase/OpenRouter e desperdício de ex-cliente, credencial/token/OAuth vencendo (token Meta expira 22/08), ROAS/CPL fora do padrão, task do Asana vencida/recorrente, ou o radar de bloqueios e decisões pendentes. Dispara com "tá tudo no ar", "algum portal caiu", "quanto tá gastando", "tem desperdício", "o que tá pra vencer", "quando expira o token", "o ROAS tá estranho", "o que tá atrasado", "o que depende de mim", "quais bloqueios".
---

# monitor: vigia saúde, custo, prazo, ROAS, atraso e bloqueio

Nada na Miner avisa quando algo cai, sangra dinheiro, vence ou fura o padrão: 35 projetos Vercel, edges no MinerOS, 5 MCPs custom, login do MinerCRM, tokens com prazo, ROAS por cliente e backlog do Asana, tudo sem alarme. Esta skill vigia e cobra **antes de virar incidente**. Ela detecta, não conserta nem decide (ligar/consertar é [[robo]], fechar risco é [[blindar]]).

## Modos
- **saúde** (monitor-saude): pinga portais/edges, smoke test dos MCPs e do login, roda advisors.
- **custo** (monitor-custo): soma gasto de MCPs/Vercel/Supabase/OpenRouter e caça desperdício.
- **credencial/prazo** (monitor-credencial): calcula os dias até vencer e cobra com antecedência.
- **ROAS/CPL** (alerta-roas): semáforo por cliente sobre o `miner_reports_log`.
- **atraso Asana** (alerta-atrasos): junta as tasks vencidas e marca as recorrentes.
- **radar de bloqueios** (radar-bloqueios): lista o que trava e depende do Gustavo, destrava quando ele resolve.

## Quando disparar
- Saúde: "tá tudo no ar / algum portal caiu / o login funciona / os MCPs respondem"; após deploy ou hardening.
- Custo: "quanto tá gastando / tem desperdício / a chave de IA tá acabando / algum robô de ex-cliente rodando".
- Prazo: "o que tá pra vencer / quando expira o token / me avisa antes de vencer"; ao ver credencial com validade.
- ROAS: "o ROAS tá estranho / algum cliente fora do padrão / coloca semáforo"; ao gerar relatório e a métrica destoar.
- Atraso: "o que tá atrasado / me cobra os atrasos / o que arrasta há semanas"; ao revisar backlog ou preparar 1:1.
- Bloqueio: "o que falta / o que depende de mim / o que tá travado / quais bloqueios"; ao ver `[VC]` no plano.

## Como executar
Comum: rode na rotina (encaixa no `miner-daily-briefing` 06:30 BRT), **avise só o que saiu do baseline** (DM Slack / WhatsApp / linha no daily-brief) e **registre no vault** (`~/ObsidianVaults/miner`) pra não repetir o mesmo alerta nem perder contagem entre sessões. Detecta, não age.

- **Saúde:** pinga esperando 200 `portal.minerbz.com.br`, `normatel.vercel.app`, `prls.vercel.app`, `miner-aco-cearense.vercel.app`, `app-relatorios.vercel.app` (reintente antes de alarmar). Edges do MinerOS (`frocxapiowyjrdhlirnu`) em ACTIVE; smoke test dos 5 MCPs (Suri, Omnichat, Chat.guru, Blip, Reportei) com handshake `initialize` + guard `x-miner-mcp-secret` (401 sem header). Login MinerCRM (`stpstwsqtuubpxvvexte`): `curl -I ".../auth/v1/authorize?provider=google"` tem que dar **302**, não 400 (incidente 15/06, toggle Google desligado). `get_advisors` ERROR = **0** (baseline do [[blindar]]).
- **Custo:** OpenRouter tem **teto de $5 por chave** (4 chaves, `gustavo@minerbz.com.br`, $10 de crédito); avise a que se aproxima antes de o produto cair. Vercel: cruze com [[faxina-web]] pra achar deploy morto/duplicado. Supabase: crons de alta frequência (`*/15`) multiplicam invocação. **Ex-cliente sangrando:** `miner-weekly-report-mgtc` roda pra MGTC (saiu). Windsor ~R$137k/mês é **verba do cliente**, vigie a variação, não o valor absoluto.
- **Credencial/prazo:** token Meta em `~/.meta-ads/current_token.txt` (**expira 22/08/2026 ~11:47**, renova com `bash ~/.meta-ads/refresh.sh <token novo>`), cópia em `vault.secrets` `meta_access_token`. As **7 credenciais P1**: Meta, Google Ads, Asana PAT, Drive OAuth, Webhook HDTS, HubSpot Private App, Kinbox API (+ OAuth Granola/Box/Gong). Calcule os dias e cobre a partir de ~15 (o lembrete Asana `1215969231104109` + evento 21/08 avisam só 1 dia antes). A ação é do Gustavo; ao renovar, reagende o próximo vencimento.
- **ROAS/CPL:** leia `miner_reports_log` (`source in (meta_ads, all_ads, google_ads)`, `metric in (roas, cpl, ctr, receita, investimento)`, `delta_pct` já vem calculado). Compare com o padrão do cliente (NMTL: ROAS 30d 1.5+, 60d 2.0+): semáforo verde/amarelo/vermelho. **NMTL apareceu com ROAS 0.86** (semana 21-27/05) e o alerta morreu no log. Não acenda vermelho por um único breakdown ([[midia]]).
- **Atraso Asana:** `get_my_tasks` (owner `gustavo@minerbz.com.br`, `completed=false`), `due_on < hoje` em America/Sao_Paulo (não UTC), agrupe por projeto (~23 que ele é owner) do mais antigo. Flag **"RECORRENTE"** à mesma `gid` que aparece em 3+ varreduras (persista a contagem no vault). Backlog real: 21 tasks em NMTL+NMPR, 12 vencidas, a mais antiga de 14/04.
- **Radar de bloqueios:** fontes `~/Documents/Claude/plano-modulos-e-skills.md` (itens `[VC]`) + vault via [[obsidianminer]] (project_relatorios_vivos = `WINDSOR_API_KEY`; token Meta 60d; PAT a revogar). Ordene por prazo quente (token Meta 22/08 = item 108, derruba todos os relatórios vivos). Ao Gustavo resolver, **destrave só depois de confirmar que a credencial funciona** e aponte a skill que volta a rodar ([[robo]]).

## Gotchas
- **302 vs 400 no authorize** é o toggle Google (15/06); **portal stale ≠ portal caído** (dado velho é ingestão, não disponibilidade).
- **Teto de $5** estourado para o produto que usa a chave: avise antes, não depois. Cron de ex-cliente é custo puro, mas confirme o churn ([[cliente]]) antes de propor matar.
- `refresh.sh` atualiza `~/.claude.json` + `current_token.txt` mas **não** o `vault.secrets`: re-sincronize a cópia do cofre, senão o ingestor segue com o token velho. Não há auto-renovação do token Meta (manual a cada ~60d).
- Semáforo é por cliente (o normal da Normatel não é o da Estela); ROAS zerado costuma ser fonte faltando, não performance ruim; não alarme sobre competência stale.
- Recorrente ≠ recriada: conte pela mesma `gid`; sem persistir, toda varredura zera. `[VC]` às vezes é decisão, não credencial: diga exatamente o que se pede ao Gustavo, e não invente prazo.

## O que NÃO fazer
- NÃO religar toggle, redeployar, pausar campanha, girar chave, renovar token, fechar/reatribuir task nem desligar cron por conta própria: monitor **avisa**, quem age é o Gustavo/time ([[cos]] redistribui carga).
- NÃO alarmar por timeout único (reintente) nem sobre dado de teste/competência velha.
- NÃO comprar crédito, assinar plano nem mexer em pagamento.
- NÃO expor chave nem pôr dado sensível em modelo free ([[ia]]).
- NÃO dar item por destravado no boca a boca nem deixar o radar só na conversa: persista no vault.
