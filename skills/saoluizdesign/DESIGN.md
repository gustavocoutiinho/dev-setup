---
version: 1.0
name: São Luiz Supermercado Design System
description: >
  Identidade visual do São Luiz Supermercado (marca-mãe do Grupo São Luiz / MSLZ,
  cliente Miner). Manual "Nova Marca São Luiz 2025 — Maio 2025". Paleta creme +
  marrom + laranja, símbolo trevo-de-corações, wordmark serif Georgia + sublinha
  sans caixa alta, grafismos de silhueta de alimentos/utensílios. Fonte de tokens
  para social, encarte, papelaria, embalagem, uniforme, fachada, sinalização, deck,
  site e portal. Para o pipeline completo (fontes, imagens, verificação) use a
  skill saoluizdesign.
---

# ---- Design tokens (machine-readable) ----
colors:
  cream:            "#fff4e8"   # fundo mais leve, informativo. Predominante em encarte/tabloide.
  brown:            "#7c4016"   # marrom oficial da marca. Fundo assinado + wordmark sobre creme.
  brown-deep:       "#3d2016"   # marrom escuro/quase-preto. Apoio: tipografia com peso sobre creme, fita de rodapé, borda de sinalização. NÃO é fundo de peça inteira.
  orange:           "#f4951e"   # laranja oficial. Fundo enérgico (oferta, chegada) + sublinha "SUPERMERCADO" + selo de preço.

# Pares válidos (fundo → tipografia). Nada fora daqui:
pairs:
  cream-bg:         { bg: cream,  title: brown,      accent: orange, body: brown-deep }
  brown-bg:         { bg: brown,  title: cream,      accent: orange, body: cream }
  orange-bg:        { bg: orange, title: brown,      accent: cream,  body: brown-deep }

typography:
  # Georgia = fonte-âncora (já é web-safe, cai automático em qualquer sistema).
  # Para paridade exata com o manual, comprar/licenciar a família Georgia Pro se a peça for impressa.
  title-family:     "'Georgia', 'Georgia Pro', 'Times New Roman', serif"
  # Akzidenz Grotesk Next é licenciada (Berthold). Fallback livre: Neue Haas Grotesk / Inter.
  body-family:      "'Akzidenz Grotesk Next', 'Neue Haas Grotesk Text Pro', 'Inter', system-ui, sans-serif"
  # League Gothic é Google Fonts (free). Só para palavras curtas e sinalização.
  signage-family:   "'League Gothic', 'Oswald', 'Impact', sans-serif"
  weights:
    title-regular:  400
    title-bold:     700
    body-regular:   400
    body-bold:      700
    signage:        400   # já é condensada e pesada por natureza
  scale:
    # Escala relativa a rem (16px = 1rem). Ajuste conforme o suporte.
    display:        "clamp(3rem, 6vw, 6rem)"     # capa/hero, serif
    title-1:        "2.25rem"                     # 36px — títulos de seção
    title-2:        "1.5rem"                      # 24px — subtítulos
    body:           "1rem"                        # 16px — corpo
    caption:        "0.875rem"                    # 14px — legenda, "/unidade"
    signage:        "clamp(1.5rem, 4vw, 3rem)"    # placas, sinalização, corredor
  letter-spacing:
    body:           "0"
    signage:        "0.06em"                      # League Gothic + tracking sutil

logo:
  wordmark:         "São Luiz"                    # Georgia, S e L maiúsculos, sem espaço entre "São" e "Luiz"
  tagline:          "SUPERMERCADO"                # sans caixa alta, laranja sobre fundo claro / creme sobre fundo escuro
  symbol:           "trevo-de-corações"           # 4 pétalas, cada pétala é um coração; pétala superior levemente destacada
  grid-unit:        "X = altura da palavra SUPERMERCADO"
  symbol-height:    "3X"
  clear-space:      "3X em todos os lados do lockup"
  valid-symbol-colors:
    - "orange over cream/brown-bg"                # laranja sólido
    - "brown over cream"                          # monocolor marrom
    - "cream over brown/orange"                   # sólido creme (versão invertida)
  never:
    - "outline no lugar do fill"                  # símbolo é sempre chapado
    - "gradient em pétala"
    - "pétala trocada por círculo/estrela/folha"
    - "cor fora da paleta"

