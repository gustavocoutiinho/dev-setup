---
name: raiox
description: Use SEMPRE que o trabalho for análise ou diagnóstico completo de performance digital de um cliente, cruzando redes sociais (orgânico e concorrentes) com site, e-commerce e conversão, no padrão anti-alucinação com comparação temporal obrigatória, scorecard, ranking de conteúdo/página/produto, funil de conversão e plano de ação priorizado. Dispara com "faz um raio-x digital do <cliente>", "análise de performance completa", "o que melhorou ou piorou no período", "compara com os concorrentes", "monta o scorecard", "por que esse resultado aconteceu", "quais são os gargalos", "relatório com plano de ação priorizado", "cruza as redes sociais com o site". Não é diagnóstico de campanha isolado (isso é [[midia]]) nem a fundação técnica de dado vivo (isso é [[relatorio]]): é a leitura analítica de cima, que consome o que essas duas já entregam.
---

# raiox: raio-x completo de performance digital

Framework analítico único (13 seções) pra transformar dados de redes sociais, concorrentes, site e e-commerce num relatório técnico, comparável e orientado à decisão. Responde sempre: o que melhorou/piorou, o que gerou resultado, por quê, onde está o gargalo, o que manter/parar/corrigir/testar/ampliar, e o que o concorrente está explorando que ainda não é aproveitado.

Não substitui [[midia]] (diagnóstico de campanha isolada) nem [[relatorio]] (fundação técnica que liga a fonte e mantém o dado vivo): este raio-x **consome** o que as duas entregam e cruza tudo. A metodologia completa (princípios anti-alucinação, fórmulas de engajamento ponderado, outlier score, funil de conversão, scorecard, estrutura do relatório final) está em `metodologia.md`, prompt mestre fornecido pelo Gustavo em 23/07/2026. Leia esse arquivo inteiro antes de montar o relatório: é o roteiro seção a seção, sem paráfrase.

## Quando disparar
- "faz um raio-x digital do `<cliente>`", "análise de performance digital completa"
- "o que melhorou/piorou no período", "por que esse resultado aconteceu"
- "compara com os concorrentes", "o que o concorrente está fazendo que a gente não"
- "monta o scorecard", "quais são os gargalos", "plano de ação priorizado"
- "cruza as redes com o site", "cruza engajamento com conversão", "pergunte aos números" (nível estratégico, não só comentário de IA)

## Como executar
1. **Contexto pelo vault primeiro, não por pergunta.** A seção 2 da metodologia pede ~25 perguntas de setup (segmento, objetivo, metas, contas, ferramentas). Antes de perguntar qualquer uma ao Gustavo, puxe o cliente no [[obsidianminer]] (nota `companies/<Cliente>.md` + memórias ligadas: `reference_contas_meta_ativas`, `reference_fontes_por_cliente`, o que já está cadastrado na fundação `app-relatorios`). Só pergunte o que realmente não está registrado.
2. **Rode a metodologia completa** (`metodologia.md`), alimentando cada seção só com a fonte real mapeada abaixo. Onde a fonte não existir, não estiver ligada pro cliente, ou não responder: escreva literalmente "Dado não disponível", nunca estime nem preencha com número de outro período/cliente.
3. **Comparação temporal é obrigatória** em toda métrica (atual x anterior, absoluto e percentual), mesmo que o Gustavo não peça explicitamente.
4. **Separe fato, interpretação e hipótese** em cada conclusão (regra 1.2 da metodologia). Três períodos comparáveis antes de chamar algo de tendência.
5. Cálculo (mediana, outlier score, funil, engajamento ponderado) sempre por código/query, nunca de cabeça.
6. Se o output for pra um cliente específico (deck ou portal), sai no visual dele ([[minerdesign]] + tema do cliente via `theme_primary`), não em markdown cru. Slide de comentário/anomalia/resumo passa pelo `ai-json`.

## Cobertura de fontes hoje (mapeado em 23/07/2026)

