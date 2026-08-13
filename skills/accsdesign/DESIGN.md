---
version: 1.0
name: Grupo Aço Cearense Design System
description: >
  Identidade visual do Grupo Aço Cearense (GAC), holding de siderurgia/aço do Ceará
  (marcas: Aço Cearense, SINOBRAS, SINOBRAS Florestal, Instituto Aço Cearense).
  Azul-marinho + azul-claro institucionais, wordmark bicolor em "K", fotografia industrial
  com filtro azul, grafismo diagonal derivado do logo. Fonte de tokens para deck, KV/campanha,
  papelaria e web. Para o pipeline completo (fontes, imagens, verificação) use a skill accsdesign.
---

# ---- Design tokens (machine-readable) ----
colors:
  navy:              "#223564"   # institucional, predominante sempre. Pantone 534 C / CMYK 99,84,31,20
  light-blue:        "#6EAFD5"   # institucional, predominante sempre. Pantone 542 C / CMYK 59,18,8,0
  black:             "#000000"   # neutro, só apoio
  gray:              "#9D9D9C"   # neutro, só apoio. Pantone Cool Gray 7C
  white:             "#FFFFFF"
  secondary-teal:    "#55C0B3"   # "turquesa-rio"
  secondary-lime:    "#94C120"
  secondary-coral:   "#FF5C60"
  secondary-navy-2:  "#102D69"
  secondary-blue-2:  "#7DB5DA"
  secondary-green:   "#00A25E"
  secondary-beige:   "#D9BF9E"
  secondary-brown:   "#8B5843"
  secondary-lavender: "#E3E1E6"
  restricted-yellow: "#F8BE38"   # SÓ casos especiais (ex. Setembro Amarelo), nunca uso livre
  alert:             "#D84854"   # só diagramação/aviso, não é cor de marca aplicável a peça
  gradient-institucional: "linear-gradient(135deg, #6EAFD5, #223564)"  # o degradê-padrão de fundo/filtro foto

  # cor de identificação por marca do grupo (ver references/logo-e-submarcas.md)
  marca-grupo:       "{colors.navy} + {colors.light-blue}"
  marca-aco-cearense: "#4496BB"   # azul médio/petróleo (crachás)
  marca-sinobras:    "#CECECE"    # cinza/prata
  marca-florestal:   "#1D9F61"    # verde
  marca-instituto:   "{colors.navy}"  # sem cor própria documentada, usa institucional

typography:
  display:   { fontFamily: "Herokid", fallback: "'Big Shoulders Display', 'Anton', sans-serif", fontWeight: 800, textTransform: "uppercase" }
  script:    { fontFamily: "Monstane Olstd", fallback: "'Yellowtail', 'Sacramento', cursive", fontWeight: 400 }
  body:      { fontFamily: "Manrope", fontWeight: 400, lineHeight: 1.6 }
  body-bold: { fontFamily: "Manrope", fontWeight: 700 }
  office-fallback: { fontFamily: "Arial", pair: "Montserrat" }  # só quando Manrope indisponível (Office/sistemas)

spacing:   # módulo = maior lado da peça ÷ 40 (ou menor lado ÷ 14 se quadrada/muito alongada); gutter = 2/3 do módulo
  module-formula: "max(width,height) / 40, ou min(width,height) / 14 se quadrada"
  gutter: "2/3 do módulo"
  columns: "múltiplos de 2 (2,4,6,8,12,16,20,24)"

logo:
  clear-space: "X = altura da letra G do wordmark, nos 4 lados"
  min-size-full: "7.5mm / 22px de altura"
  min-size-compact: "5mm / 14px de altura (símbolo isolado ou lockup reduzido)"
  min-size-floor: "3mm, abaixo disso usar só a versão monogramática de uso restrito"
  pairing-gap: "2X entre a marca prioritária e a marca acompanhante; respiro externo 1X; módulo da marca acompanhante = X/2"

components:
  kv-campanha:
    layout: "fotografia em 2-4 fatias diagonais (grafismo) + bloco de texto lateral"
    text-block: "hashtag da marca no topo, tagline (sans + script) abaixo, rodapé com URL em pílula + logo"
    bg-default: "{colors.navy} com {colors.gradient-institucional}"
    bg-esg-variant: "verde, para pautas de sustentabilidade/ESG"
  card-corporativo:
    backgroundColor: "{colors.white}"
    logo-position: "rodapé, alinhado à direita ou esquerda conforme peça"
  selo-projeto:
    font: "Manrope Medium (qualificador) + Bold (nome do projeto)"
    layout: "ícone de linha à esquerda + texto empilhado (2 linhas) à direita"
  icone:
    grid: "24x24px, traço 1px"
    style: "outline, cantos arredondados, uma cor só por ícone"
---

## Overview

O Grupo Aço Cearense é uma holding de siderurgia (Ceará, Brasil) com 4 marcas sob o guarda-chuva institucional: **Aço Cearense** (aços planos), **SINOBRAS** (aços longos), **SINOBRAS Florestal** (biorredutor florestal) e **Instituto Aço Cearense** (impacto social). A identidade é industrial-confiante: azul-marinho profundo, fotografia real de gente trabalhando (nunca stock genérico), um símbolo geométrico anguloso ("K", ligadura de A+C) que se repete em grafismo, textura e ícones. Tagline-mãe: **"Nossa gente dá liga. Nossa liga constrói o futuro."**

Três decisões fundam tudo:

