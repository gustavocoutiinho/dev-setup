---
name: alerta-roas
description: Use SEMPRE que um número de mídia paga sair do padrão de um cliente (ROAS baixo, CPL alto, CTR no chão) e ninguém tiver sido avisado, ou ao gerar/atualizar relatório e ver métrica fora da faixa. Vigia o miner_reports_log (populado pelo robô semanal) e vira o dado em aviso ativo com semáforo por cliente, em vez de deixar o alerta morrer no banco (foi o que aconteceu com o NMTL ROAS 0.86). Dispara com "ROAS tá estranho", "algum cliente fora do padrão?", "avisa quando o ROAS/CPL furar", "coloca semáforo nos clientes", "qual conta tá sangrando", "monitora a mídia".
---

# alerta-roas: semáforo de ROAS/CPL que cobra quando fura o padrão

O robô semanal já popula o `miner_reports_log` com ROAS, CPL e entrega por cliente, mas ninguém abre o banco. Quando o NMTL deu **ROAS 0.86** (semana 21-27/05/2026) o alerta ficou só na linha do log e no card do Notion. Esta skill vira esse dado passivo em **aviso ativo**: compara cada cliente com o próprio padrão e dispara quando cruza o limiar. Ela avisa, não mexe na campanha.

## Quando disparar
- Rotina de checagem (após o robô semanal rodar seg 09:00 BRT) ou "monitora a mídia / algum cliente fora do padrão?".
- Ao gerar/atualizar relatório e uma métrica destoar da faixa do cliente.
- Gustavo pediu semáforo, alerta de ROAS/CPL, ou "avisa quando furar".

## Como executar
1. **Leia a fonte.** `miner_reports_log` no MinerOS (`frocxapiowyjrdhlirnu`), `source in (meta_ads, all_ads, google_ads)`, `metric in (roas, cpl, ctr, receita, investimento)`, competência corrente + anterior (o campo `delta_pct` já vem calculado).
2. **Compare com o padrão do cliente**, não com um número absoluto único. Metas de referência NMTL: ROAS 30d 1.5+, 60d 2.0+. Semáforo: verde (dentro), amarelo (queda relevante mês a mês), vermelho (abaixo da meta, ex 0.86).
3. **Cuidado com o breakdown effect.** Não dispare vermelho por um recorte (praça/criativo/dia) ruim: olhe o agregado ponderado antes. Raciocínio em [[meta-ads-analyzer]].
4. **Avise** só os que acenderam amarelo/vermelho: DM no Slack, WhatsApp pessoal (MCP) ou linha no daily-brief do vault (`~/ObsidianVaults/miner`), com cliente, métrica, valor, delta e a leitura em texto ([[relatorio-inteligente]]).
5. **Registre** o disparo no vault pra não repetir o mesmo alerta toda semana.

## Gotchas
- **Dado de teste velho:** parte do log é de maio (28/05). Não alarme sobre janela stale; confirme a competência antes.
- **ROAS pode não existir:** `get_insights` padrão do Meta só traz entrega; conversões WhatsApp/offline não vêm. Se o ROAS estiver zerado, é fonte faltando, não performance ruim.
- Semáforo é por cliente: o "normal" da Normatel não é o da Estela.

## O que NÃO fazer
- NÃO pausar/editar campanha sozinho: isto avisa, quem decide é o Gustavo/time.
- NÃO acender vermelho por um único breakdown ([[meta-ads-analyzer]]).
- NÃO disparar sobre dado de teste ou competência velha.
