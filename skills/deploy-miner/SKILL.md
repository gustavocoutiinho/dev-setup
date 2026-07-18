---
name: deploy-miner
description: Use SEMPRE que for subir qualquer coisa da Miner pro ar (portal, deck, site, app, CRM) ou versionar código. Dispara com "sobe pro ar", "deploya isso", "põe no ar", "versiona no GitHub", "manda pra produção", "atualiza o que está no ar". Guarda o checklist de deploy da casa e evita os erros que já quebraram cliente no ar.
---

# deploy-miner: checklist de deploy padrão Miner

Deploy na Miner erra fácil e tem gotcha que já derrubou cliente. Esta skill fixa o passo a passo: branch certo, commit verificado, deploy da pasta certa, confirma no ar. Editar = deployar: nada conta até estar no ar e confirmado.

## Quando disparar
- "sobe/deploya/põe no ar", "versiona", "manda pra produção", "atualiza o que está publicado".

## Como executar
1. **Pull antes.** GitHub é a nuvem do código: branch da última `origin/main`, nunca desfazer o que já está no ar.
2. **Commit verificado.** A Vercel BLOQUEIA deploy de commit não-verificado. Garanta a verificação antes de empurrar.
3. **Deploy da pasta certa.** Vercel CLI logado como `gustavocoutiinho`, team `gustavo-4410s-projects`. Deploya o projeto inteiro, não um arquivo solto.
4. **Confirma no ar.** Abre a URL de produção e confirma que respondeu e bate com o esperado. Sem isso, não está pronto.
5. **Repo em dia.** Se o projeto não tem remote, resolve isso ([[faxina-vercel]]): deploy sem repo é dívida.

## Gotchas
- **Deploy só do `index.html` num portal com `/api` quebra TODAS as rotas** (caso portal-accs). Deploya a pasta inteira, de `~/Documents/Sistema - Aço /portal/` no caso do ACCS.
- Commit não-verificado passa local mas a Vercel recusa: cheque antes de perder tempo.
- Dois deploys do mesmo projeto de pastas diferentes já aconteceu: confirme qual é o source canônico.

## O que NÃO fazer
- NÃO deployar de branch velha nem sobrescrever o que está no ar sem checar.
- NÃO dar por pronto sem abrir a URL de produção.
- NÃO deployar arquivo isolado num projeto com backend.