1. **Azul institucional sempre predominante.** Navy `#223564` + azul-claro `#6EAFD5` são as únicas cores "obrigatórias" em qualquer peça, de qualquer marca do grupo. Cores secundárias e a cor própria de cada submarca ampliam, nunca substituem essa base.
2. **O símbolo "K" é a origem de tudo.** Logo, ícones, textura e grafismo (o corte diagonal de cantos opostos arredondados/retos) vêm todos do mesmo ângulo geométrico. Nada nasce solto.
3. **Fotografia é gente de verdade, tratada com o filtro azul.** Sempre pessoas reais em contexto de trabalho (nunca olhando pra câmera), sempre com o degradê institucional `#6EAFD5→#223564` por cima como filtro de cor.

Quando uma regra não cobrir um caso, decida pela opção mais **sóbria e industrial**: mais azul-marinho, menos cor solta, ângulos retos em vez de curvas.

## Colors

Ver paleta completa (institucional, neutra, 12 secundárias, paletas por submarca, com HEX/RGB/Pantone/CMYK) em [references/cores-e-tipografia.md](references/cores-e-tipografia.md). Resumo de uso:

- **Navy `#223564`** e **azul-claro `#6EAFD5`**: institucionais, predominantes sempre, em qualquer marca do grupo.
- **Preto e cinza `#9D9D9C`**: neutros, só apoio, nunca cor principal de uma peça.
- **12 secundárias**: ampliam a composição e sinalizam campanha/submarca. `#F8BE38` (amarelo) é **restrita**: só para casos especiais (ex. Setembro Amarelo), nunca uso livre.
- **Cor de identificação por submarca**: Aço Cearense = azul médio/petróleo; Sinobras = cinza/prata; Florestal = verde; Instituto = sem cor própria (usa institucional). Ao fazer peça de uma submarca específica, ela pode dominar até 60% da composição, mas o navy/azul-claro institucional nunca desaparece.

## Typography

- **Herokid** (display bold condensada/expandida): títulos de impacto, sinalização, campanhas. Fallback de protótipo: Big Shoulders Display.
- **Monstane Olstd** (script/manuscrita): só para 1-2 palavras-chave dentro de uma frase de campanha (ex. "gente", "constrói" na tagline). Nunca para blocos de texto inteiros. Fallback: Yellowtail/Sacramento.
- **Manrope** (sans-serif principal, Google Fonts): todo texto corrido, web, e obrigatória em comunicação de produto/selo de projeto. É a fonte mais segura pra qualquer protótipo, já que é gratuita e cobre 7 pesos.
- **Arial + Montserrat**: só quando as fontes institucionais não puderem ser usadas (Office, sistemas, e-mail).

Regra de composição: frase de campanha = sans-serif (Herokid ou Manrope) + script (Monstane Olstd) só na(s) palavra(s)-âncora. Texto institucional mais sóbrio = só Manrope, variando cor (azul vívido/navy) em vez de fonte.

## Layout

- **Módulo de grid**: maior lado da peça ÷ 40 (retangular comum) ou menor lado ÷ 14 (quadrada/muito alongada). Gutter = 2/3 do módulo. Colunas em múltiplos de 2.
- **Grafismo sangra**: o corte diagonal de cantos opostos (arredondado/reto) sempre ultrapassa a borda da peça, nunca fica "fechado" dentro dela.
- **Área de proteção do logo**: X = altura da letra "G" do wordmark, nos 4 lados. Ao parear com outra marca: 2X de vão entre elas, X/2 de módulo pra marca acompanhante, marca prioritária sempre mais à direita.

## Photography

Pessoas reais, nunca olhando pra câmera, foco seletivo, luz natural, "brasilidade". Filtro de cor institucional (`#6EAFD5→#223564`) por cima de toda foto oficial. Nunca banco de imagens genérico, nunca pose forçada. Ver [references/icones-texturas-fotografia.md](references/icones-texturas-fotografia.md) pro antes/depois e a lista completa do que evitar.

## Shapes & Grafismo

O corte diagonal de 2 cantos arredondados + 2 cantos retos (derivado do símbolo "K") é a assinatura gráfica da marca: usado pra dividir fotos em KVs, como moldura de textura hexagonal, e em qualquer peça que precise de dinamismo. Pode girar/espelhar/redimensionar, mas precisa sempre sangrar pra fora da peça.

Ícones: grid 24x24px, traço 1px, outline, cantos arredondados, uma cor só (nunca gradiente, nunca duas cores no mesmo ícone).

## Do's and Don'ts

**Do**
- Mantenha navy + azul-claro institucionais presentes em qualquer peça, de qualquer marca do grupo.
- Use fotografia real de gente trabalhando, tratada com o filtro azul institucional.
- Deixe o grafismo diagonal sangrar pra fora da composição.
- Ao citar produto específico, use os atributos do glossário oficial ([references/marca-e-verbal.md](references/marca-e-verbal.md)).
- Ao parear marcas do grupo, respeite a prioridade posicional (marca-mãe/protagonista sempre mais à direita, nunca menor que a acompanhante).

**Don't**
- Não use as cores neutras (preto/cinza) como cor principal de uma peça.
- Não use o amarelo restrito `#F8BE38` fora de campanhas especiais explicitamente aprovadas.
- Não distorça, gire, aplique gradiente/sombra ou recolora o logo (são 8 proibições explícitas, ver [references/logo-e-submarcas.md](references/logo-e-submarcas.md)).
- Não deixe um ícone com mais de uma cor, gradiente, ou fora do grid 24px/1px.
- Não use travessão (—) em texto algum, nem palavras da lista de proibidas ("único", "premium", "designer", "artesanal", etc. — ver [references/marca-e-verbal.md](references/marca-e-verbal.md)).
- Não invente cor própria para o Instituto Aço Cearense nem identidade visual para "Rede OCA"/"WMA": não estão documentadas, confirme com o cliente antes.
