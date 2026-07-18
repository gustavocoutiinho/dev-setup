---
name: shopify-estrutura
description: Use SEMPRE que for criar ou ligar dados estruturados numa loja Shopify de cliente Miner: metaobjects, metafields, guia de tamanhos, FAQ, e ligar isso no tema pra renderizar. Dispara com "cria o guia de tamanhos na loja", "sobe os metafields da PRLS", "liga a seção no tema", "replica a estrutura da PRLS pra <marca>", "FAQ no produto", "dados estruturados no Shopify". Também quando metaobject/metafield já existe mas não aparece no storefront. Cria via Admin GraphQL e liga no tema, sem tocar preço/estoque.
---

# shopify-estrutura: metaobjects/metafields ligados no tema

Estruturar loja Shopify de cliente (guia de tamanhos, FAQ, atributos de produto) é trabalho que a Miner já fez inteiro na PRLS (prls.com.br, 68 produtos). O padrão: criar metaobjects/metafields via Admin GraphQL e **ligar no tema**, porque criar a infra não basta, ela só renderiza depois de entrar numa seção do tema. Esta skill replica isso, sem tocar preço/estoque/frete.

## Quando disparar
- "cria o guia de tamanhos", "sobe os metafields", "liga a seção no tema", "FAQ no produto", "dados estruturados no Shopify".
- Metaobject/metafield já existe mas não aparece no storefront (falta ligar no tema).
- Replicar a estrutura da PRLS pra outra marca Shopify (ex: DLT / estilodlt.com.br).

## Como executar
1. **Contexto** ([[obsidianminer]], [[prls-shopify-structured-data]]): na PRLS os metaobjects `guia_de_tamanhos` (def `20774388010`) e `faq_prls` (def `20774420778`) + metafields namespace `prls` foram criados 07/06; faltava ligar no tema.
2. **Metaobjects com `access: PUBLIC_READ`** (senão o storefront não lê) + metafield no produto (`metaobject_reference` amarra o produto ao guia).
3. **Ligar no tema é o passo que sempre falta.** O MCP Shopify escreve só em **tema não-publicado** (`themeFilesUpsert`/`themeDuplicate`); o MAIN/live é bloqueado. Crie a cópia, adicione `sections/prls-product-extras.liquid` + inclua no `templates/product.json`, valide no theme-check, confira no `?preview_theme_id=`.
4. **Não duplique o que o tema já faz:** o tema v8 da PRLS já tinha bloco de material/cuidados; a seção nova ficou com toggles e Material/Cuidados OFF por padrão.
5. **Publicar é decisão do Gustavo** (manual via themePublish).

## Gotchas
- Criar metafield/metaobject sem ligar no tema = nada aparece na PDP. Só "conta" renderizando ([[feedback_editar_e_deployar]]).
- MCP Shopify é do ambiente de chat; portal/function precisa de token próprio (custom app `shpat_`).
- SEO/blog da loja é [[seo-blog]]; deixar dado vivo em vez de chumbado é [[dado-vivo]].

## O que NÃO fazer
- NÃO editar o tema publicado direto (bloqueado; use cópia + preview).
- NÃO mexer em preço/estoque/frete/cupom.
- NÃO deixar metaobject sem PUBLIC_READ.
