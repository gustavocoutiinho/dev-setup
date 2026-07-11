#!/bin/bash
# Faxina do MacBook — reorganização "3 casas" (11/07/2026)
# Espelho da faxina feita no Mac mini. NADA é deletado: só movido (reversível).
# ~/Documents e ~/Desktop NÃO são tocados aqui: sincronizam via iCloud e já
# foram organizados pelo Mac mini (estrutura numerada 01-06).
# Uso: bash ~/dev/dev-setup/scripts/faxina-macbook-2026-07.sh

set -u
echo "======================================"
echo " FAXINA MACBOOK — $(date '+%Y-%m-%d %H:%M')"
echo "======================================"

# ---------- 1. Symlink da memória do Claude -> vault ----------
VAULT="$HOME/ObsidianVaults/miner"
MEMLINK="$HOME/.claude/projects/-Users-gustavocoutinho-Documents-Claude/memory"
if [ -d "$VAULT/memory" ]; then
  mkdir -p "$(dirname "$MEMLINK")"
  if [ -L "$MEMLINK" ]; then
    echo "[1] Symlink da memória já existe -> $(readlink "$MEMLINK")"
  elif [ -d "$MEMLINK" ]; then
    echo "[1] ATENÇÃO: $MEMLINK é diretório real (não symlink)."
    echo "    Movendo pra quarentena e criando symlink pro vault."
    mv "$MEMLINK" "$HOME/_MEMORY_LOCAL_MACBOOK_$(date +%Y-%m-%d)"
    ln -s "$VAULT/memory" "$MEMLINK"
    echo "    Symlink criado. Quarentena: ~/_MEMORY_LOCAL_MACBOOK_$(date +%Y-%m-%d) (comparar e apagar depois)."
  else
    ln -s "$VAULT/memory" "$MEMLINK"
    echo "[1] Symlink da memória criado -> $VAULT/memory"
  fi
else
  echo "[1] AVISO: vault não encontrado em $VAULT (Obsidian Sync não baixou?). Symlink NÃO criado."
fi

# ---------- 2. Inventário: repos git fora de ~/dev (zona de risco) ----------
echo ""
echo "[2] Repos git FORA de ~/dev (iCloud/Documents = risco de corrupção):"
find "$HOME/Documents" "$HOME/Desktop" -maxdepth 4 -name ".git" -type d 2>/dev/null | sed 's|/.git$||' | while read -r r; do
  echo "    RISCO: $r"
done
echo "    (se apareceu algo acima: pushar pro GitHub e mover pra ~/dev — NÃO é automático)"

# ---------- 3. Desktop: capturas de tela ----------
# Desktop sincroniza via iCloud, mas capturas tiradas NO MacBook nascem aqui.
DEST_SS="$HOME/Documents/05-MIDIAS/Screenshots/2026-07-macbook"
count=$(find "$HOME/Desktop" -maxdepth 1 \( -name "Captura de Tela*.png" -o -name "Screenshot*.png" \) 2>/dev/null | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
  mkdir -p "$DEST_SS"
  find "$HOME/Desktop" -maxdepth 1 \( -name "Captura de Tela*.png" -o -name "Screenshot*.png" \) -exec mv {} "$DEST_SS/" \;
  echo "[3] $count capturas do Desktop -> $DEST_SS"
else
  echo "[3] Desktop sem capturas soltas."
fi

# ---------- 4. Downloads: triagem conservadora (>30 dias) ----------
ARQ="$HOME/Downloads/_Arquivo-2026-07"
DOC="$HOME/Documents/06-ARQUIVO/Downloads-Antigos-2026-07-macbook"
mkdir -p "$ARQ/Instaladores" "$ARQ/Compactados-Grandes" "$ARQ/Videos-Grandes" \
         "$DOC"/{PDFs,Imagens,Planilhas-CSVs,Docs,Outros}
moved=0
while IFS= read -r -d '' f; do
  name=$(basename "$f"); ext=$(echo "${name##*.}" | tr 'A-Z' 'a-z'); size=$(stat -f%z "$f")
  case "$ext" in
    dmg|pkg) mv "$f" "$ARQ/Instaladores/" ;;
    zip|rar|7z|gz|tar) if [ "$size" -gt 52428800 ]; then mv "$f" "$ARQ/Compactados-Grandes/"; else mv "$f" "$DOC/Outros/"; fi ;;
    mp4|mov|webm) if [ "$size" -gt 52428800 ]; then mv "$f" "$ARQ/Videos-Grandes/"; else mv "$f" "$DOC/Outros/"; fi ;;
    pdf) mv "$f" "$DOC/PDFs/" ;;
    png|jpg|jpeg|gif|webp|svg|heic) mv "$f" "$DOC/Imagens/" ;;
    xlsx|xls|csv|numbers) mv "$f" "$DOC/Planilhas-CSVs/" ;;
    docx|doc|pptx|key|md|txt|html) mv "$f" "$DOC/Docs/" ;;
    *) if [ "$size" -gt 52428800 ]; then mv "$f" "$ARQ/Compactados-Grandes/"; else mv "$f" "$DOC/Outros/"; fi ;;
  esac
  moved=$((moved+1))
done < <(find "$HOME/Downloads" -maxdepth 1 -type f -mtime +30 ! -name ".*" -print0)
echo "[4] Downloads: $moved arquivos >30 dias triados (pesados ficam locais em _Arquivo-2026-07)."

# ---------- 5. Home: inventário de pastas fora do padrão ----------
echo ""
echo "[5] Pastas no home fora do padrão (avaliar manualmente, NÃO movidas):"
ls -d "$HOME"/*/ 2>/dev/null | grep -v -E "/(Applications|Desktop|Documents|Downloads|Library|Movies|Music|Pictures|Public|ObsidianVaults|dev|Google Drive|OrbStack)/$" || echo "    (nenhuma)"

# ---------- 6. Estado das casas ----------
echo ""
echo "[6] Estado das 3 casas nesta máquina:"
[ -d "$HOME/dev" ] && echo "    ~/dev existe ($(ls "$HOME/dev" | wc -l | tr -d ' ') itens)" || echo "    ~/dev NÃO existe — criar e clonar do GitHub (nunca copiar pastas entre máquinas)"
[ -d "$VAULT" ] && echo "    vault OK" || echo "    vault AUSENTE"
[ -e "$HOME/Library/CloudStorage" ] && ls "$HOME/Library/CloudStorage" | sed 's/^/    CloudStorage: /'
echo ""
echo "LEMBRETE (manual): conferir no app Google Drive deste MacBook se o backup"
echo "de Documentos/Mesa está ligado — se estiver, DESLIGAR (o iCloud já cuida)."
echo "======================================"
echo " FIM — nada foi deletado."
echo "======================================"
