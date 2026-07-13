#!/usr/bin/env bash
# armar-cruzamento.sh — arma (ou re-arma) o agendamento diário do cruzar-dados no Mac.
# Roda no Mac mini (onde vivem os MCPs, inclusive o WhatsApp local). Idempotente.
# Desarmar:  launchctl unload ~/Library/LaunchAgents/com.miner.cruzar-dados.plist
set -uo pipefail
SRC="$HOME/dev/dev-setup/automacao/com.miner.cruzar-dados.plist"
DST="$HOME/Library/LaunchAgents/com.miner.cruzar-dados.plist"
chmod +x "$HOME/dev/dev-setup/automacao/cruzar-dados.sh"
mkdir -p "$HOME/Library/LaunchAgents"
cp "$SRC" "$DST"
launchctl unload "$DST" 2>/dev/null || true
launchctl load "$DST" && echo "✅ agendamento armado: cruzar-dados roda todo dia às 8h" || echo "!! falhou ao carregar o launchd"
echo "   log: ~/ObsidianVaults/miner/cruzamentos/launchd.log"
echo "   desarmar: launchctl unload $DST"
