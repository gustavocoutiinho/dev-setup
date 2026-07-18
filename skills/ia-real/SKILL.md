---
name: ia-real
description: Pega uma tela de IA que é fachada (score aleatório com Math.random, "análise" hardcoded, prompt gigante com botão copiar mas sem fetch, selo "IA" sem chamada nenhuma) e liga de verdade no proxy ai-json da Miner, pra parar de vender IA que não roda. Dispara ao ver "Math.random" fingindo score/nota/probabilidade, tela com prompt estático e botão "copiar prompt", componente marcado "IA"/"powered by AI" sem nenhuma requisição, ou quando o Gustavo disser "essa IA é de mentira", "isso é fachada", "liga a IA de verdade", "o score é aleatório", "faz chamar o modelo". Testa antes de deployar.
---

# IA de verdade (tira a fachada, liga no ai-json)

Várias telas de IA da Miner são cenário: o "Score de lead" é `Math.random()`, a "análise" é texto fixo, o "assistente" mostra um prompt enorme com botão **copiar** (o usuário cola no ChatGPT na mão) e o selo "IA" não dispara request nenhum. Esta skill troca a fachada por uma chamada real ao proxy **`ai-json`** (edge do Supabase minercrm, projeto `stpstwsqtuubpxvvexte`, reusa o secret `OPENROUTER_API_KEY`, modelo pago default `google/gemini-2.5-flash-lite`).

## Quando disparar
- `Math.random()` (ou `Math.floor(Math.random()*100)`) alimentando score, nota, probabilidade, "confiança", "match".
- Prompt montado em string gigante só pra um botão `copiar`/`copy` (sem `fetch`/`await` depois).
- Componente/aba com rótulo "IA", "Análise inteligente", "powered by AI" e **zero** requisição de rede.
- Valor "de IA" que nunca muda entre reloads com a mesma entrada.

## Como executar
1. **Confirme que é mock**: `grep -rniE "math\.random|copiar prompt|copy.*prompt|// ?TODO.*IA|fake.*score|mock.*ai" <repo>`. Cheque no DevTools/Network que a tela não faz request ao abrir. Se não faz, é fachada.
2. **Descubra o que a tela promete**: qual número/texto ela deveria produzir (score 0-100? diagnóstico? categoria?) e com que entrada (o lead, o criativo, a linha do DRE).
3. **Escreva o system pedindo JSON no shape que a tela já renderiza**. Ex.: se a UI mostra `score` e `motivo`, peça exatamente `{ "score": number, "motivo": string }`.
4. **Ligue no proxy** no lugar do random/estático:
   ```ts
   async function pontuarLead(lead: Lead) {
     const system = "Você avalia potencial de compra de um lead B2B. Responda só JSON: { \"score\": 0-100, \"motivo\": string }.";
     const user = JSON.stringify(lead);
     const r = await fetch(
       "https://stpstwsqtuubpxvvexte.supabase.co/functions/v1/ai-json?key=miner_ai_9f2c7b41",
       { method: "POST", headers: { "Content-Type": "application/json" },
         body: JSON.stringify({ system, user, model: "google/gemini-2.5-flash-lite", temperature: 0.2 }) }
     );
     const { ok, data } = await r.json();
     if (!ok) return null;         // fallback: mostra "sem análise", NÃO volta pro random
     return data;                  // { score, motivo }, já parseado
   }
   ```
5. **Troque a UI**: onde tinha `Math.random()`, chame `pontuarLead`; trate loading e erro. O botão "copiar prompt" some (ou vira "gerar de novo").
6. **Grave o resultado se fizer sentido** numa coluna JSON existente (ex.: `leads.ai_meta`), pra não recalcular e pra rastrear. Aditivo, sem coluna nova se já houver uma de payload.
7. **Teste com entrada real e só então deploy** com ok do Gustavo.

## Gotchas
- **Fallback nunca volta ao aleatório.** Se o ai-json falhar, mostre estado honesto ("análise indisponível"), não um número inventado. A dor é justamente número fingido.
- Peça o **shape exato** que a tela renderiza; senão você troca um mock por um erro de `undefined`.
- Se o mock rodava no client a cada render, cacheie o resultado (estado/coluna) pra não chamar o modelo a cada re-render.
- Dado de cliente pode ir: o default é modelo pago. Não rebaixe pra modelo grátis.
- Chame `guarda-ia` junto se a tela dispara por ação do usuário sem limite (evita queimar crédito).

## O que NÃO fazer
- Não deixar o `Math.random` como "fallback".
- Não trocar a fachada por outra fachada (texto fixo "melhorado").
- Não criar chave nova de provedor: use o proxy ai-json.
- Não deployar sem ver a chamada real acontecendo no Network e sem ok do Gustavo.
