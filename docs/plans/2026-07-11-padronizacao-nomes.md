# Padronização de nomes Miner — Plano de execução

> **Para workers:** operação de infra (rename/mover/favicon/topics), não código com testes.
> Cada passo tem um comando exato + uma **verificação** (a "prova" no lugar do teste).
> Referência: `docs/convencao-nomes.md`.

**Goal:** aplicar o slug canônico `tipo-cliente` em GitHub + Vercel + `~/dev`, sem quebrar
nenhuma URL publicada, com favicon Miner e organização por pastas/topics.

**Estratégia:** Fase 0 (de-para, feito) → piloto `site-miner` → escala por tipo. O repo é a
fonte de verdade; a URL antiga sempre fica viva.

---

## Runbook por projeto (procedimento seguro)

Para cada projeto, na ordem:

1. **GitHub**
   - Se já tem repo: `gh repo rename <novo> -R gustavocoutiinho/<antigo>` (redirect automático).
   - Se não tem repo (site solto): `git init` + commit + `gh repo create <novo> --private --source . --push` (passa a versionar).
   - Topics: `gh repo edit gustavocoutiinho/<novo> --add-topic <tipo> --add-topic <cliente>`.
2. **Local:** mover pra `~/dev/<pasta-tipo>/<novo>` + `git remote set-url origin <nova-url>` (se tiver git). O `.vercel/project.json` viaja junto (projectId não muda, deploy segue).
3. **Vercel** (regra da URL viva):
   - Projeto com **domínio custom** (`*.minerbz.com.br`, `*.prls.com.br`): `vercel project rename <antigo> <novo>` — a URL pública não muda. ✅
   - Projeto **só `.vercel.app`**: **NÃO renomear** (mataria a URL). Mantém o nome na Vercel até ganhar domínio custom. O canônico vale no GitHub + `~/dev`.
4. **Favicon:** garantir o set oficial Miner no projeto (de `dev-setup/assets/favicon-miner/`).
5. **De-para:** marcar item como feito.

**Rollback:** rename de repo GitHub é reversível (`gh repo rename` de volta; o redirect
antigo continua). Mover pasta é reversível (`mv` de volta). Nada é destrutivo.

---

## Fila de execução (ordem por risco crescente)

1. **Piloto:** `site-miner` (interno, sem cliente) — valida o processo.
2. **Decks** (baixo risco, `.vercel.app`): só GitHub+local+favicon; Vercel intocada (URLs enviadas vivas).
3. **Apps internos** (`app-command-center`, `app-mineros`, `app-financeiro*`, `app-pim`).
4. **MCPs/bots** (`mcp-blip`, `mcp-whatsapp`, `bot-telegram`).
5. **Portais** (domínio custom, rename Vercel seguro): `portal-accs`, etc.
6. **CRMs** (produção de cliente, máximo cuidado): `crm-miner`, `crm-normatel`.
7. **Arquivar:** archived no GitHub + `~/dev/interno/arquivo/`.

Cada grupo é um checkpoint: executo, mostro, você confere, sigo.

---

## Task 1 — Piloto: `site-miner` (era `miner-website`)

Estado atual (verificado): site estático, **sem repo GitHub**, pasta `~/dev/miner-website`
(sem git), projeto Vercel `miner-website` → `miner-website-beta.vercel.app`. Favicons já
presentes.

- [ ] **1. Versionar no GitHub como `site-miner`** (hoje não é versionado — ganho real)

```bash
cd ~/dev/miner-website
printf 'node_modules/\n.DS_Store\n' > .gitignore
git init -q && git add -A && git -c user.email=gustavo@minerbz.com.br commit -q -m "Site institucional Miner (versionado como site-miner)"
gh repo create site-miner --private --source . --remote origin --push
```
Verificação: `gh repo view gustavocoutiinho/site-miner --json url` retorna a URL.

- [ ] **2. Topics no GitHub**

```bash
gh repo edit gustavocoutiinho/site-miner --add-topic site --add-topic miner
```
Verificação: `gh repo view gustavocoutiinho/site-miner --json repositoryTopics`.

- [ ] **3. Mover a pasta pra `~/dev/sites/site-miner`**

```bash
mkdir -p ~/dev/sites && mv ~/dev/miner-website ~/dev/sites/site-miner
```
Verificação: `ls ~/dev/sites/site-miner/.vercel/project.json` existe (deploy segue).

- [ ] **4. Favicon Miner oficial** — confirmar que `favicon.*` da pasta são a logo Miner
      (já estão lá desde jun/2026). Se sim, nada a fazer; senão, copiar de
      `festival-costume-gourmet/public/brand/`.

- [ ] **5. Vercel — manter URL antiga viva**

Projeto usa só `.vercel.app` (não enviado a cliente, mas regra vale): **não renomear**.
Fica `miner-website` na Vercel até definirmos o domínio custom do site (`site.minerbz.com.br`
ou a migração de `minerbz.com.br`). Nome canônico vale no GitHub + `~/dev`.
Verificação: `curl -sI https://miner-website-beta.vercel.app` responde 200 (URL intacta).

- [ ] **6. Fechar** — marcar `site-miner` como feito no de-para.

**Resultado esperado:** o site vira versionado (`site-miner` no GitHub), organizado
(`~/dev/sites/site-miner`), com topics, favicon Miner, e a URL de produção **inalterada**.
