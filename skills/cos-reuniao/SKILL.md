---
name: cos-reuniao
description: Use SEMPRE que o Gustavo tiver uma transcrição ou áudio de reunião (de projeto, cliente ou demanda) pra virar action items e tasks no Asana. Dispara com "processa essa reunião", "transforma a transcrição em tasks", "tira os action items dessa call", "roteia essa reunião", "cria as tasks da reunião do <cliente>", "o que ficou dessa reunião". As ~120 reuniões/mês não podem virar só anotação parada no Gemini.
---

# cos-reuniao: transcrição de reunião vira action items e tasks Asana

Hoje ~120 reuniões/mês viram só anotação no Gemini e morrem ali: decisão sem registro, action item sem dono. Esta skill transforma a transcrição em registro + action items + tasks Asana com o assignee certo. O destino é o Granola Router automático; até o OAuth conectar, roda manual.

## Quando disparar
- "processa essa reunião", "tira os action items", "cria as tasks da reunião do <cliente>".
- Qualquer transcrição/áudio de reunião de projeto, cliente ou demanda a debriefar.

## Como executar
1. **Contexto.** Playbook "Granola Router" (Notion, página `36e12a5d-1b46-81b2-b1d1-e36766ee01fc`). Cliente/projeto via [[obsidianminer]].
2. **Classifique o projeto** da reunião. Se 2+ projetos sem um dominante, trate como standalone (registro único, tasks roteadas por projeto).
3. **Extraia:** decisões (com racional, quem decidiu), action items (cada um com dono e prazo), riscos com severidade.
4. **Crie a task Asana** com o assignee certo pelo mapping cliente→owner (`context/cos-config.md`; ex: NMTL→Caio, PRLS→Gustavo, TRFT→Rafael, GRBS→ygor). Workspace `1201866314544289`. "Source: Reunião <projeto> YYYY-MM-DD" na descrição.
5. **Salve** o registro e leve decisões grandes ao Decision Log. Debrief antes de salvar: conversa com o Gustavo primeiro.

## Gotchas
- **OAuth Granola PENDENTE:** a edge `meeting-router` só entra no ar quando o OAuth Granola conectar (`context/pendings.md`). Registre e cobre em [[radar-bloqueios]]; até lá é 100% manual.
- Todo action item tem dono. Prazo é confirmado com o Gustavo, não assumido.
- Trecho inaudível marca `[inaudível]`, não preenche com suposição.

## O que NÃO fazer
- Não deixar a reunião virar anotação parada (essa é a dor que a skill mata).
- Não criar task sem assignee nem prazo.
- Não registrar decisão só de boca: decisão por escrito ou não aconteceu.
