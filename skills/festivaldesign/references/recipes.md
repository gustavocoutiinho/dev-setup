# Receitas de montagem, verificação e exportação

Pipeline para peças do Festival Costume Gourmet. O produto final é sempre um arquivo único autocontido (fontes e imagens em base64), que funciona offline, anexa em mensagem e deploya sem ajuste. Peça social vira PNG; material longo vira página/PDF.

## 1. Fontes (uma vez por projeto, no scratchpad)

Playfair Display e Montserrat são Google Fonts (OFL). Baixe as *variable fonts* (um arquivo cobre todos os pesos) do repositório oficial:

```bash
FONTS="$SCRATCH/fonts"; mkdir -p "$FONTS"
base="https://github.com/google/fonts/raw/main/ofl"
curl -fsSL "$base/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf"        -o "$FONTS/Playfair.ttf"
curl -fsSL "$base/playfairdisplay/PlayfairDisplay-Italic%5Bwght%5D.ttf" -o "$FONTS/Playfair-Italic.ttf"
curl -fsSL "$base/montserrat/Montserrat%5Bwght%5D.ttf"                  -o "$FONTS/Montserrat.ttf"
ls -la "$FONTS"   # ~ Playfair 200KB, Montserrat 700KB
```

No `@font-face`, variable font pede `font-weight` em faixa:

```css
@font-face{font-family:'Playfair';src:url(data:font/ttf;base64,%%F_SERIF%%) format('truetype');font-weight:400 900;font-style:normal;}
@font-face{font-family:'Playfair';src:url(data:font/ttf;base64,%%F_SERIF_IT%%) format('truetype');font-weight:400 900;font-style:italic;}
@font-face{font-family:'Montserrat';src:url(data:font/ttf;base64,%%F_SANS%%) format('truetype');font-weight:400 800;}
```

## 2. Preparar imagens de conteúdo (fotos de chef, ambiente)

Os assets da marca (logo, selo, ícones, ilustrações) já estão prontos em `assets/img/`. Fotos de conteúdo entram em **duotone na cor do mundo** (nunca cruas sob texto). Receita Pillow:

```python
from PIL import Image
def duotone(src, dst, sombra, luz, escurece=0.72):
    g = Image.open(src).convert("L")
    lut = []
    for ch in range(3):
        lut += [int(sombra[ch] + (luz[ch]-sombra[ch])*(i/255)) for i in range(256)]
    im = g.convert("RGB").point(lut*1 if False else lut)   # aplica gradient map
    from PIL import ImageEnhance
    im = ImageEnhance.Brightness(im).enhance(escurece)
    im.save(dst, quality=88)
# Vinho: sombra escura -> realce quente
duotone("chef.jpg","chef-vinho.jpg",(26,7,7),(214,116,46))
# Oliva: sombra escura -> musgo
duotone("chef.jpg","chef-oliva.jpg",(20,20,6),(160,158,77))
```

Fotos: JPEG qualidade 85–90, máx 1200px no lado maior (peça social é 1080). Sempre escureça o suficiente pro texto claro por cima ler.

## 3. Template com tokens + montagem em Python

No HTML de trabalho, referencie por token: fontes `%%F_SERIF%%`/`%%F_SERIF_IT%%`/`%%F_SANS%%`, assets da marca `%%LOGO_FCG%%`, `%%SELO%%`, `%%IC_VINHO%%`, `%%ILUSTRA_MESA%%`, fotos `%%IMG_CHEF%%`. Monte:

```python
import base64, pathlib
SKILL = pathlib.Path.home()/"dev/dev-setup/skills/festivaldesign"  # ou ~/.claude/skills/festivaldesign
IMG = SKILL/"assets"/"img"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
tokens = {
  "%%F_SERIF%%":    b64(FONTS/"Playfair.ttf"),
  "%%F_SERIF_IT%%": b64(FONTS/"Playfair-Italic.ttf"),
  "%%F_SANS%%":     b64(FONTS/"Montserrat.ttf"),
  "%%LOGO_FCG%%":   b64(IMG/"logo-fcg.png"),
  "%%LOGO_SL%%":    b64(IMG/"logo-saoluiz.png"),
  "%%SELO%%":       b64(IMG/"selo-100anos.png"),
  "%%IC_VINHO%%":   b64(IMG/"icones/ic-vinho.png"),
  "%%ILUSTRA_MESA%%": b64(IMG/"ilustra-mesa-vinho.png"),
  # ... só os assets que a peça usa
}
html = (SKILL/"assets/festival-skeleton.html").read_text()  # ou seu template de trabalho
for k,v in tokens.items(): html = html.replace(k, v)
assert "%%" not in html, "token esquecido"
pathlib.Path(OUT/"peca.html").write_text(html)
```

Edite sempre o template (arquivo pequeno), nunca o compilado (megabytes de base64 quebram o Edit). Recompile a cada mudança. Embuta só os assets que a peça usa (base64 pesa ~1.35x o binário).

## 4. Formatos e viewport

| Formato | px | Uso |
|---|---|---|
| Feed 4:5 | 1080×1350 | Padrão do festival |
| Story 9:16 | 1080×1920 | Stories/reels cover |
| Quadrado 1:1 | 1080×1080 | Grade, avatar, card |

Cada peça é um `<section class="peca fmt-45">` (ou `fmt-916`, `fmt-11`) de dimensão fixa. Um HTML pode conter várias peças (carrossel) empilhadas; exporte uma a uma.

## 5. Verificar no navegador antes de entregar

O preview do harness não lê `~/Documents` nem serve bem de fora do scratchpad. Receita que funciona:
1. Copiar o compilado pro scratchpad.
2. `.claude/launch.json` com config `static-preview` (SimpleHTTPRequestHandler com `directory=` no scratchpad).
3. `preview_start` em static-preview; navegar até `http://localhost:8765/peca.html`.
4. Para peça específica num HTML multi, isolar: `document.querySelectorAll('.peca').forEach((s,i)=>s.style.display=i===N?'flex':'none')` e screenshot.
5. Conferir SEMPRE: co-branding presente (FCG + São Luiz/selo), moldura sem corte nas 4 bordas, sparkle no canto, título com alternância de fonte/cor, e em card de foto o duotone + legibilidade do texto claro.

## 6. Exportar PNG por peça (social) e PDF (material longo)

**PNG (o mais comum, é social)** — Chrome headless por peça, em 2x (retina):

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1080,1350 --screenshot="$OUT/peca-01.png" "file://$OUT/peca-01.html"
```

Para várias peças, gere um HTML por peça (mais simples pro screenshot) ou use `--window-size` casando o formato (1080×1920 story, 1080×1080 quadrado). Confira o PNG lendo com Read.

**PDF (convite, cardápio, deck)** — página por peça:

```bash
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT/festival.pdf" "file://$OUT/pecas.html"
```

O CSS de print (`@page{margin:0}` + `print-color-adjust:exact`) já está no esqueleto; sem ele o fundo escuro sai branco.

## 7. Entrega

`open` no arquivo/PNG pro Gustavo ver na hora + SendUserFile. Nome no padrão do Gustavo, em português: `Ⓜ️ Festival Costume Gourmet - <peça>.png`. Se ele pedir "salva nos downloads", copiar pra `~/Downloads/`. Deploy Vercel só se ele pedir (o site do evento já é `festival-costume-gourmet.vercel.app`, ver `festival-gate-stack` no vault).
