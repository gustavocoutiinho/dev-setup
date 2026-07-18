---
name: cliente-fora
description: Use SEMPRE que a Miner sair de um cliente (churn, demissão, cliente pediu pra sair) e for preciso desligar tudo que ainda consome operação. Dispara com "o <cliente> saiu", "desliga o <cliente>", "offboarding do <cliente>", "encerra a operação do <cliente>", "ainda tem coisa rodando pro ex-cliente?", ou quando um ex-cliente aparece num cron, anúncio no ar ou grupo WhatsApp aberto. Ex-cliente vaza operação: desliga sem hard-delete, marca churn.
---

# cliente-fora: offboarding: desliga tudo do ex-cliente

Ex-cliente na Miner continua consumindo operação: o cron `miner-weekly-report-mgtc` roda toda segunda pra MGTC (ex-cliente), Luxo e Sodine com anúncio no ar, grupos WhatsApp de DLT/Tallis/Lasso/Cacau/MGTC abertos. Esta skill desliga cada ponta que sobra, sem apagar dado.

## Quando disparar
- Cliente saiu (churn/demissão) e precisa encerrar acessos, crons, anúncios.
- Ex-cliente detectado ativo: cron rodando, campanha no ar, grupo aberto.
- "Desliga o <cliente>", "offboarding", "ainda tem coisa rodando?".

## Como executar
1. **Org no CRM: soft-delete, nunca hard.** `DELETE /api/admin/organizations/[id]` marca `deleted_at` + `pending_deletion`, reversível ([[crm-guard]]). Nunca dropar dado.
2. **Asana.** Arquiva o projeto do cliente (não deleta). Confirma a sigla no [[obsidianminer]] antes.
3. **Desliga os crons.** Remove/desativa os `miner-weekly-report-<sigla>` e afins no pg_cron do MinerOS (`frocxapiowyjrdhlirnu`). É o que mais vaza ([[monitor-custo]]).
4. **Para os anúncios.** Pausa campanhas Meta/Google ativas (Luxo e Sodine ficaram no ar por esquecimento).
5. **Grupos WhatsApp.** Arquiva `G# Ⓜ️ <cliente> + Miner` (DLT, Tallis, Lasso, Cacau, MGTC pendentes).
6. **Revoga acessos** Meta BM, GA4, CRM, e-commerce, e libera a capacity do owner.
7. **Marca churn no vault:** `companies/<Cliente>.md` status "ex-cliente" e tira da carteira `clientes-ativos-jul2026`.

## Gotchas
- Org com conta `@minerbz.com.br` não desativa pelo endpoint: trate à parte.
- GRBS teve acesso combinado até 30/07: respeite a data de corte contratada, não desligue antes.
- Sodine pediu reunião pós-saída: é resposta de encerramento, não reativação.
- Registre o que ficou pendente no [[radar-bloqueios]] (crédito de mídia, última fatura).

## O que NÃO fazer
- NÃO hard-delete de org nem de dado: sempre soft-delete reversível.
- NÃO deletar projeto Asana nem grupo (arquiva).
- NÃO deixar cron ou anúncio do ex-cliente vivo: é dinheiro e dado vazando.