| Bloco da metodologia | Fonte real Miner | Status | Gotcha |
|---|---|---|---|
| Redes — Instagram orgânico (seguidores, alcance, top posts) | `instagram-ingestor` (MinerOS) → `report_top_posts`, via [[relatorio]] modo social | ⚠️ parcial — só Normatel ligado hoje | pra outro cliente: cadastrar IG business id em `report_accounts` + rodar o ingestor uma vez |
| Redes — TikTok / YouTube / LinkedIn / Pinterest orgânico | nenhuma | ❌ não existe | sem MCP nem ingestor; precisa API própria por rede ou agregador terceiro |
| Redes — concorrentes (engajamento público) | CSV manual "Social Tracker" **ou** Reportei "Interações totais" (só pras marcas que a Miner atende) | ⚠️ manual, não automatizado | nunca misturar as duas métricas no mesmo ranking; rotular a fonte no slide |
| Mídia — Meta Ads (spend, impr, cliques, CTR, CPC, CPM) | MCP `meta-ads` (39 tools, npm meta-ads-mcp) | ✅ live | token expira 22/08/2026 (renovação manual ~30s); listagem só mostra 25 contas, mas acesso direto por `account_id` funciona nas 206 |
| Mídia — Meta Ads (ROAS, CPA, conversões) | `get_insights` nativo NÃO traz (só delivery); Windsor cobre dentro da fundação | ⚠️ só se o cliente estiver cadastrado em `report_accounts` | sem fundação ligada = sem ROAS/CPA reais |
| Mídia — Google Ads | MCP `google-ads` instalado | ❌ sem dado real | developer token em nível "conta de teste" (não vê contas de produção); falta acesso Basic aprovado + OAuth client + refresh token |
| Site — GA4 (sessões, usuários, eventos, conversão) | Windsor via `windsor-ingestor`, só dentro da fundação `app-relatorios` | ⚠️ só quem já está cadastrado | não dá pra puxar GA4 ad-hoc de qualquer cliente nesta sessão |
| Site — Search Console (cliques, impressões, CTR, posição) | nenhuma API/MCP; acesso manual via login (ex.: PRLS em squad@minerbz, authuser=2) | ❌ manual | sem automação, número exige login do Gustavo/squad |
| Site — heatmap / gravação de sessão (Hotjar, Clarity) | Microsoft Clarity, projeto por cliente | ✅ PRLS, Le Salis, Normatel; ⏳ Normatel Premium (PR aberto) | rate limit 10 req/dia/projeto; detalhe completo em `setup-integracoes.md` |
| Site — portais/decks próprios da Miner (Vercel) | MCP Vercel `get_web_analytics` | ✅ só pro que a Miner hospeda | não serve pro site do cliente em geral |
| E-commerce — Shopify (produtos, pedidos, clientes, estoque) | MCP Shopify | ✅ conectado (loja PRLS confirmada) | outra loja Shopify de cliente precisa ser conectada à parte |
| E-commerce — Shopify Analytics (ShopifyQL) | MCP Shopify `run-analytics-query` | ✅ | "visualizações de produto" e funil carrinho→checkout completo normalmente vêm do GA4 Enhanced Ecommerce, não do Shopify puro |
| E-commerce — Bling / Olist / Tiny (contatos, pedidos) | ingestão custom com dedup + checkpoint ([[dados]]) | ⚠️ script, não MCP | rate limit Tiny ~30-40/min, Bling ~3/s; retomar do offset, nunca reiniciar |
| CRM/funil — MinerCRM | MCP Supabase (`execute_sql` no projeto minercrm) | ✅ | sempre filtrar por org (multi-tenant); nome de vendedor vem do CRM da org, nunca de lista solta |
| CRM/funil — Salesforce (ACCS) | CLI `sf` ([[salesforce]]) | ✅ | match por telefone/CNPJ, nunca por nome (org tem ~22k ops/mês) |
| Concorrência — Ad Library (quem anuncia, tempo no ar) | scraper via browser (claude-in-chrome), sem API oficial BR pra comercial | ⚠️ manual, sem gasto/impressão | só dá tempo no ar + nº de variações |
| Concorrência — tráfego/keywords estimados | Semrush (MCP presente) | ⚠️ consome crédito por chamada | usar com parcimônia; sempre rotular "estimado por ferramenta externa" |
| Concorrência — tráfego/autoridade (Similarweb, Ahrefs) | MCPs existem no catálogo, sem login | ❌ precisam OAuth | autorizar via `/mcp` numa sessão interativa antes de usar |
| Agregador multi-fonte (Supermetrics: GA4+GSC+Ads+redes num só lugar) | MCP existe no catálogo, sem login | ❌ precisa OAuth + licença Supermetrics ativa | maior alavancagem se autorizado: fecha várias linhas ❌ de uma vez |
| Interpretação por IA (comentário, alerta de anomalia, resumo executivo) | edge `ai-json` (MinerOS) | ✅ | só interpreta o dump que você manda, nunca inventa número fora dele |

## Lacunas: o que falta pra chegar em 100%

Decisão de 23/07/2026: Supermetrics ficou de fora (caro); em vez de agregador único, a Miner está construindo direto as integrações que faltam. Plano técnico completo (passo a passo, prazo de aprovação, gotchas de cada uma) em `setup-integracoes.md` — leia esse arquivo antes de mexer em qualquer console. Resumo por ordem de alavancagem:

