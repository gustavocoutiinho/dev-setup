---
name: umbrella-kit
description: Use SEMPRE que for criar um portal guarda-chuva multi-marca na Miner (uma casca que hospeda várias marcas ou unidades sob o mesmo teto). Dispara com "portal multi-marca", "guarda-chuva de marcas", "um portal pra todas as marcas do grupo", "portal umbrella", "junta as marcas num portal só". Cada marca isolada, mas sob a mesma estrutura.
---

# umbrella-kit: portal guarda-chuva multi-marca

Quando um grupo tem várias marcas ou unidades, a Miner monta um portal guarda-chuva (umbrella) que hospeda todas sob a mesma casca, com isolamento por marca. É o padrão do Portal Guarda-Chuva (separado do portal-accs) e do ACCS GP. Esta skill instancia esse tipo.

## Quando disparar
- "portal multi-marca", "guarda-chuva", "um portal pra o grupo com N marcas".
- Grupo com marcas/unidades que precisam de páginas próprias mas gestão unificada.

## Como executar
1. **Mapeie as marcas** e o que cada uma expõe (no [[obsidianminer]]).
2. **Casca umbrella** ([[portal-kit]] como base), roteamento por marca (`/marca` ou subdomínio), isolamento de dado por marca.
3. **Dado vivo por marca** ([[dado-vivo]]), nunca misturar base de uma marca com outra.
4. **Gate e permissão** por marca ([[blindar-portal]]): quem vê o quê. Multi-tenant de verdade.
5. **Identidade** compartilhada (KV Miner) com espaço pra marca de cada uma ([[minerdesign]]).
6. **Domínio** ([[dominio-miner]]), deploy e confirma ([[deploy-miner]]).

## Gotchas
- O risco número 1 é vazamento cruzado entre marcas: teste que a marca A nunca enxerga dado da marca B.
- Umbrella sem isolamento vira um monólito difícil de manter; separe as fontes desde o início.

## O que NÃO fazer
- NÃO servir todas as marcas do mesmo blob sem isolamento.
- NÃO expor dado de marca sem sessão.
- NÃO duplicar um umbrella que já exista (cheque [[faxina-vercel]]).
