---
name: conserta-web
description: Use SEMPRE que um portal/app da Miner que JÁ existe estiver com defeito funcional: dado real chumbado à mão (snapshot estático que envelhece, require de *.json de dado, sf-snapshot.json commitado, carimbo de data fixo) que deveria ler a fonte viva, ou CTA/formulário que engole o lead (toast de sucesso sem POST, botão que só abre wa.me sem registrar, consentimento LGPD pré-marcado). Não é criar do zero nem redesign. Dispara com "esse dado tá desatualizado", "de onde vem esse número", "isso é snapshot manual", "deixa vivo", "para de redigitar", "o form não salva nada", "cadê os leads", "esse botão não registra", "consentimento já vem marcado".
---

# conserta-web: dado vivo e captura de lead que grava de verdade

Conserta o defeito FUNCIONAL num portal/app que já existe (não é criar do zero, [[criar-web]], nem redesign). Dois padrões que sangram na Miner: dado real chumbado à mão que envelhece parado no repo, e CTA que parece converter mas não grava lead nenhum. Padrão da casa: Vercel + Supabase, nunca Lovable. Sempre aditivo, sem regressão, confirmado no ar.

## Modos
- **dado assado → vivo:** troca snapshot estático por leitura da fonte real (edge function) com cache versionado por hash.
- **capta lead:** faz o form/CTA GRAVAR o lead num destino real e corrige o consentimento LGPD (nunca pré-marcado).

## Quando disparar
- **dado:** `require('...json')` ou `import dados from './data/*.js'` com dado real de cliente; arrays gigantes de registros num `.js/.jsx/.html` (ex: `~/dev/portais/portal-normatel/data/*.js`, snapshot ~1,28MB); um `sf-snapshot.json` commitado (ex: `~/dev/portais/portal-accs/`); um "atualizado 18/07/2026" chumbado. "esse dado tá desatualizado", "de onde vem esse número", "deixa vivo", "para de redigitar".
- **lead:** `<form>` cujo submit só dá toast/alert com `preventDefault` e sem `fetch`/POST; CTA que é só `window.open('https://wa.me/...')` sem registrar; checkbox de consentimento que nasce `checked`. "o form não salva nada", "cadê os leads", "esse botão não registra", "consentimento já vem marcado".

## Como executar
Comum: confirme no vault ([[obsidianminer]]) qual é a fonte/destino REAL daquele cliente antes de criar coisa nova. Se falta credencial ou decisão, PARE e registre o bloqueio, não invente número. Mudança aditiva, testada local, deploy só com o Gustavo confirmando ([[deploy]]).

**Dado vivo:** mapeie a fonte de verdade (Salesforce no ACCS, Meta Ads, Bling/Olist, base do Supabase MinerOS; a integração pode já existir em [[dados]]). Mantenha o MESMO shape do JSON que o front já consome (a troca é na origem, não no consumo). Sirva por edge function no Supabase MinerOS que lê a fonte e devolve o JSON esperado (reaproveite edge que já exista pro cliente antes de subir outra). Cache versionado: a página busca `/<recurso>?v=<hash>` com `Cache-Control: public, max-age=..., immutable`; mudou o dado, muda o hash, muda a URL, invalida sozinho (nunca `no-store` em dado que muda devagar). Fallback: se a fonte cair, sirva o último cache bom e mostre a data REAL da última sincronização (vinda da fonte), nunca um "atualizado hoje" mentiroso.

**Capta lead:** ache o destino certo (CRM Miner na org/tenant do cliente, tabela no Supabase MinerOS, ou planilha do cliente). No submit, `await` o POST que persiste o lead, cheque o retorno, e SÓ então mostre sucesso ou abra o `wa.me`; se o POST falhar, mostre erro real, nada de fire-and-forget que engole a falha. Grave no mínimo: nome, contato (telefone/e-mail), origem (página/campanha), timestamp e o consentimento real + data. Checkbox de consentimento nasce `unchecked` e o envio exige o opt-in marcado pelo usuário (pré-marcado é irregular na LGPD e não vale). Confirme de ponta a ponta: teste um envio real e veja o registro chegar no destino ("toast apareceu" não é prova; o dado no Supabase/CRM é).

## Gotchas
- Snapshot ACCS costuma carregar PII (lead com nome/telefone). Ao mover pra rota viva, cheque se ela exige sessão; se estava público, é caso de [[blindar]] junto, não só de dado vivo.
- TTL por tipo de dado: mídia muda de hora em hora (cache curto), base muda por semana (cache longo com hash). Não use o mesmo TTL pra tudo. `immutable` só com hash no nome.
- Confira se sobrou o snapshot velho no repo depois de migrar: órfão continua vazando dado antigo e engorda o bundle (aí é [[faxina-web]]).
- Não exponha chave de escrita no front: o POST vai numa edge/rota server-side ou usa a anon key com RLS que só permite insert; service_role NUNCA no client.
- CTA de WhatsApp costuma estar em vários pontos (hero, footer, sticky): corrija todos, não só o primeiro. Se o destino é o CRM, o lead cai na org certa do cliente (tenant), não numa genérica.

## O que NÃO fazer
- NÃO trocar o dado sem manter o mesmo shape (quebra o front silenciosamente), nem inventar número quando a fonte não responde (sirva o último cache e marque "fonte não respondeu").
- NÃO mostrar sucesso antes de o POST gravar, nem deixar consentimento nascer `checked` ou gravar lead sem registrar o consentimento real.
- NÃO pôr chave privada de gravação no front.
- NÃO deletar o snapshot antigo antes de confirmar a leitura viva no ar batendo com o histórico.
- NÃO reescrever a copy/oferta do CTA a pretexto de "consertar": o escopo é o dado e a captura, não o texto. Sem provedor fora do padrão (Vercel + Supabase, sem Lovable).
