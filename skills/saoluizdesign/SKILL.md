---
name: saoluizdesign
description: Aplica a nova identidade visual do São Luiz Supermercado (marca-mãe do Grupo São Luiz/MSLZ, manual maio/2025) a QUALQUER material do cliente: post/story/feed, encarte, tabloide, banner, KV de campanha, papelaria, uniforme, embalagem, sacola, fachada, sinalização de loja, deck institucional, site, portal, e-commerce, painel de preço. Paleta creme+marrom+laranja, símbolo trevo-de-corações, tipografia Georgia (títulos) + Akzidenz Grotesk Next (texto) + League Gothic (sinalização), grafismos de silhueta de alimentos/utensílios. Tem DESIGN.md portátil com os tokens (colável em v0/Cursor/Lovable). Use SEMPRE que o Gustavo pedir material para São Luiz Supermercado / MSLZ / Grupo São Luiz na marca institucional (NÃO para o Festival Costume Gourmet — esse é o escopo da [[festivaldesign]]), pedir pra "deixar com a cara do São Luiz", estilizar ou criar do zero peça, papelaria, ambiente ou tela em nome do supermercado, mesmo que não cite a skill pelo nome. Se é do São Luiz Supermercado (marca institucional) e é visual, passe por aqui.
---

# saoluizdesign

Aplica o design da nova marca do **São Luiz Supermercado** (Grupo São Luiz, alias MSLZ, cliente Miner) a qualquer material visual em nome desse cliente. O trabalho é de pele, não de órgão: o conteúdo que já existe (textos, preços, ofertas, datas, número de loja) permanece intacto. Se durante o trabalho um erro de conteúdo aparecer, reporte ao Gustavo e não corrija por conta própria.

Esta skill é irmã da [[minerdesign]] (identidade da própria Miner), [[accsdesign]] (Grupo Aço Cearense) e [[festivaldesign]] (Festival Costume Gourmet), mas com design system próprio: quente, afetivo, gastronômico-popular, trevo-de-corações + serif Georgia + laranja assinado. Nunca misture com a paleta/tipografia da Miner ou de outro cliente.

## Escopo: quando NÃO usar

Esta skill é da **marca-mãe institucional** do supermercado (uso ano todo). Se o pedido é de material do **Festival Costume Gourmet** (evento sazonal apresentado pelo São Luiz), a skill correta é [[festivaldesign]] — ela tem paleta vinho/oliva/creme, molduras vintage, sparkle dourado e assets específicos do evento. Na dúvida, pergunte ao Gustavo qual dos dois universos. Diretriz-padrão sem confirmação: se a peça fala do evento (chef, degustação, programação, save the date), é festival; se fala do supermercado no dia a dia (oferta, delivery, uniforme, papelaria, campanha institucional, comunicado interno de loja), é saoluizdesign.

## Fonte da verdade

A IDV oficial nasceu no manual **"Nova Marca São Luiz 2025 — Manual de aplicação de marca | Maio 2025"** (20 páginas, PDF gerado no Adobe Illustrator, page size 1920×1080). Assets de referência visual (as próprias páginas do manual) vivem em [`assets/manual/`](assets/manual/) desta skill. As duas fontes-âncora são obtidas em **Google Fonts** onde possível: **Georgia** (serif clássica, títulos e textos — já vive nativamente em qualquer sistema) e uma sans próxima de **Akzidenz Grotesk Next** (fonte suporte); para **League Gothic** (palavras curtas e sinalização), usar direto do Google Fonts. Os detalhes finos (paleta HEX exata, hierarquia tipográfica, aplicação do símbolo, grafismos, grid, área de proteção, tom visual) estão em:

- [references/paleta-e-tipografia.md](references/paleta-e-tipografia.md) — 4 cores da paleta oficial (HEX) e as 3 famílias tipográficas com regras de uso.
- [references/logo-e-simbolo.md](references/logo-e-simbolo.md) — símbolo (trevo-de-corações), variações do logotipo, ícone, grid e área de proteção.
- [references/grafismos-e-aplicacoes.md](references/grafismos-e-aplicacoes.md) — silhuetas de alimentos/utensílios, patterns, aplicação em papelaria, embalagem, uniforme, fachada, sinalização e tom.

Leia essas três referências antes de escolher fundo, tipo ou grafismo. Para uso em código (v0, Cursor, Lovable, tema de site), a fonte-única de tokens é [DESIGN.md](DESIGN.md) — colável direto na conversa do agente de código.

## O design system em uma tela

**Quatro cores, três fundos**. A paleta oficial tem quatro cores; três delas são fundos legítimos:

- **Creme** `#fff4e8` — fundo mais leve, para peças informativas, tabloide, encarte, quando a mensagem precisa respirar.
- **Marrom** `#7c4016` — fundo mais assinado, transmite acolhimento e é o marrom da marca (não é um marrom qualquer). Sempre com título em creme.
- **Laranja** `#f4951e` — fundo enérgico, para chamada de oferta, "chegou", "novidade", KV de vitrine. Texto em marrom, nunca preto.
- **Marrom escuro / quase-preto** `#3d2016` — apoio para tipografia sobre creme quando precisar de mais peso, e para acabamentos (fita de rodapé, borda de sinalização). Não é um fundo de peça inteira.