1. **Google Search Console** — ✅ pronto (24/07/2026). Zero fila, reaproveita o projeto GCP do Google Ads.
2. **Google Ads Basic Access** — ⏳ pedido enviado 24/07/2026, aguardando aprovação do Google (~5 dias úteis).
3. **Microsoft Clarity** — ✅ pronto em PRLS, Le Salis e Normatel; ⏳ Normatel Premium instalado no código, PR aberto aguardando merge do Gustavo (github.com/gustavocoutiinho/crm-normatel/pull/1); ⏳ Costume Saudável/Festival Costume Gourmet instalado no código (`~/dev/sites/fcg-site`), aguardando o Gustavo rodar o deploy; ⚠️ ForYou já tem Clarity próprio noutra conta Microsoft, não duplicado; ❌ bloqueado em Clínica OTHN, Hidrotintas, Aço Cearense, Mercadinhos São Luiz e Mercadão São Luiz (GTM/wp-admin sem acesso da conta Miner); ❌ Ju Omakase sem GTM, precisa instalação manual; ⏸️ Porão sem URL confirmada — falta o Gustavo destravar/confirmar. Rate limit apertado (10 req/dia/projeto): serve pro raiox mensal, não pra dashboard ao vivo. Detalhe completo por cliente em `setup-integracoes.md`.
4. **TikTok Organic API** (Accounts API, não a Marketing/Ads) — próximo da fila, ainda não iniciado.
5. **Pinterest API v5** — ❌ descartado (Gustavo decidiu não ter interesse, 24/07/2026). Não retomar sem pedido explícito.
6. **YouTube Data/Analytics API** — ❌ descartado (Gustavo decidiu não ter interesse, 24/07/2026). Não retomar sem pedido explícito.
7. **LinkedIn Community Management API** — o mais caro: Standard Tier pode levar de 1 a 6 meses, app rejeitado não pode reaplicar, e por cliente exige que ele te torne Administrator (não Analyst) da própria Company Page. Avaliar se algum cliente relevante realmente usa LinkedIn antes de entrar nessa fila.
8. **Cadastrar clientes recorrentes na fundação `app-relatorios`** (skill [[relatorio]]) segue valendo em paralelo: quem estiver lá ganha GA4/GSC/Google Ads via Windsor sem depender dessas integrações novas.
9. **Replicar o `instagram-ingestor`** pros clientes além da Normatel: é cadastro (IG business id em `report_accounts`), não lacuna de ferramenta.

**Regra pra qualquer integração nova: sempre conectar em conta/projeto/GTM que já existe antes de criar um novo** (instrução do Gustavo, 24/07/2026).
10. **Similarweb ou Ahrefs** só se a análise de tráfego/autoridade de concorrente virar recorrente (hoje só Semrush cobre, cobrando crédito por chamada).

Nenhuma dessas integrações tem etapa que se resolve sem o Gustavo: todo fluxo tem pelo menos um clique de login/senha/2FA/consentimento que só ele pode fazer (mapeado em `setup-integracoes.md`, seção "onde precisa login humano" de cada uma).

## Gotchas
- Token Meta expira 22/08/2026; sem renovação, o MCP `meta-ads` para de trazer dado vivo (procedimento em `ads-mcp-servers-setup`).
- Windsor só cobre quem está em `report_accounts`: nunca assuma GA4/GSC disponível sem confirmar o cadastro.
- Reportei tem integrações GA4/Google Ads pra alguns clientes (ex.: STKR), mas o token é **somente leitura de catálogo de definições**, não devolve valor resolvido — não é fonte viável de número real.
- Ad Library não expõe gasto nem impressão de anúncio comercial no Brasil (só político); proxy de "performance" de concorrente é tempo no ar + nº de variações, nunca métrica paga.
- Semrush e outras ferramentas de crédito: não rodar consulta "pra ver o que vem" — cada chamada custa.

## O que NÃO fazer
- NÃO estimar GA4/Search Console/Google Ads quando a fonte não estiver ligada: escreva "Dado não disponível" e liste a integração que falta.
- NÃO misturar dado estimado (Semrush, Ad Library, Social Tracker) com dado real na mesma célula sem rotular a origem.
- NÃO comparar reels, carrosséis e imagens estáticas direto sem normalizar por formato e perfil (seção 4.3 da metodologia).
- NÃO chamar uma variação isolada de tendência: exigir pelo menos três períodos comparáveis.
- NÃO recomendar cortar segmento de mídia só por CPA/CPM médio alto (Breakdown Effect, regra também em [[midia]]).
