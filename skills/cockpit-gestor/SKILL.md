---
name: cockpit-gestor
description: Use quando o Gustavo for montar ou ajustar a "visão gestor" de um portal de cliente (dashboard de gestão com meta x realizado, placar de vendedores, funil do mês e risco de crédito), não a lista de leads. Dispara com "visão gestor", "cockpit do gestor", "dashboard de gestão no portal", "placar dos vendedores", "risco de crédito no portal", "monta a visão gestor do <portal>", ou quando o gestor precisa enxergar conversão e onde trava, não o grid de leads.
---

# cockpit-gestor, visão gestor de portal de cliente

Monta a persona "Visão gestor" de um portal: um dashboard de gestão completo (não grid de leads), com KPIs de conversão + risco de crédito, placar de vendedores e funil do mês, tudo ao vivo. Referência canônica: Cockpit do Gestor do ACCS (Caça Negócio, portal.minerbz.com.br), em `~/dev/portal-accs/index.html` como `window.GESTOR_COCKPIT`, container `#cn-view-gestor`, ativado por `cn_applyPersonaView('gestor')`.

## Quando disparar
- "visão gestor", "cockpit do gestor", "dashboard de gestão", "placar dos vendedores", "risco de crédito no portal".
- Gestor precisa enxergar meta x realizado e onde trava, não a lista de leads.
- Fonte sempre viva por edge ([[dado-vivo]]), nunca número chumbado.

## Como executar
1. **Contexto primeiro.** Puxe o portal no [[obsidianminer]] (memória `cockpit-gestor-accs`). Confirme as fontes ao vivo: no ACCS é `/api/prospec/funil-sf` (PROSPEC_LIVE) + `/api/caca-negocio/pipeline`.
2. **Escopo + metas.** Defina os vendedores do escopo (ACCS = 3: Gabrielle, Letícia, Welson) e as metas (`window.PROSPEC_METAS`, 300t total).
3. **5 KPIs:** faturado vs meta proporcional, orçado, em negociação, faturados, risco de crédito.
4. **Blocos:** placar dos vendedores (ranking + ritmo + falta), tendência com YoY, funil do mês (Orçado → Pedido → Faturado), saúde por idade do negócio, top oportunidades clicáveis, ações do gestor.

## Gotchas (o Gustavo é sensível a "não bate")
- **Conversão por QUANTIDADE de negócios (qtd fechados / qtd oportunidades ~17%), NUNCA por tonelada** (positivado_t/orçado_t dá ~2% falso, distorcido por cotações gigantes especulativas).
- **Risco/crédito vem do funil-sf** (`cur.credito`/`cur.recusado`), NÃO dos deals abertos (o feed filtra `ApprovalStatus != Rejeitado` e mostra 0 falso). São TONELADAS: rotule "t".
- **Motivo de perda é `ClosingReason__c`**, não `Loss_Reason__c` (vazio em 100%). Maior motivo real: "Atualização do Preço".
- **Não use "pipeline por estágio":** no SF deles quase tudo fica em "Em Rascunho" (painel degenerado).
- **ICP não tem campo limpo:** classifique no front por regex na razão social.

## O que NÃO fazer
- NÃO reportar conversão em tonelada.
- NÃO chumbar KPI: cai fora do [[cockpit-kit]] e do [[dado-vivo]].
- NÃO inventar meta: vem do `PROSPEC_METAS`.