O par sempre-vivo é **marrom `#7c4016` + laranja `#f4951e`**: o wordmark do "São Luiz" é serif marrom, o "SUPERMERCADO" abaixo é sans caixa alta laranja. Nas versões sobre marrom ou sobre laranja, o wordmark vira creme (`#fff4e8`) mantendo a sublinha em laranja ou creme.

**Símbolo: trevo-de-corações.** Um trevo de 4 pétalas onde cada pétala é um **coração** (referência às raízes cearenses e à ideia de "faz com o coração"). Cor: laranja + marrom sobre creme; marrom sobre creme; creme sobre marrom/laranja. Nunca deforme, nunca coloque em cor fora da paleta, nunca inverta pétalas. Grid: o símbolo ocupa **3X de altura** onde X = altura da palavra "SUPERMERCADO"; área de proteção = 3X ao redor do lockup.

**Tipografia**:
- **Georgia** (serif) — títulos-âncora e textos longos. É a fonte que constrói o wordmark "SãoLuiz" (S e L maiúsculos, sem espaço). Aceita variação **Outline** para palavras decorativas.
- **Akzidenz Grotesk Next** (sans humanista) — fonte suporte para textos corridos, legendas, corpo de anúncio, tabela de preços.
- **League Gothic** (sans condensada caixa alta) — só para palavras curtas e sinalização (setas, ENTRADA, CAIXA, CEREAIS, número de corredor). Nunca use para texto corrido.

**Grafismos**: silhuetas planas e fechadas (fill único, sem contorno, sem gradiente) de alimentos e utensílios — maçã, banana, limão, garrafa, taça, batedor, cupcake, croissant, spray, balde — sempre em uma das duas cores assinadas: **marrom** `#7c4016` ou **laranja** `#f4951e`. Usam-se como ícones soltos, em fila (feed horizontal), ou como pattern grande (crop dentro de retângulo com cantos arredondados). Nunca colorir dentro (a silhueta é chapada) e nunca combinar mais de duas cores numa mesma composição.

**Regras de composição**:
1. Toda peça nasce num dos três fundos (Creme, Marrom ou Laranja). Escolha pelo tom da mensagem, não pelo estilo do designer.
2. O símbolo aparece sempre com o wordmark em pelo menos uma peça da campanha (feed, story, capa). Ícone isolado (só o trevo) é permitido em selo, favicon, uniforme e sinalização.
3. Fotografia é real, quente, gastronômica — comida de verdade, mão de gente de verdade, mesa posta, ambiente com iluminação âmbar/terracota. Nunca render 3D genérico, nunca stock frio azulado.
4. Selo de preço é círculo laranja com número Georgia em creme; a fração "/unidade" ou centavos usa sans pequeno.
5. Uniforme e sacola são marrom `#7c4016` com o lockup em creme `#fff4e8`; embalagem/caixa kraft usa o ícone (trevo) marrom sobre o kraft cru.
6. Sem travessão em texto algum, sem emoji em peça oficial (regras de escrita do Gustavo valem para qualquer texto que a estilização obrigue a tocar).

**Assinatura verbal recorrente** (vistas no manual, use quando cabíveis): *"Lugar de quem faz com o coração."* / *"A gente encontra e se encontra aqui."* Tom: afetivo, direto, popular sem ser vulgar, próximo do cearense sem caricatura.

## Como executar

1. Leia o material de origem inteiro antes de tocar em qualquer coisa e liste as seções/peças pra garantir que nada será perdido na reestilização. Se for criar do zero, confirme com o Gustavo o texto e o formato (feed, story, encarte, banner, papelaria…).
2. Leia as três referências desta skill (`paleta-e-tipografia.md`, `logo-e-simbolo.md`, `grafismos-e-aplicacoes.md`) e escolha o fundo (Creme/Marrom/Laranja), o par tipográfico e os grafismos que conversem com o assunto da peça.
3. Para material em código (web, e-commerce, portal, dashboard interno, template de e-mail), cole [DESIGN.md](DESIGN.md) no agente de código (v0, Cursor, Lovable) como fonte-única de tokens e peça a composição já sob esses tokens.
4. Para material gráfico (feed, story, encarte, deck), use os HEX e a tipografia listados como fonte-única — não invente variações de tom nem substitua fontes por "equivalentes visuais".
5. Verifique visualmente antes de entregar: confira símbolo com área de proteção respeitada, wordmark em par de cor válido (marrom+laranja sobre creme, creme+laranja sobre marrom, creme+marrom sobre laranja, marrom+marrom sobre creme como versão monocolor), foto quente e comida real, sem travessão e sem emoji.
6. Se o Gustavo quiser PNG/JPG por peça (comum em social e encarte) ou PDF (comum em papelaria e deck), exporte com Chrome headless e confira lendo o resultado.

## Referência viva

O PDF fonte da IDV é `~/Documents/Nova Marca São Luiz 2025 (1) (2).pdf` (20 páginas, 164 MB, gerado no Adobe Illustrator). As páginas renderizadas em 72dpi vivem em [`assets/manual/`](assets/manual/) e servem como amostra visual rápida — quando bater dúvida de como um componente aparece na marca, olhe lá. Os HEX e a tipografia foram extraídos exatamente desse arquivo.

Contexto do cliente e do projeto: ver [[project_mslz]] (Portal MSLZ — SAC interno do Grupo São Luiz) e [[project_festival_costume_gourmet]] (contrato Miner × MSLZ do festival, escopo da irmã festivaldesign) no vault do Gustavo.
