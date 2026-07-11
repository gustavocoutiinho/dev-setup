# dev-setup

Setup do ambiente do Gustavo (Mac mini + MacBook + qualquer Mac novo). Mantém o "3 casas":

- **Código** → GitHub, cópia de trabalho em `~/dev/` (fora de iCloud)
- **Conhecimento + memória do Claude** → vault Obsidian em `~/ObsidianVaults/miner` (Obsidian Sync)
- **Docs / planilhas / PDFs** → Google Drive (gustavo@minerbz.com.br)

## Bootstrap de um Mac novo

No terminal do Mac novo, **1 comando**:

```bash
curl -fsSL https://raw.githubusercontent.com/gustavocoutiinho/dev-setup/main/bootstrap-macbook.sh | bash
```

O script faz:

1. Instala Homebrew (se faltar)
2. Instala `gh`, `jq`, `nvm`
3. Instala Node 22 + `pnpm`, `vercel`, `supabase`
4. Configura git global: `gustavo@minerbz.com.br`, rebase em pull, autosetup de remote em push
5. Faz `gh auth login` e `vercel login` (browser abre, você loga)
6. Clona/atualiza 13 repos em `~/dev/`:
   - antigrativity, crm-miner, dashboard-financeiro, festival-costume-gourmet, mig1, minercrm, mineros, next-shadcn-admin-dashboard, normatel-portal-unified, normatel-premium, porao, portal-accs, postiz-local
7. Cria symlink `~/.claude/projects/.../memory` → `~/ObsidianVaults/miner/memory/` (se o vault já estiver no lugar)

Idempotente: pode rodar quantas vezes quiser. Em repos já clonados faz `git fetch + pull --rebase`.

## Skills + plugins do Claude Code

Depois do bootstrap (ou a qualquer momento), sincronize skills e plugins entre os Macs:

```bash
cd ~/dev/dev-setup && git pull && ./install-skills.sh
```

O `install-skills.sh` (idempotente) instala:

- **11 skills custom** de `skills/` → `~/.claude/skills/` (adkit, google-ads-strategy, meta-ads-analyzer, meta-ads-strategy, miner-context, minerdesign, obsidianminer, relatorio-accs, sf-apex-development, sf-cli-deployment, sf-lwc-development) e remove as fundidas antigas (cerebro-miner, vault-context).
- **CLAUDE.md global** + `language = português brasileiro` no `~/.claude/settings.json`.
- **17 plugins de marketplace + 7 marketplaces** (de `plugins.json`), via merge que **preserva** o que a máquina já tem. Reinicie o Claude Code depois pra baixar os plugins.

> Ganhou uma skill nova numa máquina? Copie pra `skills/`, `git add -A && git commit && git push`, e na outra `git pull && ./install-skills.sh`. Os **connectors da conta** (Notion, Asana, Gmail, etc.) não entram aqui: sincronizam sozinhos pelo login `claude.ai`.

## Organizar o ~/dev por tipo (convenção de nomes)

```bash
cd ~/dev/dev-setup && git pull && ./reorg-dev.sh
```

`reorg-dev.sh` (idempotente) descobre o nome canônico de cada repo em `~/dev` pelo próprio
GitHub (segue o redirect do rename), move a pasta pra `~/dev/<tipo>/<nome>` (`sites/ decks/
crms/ portais/ apps/ mcps/ bots/`) e atualiza o `git remote`. Não commita nada, preserva
trabalho não salvo. A convenção completa (formato `tipo-cliente`, de-para, regras de URL e
favicon) está em `docs/convencao-nomes.md`.

**Setup completo de um Mac (ex: MacBook):**
```bash
cd ~/dev/dev-setup && git pull && ./install-skills.sh && ./reorg-dev.sh
```

## Pendências manuais (humano faz)

1. **Obsidian Sync**: abrir Obsidian, logar com `gustavo@minerbz.com.br`, ativar Sync, cofre remoto `miner`, pasta local `~/ObsidianVaults/miner` (FORA do iCloud).
2. **Claude Code**: confirmar instalação e login (`npm install -g @anthropic-ai/claude-code`).
3. **Supabase** (se for usar): `supabase login`.

## O que NÃO está coberto

- 5 repos sem GitHub remote no Mac mini (grbs-apresentacao, lesalis-proposta, miner-financeiro, miner-financeiro-cloud, miner-website). Esses ficam de fora até ganharem remote.
- Apps GUI (Obsidian, Cursor, Raycast, etc): instale manualmente ou via `brew install --cask`.

## Regra de ouro

GitHub é a "nuvem" do código. **Sempre `git pull` antes de mexer · sempre `git push` ao terminar.** Nunca colocar `.git` dentro de iCloud, Dropbox ou Google Drive (corrompe).
