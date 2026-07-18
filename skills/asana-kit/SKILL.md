---
name: asana-kit
description: Use SEMPRE que precisar criar ou padronizar um projeto no Asana da Miner (cliente novo, frente nova, ou arrumar um projeto fora do molde). Dispara com "cria o projeto do <cliente> no Asana", "monta o Kanban", "instancia o template", "põe no padrão do Asana", "clona a estrutura do BNYS/PRLS", ou dentro do onboarding quando o passo é o projeto Asana. Esqueleto clonado idêntico em BNYS, OTRH, LSL, PRLS, HDTS, 4YOU, PRCF: nasce igual, não improvisado.
---

# asana-kit: projeto Asana no template Kanban padrão

Todo cliente Miner tem projeto Asana no mesmo esqueleto. Esta skill instancia esse molde pra o projeto nascer clonado dos que já rodam (BNYS, OTRH, LSL, PRLS, HDTS, 4YOU, PRCF), não montado do zero cada vez.

## Quando disparar
- Passo "projeto Asana" do [[cliente-novo]], ou frente nova precisando de board.
- Projeto existente bagunçado, fora do esqueleto padrão.
- "Clona a estrutura do <projeto>", "põe no molde do Asana".

## Como executar
1. **Coordenadas.** Workspace `1201866314544289`, time Miner `1206315371746083`. Hub de entrada de demanda: projeto "Solicitações de trabalho" `1206414904890927`.
2. **Esqueleto Kanban padrão (seções):** `BACKLOG → TO DO → IN PROGRESS → DONE` + `SITE` + `Reuniões/Alinhamento Semanal`. Este é o default; clone de um projeto vivo (ex: BNYS `1206341323578421`, PRLS `1206341556294506`).
3. **Owner + assignee.** Owner Miner do cliente como assignee primário; adicione os diretos da carteira.
4. **Código no nome.** Nome com a sigla padrão (3-4 letras) igual em Asana, Drive e vault ([[cliente-novo]]).
5. **Variações por porte.** Conta grande vira board por área (padrão NMTL) ou Scrum com emojis nas seções (padrão ACSC). Só use variação se o volume pedir.

## Gotchas
- Hoje é tudo manual: 0 AI Teammates no workspace. Não prometa automação de board que não existe.
- Não crie projeto sem antes decodificar a sigla ([[decodifica-sigla]]): duplicado suja a carteira.
- NMTL (por área) e ACSC (Scrum) são exceções conscientes, não o default. O default é o Kanban simples.

## O que NÃO fazer
- NÃO inventar seção fora do esqueleto sem motivo (quebra a comparabilidade entre clientes).
- NÃO montar do zero quando dá pra clonar um projeto vivo.
- NÃO usar workspace ou time diferentes dos gids acima.
