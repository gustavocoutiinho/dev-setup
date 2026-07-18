---
name: portal-kit
description: Use SEMPRE que for criar um portal, site ou app novo de cliente do zero na Miner (não editar um que já existe). Dispara com "cria um portal pro <cliente>", "novo portal", "monta o site do <cliente>", "começa o app do <cliente> do zero", "preciso de um portal novo". Também quando o trabalho começa sem repo, sem projeto Vercel e sem domínio ainda. Nasce no padrão (repo + Vercel + Supabase + favicon Miner + KV + domínio + gate), não improvisado.
---

# portal-kit: portal de cliente nascendo no padrão Miner

A Miner cria portal de cliente o tempo todo (34+ na Vercel). Sem um trilho, cada um nasce diferente: nome fora do padrão, sem repo, dado chumbado, exposto. Esta skill faz o portal nascer certo desde o primeiro commit.

## Quando disparar
- "cria/monta um portal (ou site, ou app) novo pro <cliente>", trabalho começa sem repo/projeto Vercel/domínio.
- Vai clonar um portal existente pra um cliente novo.
- NÃO use pra editar portal que já existe (aí é a skill do caso: [[dado-vivo]], [[web-enxuta]], [[blindar-portal]]).

## Como executar
1. **Contexto primeiro.** Puxe o cliente no [[obsidianminer]] (quem é, stack, lead Miner, o que já existe). Nunca invente.
2. **Nome no padrão.** Slug `tipo-cliente` (ex: `portal-normatel`, `deck-barneys`) idêntico em GitHub, Vercel e `~/dev`. Confirme que a URL antiga (se houver) continua viva. Cheque duplicados com [[faxina-vercel]].
3. **Repo primeiro (GitHub é a nuvem).** Cria o repo em `~/dev`, git init, primeiro commit. Nada de projeto sem repo.
4. **Stack da casa.** Next.js 14 (App Router) ou HTML single-file conforme o peso. Supabase MinerOS (`frocxapiowyjrdhlirnu`) ou projeto dedicado. Sem Lovable.
5. **Identidade.** Aplica o KV Miner via [[minerdesign]] (ou a marca do cliente quando for entregável dele) + favicon Miner.
6. **Dado vivo, não snapshot.** Se serve dado de cliente, já nasce lendo a fonte por edge ([[dado-vivo]]), não colado no front.
7. **Gate + domínio.** Se tem área logada ou PII, gate real ([[blindar-portal]], magic link Workspace SMTP). Aponta `<slug>.minerbz.com.br` ([[dominio-miner]]).
8. **Deploy e confirma no ar.** Deploy da última `main`; Vercel exige commit verificado. Editar = deployar: confirma a URL respondendo antes de dar por pronto.

## Gotchas
- Deploy só do `index.html` num portal com `/api` quebra todas as rotas (caso portal-accs). Deploya a pasta inteira.
- Se o portal serve PII sem sessão, não é "portal pronto", é vazamento: chama [[blindar-portal]] junto.
- 3 CRMs paralelos já viraram desperdício uma vez: antes de criar, confirme que não existe um canônico (via [[faxina-vercel]]).

## O que NÃO fazer
- NÃO subir projeto sem repo git (quebra "GitHub é a nuvem").
- NÃO usar Lovable nem provider fora do padrão Vercel + Supabase.
- NÃO chumbar dado real no front pra "funcionar hoje".
- NÃO deployar sem confirmar a URL no ar.
