---
name: monitor-custo
description: Use SEMPRE que precisar saber quanto os sistemas estão gastando ou se tem desperdício sangrando (chave OpenRouter perto do teto, projeto Vercel morto, automação de ex-cliente ainda rodando). Soma o gasto de MCPs/Vercel/Supabase/OpenRouter e avisa o que dispara, incluindo robô de quem já saiu (o cron do MGTC, ex-cliente, roda toda segunda). Dispara com "quanto tá gastando", "tem desperdício?", "a chave de IA tá acabando?", "custo dos sistemas", "algum robô de ex-cliente rodando?", "vigia o gasto", "onde tá sangrando dinheiro".
---

# monitor-custo: vigia o gasto e caça desperdício

Ninguém olha o gasto dos sistemas até estourar. A chave OpenRouter tem **teto de $5** (4 chaves, conta `gustavo@minerbz.com.br`, $10 de crédito) e o produto para de responder quando bate o limite; são **35 projetos Vercel**; e há robô de **ex-cliente ainda queimando recurso** (o cron `miner-weekly-report-mgtc` roda toda segunda pro MGTC, que **saiu**). Esta skill soma o custo e avisa o que dispara. Ela sinaliza, não paga nem desliga sozinha.

## Quando disparar
- Rotina de custo (mensal/semanal) ou "quanto tá gastando / tem desperdício?".
- Chave de IA perto do teto, projeto Vercel suspeito de morto, cron de cliente que churnou.
- Gustavo pediu vigilância de gasto ou "onde tá sangrando".

## Como executar
1. **OpenRouter:** Activity/Logs por chave; alerte a que se aproxima do teto de $5 (senão o produto que a usa cai). Nada de dado de cliente em modelo free.
2. **Vercel (35 projetos):** cruze com [[faxina-vercel]] pra achar deploy morto/duplicado que ainda conta.
3. **Supabase MinerOS/MinerCRM:** olho em edge functions e crons de alta frequência (ex `*/15`), que multiplicam invocação.
4. **Automação de ex-cliente:** liste crons/robôs e cruze com a carteira ativa. Hoje o `miner-weekly-report-mgtc` roda pra MGTC, **ex-cliente**, candidato a desligar ([[cliente-fora]] conduz o offboarding).
5. **Mídia (contexto, não caixa Miner):** o Windsor agrega ~R$137k/mês de mídia dos clientes; vigie **variação** brusca, não o valor absoluto (é verba do cliente, não custo da Miner).
6. **Avise** o gasto anômalo/desperdício (Slack/WhatsApp/daily-brief) e registre no vault.

## Gotchas
- **Teto de $5 por chave:** estourou, o produto que depende dela para; avise antes, não depois.
- **Cron de ex-cliente = custo puro:** mas confirme que o cliente saiu ([[cliente-fora]]) antes de propor matar; MGTC está confirmado como churn.
- **R$137k é mídia do cliente**, não caixa da Miner: só a variação importa, não confunda com custo interno.

## O que NÃO fazer
- NÃO comprar crédito, assinar plano nem mexer em pagamento: é do Gustavo.
- NÃO desligar cron/projeto sem confirmar que é ex-cliente/morto.
- NÃO expor chave nem colocar dado sensível em modelo free ([[guarda-ia]] cuida da cota por usuário).
