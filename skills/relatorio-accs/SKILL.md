---
name: relatorio-accs
description: Use quando o Gustavo pedir relatório mensal ou trimestral da Aço Cearense (ACCS), atualizar o deck accs-proposta, cruzar leads do Meta Ads com o Salesforce da ACCS, calcular quanto os leads venderam ou faturaram, ou montar/deployar apresentação de resultados ACCS (Meta × Salesforce).
---

# Relatório ACCS · Meta Ads × Salesforce

## Visão geral

Produz o deck de resultados ACCS (mídia paga → leads → orçamentos → pedidos faturados) com **prova por linha**. Princípio inegociável: **nenhum número sem rastreabilidade** — lead casa com conta por e-mail, telefone ou CNPJ; **match por semelhança de nome é PROIBIDO** (puxa oportunidade errada: cada conta tem várias ops no mês; regra do Gustavo: "tenho que provar que veio desse cliente").

## Fontes (onde tudo vive)

| O quê | Onde |
|---|---|
| Deck + scripts | repo `~/dev/accs-proposta` (git; **pull antes, push depois**). `index.html` = mês, `trimestre.html` = trimestre, abas fixas ligam os dois |
| Mídia (investido/impressões/leads) | Meta Ads MCP, conta `act_1919182935615902`. Leads = action `lead`; conversas = `onsite_conversion.messaging_conversation_started_7d` |
| Leads brutos (nome/fone/email) | Export do Meta Lead Ads "FORMS B" em `~/Downloads/FORMS B - *.csv` — **UTF-16, delimitador TAB** (csv.reader padrão quebra com NUL). Períodos novos exigem export novo |
| Base/orçamentos/pedidos | `sf` CLI, org alias `aco-prospec` (acocearense.my.salesforce.com). Opportunity = orçamento; Order = pedido (OV) |
| Match pronto | `tools/match_accs.py --since AAAA-MM-DD --until AAAA-MM-DD --ops-until AAAA-MM-DD --out dump.json` |

## Processo

1. `git pull` no repo; conferir produção antes de mexer.
2. Meta: `get_insights` (account e campaign level, `time_range` do período).
3. Rodar `tools/match_accs.py`. **`--until` = última data do CSV; `--ops-until` = fim real do período** (senão corta orçamentos/pedidos dos últimos dias — em jun/26 isso escondeu R$ 201k de 30/06).
4. **Validar antes de publicar**: leads do CSV por campanha ≈ leads do Meta por campanha (jun/26 bateu 1:1); recorte de período anterior deve reproduzir o deck anterior.
5. Gerar números/tabelas do deck **por script a partir do dump** (nunca digitar número à mão; toda média citada tem que ser calculada).
6. Salvar `rastreio-<período>.json` **sem PII** no repo para auditoria.
7. Preview → verificar slides → commit → push → `vercel --prod`.

## Régua de negócio (definida pelo Gustavo)

- **Atribuível** = orçamento/pedido criado **no dia do lead ou depois**, na conta casada por e-mail/fone/CNPJ.
- **VENDIDO = pedido faturado**: status `TotalDelivery`, `NotDelivered`, `PartialDelivery`. **Tudo que faturou entra** (cliente recorrente incluso, com split transparente). `Declined` (recusado no crédito) e `InCreditAnalysis` ficam FORA.
- Fases de Opportunity: Em Rascunho → Enviado Para Aprovação → Fechado e ganho/perdido.
- **Paridade de abas**: o deck trimestral tem TODOS os slides do mensal, na mesma ordem, com dados do período (+ slide extra de evolução mensal). Slide novo no mensal replica no trimestral. Gerar por script (`build_tri_v2.py` no scratchpad da sessão de 03/07 é o molde); imagens de criativos por atribuição POSICIONAL aos cards (troca sequencial de src colide).

## Gotchas (falhas já cometidas — não repetir)

| Armadilha | Realidade |
|---|---|
| Telefone no SOQL | SF grava `(86)9411-3538`. `LIKE '%94113538'` retorna 0. Usar últimos 8 com hífen: `LIKE '%9411-3538'` |
| Objeto Lead do SF | Leads de formulário NÃO viram Lead (0 com origem FACEBOOK); `LeadSource`/`CampaignId` das ops = NULL. A ponte é só o match do CSV |
| PII | CSV tem fone/email de centenas de leads. **Nunca** comitar/deployar cru: o site serve a pasta toda. `tools/` e `rastreio*.json` ficam no `.vercelignore` |
| Agregados da org | Org tem ~22k ops/mês (ACCS inteira). Nunca somar sem filtrar pelas contas casadas |
| Deploy | Sessões paralelas mexem no mesmo repo/projeto Vercel (deploy storm; domínio já migrou de accs-proposta.vercel.app para domínios minerbz). Conferir `git log`, `vercel ls` e QUAL URL vale antes de afirmar "no ar" |
| CNPJ no Account | Campos `CNPJNUM__c` / `CPFCNPJNUM__c` (dígitos) |

## Referência rápida

```bash
sf data query --target-org aco-prospec -q "SELECT ..."   # SOQL ao vivo
python3 tools/match_accs.py --since 2026-07-01 --until 2026-07-31 \
  --ops-until 2026-07-31 --csv ~/Downloads/<export>.csv --out /tmp/match_jul.json
```

Memória relacionada: `accs-relatorio-jun26.md` (histórico e números fechados de jun e do 2º tri/26).
