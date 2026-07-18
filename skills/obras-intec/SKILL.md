---
name: obras-intec
description: Use SEMPRE que precisar incluir obras novas da Intec na Base de Obras da Normatel. Dispara com "ingere as obras novas", "atualiza a Base de Obras", "puxa a Intec", "entrou obra nova da Intec", "sincroniza as obras". Alimenta o motor de arquitetos/obras da Normatel Premium sem redigitar.
---

# obras-intec: ingestão de obras novas da Intec

A Normatel trabalha com uma Base de Obras que alimenta o portal de arquitetos (Normatel Premium). Obras novas chegam via Intec e precisam entrar na base sem digitação manual. Esta skill é a receita dessa ingestão.

## Quando disparar
- "ingere as obras novas", "atualiza a Base de Obras", "puxa a Intec", "entrou obra nova".
- Cadência de atualização da base de obras da Normatel.

## Como executar
1. **Contexto** no [[obsidianminer]]: como a Base de Obras está modelada e onde a Normatel Premium consome ([[dado-vivo]]).
2. **Fonte Intec:** identifica o formato de entrega das obras novas (planilha/export/API).
3. **Ingestão com dedup** ([[ingere-base]]): casa obra por identificador único, evita duplicar obra que já existe, faz backfill do que falta.
4. **Enriquece** os campos que o portal usa (arquiteto, região, fase da obra).
5. **Confirma no portal:** a obra nova aparece pro arquiteto certo, sem quebrar o que já estava.

## Gotchas
- Sem dedup, a mesma obra entra duas vezes e polui o ranking/base do portal.
- Base de Obras é dado vivo: o portal deve ler a fonte, não um snapshot recolado a cada ingestão.

## O que NÃO fazer
- NÃO reimportar a base inteira quando só faltam as obras novas.
- NÃO duplicar obra por falta de chave única.
- NÃO chumbar as obras no front da Normatel Premium.
