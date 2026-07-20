---
version: 1.0
name: Miner Design System
description: >
  Identidade visual da Miner (MinerBZ), agência de dados e vendas. Dark UI editorial,
  um único acento azul (Hudson), tipografia com contraste agressivo entre serif display
  e sans geométrica. Fonte única de tokens para UI web, app, portal, dashboard e landing.
  Para deck/slide use o pipeline da skill minerdesign (assets/slides-skeleton.html).

# ---- Design tokens (machine-readable) ----
colors:
  background:        "#0A0A0B"   # fundo padrao de todo produto
  surface:           "#141417"   # cards, paineis, inputs
  surface-2:         "#1B1B1F"   # cabecalho de tabela, camada acima da surface
  border:            "#2A2A2F"   # borda de 1px, o separador padrao (profundidade vem daqui, nao de sombra)
  primary:           "#4562FF"   # Hudson, o UNICO acento da marca
  primary-soft:      "rgba(69,98,255,0.14)"  # fundo de chip/badge/estado ativo em azul
  on-primary:        "#FFFFFF"
  text:              "#F4F4F2"   # titulos e texto de alto contraste
  text-body:         "#C6C6C4"   # corpo
  text-muted:        "#87878A"   # legenda, meta, fonte de dado
  neutral-soho:      "#CBCBCB"   # cinza claro, fundo de chip de icone
  neutral-brooklyn:  "#AEAEAE"   # cinza medio, apoio sobre escuro
  success:           "#7FD49A"   # EXCLUSIVO de incluso/free/bonus, nunca decorativo
  danger:            "#E5484D"   # funcional, so feedback de erro em form/toast

