---
name: cliente-novo
description: Use SEMPRE que um cliente novo entrar na operação Miner e precisar nascer com estrutura (contrato assinado, kick-off marcado, owner Miner definido). Dispara com "entrou cliente novo", "onboarding do <cliente>", "monta a operação do <cliente>", "fecha o setup do <cliente>", "cliente novo, começa a esteira", ou quando aparece uma sigla Asana nova sem projeto, pasta Drive, nota no vault nem grupo WhatsApp. Sequência quase fixa (PRCF, HDTS, SNBR): nada de improviso, tudo no padrão.
---

# cliente-novo: onboarding completo no padrão Miner

A Miner entra cliente o tempo todo (21 ativos hoje). Sem trilho, cada um nasce diferente: sigla sem projeto, dado solto, sem grupo, invisível nos sistemas. Esta skill roda a esteira de ~45 dias quase fixa (a mesma dos últimos: PRCF, HDTS, SNBR) pra o cliente nascer com governança.

## Quando disparar
- Contrato assinado, owner Miner (Caio/Davi/Rafael/ygor/Cecilia) e código Asana (3-4 letras) definidos.
- Sigla nova aparece sem projeto Asana, pasta Drive, nota `companies/` nem grupo WhatsApp.
- Gustavo diz "entrou cliente novo", "monta a operação do <cliente>".

## Como executar
1. **Contexto primeiro.** Puxe o [[obsidianminer]] pra ver se o cliente já existe no vault (não duplique). Registre na carteira `clientes-ativos-jul2026`.
2. **Projeto Asana no template.** Instancie o Kanban padrão via [[asana-kit]] (workspace `1201866314544289`, time Miner `1206315371746083`), owner como assignee.
3. **Semeia o setup.** Cria as tarefas fixas: pixel + catálogo, CRM ([[crm-org]]), WhatsApp/Zap.Guru (Suri/Omnichat/Chat.guru/Blip), acessos de leitura Meta/TikTok/GA4/Search Console, SEO, modelo de recebimento de leads + planilha de base.
4. **Pasta Drive** `/Clientes/<código>/` (01-Contrato ... 05-Reuniões).
5. **Nota vault** `companies/<Cliente>.md` + briefing Claude do cliente.
6. **Grupo WhatsApp** no naming `G1 Ⓜ️ <CLIENTE> + Miner | (contexto)`.

## Gotchas
- Slack `#cli-<código>` do SOP velho está morto: o canal real é WhatsApp. Não crie Slack.
- Sigla ambígua? Decodifique antes ([[decodifica-sigla]]): projeto duplicado suja o Asana.
- Acesso Meta só serve se a conta for "Oficial"; "Read-Only" devolve 0 insight.

## O que NÃO fazer
- NÃO subir criativo antes de mapear funil e conectar as leituras.
- NÃO deixar o cliente fora dos sistemas Miner (vira invisível).
- NÃO inventar owner nem código: confirme com o Gustavo.
