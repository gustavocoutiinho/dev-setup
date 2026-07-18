---
name: nfe-automatiza
description: Use SEMPRE que o assunto for emissão recorrente de NF ou boleto de mídia dos clientes da Miner. Dispara com "emite a NF dos anúncios", "gera o boleto de mídia", "faturamento de mídia do mês", "NF do <cliente>", "cobra os anúncios". Financeiro é sensível: a skill prepara, mas a emissão e o envio são por item, com confirmação.
---

# nfe-automatiza: faturamento recorrente de mídia

Todo mês reaparecem as tarefas "Emitir NF's dos anúncios", "Gerar boleto dos anúncios" (JCNA), "Enviar boleto / ADS" (GRBS). É repetitivo mas financeiro, então a skill organiza e prepara, sem nunca disparar cobrança sozinha. Casa com o Sistema Financeiro Miner (`~/dev/apps/app-financeiro`, Next + Supabase).

## Quando disparar
- "emite NF/boleto de mídia", "faturamento de mídia do mês", "cobra os anúncios do <cliente>".
- Virada de mês, quando o ciclo de faturamento de mídia abre.

## Como executar
1. **Levanta o que fatura:** por cliente, o gasto de mídia do período (Windsor/Meta) e o combinado.
2. **Monta a lista** de NF/boletos a emitir, com valor, cliente e vencimento, pra revisão.
3. **Confirma item a item com o Gustavo** antes de emitir qualquer coisa. Financeiro não é ação automática.
4. **Emite/gera** só o que foi aprovado, registrando no Sistema Financeiro.
5. **Envio ao cliente** é passo separado e só com ordem explícita por item (regra: nunca enviar por ele sem comando).
6. **Registra** o que saiu, pra o [[monitor-custo]] cruzar receita de mídia vs gasto.

## Gotchas
- Boleto vencido já apareceu (dLocal LXNT): confira vencimentos e inadimplência antes de reemitir.
- Ex-cliente não fatura: cruze com a carteira ativa antes de gerar cobrança.

## O que NÃO fazer
- NÃO emitir NF/boleto em lote sem confirmação por item.
- NÃO enviar cobrança ao cliente sem ordem explícita.
- NÃO faturar cliente que já saiu.
