---
name: blindar-portal
description: Use SEMPRE que um portal/site da Miner servir dado sensível ou de cliente sem autenticação, ou tiver gate de login cosmético. Dispara ao ver arquivo de dado público (sf-snapshot.json, apollo-enriched.json, data/clientes-*.js, rastreio*.json respondendo HTTP 200), gate que "só troca um badge" sem redirect, PII em asset estático, chave server-side exposta, iframe sem sandbox, ou quando o Gustavo disser "fecha o vazamento", "blinda o portal", "isso tá exposto?", "tem dado vazando", "protege o portal X". Ação defensiva: fecha sem derrubar o cliente no ar.
---

# blindar-portal

Fecha vazamento de dado de cliente e auth cosmético em portais da Miner. O padrão que se repete: um portal serve `.json`/`.js` com dado real como asset estático (baixável por URL direta) e o "login" só mexe num badge no front, sem proteger nada server-side. Já confirmado no portal-accs e no portal-normatel; vale pra qualquer portal novo.

## Quando disparar
- `curl https://<portal>/<arquivo>.json` responde 200 com dado de cliente (nome, CNPJ, telefone, faturamento, base de CRM).
- Gate de login que no `!authenticated` só faz `return`/troca classe, sem redirect nem checagem server-side.
- Segredo (service_role, API key paga) hardcoded no front ou `.env` versionado (aí combine com [[varredura-segredos]]).
- Deploy antigo/fantasma (ex: `<projeto>-fix.vercel.app`) duplicando a mesma exposição.

## Como executar (na ordem)
1. **Mapeie o que está público.** `curl -s -o /dev/null -w "%{http_code}" https://<portal>/<arquivo>` em cada arquivo de dado; liste os que dão 200. Ache todos os deploys do projeto (`npx vercel ls <projeto>`) porque o vazamento pode estar num deploy esquecido.
2. **Decida se dá pra bloquear sem quebrar.** Para CADA arquivo, `grep -rn "<nome-do-arquivo>"` no repo: o **front** consome (`fetch('/x.json')`, `<script src="data/x.js">`) ou só o **backend** (`require('./x.json')` no proxy/api)?
   - **Só backend** → mova o arquivo pra fora do diretório público (`server/`, `_private/`, `data-internal/`), ajuste o `require`, e adicione ao `.vercelignore`. É o mais robusto: o dado nem é servido.
   - **Front consome** → o dado precisa ir pra trás de uma rota autenticada (um endpoint `/api/...` que valida a sessão antes de devolver). Não dá pra só bloquear o arquivo sem trocar a origem do front.
3. **Torne o gate real.** O dado não pode ser servível sem sessão válida: middleware/verificação server-side (cookie HMAC como o portal-accs/financeiro já usam), não um `if` no JS.
4. **Tire do git.** `git rm --cached <arquivos>` e endureça o `.gitignore`/`.vercelignore` (nunca só `.env`: cubra `*-enriched.json`, `sf-snapshot.json`, `rastreio*.json`, `data/*.js` de dado real).
5. **iframe** que renderiza URL do banco → sempre `sandbox`.
6. **Deploy + verifique** (ver abaixo). Mudança defensiva (mais restritiva) tende a não quebrar, mas confirme o portal logado depois.

## Como verificar
- O `curl` no arquivo vazado passa a dar **403/404**.
- O portal **logado ainda funciona** (as telas que usavam o dado carregam via a nova rota autenticada ou via backend).
- Nenhum outro deploy do projeto serve o arquivo.

## Gotchas
- Bloquear um arquivo que o **front consome** derruba a tela do cliente. Sempre cheque o consumo antes (passo 2).
- `.vercelignore`/`.gitignore` **não apaga o histórico**: arquivo já commitado continua no git history. Se havia segredo junto, ele está comprometido → rotacionar ([[varredura-segredos]]).
- Anon key do Supabase no front é **esperada** (não é vazamento). O problema é service_role e dado servido sem auth.
- Achar TODOS os deploys: um `<projeto>-fix`/`-old`/preview esquecido pode vazar o mesmo dado numa URL adivinhável.

## O que NÃO fazer
- Não confiar em gate client-side como proteção.
- Não deletar deploy/projeto sem o ok do Gustavo (delete é irreversível); despublicar/proteger primeiro.
- Não deployar em produção de cliente sem verificar que o portal ainda sobe depois.
