---
name: salesforce
description: Use SEMPRE que o trabalho for desenvolvimento na plataforma Salesforce (usada na Aço Cearense): Apex (classes, triggers, testes), deploy via Salesforce CLI (sf, sandbox, scratch org), ou Lightning Web Components (LWC). Dispara com "mexe no Apex", "cria a trigger", "escreve o teste de Apex", "deploya no Salesforce", "sobe pra sandbox", "sf deploy", "cria o LWC", "componente Lightning", "conserta o LWC". Guia técnico de desenvolvimento SF no padrão da casa.
---

# salesforce: desenvolvimento na plataforma Salesforce

A Aço Cearense roda em Salesforce, e o portal da Miner lê o SF (funil, conversões). Esta skill guia o desenvolvimento SF no padrão: Apex, deploy por CLI e LWC. Três modos. Consolida as antigas `sf-apex-development`, `sf-cli-deployment` e `sf-lwc-development` (e corrige o `name` que divergia da pasta).

## Modos
- **apex**: classes, triggers e testes em Apex, seguindo o style guide NimbleUser.
- **cli**: deploy e teste via Salesforce CLI (`sf`), em sandbox / scratch org antes de produção.
- **lwc**: Lightning Web Components (criar/modificar componentes).

## Quando disparar
- "mexe no Apex", "cria a trigger", "escreve o teste", "cobertura de teste".
- "deploya no Salesforce", "sobe pra sandbox", "sf deploy", "scratch org".
- "cria/conserta o LWC", "componente Lightning".

## Como executar
1. **Contexto** do cliente/org via [[obsidianminer]] (a org SF ativa é a ACCS; o portal consome o funil via [[relatorio]]).
2. **Apex**: siga o padrão NimbleUser (nomenclatura, bulkificação, sem SOQL/DML em loop, uma trigger por objeto com handler). Toda classe com teste e cobertura real, não teste vazio.
3. **CLI**: use `sf` para deploy. SEMPRE valide em sandbox / scratch org antes de produção. Rode os testes no deploy.
4. **LWC**: componentes com dados via Apex (`@AuraEnabled` cacheável quando fizer sentido), sem lógica de negócio no front.
5. **Deploy com verificação**: nunca suba pra produção sem os testes passando e sem revisar o diff.

## Gotchas
- SOQL/DML dentro de loop estoura o governor limit: bulkifique sempre.
- Teste que não faz asserção real infla a cobertura sem proteger nada.
- Mudança direta em produção sem sandbox é risco: valide antes.

## O que NÃO fazer
- NÃO fazer SOQL/DML em loop.
- NÃO subir Apex sem teste com asserção real.
- NÃO deployar em produção sem validar em sandbox/scratch org primeiro.