graphics:
  # Silhuetas planas de alimentos/utensílios. Sempre em UMA cor (marrom OU laranja).
  vocabulary:
    - apple
    - banana
    - lemon
    - wine-bottle
    - wine-glass
    - whisk
    - cupcake
    - croissant
    - spray-bottle
    - bucket
  rules:
    - "fill único, sem contorno, sem gradiente"
    - "cor: brown (#7c4016) OU orange (#f4951e). Nunca as duas na mesma silhueta."
    - "aparecem soltas (ícone), em fila (grid horizontal) ou como pattern grande (crop em retângulo)"
    - "quando usadas em pattern de fundo em peça vertical (story/banner), usar rounded rectangle radius: 24-32px"

photography:
  style:
    - "real, quente, gastronômica"
    - "iluminação âmbar/terracota, sombra suave"
    - "comida de verdade, mão de gente de verdade, mesa posta"
    - "cortes cinematográficos, plano fechado no produto/gesto"
  never:
    - "render 3D genérico"
    - "stock corporativo azulado/frio"
    - "foto de gente sorrindo forçado para câmera de forma stock"

components:
  price-badge:
    shape:          "círculo laranja (#f4951e)"
    price-number:   "Georgia bold em creme (#fff4e8)"
    price-unit:     "sans caps pequeno em creme"
    label-top:      "'A PARTIR DE' em sans caps pequeno, opcional"
  signage:
    background:     "brown (#7c4016) ou brown-deep (#3d2016)"
    text:           "League Gothic caixa alta em cream"
    accent-element: "letra em círculo cream, o círculo é fill cream, letra em brown"
    layout:         "leitura vertical em placa alta (rua) ou horizontal em placa suspensa (dentro de loja)"
  bag-uniform:
    fabric:         "brown (#7c4016)"
    print:          "lockup completo em cream, ou só o símbolo em orange/cream repetido pequeno como pattern"
  packaging-kraft:
    base:           "papelão kraft cru"
    print:          "ícone (trevo) em brown, wordmark em brown com sublinha orange"

layout:
  radius:           { sm: "12px", md: "24px", lg: "32px", pill: "999px" }
  spacing-scale:    ["4px","8px","12px","16px","24px","32px","48px","64px","96px"]
  container:        { max-width: "1280px", padding-inline: "24px" }
  grid-hero:        "12 cols, gap 24px"
  # Todas as fotos e patterns entram dentro de retângulos com radius lg (32px).

voice:
  # Assinaturas verbais oficiais vistas no manual. Use quando cabível.
  taglines:
    - "Lugar de quem faz com o coração."
    - "A gente encontra e se encontra aqui."
  register: "afetivo, direto, popular sem ser vulgar; próximo do cearense sem caricatura"
  writing-rules:
    - "sem travessão (em-dash) — trocar por vírgula, dois-pontos, parênteses ou ponto"
    - "sem emoji em peça oficial"

