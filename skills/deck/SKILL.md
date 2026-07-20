---
name: deck
description: Use SEMPRE que o trabalho for um deck/relatório HTML da Miner em ~/dev/decks: criar um deck do zero no molde KV (fontes, tokens, favicon, server de dev), virar o mês de um deck que já existe (números chumbados no HTML viram JSON por competência, deltas calculados e não digitados), rodar o ciclo mensal de um cliente (Barney's, Estela, Olli's, Normatel, Maresia), gerar a versão trimestral do mesmo dado, ou exportar em PDF/PNG retina via Chrome headless. Dispara com "abre um deck do zero", "novo deck do <cliente>", "usa o molde de deck", "com a cara da Miner (KV)", "atualiza o deck do mês", "fecha o mês do <cliente>", "não quero redigitar número", "clona o deck pro mês novo", "compara com o mês passado", "gera o trimestral", "gera o PDF do deck", "exporta o deck em imagem", "PNG de cada tela".
---

# deck: deck/relatório HTML da Miner, do zero ao PDF

A Miner refaz decks de resultado o tempo todo (`~/dev/decks/deck-*`, HTML estático, um arquivo por mês). Sem trilho, cada virada é retrabalho: clona HTML, redigita dezenas de números, erra delta. Esta família dá um esqueleto único, separa dado de esqueleto e padroniza o export. O esqueleto NUNCA muda; só o dado do mês muda.

## Modos
- **criar do zero** (deck-kit): clona o esqueleto do Barney's (fonts, favicon Miner, `server.js`, `vercel.json`), aplica tokens KV. Não começa do zero.
- **dado vivo / JSON** (deck-vivo): extrai os `<span class="num">` chumbados pra `dados/<competencia>.json`; delta vira cálculo, não digitação; o mesmo JSON gera mensal e trimestral.
- **ciclo mensal** (deck-mes): wrapper "novo mês do cliente X" que orquestra estrutura + dado + visual numa virada só.
- **export** (exporta-deck): PDF do deck inteiro e PNG retina por tela via Chrome headless.

## Quando disparar
- "abre um deck do zero / novo deck do <cliente> / usa o molde": modo criar.
- "fecha o mês do <cliente>", "roda o deck de julho da Estela", "não quero redigitar número", "compara com o mês passado", "gera o trimestral": modo mensal + dado vivo.
- "gera o PDF do deck", "PNG de cada tela", "versão pra enviar": modo export.
- NÃO é relatório vivo multi-tenant (fundação app-relatorios), social ou ACCS: isso é [[relatorio]].

## Como executar
1. **Contexto primeiro.** Puxe o cliente e o histórico do deck no [[obsidianminer]] (memórias `feedback_decks_relatorio_padrao`, `barneys-deck-relatorio`). Nunca invente número.
2. **Esqueleto é fixo.** A lógica de slides é SEMPRE a do `~/dev/decks/deck-barneys/junho.html` (regra 09/07: dados mudam, esqueleto não). Clonar componentes já prontos (capa-kv, `.why`, `.adrk`).
3. **Criar do zero:** copie `fonts.css` + `fonts/`, favicon Miner, `server.js`, `vercel.json` e o HTML molde. Pasta `deck-<cliente>` (convenção `tipo-cliente`, igual GitHub/Vercel/~/dev). Tokens KV: Hudson `#4562FF`, base zinc, **VisbyCF** + **Behind The Nineties** servidas por `fonts.css` local (nunca CDN). Detalhe visual e `.why` em todo número: [[minerdesign]].
4. **Dado no JSON, não à mão:** varra os `<span class="num">`/`.metric` e monte `dados/2026-06.json` (`{ competencia, cliente, kpis:{...} }`); guarde o número cru (`92833`, `1.15`), formate no render. Delta = `(atual-anterior)/anterior` lido do mês anterior; sem base, omite (não inventa).
5. **Trimestral do MESMO dado:** agrega as 3 competências (soma leads/investido; média ponderada CPM/frequência/CTR). Paridade obrigatória: o trimestral tem TODOS os slides do mensal, na mesma ordem.
6. **Números reais, mês explícito** (regra Normatel): KPI sai do Histórico real, cada card carrega o mês; nunca extrapolar snapshot velho nem rotular dado antigo com mês novo.
7. **Export (base `deck-festival/_src/export.py`):** Chrome em `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. PNG por `<section class="tela...">` isolada com `--force-device-scale-factor=2 --window-size=1280,720`; PDF com `--print-to-pdf --no-pdf-header-footer` no `index.html`. Saída em `_src/export/`. Confira o `assert len(telas)==len(nomes)`.
8. **Deploy = está no ar.** `vercel --prod` da pasta, da última main (via [[deploy]]). Editar = deployar: confirme a URL respondendo.

## Gotchas
- **Fonte local é obrigatória:** o headless carrega `file://`; fonte via CDN não entra no PNG/PDF nem abre offline.
- **Milhar pt-BR:** `92.833` = 92 mil (ponto = milhar), `1,15` = decimal. No JSON `92833`/`1.15`; máscara é do render.
- **Slide number não é KPI:** `<span class="num">01</span>` é numeração de tela; ignore os `>0\d<` de sequência.
- **Ilustrativo vs real:** deck com números ilustrativos (ex. Festival) marca `"origem":"ilustrativo"` no JSON pra não virar dado fechado.
- **Export:** se o `assert` de telas x nomes falha, o deck ganhou/perdeu seção: atualize a lista, não force. Não deployar a pasta `_src/export/` junto do site.
- **server.js é dev only** (porta 8901); produção é Vercel estático.
- Sem criativo repetido nos slides de Meta Ads; foto grande só com fonte hi-res.

## O que NÃO fazer
- NÃO editar o esqueleto pra "encaixar" o mês nem duplicar CSS/tokens divergentes por repo.
- NÃO redigitar número que dá pra extrair, nem digitar delta/variação.
- NÃO misturar cliente/competência no mesmo JSON, nem puxar fonte de CDN.
- NÃO aplicar KV Miner por cima de cliente com IDV própria (Festival usa [[festivaldesign]]).
- NÃO enviar PDF/PNG pro cliente sem ordem explícita do Gustavo (só leitura; envio só por item).
