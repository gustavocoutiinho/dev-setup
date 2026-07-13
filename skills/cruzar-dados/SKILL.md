---
name: cruzar-dados
description: Cruza e consolida no Obsidian (vault miner) os dados das ferramentas conectadas (Asana, Meta Ads, WhatsApp e o que mais tiver MCP), num retrato por cliente. Use quando o Gustavo disser "cruza os dados", "atualiza o obsidian com as ferramentas", "consolida o retrato dos clientes", "puxa o que mudou", ou quando rodar agendado 1x/dia de manhã. Sempre escreve no vault ~/ObsidianVaults/miner; nunca inventa dado de ferramenta que não respondeu.
---

# Cruzar dados das ferramentas → Obsidian

Objetivo: manter o vault (o cérebro do Gustavo) refletindo o estado atual das ferramentas, com um **retrato por cliente** sempre atualizado. Roda agendado 1x/dia de manhã (launchd) ou sob demanda.

## Processo

1. **Carteira**: leia os clientes ativos em `clientes-ativos-jul2026.md` (fonte oficial). Só cruze quem está ativo.
2. **Puxe das ferramentas conectadas** (use só as que responderem; PULE as que pedirem login e registre como "sem auth"):
   - **Asana** (`mcp productivity:asana`): tarefas/projetos abertos por cliente, responsável, prazo, status.
   - **Meta Ads** (`mcp meta-ads`): gasto, leads, CPA, ROAS, últimos 7 dias. **Use a conta que VEICULA**, não a "Read-Only" (essas retornam 0). Consulte `reference_contas_meta_ativas` pro mapa cliente→conta. Se só houver Read-Only/0, escreva "mídia: conta não compartilhada com o token", nunca reporte R$ 0 como pausa real. `date_preset` "last_week" não existe no Meta: use `time_range` {since, until}.
   - **WhatsApp** (`mcp whatsapp`): últimas interações dos grupos "Ⓜ️ [cliente] + Miner" (decisões, pendências). É LOCAL, só roda no Mac mini.
   - Qualquer outra ferramenta com MCP conectado (Notion, Gmail, Calendar, Supabase…).
3. **Cruze por cliente**: para cada cliente ativo, atualize a nota dele no vault com um bloco datado:
   ```
   ## Retrato — AAAA-MM-DD
   - Tarefas abertas (Asana): …
   - Mídia 7d (Meta Ads): gasto R$…, leads …, CPA R$…
   - Últimas conversas (WhatsApp): …
   - Pendências / decisões: …
   ```
   Não apague o histórico: acrescente um bloco novo por dia.
4. **Log**: em `cruzamentos/log.md`, registre data, o que foi cruzado com sucesso e o que falhou (MCP sem auth), pra ficar rastreável.
5. **Regra de ouro**: se uma ferramenta não respondeu, escreva "sem dados (não conectada hoje)" e siga. NUNCA invente número.

## Gatilho automático
Agendado via `launchd` no Mac mini, 1x/dia de manhã (o plist e o wrapper ficam em `~/dev/dev-setup/automacao/`). Depende dos MCPs estarem autenticados no Mac mini na hora da execução; os que usam OAuth interativo (Asana, Notion) podem cair e serão marcados como "sem auth" no log até renovar o login.
