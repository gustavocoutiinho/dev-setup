---
name: relatorio-inteligente
description: Use quando o Gustavo pedir pra "comentar o desempenho", "escrever o resumo executivo do relatório", "o que aconteceu nesse mês", "tem alguma anomalia?", "alertar quando ROAS/CPL sair do padrão", "pergunte aos números", "explica esse resultado pro cliente", ou ao gerar/atualizar qualquer relatório ou deck e faltar a leitura em texto dos números. Via ai-json (IA da Miner), transforma o dump de métricas em comentário de desempenho, alerta de anomalia, resumo executivo e Q&A sobre os próprios números. Dispara sempre que um relatório tiver dados mas não tiver a narrativa.
---

# relatorio-inteligente · a leitura em texto dos números

## O que faz
Pega o **dump de métricas já apurado** (do report-data, do JSON do deck-vivo, ou de um export
Meta) e gera 4 saídas em pt-BR: (1) comentário de desempenho, (2) alerta de anomalia,
(3) resumo executivo, (4) "pergunte aos números" (Q&A). Tudo pela IA da Miner, nunca inventando
número: a IA só interpreta o que está no dump.

## IA da Miner (ai-json)
Endpoint único:
```
POST https://stpstwsqtuubpxvvexte.supabase.co/functions/v1/ai-json?key=miner_ai_9f2c7b41
corpo: { "system": "...", "user": "<dump + pergunta>", "model?": "google/gemini-2.5-flash-lite", "temperature?": 0.2 }
resposta: { "ok": true, "data": { ... } }   # data já vem em JSON estruturado
```
Modelo padrão `google/gemini-2.5-flash-lite` (OpenRouter). `temperature` baixa (0.1–0.3) pra
comentário e alerta; a resposta sempre estruturada (peça JSON no system).

## Base analítica (obrigatória): meta-ads-analyzer
Para qualquer leitura de Meta Ads, aplicar a lente da skill **meta-ads-analyzer**, sobretudo o
**Breakdown Effect**: NÃO recomendar pausar/cortar segmento só porque o CPA/CPM médio está mais
alto (custo médio alto ≠ desempenho ruim; costuma ser o sistema pegando custo marginal baixo
antes). Avaliar no nível certo (CBO = campanha; sem CBO = conjunto), marginal sobre média,
holístico antes de drilar. Toda recomendação é hipótese testável com evidência de dado, não
ordem.

## Como executar
1. **Reunir o dump** (números apurados + período + período de comparação). Nunca peça pra IA
   "buscar" dado: ela só lê o que você mandar.
2. **Comentário de desempenho:** system pede um parágrafo objetivo por bloco (mídia, orgânico,
   funil), citando o número e a variação vs período anterior. Sem adjetivo vazio; todo elogio
   ou alerta ancorado no dado.
3. **Alerta de anomalia:** mande limiares no user (ex. ROAS caiu >30% vs média móvel; CPL
   acima do teto do cliente; frequência > X). A IA retorna `{ "alertas": [{ "metrica", "valor",
   "esperado", "severidade", "hipotese" }] }`. Hipótese sempre pela lente Breakdown Effect.
4. **Resumo executivo:** 2 a 3 achados no topo, linguagem de dono/cliente, sem jargão de
   plataforma. Estrutura do meta-ads-analyzer (achados → diagnóstico → recomendação testável).
5. **Pergunte aos números:** Q&A onde a pergunta do Gustavo/cliente vai no user junto do dump;
   a IA responde só com o que dá pra derivar do dump, e diz "não dá pra afirmar com esses dados"
   quando faltar base.
6. **Escrita Miner:** pt-BR, sem travessão (—), sem emoji em material de cliente. Números com
   máscara pt-BR (milhar com ponto, decimal com vírgula).

## Gotchas
- **A IA não é fonte de número.** Se um valor não está no dump, ela não pode citar; peça no
  system pra ela sinalizar lacuna em vez de estimar.
- **Nível de avaliação errado gera conclusão errada** (Breakdown Effect). Informe no dump se é
  CBO/campanha ou conjunto; a leitura muda.
- **Learning phase / amostra pequena:** poucos eventos = achado preliminar. Peça pra IA
  ressalvar quando o volume for baixo.
- **ai-json pode devolver `ok:false`** ou texto fora do JSON: valide `data` antes de usar; se
  vier sujo, baixe a temperature e reforce "responda só JSON" no system.
- **Sem PII no prompt:** não jogar telefone/email de lead no ai-json; mande só métrica agregada.

## NÃO fazer
- Não deixar a IA inventar ou "completar" número ausente.
- Não recomendar cortar segmento por CPA/CPM médio alto (Breakdown Effect).
- Não usar emoji nem travessão em texto que vai pro cliente.
- Não mandar dado sensível/PII pro endpoint.
