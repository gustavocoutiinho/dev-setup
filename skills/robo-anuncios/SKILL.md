---
name: robo-anuncios
description: Use SEMPRE que for armar ou consertar o checador diário de "os anúncios estão rodando?", ou o Gustavo disser "os anúncios estão no ar?", "valida se os anúncios estão rodando", "caiu alguma campanha?", "checa se parou anúncio", "alerta se conta pausar". Dispara na task recorrente "Validar Se Anúncios Estão Rodando" (aparece 4x/semana) e no cron miner-ads-running-check-daily.
---

# robo-anuncios: checador diário "os anúncios estão rodando?"

"Validar Se Anúncios Estão Rodando" é task manual que reaparece 4x por semana. Um anúncio pausado ou conta bloqueada sem ninguém ver = verba parada e cliente sem entrega. Esta skill mantém o checador automático que roda isso todo dia de manhã.

## Quando disparar
- Task "Validar Se Anúncios Estão Rodando" de qualquer cliente.
- "os anúncios estão no ar?", "caiu campanha?", "checa se parou anúncio".

## Como executar
1. **Fundação já existe.** Edge `ads-running-check` no MinerOS `frocxapiowyjrdhlirnu` (`verify_jwt=true`), disparada pelo cron pg_cron `miner-ads-running-check-daily` em `0 10 * * *` (07h BRT).
2. **Cobertura das contas.** A checagem bate na Meta API e na Google Ads API pra ver se há campanha ativa entregando por cliente. Carteira real (37 Meta + 6 Google) em `dossier/24-windsor-carteira-real-midia-paga`.
3. **O que conta como alerta.** Conta sem nenhuma campanha ativa, campanha ACTIVE com entrega zerada, ou conta em erro de política (ex.: risco WhatsApp Business da Hidrotintas). Anomalia vira aviso.
4. **Roteia o alerta.** Sinal fora do padrão desce pro [[alerta-roas]] / entra no relatório do [[robo-relatorio]]; hoje o alerta é in-app (não há webhook externo Slack/e-mail na infra ainda).
5. **Edge nova ou ajuste** segue o [[edge-kit]]; valide HTTP 200 antes de confiar.

## Gotchas
- `verify_jwt=true`: o cron precisa do service_role JWT do Vault; placeholder derruba a chamada.
- Cron em UTC: `0 10 * * *` é 07h BRT.
- Google Ads pode não estar conectado por token direto em todos os clientes; sem credencial, a fonte fica declarada e inativa, não simulada.
- "Campanha ACTIVE" não garante entrega; cheque impressão/gasto do dia, não só o status.

## O que NÃO fazer
- NÃO dar "tudo certo" checando só status sem olhar entrega.
- NÃO simular resposta de conta que a API não devolveu.
- NÃO deixar o checador rodando pra ex-cliente.
