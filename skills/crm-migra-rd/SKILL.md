---
name: crm-migra-rd
description: Use SEMPRE que for migrar um funil do RD Station CRM pro MinerCRM (tirar cliente da RD e deixar no CRM próprio, como a Stalker). Dispara com "migra a <cliente> da RD pro CRM", "tira tudo da RD", "traz o funil do RD Station", "importa os deals da RD", "sincroniza RD → MinerCRM", "o CRM tá com menos deals que o RD". Motor stalker_* e edge de sync. NÃO é criar a org do zero ([[crm-org]]).
---

# crm-migra-rd: RD Station → MinerCRM sem perder campo

A Stalker saiu de RD+Make+Suri pro MinerCRM. A migração roda por um motor próprio (`stalker_*`) que traz o deal inteiro do RD, não só o nome. Esta skill repete isso pra outro cliente (Maresia tem arquitetura idêntica `maresia_*`), no Supabase minercrm `stpstwsqtuubpxvvexte`.

## Quando disparar
- "Migra o <cliente> da RD", "traz o funil do RD Station", "o CRM tá com menos deals que o RD".
- NÃO use pra criar a org antes de existir (aí é [[crm-org]]).

## Como executar
1. **Credenciais RD**: token da conta + pipeline id + responsável RD. Ex Stalker: token `68ed0b11e131910020b18ed5`, pipeline Franquias Stalker `68ef8dfb75222800145ef320` (a mesma conta RD serve o pipeline Atacado Maresia).
2. **Motor**: edge `stalker-rd-sync` → função `stalker_load_rd_batch` grava `deals` + `contacts`. Crons a cada 15 min (`?key=stkr_sync_7f3a9c2e`).
3. **Traz TODOS os campos**: motivo de perda, fonte, valor, produto, datas, `is_lost`/`win` real. Casa RD↔CRM por `deals.external_id` = id do deal no RD, e o contato por **telefone E.164**. Ordem de grandeza de uma corrida: ~629 deals + 276 contatos completos.
4. **Régua `<cliente>_apply_eligibility`**: projeta `raw_meta` → `contacts.status`/`stage` no formato que o front lê (INACTIVE pra perdido/ganho/fora do foco geográfico).
5. **Confere a dimensão**: deals no pipeline RD × deals que entraram (o CRM já ficou com só ~56% da base uma vez). Reprocessa a edge se faltar.

## Gotchas
- Perda no RD = flag `win=false` + motivo, NÃO a etapa "Base Perdida". O `stalker_load_rd_batch` antigo marcava `is_lost` só pela etapa e deixava perdido como aberto. Corrija por `win` real.
- Correção por UPDATE direto em `contacts` é REVERTIDA pelo cron em ≤15 min: mexa no motor (função + eligibility), nunca em dados.
- O front genérico NÃO lê `raw_meta`, usa `contacts.status`/`stage`; a eligibility traduz.
- Motivo real de perda costuma ser follow-up/comunicação (~55%), não capital: não rotule "capital alto" como perda dominante.

## O que NÃO fazer
- Não sanear dado na mão (o cron desfaz): mexa no motor.
- Não copiar-colar a régua da Stalker pra outro cliente (Stalker CE/PI/PB/MA/RN; Maresia nacional; Hidrotintas BA/PA/SE/MA).
- Não mexer em `stalker_*` achando que afeta a Maresia (`maresia_*` é separado), e vice-versa.
- Base que não vem do RD entra por [[ingere-base]], não por aqui.
