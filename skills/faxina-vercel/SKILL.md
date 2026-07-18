---
name: faxina-vercel
description: Inventaria os projetos Vercel e os repos GitHub da Miner, identifica duplicados/mortos e aponta o canônico, fecha entregável de cliente exposto em *.vercel.app, normaliza slug e domínio (padrão `tipo-cliente` e `*.minerbz.com.br`), e sinaliza deploy sem repo ("GitHub é a nuvem do código"). Use SEMPRE que o Gustavo disser "faxina nos deploys", "consolida os projetos", "limpa a Vercel", "quantos projetos duplicados eu tenho", "qual é o canônico", "isso tá exposto", ou ao CRIAR um projeto novo (pra já nascer no padrão). NÃO deleta nada sozinho: prepara o plano e o Gustavo confirma cada delete (é irreversível).
---

# faxina-vercel — inventário, canônico e higiene de deploys

Hoje são ~56 projetos na Vercel (scope `gustavo-4410s-projects`) e ~46 repos no GitHub, com duplicados, mortos e entregável de cliente solto em `*.vercel.app`. Esta skill faz o retrato, decide o canônico e **prepara** a limpeza. Delete é irreversível: a skill nunca apaga sozinha, ela deixa o plano pronto pro Gustavo confirmar item a item.

## Quando disparar
- "faxina/consolidar/limpar deploys", "qual o canônico", "tem duplicado", "isso tá no ar exposto".
- Ao criar projeto novo: rodar a checagem de nome/domínio antes, pra já nascer no padrão.

## Como executar
1. **Inventário Vercel:**
   ```bash
   vercel projects ls --scope gustavo-4410s-projects
   vercel domains ls --scope gustavo-4410s-projects
   ```
   Pra um projeto suspeito: `vercel inspect <url> --scope gustavo-4410s-projects` e `vercel ls <projeto> --scope gustavo-4410s-projects` (últimos deploys, pra ver o que é morto).
2. **Inventário GitHub:**
   ```bash
   gh repo list --limit 100
   gh repo view <repo> --json name,pushedAt,isArchived,url
   ```
3. **Cruze projeto ↔ repo.** Pra cada projeto Vercel ache o repo de origem. Marque três estados: **canônico** (o que está no ar e é fonte da verdade), **duplicado** (mesma coisa em outro nome/repo), **órfão** (deploy sem repo no GitHub, ou repo sem deploy).
4. **Escolha o canônico** pela regra: está no domínio final (`*.minerbz.com.br`), tem repo em `~/dev` no padrão de nomes, e é o mais recentemente deployado/committado. Os demais viram "aposentar".
5. **Exposição de cliente.** Entregável de cliente em `*.vercel.app` sem gate/domínio próprio é achado prioritário. Anote pra fechar (domínio + auth). Se serve dado sem auth, é caso de `blindar-portal` junto.
6. **Normalize nomes e domínio.** Slug `tipo-cliente` (ex: `portal-accs`, `deck-barneys`), mesmo slug em GitHub/Vercel/`~/dev`, favicon Miner, domínio final `*.minerbz.com.br`. URL antiga continua viva (não quebrar link em uso).
7. **Deploy sem repo.** Todo projeto no ar tem que ter repo no GitHub. Se achar deploy sem origem, crie/publique o repo (nunca `.git` em iCloud/Drive) antes de qualquer limpeza.
8. **Entregue o plano, não o estrago.** Monte a tabela: projeto → estado → canônico/aposentar → ação. O comando de delete (`vercel remove <projeto> --scope gustavo-4410s-projects`) fica ESCRITO no plano, comentado, pra o Gustavo rodar/confirmar. Você não executa delete.

## Gotchas
- Deploy só do `index.html` num portal single-file quebra os `/api` (gotcha do ACCS). Ao consolidar, deploye o projeto inteiro, não um arquivo.
- Dois projetos podem apontar pro mesmo domínio; confira qual domínio está de fato resolvendo antes de aposentar o "duplicado".
- Repo arquivado no GitHub ainda pode ter deploy vivo. `isArchived: true` não quer dizer morto no ar.
- Aposentar não é deletar de cara: primeiro tire tráfego/domínio, confirme que ninguém usa, depois o Gustavo deleta.

## O que NÃO fazer
- NÃO rodar `vercel remove` nem apagar repo automaticamente. Delete é do Gustavo, por item.
- NÃO renomear/mover domínio que está em uso sem manter a URL antiga viva.
- NÃO decidir canônico "no olho": use no ar + repo no padrão + data mais recente.
- NÃO deixar deploy sem repo depois da faxina.
