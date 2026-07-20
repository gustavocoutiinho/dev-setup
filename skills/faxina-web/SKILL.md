---
name: faxina-web
description: Use SEMPRE que precisar arrumar web que JÁ existe na Miner: inventariar/consolidar projetos Vercel e repos duplicados/mortos e achar o canônico, otimizar performance (bundle, cache, asset pesado, código morto, drift de config), ou migrar um projeto do Lovable pro padrão local + Vercel + Supabase. Também ao criar projeto novo (nasce no padrão) e quando um entregável de cliente está exposto em *.vercel.app. NÃO deleta nada sozinha: prepara o plano, o Gustavo confirma cada delete. Dispara com "faxina nos deploys", "consolida os projetos", "limpa a Vercel", "quantos duplicados eu tenho", "qual é o canônico", "isso tá exposto", "isso tá pesado", "carrega devagar", "enxuga o repo", "limpa código morto", "por que o bundle é tão grande", "otimiza", "migra do Lovable", "tira do Lovable".
---

# faxina-web: inventário, performance e saída do Lovable

Arrumar a web que JÁ existe na Miner. Hoje são ~56 projetos na Vercel (scope `gustavo-4410s-projects`) e ~46 repos no GitHub, com duplicado, morto, entregável exposto, bundle inchado e um resto ainda preso no Lovable. Esta skill faz o retrato, aponta o canônico, enxuga o peso e traz o que falta pro padrão da casa (Vercel + Supabase, nunca Lovable). Delete é irreversível: nunca apaga sozinha, deixa o plano pronto pro Gustavo confirmar item a item.

## Modos
- **inventário/consolidação:** mapeia Vercel + GitHub, cruza projeto↔repo, marca canônico/duplicado/órfão, prepara o plano de aposentar.
- **performance/enxugar:** code splitting, cache imutável com hash, externaliza asset pesado, mata código morto, resolve drift de config, sem mudar comportamento.
- **migração Lovable:** exporta o código, varre segredos, aponta Supabase, ajusta build Vercel, deploya e aposenta o Lovable.

## Quando disparar
- "faxina/consolida/limpa a Vercel", "qual é o canônico", "tem duplicado", "isso tá exposto".
- "isso tá pesado", "carrega devagar", "enxuga o repo", "por que o bundle é tão grande"; `Cache-Control: no-store` em asset estático, imagem base64 no código, 3 `project_id` Supabase no mesmo repo.
- "migra/tira do Lovable", "traz pro local/Vercel", "sai do Lovable".
- Ao CRIAR projeto novo: roda a checagem de nome/domínio antes, pra já nascer no padrão.

## Como executar
**Inventário:** `vercel projects ls --scope gustavo-4410s-projects` e `vercel domains ls --scope gustavo-4410s-projects`; suspeito → `vercel inspect <url> --scope ...` + `vercel ls <projeto> --scope ...` (últimos deploys). GitHub: `gh repo list --limit 100`, `gh repo view <repo> --json name,pushedAt,isArchived,url`. Cruze projeto↔repo e marque **canônico** (no ar + repo em `~/dev` no padrão + mais recente), **duplicado** (mesma coisa em outro nome/repo), **órfão** (deploy sem repo, ou repo sem deploy). Entregável de cliente em `*.vercel.app` sem gate/domínio é achado prioritário (fecha com domínio + auth; se serve dado sem sessão, chama [[blindar]] junto). Normalize slug `tipo-cliente` idêntico em GitHub/Vercel/`~/dev`, favicon Miner, domínio `*.minerbz.com.br`, URL antiga viva. Entregue a TABELA (projeto → estado → canônico/aposentar → ação) com o `vercel remove <projeto> --scope gustavo-4410s-projects` ESCRITO e comentado; você não executa delete.

**Performance (aditivo, zero regressão de função):** meça antes (`du -sh dist`, aba Network) pra provar o ganho. Code splitting + `lazy`/`import()` no que não é crítico ao primeiro paint (nunca no que aparece acima da dobra). Cache imutável só com hash no nome (`app.<hash>.js` → `Cache-Control: public, max-age=31536000, immutable`); `no-store` fica só pra HTML de entrada e dado volátil. Externalize base64/imagem/fonte gigante pra Supabase Storage referenciado por URL com hash. Mate o morto (grep confirma zero uso antes de apagar; snapshot que virou fonte viva é [[conserta-web]]). Resolva drift: uma única fonte de `project_id`/URL/chave por ambiente (env var, não valor chumbado); se achar 3 ids diferentes, confirme o certo no vault/Supabase real, não escolha no chute. Meça depois e deploy com ok ([[deploy]]).

**Lovable:** exporta o código e cria o repo em `~/dev` no nome padrão (GitHub é a nuvem). Varre as chaves que o Lovable deixou no front ([[blindar]]) e move pro server-side ANTES de qualquer deploy. Aponta o Supabase (dedicado ou MinerOS), confirma tabelas + RLS. Build pra Vercel: gotcha conhecido `.npmrc legacy-peer-deps` (foi preciso no miner-content). Deploy + domínio ([[deploy]]), confirma no ar, e só então aposenta o Lovable. Referência: miner-content saiu do Lovable 09/06 (hoje miner-content.vercel.app, Supabase `yndqwexlkrnaxxzqcdmr`); hub.minerbz.com.br ainda vive no Lovable + Cloudflare e é candidato.

## Gotchas
- Deploy só do `index.html` num single-file com `/api` quebra as rotas (gotcha ACCS): deploye o projeto inteiro.
- `isArchived: true` no GitHub não quer dizer morto no ar; dois projetos podem apontar pro mesmo domínio (confira qual resolve antes de aposentar). Aposentar não é deletar: tira tráfego/domínio, confirma que ninguém usa, depois o Gustavo deleta.
- `immutable` só é seguro com hash no nome; sem hash, cache longo serve versão velha e "some" com um fix já deployado. Cuidado com import dinâmico/string (rota montada por variável) que o grep simples não pega. Externalizar asset muda a origem: revise CSP/CORS pra não quebrar carregamento.
- Drift de config costuma esconder um repo apontando pro Supabase errado: confirme qual é produção antes de unificar.
- Lovable costuma deixar chave/segredo no bundle: nunca deploye sem varrer. Cloudflare na frente (caso hub) muda o apontamento: confirme o DNS real antes de virar.

## O que NÃO fazer
- NÃO rodar `vercel remove` nem apagar repo automaticamente: delete é do Gustavo, item a item.
- NÃO mudar comportamento/layout/dado a pretexto de "otimizar", nem pôr cache longo/immutable em asset sem hash.
- NÃO apagar código/dado sem provar (grep) zero uso, nem escolher `project_id`/chave "que parece certo": confirme a fonte real primeiro.
- NÃO manter o Lovable como fonte depois de migrar, nem deployar com segredo herdado exposto.
- NÃO renomear/mover domínio em uso sem manter a URL antiga viva.
