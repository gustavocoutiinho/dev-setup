# Receitas de montagem, verificação e PDF

Pipeline comprovado (usado na proposta Diamantes, jul/2026). O produto final é sempre um arquivo único autocontido: fontes, fotos e ícones embutidos em base64, sem dependência externa. Funciona offline, anexa em email e deploya na Vercel sem ajuste.

## 1. Preparar assets (uma vez por projeto, no scratchpad)

```bash
KV="/Users/gustavocoutinho/Documents/Miner- Base Visual - KV - ID VIsual"
# fotos: JPEG 82%, máx 1600-1920px
sips -s format jpeg -s formatOptions 82 -Z 1600 "$KV/06 - Novo site/serv3.png" --out "$SCRATCH/assets/taxi.jpg"
# ícones: manter PNG (preserva transparência), 480px
sips -Z 480 "$KV/04 - Ícones/PNG/icones-13.png" --out "$SCRATCH/assets/icons/cap.png"
```

## 2. Template com tokens + montagem em Python

No HTML de trabalho, referencie assets por token: `url(data:font/otf;base64,%%F_SERIF%%)`, `src="data:image/png;base64,%%I_CAP%%"`, `background-image:url(data:image/jpeg;base64,%%IMG_TAXI%%)`. Depois monte:

```python
import base64, pathlib
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
tokens = {"%%F_SERIF%%": b64(FONTS/"Secundária/Behind-The-Nineties-Bd 2.otf"), ...}
html = template.read_text()
for k, v in tokens.items():
    html = html.replace(k, v)
assert "%%" not in html  # nenhum token esquecido
```

Editar sempre o template (arquivo pequeno), nunca o compilado (megabytes de base64 quebram o Edit). Recompilar a cada mudança. Fontes mínimas: VisbyCF Light/Regular/DemiBold/ExtraBold + Behind-The-Nineties-Bd 2.

## 3. Estrutura de slides

Base pronta em `assets/slides-skeleton.html` (CSS completo + um exemplo de cada componente). Pontos que dão trabalho:

- `.slide{width:100vw;height:100vh;scroll-snap-align:start}` + navegação por teclado no script do esqueleto.
- Slide 16:9 tem altura fixa: conteúdo que estoura fica CORTADO silenciosamente. Painel com muitos bullets + faixa de preço + faixa de gap é o caso clássico. Verificar sempre (passo 4).
- Print CSS já incluso: `@page{size:13.333in 7.5in;margin:0}` + `print-color-adjust:exact` (sem isso o PDF sai branco).

## 4. Verificar no navegador antes de entregar

O preview do harness não lê `~/Documents` (sandbox sem permissão) e o `http.server` padrão quebra com `getcwd`. Receita que funciona:

1. Copiar o compilado pro scratchpad (`preview-slides.html`).
2. `.claude/launch.json` do projeto já tem a config `static-preview`: python `-I -c` com `SimpleHTTPRequestHandler` e `directory=` apontando pro scratchpad (se a sessão for outra, ajustar o caminho do scratchpad na config).
3. `preview_start` em static-preview, `preview_resize` 1280x720, navegar até `http://localhost:8765/preview-slides.html`.
4. O screenshot só captura o topo da página: para ver o slide N, isolar via eval `sl.forEach((s,i)=>s.style.display = i===N ? 'flex':'none'); window.scrollTo(0,0);` e então `preview_screenshot`.
5. Conferir no mínimo: capa, tabelas densas, slides com SVG e o último. Procurar estouro de altura e texto de foto cortado.
6. `preview_stop` ao terminar.

## 5. Gerar PDF (cada slide = uma página 16:9)

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-first-run \
  --user-data-dir="$SCRATCH/chrome-profile" \
  --no-pdf-header-footer --virtual-time-budget=20000 \
  --print-to-pdf="$SCRATCH/saida.pdf" "file://$SCRATCH/preview-slides.html"
```

Gotchas: o processo pode não encerrar sozinho depois de escrever o PDF (rodar em background, conferir se o arquivo apareceu com tamanho pleno e matar a task). Validar lendo o PDF (Read com pages) e conferindo a contagem: `re.findall(rb'/Type\s*/Page[^s]', data)`. Nome de entrega no padrão do Gustavo: `Ⓜ️ PROPOSTA COMERCIAL <Título> - Miner + <Cliente>.pdf`.

## 6. Entrega

`open` no arquivo pro Gustavo ver na hora + SendUserFile. Se ele pedir "salva nos downloads", copiar pra `~/Downloads/`. Deploy Vercel só se ele pedir, no padrão `<cliente>-proposta.vercel.app`.
