#!/usr/bin/env bash
# Instala/atualiza as skills pessoais do Claude Code a partir deste repo (dev-setup).
# Roda em qualquer Mac do Gustavo (mini ou MacBook). Idempotente.
# Uso:  cd ~/dev/dev-setup && git pull && ./install-skills.sh
set -uo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$DIR/skills"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"

echo "==> Instalando skills de $SRC -> $DEST"
for s in "$SRC"/*/; do
  [ -d "$s" ] || continue
  name="$(basename "$s")"
  rm -rf "$DEST/$name"
  cp -R "$s" "$DEST/$name"
  find "$DEST/$name" -name "*.sh" -exec chmod +x {} \;
  echo "  + $name"
done

# Skills antigas que foram FUNDIDAS na obsidianminer: remover pra não duplicar.
for old in cerebro-miner vault-context; do
  if [ -d "$DEST/$old" ]; then rm -rf "$DEST/$old"; echo "  - removida (fundida): $old"; fi
done

echo "==> Pronto. Skills em $DEST:"
ls "$DEST"
