---
name: marca-manual
description: Use quando precisar produzir o manual de marca de um cliente (diretrizes visuais e verbais) somado a prompts de IA prontos pra gerar conteúdo no tom daquela marca. É a marca DO CLIENTE, não o KV da Miner. Sai da task atrasada "Manual de marca + prompts IA STKR Fr" (Stalker) e casos análogos. Dispara com "monta o manual de marca do <cliente>", "diretrizes da marca <X>", "prompts de IA no tom do <cliente>", "guia de marca + prompts", "como a IA escreve no estilo da <marca>".
---

# marca-manual: manual de marca do cliente + prompts de IA prontos

Cliente pede consistência e a Miner entrega dispersa, cada peça num tom. Esta skill fecha o manual de marca do CLIENTE (visual + verbal) e, no mesmo entregável, gera os prompts de IA que fazem qualquer geração já sair no tom da marca. Task viva: "Manual de marca + prompts IA STKR Fr" (Stalker Franquias), atrasada no backlog estratégico.

## Quando disparar
- Cliente precisa de guia de marca e/ou dos prompts que padronizam a IA no tom dele.
- Antes de escalar produção de conteúdo ou criativo pra um cliente sem diretriz escrita.
- NÃO confunda com [[minerdesign]] (esse é o KV da Miner, não do cliente).

## Como executar
1. **Contexto primeiro.** Puxe o cliente no [[obsidianminer]]: material existente, público, concorrentes, lead Miner (STKR = Rafael + Raquel, e tem duas frentes, Fr Franquias e Mm Marca Mãe). Nunca invente identidade.
2. **Diretrizes visuais.** Paleta, tipografia, uso de logo, grid, do/don't. Extraia do que a marca já usa (site, Instagram, loja), não imponha o KV Miner.
3. **Diretrizes verbais.** Tom de voz, vocabulário, o que a marca fala e o que evita, exemplos de headline e legenda aprovados.
4. **Prompts de IA (o diferencial).** Traduza as diretrizes em prompts prontos: system prompt de marca + prompts por formato (post, story, descrição de produto, resposta de atendimento). Rode pela IA da Miner (ai-json), nunca por chave solta.
5. **Entregue e conecte.** Documento + biblioteca de prompts num lugar achável (Notion do cliente ou pasta do vault). Alimenta [[editorial-vendas]] (linha editorial) e [[seo-blog]] (descrições).

## Gotchas
- Manual sem prompts é meia entrega: o que padroniza a operação com IA são os prompts, não o PDF bonito.
- Marca do cliente não é a Miner: se aplicar o KV Miner por engano, quebra a identidade dele.
- Confirme qual marca antes de escrever quando o cliente tem submarcas (STKR Fr vs Mm).

## O que NÃO fazer
- NÃO usar o design da Miner como se fosse o do cliente.
- NÃO inventar tom ou valores sem base no material real da marca.
- NÃO deixar os prompts de fora, é o núcleo do entregável.
- NÃO chumbar chave de IA no prompt, passa por ai-json.
