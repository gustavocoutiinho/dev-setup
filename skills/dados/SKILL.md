---
name: dados
description: Use SEMPRE que o trabalho for dado de cliente: ingerir/importar base de Olist/Bling/planilha (com dedup e retomada), criar metaobjects/metafields no Shopify e ligar no tema, segmentar base em RFM/ICP/Pareto, ou ingerir obras novas da Intec na Base de Obras. Dispara com "importa a base do <cliente>", "o sync parou na metade", "dedup dos contatos", "cria o guia de tamanhos no Shopify", "metafields da <loja>", "segmenta a base em RFM", "quem são os VIP", "ingere as obras da Intec".
---

# dados: dado de cliente (ingestão, Shopify, RFM, obras)

Todo trabalho de dado de cliente na Miner tropeça nas mesmas pedras: sync que trava no meio e alguém recomeça do zero, base sem dedup que duplica contato, tier de RFM sem histórico de compra, metafield criado que não aparece na loja. Esta skill cobre os quatro casos com o mesmo cuidado: dedup, checkpoint e dado vivo.

## Modos
- **ingestão**: importar base de Olist/Tiny, Bling ou planilha com dedup e retomada.
- **Shopify**: criar metaobjects/metafields e ligar no tema pra renderizar.
- **RFM/ICP/Pareto**: segmentar a base por valor pra alimentar régua e cockpit.
- **obras Intec**: ingerir obras novas na Base de Obras da Normatel.

## Quando disparar
- "importa a base do <cliente>", "sobe os contatos do Olist/Bling", "o sync parou / estancou em N de M", "dedup dos contatos", "enriquece a base".
- "cria o guia de tamanhos", "sobe os metafields da <loja>", "liga a seção no tema", "metaobject não aparece no storefront".
- "segmenta a base em RFM", "quem são os VIP", "curva de Pareto", "clientes sumidos pra reativar", "define o ICP".
- "ingere as obras da Intec", "atualiza a Base de Obras".

## Como executar
Comum: contexto da fonte no [[obsidianminer]]. Dado é vivo, não snapshot: quem consome deve ler a fonte, não um número congelado. Cron pra ongoing via [[integra]]; a base vai pro CRM via [[crm]].

**ingestão**
1. Olist/Tiny V2 tem 2 níveis: `contatos.pesquisa.php` (lista leve, sem nascimento) + `contato.obter.php` (detalhe, com nascimento/telefone/CPF). O caso ForYou parou o detalhe em **200/3796** e deixou 3.596 `pending`.
2. Dedup na entrada: telefone em **E.164** (padrão `stalker_norm_phone`) e/ou **CPF** como id primário (RPC `resolve_contact_id_by_cpf`). CPF > telefone > nome.
3. Chunked com checkpoint: processe em lotes com time-budget, marque o offset e **retome do offset**, nunca recomece. Respeite rate limit (Tiny ~30-40 req/min, Bling ~3 req/s, retry no 429). Desagende o cron quando `remaining=0`.
4. Enriquecimento não-destrutivo: preencha campo vazio, não sobrescreva bom dado. Sentinela `{_enrich:'not_found'}` em quem sumiu da fonte.

**Shopify** (PRLS, prls.com.br, 68 produtos)
- Metaobjects com `access: PUBLIC_READ` (senão o storefront não lê) + metafield `metaobject_reference` amarrando produto ao guia. Na PRLS: `guia_de_tamanhos` (def `20774388010`), `faq_prls` (def `20774420778`), namespace `prls`.
- **Ligar no tema é o passo que sempre falta.** O MCP Shopify escreve só em tema não-publicado (`themeFilesUpsert`/`themeDuplicate`); o MAIN é bloqueado. Crie a cópia, adicione `sections/prls-product-extras.liquid` + inclua no `templates/product.json`, valide no theme-check, confira no `?preview_theme_id=`. Publicar é decisão do Gustavo.

**RFM/ICP/Pareto** (PRLS OS: 980 customers, 6 tiers, ICP 3,8%, Pareto em heat-map)
- Sem histórico de pedido não há RFM (a ForYou só teve depois do sync de vendas: ticket médio ~R$9.966, 1.135 compradores). Calcule recência (dias desde a última compra), frequência (nº de pedidos) e valor (`total_value`/LTV).
- Segmentos no formato do CRM: `[{op, field, value}]` com `logic: AND` (ex: "VIP inativos p/ reativar (R$50k+, 120d+)"). O segmento vira público de régua ([[zap]]) ou linha de cockpit.

**obras Intec**
- Identifica o formato de entrega da Intec (planilha/export/API), ingere com dedup por identificador único de obra (não reimporte a base inteira), enriquece o que o portal usa (arquiteto, região, fase) e confirma que a obra nova aparece pro arquiteto certo.

## Gotchas
- Sync serverless sem checkpoint estanca em timeout/rate limit: por isso retomar, não reiniciar. Backfill resolve hoje, mas sem o fix durável no adapter o próximo cliente grande estanca de novo.
- PRLS Bling migrou ~abr/26 (99,6% dos pedidos com cidade): histórico antigo mora na planilha oficial, não no Bling. Não trate snapshot parcial como base completa.
- Criar metafield/metaobject sem ligar no tema = nada na PDP. Só conta renderizando. Metaobject sem `PUBLIC_READ` não é lido.
- Base sem `total_value`/vendas: dá pra segmentar só por cadastro, não por valor. Tier existe pra virar ação (disparo, oferta), senão é slide morto.
- Deixar dado chumbado no front em vez de ler a fonte é dívida: dado vivo é [[conserta-web]].

## O que NÃO fazer
- NÃO recomeçar sync travado do zero: retome do offset. NÃO dedup só por nome.
- NÃO disparar 3796 chamadas de uma vez.
- NÃO editar o tema Shopify publicado direto (use cópia + preview); NÃO mexer em preço/estoque/frete/cupom.
- NÃO fabricar RFM sem dado de compra real; migrar de outro CRM inteiro (RD Station) é [[crm]].
