---
name: web-enxuta
description: Otimiza web app da Miner (portal, deck, site, app) sem mudar o que ele faz: code splitting e lazy-load, cache imutável com hash de asset, externalizar assets pesados (base64/imagem gigante) pra storage, matar código morto e dado órfão, e resolver drift de config (ex: 3 project ids Supabase diferentes no mesmo repo). Use SEMPRE que ver bundle grande, HTML single-file pesado, `Cache-Control: no-store` em asset estático, imagem em base64 dentro do código, dado sem uso, ou chaves/URLs de ambiente divergentes. Dispara com "isso tá pesado", "carrega devagar", "enxuga esse repo", "limpa código morto", "por que o bundle é tão grande", "otimiza".
---

# web-enxuta — performance e código limpo sem mudar comportamento

Regra de ouro: **aditivo e sem regressão de função.** A página faz exatamente o mesmo depois, só mais leve e mais organizada. Trabalhe por diffs pequenos e verificáveis, uma otimização por vez.

## Quando disparar
- Bundle grande, build lento, HTML single-file de vários MB (deck pesado, portal monolítico).
- `Cache-Control: no-store` (ou ausência de cache) em asset estático que quase nunca muda.
- Imagem/fonte em base64 embutida no JS/HTML inchando o bundle.
- Código morto (componente/rota não referenciada), dado órfão (snapshot que ninguém importa mais).
- Drift de config: mais de um `project_id`/URL Supabase, chave repetida divergente, `.env` conflitando com valor chumbado.

## Como executar
1. **Meça antes.** Veja o tamanho real (`du -sh dist`, análise de bundle, aba Network). Anote o baseline pra provar o ganho.
2. **Code splitting + lazy.** Separe rotas/telas pesadas em chunks; `lazy`/`import()` no que não é crítico pro primeiro paint. Não faça lazy do que aparece acima da dobra.
3. **Cache imutável com hash.** Asset estático com nome hashado (`app.<hash>.js`) servido `Cache-Control: public, max-age=31536000, immutable`. `no-store` fica só pra HTML de entrada e dado volátil, nunca pra asset versionado.
4. **Externalize o pesado.** Imagem/base64/font gigante sai do código e vai pro Supabase Storage (ou pasta estática servida pela Vercel), referenciada por URL com hash. O padrão da casa é Vercel + Supabase.
5. **Mate o morto.** Remova componente/rota/asset sem referência e dado órfão (grep pra confirmar zero uso antes de apagar). Snapshot que virou fonte viva (ver `dado-vivo`) sai daqui.
6. **Resolva o drift de config.** Uma única fonte de `project_id`/URL/chave por ambiente (env var, não valor chumbado repetido). Se achar 3 ids diferentes, descubra o certo (confirme no vault / Supabase real) e unifique; não escolha no chute.
7. **Meça depois e deploy com ok.** Compare com o baseline, confirme que a função é idêntica, deploy só com o Gustavo confirmando. Editar = deployar: só conta no ar.

## Gotchas
- `immutable` só é seguro com hash no nome. Sem hash, cache longo serve versão velha e você "some" com um fix já deployado.
- Antes de apagar "código morto", cheque import dinâmico/string (rota montada por variável) que o grep simples não pega.
- Externalizar asset pode mudar o domínio de origem: revise CSP/CORS pra não quebrar carregamento.
- Drift de config costuma esconder um repo apontando pro projeto Supabase errado. Confirme qual é produção antes de unificar.

## O que NÃO fazer
- NÃO mudar comportamento, layout ou dado a pretexto de "otimizar". Isso é refactor de função, não é esta skill.
- NÃO pôr cache longo/immutable em asset sem hash no nome.
- NÃO apagar dado/arquivo sem provar (grep) que ninguém usa.
- NÃO escolher um `project_id`/chave "que parece certo": confirme a fonte real primeiro.
