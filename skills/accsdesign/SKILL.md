---
name: accsdesign
description: Aplica a identidade visual do Grupo Aço Cearense/ACCS (azul-marinho + azul-claro institucionais, símbolo "K" derivado da ligadura A+C, fotografia industrial com filtro azul, grafismo diagonal, tipografia Herokid/Monstane Olstd/Manrope) a QUALQUER material do cliente: decks, propostas, relatórios, posts/KVs de redes sociais, papelaria, e também portal/web se for pedido, SEM alterar conteúdo, dados ou números. Cobre as 5 marcas do grupo (Grupo Aço Cearense, Aço Cearense, SINOBRAS, SINOBRAS Florestal, Instituto Aço Cearense), cada uma com ícone e cor próprios. Tem DESIGN.md portátil com os tokens (colável em v0/Cursor/Lovable). Use SEMPRE que o Gustavo pedir material para o cliente Aço Cearense/ACCS/Grupo Aço Cearense/Sinobras/Florestal/Instituto, pedir pra "deixar com a cara da ACCS", "minerizar pro cliente", estilizar ou criar do zero deck/proposta/KV/post/página em nome desse cliente, mesmo que não cite a skill pelo nome. Se o material é da Aço Cearense (ACCS) e é visual, passe por aqui.
---

# accsdesign

Aplica o design do Grupo Aço Cearense (cliente Miner, alias ACCS) a qualquer material visual em nome desse cliente. O trabalho é de pele, não de órgão: o conteúdo que já existe (textos, números, dados de tabela, ordem das seções) permanece intacto. Se durante o trabalho um erro de conteúdo aparecer, reporte ao Gustavo e não corrija por conta própria.

Esta skill é irmã da [[minerdesign]] (identidade da própria Miner) e da [[festivaldesign]] (Festival Costume Gourmet), mas com design system próprio: industrial, azul-marinho, fotografia de gente de verdade trabalhando, símbolo geométrico "K". Nunca misture com a paleta/tipografia da Miner ou de outro cliente.

## Qual caminho seguir

Antes de qualquer coisa, decida duas coisas: **qual marca** (Grupo, Aço Cearense, Sinobras, Florestal Sinobras ou Instituto) e **qual tipo de peça**.

- **Qual marca**: se o Gustavo não especificar, use a marca-mãe **Grupo Aço Cearense** (símbolo K bicolor navy+azul-claro). Se o pedido for claramente sobre uma unidade específica ("posta pra Sinobras", "isso é do Instituto"), use o ícone e a cor de identificação daquela unidade, mas mantenha navy+azul-claro institucionais presentes (nunca somem). Detalhe de cada marca em [references/logo-e-submarcas.md](references/logo-e-submarcas.md).
- **Qual tipo de peça**: KV/post de campanha (feed, story, banner) segue a estrutura de [references/aplicacoes-e-grid.md](references/aplicacoes-e-grid.md) (fotografia em facetas diagonais + tagline + rodapé). Deck/proposta/relatório usa os mesmos tokens de cor/tipografia num layout de slide 16:9. Papelaria/cartão/crachá/uniforme/sinalização segue os exemplos reais da mesma referência. Web/portal usa [DESIGN.md](DESIGN.md) como fonte de tokens.
- Os tokens de cor/tipografia são os mesmos em qualquer caminho; o que muda é a composição.

## Fonte da verdade

O manual oficial é "Diretrizes da Marca" (Versão 10), 139 páginas, produzido pela agência Propeg para o Grupo Aço Cearense. Esta skill foi construída lendo o documento inteiro, página por página. Os **tokens** (cores, tipografia, grid, componentes) estão canônicos em [DESIGN.md](DESIGN.md). O **detalhe completo e as regras de cada seção** vivem em `references/`, cada arquivo cobrindo um capítulo do manual original:

- [references/marca-e-verbal.md](references/marca-e-verbal.md) — quem é o cliente, arquitetura das 5 marcas, propósito/manifesto/tagline, tom de voz, palavras proibidas, glossário de produtos.
- [references/logo-e-submarcas.md](references/logo-e-submarcas.md) — construção do logo, versões, área de proteção, tamanho mínimo, os 8 usos indevidos, sistema de pareamento entre marcas, e o detalhe de cada uma das 5 marcas.
- [references/cores-e-tipografia.md](references/cores-e-tipografia.md) — paleta completa (institucional, neutra, 12 secundárias, paleta própria de cada submarca) com HEX/RGB/Pantone/CMYK, e o sistema tipográfico completo.
- [references/icones-texturas-fotografia.md](references/icones-texturas-fotografia.md) — grid e regras de ícone, as 2 texturas de fundo, o grafismo diagonal, estilo fotográfico (o que fazer/evitar).
- [references/aplicacoes-e-grid.md](references/aplicacoes-e-grid.md) — sistema de grid/módulo, estrutura do Key Visual (KV), e a galeria de aplicações reais (cartão, papelaria, e-mail, veículo, uniforme, crachá, sinalização, app).
- [references/gotchas-da-fonte.md](references/gotchas-da-fonte.md) — inconsistências reais do documento-fonte (datas de versão, numeração de página, valores de CMYK impossíveis etc.). Leia antes de estranhar qualquer divergência com o PDF original.

