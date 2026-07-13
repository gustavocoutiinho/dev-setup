#!/usr/bin/env bash
# Hook SessionStart: na 1a sessao do dia, pede pro Claude rodar o cruzar-dados em
# BACKGROUND (na sessao interativa do Gustavo, que autentica normal — contorna o 401
# do headless via launchd). Idempotente: so dispara 1x por dia. additionalContext em
# ASCII de proposito (evita problema de encoding no shell do hook).
STAMP="$HOME/.claude/.cruzamento-ultima-data"
HOJE="$(date +%Y-%m-%d)"
[ "$(cat "$STAMP" 2>/dev/null)" = "$HOJE" ] && exit 0
echo "$HOJE" > "$STAMP"
cat <<JSON
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"CRUZAMENTO DIARIO (1a sessao de ${HOJE}): dispare a skill cruzar-dados AGORA em BACKGROUND (subagente com run_in_background) para atualizar o retrato dos clientes ativos no vault, sem bloquear nem atrasar o Gustavo. Nao narre o processo nem espere terminar; siga atendendo o que ele pedir. Se ele perguntar, diga que o cruzamento do dia esta rodando em background. Somente leitura das ferramentas; nunca enviar mensagem."}}
JSON
