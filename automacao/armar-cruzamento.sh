#!/usr/bin/env bash
# armar-cruzamento.sh — arma o agendamento diário do cruzar-dados no Mac mini.
# PRÉ-REQUISITO: o launchd roda `claude -p` headless, que precisa de um token de longa
# duração. Sem ele dá 401. Rode UMA vez, interativo:  claude setup-token
# (o cruzar-dados SOB DEMANDA funciona sem isso — é só pro 8h automático.)
# Desarmar: launchctl unload ~/Library/LaunchAgents/com.miner.cruzar-dados.plist
set -uo pipefail
NODE_BIN="$(ls -d "$HOME"/.nvm/versions/node/*/bin 2>/dev/null | tail -1)"

echo "==> Verificando se o claude -p autentica em headless..."
if ! PATH="$NODE_BIN:$PATH" claude -p "responda: ok" >/dev/null 2>&1; then
  echo "!! claude -p NÃO autentica (provável 401)."
  echo "   Rode primeiro (uma vez, interativo):  claude setup-token"
  echo "   Depois rode este script de novo pra armar o 8h/dia."
  echo "   Enquanto isso, o cruzamento SOB DEMANDA funciona: diga 'cruza os dados'."
  exit 1
fi
echo "   auth ok."

SRC="$HOME/dev/dev-setup/automacao/com.miner.cruzar-dados.plist"
DST="$HOME/Library/LaunchAgents/com.miner.cruzar-dados.plist"
chmod +x "$HOME/dev/dev-setup/automacao/cruzar-dados.sh"
mkdir -p "$HOME/Library/LaunchAgents"
cp "$SRC" "$DST"
launchctl unload "$DST" 2>/dev/null || true
launchctl load "$DST" && echo "✅ agendamento armado: cruzar-dados roda todo dia às 8h" || echo "!! falhou ao carregar o launchd"
echo "   log: ~/ObsidianVaults/miner/cruzamentos/launchd.log"