Os **assets físicos** (logos recortados limpos + páginas de referência completas do manual original) vivem em `assets/img/`: `logos/` tem os lockups do Grupo e das 4 submarcas isolados em fundo branco; `paginas/` tem ~40 páginas do manual original copiadas na íntegra (prefixo indica o assunto: `logo-*`, `cores-*`, `tipografia-*`, `icones-*`, `aplicacao-*`, `kv-*`), pra consultar o layout real sempre que uma regra do texto não deixar claro como uma composição se parece.

## O design system em uma tela

**Paleta**: navy `#223564` + azul-claro `#6EAFD5` (institucionais, predominantes SEMPRE, em qualquer marca do grupo). Preto e cinza `#9D9D9C` só como apoio, nunca cor principal. 12 secundárias ampliam a composição (turquesa `#55C0B3`, verde-limão `#94C120`, coral `#FF5C60`, entre outras); o amarelo `#F8BE38` é restrito a campanhas especiais. Cada submarca tem uma paleta secundária própria e, no sistema de crachás, uma cor de identificação (Aço Cearense=azul médio, Sinobras=prata, Florestal=verde, Instituto=sem cor própria documentada).

**Tipografia**: Herokid (display bold condensada, títulos de campanha) + Monstane Olstd (script, só 1-2 palavras-âncora dentro de uma frase, nunca corpo de texto) formam o par "criativo". Manrope (Google Fonts, sans-serif) é a fonte principal pra tudo mais, obrigatória em comunicação de produto. Arial/Montserrat só quando as institucionais não puderem ser usadas (Office, sistemas).

**Composição**:
1. O símbolo "K" (ligadura geométrica de A+C, sem curvas) é a origem de tudo: logo, ícones, textura e o grafismo diagonal (corte com 2 cantos arredondados + 2 retos) vêm do mesmo ângulo. Nunca invente uma forma nova desconectada dele.
2. Fotografia é sempre gente real trabalhando, nunca olhando pra câmera, com o filtro azul institucional (`#6EAFD5→#223564`) por cima. Nunca banco de imagens genérico.
3. Grafismo sempre sangra pra fora da peça; nunca fica "fechado" dentro da composição.
4. Ícones: grid 24px, traço 1px, outline, uma cor só, nunca gradiente/sombra/rotação/distorção (8 proibições, ver referência).
5. Ao parear duas marcas do grupo (ou marca + parceiro), a marca prioritária vai sempre mais à direita e nunca aparece menor que a acompanhante; módulo de respiro X derivado da altura do logo.
6. Tagline-mãe: "Nossa gente dá liga. Nossa liga constrói o futuro." Cada submarca tem a própria variação (ver referência verbal).
7. Sem travessão em texto algum; evite a lista de palavras proibidas (ver referência verbal).

Racional completo (o "porquê" de cada decisão, com todos os valores e regras) nos arquivos de `references/` acima.

## Como executar

1. Leia o material de origem inteiro antes de tocar em qualquer coisa e liste as seções, pra garantir que nada será perdido na reestilização.
2. Decida a marca (Grupo ou uma das 4 unidades) e o tipo de peça (ver "Qual caminho seguir" acima). Se tiver dúvida de como um componente aparece na marca de verdade, olhe a página de referência correspondente em `assets/img/paginas/` antes de inventar.
3. Monte com os tokens de [DESIGN.md](DESIGN.md) (cor, tipografia, grid) e a estrutura da peça certa em `references/` (KV, papelaria, web).
4. Embuta as fontes reais antes de publicar: Manrope e Montserrat são Google Fonts (embuta via `@import` ou arquivo local, sem restrição). Herokid e Monstane Olstd provavelmente são fontes licenciadas da Propeg/cliente: peça os arquivos ao Gustavo para material oficial final; em protótipo, use os fallbacks indicados no DESIGN.md e avise que são fallback.
5. Verifique visualmente antes de entregar: sirva num servidor estático e tire screenshot da peça. Confira: navy+azul-claro presentes, grafismo sangrando pra fora, fotografia sem olhar-pra-câmera, logo com a área de proteção respeitada.
6. Se o Gustavo quiser PNG/JPG (peça de campanha/social) ou PDF (deck/proposta), exporte com Chrome headless e confira lendo o resultado.

## Referência viva

- Manual original: `~/Downloads/BRAND GUIDELINES 1920x1080px ACO CEARENSE - AF (1).pdf` (139 páginas, Versão 10). Se não estiver mais em Downloads, peça ao Gustavo o arquivo atualizado antes de assumir que esta skill já cobre uma revisão nova.
- Contexto do cliente (stakeholders, projetos ativos, portal, stack): nota `Aço Cearense` no vault Obsidian (skill `obsidianminer`) e memórias `project_portal_accs`, `project_contexto_accs`.
