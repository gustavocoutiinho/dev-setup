# Paleta e tipografia — São Luiz Supermercado (Maio 2025)

Extraídos direto do manual oficial (`~/Documents/Nova Marca São Luiz 2025 (1) (2).pdf`, p. 11 para paleta e p. 09 para tipografia). Nunca invente variação de tom nem substitua fontes por "equivalente visual" sem consultar aqui primeiro.

## Paleta oficial

Quatro cores. Nada fora daqui em peça oficial.

| Nome           | HEX       | Papel                                                                                          |
| -------------- | --------- | ---------------------------------------------------------------------------------------------- |
| Creme          | `#fff4e8` | Fundo leve, informativo. Cor de wordmark quando o fundo é marrom ou laranja.                   |
| Marrom         | `#7c4016` | Marrom oficial da marca. Fundo assinado e cor do wordmark "São Luiz" quando o fundo é creme.   |
| Marrom escuro  | `#3d2016` | Apoio: tipografia com peso sobre creme, fita de rodapé, borda de sinalização. NÃO é fundo de peça inteira. |
| Laranja        | `#f4951e` | Fundo enérgico (oferta, chegada), sublinha "SUPERMERCADO", selo de preço, pétala do símbolo.   |

### Pares válidos (fundo → tipografia)

Nunca inverta esses pares. Nunca coloque wordmark preto sobre laranja, nem laranja sobre marrom (contraste insuficiente).

- **Fundo creme `#fff4e8`** → título/wordmark **marrom `#7c4016`**, sublinha "SUPERMERCADO" em **laranja `#f4951e`**, corpo de texto em **marrom escuro `#3d2016`**.
- **Fundo marrom `#7c4016`** → título/wordmark **creme `#fff4e8`**, sublinha em **laranja `#f4951e`** OU em creme, corpo em **creme**.
- **Fundo laranja `#f4951e`** → título/wordmark **marrom `#7c4016`**, sublinha em **creme `#fff4e8`**, corpo em **marrom escuro `#3d2016`**.

### Versão monocolor

Quando a peça for impressa em uma única cor (nota fiscal, carimbo, silk 1 cor em uniforme), use tudo em **marrom `#7c4016`** sobre creme (ou em **creme `#fff4e8`** sobre marrom). Nunca faça monocolor em laranja.

## Tipografia

Três famílias, cada uma com um papel específico. Nunca use uma no papel da outra.

### 1. Georgia — títulos, textos, wordmark
**Fonte para títulos e textos** (manual pg. 09). É a espinha dorsal da marca. O próprio wordmark "São Luiz" é construído em Georgia (S e L maiúsculos, sem espaço entre "São" e "Luiz"). Aceita variação **Outline** (contorno vazado) para palavras decorativas e capas.

- Web-safe (vive nativa em qualquer sistema).
- Para impresso de alta qualidade, licenciar Georgia Pro (Ascender Corp.).
- Peso: regular 400, bold 700, italic para palavras destacadas.
- Uso: capas, títulos-âncora, subtítulos, corpo longo (encarte, deck, contrato-tipo).

### 2. Akzidenz Grotesk Next — fonte suporte para textos
**Sans humanista** (manual pg. 09). Complementa Georgia em textos que pedem sans (legenda, "/unidade" no selo de preço, corpo curto em post/story, tabela de preço).

- Fonte licenciada da Berthold. Preço alto.
- **Fallback livre para web**: `Neue Haas Grotesk Text Pro` ou `Inter`. Para paridade máxima com o manual, usar `Akzidenz-Grotesk Pro` (licenciada) em peça impressa premium.
- Peso: regular 400, semibold 600, bold 700.
- Uso: corpo de texto curto, legenda, dado numérico auxiliar, disclaimer, tabela.

### 3. League Gothic — palavras curtas e sinalização
**Sans condensada caixa alta** (manual pg. 09). Fonte de placas, sinalização, sinalização de corredor, categoria, chamada única de vitrine.

- Google Fonts (open source) — `https://fonts.google.com/specimen/League+Gothic`.
- Sempre em CAIXA ALTA. Tracking sutil (0.04 a 0.08em).
- Uso: ENTRADA / SAÍDA / CAIXA / CEREAIS / AÇÚCAR / número de corredor / eyebrows de seção do manual.
- **Nunca use** para texto corrido nem para o wordmark. É fonte de placa.

## Escala tipográfica recomendada (web)

Ponto de partida — ajuste conforme suporte:

| Papel                          | Fonte                | Tamanho                          | Peso     |
| ------------------------------ | -------------------- | -------------------------------- | -------- |
| Display / hero                 | Georgia              | `clamp(3rem, 6vw, 6rem)`         | 700      |
| Título de seção (H1)           | Georgia              | 2.25rem (36px)                   | 700      |
| Subtítulo (H2)                 | Georgia              | 1.5rem (24px)                    | 400/700  |
| Eyebrow / sublinha             | Akzidenz Grotesk     | 0.875rem, uppercase, tracking 0.14em | 700  |
| Corpo                          | Akzidenz Grotesk     | 1rem (16px)                      | 400      |
| Legenda / "/unidade"           | Akzidenz Grotesk     | 0.875rem (14px)                  | 400      |
| Sinalização                    | League Gothic        | `clamp(1.5rem, 4vw, 3rem)`, uppercase, tracking 0.06em | 400 |

## Erros comuns

- Trocar Georgia por Playfair, DM Serif ou Recoleta "porque parecem". **Não são a marca.** Playfair é da irmã festivaldesign, não desta.
- Usar League Gothic no wordmark. Wordmark é Georgia, sempre.
- Aplicar título laranja sobre fundo marrom (não passa em contraste, e nunca aparece no manual). Marrom + creme é o par nobre; laranja é acento.
- Usar o marrom escuro `#3d2016` como fundo de peça inteira. É cor de apoio, não fundo.
- Trocar `#7c4016` por "um marrom qualquer" (chocolate `#8b4513`, saddle brown, etc.). Os HEX são exatos.
