---
name: ocadesign
description: Aplica a identidade visual do OCA lab (rebranding jan/2026 da Rede OCA, o laboratório de inovação do Grupo Aço Cearense) a QUALQUER material: decks, propostas, relatórios, posts/KVs, papelaria, crachá, brinde, e também portal/web se for pedido, SEM alterar conteúdo, dados ou números. Wordmark OCA derivado do anagrama de "ACO" na tipografia do grupo, gradiente azul #6EAFD5→#223564 como assinatura, apoios verde-água #55C0B3 e coral #FF5C60, tipografia Eurostile+Herokid, universo tech-industrial (metal, hexágono, neon). Tem DESIGN.md portátil com os tokens (colável em v0/Cursor/Lovable). Use SEMPRE que o Gustavo pedir material para OCA/OCA lab/Rede OCA/laboratório de inovação da Aço Cearense, pedir pra "deixar com a cara do OCA", estilizar ou criar do zero deck/proposta/KV/post/página em nome dessa marca, mesmo que não cite a skill pelo nome. Se o material é do OCA e é visual, passe por aqui.
---

# ocadesign

Aplica o design do OCA lab (laboratório de inovação do Grupo Aço Cearense, cliente Miner via ACCS) a qualquer material visual em nome dessa marca. O trabalho é de pele, não de órgão: o conteúdo que já existe (textos, números, dados de tabela, ordem das seções) permanece intacto. Se durante o trabalho um erro de conteúdo aparecer, reporte ao Gustavo e não corrija por conta própria.

Esta skill é **filha da [[accsdesign]]** (o OCA é uma marca do universo Aço Cearense e herda os azuis institucionais, a display Herokid e a lógica de grafismo diagonal), mas tem identidade própria: gradiente como assinatura, Eurostile no lugar de Manrope, apoios verde-água/coral, universo tech em vez de industrial-fabril. Não misture com a paleta/tipografia da Miner nem de outro cliente; e não use esta skill para as demais marcas do grupo (Grupo, Aço Cearense, Sinobras, Florestal, Instituto), que continuam na accsdesign.

## Qual caminho seguir

- **Peça institucional/apresentação** (deck, proposta, relatório): tokens de [DESIGN.md](DESIGN.md) em slide 16:9; títulos Eurostile caixa alta (par itálico ou reto), gradiente como fundo de capa/separadores ou como cor do logo sobre branco.
- **KV/post/banner de campanha**: estrutura do KV oficial em [references/cores-tipografia-patterns.md](references/cores-tipografia-patterns.md) (colagem de fotos em facetas diagonais + logo em gradiente sobre área limpa + rodapé com pílula de URL e logo do grupo).
- **Papelaria/crachá/uniforme/brinde**: exemplos reais em [references/marca-logo-assinaturas.md](references/marca-logo-assinaturas.md); é onde as cores de apoio (verde-água/coral) podem aparecer com mais força.
- **Web/portal/dashboard**: [DESIGN.md](DESIGN.md) como fonte de tokens (cores, gradientes, tipografia com fallbacks Google Fonts).
- **Co-branding**: OCA lab à esquerda, marca institucional do grupo à direita (regras na reference de marca).

## Fonte da verdade

O documento oficial é a **"Apresentação OCA_2025_FINAL_13.01.26.pdf"** (52 slides, rebranding aprovado em jan/2026). Esta skill foi construída lendo o documento inteiro, slide a slide. É uma apresentação de rebranding, não um manual completo: define logo, versões, cores, tipografia, patterns, assinaturas, aplicações e KV, mas **não define** área de proteção, tamanho mínimo, usos indevidos, ícone isolado nem tom de voz. Nesses vazios, aplique o bom senso das regras do grupo ([[accsdesign]]) e confirme com o cliente antes de inventar.

