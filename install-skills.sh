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

# 3) settings.json: permissão de ler/escrever no vault Obsidian (idempotente, "sempre atualizar o Obsidian")
VAULT="$HOME/ObsidianVaults/miner"
if command -v jq >/dev/null 2>&1 && [ -f "$SETTINGS" ]; then
  tmp="$(mktemp)"
  if jq --arg v "$VAULT" '
      .permissions.allow = (((.permissions.allow // []) + ["Read(\($v)/**)","Edit(\($v)/**)","Write(\($v)/**)"]) | unique)
      | .permissions.additionalDirectories = (((.permissions.additionalDirectories // []) + [$v]) | unique)
    ' "$SETTINGS" > "$tmp" 2>/dev/null; then
    mv "$tmp" "$SETTINGS"; echo "==> settings.json: permissão de escrita no vault Obsidian"
  else
    rm -f "$tmp"; echo "!! não consegui setar permissão do vault (settings.json)"
  fi
fi

# --- Plugins de marketplace do Claude Code (merge idempotente no settings.json) ---
MANIFEST="$DIR/plugins.json"
if [ -f "$MANIFEST" ] && command -v python3 >/dev/null 2>&1; then
  python3 - "$SETTINGS" "$MANIFEST" <<'PY'
import json, os, sys
settings_path, manifest_path = sys.argv[1], sys.argv[2]
manifest = json.load(open(manifest_path))
settings = {}
if os.path.exists(settings_path):
    try: settings = json.load(open(settings_path))
    except Exception: settings = {}
ep = settings.setdefault("enabledPlugins", {})
for k, v in manifest.get("enabledPlugins", {}).items(): ep[k] = v
mk = settings.setdefault("extraKnownMarketplaces", {})
for k, v in manifest.get("extraKnownMarketplaces", {}).items(): mk[k] = v
os.makedirs(os.path.dirname(settings_path), exist_ok=True)
json.dump(settings, open(settings_path, "w"), indent=2, ensure_ascii=False)
print(f"==> plugins: {len(ep)} habilitados, {len(mk)} marketplaces (reinicie o Claude Code p/ baixar)")
PY
else
  echo "!! plugins.json ausente ou sem python3: plugins de marketplace nao aplicados"
fi

echo "==> Pronto. Skills em $DEST:"
ls "$DEST"
