---
version: 1.0
name: OCA lab Design System
description: >
  Identidade visual do OCA lab (rebranding da Rede OCA), laboratório de inovação do
  Grupo Aço Cearense. Filha da identidade do grupo: azuis institucionais navy + azul-claro,
  wordmark OCA derivado do anagrama de "ACO" na tipografia do logotipo do grupo, gradiente
  como assinatura, apoios verde-água e coral, universo tech-industrial (metal, hexágono, neon).
  Fonte de tokens para deck, KV, post, papelaria, brinde e web. Para o pipeline completo
  (fontes, imagens, verificação) use a skill ocadesign.
---

# ---- Design tokens (machine-readable) ----
colors:
  navy:        "#223564"   # institucional (herdado do Grupo Aço Cearense), ponta escura do gradiente
  light-blue:  "#6EAFD5"   # institucional (herdado do grupo), ponta clara do gradiente
  teal:        "#55C0B3"   # cor de apoio "análoga". R85 G192 B179 / Pantone 3258 C / CMYK 63,0,37,0
  coral:       "#FF5C60"   # cor de apoio "complementar". R255 G92 B96 / Pantone 184 C / CMYK 0,76,51,0
  white:       "#FFFFFF"
  gradient-primario: "linear-gradient(90deg, #6EAFD5, #223564)"   # A assinatura da marca: claro -> escuro, sentido da leitura
  gradient-teal:     "linear-gradient(90deg, #223564, #55C0B3)"   # variação de apoio (patterns, fundos)
  # Derivados (NÃO constam no doc; use só para fundo escuro de aplicação, nunca no logo):
  derived-dark: "#101A32"  # navy escurecido para fundos tipo wallpaper/letreiro; o doc usa fundos escuros sem hex documentado

typography:
  primary:  { fontFamily: "Eurostile", fallback: "'Oxanium', 'Michroma', sans-serif", note: "títulos e corpo; títulos em caixa alta" }
  display:  { fontFamily: "Herokid", fallback: "'Big Shoulders Display', 'Anton', sans-serif", fontWeight: 800, textTransform: "uppercase", note: "impacto/campanha, mesma display do grupo" }
  title-styles: "2 pares aprovados: itálico caixa alta + corpo itálico, ou bold caixa alta + corpo regular"

logo:
  wordmark: "OCA em caixa alta + sufixo 'lab' minúsculo, encaixado à direita do pé diagonal do A"
  construcao: "OCA = anagrama de ACO, desenhado na tipografia do logotipo do Grupo Aço Cearense; o A tem corte diagonal herdado do símbolo K do grupo e um pé que desce abaixo da baseline"
  versoes:
    padrao:      "wordmark com gradient-primario (claro na esquerda, navy na direita) + 'lab' em light-blue sólido; usar sobre branco/claro"
    mono:        "tudo navy #223564, sobre fundos claros quando o gradiente não render"
    negativo:    "tudo branco sobre caixa/fundo navy"
    linear:      "outline (contorno), uso pontual"
    secundarias: "monocromática teal #55C0B3 ou coral #FF5C60, para brindes/materiais de apoio"
    branca:      "branco puro sobre fotografia ou fundo escuro (aplicações)"
  nao-documentado: "área de proteção, tamanho mínimo e lista de usos indevidos NÃO constam na apresentação; na dúvida, aplique as regras do grupo (skill accsdesign): respiro generoso, nunca distorcer/rotacionar/recolorir"

components:
  co-branding:
    layout: "OCA lab à esquerda + marca do grupo (Grupo Aço Cearense, SINOBRAS ou Aço Cearense) à direita, ambas na mesma altura óptica"
    regra: "a marca endossante institucional fica à direita (mesma lógica de prioridade posicional do grupo)"
  kv:
    layout: "colagem de fotos em molduras de paralelogramo/facetas diagonais à esquerda + área branca com logo grande em gradiente à direita"
    rodape: "pílula com URL (grupoacocearense.com.br) + logo Grupo Aço Cearense, mesma estrutura do KV do grupo"
    fotos: "indústria/aço + tecnologia + pessoas, com wash azul"
  pattern-logo:
    style: "logo 'OCA lab' repetido em grade, outline tom sobre tom (navy translúcido), sobre gradient-primario ou gradient-teal"
  pattern-letras:
    style: "letras OCA gigantes cropadas (sangrando pra fora), tom sobre tom, sobre gradiente azul ou azul->coral"
  fundo-aplicacao:
    style: "azul profundo/metal escuro com luz neon ciano; logo branco por cima"
---

## Overview

