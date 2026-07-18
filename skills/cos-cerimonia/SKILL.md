---
name: cos-cerimonia
description: Use SEMPRE que o Gustavo for montar a pauta da Cerimônia Miner (segunda 9h BRT, 60 min, os 8 diretos + ele, ritmo de empresa). Dispara com "monta a pauta da cerimônia", "prepara a cerimônia de segunda", "o que levar pra cerimônia", "pauta da segunda 9h", "cerimônia semanal". É ritmo de empresa, não update operacional cliente por cliente.
---

# cos-cerimonia: pauta da Cerimônia de segunda 9h

A Cerimônia Miner é segunda 9h BRT, 60 min, 9 pessoas core (8 diretos + Gustavo). É ritmo de empresa: todos cientes das prioridades e riscos da semana, 1-2 decisões transversais por escrito, sinais de saturação capturados. Esta skill monta a pauta enxuta a partir dos sinais críticos.

## Quando disparar
- "monta a pauta da cerimônia", "pauta da segunda 9h", antes da segunda de manhã.
- Sempre que houver sinal crítico ou decisão transversal para levar ao time todo.

## Como executar
1. **Contexto.** `docs/sop/SOP Cerimonia Miner.md` (estrutura canônica) + `templates/cerimonia-miner.md`. Última ata e decisões em aberto.
2. **Sinais críticos primeiro.** Puxe saturação por direto ([[cos-capacity]]) e riscos de cliente antes de virar incidente ([[cruzar-dados]]). Sinal antes de incidente.
3. **Pauta enxuta (3-4 itens):** abertura (1-2 highlights + 1 alerta), ronda rápida por direto (prioridade da semana / risco identificado / pedido ao grupo), decisão transversal (o que se repete na ronda ou afeta 2+ diretos), próximos 7 dias.
4. **Ordem da ronda:** Caio, Rafael, Davi, ygor, Cecilia, Ricardo, Raquel, Helia.
5. **Delegação.** Item de owner escala pro owner primeiro, não vira pedido ao Gustavo.
6. **Pós:** ata em 24h, decisões grandes ao Decision Log, sinais novos ao [[cos-capacity]].

## Gotchas
- Anti-padrão: update cliente por cliente vira reunião de 3h. Sinal + decisão, não status.
- Decisão grande sem documento prévio perde rigor: leve o rascunho pronto.
- Helia muda toda cerimônia é sinal: validar participação enquanto sem status formal ([[direto-novo]]).

## O que NÃO fazer
- Não transformar em ronda de status sem decisão saindo dela.
- Não deixar risco identificado sem dono e sem ação.
- Não fechar sem ata: decisão por escrito ou não aconteceu.
