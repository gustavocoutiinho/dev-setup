---
name: festivaldesign
description: Aplica a identidade visual do Festival Costume Gourmet (fundos vinho/oliva/creme, acentos dourado/laranja/telha/coral/musgo, serif display Playfair + Montserrat em caixa alta, molduras vintage com sparkle, ícones de gravura de gastronomia, carimbo do festival, selo 100 anos São Luiz) a qualquer material do evento, SEM alterar conteúdo, dados ou números. Use SEMPRE que o Gustavo pedir arte, post, feed, story, card, convite, save the date, cardápio, programação, banner, página ou deck do Festival Costume Gourmet (FCG) ou do São Luiz Supermercado, pedir pra "deixar com a cara do Festival", "minerizar o festival", estilizar ou criar do zero material do evento, mesmo que não cite a skill. Se é do Festival Costume Gourmet e é visual, passe por aqui.
---

# festivaldesign

Aplica o design do Festival Costume Gourmet a qualquer material visual do evento. O trabalho é de pele, não de órgão: o conteúdo que já existe (textos, datas, nomes de chefs, programação, valores) permanece intacto. Se durante o trabalho um erro de conteúdo aparecer, reporte ao Gustavo e não corrija por conta própria.

Contexto do evento: Festival Costume Gourmet, apresentado pelo **São Luiz Supermercado** (que celebra 100 anos). Cliente Miner é o Grupo São Luiz (MSLZ). É um festival de gastronomia com chefs, degustações, atrações e marcas. A skill é irmã da `minerdesign`, mas com um design system próprio: quente, gastronômico, vintage-elegante, multicolor, em formato de peça social vertical (não o preto+azul sóbrio da Miner). Ver contexto do projeto em `~/ObsidianVaults/miner/memory/project_festival_costume_gourmet.md`.

## Fonte da verdade

A IDV oficial nasceu no Canva (PDF `Cópia de FCG 2026 - IDV Canva FEED.pdf`). Os assets reais (logo do festival, logo São Luiz, selo 100 anos, carimbo, ícones de gravura, ilustrações de mesa posta, ondas, pattern) foram extraídos desse PDF e vivem em `assets/img/` desta skill, já com transparência. As duas fontes são **Google Fonts** que reproduzem fielmente a arte do Canva: **Playfair Display** (serif display) e **Montserrat** (sans em caixa alta). O inventário completo (cada asset, quando usar, a paleta com hex exatos, o par tipográfico) está em [references/idv-assets.md](references/idv-assets.md): leia antes de escolher assets e cores.

## O design system em uma tela

**Três mundos de fundo** (a peça sempre nasce em um deles): **Vinho** `#3A0F0E` (a cor-assinatura, gradiente radial pra `#4E1714`), **Oliva** `#26260A` (variação, mesma diagramação em verde-escuro → `#4A4A22`), **Creme** `#FCF6EE` (fundo claro, pras frases de tipografia pura).

**Acentos quentes** (o coração multicolor da marca, intercambiáveis): Dourado/Âmbar `#D8992F`, Laranja `#D2742E`, Telha `#DC463C`, Coral `#C25D50`, Musgo `#A0A04E`. Apoios: Marrom `#6E3C16`, Bordô `#5A1414`, Nude `#D3A281`. Neutros: creme texto `#FCF6EE`, grafite (texto sobre creme) `#4A4744`. Nunca use uma cor de acento sozinha num título: a assinatura é alternar.

**Tipografia**: **Playfair Display** (serif, alto contraste) para os títulos-âncora gigantes coloridos, palavras de destaque, números e o "save the date" (em italic). **Montserrat** ExtraBold/SemiBold em CAIXA ALTA com letter-spacing para rótulos, subtítulos e o corpo (SABORES, DE SETEMBRO, SUPERMERCADO). Hierarquia agressiva: âncora serif enorme (80 a 160px numa peça de 1080) contra rótulo sans pequeno e espaçado (16 a 32px).

