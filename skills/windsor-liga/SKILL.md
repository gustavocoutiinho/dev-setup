---
name: windsor-liga
description: Use SEMPRE que for ligar o ingestor do Windsor.ai no banco pra popular os relatórios, ou o Gustavo disser "liga o Windsor", "ingestor do Windsor", "puxa o gasto de mídia pro banco", "de onde vem o dado do relatório semanal", "cria o windsor-ingestor", "por que o miner_reports_log está vazio/mock". Dispara quando o robô de relatório precisa de dado vivo de mídia e a ponte Windsor → Supabase ainda não existe ou parou.
---

# windsor-liga: liga o ingestor Windsor no banco

O Windsor.ai é a ponte de dados de mídia da Miner: 52 contas conectadas (37 Meta + 6 Google Ads + 7 GA4 + 2 Search Console), ~R$137k/mês de gasto visível. Falta a edge que puxa isso pro banco toda semana; sem ela, o robô de relatório roda em mock. Esta skill liga esse ingestor.

## Quando disparar
- `miner_reports_log` vazio ou em mock; [[robo-relatorio]] sem dado real.
- "liga o Windsor", "cria o windsor-ingestor", "de onde vem o gasto do relatório".

## Como executar
1. **Desbloqueio primeiro.** O ingestor depende de `WINDSOR_API_KEY` (bloqueio conhecido de `project_relatorios_vivos`). Sem a chave, PARE e registre no [[radar-bloqueios]]; não simular dado.
2. **Criar a edge `windsor-ingestor`** no MinerOS `frocxapiowyjrdhlirnu`, seguindo o [[edge-kit]]. Ela chama a Windsor API (get_data Facebook + Google Ads) e popula `miner_reports_log` por cliente/semana (spend, clicks, impressions, conversões).
3. **Chave no lugar certo.** `WINDSOR_API_KEY` entra como secret da função / Vault, nunca chumbada no source (padrão do repo).
4. **Cron semanal.** Agendar pg_cron pra rodar antes do disparo dos `miner-weekly-report-*` (seg 09h BRT), de modo que o robô já leia dado fresco. Usa o helper `util.invoke_edge`.
5. **Mapear conta → cliente.** Windsor tem ~37 das ~40 contas reais; algumas BMs (Meio Tom, JU, Sand Blue) não aparecem. Mapeie pelo `dossier/24-windsor-carteira-real-midia-paga` e marque quem fica de fora.
6. **Validar** batendo o gasto do `miner_reports_log` contra o Windsor num período conhecido antes de dizer "no ar".

## Gotchas
- Gasto do Windsor é janela de 30 dias por padrão; para semanal, parametrize a data range.
- Contas Read-Only entram pra insight mas sem gasto recente; não trate como inativas erradas.
- GA4/Search Console conectados não viram automaticamente KPI de relatório; ligue só o que o template consome.

## O que NÃO fazer
- NÃO chumbar `WINDSOR_API_KEY` no código.
- NÃO popular `miner_reports_log` com número inventado quando a chave falta.
- NÃO criar outro caminho de ingestão paralelo ao `windsor-ingestor`.
