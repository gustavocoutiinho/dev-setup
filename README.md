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

## Pendências manuais (humano faz)

1. **Obsidian Sync**: abrir Obsidian, logar com `gustavo@minerbz.com.br`, ativar Sync, cofre remoto `miner`, pasta local `~/ObsidianVaults/miner` (FORA do iCloud).
2. **Claude Code**: confirmar instalação e login (`npm install -g @anthropic-ai/claude-code`).
3. **Supabase** (se for usar): `supabase login`.

## O que NÃO está coberto

- 5 repos sem GitHub remote no Mac mini (grbs-apresentacao, lesalis-proposta, miner-financeiro, miner-financeiro-cloud, miner-website). Esses ficam de fora até ganharem remote.
- Apps GUI (Obsidian, Cursor, Raycast, etc): instale manualmente ou via `brew install --cask`.

## Regra de ouro

GitHub é a "nuvem" do código. **Sempre `git pull` antes de mexer · sempre `git push` ao terminar.** Nunca colocar `.git` dentro de iCloud, Dropbox ou Google Drive (corrompe).
