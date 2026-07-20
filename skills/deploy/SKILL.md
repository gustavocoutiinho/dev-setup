---
name: deploy
description: Use SEMPRE que for subir qualquer coisa da Miner pro ar, apontar domínio ou deployar o CRM. Cobre deploy de portal/deck/site/app, apontamento de subdomínio *.minerbz.com.br (registro A 76.76.21.21) e deploy de produção do MinerCRM (multi-tenant, prod=main, deploy storm multi-sessão). Dispara com "sobe pro ar", "deploya isso", "põe no ar", "versiona no GitHub", "manda pra produção", "atualiza o que está no ar", "aponta o domínio", "configura o DNS", "cria o subdomínio x.minerbz.com.br", "põe no domínio da Miner", "deploya o CRM", "sobe a prod do minercrm", "a prod do CRM regrediu", "o parceiros sumiu da prod", "promove o deploy bom".
---

# deploy: subir pro ar, domínio e prod do MinerCRM no padrão

Deploy na Miner erra fácil e tem gotcha que já derrubou cliente no ar. Esta skill fixa o trilho dos três casos que mais aparecem: subir um projeto qualquer, apontar o subdomínio e deployar a produção do CRM. Regra-mãe: **editar = deployar**, nada conta até estar no ar e confirmado.

## Modos
- **deploy geral** (portal/deck/site/app): branch da última main, commit verificado, deploy da pasta certa, confirma no ar.
- **domínio** (`<slug>.minerbz.com.br`): registro A `76.76.21.21`, adiciona no projeto Vercel, espera SSL, mantém a URL antiga viva.
- **prod MinerCRM** (multi-tenant, prod=main): entra na main por PR verificado, `.vercel/project.json` certo, confirma em `minercrm.vercel.app`.

## Quando disparar
- "sobe/deploya/põe no ar", "versiona", "manda pra produção", "atualiza o publicado".
- "aponta o domínio", "cria o subdomínio X.minerbz.com.br", "configura o DNS", "põe no domínio da Miner".
- "deploya o CRM", "sobe pra prod o minercrm", "a prod regrediu", "o parceiros sumiu", "promove o deploy bom".

## Como executar
Comum aos três: **pull antes** (GitHub é a nuvem do código; branch da última `origin/main`, nunca desfaça o que já está no ar), **commit verificado** (a Vercel BLOQUEIA commit não-verificado), **confirma no ar** abrindo a URL de produção. CLI logada como `gustavocoutiinho`, team `gustavo-4410s-projects`.

**deploy geral:** deploya o projeto INTEIRO (não um arquivo solto). Se o projeto não tem remote, resolve isso primeiro ([[faxina-web]]): deploy sem repo é dívida. Se o deploy é só pra "atualizar um número" que está chumbado no código, o certo é deixar o dado vivo ([[conserta-web]]), não redeployar o snapshot.

**domínio:** slug `tipo-cliente` idêntico em GitHub/Vercel/`~/dev`. Registro A do subdomínio pra `76.76.21.21` (ou CNAME conforme o painel pedir), adiciona o domínio no projeto Vercel, aguarda o SSL provisionar, abre `https://<slug>.minerbz.com.br` e valida certificado + conteúdo. Se já havia URL divulgada, mantém viva (redirect se preciso), nunca quebra link que o cliente usa.

**prod MinerCRM:** repo `~/dev/crms/crm-miner-prd` (github gustavocoutiinho/crm-miner.git, 100% da Miner). Branch de feature da main atual; `git config user.email gustavo@minerbz.com.br` (o gate de autor dispara com `...@Mac-mini...`, não com o e-mail certo). Entra na main por PR verificado (push direto e self-merge na main são BLOQUEADOS pelo classificador). Vercel projeto `prj_m5Eb1Bl8gN5H3JFVIT4z5azvlh2C`, team `team_rVtvuPTQbNYetvBVAjLh2OL7`: ESCREVA `.vercel/project.json` com esses ids ANTES do 1º `vercel --prod` (senão a CLI cria projeto fantasma com o nome do diretório). Confirma em `minercrm.vercel.app` (é a URL real; os custom tipo `crm.minerbz.com.br` não apontam pro Vercel). Regressão sem rebuild: `vercel promote <deploymentId-bom> --yes` (repoint do alias, ~2s, reversível).

## Gotchas
- **Deploy só do `index.html` num portal com `/api` quebra TODAS as rotas** (caso portal-accs; a pasta é `~/Documents/Sistema - Aço /portal/`). Deploya a pasta inteira.
- Vercel recusa (state BLOCKED) commit "limpo" de autor não-verificado. Passam: merge de PR no GitHub OU `vercel --prod` de árvore SUJA (gitDirty).
- Clobber no CRM: clones divergentes deployando `vercel --prod` derrubam o trabalho um do outro (o Parceiros já sumiu 3x). Detecção: `curl -s -o /dev/null -w "%{http_code}" .../api/consignment/pieces` (404 = clobber).
- `npm install --legacy-peer-deps` no CRM (conflito peer `@modelcontextprotocol/sdk`; sem pnpm na máquina). iCloud corrompe refs (dup " 2"): trabalhe em clone fresco.
- Propagação de DNS + SSL leva minutos: não conclua o domínio antes do certificado válido. Trocar o domínio sem manter o antigo derruba links já compartilhados.

## O que NÃO fazer
- NÃO deployar de branch velha, arquivo isolado num projeto com backend, nem dar por pronto sem abrir a URL de produção.
- NÃO force-push na `main` do CRM durante o storm (apaga merge de outra sessão), nem deployar snapshot combinado de várias branches (regride o trabalho dos outros).
- NÃO esquecer o `.vercel/project.json` (cria projeto fantasma), nem vazar no caminho ([[crm]]).
- NÃO matar a URL antiga que o cliente já usa, nem fugir do padrão `*.minerbz.com.br` sem motivo.
