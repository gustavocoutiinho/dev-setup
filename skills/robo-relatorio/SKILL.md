---
name: robo-relatorio
description: Use SEMPRE que for armar, ligar ou consertar o robô de relatório semanal automático de um cliente, ou o Gustavo disser "liga o relatório semanal do <cliente>", "o robô de relatório", "por que o weekly não chegou", "coloca o <cliente> no relatório automático", "desliga o relatório do <cliente que saiu>", "relatório toda segunda". Dispara em cima da fundação weekly-report-template + crons miner-weekly-report-* (Sprint 1 das automações Miner).
---

# robo-relatorio: robô de relatório semanal por cliente

A Miner já tem a fundação do relatório semanal automático (Sprint 1): edge `weekly-report-template` no MinerOS `frocxapiowyjrdhlirnu` (`verify_jwt=true`), grava em `miner_reports_log`, disparada por cron toda segunda 09h BRT. Esta skill liga/desliga cliente nessa fundação, sem criar sistema paralelo.

## Quando disparar
- "liga o relatório semanal do <cliente>", "por que o weekly parou", "desliga o do <cliente que saiu>".
- Ligar fonte nova (Meta/Google Ads) no robô de um cliente que já está na esteira.

## Como executar
1. **Contexto primeiro.** Puxe o cliente e as fontes no vault; carteira de mídia em `dossier/24-windsor-carteira-real-midia-paga`. Nunca inventar conta.
2. **Cron por cliente.** Cada cliente é um cron pg_cron `miner-weekly-report-<slug>` em `0 12 * * 1` (seg 09h BRT) chamando a edge via helper SQL `util.invoke_edge(fn_name, payload)`. Padrão dos existentes: `-stkr-fr`, `-stkr-mm`, `-nmtl`, `-nmpr`.
3. **Fonte de dados = Windsor.** O `weekly-report-template` lê o gasto/resultado via [[windsor-liga]]. Enquanto o `windsor-ingestor` não popular `miner_reports_log` sozinho (ou não houver token Meta/Google Ads direto), o robô roda em MOCK; ligar o ingestor tira do mock.
4. **Alerta no resultado.** ROAS/CPL fora do padrão dispara o [[alerta-roas]] (NMTL já apareceu com ROAS 0.86). Edge nova segue o [[edge-kit]].
5. **DESLIGAR ex-cliente.** MGTC (Mig-Tech) saiu: remova o cron `miner-weekly-report-mgtc` pra não gastar invocação nem gerar relatório de quem não é mais cliente.
6. **Valide fim a fim** (HTTP 200 + linha em `miner_reports_log`) antes de dar por ligado; bloqueio vai pro [[radar-bloqueios]].

## Gotchas
- `verify_jwt=true` exige JWT válido; o cron usa o service_role JWT do Vault (`supabase_service_role_jwt`). Se estiver placeholder, a chamada falha.
- Cron em UTC: `0 12 * * 1` é segunda 09h BRT, não meio-dia.
- Sem Windsor ligado, o número é mock; não mande relatório mock pro cliente como se fosse real.

## O que NÃO fazer
- NÃO criar repo/sistema novo de relatório: ligar na fundação existente.
- NÃO deixar cron de ex-cliente rodando.
- NÃO reportar número de fonte que não respondeu.
