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

# --- Config global do Claude Code: idioma PT-BR (aqui e no MacBook) ---
CLAUDE_DIR="$HOME/.claude"
mkdir -p "$CLAUDE_DIR"

# 1) CLAUDE.md global (regras de idioma + escrita)
if [ -f "$DIR/claude/CLAUDE.md" ]; then
  cp "$DIR/claude/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
  echo "==> CLAUDE.md global instalado em $CLAUDE_DIR/CLAUDE.md"
fi

# 2) settings.json: garantir language = português brasileiro (idempotente, preserva o resto)
SETTINGS="$CLAUDE_DIR/settings.json"
if command -v jq >/dev/null 2>&1; then
  if [ -f "$SETTINGS" ]; then
    tmp="$(mktemp)"
    if jq '.language = "português brasileiro"' "$SETTINGS" > "$tmp" 2>/dev/null; then
      mv "$tmp" "$SETTINGS"; echo "==> settings.json: language = português brasileiro"
    else
      rm -f "$tmp"; echo "!! settings.json inválido, não mexi (ajuste manual)"
    fi
  else
    printf '{\n  "language": "português brasileiro"\n}\n' > "$SETTINGS"
    echo "==> settings.json criado com language = português brasileiro"
  fi
else
  echo "!! jq não encontrado: adicione \"language\": \"português brasileiro\" manualmente em $SETTINGS"
fi

echo "==> Pronto. Skills em $DEST:"
ls "$DEST"
