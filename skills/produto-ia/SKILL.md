---
name: produto-ia
description: Molde pra criar ou estender uma função de IA dentro de um produto Miner (repurpose de conteúdo no Content, briefing no Command Center, auto-categorização no Financeiro, comentário do DRE, resumo/score num CRM), seguindo o padrão que já funciona: aditivo, com dry-run, gravando só numa coluna JSON existente, usando o proxy ai-json com fallback. Dispara em "nova função de IA no produto X", "quero uma IA que faz Y no Content/Financeiro/Command Center", "adiciona um resumo/categorização/comentário automático", "estende a IA do produto". Não reescreve o produto; encaixa a função com segurança.
---

# Produto IA (criar/estender função de IA num produto Miner)

Este é o molde pra encaixar uma função de IA nova num produto Miner sem quebrar o que roda. Segue o que já deu certo: **repurpose** no portal Content, **briefing** no Command Center, **auto-categorização** no Financeiro, **comentário do DRE**. Sempre aditivo, sempre com dry-run, gravando só em coluna JSON que já existe, usando o proxy **`ai-json`** (edge do Supabase minercrm `stpstwsqtuubpxvvexte`, secret `OPENROUTER_API_KEY`, modelo pago default `google/gemini-2.5-flash-lite`) com fallback.

## Quando disparar
- "Nova função de IA no produto X", "IA que faz Y no Content/Financeiro/Command Center/CRM".
- Pedido de resumo, categorização, briefing, comentário, score ou classificação automáticos dentro de um produto que já existe.
- Estender uma função de IA que já roda (mais um campo, outro produto).

## Padrão (as 5 regras do molde)
1. **Aditivo**: função nova, rota nova, coluna reaproveitada. Não altera fluxo existente nem shape que outra tela consome.
2. **Dry-run primeiro**: roda em N registros, mostra o que a IA produziria, **não grava**. Gustavo olha, aprova, aí liga a gravação.
3. **Grava só em coluna JSON existente**: ex. `ai_meta`, `metadata`, `enrichment`. Se não houver, adiciona **uma** coluna `jsonb` aditiva, nunca espalha colunas novas.
4. **ai-json com fallback**: chama o proxy; se falhar, deixa o registro sem o campo de IA (estado honesto), não quebra a tela nem inventa valor. Chave direta de provedor só se o produto já tiver uma e como fallback secundário.
5. **Cota**: se a função dispara por ação do usuário, passa pela `guarda-ia` (limite por usuário/dia).

## Como executar
1. **Ancore no produto real** (skill `obsidianminer`): leia a nota de stack do produto (`memory/portal-miner-content-stack.md`, `project_miner_command_center.md`, `project_financeiro_miner.md`, etc.) pra saber repo, banco e onde encaixar. Não invente caminho.
2. **Defina entrada → saída**: o que entra (o texto do post, a transação, a linha do DRE) e o JSON que sai (`{ categoria }`, `{ resumo, tags }`, `{ comentario }`).
3. **Escreva a função** com o system pedindo JSON no shape:
   ```ts
   async function categorizar(tx: Transacao) {
     const system = "Classifique a transação num plano de contas. Responda só JSON: { \"categoria\": string, \"confianca\": 0-1 }.";
     const r = await fetch(
       "https://stpstwsqtuubpxvvexte.supabase.co/functions/v1/ai-json?key=miner_ai_9f2c7b41",
       { method: "POST", headers: { "Content-Type": "application/json" },
         body: JSON.stringify({ system, user: JSON.stringify(tx), model: "google/gemini-2.5-flash-lite", temperature: 0.1 }) }
     );
     const { ok, data } = await r.json();
     return ok ? data : null; // fallback: sem categoria, revisão manual
   }
   ```
4. **Dry-run**: rode em 10-20 registros, imprima entrada + saída lado a lado. Gustavo valida a qualidade.
5. **Ligue a gravação** só na coluna JSON: `update <tabela> set ai_meta = ai_meta || :novo where id = :id`. Merge, não sobrescreve o objeto inteiro.
6. **Teste com dado real e deploy** com ok do Gustavo, da última main.

## Gotchas
- **Idempotência**: não recategorize o que já tem `ai_meta` preenchido, a menos que peçam reprocessar. Marque com timestamp/modelo pra rastrear.
- Batch/loop grande: paralelize com teto e respeite a cota; não dispare 3796 chamadas de uma vez (lembra do bug do Olist parando em 200/3796).
- `temperature` baixa (0.1-0.2) pra categorização/extração; mais alta só pra repurpose/copy.
- Comentário do DRE / briefing: dado sensível pode ir, o default é pago. Não rebaixe pra modelo grátis.
- Reuse coluna JSON existente antes de criar qualquer coisa.

## O que NÃO fazer
- Não reescrever o produto pra "encaixar melhor": a função é um enxerto aditivo.
- Não gravar sem dry-run aprovado.
- Não espalhar colunas novas por campo de IA: um `jsonb` resolve.
- Não criar chave/secret novo de provedor: o proxy ai-json é o caminho.
- Não deployar sem testar e sem ok do Gustavo.
