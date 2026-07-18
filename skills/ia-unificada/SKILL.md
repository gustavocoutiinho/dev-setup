---
name: ia-unificada
description: Troca QUALQUER provedor de IA solto (api.openai.com, api.anthropic.com, ai.gateway.lovable.dev, chaves OpenAI/Anthropic no front) pelo proxy único da Miner, a edge ai-json no Supabase minercrm, consolidando custo e chaves numa fonte só. Dispara ao ver esses provedores em código de portal/produto da Miner (portal-accs, portal-miner-base, Ann.ai, portal-hub) ou quando o Gustavo disser "migrar IA", "unificar IA", "tirar o OpenAI daqui", "consolidar as chaves de IA", "passar pro ai-json", "por que cada tela usa uma IA diferente". Mantém o mesmo contrato JSON de saída; não inventa provedor novo.
---

# IA unificada (tudo pelo proxy ai-json)

Hoje cada tela de IA da Miner fala com um provedor diferente: OpenAI direto no `portal-accs` e no `portal-miner-base`, Anthropic no "Ann.ai", Lovable AI Gateway no `portal-hub`. Isso espalha chave, espalha custo e ninguém enxerga o gasto. Esta skill troca essas chamadas pelo **proxy único da Miner**, mantendo o mesmo contrato de saída (JSON), sem chave nova no front.

O proxy é a edge function **`ai-json`** no Supabase minercrm (projeto `stpstwsqtuubpxvvexte`). Ela reusa o secret `OPENROUTER_API_KEY` (já existe no projeto): você não cria nem expõe chave nenhuma. Modelo default `google/gemini-2.5-flash-lite`, **pago** (não treina com os dados), então pode passar dado de cliente.

## Quando disparar
- Vi `api.openai.com`, `openai.ChatCompletion`, `new OpenAI(`, `api.anthropic.com`, `x-api-key` de Anthropic, ou `ai.gateway.lovable.dev` em repo da Miner.
- Vi uma chave `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `LOVABLE_API_KEY` embutida ou lida no front.
- Gustavo pediu pra unificar/migrar/consolidar IA ou "tirar o OpenAI".

## Como executar
1. **Ache todas as chamadas**: `grep -rniE "openai\.com|anthropic\.com|gateway\.lovable|OPENAI_API_KEY|ANTHROPIC_API_KEY|LOVABLE_API_KEY" <repo>`.
2. **Para cada chamada, guarde o contrato**: o `system`, o `user`/prompt, e o **formato de JSON** que o código consome depois. O ai-json já devolve JSON parseado, então some com o `JSON.parse(resp.choices[0].message.content)`.
3. **Substitua pelo proxy** (mesmo system/user):
   ```ts
   // DEPOIS: vale pra OpenAI, Anthropic ou Lovable, todos viram isto:
   const r = await fetch(
     "https://stpstwsqtuubpxvvexte.supabase.co/functions/v1/ai-json?key=miner_ai_9f2c7b41",
     { method: "POST", headers: { "Content-Type": "application/json" },
       body: JSON.stringify({ system, user, model: "google/gemini-2.5-flash-lite", temperature: 0.2 }) }
   );
   const { ok, data, usage } = await r.json();
   if (!ok) throw new Error("ai-json falhou");
   // `data` já é o JSON parseado; use no lugar do parse antigo
   ```
   Antes disso o código tinha algo como `openai.chat.completions.create({model, messages:[{role:"system"...},{role:"user"...}]})` e um parse manual. O `system` e o `user` são os mesmos; só muda o transporte.
4. **Peça JSON no system**: o ai-json espera resposta JSON. Se o prompt antigo não pedia JSON explícito, acrescente ao system "Responda só com JSON no formato {…}" com as chaves que o front consome.
5. **Teste antes de deployar**: rode a mesma entrada real e confira que `data` bate com o shape antigo. Só depois, deploy com ok do Gustavo (da última main, ver `feedback_deploy_sempre_da_ultima_main`).

## Gotchas
- **É aditivo, não é rewrite.** Troque só a camada de chamada; não reescreva a tela nem mude o shape que o resto do código espera.
- Se o provedor antigo devolvia texto livre (não JSON), o ai-json força JSON: ajuste o consumidor ou peça no system um campo `{ "texto": "..." }`.
- `temperature` default do ai-json serve; só passe explícito se a tela pedia criatividade (repurpose, copy).
- O `model` é opcional (default gemini-2.5-flash-lite). Só troque se a tarefa exige mais capacidade e o Gustavo topar o custo maior.
- Chave `miner_ai_9f2c7b41` na URL é do proxy, não é segredo de provedor: pode ir no front. O segredo real (`OPENROUTER_API_KEY`) fica só dentro da edge.

## O que NÃO fazer
- Não criar chave nova de OpenAI/Anthropic nem novo secret: o proxy já resolve.
- Não deixar duas rotas convivendo (metade OpenAI, metade proxy) "por segurança": migra e apaga a chamada antiga na mesma passada.
- Não deployar sem testar a saída real e sem ok do Gustavo.
- Não mandar dado de cliente pra modelo gratuito/que treina: o default do ai-json é pago, mantenha assim.
