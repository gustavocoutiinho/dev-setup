---
name: deck-kit
description: Use quando o Gustavo for criar um deck/relatório novo da Miner, "abrir um deck do zero", "começar o relatório de <cliente>", "novo deck-*", "usar o molde de deck", "com a cara da Miner (KV)", ou editar estrutura/estilo de um deck existente. Dá o template único de deck (fontes, tokens CSS do KV Miner, favicon, server de dev compartilhado) em vez de duplicar CSS e config a cada repo, e define quando usar o KV Miner e quando usar a marca do cliente. Dispara ao criar ou editar qualquer deck-*.
---

# deck-kit · template único de deck (para de duplicar por repo)

## Problema
Cada `~/dev/decks/deck-<cliente>` hoje recarrega fontes, CSS, favicon e server.js clonados.
Isso multiplica manutenção e faz os decks divergirem. O deck-kit é a base compartilhada:
tokens do KV, fontes, favicon Miner e o server de dev, iguais em todo deck. O que muda por
deck é conteúdo e (às vezes) a paleta da marca do cliente.

## Anatomia de um deck (padrão observado nos deck-*)
```
deck-<cliente>/
  index.html        # capa / índice
  <mes>.html        # uma competência por arquivo (maio.html, junho.html), clonada do molde
  fonts.css         # @font-face das fontes Miner
  fonts/            # arquivos das fontes
  server.js         # server estático de dev (Node puro, porta 8901)
  favicon.svg/.ico/-32/-16, site.webmanifest, apple-touch-icon.png   # favicon Miner
  vercel.json       # deploy
  img/
```
Molde de esqueleto: sempre o Barney's/junho (regra fixa, dados mudam e esqueleto não).

## Tokens KV Miner
- **Cor de marca:** Hudson `#4562FF`. Base neutra: escala **zinc**.
- **Fontes:** **VisbyCF** (títulos/números) + **Behind The Nineties** (display). Servidas por
  `fonts.css` local, nunca CDN externo.
- **Números** com máscara pt-BR e classe `.num` / blocos `.metric` (integra com deck-vivo).
- Detalhes de paleta/tipografia: skill **minerdesign** (Hudson/Soho/Brooklyn, VisbyCF +
  Behind The Nineties). Passar arte nova por lá.

## KV Miner vs marca do cliente (política)
- **KV Miner** por padrão em: relatório/deck de resultado que a Miner assina (Barney's, Estela,
  Ollis, Normatel, Otorhinos, Lesalis...). É a Miner mostrando trabalho.
- **Marca do cliente** quando o material é do evento/produto do cliente e tem IDV própria já
  definida: ex. **Festival Costume Gourmet** usa a skill `festivaldesign` (vinho/oliva/creme,
  Playfair+Montserrat), NÃO o KV Miner. Se o cliente tem skill de design própria, ela manda.
- Na dúvida: KV Miner. Nunca misturar os dois sistemas no mesmo deck.

## Como executar (deck novo)
1. Clonar o esqueleto do Barney's (não começar do zero): copiar `fonts.css`, `fonts/`,
   favicon, `server.js`, `vercel.json` e o HTML molde.
2. Nomear a pasta `deck-<cliente>` (convenção `tipo-cliente`, igual GitHub/Vercel/~/dev).
3. Manter os tokens KV; só trocar conteúdo. Se for cliente com IDV própria, aplicar a skill de
   design dele por cima (não editar token na mão).
4. Dev local: `node server.js` (sobe em `:8901`, serve a pasta, bloqueia path traversal).
5. Números entram como dado (ver **deck-vivo**), não chumbados à mão.
6. Deploy: `vercel --prod`. Deploy sempre da última main; editar = deployar (só conta no ar).

## Gotchas
- **Fonte via arquivo local**, nunca link externo (deck precisa abrir offline e no export
  headless do exporta-deck).
- **server.js é dev only** (porta 8901); produção é Vercel estático.
- **Não versionar `.git` em iCloud/Drive**; repos vivem em `~/dev`.
- Favicon Miner é parte da identidade do deck: não remover ao clonar.

## NÃO fazer
- Não duplicar CSS/tokens divergentes por repo: partir sempre do mesmo esqueleto.
- Não puxar fonte de CDN.
- Não aplicar KV Miner por cima de cliente que tem IDV própria (ex. Festival).
- Não renomear fora da convenção `tipo-cliente`.
