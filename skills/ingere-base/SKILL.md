---
name: ingere-base
description: Use SEMPRE que for ingerir/importar uma base de clientes de Olist/Tiny, Bling ou planilha pra dentro de um CRM/portal Miner, ou quando um sync existente travou no meio. Dispara com "importa a base do <cliente>", "sobe os contatos do Olist/Bling", "o sync parou na metade", "faltou nascimento/telefone nos contatos", "enriquece a base", "dedup dos contatos", "o import estancou em N de M". Ingere com dedup e retoma de onde parou, sem duplicar nem recomeçar do zero.
---

# ingere-base: ingestão de base com dedup e retomada

Ingerir base de cliente (Olist/Tiny, Bling, planilha) é recorrente e sempre tropeça nas mesmas pedras: o detalhe não roda pra toda a base e a régua/RFM fica sem dado; ou o sync trava no meio e alguém recomeça do zero. Esta skill ingere com dedup e checkpoint, retomando do offset em vez de reprocessar tudo.

## Quando disparar
- "importa a base do <cliente>", "sobe os contatos do Olist/Bling", "enriquece a base", "o sync parou / estancou em N de M".
- Contatos sem nascimento/telefone depois de um import (cobertura baixa).

## Como executar
1. **Contexto da fonte** ([[obsidianminer]]): Olist/Tiny V2 tem 2 níveis, `contatos.pesquisa.php` (lista leve, sem nascimento) + `contato.obter.php` (detalhe, com nascimento/telefone/CPF). O caso ForYou parou o detalhe em **200/3796** e deixou 3.596 `pending`.
2. **Dedup na entrada:** telefone em **E.164** (padrão `stalker_norm_phone`) e/ou **CPF** como identificador primário (RPC `resolve_contact_id_by_cpf`, nome só fallback). CPF > telefone > nome.
3. **Chunked com checkpoint:** processe em lotes com time-budget, marque o offset e **retome do offset**, nunca recomece. Respeite o rate limit (Tiny ~30-40 req/min, Bling ~3 req/s, retry no 429).
4. **Enriquecimento não-destrutivo:** preencha campo vazio, não sobrescreva bom dado. Marque sentinela (`{_enrich:'not_found'}`) em quem sumiu da fonte.
5. **Cron pra ongoing** via [[edge-kit]]; **desagende quando `remaining=0`** (senão roda idle pra sempre).

## Gotchas
- Sync serverless sem checkpoint estanca em timeout/rate limit: por isso retomar, não reiniciar.
- PRLS Bling migrou ~abr/26 (99,6% dos pedidos com cidade): histórico antigo mora na planilha oficial, não no Bling. Não trate snapshot parcial como base completa.
- Backfill imediato resolve hoje; sem o **fix durável** no adapter, o próximo cliente grande estanca de novo.
- Migrar de outro CRM inteiro (RD Station) é [[crm-migra-rd]], não só ingestão de arquivo.

## O que NÃO fazer
- NÃO recomeçar um sync travado do zero: retome do offset.
- NÃO dedup só por nome: E.164/CPF primeiro.
- NÃO disparar 3796 chamadas de uma vez.
