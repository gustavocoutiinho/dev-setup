# Convenção de nomes Miner — fonte única

> Padrão de como nomear e organizar **todo projeto** da Miner em toda plataforma
> (GitHub, Vercel, `~/dev`). Objetivo: um projeto = **um nome só**, igual em todo lugar,
> fácil de achar. Decidido com o Gustavo em 11/07/2026.

## 1. Formato canônico

**`tipo-cliente`** em kebab-case minúsculo (só letras, números e hífen).

- **O mesmo slug** vale no GitHub, na Vercel e em `~/dev`. Nunca mais divergir.
- Ordena agrupando por tipo: todos os `deck-*` juntos, `portal-*` juntos, etc.
- Projetos internos da Miner (sem cliente externo) usam `-miner` como "cliente".

### Vocabulário de TIPO (prefixo)

| tipo | o que é | exemplo |
|---|---|---|
| `portal-` | portal operacional / SAC de cliente | `portal-accs` |
| `crm-` | CRM | `crm-normatel` |
| `deck-` | relatório / proposta / apresentação a cliente | `deck-barneys` |
| `site-` | site institucional | `site-miner` |
| `app-` | aplicação / ferramenta interna | `app-financeiro` |
| `mcp-` | servidor MCP | `mcp-blip` |
| `bot-` | bot | `bot-telegram` |
| `infra-` | setup / infraestrutura | `dev-setup` (exceção histórica) |

### Vocabulário de CLIENTE (slug fixo)

accs (Aço Cearense) · normatel · foryou · prls · stalker · barneys · estela · ollis ·
otorhinos · lesalis · festival · mslz (Grupo São Luiz) · pim · **miner** (interno)

> Regra da sigla: **ACCS** sempre com dois C (nunca "ACSC").

## 2. Regras fixas

1. **URL antiga sempre viva.** Nunca quebrar um link já publicado/enviado.
   - Projeto Vercel com **domínio próprio** (`*.minerbz.com.br`, `*.prls.com.br`):
     renomear o projeto é seguro, a URL pública não muda. ✅ renomeia à vontade.
   - Projeto que usa **só `*.vercel.app`** e já foi enviado a cliente (decks):
     **não** renomear o projeto Vercel (a URL morreria). Padroniza o nome no GitHub +
     `~/dev`, e o projeto Vercel ou fica como está, ou ganha um domínio custom novo
     padronizado (`deck-cliente.minerbz.com.br`) **mantendo** o `.vercel.app` antigo vivo.
2. **Favicon Miner (logo) em todo asset** com frontend. Fonte única do set oficial:
   `dev-setup/assets/favicon-miner/` (a montar a partir do set que já existe em
   `miner-website/favicon.*` e `festival-costume-gourmet/public/brand/`).
3. **`~/dev` em subpastas por tipo:** `portais/ decks/ crms/ sites/ apps/ mcps/ interno/`.
4. **Topics no GitHub:** cada repo recebe topic do tipo (`portal`, `deck`, `crm`, …) e do
   cliente (`accs`, `normatel`, …) pra filtrar (o GitHub não tem pastas).
5. **Rename de repo no GitHub** já cria redirect automático do nome antigo (não quebra
   `git clone`/remotes), mas ainda assim atualizo o `git remote` local pro nome novo.

## 3. Processo de rename seguro (por projeto)

1. GitHub: `gh repo rename <novo>` (redirect automático do antigo).
2. Local: `git remote set-url origin <nova-url>` + mover a pasta pra `~/dev/<tipo>/<novo>`.
3. Vercel: renomear **só** se tiver domínio custom (ou se for interno sem URL enviada).
   Caso contrário, manter e/ou adicionar domínio custom novo, deixando o `.vercel.app` vivo.
4. Favicon Miner aplicado no código.
5. Topics adicionados no GitHub.
6. Atualizar este de-para (coluna "feito").

---

## 4. DE-PARA (nome atual → canônico)

> 🌐 = domínio custom (rename Vercel seguro) · 📎 = só `.vercel.app` (cuidar da URL)
> · ⚙️ = confirmar na hora de executar o item (não bloqueia o piloto).

### Portais
| Canônico | GitHub hoje | Vercel hoje | ~/dev hoje | URL prod |
|---|---|---|---|---|
| `portal-accs` | portal-accs | portal-accs 🌐 | portal-accs | portal.minerbz.com.br |
| `portal-mig` | mig-portal | — | — | protótipo cliente MIG |
| `portal-mslz` | — | (loader) | — | servido por loader Vercel + Supabase (sem repo tradicional) ⚙️ |
| `portal-content` | miner-content | (Vercel) | — | Portal Miner Content (ex-Lovable) |
| `portal-miner-base` | miner-portal | — | next-shadcn-admin-dashboard | base reutilizável de portal |
| `site-prls` ⚙️ | prls-os | prls-os-site 📎 | — | prls-os-site.vercel.app (confirmar: é site da PRLS?) |

