---
name: lp-kit
description: Use SEMPRE que for criar landing page de vertical ou nicho da Miner, principalmente várias de uma vez. Dispara com "gera uma LP pra <vertical>", "landing de <nicho>", "cria as LPs das verticais", "LP em lote", "nova landing de captação". Também quando um cliente tem N segmentos e cada um precisa da sua página de captura.
---

# lp-kit: landing de vertical no padrão, em lote

A Miner produz landing de vertical em série (as 8 do MIG: medicina, higienista, fisio, farmácia, prótese, mls, webinares, credit-journey, mais dr-dream BR/LATAM e speak-english, geradas num batch de 25/abr). Todas partem da mesma casca, muda o nicho e a copy. Esta skill mantém isso padronizado e garante que a LP capture lead de verdade.

## Quando disparar
- "cria a LP de <vertical/nicho>", "gera as landings das verticais", trabalho de captação com N segmentos.
- Clonar uma LP existente pra um nicho novo.

## Como executar
1. **Puxe o contexto** do cliente/vertical no [[obsidianminer]] (oferta, público, ângulo).
2. **Casca única.** Parte da estrutura já validada, troca hero, copy, prova e oferta por nicho. LP estática na Vercel, nome no padrão `<cliente>-<nicho>-lp`.
3. **Captura real.** O form TEM que gravar o lead num destino (Supabase/CRM), nunca só toast. Use [[capta-lead]] e o consentimento LGPD nunca nasce marcado.
4. **Identidade.** KV Miner ou marca do cliente via [[minerdesign]] + favicon Miner.
5. **Domínio e pixel.** Aponta subdomínio ([[dominio-miner]]), instala pixel/GA4 pra medir conversão por vertical.
6. **Deploy e confirma no ar** ([[deploy-miner]]).

## Gotchas
- LP de lote costuma ir sem commit rico (deploy direto): garanta que cada uma fica no repo mesmo assim.
- Sem pixel/GA4 por vertical você não sabe qual nicho converte. Instale antes de rodar mídia.
- Form bonito que não faz POST engole o lead: sempre confira o fetch ([[capta-lead]]).

## O que NÃO fazer
- NÃO subir LP sem captura real do lead.
- NÃO usar Lovable nem chumbar dado.
- NÃO deixar o consentimento pré-marcado (LGPD).
