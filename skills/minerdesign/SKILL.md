---
name: minerdesign
description: Aplica a identidade visual da Miner (paleta Hudson/Soho/Brooklyn, fontes VisbyCF e Behind The Nineties, dark UI editorial, um único acento azul) a QUALQUER material visual: apresentações, decks, propostas, relatórios E TAMBÉM interfaces web, apps, portais, dashboards e landing pages, SEM alterar conteúdo, dados ou números. Tem um DESIGN.md portátil no padrão do Google (colável em v0/Cursor/Lovable, referenciável via AGENTS.md nos repos). Use SEMPRE que o Gustavo pedir pra aplicar o design da Miner, "minerizar", "deixar com a cara da Miner", estilizar ou redesenhar material, montar a UI/tema de um portal ou app, e também ao CRIAR do zero apresentação, proposta, página, portal ou tela em nome da Miner, mesmo que ele não cite a skill. Se o material é da Miner e é visual, passe por aqui.
---

# minerdesign

Aplica o design da Miner a qualquer material visual. O trabalho é de pele, não de órgão: o conteúdo que já existe (textos, números, valores, ordem das seções, dados de tabelas) permanece intacto. Se durante o trabalho um erro de conteúdo aparecer, reporte ao Gustavo e não corrija por conta própria.

## Qual caminho seguir

Antes de qualquer coisa, decida o tipo de material. Os tokens da marca são os mesmos nos dois; o que muda é o pipeline.

- **Deck, slide, proposta, relatório em PDF** (material de leitura, 16:9): pipeline de slides. Parta de `assets/slides-skeleton.html` e monte com [references/recipes.md](references/recipes.md) (fontes/imagens/ícones em base64, arquivo único, verificação e PDF).
- **UI web, app, portal, dashboard, landing** (produto de tela): use [DESIGN.md](DESIGN.md) como fonte de tokens e `assets/web-starter.html` como vitrine de componentes prontos (botão, input, card, stat, badge, tabela, nav). Copie o tema e os componentes de lá. O `DESIGN.md` é **portátil**: cole em v0/Cursor/Lovable ou referencie via `AGENTS.md` num repo, que qualquer IA aplica a cara da Miner.
- **Precisa de inspiração de método** (densidade, ritmo editorial, força de headline, além do que o KV cobre): consulte [references/brand-references.md](references/brand-references.md). São referências de princípio (Apple, Google, Tesla, Nespresso, Ogilvy), nunca de identidade: o acento continua Hudson, o fundo continua escuro.

## Fonte da verdade

Os **tokens** (cores, tipografia, spacing, radius, componentes) são canônicos em [DESIGN.md](DESIGN.md). Os **assets físicos** (fontes reais, ícones oficiais, fotografia) vivem em `~/Documents/Miner- Base Visual - KV - ID VIsual/`. Puxe sempre de lá: não substitua por Google Fonts, emoji ou ícone de biblioteca quando o original existe. O inventário completo (caminhos exatos, mapa de ícones por tema, ponto focal de cada foto) está em [references/kv-assets.md](references/kv-assets.md): leia antes de escolher assets.

## O design system em uma tela

**Paleta**: Hudson `#4562FF` (azul, único acento), Soho `#CBCBCB`, Brooklyn `#AEAEAE`, fundo `#0A0A0B`, superfícies `#141417`/`#1B1B1F`, borda `#2A2A2F`. Verde `#7FD49A` só para "incluso/free/bônus"; vermelho `#E5484D` só para erro funcional. Nunca introduza outra cor de acento.

**Tipografia**: Behind The Nineties Bd (serif display) para o logo "Miner", números gigantes e lockups como "(Dados + Vendas)". VisbyCF para todo o resto: ExtraBold caixa alta para títulos, DemiBold para destaques, Regular/Light para corpo. Contraste agressivo: âncora grande (46 a 110px), corpo pequeno (12 a 16px).

**Composição** (vale para slide e para web):
1. Sem espaço morto. Grids esticam (`flex:1`). Painel vazio pede mais respiro tipográfico, não mais texto.
2. Profundidade por **borda**, não por sombra. Dark UI: camadas de superfície + borda de 1px. Sombra só para o que flutua (modal, dropdown, toast).
3. Fotos do KV têm letreiro, e o letreiro é o conteúdo. Nunca corte o texto da imagem.
4. Todo bloco só de texto ganha um elemento alusivo: ícone oficial, número gigante, gráfico SVG ou foto. A Miner é empresa de design; texto puro não representa a marca.
5. Sem travessão em texto algum, sem emoji em material profissional.

Detalhe e racional completos (as 8 seções, do "porquê" de cada decisão aos specs de componente) em [DESIGN.md](DESIGN.md).

## Como executar

1. Leia o material de origem inteiro antes de tocar em qualquer coisa e liste as seções pra garantir que nada será perdido na reestilização.
2. Escolha o caminho (deck ou web) e leia [references/kv-assets.md](references/kv-assets.md) pra casar fotos e ícones com o assunto.
3. **Deck:** parta de `assets/slides-skeleton.html` e siga o pipeline de [references/recipes.md](references/recipes.md). **Web:** copie tokens e componentes de [DESIGN.md](DESIGN.md) + `assets/web-starter.html`; embuta as fontes reais antes de publicar (o fallback é só pra protótipo).
4. Verifique visualmente antes de entregar: sirva num servidor estático e tire screenshots das telas críticas (capa, tabelas densas, telas com SVG, formulários). A receita, com os gotchas do sandbox e do preview, está em recipes.md. Estouro de altura em slide e input sem estado de foco são os defeitos mais comuns: confira.
5. Se o Gustavo quiser PDF, gere com Chrome headless (receita em recipes.md) e confira as páginas lendo o PDF.

## Referência viva

- Deck aprovado: `~/Documents/Claude/diamantes-proposta-slides.html` (18 slides, casa de obra em SVG, gráficos, chips de preço).
- UI web de referência: `assets/web-starter.html` (todos os componentes na linguagem Miner, verificado no navegador).
