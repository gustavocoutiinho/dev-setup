---
name: alerta-atrasos
description: Use SEMPRE que houver task do Asana vencida ou arrastando há semanas sem ninguém cobrar, ou na rotina de checar o que está atrasado. Varre as tasks do Gustavo no Asana, junta as vencidas por projeto e marca "⚠️ RECORRENTE" a que reaparece varredura após varredura (o backlog real: 21 tasks em NMTL+NMPR, 12 vencidas, a mais antiga de 14/04). Dispara com "o que tá atrasado", "quais tasks minhas venceram", "tem coisa arrastando?", "me cobra os atrasos", "o que tá parado há semanas", "backlog vencido".
---

# alerta-atrasos: o que venceu no Asana e ninguém cobrou

Task vencida no Asana não avisa sozinha: some no meio da lista. Numa varredura real o Gustavo tinha **21 tasks em NMTL+NMPR, 12 vencidas, a mais antiga de 14/04** (6+ semanas parada). Esta skill varre periodicamente, junta os atrasos e cobra, com destaque pro que vira crônico. Ela aponta, não fecha nem reagenda por conta própria.

## Quando disparar
- Rotina (encaixa no daily-briefing, `miner-daily-briefing` 06:30 BRT) ou "o que tá atrasado / me cobra os atrasos".
- Ao revisar backlog, capacidade ou preparar 1:1.
- Gustavo perguntou o que venceu, o que arrasta, o que parou.

## Como executar
1. **Puxe as tasks do Gustavo** via Asana (MCP `get_my_tasks` / owner `gustavo@minerbz.com.br`), `completed=false`.
2. **Filtre vencidas:** `due_on < hoje` no fuso America/Sao_Paulo (não UTC, senão vira meia-noite errada).
3. **Agrupe por projeto** (NMTL, NMPR, os ~23 que ele é owner) e ordene por atraso, a mais antiga primeiro.
4. **Marque "⚠️ RECORRENTE"** a task que aparece na varredura **3+ vezes seguidas** (a mesma task, não recriada). Persista a contagem por `task gid` numa nota do vault (`~/ObsidianVaults/miner`) pra sobreviver entre sessões.
5. **Avise** DM Slack / WhatsApp / linha no daily-brief, com a lista curta: projeto, título, dias de atraso, flag recorrente. Registre em `Status Agora.md`.

## Gotchas
- **Recorrente ≠ recriada:** conte pela mesma `gid` ao longo do tempo. Sem persistir a contagem, toda varredura zera e nada nunca é "recorrente".
- **Owner certo:** o Gustavo é owner de ~23 projetos; não misture task delegada ao time com task dele.
- Task sem `due_on` não é atraso, é task sem prazo: sinalize à parte, não como vencida.

## O que NÃO fazer
- NÃO fechar, reatribuir ou reagendar task sozinho ([[cos-capacity]] cuida de redistribuir carga).
- NÃO repetir a lista inteira todo dia: cobre o que mudou e o recorrente.
- NÃO cobrar em 1:1 sem antes cruzar com a capacidade do time ([[cos-1on1]]).
