---
name: cliente
description: Use SEMPRE que o trabalho for ciclo de vida de cliente na Miner: onboarding de cliente novo (esteira 45 dias), offboarding/churn (desligar tudo do ex-cliente), instanciar o projeto no template Kanban do Asana, ou decodificar uma sigla de projeto. Dispara com "entrou cliente novo", "onboarding do <cliente>", "monta a operação do <cliente>", "o <cliente> saiu", "desliga o ex-cliente", "cria o projeto no Asana", "que cliente é a sigla <X>".
---

# cliente: ciclo de vida de cliente na Miner

A Miner entra e sai de cliente o tempo todo (21 ativos hoje) e cada ponta (Asana, Drive, vault, grupo, CRM, crons, anúncios) precisa nascer e morrer no padrão. Sem trilho, cliente novo fica invisível nos sistemas e ex-cliente vaza operação: cron rodando, anúncio no ar, grupo aberto. Esta skill cobre o ciclo inteiro por modos.

## Modos
- **onboarding**: cliente novo entra e nasce com governança (esteira de ~45 dias, a mesma de PRCF, HDTS, SNBR).
- **offboarding/churn**: ex-cliente sai e desliga tudo que ainda consome operação, sem hard-delete.
- **template Asana**: instancia o Kanban padrão clonado de um projeto vivo.
- **decodificar sigla**: descobre o cliente real por trás de um código Asana de 3-4 letras.

## Quando disparar
- "entrou cliente novo", "monta a operação do <cliente>", contrato assinado + owner Miner + código Asana definidos, para onboarding.
- "o <cliente> saiu", "desliga o ex-cliente", ex-cliente detectado num cron/anúncio/grupo, para offboarding.
- Passo "projeto Asana" do onboarding, ou "clona a estrutura do BNYS/PRLS", para template.
- Sigla sem cliente óbvio ("que cliente é <SIGLA>?"), para decodificar.

## Como executar
Comum: puxe o cliente no [[obsidianminer]] antes de agir (não duplique, não invente). Sigla ambígua se decodifica antes de criar ou arquivar projeto.

**onboarding**
1. Registra na carteira `clientes-ativos-jul2026`; confirma owner (Caio/Davi/Rafael/ygor/Cecilia) e código (3-4 letras).
2. Projeto Asana no template (modo abaixo), owner como assignee.
3. Semeia as tarefas fixas: pixel + catálogo, org no CRM ([[crm]]), WhatsApp (Suri/Omnichat/Chat.guru/Blip via [[zap]]), acessos de leitura Meta/TikTok/GA4/Search Console, SEO, modelo de recebimento de leads + planilha de base.
4. Pasta Drive `/Clientes/<código>/` (01-Contrato ... 05-Reuniões); nota `companies/<Cliente>.md`; grupo WhatsApp `G1 Ⓜ️ <CLIENTE> + Miner | (contexto)`.
5. Entregáveis do cliente (portal, deck) sobem no padrão via [[deploy]].

**offboarding/churn**
1. Org no CRM: soft-delete, nunca hard. `DELETE /api/admin/organizations/[id]` marca `deleted_at` + `pending_deletion`, reversível ([[crm]]).
2. Arquiva (não deleta) o projeto Asana e os grupos WhatsApp (DLT, Tallis, Lasso, Cacau, MGTC pendentes).
3. Desliga os crons `miner-weekly-report-<sigla>` no pg_cron do MinerOS `frocxapiowyjrdhlirnu` (o `miner-weekly-report-mgtc` roda toda segunda pra ex-cliente). É o que mais vaza ([[monitor]]).
4. Pausa campanhas Meta/Google ainda no ar (Luxo e Sodine ficaram por esquecimento). Revoga acessos (Meta BM, GA4, CRM, e-commerce) e libera a capacity do owner.
5. Marca churn: `companies/<Cliente>.md` status "ex-cliente" e tira de `clientes-ativos-jul2026`. Pendências (crédito de mídia, última fatura) no [[monitor]].

**template Asana**
- Workspace `1201866314544289`, time Miner `1206315371746083`, hub de demanda "Solicitações de trabalho" `1206414904890927`.
- Esqueleto Kanban: `BACKLOG → TO DO → IN PROGRESS → DONE` + `SITE` + `Reuniões/Alinhamento Semanal`. Clone de um projeto vivo (BNYS `1206341323578421`, PRLS `1206341556294506`), não monte do zero.
- Variações conscientes só por porte: NMTL (board por área), ACSC (Scrum com emojis). O default é o Kanban simples.

**decodificar sigla**
- Consulta primeiro o mapa `reference_fontes_por_cliente` e o dossiê `20-decodificacao-completa-clientes-asana`: metade já está decodificada.
- Se não, `get_projects`/`get_tasks` no workspace `1201866314544289` e lê os títulos (loja, cidade, produto, pessoas). Nomes recorrentes amarram (Milena=TFLG, Vanessa=LZCV). Já resolvidos: TFLG=Trufflil, LZCV=Lezzcurve, LSSO=Lasso, CRAL=Cacau Real, PRCF=Porão (Meta `act_3189492807980880`).
- Confirma por grupo WhatsApp / conta Meta / owner e grava em `companies/<Cliente>.md`.

## Gotchas
- Slack `#cli-<código>` do SOP velho está morto: o canal real é WhatsApp. Não crie Slack.
- Acesso Meta só rende com conta "Oficial"; "Read-Only" devolve 0 insight.
- Org com conta `@minerbz.com.br` não desativa pelo endpoint: trate à parte.
- GRBS teve acesso combinado até 30/07: respeite a data de corte, não desligue antes. Sodine pediu reunião pós-saída (encerramento, não reativação).
- Sigla parecida não é a mesma operação (TRFT não é TRFL). Ex-cliente ainda tem projeto (DLT, LXNT, EMRB, GRBS): decodificar não quer dizer ativo, cheque `clientes-ativos-jul2026`.
- Asana é tudo manual: 0 AI Teammates no workspace. Não prometa automação de board que não existe.

## O que NÃO fazer
- NÃO hard-delete de org, dado, projeto Asana ou grupo: soft-delete ou arquiva, sempre reversível.
- NÃO deixar cron ou anúncio de ex-cliente vivo (é dinheiro e dado vazando).
- NÃO subir criativo antes de mapear funil e conectar as leituras.
- NÃO inventar owner, código ou cliente por semelhança de letras: confirme no Asana e com o Gustavo.