- Os **tokens** (cores, tipografia, logo, componentes) estão canônicos em [DESIGN.md](DESIGN.md).
- [references/marca-logo-assinaturas.md](references/marca-logo-assinaturas.md): quem é o OCA, construção do logo (OCA = anagrama de ACO), versões, antes/depois, co-branding, galeria de aplicações, e o que a skill não deve inventar.
- [references/cores-tipografia-patterns.md](references/cores-tipografia-patterns.md): paleta completa com HEX/RGB/Pantone/CMYK, tipografia e pares aprovados, os 2 patterns oficiais, estrutura do KV e universo visual.
- Os **assets físicos** (19 páginas-chave do doc em PNG) vivem em `assets/img/paginas/`, com prefixo por assunto (`logo-*`, `cores-*`, `tipografia-*`, `assinatura-*`, `aplicacao-*`, `pattern-*`, `kv-*`). Consulte o layout real sempre que o texto não deixar claro como a composição se parece.

## O design system em uma tela

**Marca**: OCA lab, hub de inovação do grupo (benchmarks: Cubo Itaú, Açolab, LuizaLabs). Valores: inovação, colaboração, agilidade, coragem. Nome antigo "Rede OCA" e logo antigo (corrente rosa/roxa) aposentados.

**Logo**: wordmark "OCA" (anagrama de ACO na tipografia do logotipo do grupo, A com corte do "K" e pé abaixo da baseline) + "lab" minúsculo à direita. Versões: padrão (gradiente + lab azul-claro, sobre claro), mono navy, negativo (branco em caixa navy), linear, secundárias teal/coral (brindes), branca (sobre foto/escuro).

**Cores**: gradiente `#6EAFD5 -> #223564` (claro à esquerda, sempre) é a assinatura. Apoios: verde-água `#55C0B3` (análoga) e coral `#FF5C60` (complementar), ambos já da paleta secundária do grupo; nunca dominam peça institucional.

**Tipografia**: Eurostile (principal, títulos caixa alta em par itálico ou reto) + Herokid (display, a mesma do grupo). Fallbacks de protótipo: Oxanium/Michroma e Big Shoulders Display/Anton.

**Composição**: patterns de logo repetido ou letras OCA cropadas, tom sobre tom sobre gradiente; colagem de fotos em facetas diagonais; universo metal escuro + hexágono + neon ciano; fotos com wash azul misturando aço e tecnologia; endosso do grupo no rodapé (pílula de URL + logo navy).

## Como executar

1. Leia o material de origem inteiro antes de tocar em qualquer coisa e liste as seções, pra garantir que nada será perdido na reestilização.
2. Decida o tipo de peça (ver "Qual caminho seguir"). Se tiver dúvida de como um componente aparece na marca de verdade, olhe a página correspondente em `assets/img/paginas/` antes de inventar.
3. Monte com os tokens de [DESIGN.md](DESIGN.md) e a estrutura da peça certa nas references.
4. Fontes: Eurostile e Herokid são licenciadas; peça os arquivos ao Gustavo para material oficial final. Em protótipo use os fallbacks Google Fonts (Oxanium/Michroma, Big Shoulders Display) e avise que são fallback.
5. Verifique visualmente antes de entregar: sirva num servidor estático e tire screenshot. Confira: gradiente no sentido certo (claro à esquerda), logo na versão certa pro fundo, azul dominante com apoios como acento, endosso do grupo presente quando a peça for externa.
6. Se o Gustavo quiser PNG/JPG (peça de campanha/social) ou PDF (deck/proposta), exporte com Chrome headless e confira lendo o resultado.

## Referência viva

- Doc original: `~/Downloads/Apresentação OCA_2025_FINAL_13.01.26 .pdf` (52 slides). Se não estiver mais em Downloads, peça ao Gustavo o arquivo atualizado antes de assumir que esta skill já cobre uma revisão nova.
- Contexto do cliente (stakeholders, projetos, portal, stack): nota `Aço Cearense` no vault Obsidian (skill `obsidianminer`) e memórias `project_portal_accs`, `project_contexto_accs`.
- Identidade das demais marcas do grupo: [[accsdesign]]. Copy/texto em nome do cliente: [[accscopy]].
