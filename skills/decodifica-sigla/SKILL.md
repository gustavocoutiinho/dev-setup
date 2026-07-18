---
name: decodifica-sigla
description: Use SEMPRE que aparecer um código/sigla de projeto Asana da Miner (3-4 letras) sem cliente óbvio por trás. Dispara com "que cliente é <SIGLA>", "de quem é o projeto <SIGLA>", "decodifica essa sigla", "o que é PRCF/RDCA/MSJS", "esse código não tá no vault", ou quando um relatório ou cruzamento esbarra numa sigla desconhecida. Descobre o cliente real lendo nomes de tarefa e de pessoas: não chuta, confirma.
---

# decodifica-sigla: descobre o cliente por trás do código Asana

O Asana da Miner tem dezenas de projetos por sigla (3-4 letras) que não batem com nome de cliente. Esta skill descobre quem é o cliente real lendo o conteúdo das tarefas, sem chutar. Já resolvidos assim: TFLG=Trufflil, LZCV=Lezzcurve, LSSO=Lasso, CRAL=Cacau Real, EMRB=Educação Médica, BTCH=Butcher's, PRCF=Porão (conta Meta `act_3189492807980880`, "PRCF - GRUPO | BM1").

## Quando disparar
- Sigla Asana sem cliente mapeado no vault (`companies/` ou `reference_fontes_por_cliente`).
- Cruzamento ou relatório esbarra num código desconhecido.
- "Que cliente é <SIGLA>?", "de quem é esse projeto?".

## Como executar
1. **Consulta o mapa primeiro.** Veja `reference_fontes_por_cliente` e o dossiê `20-decodificacao-completa-clientes-asana` no [[obsidianminer]]: metade das siglas já está decodificada.
2. **Se não estiver, lê o Asana.** `get_projects` no workspace `1201866314544289`, depois `get_tasks` no projeto e leia os títulos: nome de loja, cidade, produto e pessoas revelam o cliente (ex: "loja Lezzcurve Fortaleza Sul" → LZCV).
3. **Cruza pessoas.** Nomes recorrentes nas tarefas (Milena=TFLG, Vanessa=LZCV) amarram a identidade.
4. **Confirma por outra fonte.** Grupo WhatsApp `G# Ⓜ️ <sigla> + Miner`, conta Meta ou owner do direto fecham a prova.
5. **Registra.** Grava a decodificação em `companies/<Cliente>.md` pra não redescobrir depois.

## Gotchas
- Sigla parecida não é a mesma operação: TRFT e TRFL são unidades distintas; confirme.
- Ex-cliente ainda tem projeto (DLT, LXNT, EMRB, GRBS): decodificar não quer dizer ativo (cheque `clientes-ativos-jul2026`).
- Conta Meta às vezes usa a sigla no nome ("PRCF - GRUPO | BM1"): ótimo sinal de confirmação.

## O que NÃO fazer
- NÃO afirmar o cliente por semelhança de letras: leia tarefa de verdade.
- NÃO tratar sigla decodificada como cliente ativo sem checar a carteira.
