# Instruções globais do Claude Code — Gustavo Coutinho (Miner)

> Fonte única versionada em `~/dev/dev-setup/claude/CLAUDE.md`.
> Instalado em `~/.claude/CLAUDE.md` pelo `install-skills.sh`.
> Vale em TODAS as máquinas (Mac mini e MacBook) e em TODOS os projetos.

## Idioma: SEMPRE português brasileiro (pt-BR)

Escreva TUDO em português brasileiro, sem exceção. Não é só a resposta no chat: é todo texto que o Gustavo vê na interface.

- Respostas e explicações no chat.
- **Títulos de sessão / conversa** (o rename automático que aparece na lista lateral de sessões).
- **Títulos de capítulo** (`mark_chapter`) e seus resumos.
- **Nomes e descrições de tarefas / todos** (TodoWrite, task chips, títulos de tarefa spawnada).
- Mensagens de commit e descrições de PR quando o conteúdo é do Gustavo.
- Nomes descritivos de arquivos e artefatos de trabalho (decks, relatórios, docs, propostas).

Nunca gere títulos, nomes ou resumos em inglês para o trabalho do Gustavo. Se um termo técnico não tem tradução natural (deploy, commit, branch, funil, dashboard, pixel, etc.), mantenha o termo, mas a frase é em português.

Exceção: identificadores de código (nomes de variáveis, funções, chaves, slugs técnicos, nomes de branch git) seguem a convenção do projeto, não esta regra.

## Escrita

- **Sem travessão (em-dash `—`).** Troque por vírgula, dois-pontos, parênteses ou ponto final.
- Tom direto e objetivo. Não repita o que já foi dito nem narre o óbvio.

## Skills automáticas: a linguagem natural já puxa (não espere `/comando`)

Quando eu falar em linguagem natural, INVOQUE a skill relevante sozinho, ANTES de responder ou agir. Nunca me faça digitar `/skill` pra ativar. Em especial:

- **Qualquer assunto da Miner** (cliente, marca, projeto, portal, pessoa do time, sistema, MCP, automação, mídia, financeiro, deploy, onde mora o quê) → carregue o contexto com **`obsidianminer`** antes de responder. Nunca invente contexto: leia o vault primeiro.
- **Design, deck, proposta, relatório, página, "minerizar", "cara da Miner"** → **`minerdesign`**.
- **Análise/diagnóstico de Meta Ads** → **`meta-ads-analyzer`**. **Relatório/deck ACCS** → **`relatorio-accs`**. **Salesforce/LWC/Apex** → as skills `sf-*`.
- Na dúvida entre puxar ou não o contexto do vault: **puxe**. É melhor sobrar contexto do que responder sobre cliente/projeto sem saber o que já existe.
