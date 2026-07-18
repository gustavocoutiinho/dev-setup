---
name: relatorio-vivo
description: Use quando o Gustavo pedir pra "montar/atualizar relatório de <cliente>", "ligar o cliente na fundação de relatórios", "puxar dados vivos de <cliente>", "conectar Meta/Google/GA4/Shopify/Blip do cliente", "por que o relatório tá desatualizado", "colocar o <cliente> no app-relatorios", ou unificar os relatórios num sistema só. Liga um cliente/fonte novo na fundação viva (app-relatorios, endpoint report-data) em vez de deck manual; unifica os 3 sistemas de relatório e os 3 modelos de auth num só, com cron real e log de freshness. Dispara em qualquer trabalho de relatório recorrente de cliente.
---

# relatorio-vivo · fundação única de relatórios de cliente

## Contexto
Hoje existem 3 jeitos soltos de fazer relatório (deck HTML manual, portais por cliente,
scripts avulsos) e 3 jeitos de autenticar fonte. A fundação viva é
`~/dev/apps/app-relatorios` (frontend estático que consome o endpoint **`report-data`**,
edge function no Supabase Miner). Estado atual: **só Meta ligado, 2 de 21 clientes**. Esta
skill é o caminho pra ligar mais clientes/fontes por cima da MESMA fundação, sem criar mais
um sistema paralelo.

## Quando disparar
- "montar/atualizar relatório do <cliente>", "liga o <cliente> na fundação".
- Conectar fonte nova (Meta, Google Ads, GA4, Shopify, Blip) a um cliente existente.
- Reclamação de relatório velho/parado (vira diagnóstico de freshness).

## Como executar
1. **Ler o vault antes** (obsidianminer): qual conta/fonte o cliente tem, qual token, o que já
   está ligado. Fontes por cliente mapeadas em `reference_fontes_por_cliente` e
   `reference_contas_meta_ativas`. Nunca inventar conta/ID.
2. **Cadastrar o cliente na fundação**, não em repo novo. O cliente vira uma entrada de
   config (slug + fontes + IDs) consumida pelo `report-data`. Slug segue a convenção
   `tipo-cliente` (mesma do GitHub/Vercel/~/dev).
3. **Ligar a fonte pelo conector certo (auth unificada):**
   - **Meta Ads:** já é o caminho quente. Conta `act_...`, token Miner Ads (memória
     `ads-mcp-servers-setup`; token 60d + `refresh.sh`). Insights via a mesma rota do MCP.
   - **Google Ads / GA4:** pendentes de credencial (Google Ads não conectado ainda). Marcar
     como fonte declarada mas inativa até a credencial existir; não simular dado.
   - **Shopify:** por loja, ex. PRLS `prls.com.br` via API (`prls-ads-shopify-access`).
   - **Blip / Omnichat / chat:** via `miner_api_credentials` multi-tenant (`miner-custom-mcps`).
   Toda credencial nova entra por variável de ambiente / tabela de credenciais, nunca chumbada
   no front (o `app-relatorios` é estático e público).
4. **Cron real + log de freshness.** Cada fonte grava `ultima_atualizacao` por cliente.
   Agendar refresh (edge cron, padrão dos crons Miner) e expor no relatório "dados de
   DD/MM HH:MM". Sem cron, o relatório é um print, não é vivo.
5. **Validar:** bater os números do `report-data` contra a fonte oficial (Meta Ads Manager,
   painel Shopify) num período conhecido antes de dizer "no ar".
6. **Deploy:** `vercel --prod` no `app-relatorios` (frontend); edge functions pelo fluxo
   Supabase Miner. Deploy sempre da última main (`git pull` antes).

## Gotchas
- **Bloqueio conhecido:** relatórios vivos multi-tenant dependem de `WINDSOR_API_KEY` (memória
  `project_relatorios_vivos`). Fonte que dependa dela fica pendente até a chave existir.
- **Só Meta ligado.** Não prometer Google/GA4/Shopify "vivo" antes da credencial. Fonte sem
  credencial = declarada e inativa, com aviso no log de freshness.
- **Público e estático:** `app-relatorios` serve a pasta toda. Zero segredo/PII no front;
  tudo sensível fica no edge/Supabase.
- **Omnichat congelada** em alguns clientes (ex. Normatel devolve só jun/2022): renovar
  credencial antes de tratar como fonte viva.

## NÃO fazer
- Não criar mais um repo/sistema de relatório: ligar na fundação `app-relatorios`.
- Não chumbar token/credencial no front nem no JSON público.
- Não reportar número de fonte que não respondeu; marcar a fonte como sem dado.
- Não pular o log de freshness: relatório sem carimbo de atualização não é "vivo".
