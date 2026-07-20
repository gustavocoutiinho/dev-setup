---
name: vault
description: Use SEMPRE que o trabalho for cuidar do cérebro/vault Obsidian da Miner: consolidar/limpar a memória (nota duplicada, MEMORY.md desalinhado do que existe em memory/), processar o +Inbox (classificar e distribuir as capturas), ou backup versionado do vault no GitHub. Dispara com "consolida a memória", "limpa o vault", "tem nota duplicada?", "organiza a memória", "processa o inbox", "o que caiu no +Inbox?", "distribui as capturas", "backup do vault", "commita o cérebro", "salva o vault", "o vault tá seguro?".
---

# vault: cuidar do cérebro Obsidian da Miner

O vault `~/ObsidianVaults/miner` é a memória viva da operação. Esta skill mantém ele são: memória sem duplicata, +Inbox vazio e distribuído, backup seguro no GitHub. Três modos.

## Modos
- **memória**: acha duplicata/sobreposição e funde no arquivo canônico; princípio de fonte única (unificada 17/06).
- **inbox**: triagem do `+Inbox/`, cada captura vai pro lugar certo ou vira ação.
- **backup**: versiona o vault no GitHub com segurança.

## Quando disparar
- "consolida/limpa/organiza a memória", "tem nota duplicada?", "unifica isso".
- "processa/limpa o inbox", "o que caiu no +Inbox?", "distribui as capturas".
- "backup/commita/salva o vault", "versiona o Obsidian", "o cérebro tá seguro?".

## Como executar
**Sempre:** leia o vault via [[obsidianminer]] antes de mexer. Não invente.

**Modo memória:** cruze `memory/MEMORY.md` (índice, uma linha por nota) com os arquivos reais em `memory/`. Ache duplicata, funde no canônico (o mais completo), preservando `**Why:**`/`**How to apply:**` de feedback/project, linkando as relacionadas por wikilink. Delete o duplicado, corrija o `MEMORY.md`. Frontmatter `type: user|feedback|project|reference`; datas relativas viram absolutas. Nota recente sobre carteira/estado sobrepõe o diretório antigo.

**Modo inbox:** liste o `+Inbox/`, leia cada item, classifique (companies/projects/people/Decision Log/draft) e distribua pro arquivo canônico com wikilinks. Ação pendente vira tarefa clara. Draft de mensagem fica marcado como aguardando disparo, nunca enviar por conta própria. Esvazie o item processado.

**Modo backup:** `git -C ~/ObsidianVaults/miner status`, commit em pt-BR, pull antes de push (duas máquinas), push. Integridade: nunca `rm` de original sem checar antes; nunca opere arquivo dataless do iCloud.

## Gotchas
- MEMORY.md nunca guarda conteúdo, só o índice de uma linha.
- Incidente 13/07: `rm` num arquivo iCloud não baixado apaga sem volta; confirme materializado antes.
- `.git` NUNCA em iCloud/Drive: corrompe o repo.
- Draft pronto não é permissão de envio.

## O que NÃO fazer
- NÃO criar nota nova quando já existe uma pro tema.
- NÃO enviar mensagem que estava como draft sem ordem por item.
- NÃO deixar o vault dias sem commit, nem `rm` original sem checar integridade.
