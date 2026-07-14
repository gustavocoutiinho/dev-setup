# Inventário da IDV do Festival Costume Gourmet

Todos os assets foram extraídos do PDF oficial `~/Documents/Cópia de FCG 2026 - IDV Canva FEED.pdf` (IDV feita no Canva) e vivem em `assets/img/` desta skill, já com fundo transparente (alpha). Caminhos relativos à raiz da skill.

## Paleta (hex amostrados do PDF)

### Os três mundos de fundo
| Nome | Base | Realce (gradiente) | Uso |
|---|---|---|---|
| **Vinho** | `#3A0F0E` | centro `#4E1714` | Fundo-assinatura. Gradiente radial (centro mais quente, bordas escuras) |
| **Oliva** | `#26260A` | `#4A4A22` | Variação verde-escuro, mesma diagramação. Alternar com Vinho na campanha |
| **Creme** | `#FCF6EE` | — | Fundo claro, para peças de frase com tipografia colorida pura |

O fundo escuro nunca é chapado: use `radial-gradient` do realce (topo/centro) para a base (bordas), dá o ar de vinheta da arte original.

### Acentos quentes (o multicolor da marca — alterne, nunca use um só num título)
| Nome | Hex | Onde aparece |
|---|---|---|
| Dourado / Âmbar | `#D8992F` (claro `#E2A94C`) | Títulos-âncora, "save the date", números, "Quando/Onde" |
| Laranja | `#D2742E` | Palavras de destaque, "Costume", "Degustações", "futuro" |
| Telha | `#DC463C` | Palavra-âncora viva, "Gourmet", "histórias", "passado" |
| Coral / Rosé | `#C25D50` | Subtítulos e tom suave, "de uma bela" |
| Musgo | `#A0A04E` | Acento verde (protagonista no mundo Oliva), "presente", "experiências" |
| Marrom / Cacau | `#6E3C16` | Apoio, palavra de peso sobre creme |
| Bordô | `#5A1414` | Apoio escuro, sombra de palavra |
| Nude / Trigo | `#D3A281` | Apoio quente claro |
| Marinho | `#3F3275` | Raríssimo (só o ícone da rolha); não é cor de texto |

### Neutros
| Nome | Hex | Uso |
|---|---|---|
| Creme texto | `#FCF6EE` | Texto claro sobre fundo escuro |
| Creme suave | `#EADFCF` | Corpo/legenda sobre fundo escuro |
| Grafite | `#4A4744` | Texto neutro sobre fundo Creme (o cinza das frases) |

## Tipografia (Google Fonts — reproduzem a arte do Canva)

- **Playfair Display** (serif display, alto contraste, terminais em gota). É a fonte dos **títulos-âncora gigantes coloridos**, palavras de destaque, números grandes e o "save the date" (em **italic**). Pesos: 400/500/600/700/800/900 + italic. Baixar de Google Fonts (ver recipes.md); embutir Regular, SemiBold, Bold, Black + BoldItalic.
- **Montserrat** (sans geométrica). É a fonte dos **rótulos e subtítulos em CAIXA ALTA com letter-spacing** (SABORES, DE SETEMBRO, ATRAÇÃO CONFIRMADA, SUPERMERCADO) e do corpo. Pesos: 400/500/600/700/800. Sempre com `letter-spacing` generoso quando em caps (0.15em a 0.35em).

Assinatura tipográfica: título empilhado alternando as duas fontes e as cores, linha a linha. Ex.: `SABORES` (Montserrat caps creme) / `de uma bela` (Montserrat caps coral) / `história` (Playfair enorme dourado). Contraste de tamanho é agressivo: âncora 80–160px vs rótulo 16–32px numa peça de 1080px.

## Logos e selo (co-branding — sempre presentes)

| Arquivo | O que é | Quando usar |
|---|---|---|
| `img/logo-fcg.png` | Logo Festival Costume Gourmet (símbolo G + "FESTIVAL Costume Gourmet"), colorido | Topo da peça. Funciona sobre Vinho, Oliva e Creme. Para versão branca sobre escuro, aplicar `filter:brightness(0) invert(1)` |
| `img/logo-saoluiz.png` | Logo São Luiz Supermercado (trevo + wordmark) | Rodapé, co-branding. Trevo laranja + wordmark creme |
| `img/selo-100anos.png` | Selo dourado metálico "100 anos São Luiz" | Rodapé, ao lado do logo São Luiz. É a razão do festival (centenário) |

