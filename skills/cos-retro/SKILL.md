---
name: cos-retro
description: Use quando o Gustavo for fechar a retrospectiva do mês (último dia útil), com números do mês + executado vs planejado + aprendizados. Dispara com "fecha a retrospectiva do mês", "monta a retro mensal", "retrospectiva de <mês>", "o que rolou esse mês", "fecha o mês". Base pro planejamento do mês seguinte e pra revisão de OKRs trimestral.
---

# cos-retro: fechar a retrospectiva mensal

A retrospectiva mensal roda no último dia útil do mês. Consolida números do mês, executado vs planejado e aprendizados. É a base do plano do mês seguinte e da revisão trimestral de OKRs. Sem ela, o mês some sem leitura.

## Quando disparar
- "fecha a retrospectiva do mês", "retro mensal", "o que rolou esse mês".
- No último dia útil, antes de planejar o mês seguinte.

## Como executar
1. **Contexto.** `weeklys/YYYY-MM Retrospectiva Mensal.md` (o do mês; molde `templates/retrospectiva-mensal.md`), as weeklies do mês (`weeklys/2026-Wxx.md`) e o Decision Log.
2. **Números do mês.** Cerimônias, 1:1s, tasks Asana concluídas, métricas-âncora (ex: ROAS NMTL início→fim). Puxe via [[cruzar-dados]], não estime.
3. **Executado vs planejado.** Compare com o plano do mês anterior. Gaps explícitos, separados em operação e estratégico.
4. **Sinais e lições.** Positivos e negativos do mês + lições sobre delegação, tooling, time, clientes e risco.
5. **Fechar.** Pauta pra Cerimônia da 1ª semana do mês seguinte + plano macro por semana. Salve em `weeklys/`. Se algum KR mudou, registre pra revisão trimestral.

## Gotchas
- Roda no último dia útil, não no dia 1 do mês seguinte (senão a leitura do mês se perde).
- Métrica-âncora precisa de início E fim reais do mês. Normatel: usar números do Histórico, mês explícito, nunca extrapolar snapshot velho.
- Retro sem baseline vira diário: sempre compare com o planejado.

## O que NÃO fazer
- Não inventar número de entrega ("~X tasks") sem puxar do Asana.
- Não fechar sem comparar executado vs planejado.
- Não deixar decisão grande do mês fora do Decision Log.
