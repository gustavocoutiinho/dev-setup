---
name: pre-orcamento
description: Use quando o Gustavo for criar ou ajustar um bloco de pré-orçamento dentro de um portal de cliente pra substituir planilha Excel paralela por registro estruturado no Supabase. Dispara com "pré-orçamento", "elimina a planilha Excel", "orçamento estruturado no portal", "tira o Excel do fluxo", "calculadora do portal", "ACSC-OPS-001", ou quando o cliente ainda monta orçamento fora do sistema e você quer fonte única no banco.
---

# pre-orcamento, pré-orçamento no portal que mata o Excel

Bloco de pré-orçamento no portal do cliente que troca a planilha Excel paralela por registro estruturado no Supabase, fonte única. Referência: Pré-Orçamento ACCS (regra ACSC-OPS-001), no portal.minerbz.com.br em Calculadora > Pré-Orçamento, salvando no Supabase MinerOS (`frocxapiowyjrdhlirnu`).

## Quando disparar
- "pré-orçamento", "elimina a planilha Excel", "orçamento estruturado no portal", "tira o Excel do fluxo", "ACSC-OPS-001".
- Cliente monta orçamento fora do sistema (é uma das 11 categorias de problema do funil ACCS) e você quer fonte única.
- Nasce como bloco de um portal existente, no padrão [[portal-kit]].

## Como executar
1. **Contexto primeiro.** Puxe no [[obsidianminer]] (memória `acsc-preorcamento`). Confirme o que já está em produção antes de recriar.
2. **Banco no Supabase MinerOS.** Cabeçalho `acsc_preorcamentos` (cliente + vendedor + comercial + totais + status `rascunho|enviado_sf|aguardando_cliente|fechado|perdido`) + itens `acsc_preorcamento_itens` (FK cascade). View `v_acsc_preorcamentos_recentes` (90 dias). Numeração `PO-YYYY-NNNN` por sequência. RLS ligada, sem policy anon, só service_role.
3. **Edge function `acsc-preorcamento`** (guard `?key=`): GET list/get, POST cria header + itens em transação, PATCH status, DELETE. Totais calculados server-side, nunca confie no client.
4. **Bloco na UI:** cabeçalho (vendedor + CNPJ com máscara + razão + UF), itens com cross-fill kg↔un por peso de bitola (CA-50/CA-60, preço/kg padrão), totais auto, checklist P02/P03, aviso de pedido mínimo (4.000 kg no ACCS), ações (salvar, rascunho, PDF, copiar pro SF, WhatsApp), histórico de 90 dias.
5. **Publique a regra.** No Manual Operacional: 100% dos PO do mês registrados na tabela, planilha paralela proibida, auditoria semanal.

## Gotchas
- **Totais sempre server-side.** O client não fecha conta (evita divergência kg/un/R$).
- **Sem PII exposta.** Tabela é service_role, sem policy anon; a edge tem guard por key (migrar pro Vault depois).
- **É dado vivo, não snapshot:** o registro no Supabase é a fonte, não o PDF gerado ([[dado-vivo]]).
- **Deploy do portal-accs:** deploy só do `index.html` quebra os `/api`; deploya a pasta inteira e confirme no ar (editar = deployar).

## O que NÃO fazer
- NÃO deixar a planilha Excel paralela sobreviver: fere a ACSC-OPS-001.
- NÃO calcular total no front.
- NÃO comitar tabela/guard com dado real exposto.