**Componentes recorrentes** (todos prontos no esqueleto em `assets/slides` → `assets/festival-skeleton.html`):
- Moldura de linha fina dupla com cantos chanfrados + sparkle (estrela de 4 pontas) dourado no canto: a "carteira" vintage que envolve quase toda peça (SVG, recriada, não bitmap)
- Título empilhado alternando fonte e cor linha a linha ("SABORES / de uma bela / história")
- Co-branding de rodapé: logo do Festival + logo São Luiz + selo 100 anos (o evento é dos 100 anos do São Luiz; os três costumam aparecer juntos)
- Card de foto em duotone (foto tingida na cor do fundo) com moldura interna arredondada e título por cima
- Card de atração/chef: retrato em moldura arredondada de borda dourada + nome serif + sobrenome sans caps
- Chip de ícone de gravura (café, vinho, queijo, cogumelo, ramo, alho, saca-rolha…) e carimbo circular do festival como selo decorativo
- Ilustração de mesa posta / ramo como textura de fundo tom-sobre-tom em baixa opacidade

**Regras de composição**:
1. Toda peça nasce num dos três mundos (Vinho, Oliva ou Creme) e carrega a moldura + sparkle. Vinho é o default; ofereça a versão Oliva quando fizer sentido variar (as duas convivem na campanha).
2. Co-branding é obrigatório: o Festival não aparece sozinho. Traga logo do Festival, logo São Luiz e o selo 100 anos (pelo menos dois dos três, tipicamente FCG no topo + São Luiz/selo no rodapé).
3. Título sempre quebrado em linhas com alternância de fonte e cor (serif colorido gigante ↔ sans caps neutro). Uma palavra-âncora recebe o maior tamanho e a cor mais forte.
4. Fotos entram em duotone na cor do mundo (vinho ou oliva) com leve escurecimento, para o texto respirar por cima. Nunca foto crua colorida sob texto.
5. Formatos: feed 4:5 (1080×1350) é o padrão; stories 9:16 (1080×1920), quadrado 1:1 (1080×1080) e, quando o material for maior (convite, cardápio, página, deck), reaproveite os mesmos tokens de cor/tipografia/moldura adaptando o layout.
6. Sem travessão em texto algum, sem emoji em peça oficial (regras de escrita do Gustavo valem para qualquer texto que a estilização obrigue a tocar).

## Como executar

1. Leia o material de origem inteiro antes de tocar em qualquer coisa e liste as seções/peças pra garantir que nada será perdido na reestilização. Se for criar do zero, confirme com o Gustavo o texto e o formato (feed, story, card, convite…).
2. Leia [references/idv-assets.md](references/idv-assets.md) e escolha o mundo (Vinho/Oliva/Creme), os acentos e os ícones/ilustrações que conversem com o assunto da peça.
3. Parta do esqueleto `assets/festival-skeleton.html` (CSS completo do design system + um exemplo de cada componente e formato, com tokens `%%...%%` para fontes e imagens). Para material longo (página, cardápio, deck), reaproveite os tokens adaptando o layout.
4. Monte com o pipeline de [references/recipes.md](references/recipes.md): preparar imagens, embutir fontes (Playfair/Montserrat) e assets em base64 via script Python de tokens, gerar arquivo único autocontido.
5. Verifique visualmente antes de entregar: sirva no servidor estático e tire screenshots das peças críticas. Confira co-branding presente, moldura sem corte, título com alternância de cor, e (em card de foto) o duotone e a legibilidade do texto.
6. Se o Gustavo quiser PNG/JPG por peça (é o mais comum, é social) ou PDF, exporte com Chrome headless (receita em recipes.md) e confira lendo o resultado.

## Referência viva

O PDF fonte da IDV é `~/Documents/Cópia de FCG 2026 - IDV Canva FEED.pdf` (28 peças: capas, save the date, frases, cards de foto, atração confirmada, elementos). Quando bater dúvida de como um componente aparece na marca, olhe lá. Assets e paleta foram extraídos exatamente desse arquivo.
