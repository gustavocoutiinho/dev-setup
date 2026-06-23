#!/usr/bin/env bash
# Bootstrap do MacBook do Gustavo
# Replica o setup do Mac mini: Homebrew, CLIs, git config, 13 repos em ~/dev, symlink memória Claude.
# Idempotente: pode rodar várias vezes. Assume username gustavocoutinho.

set -euo pipefail

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; BLUE='\033[0;34m'; NC='\033[0m'
say()  { printf "${BLUE}→${NC} %s\n" "$*"; }
ok()   { printf "${GREEN}✓${NC} %s\n" "$*"; }
warn() { printf "${YELLOW}!${NC} %s\n" "$*"; }
fail() { printf "${RED}✗${NC} %s\n" "$*"; }

if [ "$(whoami)" != "gustavocoutinho" ]; then
  warn "username atual é '$(whoami)' (esperado: gustavocoutinho). Continua mesmo assim."
fi

# ============================================================
# 1. Homebrew
# ============================================================
if ! command -v brew >/dev/null 2>&1; then
  say "instalando Homebrew..."
  NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  if [ -d /opt/homebrew ]; then
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> "$HOME/.zprofile"
    eval "$(/opt/homebrew/bin/brew shellenv)"
  fi
fi
ok "Homebrew $(brew --version | head -1 | awk '{print $2}')"

# ============================================================
# 2. CLIs essenciais
# ============================================================
say "verificando CLIs (gh, jq, nvm)..."
for pkg in gh jq nvm; do
  if brew list "$pkg" >/dev/null 2>&1; then
    ok "$pkg já instalado"
  else
    say "instalando $pkg..."
    brew install "$pkg"
  fi
done

# ============================================================
# 3. nvm + Node 22 + pnpm + vercel + supabase
# ============================================================
export NVM_DIR="$HOME/.nvm"
mkdir -p "$NVM_DIR"
NVM_SH="$(brew --prefix)/opt/nvm/nvm.sh"
# shellcheck disable=SC1090
[ -s "$NVM_SH" ] && . "$NVM_SH"

# adiciona nvm ao ~/.zshrc se ainda não estiver
if ! grep -q "NVM_DIR" "$HOME/.zshrc" 2>/dev/null; then
  cat >> "$HOME/.zshrc" <<'EOF'

# nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$(brew --prefix)/opt/nvm/nvm.sh" ] && . "$(brew --prefix)/opt/nvm/nvm.sh"
[ -s "$(brew --prefix)/opt/nvm/etc/bash_completion.d/nvm" ] && . "$(brew --prefix)/opt/nvm/etc/bash_completion.d/nvm"
EOF
  ok "nvm adicionado ao ~/.zshrc"
fi

if ! nvm ls 22 >/dev/null 2>&1; then
  say "instalando Node 22.22.1..."
  nvm install 22.22.1
  nvm alias default 22.22.1
fi
nvm use 22.22.1 >/dev/null
ok "Node $(node --version) / npm $(npm --version)"

say "instalando vercel, pnpm, supabase via npm global..."
npm install -g vercel@latest pnpm@latest supabase@latest 2>&1 | tail -3 || true
ok "vercel $(vercel --version 2>/dev/null | head -1) / pnpm $(pnpm --version) / supabase $(supabase --version 2>/dev/null | head -1)"

# ============================================================
# 4. Git config global (identidade Miner)
# ============================================================
say "configurando git global..."
git config --global user.email "gustavo@minerbz.com.br"
git config --global user.name "Gustavo Coutinho"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global push.autoSetupRemote true
ok "git: $(git config --global user.email) / $(git config --global user.name)"

# ============================================================
# 5. Logins (interativos)
# ============================================================
if gh auth status >/dev/null 2>&1; then
  ok "gh já autenticado ($(gh api user --jq .login 2>/dev/null))"
else
  warn "gh precisa de login. Abrindo browser..."
  gh auth login --hostname github.com --web --git-protocol https
fi

if vercel whoami >/dev/null 2>&1; then
  ok "vercel já autenticado ($(vercel whoami 2>/dev/null))"
else
  warn "vercel precisa de login. Abrindo browser..."
  vercel login
fi

# ============================================================
# 6. ~/dev + clonar/atualizar repos
# ============================================================
mkdir -p "$HOME/dev"
say "preparando ~/dev (clone/pull dos 13 repos)..."

