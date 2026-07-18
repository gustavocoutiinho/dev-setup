---
name: dado-vivo
description: Troca dado real "assado" à mão (snapshot estático de dado num portal) por leitura viva de uma fonte (edge function / API) com cache versionado. Use SEMPRE que ver um portal ou app da Miner servindo dado de cliente chumbado no código: require de um *.json de dado, arrays gigantes de dado real dentro do front, um "atualizado: <data>" fixo no HTML, ou arquivos como portal-normatel/data/*.js e portal-accs/sf-snapshot.json. Dispara com "esse dado tá desatualizado", "de onde vem esse número", "isso é snapshot manual", "deixa vivo", "para de redigitar". O snapshot sempre desatualiza: o objetivo é a página ler a fonte de verdade sozinha.
---

# dado-vivo — do snapshot assado à leitura viva

Padrão recorrente na Miner: alguém colou o dado real (leads do Salesforce, base de obras, números do Meta) direto no repositório pra o portal funcionar hoje. Amanhã o dado envelhece e ninguém lembra de recolar. Esta skill mantém o **backend/portal funcionando** e move a **fonte do dado** pra algo vivo: uma edge function ou API que devolve o dado atual, com **cache versionado por hash** pra não bater na fonte a cada request.

## Quando disparar
- `require('...json')` ou `import dados from './data/*.js'` onde o conteúdo é dado real de cliente (não config).
- Arrays gigantes de registros reais embutidos num `.js`/`.jsx`/`.html` (ex: `~/dev/portais/portal-normatel/data/*.js`, o snapshot de 1,28MB).
- Um `sf-snapshot.json` ou parecido no repo (ex: `~/dev/portais/portal-accs/`), gerado à mão e commitado.
- Texto tipo `atualizado: 18/07/2026` chumbado, ou "última sincronização" que nunca muda.

## Como executar
1. **Mapeie a fonte de verdade.** De onde esse dado deveria vir? Salesforce (ACCS), Meta Ads, Bling/Olist, base do Supabase MinerOS. Confirme no vault (`obsidianminer`) qual credencial/edge já existe antes de criar coisa nova. Se a fonte depende de credencial pendente, PARE e registre no `radar-bloqueios`, não invente.
2. **Não quebre o backend.** Mantenha o mesmo contrato de dado (mesmo shape do JSON) que o front já consome. A troca é só na origem, não no consumo.
3. **Fonte viva via edge.** Prefira uma edge function no Supabase MinerOS que lê a fonte e devolve o JSON no shape esperado (o padrão da casa é Vercel + Supabase, nunca Lovable). Reaproveite edge que já exista pro cliente antes de subir outra.
4. **Cache versionado por hash.** A página busca `/<recurso>?v=<hash>` e serve com `Cache-Control: public, max-age=... , immutable`. Quando o dado muda, muda o hash, muda a URL, invalida sozinho. Nunca `no-store` em dado que muda devagar (isso mata a performance sem necessidade).
5. **Fallback e carimbo real.** Se a fonte cair, sirva o último cache bom e mostre a data REAL da última sincronização (vinda da fonte), não um texto fixo. Nada de "atualizado hoje" mentiroso.
6. **Deploy com ok.** Mudança aditiva, testada local, deploy só depois do Gustavo confirmar. Editar = deployar: só conta depois de estar no ar e confirmado.

## Gotchas
- Snapshot ACCS costuma carregar PII (lead com nome/telefone). Ao mover, cheque se a rota nova exige sessão. Se estava público, isso é caso de `blindar-portal` junto, não só de dado-vivo.
- Dado que muda de hora em hora (mídia) pede cache curto; base que muda por semana pede cache longo com hash. Não use o mesmo TTL pra tudo.
- Confira se sobrou o arquivo velho no repo depois da migração: snapshot órfão continua vazando dado antigo e engorda o bundle (aí chama `web-enxuta`).

## O que NÃO fazer
- NÃO trocar o dado sem manter o mesmo shape: quebra o front silenciosamente.
- NÃO inventar número quando a fonte não responde: sirva o último cache e marque "fonte não respondeu".
- NÃO subir provedor/serviço fora do padrão (Vercel + Supabase). Sem Lovable.
- NÃO deletar o snapshot antigo antes de confirmar que a leitura viva está no ar e batendo com o histórico.
