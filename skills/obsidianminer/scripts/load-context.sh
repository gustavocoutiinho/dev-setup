#!/usr/bin/env bash
# Carrega a espinha dorsal do vault Obsidian "miner" (retrato operacional completo
# do Gustavo / MinerBZ). Chamado pela skill obsidianminer (modo total). NÃO dumpa as
# 487 notas: carrega os MOCs/Mundos (que resumem tudo) + os índices pra cavar o detalhe.
set -uo pipefail
shopt -s nullglob
V="$HOME/ObsidianVaults/miner"
[ -d "$V" ] || { echo "ERRO: vault não encontrado em $V"; exit 1; }

sep() { printf '\n\n================ %s ================\n' "$1"; }

echo "OBSIDIANMINER — backbone do vault Obsidian"
echo "Fonte: $V (487 notas, ~318k palavras). Abaixo: resumo operacional + índices."
echo "Para detalhe de um cliente/pessoa/projeto, LEIA a nota específica citada nos índices."

# --- Notas-âncora da raiz (o retrato geral) ---
for f in "OVW Miner.md" "Status Agora.md" "Cheat Sheet Miner.md" \
         "CoS Operating Manual.md" "Proximas Acoes Priorizadas.md" \
         "🌐 Mundos.md" "MOC Vault.md" "CLAUDE.md"; do
  [ -f "$V/$f" ] && { sep "$f"; cat "$V/$f"; }
done

# --- Mundos (MOCs temáticos: clientes, time, operação, marketing, projetos, estratégia, sistemas, pessoal) ---
for f in "$V"/Mundos/*.md; do
  case "$(basename "$f")" in _plugins-recomendados.md) continue ;; esac
  sep "Mundos/$(basename "$f")"; cat "$f"
done

# --- Índices: o que EXISTE pra cavar sob demanda ---
for d in companies people projects team stack dossier; do
  sep "ÍNDICE $d/"
  ls "$V/$d" 2>/dev/null | sed 's/\.md$//'
done

printf '\n\n================ COMO USAR ================\n'
printf 'Isto é o backbone. Para aprofundar em algo específico:\n'
printf '  • cliente  -> Read "%s/companies/<Nome>.md"\n' "$V"
printf '  • pessoa   -> Read "%s/people/<Nome>.md"\n' "$V"
printf '  • projeto  -> Read "%s/projects/<Nome>.md"\n' "$V"
printf '  • buscar   -> grep -ri "<termo>" "%s" --include="*.md"\n' "$V"