# Formato: pasta_local|url-https
REPOS=(
  "antigrativity|https://github.com/gustavocoutiinho/antigrativity.git"
  "crm-miner|https://github.com/gustavocoutiinho/crmminer.git"
  "dashboard-financeiro|https://github.com/gustavocoutiinho/dashboard-financeiro.git"
  "festival-costume-gourmet|https://github.com/gustavocoutiinho/festival-costume-gourmet.git"
  "mig1|https://github.com/gustavocoutiinho/mig1.git"
  "minercrm|https://github.com/gustavocoutiinho/minercrm.git"
  "mineros|https://github.com/gustavocoutiinho/mineros.git"
  "next-shadcn-admin-dashboard|https://github.com/gustavocoutiinho/miner-portal.git"
  "normatel-portal-unified|https://github.com/gustavocoutiinho/normatel-portal.git"
  "normatel-premium|https://github.com/gustavocoutiinho/normatel-premium.git"
  "porao|https://github.com/gustavocoutiinho/porao.git"
  "portal-accs|https://github.com/gustavocoutiinho/portal-accs.git"
  "postiz-local|https://github.com/gitroomhq/postiz-docker-compose.git"
)

for entry in "${REPOS[@]}"; do
  name="${entry%%|*}"
  url="${entry##*|}"
  target="$HOME/dev/$name"
  if [ -d "$target/.git" ]; then
    say "$name: já existe, fetch + pull..."
    git -C "$target" fetch origin --quiet 2>&1 || warn "  fetch falhou em $name"
    branch=$(git -C "$target" rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)
    git -C "$target" pull --rebase --quiet 2>&1 || warn "  pull com conflito em $name ($branch) — resolver manualmente"
    ok "  $name pronto"
  else
    say "$name: clonando..."
    if git clone --quiet "$url" "$target" 2>&1; then
      ok "  $name clonado"
    else
      fail "  $name falhou (repo privado? URL mudou?)"
    fi
  fi
done

# ============================================================
# 7. Symlink: memória do Claude → vault Obsidian
# ============================================================
VAULT="$HOME/ObsidianVaults/miner"
MEM_LINK="$HOME/.claude/projects/-Users-gustavocoutinho-Documents-Claude/memory"
if [ -d "$VAULT/memory" ]; then
  if [ -L "$MEM_LINK" ]; then
    ok "symlink memória → vault já existe"
  else
    mkdir -p "$(dirname "$MEM_LINK")"
    if [ -e "$MEM_LINK" ]; then
      backup="$MEM_LINK.local-backup-$(date +%Y-%m-%d)"
      mv "$MEM_LINK" "$backup"
      warn "memória local antiga movida pra $backup"
    fi
    ln -s "$VAULT/memory" "$MEM_LINK"
    ok "symlink memória criado ($MEM_LINK → $VAULT/memory)"
  fi
else
  warn "vault Obsidian ainda não está em $VAULT — pulando symlink"
  warn "  (depois de ativar Obsidian Sync, rode este script de novo pra criar o symlink)"
fi

# ============================================================
# Resumo final + pendências manuais
# ============================================================
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  ✓ BOOTSTRAP COMPLETO"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "JÁ FEITO:"
echo "  • Homebrew, gh, jq, nvm, Node 22, pnpm, vercel, supabase"
echo "  • Git config global (gustavo@minerbz.com.br)"
echo "  • gh + vercel autenticados"
echo "  • 13 repos clonados/atualizados em ~/dev/"
[ -L "$MEM_LINK" ] && echo "  • Memória do Claude → vault Obsidian (symlink)"
echo ""
echo "PENDÊNCIAS MANUAIS (você precisa fazer):"
echo ""
echo "1. OBSIDIAN SYNC"
echo "   • Abrir Obsidian, fazer login com gustavo@minerbz.com.br"
echo "   • Ativar Obsidian Sync, cofre remoto 'miner'"
echo "   • Pasta local: ~/ObsidianVaults/miner (FORA do iCloud)"
echo "   • Se vault no MacBook ainda está no iCloud, mover ANTES de ativar sync"
echo "     (rodar este script de novo depois pra criar o symlink da memória)"
echo ""
echo "2. REPOS SEM REMOTE GITHUB (não foram clonados, não tinha remote no Mac mini):"
echo "   • grbs-apresentacao, lesalis-proposta"
echo "   • miner-financeiro, miner-financeiro-cloud, miner-website"
echo "   Se precisar deles, crie remote no GitHub e atualize este script."
echo ""
echo "3. SUPABASE (opcional, se for usar): supabase login"
echo ""
echo "4. CLAUDE CODE: confirme que está instalado e logado no MacBook"
echo "   (npm install -g @anthropic-ai/claude-code, depois claude)"
echo ""
echo "Regra de ouro: SEMPRE 'git pull' antes de mexer · SEMPRE 'git push' ao terminar."
echo "═══════════════════════════════════════════════════════════"
