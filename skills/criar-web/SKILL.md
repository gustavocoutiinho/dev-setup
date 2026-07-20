---
name: criar-web
description: Use SEMPRE que for criar do zero qualquer coisa web de cliente na Miner: portal ou app, landing de vertical em lote, cockpit multi-departamento, site institucional, dashboard rápido de leads/funil/kanban, portal guarda-chuva multi-marca, a visão-gestor de um portal, ou um bloco de pré-orçamento. Dispara com "cria um portal/site/app/landing/cockpit/dashboard do <cliente>", "monta o site do <cliente>", "gera as LPs das verticais", "portal multi-marca", "guarda-chuva de marcas", "visão gestor", "placar dos vendedores no portal", "pré-orçamento sem Excel", "ACSC-OPS-001", "começa o <projeto> do zero". Nasce no padrão (repo + Vercel + Supabase + favicon Miner + KV + domínio + gate). NÃO é editar web que já existe (isso é [[conserta-web]], [[faxina-web]] ou [[blindar]]).
---

# criar-web: qualquer web de cliente nascendo no padrão Miner

A Miner cria web de cliente o tempo todo (34+ projetos na Vercel). Sem um trilho, cada peça nasce diferente: nome fora do padrão, sem repo, dado chumbado, exposto. Esta skill faz qualquer web nova (portal, landing, cockpit, site, dashboard, umbrella, visão-gestor, pré-orçamento) nascer certa desde o primeiro commit.

## Modos
- **portal/app** (portal-kit): a casa completa de cliente, com dado vivo e área logada.
- **landing em lote** (lp-kit): página de captura por vertical/nicho, várias da mesma casca.
- **cockpit multi-departamento** (cockpit-kit): visão de gestor com nav por área (financeiro, clientes/RFM, mídia, marca).
- **site institucional** (site-kit): apresentação estática que capta contato, sem login.
- **dashboard rápido** (dash-kit): uma tela single-file de leads/funil/kanban, descartável.
- **umbrella multi-marca** (umbrella-kit): casca guarda-chuva que hospeda N marcas isoladas.
- **visão-gestor** (cockpit-gestor): persona de gestão dentro de um portal (meta x realizado, placar, funil).
- **pré-orçamento** (pre-orcamento): bloco num portal que troca a planilha Excel por registro no Supabase.

## Quando disparar
- "cria/monta/começa do zero" um portal, site, app, landing, cockpit, dashboard, umbrella ou pré-orçamento de cliente.
- Trabalho começa sem repo, sem projeto Vercel e sem domínio; ou vai clonar algo existente pra um cliente/nicho novo.
- NÃO use pra editar web que já existe: dado desatualizado ou página pesada é [[conserta-web]], dedup/consolidação é [[faxina-web]], brecha de segurança é [[blindar]].

## Como executar
Comum a todos os modos:
1. **Contexto primeiro.** Puxe o cliente no [[obsidianminer]] (quem é, stack, lead Miner, o que já existe). Nunca invente.
2. **Nome no padrão.** Slug `tipo-cliente` (ex: `portal-normatel`, `cockpit-prls`) idêntico em GitHub, Vercel e `~/dev`. URL antiga viva. Cheque duplicado/canônico com [[faxina-web]] (3 CRMs paralelos já viraram desperdício).
3. **Repo primeiro (GitHub é a nuvem).** Repo em `~/dev`, git init, primeiro commit. Nada de projeto sem repo.
4. **Stack da casa.** Next.js 14 (App Router) ou HTML single-file conforme o peso. Supabase MinerOS (`frocxapiowyjrdhlirnu`) ou projeto dedicado. Sem Lovable.
5. **Identidade.** KV Miner (ou a marca do cliente quando for entregável dele) via [[minerdesign]] + favicon Miner.
6. **Dado vivo, não snapshot.** Se serve dado de cliente, já nasce lendo a fonte por edge ([[dados]]), não colado no front.
7. **Gate + domínio + deploy.** PII ou área logada exige gate real ([[blindar]], magic link Workspace SMTP). Aponta `<slug>.minerbz.com.br`, deploya da última `main` (Vercel exige commit verificado) e confirma a URL no ar ([[deploy]]). Editar = deployar.

