---
name: edge-ia
description: Use SEMPRE que for criar do zero uma edge function de IA no Supabase (o scaffold cru do proxy ai-json ou uma edge irmã que chama o modelo), não encaixar IA num produto que já existe. Dispara com "cria uma edge de IA", "scaffold da ai-json", "monta o proxy de IA no Supabase", "uma edge function que chama o modelo", "preciso de uma function serverless de IA do zero". É o esqueleto cru: a função de IA DENTRO de um produto é a [[produto-ia]].
---

# edge-ia: scaffold cru de edge de IA (proxy ai-json)

Este é o esqueleto de uma edge function de IA no Supabase minercrm, o padrão do proxy `ai-json`. É o scaffold CRU: encaixar IA num produto que já roda é a [[produto-ia]]; trocar provedor solto pelo proxy é a [[ia-unificada]].

## Quando disparar
- "Cria uma edge de IA", "scaffold da ai-json", "proxy de IA no Supabase", "function serverless de IA do zero".
- NÃO use pra estender IA num produto existente ([[produto-ia]]) nem pra migrar provedor solto ([[ia-unificada]]).

## Como executar
1. **Edge no Supabase minercrm** (`stpstwsqtuubpxvvexte`), `verify_jwt=false`, auth por `?key=miner_ai_9f2c7b41` na URL (não é segredo). Reusa o secret `OPENROUTER_API_KEY` que já existe: não cria chave nova.
2. **Contrato**: `POST {system, user, model?, temperature?}` → `{ok, data (JSON parseado), usage}`. Proxy burro de chave, sem lógica de negócio.
3. **Provedor**: OpenRouter (base `https://openrouter.ai/api/v1`, conta gustavo@minerbz.com.br), API compatível com OpenAI. Modelo default `google/gemini-2.5-flash-lite` (pago, não treina: pode passar dado de cliente).
4. **Sempre JSON**: o `system` pede resposta só em JSON no shape que o consumidor lê.
5. **Aditivo + dry-run**: grava só em coluna `jsonb` JÁ existente (`ai_meta`/`metadata`); roda em N registros e mostra antes de ligar a gravação.
6. **Fallback honesto**: se a IA falhar, `ok=false` e o registro fica sem o campo (não quebra a tela, não inventa valor).
7. **Deploy da edge** + teste com dado real + ok do Gustavo.

## Gotchas
- Modelo pago é o default: NÃO rebaixar pra free com dado de cliente (free pode treinar).
- Batch grande: paralelize com teto e respeite a cota ([[guarda-ia]]); não dispare milhares de chamadas de uma vez (bug Olist parando em 200/3796).
- `temperature` 0 a 0.2 pra extração/classificação; mais alta só pra copy.
- O segredo real fica DENTRO da edge; a `key` da URL pode ir no front sem medo.

## O que NÃO fazer
- Não criar secret/chave nova de provedor: reusa `OPENROUTER_API_KEY`.
- Não pôr lógica de negócio no proxy: ele é burro, o produto é que decide.
- Não gravar sem dry-run aprovado.
- Não reescrever o boilerplate de edge do zero: use [[edge-kit]] pro esqueleto base.
