#!/usr/bin/env bash
# cruzar-dados.sh — roda o Claude Code headless 1x/dia pra cruzar as ferramentas
# conectadas (Asana, Meta Ads, WhatsApp…) e atualizar o retrato de cada cliente no
# vault Obsidian. Chamado pelo launchd com.miner.cruzar-dados. Ver skill `cruzar-dados`.
set -uo pipefail

# launchd não herda o PATH do shell interativo — resolve o node/claude na mão.
NODE_BIN="$(ls -d "$HOME"/.nvm/versions/node/*/bin 2>/dev/null | tail -1)"
export PATH="/opt/homebrew/bin:/usr/local/bin:${NODE_BIN}:$PATH"
CLAUDE="$(command -v claude || echo "$NODE_BIN/claude")"

LOGDIR="$HOME/ObsidianVaults/miner/cruzamentos"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/launchd.log"

{
  echo "════════ $(date '+%Y-%m-%d %H:%M') — cruzamento diário ════════"
  if [ ! -x "$CLAUDE" ]; then echo "!! claude não encontrado ($CLAUDE) — abortando"; exit 1; fi
  cd "$HOME/Documents/Claude" 2>/dev/null || cd "$HOME"
  "$CLAUDE" -p "Rode a skill cruzar-dados agora: leia os clientes ativos, puxe o que estiver conectado (Asana, Meta Ads, WhatsApp e outros MCPs), atualize o bloco 'Retrato — hoje' de cada cliente ativo no vault Obsidian, e registre em cruzamentos/log.md o que funcionou e o que caiu por falta de auth. Não invente dado de ferramenta que não respondeu." 2>&1
  echo "════════ $(date '+%H:%M') — fim ════════"
} >> "$LOG" 2>&1
