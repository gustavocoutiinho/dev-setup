---
name: traz-lovable
description: Use SEMPRE que for tirar um projeto do Lovable e trazer pro padrão da Miner (local + GitHub + Vercel + Supabase). Dispara com "migra do Lovable", "tira isso do Lovable", "traz o <projeto> pro local", "sai do Lovable", "importa o projeto do Lovable". A casa é Vercel + Supabase; o Lovable é ponto de partida a ser abandonado.
---

# traz-lovable: migração Lovable para o padrão Miner

A Miner às vezes começa no Lovable e depois traz pro padrão (Vercel + Supabase + repo GitHub). Já foi feito com o miner-content (importado 09/06, hoje miner-content.vercel.app + repo github miner-content, Supabase `yndqwexlkrnaxxzqcdmr`). O hub.minerbz.com.br ainda vive no Lovable + Cloudflare e é candidato. Esta skill padroniza a saída.

## Quando disparar
- "migra do Lovable", "tira do Lovable", "traz pro local/Vercel", "sai do Lovable".

## Como executar
1. **Exporta o código** do Lovable e cria o repo em `~/dev` no nome padrão (GitHub é a nuvem).
2. **Segredos.** Varre chaves que o Lovable deixou no front ([[varredura-segredos]]) e move pro server-side antes de qualquer deploy.
3. **Banco.** Aponta pro Supabase (dedicado ou MinerOS), confirma as tabelas e RLS.
4. **Build.** Ajusta o projeto pra Vercel. GOTCHA conhecido: `.npmrc` com `legacy-peer-deps` foi necessário no miner-content.
5. **Deploy e domínio** ([[deploy-miner]], [[dominio-miner]]), confirma no ar.
6. **Aposenta o Lovable** só depois que a versão nova estiver no ar e batendo.

## Gotchas
- `.npmrc legacy-peer-deps` resolve conflito de dependência herdado do export Lovable.
- Lovable costuma deixar chave/segredo no bundle: nunca deploye sem varrer ([[varredura-segredos]]).
- Cloudflare na frente (caso hub) muda o apontamento: confirme o DNS real antes de virar.

## O que NÃO fazer
- NÃO manter o projeto no Lovable como fonte depois de migrar.
- NÃO deployar com segredo exposto herdado do Lovable.
- NÃO virar produção sem confirmar a versão nova no ar.