### Decks / propostas
| Canônico | GitHub hoje | Vercel hoje | ~/dev hoje | URL prod |
|---|---|---|---|---|
| `deck-accs` | accs-proposta | accs-proposta 🌐 (+ acsc-levantamento ⚙️) | accs-proposta | acomkt.minerbz.com.br |
| `deck-barneys` | barneys-proposta | barneys-proposta 📎 | barneys-proposta | barneys-proposta.vercel.app |
| `deck-estela` | estela-proposta | estela-proposta 📎 | estela-proposta | estela-proposta.vercel.app |
| `deck-ollis` | (criar repo) | ollis-proposta 📎 | — | ollis-proposta.vercel.app |
| `deck-otorhinos` | (criar repo) | otorhinos-proposta 📎 | otorhinos-proposta | otorhinos-proposta.vercel.app |
| `deck-normatel` | miner-proposta-normatel | normatel-proposta + normatel.mkt.miner 📎 | normatel-proposta | consolidar 3→1 |
| `deck-lesalis` | (criar repo) | lesalis-proposta 📎 | lesalis-proposta | lesalis-proposta.vercel.app |

### CRMs
| Canônico | GitHub hoje | Vercel hoje | ~/dev hoje | Nota |
|---|---|---|---|---|
| `crm-miner` | minercrm | minercrm 🌐 (crm.prls.com.br) | minercrm | o SaaS multi-tenant (marca MinerCRM) |
| `crm-miner-backup` | minercrm-private | — | — | mirror de backup |
| `crm-normatel` | normatel-premium | — | normatel-premium | "Normatel Premium" |

### Sites
| Canônico | GitHub hoje | Vercel hoje | ~/dev hoje | URL prod |
|---|---|---|---|---|
| `site-miner` ✅ | site-miner (novo, versionado) | miner-website 📎 (mantido: URL viva) | sites/site-miner | miner-website-beta.vercel.app (200) |

### Apps internos
| Canônico | GitHub hoje | Vercel hoje | ~/dev hoje | Nota |
|---|---|---|---|---|
| `app-command-center` | (—) ⚙️ | miner-command-center 📎 | miner-command-center | cockpit pessoal |
| `app-financeiro` | miner-financeiro | miner-controle 📎 | miner-financeiro / miner-financeiro-cloud | app avançado (Supabase/PTAX) — o "principal" |
| `app-financeiro-v1` | (—) | financeiro-miner 🌐 | (deploy do miner-financeiro) | v1 publicada à parte (financeiro.minerbz.com.br) — **manter separada** (decisão sua) ⚙️ |
| `app-mineros` | mineros | — | mineros | MinerOS orchestrator |
| `app-pim` | pimfood-onboard-zen | pimfood-onboard-zen 📎 | — | cockpit PIM (Vite SPA) |
| `app-foryou-olist` | miner-foryou-olist-backfill | — | — | script de backfill Olist |

### MCP / Bots
| Canônico | GitHub hoje | Nota |
|---|---|---|
| `mcp-blip` | miner-blip-mcp | MCP Blip |
| `mcp-whatsapp` | minerwpp | WhatsApp MCP |
| `bot-telegram` | -miner-bot | corrige o hífen inicial |

### Infra / interno
| Canônico | Hoje | Nota |
|---|---|---|
| `dev-setup` | dev-setup | mantém (fonte única de setup) |

### Arquivar — "só guardar" (fora do padrão, decisão do Gustavo)
Sem rename, sem favicon. Marcar como archived no GitHub + mover pra `~/dev/interno/arquivo/`.
- `crmminer` (CRM legado React+Vite+Express)
- `grbs-apresentacao` (cliente saiu)
- `antigrativity` · `mig1` · `miner-caminho-santiago` (pessoais / experimentais)
- `porao` / `dashboard-financeiro` (fora de uso — "não vou usar")

---

## 5. Piloto proposto

**`site-miner`** (hoje `miner-website`): interno, sem cliente, URL `.vercel.app` beta (não
enviada). Aplico o processo inteiro ponta a ponta com **risco zero**:
GitHub `miner-website`→`site-miner` (redirect automático) · `git remote` + pasta
`~/dev/sites/site-miner` · Vercel renomeia mantendo o `.vercel.app` antigo vivo · favicon
Miner · topics `site`+`miner`. Você confere, e aí escalo por tipo (decks → apps → portais →
crms), sempre com a URL antiga viva.

---

## 6. Status de execução (11/07/2026)