typography:
  display:   { fontFamily: "Behind The Nineties", fontSize: "72px", fontWeight: 700, lineHeight: 1.0 }
  h1:        { fontFamily: "Visby CF", fontSize: "40px", fontWeight: 800, lineHeight: 1.05, letterSpacing: "0.2px" }
  h2:        { fontFamily: "Visby CF", fontSize: "28px", fontWeight: 800, lineHeight: 1.1, letterSpacing: "0.6px", textTransform: "uppercase" }
  h3:        { fontFamily: "Visby CF", fontSize: "20px", fontWeight: 800, lineHeight: 1.15, letterSpacing: "0.6px", textTransform: "uppercase" }
  body-lg:   { fontFamily: "Visby CF", fontSize: "16px", fontWeight: 400, lineHeight: 1.6 }
  body:      { fontFamily: "Visby CF", fontSize: "14px", fontWeight: 400, lineHeight: 1.55 }
  label:     { fontFamily: "Visby CF", fontSize: "13px", fontWeight: 600, lineHeight: 1.4 }
  caption:   { fontFamily: "Visby CF", fontSize: "12px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "1px", textTransform: "uppercase" }
  micro:     { fontFamily: "Visby CF", fontSize: "10px", fontWeight: 800, lineHeight: 1.3, letterSpacing: "1.5px", textTransform: "uppercase" }

spacing:   # base 4
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  2xl: "32px"
  3xl: "48px"
  4xl: "64px"

rounded:
  sm:   "10px"
  md:   "12px"
  lg:   "16px"
  xl:   "18px"
  pill: "999px"

elevation:
  flat:    "none"                                  # o padrao: profundidade por borda, nao por sombra
  overlay: "0 12px 40px rgba(0,0,0,0.55)"          # so para modal, dropdown, toast

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor:       "{colors.on-primary}"
    radius:          "{rounded.md}"
    fontWeight:      "800"
    padding:         "12px 20px"
  button-secondary:
    backgroundColor: "transparent"
    textColor:       "{colors.text}"
    border:          "1px solid {colors.border}"
    radius:          "{rounded.md}"
    fontWeight:      "600"
    padding:         "12px 20px"
  input:
    backgroundColor: "{colors.surface}"
    textColor:       "{colors.text}"
    placeholderColor: "{colors.text-muted}"
    border:          "1px solid {colors.border}"
    focusBorder:     "1px solid {colors.primary}"
    radius:          "{rounded.md}"
    padding:         "12px 14px"
  card:
    backgroundColor: "{colors.surface}"
    border:          "1px solid {colors.border}"
    radius:          "{rounded.xl}"
    padding:         "24px"
  stat-card:
    backgroundColor: "{colors.surface}"
    border:          "1px solid {colors.border}"
    radius:          "{rounded.lg}"
    accentBar:       "4px solid {colors.primary}"   # filete azul na lateral esquerda
    valueFont:       "Behind The Nineties"
  badge:
    backgroundColor: "{colors.primary-soft}"
    textColor:       "{colors.text}"
    border:          "1px solid {colors.primary}"
    radius:          "{rounded.pill}"
    textTransform:   "uppercase"
  badge-success:
    backgroundColor: "transparent"
    textColor:       "{colors.success}"
    border:          "1px solid {colors.success}"
    radius:          "{rounded.pill}"
  table-header:
    backgroundColor: "{colors.surface-2}"
    textColor:       "{colors.text-muted}"
    textTransform:   "uppercase"
    fontWeight:      "800"
---

## Overview

A Miner é uma agência de **dados e vendas** ("(Dados + Vendas)"). A interface tem que parecer o que a empresa vende: precisão, inteligência e resultado, sem ruído. A sensação é de **produto de dados premium**: escuro, editorial, confiante, denso onde precisa e arejado onde respira. Nunca infantil, nunca cheio de cor, nunca genérico de template.

Três decisões fundam tudo:

1. **Fundo escuro sempre.** O produto vive sobre preto `#0A0A0B`. Claridade vem da tipografia e de um único azul, não de fundos claros.
2. **Um acento só.** Hudson `#4562FF` é a única cor de marca. Ela marca o que importa (ação, número-âncora, destaque) e por ser única, tem força. Verde entra só para "incluso/bônus"; vermelho só para erro funcional.
3. **Contraste tipográfico agressivo.** Um número ou título gigante em serif display ao lado de corpo pequeno. O olho salta direto para o que vale. Cinza no meio-termo não existe: ou é âncora, ou é apoio.

Quando uma regra não cobrir um caso, decida pela opção mais **sóbria e contrastada**: menos cor, mais espaço, hierarquia mais dura.

## Colors

Paleta com nomes oficiais da marca (bairros de NY):

- **Hudson `#4562FF`** é o acento único. Botão primário, link, foco, filete de stat, `→` de bullet, destaque de título. Se algo precisa gritar "clique aqui" ou "olhe este número", é Hudson. Não introduza segundo acento.
- **Fundos em camadas:** `background #0A0A0B` (base) → `surface #141417` (card/input) → `surface-2 #1B1B1F` (cabeçalho de tabela). A profundidade é essa escada de cinza-quase-preto, reforçada por `border #2A2A2F` de 1px.
- **Texto em três níveis:** `text #F4F4F2` (título), `text-body #C6C6C4` (corpo), `text-muted #87878A` (legenda, fonte de dado, meta). Sempre respeite os três níveis: tudo no mesmo tom achata a leitura.
- **Verde `#7FD49A`** é reservado. Só aparece para sinalizar "sem custo / incluso / bônus". Usar verde como decoração quebra a semântica da marca.
- **Vermelho `#E5484D`** é funcional e raro: validação de formulário, toast de erro. Nunca decorativo.
- **Soho `#CBCBCB`** é o fundo dos chips de ícone (ícone azul sobre quadrado claro arredondado). **Brooklyn `#AEAEAE`** é apoio de texto sobre escuro.

## Typography

Duas famílias, papéis que não se misturam:

- **Behind The Nineties** (serif display, weight 700): é a voz da marca. Usar em: logo "Miner", números-âncora gigantes, hero de capa, valores de preço em destaque, lockups como "(Dados + Vendas)". É pontuação, não corpo: aparece pouco e grande.
- **Visby CF** (sans geométrica): faz todo o resto. ExtraBold (800) em **caixa alta com letter-spacing** para títulos e cabeçalhos; DemiBold (600) para leads e labels; Regular/Light (400/300) para corpo. Nunca use a serif para texto corrido nem a sans para o número-herói.

**Hierarquia é por tamanho, não por cor.** Um `display` de 72px e um `body` de 14px na mesma tela é o normal, não o exagero. Títulos de seção vão em `h2`/`h3` caixa alta. Legendas e fontes de dado em `micro`/`caption` caixa alta com tracking, sempre em `text-muted`.

**Fontes proprietárias.** Visby CF e Behind The Nineties são licenciadas e vivem no KV (`references/kv-assets.md`). Em **material oficial** (proposta, deck, site publicado) são obrigatórias, embutidas em base64/woff2. Em **protótipo numa ferramenta sem a licença** (v0, Lovable), use o fallback e troque a fonte antes de publicar: sans → `"Geist", "Inter", system-ui`; serif display → `"Playfair Display", Georgia, serif` (aproximação; a real tem serifas mais encorpadas).

## Layout

- **Espaçamento em base 4** (`spacing`): respiro entre blocos em `xl`/`2xl` (24/32), padding interno de card em `xl` (24), gaps de grid em `lg` (16). Consistência de ritmo importa mais que valores "perfeitos".
- **Densidade dupla.** Áreas de dado (tabela, dashboard, stat grid) podem ser densas; áreas de mensagem (hero, statement, CTA) precisam de muito ar. A mesma tela alterna as duas.
- **Sem espaço morto.** Grids esticam para preencher (`flex:1`); se sobrou vazio, aumente o respiro tipográfico do conteúdo, não adicione texto de enchimento.
- **Largura de leitura:** corpo longo no máximo ~70ch. Hero e statement podem ocupar largura cheia.
- **Alinhamento à esquerda** como padrão; centralizado só em fecho/capa curtos.

## Elevation & Depth

Dark UI: profundidade vem de **borda + camada de superfície**, não de sombra. Um card é `surface` sobre `background` com `border` de 1px, e pronto. Não empilhe drop-shadows: isso suja o preto e parece template claro invertido.

Sombra só existe para elementos que **flutuam sobre o conteúdo**: modal, dropdown, toast, popover, usando `elevation.overlay`. Estado de foco/hover se resolve com a borda virando Hudson ou com um leve `primary-soft` de fundo, não com sombra.

## Shapes

Cantos arredondados, escala `rounded`: chips e botões em `sm`/`md` (10/12), cards e painéis em `lg`/`xl` (16/18), pills e avatares em `pill` (999). Nada de canto vivo (0px) nem de raio exagerado que vire "bolha". O filete de acento (barra de 4px Hudson na lateral do stat-card) é uma assinatura da marca: use em números que merecem peso.

Ícones são de **linha desenhada à mão** (KV, azul Hudson), não ícones de biblioteca genérica. Sobre fundo escuro, versão branca via `filter: brightness(0) invert(1)`. O `→` (seta) é o marcador de bullet padrão, sempre em Hudson.

## Components

Specs completas e prontas para copiar em **`assets/web-starter.html`** (o equivalente web do slides-skeleton). Resumo:

- **Botão primário:** fundo Hudson, texto branco, `rounded.md`, DemiBold/ExtraBold. **Secundário:** transparente + borda, texto claro. **Ghost:** só texto Hudson.
- **Input/select/textarea:** fundo `surface`, borda 1px, **foco = borda Hudson**, placeholder `text-muted`, `rounded.md`.
- **Card:** `surface` + borda + `rounded.xl`, padding `xl`. **Stat-card:** card + filete Hudson de 4px + número em serif gigante.
- **Badge/pill:** `micro` caixa alta; variante azul (borda Hudson + `primary-soft`) e variante `success` (verde, só incluso).
- **Tabela:** `th` caixa alta `text-muted` sobre `surface-2`; `td` sobre `surface` com `border-top`; primeira coluna em `text`.
- **Topbar/nav:** faixa com `border-bottom`, itens em `label`, lockup "Miner ▲" (serif + triângulo Hudson) à direita.
- **Bullet:** lista sem marcador, `→` Hudson absoluto à esquerda, lead do item em `text` bold.

## Do's and Don'ts

**Do**
- Use Hudson com parcimônia: quanto mais raro, mais forte.
- Deixe um número ou título respirar grande em serif. A Miner é dados; o dado é o herói visual.
- Mantenha os três níveis de texto (título/corpo/muted) sempre distintos.
- Cite a fonte de todo dado, em `micro` `text-muted`.
- Troque a fonte de fallback pela oficial antes de qualquer publicação.

**Don't**
- Não introduza um segundo acento nem gradientes coloridos. Verde e vermelho têm função fixa.
- Não use fundo claro. O produto é escuro.
- Não empilhe sombras nem use ícones de biblioteca genérica no lugar dos do KV.
- Não use travessão (—) em texto algum, nem emoji em material profissional.
- Não deixe espaço morto no rodapé nem grids sem esticar.
- Nunca importe a cor/tipografia das marcas de referência (`references/brand-references.md`): elas inspiram método, não a identidade. O acento é sempre Hudson.