O **OCA lab** é o laboratório de inovação do Grupo Aço Cearense (rebranding da "Rede OCA", aprovado em janeiro/2026). Nasceu como espaço de testes digitais e virou hub estratégico do grupo; os pares de referência são Cubo Itaú, Açolab (ArcelorMittal) e LuizaLabs (Magalu). Valores: **inovação, colaboração, agilidade, coragem**. A identidade é "moderna com identidade do grupo": tecnologia e futuro, mas sempre reconhecível como filha do Grupo Aço Cearense.

Três decisões fundam tudo:

1. **Filha do grupo, sem disfarce.** O nome OCA é o anagrama de "ACO"; o wordmark usa a tipografia do logotipo do grupo e o A carrega o corte diagonal do símbolo "K". As cores-mãe são os mesmos azuis institucionais do grupo (navy `#223564` + azul-claro `#6EAFD5`).
2. **O gradiente é a assinatura.** Enquanto o grupo usa os azuis chapados, o OCA se diferencia pelo degradê `#6EAFD5 -> #223564` (claro à esquerda, escuro à direita) no logo, nos fundos e nos patterns.
3. **Universo tech-industrial.** Superfícies metálicas, malhas hexagonais, neon ciano, hologramas, fotografia com wash azul. O aço do grupo continua presente, mas visto pela lente da tecnologia.

Quando uma regra não cobrir um caso, decida pela opção mais próxima do grupo: mais azul, mais geometria, menos cor solta. Verde-água e coral são apoio, nunca protagonistas de peça institucional.

## Colors

- **Navy `#223564`** e **azul-claro `#6EAFD5`**: base institucional herdada do grupo. O gradiente entre os dois é a marca registrada do OCA.
- **Verde-água `#55C0B3`** (análoga) e **coral `#FF5C60`** (complementar): cores de apoio oficiais. Aparecem em versões secundárias do logo, brindes (caneca, caderno, gola de uniforme), detalhes e patterns. Nunca substituem o azul em peça institucional.
- Ambas as cores de apoio já pertencem à paleta secundária do Grupo Aço Cearense (turquesa e coral), o que mantém o OCA dentro do sistema do grupo.
- Fundos escuros de aplicação (wallpaper, letreiro, telas): azul profundo/metal sem hex documentado; derive do navy (ex. `#101A32`) e sinalize como derivado.

## Typography

- **Eurostile** (principal): títulos e corpo. Títulos em caixa alta, nos 2 pares aprovados (itálico ou bold). Fonte licenciada; em protótipo use Oxanium (corpo, vários pesos) ou Michroma (títulos curtos, efeito Extended) e avise que é fallback.
- **Herokid** (display): impacto e campanha, a mesma display do grupo. Fallback de protótipo: Big Shoulders Display/Anton.

## Logo

Versões e regra de fundo na tabela de tokens acima. Resumo de decisão: fundo branco/claro = padrão em gradiente; fundo navy/escuro/foto = branco (ou negativo em caixa navy); brinde/material de apoio = pode usar secundária teal ou coral monocromática; documento sóbrio = mono navy. A apresentação NÃO define área de proteção nem tamanho mínimo: use o bom senso das regras do grupo (accsdesign) e nunca distorça, rotacione ou recolora fora das versões listadas.

## Patterns & KV

- **Pattern de logo**: "OCA lab" repetido em grade, outline tom sobre tom, sobre o gradiente (azul ou azul->verde-água). Usado em envelope, caneca, fundos.
- **Pattern de letras cropadas**: as letras OCA gigantes, cortadas pelas bordas (sangrando), tom sobre tom sobre gradiente. Versão azul e versão azul->coral.
- **KV oficial**: colagem de fotos (aço, indústria, tecnologia, pessoas) em molduras de paralelogramo à esquerda, logo grande em gradiente sobre área branca à direita, rodapé com pílula de URL + logo do Grupo Aço Cearense.

## Do's and Don'ts

**Do**
- Use o gradiente `#6EAFD5 -> #223564` como elemento identitário número 1.
- Mantenha o vínculo visível com o grupo: azuis institucionais, co-branding com a marca do grupo à direita, corte do K no A.
- Use verde-água/coral como acento (gola, brinde, detalhe, pattern), sempre com o azul presente na peça.
- Sobre foto ou fundo escuro, use o logo branco.
- Fotografia com wash azul, misturando indústria/aço e tecnologia/pessoas.

**Don't**
- Não use o logo antigo da Rede OCA (corrente rosa/roxa com casinha): foi substituído no rebranding.
- Não inverta o sentido do gradiente no logo padrão (claro fica à esquerda, navy à direita).
- Não faça peça institucional dominada por verde-água ou coral; são apoio.
- Não misture a identidade do OCA com a paleta/tipografia da Miner ou de outro cliente.
- Não invente área de proteção, ícone isolado ou submarca do OCA: o doc não define; confirme com o cliente antes.
