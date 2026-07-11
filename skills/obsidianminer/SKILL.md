---
name: obsidianminer
description: Use SEMPRE que a conversa tocar em qualquer coisa da Miner/MinerBZ (cliente, marca, projeto, portal, pessoa do time, sistema, MCP, automação, mídia, financeiro, deploy) ANTES de responder ou agir, E também quando o Gustavo quiser carregar TODO o contexto de uma vez. Dispara com /obsidianminer, "carrega meu cérebro", "contexto total", "puxa o vault", "olha no obsidian", "o que a gente sabe sobre X", ou ao citar clientes como ForYou, Aço Cearense, Normatel, Stalker, GRBS, Maresia. Lê o vault Obsidian antes de afirmar; nunca inventa contexto.
---

# ObsidianMiner (contexto do vault "miner")

Toda a inteligência da operação Miner vive num vault Obsidian: `~/ObsidianVaults/miner/` (487 notas, ~318k palavras). Esta skill é a porta única pra esse cérebro. **O objetivo do Gustavo é parar de repetir contexto:** se você responder de memória e errar um detalhe (quem é o lead, a stack, o que está no ar), você quebra exatamente a dor que ele quer resolver. Leia o vault primeiro.

Ela tem **dois modos**. Escolha pelo que a situação pede:

| Modo | Quando | O que fazer |
|---|---|---|
| **TOTAL** (cérebro inteiro) | Ele pede o contexto todo, começo de trabalho pesado, ou você quer o panorama antes de decidir | Rode o loader (abaixo) |
| **CIRÚRGICO** (só o relevante) | A conversa cita 1-2 entidades específicas (um cliente, um projeto, uma pessoa) | Ache e leia só a(s) nota(s) daquilo |

## Modo TOTAL
Carrega a espinha dorsal (MOCs da raiz + os 8 Mundos + Status Agora + Cheat Sheet + CoS Manual) e os índices de tudo que existe, num output só (~12k palavras):
```bash
bash ~/.claude/skills/obsidianminer/scripts/load-context.sh
```
Leia esse output inteiro. Depois, se precisar de detalhe de algo citado nos índices, aprofunde como no modo cirúrgico.

## Modo CIRÚRGICO
1. **Identifique a entidade**: cliente/marca, projeto/portal, pessoa, sistema/MCP/automação, ou tema (mídia, financeiro, deploy).
2. **Ache a nota** (pare ao achar): caminho direto `companies/<Nome>.md` (cuidado com acentos e apelidos: ForYou = 4YOU, Aço Cearense = ACCS); senão `grep -ril "<nome>\|<alias>\|<asana_code>" ~/ObsidianVaults/miner`; senão abra o `Mundo` da área e siga os wikilinks. Cheque também `memory/MEMORY.md` (já em contexto) e leia a nota de memória correspondente (tem gotchas/decisões que não estão no código).
3. **Leia o que importa** (nota do cliente + nota de memória costumam bastar). Arquivos grandes: leia só a seção relevante (`offset`/`limit`), não despeje inteiro.
4. **Sintetize um briefing curto** (o que é, status, stack, lead Miner, gotchas) e **cite os caminhos** dos arquivos lidos.

## Regras
- **Leia antes de afirmar.** Nunca diga "a stack do cliente X é Y" sem abrir a nota. Se a nota não existir ou estiver vazia, diga isso, não preencha o vazio.
- **O vault é a fonte da verdade viva**, não sua memória de conversas. Notas de memória refletem o que era verdade quando escritas: se citam arquivo/flag/rota, confirme que ainda existe antes de recomendar.
- **Não edite o vault** a menos que o Gustavo peça (regras de escrita no vault: `reference_obsidian_vault`).
- **Estilo do Gustavo** em qualquer texto em nome dele: sem travessão (vírgula, dois-pontos, parênteses ou ponto), direto, sem enrolação.

## Estrutura do vault (pra navegar)
- `companies/<Cliente>.md` — nota por cliente. Frontmatter: `status`, `aliases`, `asana_codes`, `asana_lead_miner`.
- `Mundos/*.md` — hubs por área (Clientes, Projetos, Sistemas, Time, Operação, Marketing, Estratégia, Pessoal). Bom ponto de partida quando não sabe o nome exato.
- Raiz: `Cheat Sheet Miner.md`, `OVW Miner.md`, `Status Agora.md`, `Proximas Acoes Priorizadas.md`, `CoS Operating Manual.md`, `MOC *`.
- `people/`, `projects/`, `team/`, `stack/`, `dossier/`, `memory/` (índice `memory/MEMORY.md`), `+Inbox/` (capturas recentes).

## Se o vault não estiver lá
O loader aponta erro se `~/ObsidianVaults/miner` não existir (iCloud não baixou, outra máquina). Confirme com `ls ~/ObsidianVaults` antes de seguir.