Regra: o Festival não aparece sozinho. Pelo menos dois dos três (tipicamente FCG no topo + São Luiz e/ou selo no rodapé).

## Elementos gráficos

| Arquivo | O que é | Quando usar |
|---|---|---|
| `img/carimbo-vinho.png` / `img/carimbo-oliva.png` | Carimbo circular "FESTIVAL COSTUME GOURMET" (efeito stamp gasto) com toque de chef no centro | Selo decorativo grande, semi-transparente, atrás do conteúdo num canto. Use a cor do mundo oposto ou baixe a opacidade |
| `img/ondas-vinho.png` / `img/ondas-oliva.png` | Ondas de carimbo postal | Canto superior direito das peças "save the date", reforça o ar de convite/correspondência |
| `img/ilustra-mesa-vinho.png` / `img/ilustra-mesa-oliva.png` | Gravura de mesa posta (garrafas, taças, pratos) | Textura de fundo tom-sobre-tom em baixa opacidade (0.06–0.12), embaixo do texto |
| `img/ilustra-ramo-vinho.png` / `img/ilustra-ramo-oliva.png` | Gravura de ramo/ervas vertical | Textura lateral de fundo, mesma lógica de opacidade baixa |
| `img/pattern-vinho.png` | Pattern de ícones de comida (taças, queijo, pão, garrafa…) | Papel de parede/textura densa; use recortado e suave, não protagonista |

Moldura + sparkle **não são bitmap**: são recriados em SVG/CSS no esqueleto (linha fina dupla com cantos chanfrados em gradiente dourado→telha + estrela de 4 pontas dourada). Assim escalam em qualquer formato sem perder nitidez.

## Ícones circulares de gravura (13 sabores)

Círculo de cor sólida da paleta + desenho branco de gravura à mão. Ficam em `img/icones/`. São os chips temáticos da marca (cada assunto tem o seu). PNG com alpha; a cor já vem embutida.

| Arquivo | Desenho | Cor do círculo | Sugestão de tema |
|---|---|---|---|
| `ic-ramo.png` | Ramo de oliveira | Musgo | Ingredientes, natural, orgânico |
| `ic-cafe.png` | Grãos de café | Marrom | Café, aroma, degustação |
| `ic-sacarolha.png` | Saca-rolha | Bordô | Vinho, harmonização |
| `ic-graos.png` | Grãos (símbolo da marca) | Bordô | Marca, abertura, genérico |
| `ic-alho.png` | Alho | Nude | Tempero, cozinha, sabor |
| `ic-vinho.png` | Garrafa + taça | Coral | Vinho, brinde, bar |
| `ic-canela.png` | Rolo de canela | Bordô | Especiaria, doce, aroma |
| `ic-queijo.png` | Queijo | Laranja | Queijos, tábua, marcas |
| `ic-rolha.png` | Rolha | Marinho | Vinho, adega |
| `ic-pao.png` | Baguete | Nude | Padaria, pães, básico |
| `ic-ervas.png` | Ervas / manjericão | Musgo | Ervas, frescor, saudável |
| `ic-cogumelo.png` | Cogumelo | Telha | Ingrediente, prato, chef |
| `ic-livro.png` | Livro aberto | Laranja | História, receita, memória, "há histórias" |

Para chip com fundo claro (Creme), o próprio círculo colorido já resolve. Sobre fundo escuro, os círculos coloridos também funcionam; se quiser o desenho recortado em branco puro, dá pra recriar via máscara, mas normalmente o ícone colorido pronto basta.

## Voz da copy (quando criar texto do zero)

Evocativa, sensorial, ligada a história / memória / sabor / experiência. Exemplos reais da IDV: "Sabores de uma bela história", "Há histórias que não se contam apenas com palavras", "Diferente de tudo que você já viu", "Uma edição única e exclusiva", "Prove sabores que marcaram o passado, transformam o presente e inspiram o futuro". Palavras-âncora recorrentes: **sabores, história, gastronomia, experiências, chefs, degustações, atrações**. Rótulos utilitários em caps: SAVE THE DATE, QUANDO, ONDE, ATRAÇÃO CONFIRMADA.
