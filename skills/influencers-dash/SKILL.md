---
name: influencers-dash
description: Use quando o trabalho for o dashboard do squad de influencers do Mercadão São Luiz (MSLZ/SLZS), consolidar os dados de Instagram dos 11 influencers ao longo do ano num painel vivo. Vem do projeto Dashboard Influencers MSLZ e do portal patrocinios-mslz (mslz.minerbz.com.br). Dispara com "dashboard de influencers", "squad de influencers do São Luiz", "performance dos 11 influencers", "painel de patrocínios MSLZ", "atualiza o dashboard de influencer", "dados de Instagram dos influencers".
---

# influencers-dash: painel do squad de influencers do São Luiz

O Mercadão São Luiz opera um squad de 11 influencers e precisa ver a performance de Instagram deles ao longo do ano num painel, não numa planilha solta. Esta skill monta e mantém esse dashboard vivo. Canônico: nota "Dashboard Influencers MSLZ"; portais patrocinios-mslz / portal-mslz (mslz.minerbz.com.br); lead Caio Amorim + Cecília Maia.

## Quando disparar
- Precisa consolidar ou atualizar os dados de Instagram dos 11 influencers MSLZ num painel.
- Vai criar ou mexer no patrocinios-mslz / dashboard de influencers.
- NÃO use pra relatório mensal de mídia paga do cliente (é [[relatorio-vivo]]).

## Como executar
1. **Contexto primeiro.** Puxe MSLZ no [[obsidianminer]]: 11 influencers, dados de Instagram ao longo do ano, integração Facebook BM com Salesforce Marketing Cloud. Nunca invente número de influencer.
2. **Fonte viva, não planilha.** O dado do painel lê a fonte (Instagram/BM) por edge com cache versionado, no padrão [[dado-vivo]]. Nada de snapshot colado que envelhece.
3. **Métricas do squad.** Por influencer e agregado: seguidores, alcance, engajamento, evolução no ano. Comparável entre os 11 pra ranquear.
4. **Monte no padrão de cockpit.** Reuse a fundação de painel ([[cockpit-kit]]): Vercel + Supabase MinerOS (`frocxapiowyjrdhlirnu`), favicon Miner, KV. Sem Lovable.
5. **Deploy e confirme no ar.** Deploy da última main; editar = deployar, confirma a URL respondendo antes de dar por pronto.

## Gotchas
- Dado de Instagram por API exige token e permissão da BM: se cair, sirva o último cache com data real e registre no [[radar-bloqueios]] (nada de "atualizado hoje" mentiroso).
- São 3 BMs no MSLZ (Mercadinho Read-Only, Mercadão, principal): confirme de qual conta vem o dado do squad.
- "Ao longo do ano" pede série histórica, guarde os pontos no Supabase, não só o snapshot atual.

## O que NÃO fazer
- NÃO chumbar os números dos influencers no front, vira snapshot morto.
- NÃO subir fora do padrão Vercel + Supabase (sem Lovable).
- NÃO deployar sem confirmar a URL no ar.
- NÃO inventar métrica que a fonte não devolveu.
