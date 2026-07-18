---
name: inbox-processa
description: Use SEMPRE que o +Inbox do vault Miner acumular capturas soltas pra classificar e distribuir. Dispara com "processa o inbox", "o que caiu no +Inbox?", "organiza as capturas", "distribui o que está no inbox", "limpa o +Inbox". Cada item vira arquivo no lugar certo (companies/projects/people) ou uma ação, e o inbox fica vazio.
---

# inbox-processa: triagem do +Inbox do vault

O `+Inbox/` do vault `~/ObsidianVaults/miner` acumula captura rápida: alertas, drafts de mensagem, notas cruas, decisões pendentes. Esta skill processa esse acúmulo, classifica cada item e manda pro lugar certo, seguindo o SOP cos-inbox-process.

## Quando disparar
- "processa/limpa o inbox", "o que caiu no +Inbox?", "distribui as capturas".
- Início de sessão de organização, quando o +Inbox está cheio.

## Como executar
1. **Lista o +Inbox** e lê cada item (via [[obsidianminer]]).
2. **Classifica:** é sobre cliente (vai pra `companies/`), projeto (`projects/`), pessoa (`people/`), decisão (Decision Log), ou é um draft de mensagem que aguarda disparo?
3. **Distribui** pro arquivo canônico, fundindo se já existe ([[memoria-consolida]]), com frontmatter e wikilinks corretos.
4. **Ação pendente vira tarefa** clara (Asana ou lista priorizada), não fica solta no inbox.
5. **Draft de mensagem** fica marcado como aguardando disparo: nunca enviar por conta própria (regra do Gustavo, envio só por ordem item a item).
6. **Esvazia:** item processado sai do +Inbox.

## Gotchas
- Alerta P0 no inbox (credencial exposta, WhatsApp violando política) tem prioridade: trata antes de arquivar.
- Draft pronto não é permissão de envio: só dispara com ordem explícita por item.

## O que NÃO fazer
- NÃO enviar mensagem que estava como draft sem ordem por item.
- NÃO deixar item processado duplicado no +Inbox.
- NÃO classificar sem ler (capa engana).
