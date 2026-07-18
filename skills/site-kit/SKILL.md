---
name: site-kit
description: Use SEMPRE que for criar um site institucional novo da Miner ou de cliente (site de apresentação, não app com login nem dashboard). Dispara com "cria o site institucional do <cliente>", "site novo da Miner", "landing institucional", "site de apresentação", "redesign do site". Estático, rápido, React/Vite ou HTML, focado em apresentar e converter contato.
---

# site-kit: site institucional estático no padrão Miner

Site institucional é uma casa mais simples que portal: apresenta a marca e capta contato, sem área logada. A Miner já tem esse padrão no site-miner (`~/dev/sites/site-miner`) e no fcg-site (`~/dev/sites/fcg-site`, LIVE em costumegourmet.minerbz.com.br). Esta skill instancia um novo do jeito certo.

## Quando disparar
- "cria/refaz o site institucional do <cliente>", "site de apresentação", "landing institucional".
- NÃO use pra app com login/dashboard (aí é [[portal-kit]] ou [[cockpit-kit]]).

## Como executar
1. **Contexto e conteúdo** no [[obsidianminer]] (posicionamento, seções, CTA).
2. **Stack estática:** React/Vite SPA ou HTML, em `~/dev/sites/<slug>`, nome no padrão.
3. **Identidade** KV Miner ou marca do cliente ([[minerdesign]]) + favicon Miner.
4. **Contato que grava** o lead ([[capta-lead]]), não só um `wa.me` cego.
5. **SEO básico** (title, og:image, sitemap) e performance ([[web-enxuta]]).
6. **Domínio** ([[dominio-miner]]), deploy e confirma no ar ([[deploy-miner]]).

## Gotchas
- Institucional pesa fácil com imagem grande em base64: externalize e use cache imutável ([[web-enxuta]]).
- og:image ausente deixa o link feio quando compartilhado: sempre configure.

## O que NÃO fazer
- NÃO usar Lovable nem provider fora de Vercel.
- NÃO deixar CTA que abre WhatsApp sem registrar quem clicou.
- NÃO subir sem repo git.
