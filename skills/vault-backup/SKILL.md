---
name: vault-backup
description: Use SEMPRE que for salvar/versionar o vault Obsidian da Miner ou garantir que o cérebro está seguro no GitHub. Dispara com "backup do vault", "commita o cérebro", "salva o vault", "versiona o Obsidian", "o vault está seguro?", "sobe o vault pro GitHub". GitHub é a nuvem do código; nunca .git em iCloud/Drive.
---

# vault-backup: backup versionado do cérebro Miner

O vault `~/ObsidianVaults/miner` é o cérebro da operação e precisa estar sempre versionado no GitHub. Esta skill mantém o backup em dia com segurança, respeitando a cicatriz do incidente iCloud de 13/07 (arquivo dataless que sumiu).

## Quando disparar
- "backup/commita/salva o vault", "versiona o Obsidian", "o cérebro está seguro?".
- Depois de uma sessão que mexeu bastante no vault.

## Como executar
1. **Status primeiro.** `git -C ~/ObsidianVaults/miner status` pra ver o que mudou.
2. **Commit em pt-BR** descrevendo o que entrou (ex: "captura da varredura de skills 18/07").
3. **Pull antes de push** (GitHub é a nuvem): evita divergência entre Mac mini e MacBook.
4. **Push** pro remote do vault.
5. **Integridade:** nunca `rm` de arquivo original sem antes um `gzip -t`/checagem; nunca opere arquivo dataless do iCloud (baixe primeiro).

## Gotchas
- Incidente 13/07: `rm` num arquivo iCloud não baixado apaga sem volta. Confirme que o arquivo está materializado antes de qualquer remoção.
- `.git` NUNCA em iCloud/Drive: corrompe o repo. O vault fica fora de pasta sincronizada por serviço de arquivo.
- Duas máquinas: sempre pull antes de push pra não sobrescrever o trabalho da outra.

## O que NÃO fazer
- NÃO deixar o vault dias sem commit.
- NÃO `rm` original sem checar integridade primeiro.
- NÃO colocar o repo git dentro de iCloud/Drive.
