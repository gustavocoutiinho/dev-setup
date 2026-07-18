---
name: exporta-deck
description: Use quando o Gustavo pedir pra "gerar PDF do deck", "exportar o deck em imagem", "PNG de cada tela", "manda o deck em PDF pro cliente", "exporta o relatório", "versão pra enviar", ou precisar do deck fora do navegador. Gera PDF e imagens retina de qualquer deck-* de forma programática, via Chrome headless, padronizando o export.py que hoje só o Festival tem. Dispara em qualquer pedido de export/PDF/imagem de deck.
---

# exporta-deck · PDF e PNG retina de qualquer deck

## O que faz
Hoje só o `deck-festival` tem export (`~/dev/decks/deck-festival/_src/export.py`): gera um PNG
retina por tela e um PDF do deck inteiro, via **Chrome headless**. Esta skill generaliza esse
export.py pra qualquer `deck-*`, sem depender de print manual.

## Como funciona (base: export.py do Festival)
- Chrome em `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.
- **PNG por tela:** o HTML é quebrado por `<section class="tela...">`; cada tela vira um HTML
  isolado (reaproveitando o `<head>` com fontes/estilos) e é fotografada com
  `--force-device-scale-factor=2` (retina) e `--window-size=1280,720`.
- **PDF do deck inteiro:** `--print-to-pdf` no `index.html` com `--no-pdf-header-footer`.
- Saída em `_src/export/`.

## Como executar
1. **Conferir o seletor de tela.** O split depende da classe da seção (no Festival é
   `class="tela`). Se o deck usa outra classe (`slide`, `screen`), ajustar o `split` e a lista
   de nomes de arquivo pra bater 1:1 com o número de telas (o script tem `assert len==len`).
2. **Rodar o build antes se houver** (`build.py`): decks montados por script precisam gerar o
   `index.html` final antes do export. Deck single-file pula essa etapa.
3. **Gerar:** adaptar o `export.py` pro deck alvo (ou copiar pro `_src/` do deck) e rodar
   `python3 _src/export.py`. Comando headless por tela:
   ```
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless=new --disable-gpu --hide-scrollbars \
     --force-device-scale-factor=2 --window-size=1280,720 \
     --screenshot="_src/export/<nome>.png" "file://<tela.html>"
   ```
   PDF do deck:
   ```
   "...Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="_src/export/<deck>.pdf" "file://<index.html>"
   ```
4. **Fundo/padding:** o export do Festival injeta `body{padding:0;gap:0;background:...}` no
   `<head>` de cada tela pra não sobrar borda. Ajustar a cor de fundo ao KV do deck.
5. **Nome do arquivo em pt-BR**, descritivo (cliente + tipo + competência), sem travessão.

## Gotchas
- **Fontes locais são essenciais.** O headless carrega `file://`; fonte via CDN externo não
  entra no PNG/PDF. Por isso o deck-kit serve fonte local.
- **Contagem de telas.** Se o `assert` de telas x nomes falhar, é sinal de que o deck ganhou ou
  perdeu uma seção: atualizar a lista de nomes, não forçar o assert.
- **1280x720 é 16:9.** Decks em outra proporção precisam de `--window-size` próprio.
- **PDF vs PNG:** PDF é o deck inteiro num arquivo (bom pra enviar); PNGs são tela a tela (bom
  pra feed/story/anexo). Gerar o que o pedido pede, não sempre os dois.
- **Não deployar a pasta `_src/export/`** junto do site; é artefato de entrega, não do deck no
  ar (mantê-la fora do que o Vercel publica).

## NÃO fazer
- Não tirar screenshot manual do navegador: usar o headless (retina, reproduzível).
- Não exportar deck com fonte de CDN sem antes localizar as fontes.
- Não enviar o PDF/PNG pro cliente sem ordem explícita do Gustavo (regra: só leitura, envio só
  por item).