O que muda por modo:
- **portal/app:** a casca completa acima.
- **landing em lote:** casca única, troca hero/copy/prova/oferta por nicho, nome `<cliente>-<nicho>-lp`. Ref: as 8 LPs do MIG (medicina, higienista, fisio, farmácia, prótese, mls, webinares, credit-journey + dr-dream BR/LATAM + speak-english, batch de 25/abr). O form TEM que gravar o lead num destino real (Supabase/CRM), nunca só toast; consentimento LGPD nunca nasce marcado. Pixel/GA4 por vertical antes de rodar mídia.
- **cockpit multi-departamento:** nav lateral por departamento, nome `cockpit-<cliente>` ou `<cliente>-os`, cada aba lê a fonte real. RFM/base via [[dados]] (tiers, ICP, Pareto). Refs: PRLS OS (/financeiro DRE/DFC/simuladores, /clientes 980 customers em 6 tiers, /marca), pimfood-onboard-zen (3 marcas x meses), cockpitgb (Movimento & Funil + Auditoria + Raio-X via Omnichat por edge). Product-led: defina quem opera pós-entrega e como cobra manutenção.
- **site institucional:** estático React/Vite ou HTML em `~/dev/sites/<slug>`, sem login. Refs: site-miner e fcg-site (LIVE costumegourmet.minerbz.com.br). SEO básico (title, og:image, sitemap), contato que grava o lead (não `wa.me` cego), performance via [[conserta-web]].
- **dashboard rápido:** single-file HTML+JS, views tabela filtrável/funil por etapa/kanban por status, lê a fonte viva por edge. Deploy só se precisar compartilhar. Se serve PII, exige gate ([[blindar]]).
- **umbrella multi-marca:** casca base + roteamento por marca (`/marca` ou subdomínio) + isolamento de dado por marca. Refs: Portal Guarda-Chuva (separado do portal-accs) e ACCS GP. Teste que a marca A nunca enxerga dado da marca B.
- **visão-gestor:** dashboard de gestão (não grid de leads) dentro de um portal. Ref canônica: Cockpit do Gestor ACCS em `~/dev/portal-accs/index.html` (`window.GESTOR_COCKPIT`, container `#cn-view-gestor`, `cn_applyPersonaView('gestor')`), fontes `/api/prospec/funil-sf` (PROSPEC_LIVE) + `/api/caca-negocio/pipeline`, metas em `window.PROSPEC_METAS` (300t). 5 KPIs + placar de vendedores + funil do mês.
- **pré-orçamento:** bloco num portal existente que mata a planilha Excel (regra ACSC-OPS-001). Supabase MinerOS: `acsc_preorcamentos` + `acsc_preorcamento_itens` (FK cascade), view `v_acsc_preorcamentos_recentes` (90d), numeração `PO-YYYY-NNNN`, RLS só service_role. Edge `acsc-preorcamento` (guard `?key=`), totais server-side, cross-fill kg↔un por bitola (CA-50/CA-60), pedido mínimo 4.000 kg.

## Gotchas
- Deploy só do `index.html` num portal com `/api` quebra todas as rotas (caso portal-accs): deploya a pasta inteira.
- PII sem sessão não é "portal pronto", é vazamento: chama [[blindar]] junto.
- Antes de criar, confirme que não existe um canônico ([[faxina-web]]): 3 CRMs paralelos já foram desperdício.
- Form/dashboard bonito que não faz POST engole o lead; consentimento LGPD nunca pré-marcado.
- Umbrella: vazamento cruzado entre marcas é o risco número 1; isole as fontes desde o início.
- Cockpit: aba que nunca carrega dado (painel silencioso) é pior que não ter; valide cada fonte antes de entregar.
- Visão-gestor: conversão por QUANTIDADE de negócios (~17%), NUNCA por tonelada (positivado_t/orçado_t dá ~2% falso, distorcido por cotações gigantes). Risco/crédito vem do `funil-sf` (`cur.credito`/`cur.recusado`), são toneladas, rotule "t". Motivo de perda é `ClosingReason__c`, não `Loss_Reason__c` (vazio). Não use "pipeline por estágio" (quase tudo fica em "Em Rascunho").
- Pré-orçamento: totais SEMPRE server-side (o client não fecha conta); tabela é service_role, sem policy anon.

## O que NÃO fazer
- NÃO subir projeto sem repo git (quebra "GitHub é a nuvem").
- NÃO usar Lovable nem provider fora do padrão Vercel + Supabase.
- NÃO chumbar dado real no front pra "funcionar hoje".
- NÃO expor financeiro/clientes/PII sem sessão real (chama [[blindar]]).
- NÃO duplicar cockpit/portal/umbrella que já existe para o cliente ([[faxina-web]]).
- NÃO deployar sem confirmar a URL no ar.
