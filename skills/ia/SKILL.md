---
name: ia
description: Use SEMPRE que o trabalho for IA dentro de um produto da Miner: ligar de verdade uma tela de IA que hoje é fachada (score com Math.random, análise hardcoded, prompt com botão copiar mas sem fetch, selo IA sem chamada), unificar qualquer provedor solto (OpenAI/Anthropic/Lovable, chave no front) no proxy único ai-json, ou criar/estender uma função de IA num produto (resumo, categorização, comentário do DRE, score). Dispara com "essa IA é de mentira", "o score é aleatório", "liga a IA de verdade", "isso é fachada", "migrar IA", "unificar IA", "tirar o OpenAI daqui", "consolidar as chaves de IA", "nova função de IA no produto <X>".
---

# ia: IA de verdade dentro dos produtos Miner

Padrão da casa: uma IA só, o proxy `ai-json` (edge no Supabase do minercrm), com um contrato JSON de saída. Esta skill liga IA real onde tem fachada, unifica provedores soltos nesse proxy, e encaixa função de IA nova em produto de forma segura. Três modos.

## Modos
- **liga (ia-real)**: tela marcada "IA" que não chama modelo nenhum (Math.random, hardcoded) passa a chamar o ai-json de verdade.
- **unifica (ia-unificada)**: troca qualquer provedor solto (api.openai.com, api.anthropic.com, gateway Lovable, chave no bundle) pelo ai-json único.
- **estende (produto-ia)**: cria/amplia função de IA dentro de um produto, aditiva e segura.

## Quando disparar
- "essa IA é fachada", "o score é aleatório com Math.random", "liga a IA de verdade".
- "migra/unifica a IA", "tira o OpenAI daqui", "por que cada tela usa uma IA diferente".
- "quero uma IA que faz Y no Content/Financeiro/Command Center", "adiciona resumo/categorização automática".

## Como executar
1. **Contrato ai-json.** Todo modo usa a edge `ai-json` no Supabase minercrm (`stpstwsqtuubpxvvexte`), modelo `gemini-2.5-flash-lite` por padrão, chave via `OPENROUTER_API_KEY` no cofre. A saída é JSON no shape que a tela já espera.
2. **Aditivo e com dry-run.** Nova função grava só numa coluna jsonb existente, nunca reescreve o produto. Rode dry-run antes de ligar.
3. **Fallback.** Se o modelo não responder ou vier fora do shape, sirva o fallback (último bom / valor neutro), nunca quebre a tela nem invente número.
4. **Sem provedor novo.** Nunca suba OpenAI/Anthropic/Lovable direto; tudo passa pelo ai-json. Sem chave no front.
5. **Cota.** Endpoint de IA sem contagem por usuário é brecha de custo: garanta o rate-limit ([[blindar]]).
6. **Testa antes de deployar** ([[deploy]]). Editar = deployar.

## Gotchas
- Score/nota/probabilidade com `Math.random` é o sinal clássico de fachada: é isso que o modo liga resolve.
- Prompt gigante com botão "copiar" e sem `fetch` também é fachada.
- ai-json tem contrato de saída fixo: respeite o shape ou a tela quebra silenciosa.

## O que NÃO fazer
- NÃO deixar provedor de IA solto nem chave no bundle.
- NÃO ligar IA em produção sem dry-run e sem fallback.
- NÃO criar endpoint de IA sem cota por usuário.
