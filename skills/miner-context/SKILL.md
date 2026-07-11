---
name: miner-context
description: Carrega de uma vez o retrato operacional do Gustavo Coutinho e da Miner (MinerBZ): quem ele é, como trabalhar com ele (convenções e regras fixas), a stack e ferramentas que ele já usa, o time, os clientes ativos e onde vive o código. Use no INÍCIO de qualquer trabalho substantivo pra Miner, quando o Gustavo disser "usa meu contexto", "o que eu uso mesmo", "monta o setup", "me lembra das regras", ao abrir uma sessão nova/agente na nuvem que não tem a memória local dele, ou antes de escrever/deployar/decidir qualquer coisa em nome da Miner. Assim ele para de repetir as mesmas coisas toda hora.
---

# Miner Context (retrato operacional do Gustavo / MinerBZ)

Esta skill existe pra um motivo: o Gustavo não quer mais repetir as mesmas informações a cada sessão. Aqui está o retrato destilado do que ele é e do que ele usa. Trate como ponto de partida sempre-disponível. Para profundidade e o estado mais atual, o **vault é a fonte da verdade** (veja a skill `obsidianminer`); esta skill é o resumo que você carrega de cara.

## Quem é o Gustavo

Gustavo Simões Coutinho, fundador e arquiteto de negócios digitais. Fortaleza/CE. Empresa: **Miner (MinerBZ)**. Não é agência nem gestor de tráfego: é firma de arquitetura de operações digitais B2B/B2C (posicionamento, modelo comercial, CRM, processos, automação, dados, governança). Perfil analítico, causal, orientado à execução real. Baixa tolerância a diagnóstico genérico e recomendação sem base operacional.

Fonte completa: `~/ObsidianVaults/miner/OVW Miner.md` e `Cheat Sheet Miner.md`.

## Como trabalhar com ele (regras fixas)

Estas são regras que já foram ditas e valem sempre. Seguir sem precisar perguntar:

- **Sem travessão (em-dash).** Nunca use `—`. Troque por vírgula, dois-pontos, parênteses ou ponto final. Vale pra todo texto em nome dele.
- **Escrita direta**, sem enrolação, causal, aderente ao concreto. Detalhe em `memory/writing-style-gustavo.md`.
- **Identidade padrão sempre `gustavo@minerbz.com.br`** (login, commits, SSO). Nunca gmail.
- **Consulte o vault antes de agir** sobre cliente/projeto/pessoa/stack (skill `obsidianminer`).
- **Deploy: sempre da última `main`.** Antes de mexer em portal-accs/minercrm, branch da `origin/main` mais recente e confira produção. Nunca desfaça o que já está no ar.
- **GitHub é a nuvem do código.** `git pull` antes, `git push` depois. Repos ficam em `~/dev/`. Nunca `.git` dentro de iCloud/Dropbox/Drive.
- **Design MinerCRM: monocromático** (preto/branco/chumbo, sem azul), mantendo cores funcionais por usabilidade.

## Stack e ferramentas que ele usa

- **MinerOS (Supabase):** projeto `frocxapiowyjrdhlirnu`, região `sa-east-1`. Banco/razão da operação.
- **Vercel:** ~35 projetos (portais de cliente, cockpits, sistemas internos). Deploy de vários é só via CLI.
- **Notion:** Hub privado da Miner (DBs de automação em `memory/miner-automation-infra.md`).
- **4 MCPs custom de atendimento:** Suri, Omnichat, Chat.guru, Blip (multi-tenant via `miner_api_credentials`). Detalhes: `memory/miner-custom-mcps.md`, `miner-mcp-strategy.md`.
- **Mídia paga:** Meta Ads MCP LIVE (app Miner Ads, 206 contas, refresh manual via `~/.meta-ads/refresh.sh`); Google Ads pendente. Windsor.ai como conector (Meta + GAds + GA4). Ver `memory/ads-mcp-servers-setup.md`.
- **Produtos SaaS:** MinerCRM (Next.js + Supabase, multi-tenant, mantido por Thales Laray) e CRM legado crmminer. Ver `memory/project_nossocrm.md`, `project_minercrm_deploy_prod.md`.
- **Portais single-file / cockpits:** ACCS, Normatel, MSLZ, PIM/pimfood, Cockpit GB, Festival Costume Gourmet. Cada um tem nota de stack em `memory/` (ex.: `portal-accs-stack.md`).
- **Obsidian vault "miner"** como cérebro/PKM (Chief of Staff).

## Time (8 diretos)

Caio (operação ampla), Davi (squad próprio + ACCS), Rafael (carteira média), Raquel (Suri cross), Cecilia (MSLZ + Porão), Ricardo (LPs), Ygor (carteira em ramp up), Helia (a formalizar). Mapa vivo: `memory/miner-team-and-clients.md` e `Mundos/👥 Mundo Time.md`.

## Clientes ativos

Cada cliente tem nota em `~/ObsidianVaults/miner/companies/<Nome>.md` (com apelidos e códigos Asana no frontmatter). A lista viva e o status por cliente ficam em `companies/` (frontmatter `status`) e em `memory/miner-team-and-clients.md`: consulte lá em vez de confiar numa lista fixa aqui, porque carteira muda (cliente entra e sai). Não afirme que um cliente está ativo sem conferir a nota.

## Onde está tudo

- **Código:** `~/dev/` (cada projeto seu repo; GitHub é a nuvem).
- **Cérebro/PKM:** `~/ObsidianVaults/miner/`.
- **Memória do Claude:** `~/ObsidianVaults/miner/memory/` (índice `MEMORY.md`, já carregado por sessão).
- **Docs:** Google Drive. Princípio: fonte única, sem duplicação (Drive=docs / GitHub=código / vault=cérebro). Ver `memory/project_reorg_setup.md`.

## Como usar este contexto

1. Ao começar algo pra Miner, ancore no retrato acima em vez de perguntar o básico de novo.
2. Para o estado atual e detalhes de um cliente/projeto específico, use `obsidianminer` e leia a nota real: este resumo pode estar defasado, o vault não.
3. Antes de recomendar mexer em algo no ar (deploy, infra, integração), confirme a regra de deploy e leia a memória do projeto. O que já está em produção não se desfaz.
4. Escreva sempre no estilo dele: sem travessão, direto.
