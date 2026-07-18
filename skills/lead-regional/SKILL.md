---
name: lead-regional
description: Use SEMPRE que for pontuar ou rotear lead por região/porte (Hidrotintas e afins), ou o Gustavo disser "score de lead", "esse lead é da minha região?", "filtra lead por CNPJ e porte", "qual lead vale a pena", "por que lead da Bahia entrou como quente", "roteia os leads por região". Dispara no fluxo de Lead Ads da Hidrotintas (HDTS) e em qualquer cliente que precise qualificar lead por geografia + perfil de empresa antes de mandar pro vendedor.
---

# lead-regional: score regional de leads

Lead de mídia entra sem qualificação: vendedor perde tempo com quem está fora da região ou fora do perfil. Esta skill pontua o lead por região e porte antes de rotear, no padrão do fluxo Hidrotintas (HDTS).

## Quando disparar
- Lead novo de Lead Ads que precisa ser qualificado por geografia + perfil antes de virar card no funil.
- "por que lead do PA entrou como quente", "score da região tá errado", "roteia por região".
- Cliente novo precisa replicar o motor de scoring regional da HDTS.

## Como executar
1. **Ingestão do lead** pela esteira do cliente ([[ingere-base]] / o `hdts-leads-sync` no MinerCRM `stpstwsqtuubpxvvexte`), idempotente por `external_id`.
2. **Enriquecimento por CNPJ.** Enriqueça a empresa (Apollo) pra ter porte, setor e localização confiáveis; não confie só no que o lead digitou no form.
3. **Score regional.** Chame a edge `hdts-lead-scorer` (Supabase MinerOS `frocxapiowyjrdhlirnu`, `verify_jwt=false`, webhook público protegido por header `x-miner-webhook-secret`). Ela grava em `hdts_lead_scores`. Regra de região da HDTS: **BA/PA/SE/MA/PE/AM = frio** (fora do raio de entrega); região-alvo = quente/morno.
4. **Roteamento.** O score vira temperatura no funil e alimenta a distribuição pro vendedor (round-robin entre `profiles` role `vendedor`); gerente (admin) não recebe lead. O volume por região/temperatura entra no relatório semanal do cliente via [[robo-relatorio]].
5. **Registre bloqueio, não invente.** Se falta o secret do webhook ou a chave Apollo, PARE e registre no [[radar-bloqueios]].

## Gotchas
- `verify_jwt=false` só é seguro porque valida `x-miner-webhook-secret`; sem o header, a função tem que recusar (não deixar webhook público sem guarda).
- Round-robin fica dormente enquanto nenhum vendedor aceitou convite (0 perfis); o backfill atribui quando o primeiro entra.
- Conta de mídia via agência (Hidrotintas/Mulato) não dá API direta do Meta; a fonte de lead é a planilha exportada em CSV.

## O que NÃO fazer
- NÃO mandar lead pro vendedor sem passar pelo score.
- NÃO tratar região fria como quente pra inflar volume.
- NÃO deixar a edge de scoring como webhook aberto sem o secret.
