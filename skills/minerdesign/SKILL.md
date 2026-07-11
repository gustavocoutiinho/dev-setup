---
name: minerdesign
description: Aplica a identidade visual da Miner (paleta Hudson/Soho/Brooklyn, fontes VisbyCF e Behind The Nineties, fotografia urbana com letreiros, ícones de linha à mão) a apresentações, decks, propostas, relatórios, páginas HTML, portais e PDFs, SEM alterar conteúdo, dados ou números. Use SEMPRE que o Gustavo pedir pra aplicar o design da Miner, "minerizar", "deixar com a cara da Miner", estilizar ou redesenhar qualquer material, e também ao CRIAR do zero apresentação, proposta ou página em nome da Miner, mesmo que ele não cite a skill. Se o material é da Miner e é visual, passe por aqui.
---

# minerdesign

Aplica o design da Miner a qualquer material visual. O trabalho é de pele, não de órgão: o conteúdo que já existe (textos, números, valores, ordem das seções, dados de tabelas) permanece intacto. Se durante o trabalho um erro de conteúdo aparecer, reporte ao Gustavo e não corrija por conta própria.

## Fonte da verdade

Todos os assets vivem em `~/Documents/Miner- Base Visual - KV - ID VIsual/`. Puxe sempre de lá: fontes reais, ícones oficiais e fotografia da marca. Não substitua por Google Fonts, emoji ou ícone de biblioteca quando o original existe. O inventário completo (caminhos exatos, mapa de ícones por tema, ponto focal de cada foto) está em [references/kv-assets.md](references/kv-assets.md): leia antes de escolher assets.

## O design system em uma tela

**Paleta** (nomes oficiais): Hudson `#4562FF` (azul, único acento), Soho `#CBCBCB` (cinza claro, fundo de chips de ícone), Brooklyn `#AEAEAE` (cinza médio), preto `#0A0A0B` de fundo, painéis `#141417`, bordas `#2A2A2F`. Verde `#7FD49A` só para "incluso/free/bônus". Nunca introduza outra cor de acento.

**Tipografia**: Behind The Nineties Bd (serif display) para o logo "Miner", números gigantes e lockups como "(Dados + Vendas)". VisbyCF para todo o resto: ExtraBold em caixa alta para títulos e headers, DemiBold para destaques, Regular/Light para corpo. Hierarquia agressiva: número ou título âncora grande (46 a 110px), corpo pequeno (12 a 15px), muito contraste entre os dois.

**Componentes recorrentes** (todos prontos no esqueleto em `assets/slides-skeleton.html`):
- Header band: chip numerado com borda azul + título caps + subtítulo discreto + "Miner ▲" serif à direita
- Painéis escuros com bullets de seta azul (`→`) e leads em bold branco
- Chips de ícone: PNG oficial azul sobre quadrado Soho arredondado
- Stat cards com filete azul lateral e número serif gigante
- Faixas: azul para condição/preço, verde para incluso, azul-escuro com borda pra citações e gaps
- Fechos da marca: "It's ready?", "(Dados + Vendas)", "It's all in data"

**Regras de composição**:
1. Slides 16:9 sempre cheios: sem espaço morto no rodapé, grids esticando com `flex:1`. Se um painel ficou vazio, o conteúdo precisa de mais respiro tipográfico, não de mais texto.
2. Fotos do KV têm letreiro, e o letreiro é o conteúdo da foto. Nunca corte o texto da imagem: use painéis laterais de altura cheia com `background-position` calculado pro letreiro aparecer inteiro. Nada de faixas horizontais baixas que decapitam a mensagem.
3. Todo slide só de texto recebe pelo menos um elemento alusivo: ícone oficial, gráfico SVG inline (barras, curvas, funil, diagrama), número gigante ou foto. A Miner é uma empresa de design; texto puro não representa a marca.
4. Sem travessão em texto algum, sem emoji em material profissional (regras de escrita do Gustavo valem para qualquer texto que a estilização obrigar a tocar).

## Como executar

1. Leia o material de origem inteiro antes de tocar em qualquer coisa e liste as seções pra garantir que nada será perdido na reestilização.
2. Leia [references/kv-assets.md](references/kv-assets.md) e escolha fotos e ícones que conversem com o assunto de cada tela ou seção.
3. Parta do esqueleto `assets/slides-skeleton.html` (CSS completo do design system, com tokens `%%...%%` para os assets). Para páginas longas (não slides), reaproveite os mesmos tokens de cor, tipografia e componentes adaptando o layout.
4. Monte com o pipeline de [references/recipes.md](references/recipes.md): preparar imagens com sips, embutir fontes/imagens/ícones em base64 via script Python de tokens, gerar arquivo único autocontido.
5. Verifique visualmente antes de entregar: sirva com o servidor estático do launch.json e tire screenshots dos slides críticos (capa, tabelas, telas com SVG). A receita, com os gotchas do sandbox, está em recipes.md. Estouro de altura em slide é o defeito mais comum: confira.
6. Se o Gustavo quiser PDF, gere com Chrome headless (receita em recipes.md) e confira as páginas lendo o PDF.

## Referência viva

Exemplo completo e aprovado deste design aplicado: `~/Documents/Claude/diamantes-proposta-slides.html` (18 slides, com casa de obra em SVG, gráficos, chips de preço). Template fonte com tokens da última versão: procure `slides-template.html` no scratchpad da sessão que o gerou, ou use o esqueleto desta skill.
