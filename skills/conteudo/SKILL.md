---
name: conteudo
description: Use SEMPRE que o trabalho for conteúdo ou marca de um cliente da Miner: manual de marca (diretrizes visuais e verbais) somado a prompts de IA no tom da marca, linha editorial focada em vendas (calibrada por deals do HubSpot e GA4), SEO de blog e descrição de produto no Shopify com IA, ou o dashboard do squad de influencers (Mercadão São Luiz). Dispara com "monta o manual de marca do <cliente>", "prompts de IA no tom da marca", "guia da marca <X>", "linha editorial de vendas", "pauta que vende", "conteúdo focado em vendas", "padroniza o blog/SEO", "palavras-chave pro Shopify", "melhora o texto de produto com IA", "dashboard de influencers do São Luiz".
---

# conteudo: marca, editorial, SEO e influencers do cliente

Consolida o trabalho de conteúdo de cliente: definir a marca e como a IA escreve nela, pautar conteúdo que puxa venda, padronizar SEO no Shopify e acompanhar o squad de influencers. É a marca DO CLIENTE, não o KV da Miner (isso é [[minerdesign]]). Quatro modos.

## Modos
- **marca**: manual de marca (visual + verbal) + prompts de IA prontos pra gerar no tom daquela marca (task atrasada STKR Fr).
- **editorial**: linha editorial focada em vendas, não alcance (HubSpot deals + GA4 → drafts no Asana), padrão MGTC.
- **seo**: padroniza blog e descrição de produto com IA e publica em metafields Shopify (DLT; replica o SEO da PRLS).
- **influencers**: dashboard do squad de 11 influencers do MSLZ com dados de Instagram no ano.

## Quando disparar
- "manual/guia de marca do <cliente>", "prompts de IA no tom da marca".
- "linha editorial de vendas", "pauta que vende", "o que postar pra gerar deal".
- "padroniza o blog", "SEO com IA", "palavras-chave pro Shopify", "replica o SEO da PRLS".
- "dashboard de influencers", "performance dos influenciadores do São Luiz".

## Como executar
1. **Contexto** do cliente via [[obsidianminer]]: marca, público, oferta, o que já existe.
2. **Marca**: destile diretrizes visuais e verbais do cliente e escreva prompts prontos pra IA gerar no tom (via ai-json, ver [[ia]]).
3. **Editorial**: puxe deals do HubSpot + comportamento do GA4, gere as pautas com ai-json, jogue como drafts no Asana. Cada pauta amarra a um objetivo de venda.
4. **SEO**: cruze GA4 + Search Console, gere descrições/palavras-chave com IA, publique em metafields Shopify ([[dados]]). Replique o padrão que já roda na PRLS pras outras marcas.
5. **Influencers**: consolide dados de Instagram dos influencers num painel vivo ([[conserta-web]] via [[criar-web]]), projeto patrocinios-mslz.

## Gotchas
- Editorial de venda não é calendário de alcance: cada pauta tem que ter hipótese de conversão.
- SEO no Shopify vai em metafield ligado ao tema, não texto solto que o tema ignora.
- Manual de marca sem os prompts de IA fica pela metade: o valor é a IA escrever no tom depois.

## O que NÃO fazer
- NÃO usar o KV da Miner quando o material é do cliente (use a marca dele).
- NÃO gerar conteúdo com IA fora do ai-json.
- NÃO publicar SEO sem ligar no tema do Shopify.
