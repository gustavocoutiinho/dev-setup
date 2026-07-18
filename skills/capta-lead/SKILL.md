---
name: capta-lead
description: Conserta CTA que "engole o lead": formulário que mostra toast de sucesso mas não faz POST nenhum, botão que só abre wa.me/window.open sem registrar quem clicou, contato que some sem ir pra lugar algum. Troca por captura real que GRAVA o lead num destino (Supabase / CRM Miner / planilha) e corrige o consentimento LGPD (checkbox de consentimento nunca nasce `checked`). Use SEMPRE que ver, num site ou landing da Miner, um form sem `fetch`/POST, um submit que só dá toast, um CTA que é só `window.open('https://wa.me/...')`, ou um `checked` num campo de consentimento. Dispara com "o form não salva nada", "cadê os leads", "esse botão não registra", "consentimento já vem marcado".
---

# capta-lead — captura real e consentimento honesto

Padrão que sangra dinheiro: a página parece converter (mostra "recebemos seu contato!") mas o lead não vai pra lugar nenhum. Esta skill faz o lead ser **gravado de verdade** e o consentimento ser **honesto** (opt-in real, nunca pré-marcado).

## Quando disparar
- `<form>` cujo submit só chama um toast/alert e um `preventDefault`, sem `fetch`/POST.
- CTA que é só `window.open('https://wa.me/...')` ou `location.href = 'wa.me/...'` sem registrar o clique/contato.
- Handler que "manda pro WhatsApp" mas não persiste nome/telefone em nenhum destino.
- Checkbox de consentimento/LGPD que nasce `checked` (pré-marcado) no HTML/JSX.

## Como executar
1. **Ache o destino certo.** Onde esse lead deveria cair? CRM Miner (multi-tenant, org do cliente), tabela no Supabase MinerOS, ou planilha do cliente. Confirme no vault (`obsidianminer`) qual é o destino daquele cliente antes de criar tabela nova. Padrão da casa: Vercel + Supabase, nunca Lovable.
2. **Grave antes de redirecionar.** No submit: `await` o POST que persiste o lead, cheque o retorno, e SÓ então mostre sucesso ou abra o `wa.me`. Se o POST falhar, mostre erro real, não toast de sucesso. Nada de fire-and-forget que engole a falha.
3. **Mínimo gravado:** nome, contato (telefone/e-mail), origem (qual página/campanha), timestamp, e o consentimento (valor real do checkbox + data). O `wa.me` continua abrindo, mas depois de gravar.
4. **Consentimento honesto.** Checkbox de consentimento nasce `unchecked`. O envio exige o opt-in marcado pelo usuário (valide no submit). Guarde o estado real do consentimento junto do lead, com data. Consentimento pré-marcado é irregular na LGPD e não vale.
5. **Confirme a captura de ponta a ponta.** Teste um envio real e veja o registro chegar no destino. "Toast apareceu" não é prova; o dado no Supabase/CRM é.
6. **Deploy com ok.** Aditivo, testado, deploy só com o Gustavo confirmando. Editar = deployar: só conta no ar.

## Gotchas
- Não exponha chave de escrita no front. O POST vai numa edge/rota server-side ou usa a anon key com RLS que só permite insert. Chave service_role nunca no client.
- CTA de WhatsApp costuma estar em vários pontos da página (hero, footer, sticky). Corrija todos, não só o primeiro.
- Se o destino é o CRM Miner, o lead tem que cair na org certa do cliente (tenant), não numa genérica.
- Guarde a origem do lead: sem isso o cliente recebe contato "do nada" e não sabe qual campanha converteu.

## O que NÃO fazer
- NÃO mostrar sucesso antes de confirmar que o POST gravou.
- NÃO deixar consentimento nascer `checked`, nem gravar lead sem registrar o consentimento real.
- NÃO pôr chave privada de gravação no front.
- NÃO trocar o texto/oferta do CTA a pretexto de "consertar": o escopo é capturar o lead e o consentimento, não reescrever a copy.
