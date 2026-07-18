---
name: seo-blog
description: Use quando o trabalho for padronizar blog, descrições e SEO de um e-commerce Shopify com IA e publicar direto na loja via metafields. Vem das tasks DLT "Padronização blog descrições com IA" e "Enviar palavras chaves SEO DLT", e de replicar o SEO estruturado da PRLS pras outras lojas. Dispara com "padroniza as descrições da <loja>", "SEO do blog do <cliente>", "palavras-chave pro Shopify", "joga o SEO no Shopify", "replica o SEO da PRLS", "melhora o texto de produto com IA".
---

# seo-blog: SEO de e-commerce padronizado com IA, direto no Shopify

Loja com descrição solta e sem palavra-chave perde busca orgânica. Esta skill padroniza blog e descrições de produto com IA, calibrada por dado real (GA4 + Search Console), e publica no Shopify via metafields. Origem: tasks DLT (Estilo DLT, estilodlt.com) "Padronização blog descrições com IA" e "Enviar palavras chaves SEO DLT"; o Playbook DLT SEO+IA está no Notion.

## Quando disparar
- E-commerce Shopify precisa de descrições e blog padronizados e otimizados.
- Vai replicar o SEO estruturado da PRLS (prls.com.br, metaobjects/metafields) pras outras lojas (DLT, Le Salis).
- NÃO use pra conteúdo de topo focado em deal B2B (é [[editorial-vendas]]).

## Como executar
1. **Contexto primeiro.** Puxe a loja no [[obsidianminer]] e a estrutura Shopify em [[shopify-estrutura]]. Confirme token Admin vivo da loja (os antigos morreram, 401).
2. **Leia a busca.** GA4 (tráfego e conversão por página) + Search Console (query, impressão, posição). A palavra-chave vem do que já busca e rankeia, não de chute.
3. **Padronize com IA.** Rode via IA da Miner (ai-json): template único de descrição (título, bullets, texto, meta) e pauta de blog por cluster de keyword, no tom do [[marca-manual]].
4. **Drafts antes de publicar.** Gere rascunhos revisáveis, nada entra direto na loja sem conferência.
5. **Publique no Shopify.** Grave em metafields/metaobjects (padrão PRLS) via MCP Shopify. Estrutura reusável entre lojas ([[shopify-estrutura]]).

## Gotchas
- Token Shopify Admin é "mostrado uma vez", o antigo (shpat_570424...) está morto. Sem token vivo, PARE e registre no [[radar-bloqueios]].
- Keyword sem lastro no Search Console é achismo: sempre valide com dado.
- Metafield errado não aparece no tema, confirme o namespace e a key que o tema lê ([[shopify-estrutura]]).

## O que NÃO fazer
- NÃO publicar descrição de IA sem revisão humana.
- NÃO inventar volume de busca, puxe do Search Console.
- NÃO deletar descrição antiga antes de confirmar a nova no ar (editar = deployar).
- NÃO rodar IA por chave solta, passa por ai-json.
