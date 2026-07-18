---
name: crm-deploy
description: Use SEMPRE que for deployar produção do MinerCRM (subir mudança pro minercrm.vercel.app no ar). Dispara com "deploya o CRM", "sobe pra prod o minercrm", "manda pro ar a mudança do CRM", "por que a prod do CRM regrediu/voltou", "o parceiros sumiu da prod", "promove o deploy bom". Prod=main, multi-tenant no mesmo deploy, deploy storm multi-sessão. NÃO é deploy de portal ou site avulso ([[deploy-miner]]).
---

# crm-deploy: deploy de produção do MinerCRM

Prod do MinerCRM é multi-tenant no MESMO deploy (mexeu, mexeu em todo cliente). Várias sessões Claude deployam em paralelo e a prod "pisca". Esta skill é o caminho limpo pra subir sem clobber.

## Quando disparar
- "Deploya o CRM", "sobe pra prod", "a prod regrediu", "o parceiros sumiu", "promove o deploy bom".
- NÃO use pra portal/site genérico da Miner ([[deploy-miner]]).

## Como executar
1. **Prod = main**. Repo `~/dev/crms/crm-miner-prd` (github gustavocoutiinho/crm-miner.git, 100% da Miner). Pull/clone da última `origin/main` antes de mexer.
2. **Branch de feature** da main atual. `git config user.email gustavo@minerbz.com.br` (o gate de autor não-verificado dispara com `...@Mac-mini...`, não com o e-mail certo).
3. **Entra na main por PR verificado** no GitHub (push direto e self-merge na main são BLOQUEADOS pelo classificador).
4. **Deploy**: Vercel projeto `prj_m5Eb1Bl8gN5H3JFVIT4z5azvlh2C`, team `team_rVtvuPTQbNYetvBVAjLh2OL7`. ESCREVA `.vercel/project.json` com esses ids ANTES do 1º `vercel --prod` (senão a CLI cria projeto fantasma com o nome do diretório).
5. **Confirma no ar** em `minercrm.vercel.app` (é a URL real; os custom `crm.minerbz.com.br` etc. não apontam pro Vercel). Editar = deployar: só conta confirmado no ar.
6. **Regressão sem rebuild**: `vercel promote <deploymentId-bom> --yes` (repoint do alias, ~2s, reversível).

## Gotchas
- Vercel BLOQUEIA (state BLOCKED) commit "limpo" de autor não-verificado. Passam: merge de PR no GitHub OU `vercel --prod` de árvore SUJA (gitDirty).
- Clobber recorrente: clones divergentes deployando `vercel --prod` derrubam o trabalho um do outro (o Parceiros já sumiu 3x). Detecção: `curl -s -o /dev/null -w "%{http_code}" .../api/consignment/pieces` (404 = clobber).
- `npm install --legacy-peer-deps` (conflito peer `@modelcontextprotocol/sdk`); sem pnpm na máquina.
- iCloud corrompe refs (dup " 2"): trabalhe em clone fresco.

## O que NÃO fazer
- Não force-push na `main` durante o storm (apaga merge de outra sessão).
- Não deployar snapshot combinado de várias branches (regride o trabalho dos outros).
- Não esquecer o `.vercel/project.json` (cria projeto fantasma).
- Não dar por pronto sem confirmar a URL no ar, nem vazar no caminho ([[crm-guard]]).