# ---- CSS (drop-in variables) ----
css: |
  :root {
    --sl-cream:       #fff4e8;
    --sl-brown:       #7c4016;
    --sl-brown-deep:  #3d2016;
    --sl-orange:      #f4951e;

    --sl-bg:          var(--sl-cream);
    --sl-fg:          var(--sl-brown);
    --sl-accent:      var(--sl-orange);
    --sl-body:        var(--sl-brown-deep);

    --sl-title:       'Georgia', 'Georgia Pro', 'Times New Roman', serif;
    --sl-body-font:   'Akzidenz Grotesk Next', 'Neue Haas Grotesk Text Pro', 'Inter', system-ui, sans-serif;
    --sl-signage:     'League Gothic', 'Oswald', 'Impact', sans-serif;

    --sl-radius-sm:   12px;
    --sl-radius-md:   24px;
    --sl-radius-lg:   32px;
  }

  html, body {
    background: var(--sl-bg);
    color: var(--sl-body);
    font-family: var(--sl-body-font);
  }

  /* Utilitários de fundo — troque no <html data-bg="brown"> etc. */
  [data-bg="brown"]  { --sl-bg: var(--sl-brown);  --sl-fg: var(--sl-cream);      --sl-body: var(--sl-cream); }
  [data-bg="orange"] { --sl-bg: var(--sl-orange); --sl-fg: var(--sl-brown);      --sl-body: var(--sl-brown-deep); }
  [data-bg="cream"]  { --sl-bg: var(--sl-cream);  --sl-fg: var(--sl-brown);      --sl-body: var(--sl-brown-deep); }

  h1, h2, h3, .sl-title {
    font-family: var(--sl-title);
    color: var(--sl-fg);
    font-weight: 700;
    letter-spacing: -0.01em;
  }

  .sl-sublinha, .sl-eyebrow {
    font-family: var(--sl-body-font);
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--sl-accent);
    font-weight: 700;
    font-size: 0.875rem;
  }

  .sl-signage {
    font-family: var(--sl-signage);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--sl-cream);
  }

  .sl-price-badge {
    display: inline-grid;
    place-items: center;
    background: var(--sl-orange);
    color: var(--sl-cream);
    border-radius: 999px;
    aspect-ratio: 1;
    padding: 1.25rem;
    font-family: var(--sl-title);
    font-weight: 700;
  }

  .sl-card, .sl-photo, .sl-pattern {
    border-radius: var(--sl-radius-lg);
    overflow: hidden;
  }

# ---- Tailwind (theme.extend) ----
tailwind: |
  // tailwind.config.js
  module.exports = {
    theme: {
      extend: {
        colors: {
          saoluiz: {
            cream:     '#fff4e8',
            brown:     '#7c4016',
            'brown-2': '#3d2016',
            orange:    '#f4951e',
          },
        },
        fontFamily: {
          'sl-title':   ['Georgia', 'Georgia Pro', 'Times New Roman', 'serif'],
          'sl-body':    ['"Akzidenz Grotesk Next"', 'Inter', 'system-ui', 'sans-serif'],
          'sl-signage': ['"League Gothic"', 'Oswald', 'Impact', 'sans-serif'],
        },
        borderRadius: {
          'sl-sm': '12px',
          'sl-md': '24px',
          'sl-lg': '32px',
        },
      },
    },
  }

# ---- Prompt colável em v0 / Cursor / Lovable ----
paste-prompt: |
  Você vai usar o design system do São Luiz Supermercado (cliente Miner). Regras:

  Paleta (nada fora daqui):
  - creme  #fff4e8  (fundo leve, informativo)
  - marrom #7c4016  (fundo assinado + wordmark sobre creme)
  - marrom escuro #3d2016 (apoio para tipografia sobre creme e rodapés — NÃO fundo de página inteira)
  - laranja #f4951e (fundo enérgico + sublinha SUPERMERCADO + selo de preço)

  Pares válidos:
  - Sobre CREME: título marrom, acento laranja, corpo marrom-escuro.
  - Sobre MARROM: título creme, acento laranja, corpo creme.
  - Sobre LARANJA: título marrom, acento creme, corpo marrom-escuro.

  Tipografia:
  - Títulos e textos longos: Georgia (serif). O wordmark "São Luiz" é sempre Georgia com S e L maiúsculos, sem espaço.
  - Corpo/legenda: Akzidenz Grotesk Next; fallback livre: Inter.
  - Sinalização (palavras curtas, placas, categoria): League Gothic, caixa alta, tracking 0.06em.

  Símbolo: trevo-de-corações (4 pétalas em formato de coração). Sempre chapado, uma cor só (laranja, marrom ou creme conforme fundo).

  Componentes recorrentes:
  - Selo de preço: círculo laranja com número Georgia em creme.
  - Placas de sinalização: fundo marrom, texto League Gothic em creme.
  - Sacola/uniforme: marrom com lockup creme.
  - Fotos: quentes, gastronômicas, iluminação âmbar; cortes com radius 32px.

  Assinatura verbal quando fizer sentido: "Lugar de quem faz com o coração." / "A gente encontra e se encontra aqui."

  Regras de escrita: sem travessão (em-dash), sem emoji.