### ✅ Feito (grupos seguros — nenhuma URL de cliente tocada)
- **Piloto:** `site-miner` (versionado + pasta `sites/` + topics; URL de prod 200 intacta)
- **Decks:** `deck-barneys` `deck-estela` `deck-normatel` `deck-otorhinos` `deck-lesalis`
  (GitHub renomeado/criado + pasta `decks/` + topics; Vercel **intocada**, `.vercel.app` vivos)
- **Apps:** `app-pim` (era pimfood-onboard-zen) · `app-foryou-olist` (rename repo)
- **MCPs/bot:** `mcp-blip` · `mcp-whatsapp` · `bot-telegram` (era `-miner-bot`)
- **Arquivados** ("só guardar"): `crmminer` `antigrativity` `mig1` `miner-caminho-santiago`
  (archive no GitHub) + pastas movidas pra `~/dev/interno/arquivo/`

### ⏸️ A fechar quando você commitar o trabalho pendente (git sujo)
- `app-mineros` (era mineros) e `app-financeiro` (era miner-financeiro): **repo já renomeado**; falta mover a pasta pra `apps/` e atualizar o `git remote` (aponta pro nome antigo, que redireciona).
- `app-command-center` (miner-command-center): **sem repo GitHub** (não versionado) + pasta suja — versionar depois de commitar.

### ✅ Feito (2ª rodada — repos, sem tocar Vercel; URLs custom intactas)
- **`deck-accs`** (era accs-proposta) + pasta `decks/`. ⚠️ **Caso especial:** o deck ACCS ao vivo (`acomkt.minerbz.com.br`) é servido por um projeto Vercel SEPARADO `acomkt-deck` **com gate de "Acesso restrito"** — a pasta local (`accs-proposta`, que dá 404) NÃO é a fonte. Favicon Miner do deck-accs ao vivo pendente (não deployar a pasta por cima sem preservar o gate).
- **Portais/base:** `portal-mig` `portal-content` `portal-miner-base` (rename repo) · `portal-accs` (já canônico, + topics; portal.minerbz.com.br 200)
- **`crm-normatel`** (era normatel-premium; rename repo — pasta local suja, mover quando limpa)

### ✅ Feito (3ª rodada — "só faça")
- **`crm-miner`** (era minercrm): rename **do repo** + pasta → `~/dev/crms/crm-miner`. Projeto Vercel **intocado** (OAuth Bling da PRLS vivo); produção `minercrm.vercel.app` 200. ⚠️ **avisar o Thales** do nome novo (o redirect cobre enquanto isso).
- **`app-festival`** (era festival-costume-gourmet): repo + pasta → `~/dev/apps/app-festival`. Vercel intocada (DNS custom fora).

### ✅ Feito (4ª rodada) + arquivados
- **Renomeados:** `crm-miner-backup` (era minercrm-private) · `portal-normatel` (era normatel-portal; normatel.vercel.app 200 intacto) · `site-prls` (era prls-os).
- **Arquivados** (legado jan/2026, fora de uso): `porao` `dashboard-financeiro` `miner-proposta-porao`.

### ✅ Colisão de slug — resolvida com qualificador (repo only; ajuste se quiser)
Cliente com >1 projeto do mesmo tipo → acrescentei qualificador (rename reversível, produção intocada):
- `portal-normatel-b2b` (era miner-normatel; 2º portal Normatel, B2B/login/api)
- `deck-normatel-instagram` (era miner-proposta-normatel; IG orgânico)
- `deck-accs-central` (era miner-proposta-acocearense; central de atendimento — tem `server.js`, se preferir `portal-accs-central` é só avisar)

Regra fixada: quando há >1 do mesmo `tipo+cliente`, acrescentar qualificador.

### ⏳ Resta (passe cuidadoso / fora do meu alcance seguro)
- **Favicon em produção:** portais, apps, `crm-miner` (editar + deploy de produção ativa) e `deck-accs` (gate `acomkt-deck`).
- `portal-mslz` (loader, sem repo tradicional) · `ollis` (só Vercel) · `claude-setup` (duplicado meu — deletar no GitHub, falta `delete_repo` scope).
- ⚠️ `crm.prls.com.br` e `festival.minerbz.com.br` respondem 000 (DNS do domínio custom, **preexistente**; apps vivos pelo `.vercel.app`).

### 📋 Passes dedicados (à parte)
- **Favicon Miner:** set oficial montado em `dev-setup/assets/favicon-miner/` ✅. Aplicado + deployado (URL intacta) em **5 decks**: `deck-barneys` `deck-estela` `deck-otorhinos` `deck-normatel` `deck-lesalis` ✅. Decisão: favicon Miner em TUDO (troca o logo do cliente na aba). Pendente: `deck-accs` (gate acomkt-deck), portais/apps de cliente (no checkpoint).
- **`site-miner` na Vercel:** renomear quando definir o domínio custom do site.
- **ollis-proposta:** só existe na Vercel (`.vercel.app`), sem repo/pasta — nada a padronizar fora da Vercel.
