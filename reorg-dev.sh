#!/usr/bin/env bash
set -uo pipefail
#
# reorg-dev.sh — organiza ~/dev em subpastas por tipo conforme a convenção tipo-cliente.
# Pra cada repo git em ~/dev, descobre o nome canônico ATUAL via GitHub (segue o redirect
# do rename), move a pasta pra ~/dev/<tipo>/<canonico> e atualiza o git remote.
# Idempotente · preserva working tree sujo (usa mv, não commita nada) · roda em qualquer Mac.
# Requer gh autenticado. Ref: docs/convencao-nomes.md
#
DEV="$HOME/dev"
OWNER="gustavocoutiinho"

command -v gh >/dev/null 2>&1 || { echo "!! gh não instalado — rode bootstrap-macbook.sh antes"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "!! gh não autenticado — rode: gh auth login"; exit 1; }

tipo_de() {
  case "$1" in
    site-*)   echo sites   ;; deck-*)  echo decks  ;; crm-*)    echo crms    ;;
    portal-*) echo portais ;; app-*)   echo apps   ;; mcp-*)    echo mcps    ;;
    bot-*)    echo bots     ;; *)       echo ""     ;;
  esac
}

echo "==> Reorganizando $DEV por tipo (canônico via GitHub)..."
moved=0; skipped=0
for dir in "$DEV"/*/; do
  dir="${dir%/}"
  [ -d "$dir/.git" ] || continue                      # só repos git no nível raiz
  name="$(basename "$dir")"
  url="$(git -C "$dir" remote get-url origin 2>/dev/null)" || continue
  case "$url" in *"$OWNER"/*) ;; *) continue ;; esac   # só repos da conta
  repo="$(basename "$url" .git)"
  canon="$(gh api "repos/$OWNER/$repo" --jq .name 2>/dev/null)"   # segue o redirect
  [ -z "$canon" ] && canon="$repo"
  tipo="$(tipo_de "$canon")"
  [ -z "$tipo" ] && { skipped=$((skipped+1)); continue; }   # sem prefixo de tipo: não mexo
  dest="$DEV/$tipo/$canon"
  [ "$dir" = "$dest" ] && continue                    # já no lugar
  if [ -e "$dest" ]; then echo "  ~ $name -> $tipo/$canon (destino já existe, pulo)"; continue; fi
  mkdir -p "$DEV/$tipo"
  mv "$dir" "$dest"
  git -C "$dest" remote set-url origin "https://github.com/$OWNER/$canon.git"
  echo "  + $name -> $tipo/$canon"
  moved=$((moved+1))
done
echo "==> $moved movida(s), $skipped sem tipo (mantidas na raiz). Fonte da verdade: dev-setup/docs/convencao-nomes.md"
