# Regras de casa dos portais Miner

Fonte única das armadilhas já pagas em produção. Vale para todo portal, site, LP e app de cliente da Miner, inclusive os que ainda vão nascer.

Cada regra aqui saiu de um incidente real, com data. Não são boas práticas genéricas: são erros que já custaram retrabalho, dado perdido ou cliente fora do ar. Antes de mexer em qualquer portal, leia. Ao aprender algo novo do mesmo tipo, acrescente aqui (ver "Como manter isto vivo", no fim).

Instalado em `~/.claude/estaleiro/portais-miner.md` pelo `install-skills.sh`. Fonte versionada: `~/dev/dev-setup/claude/portais-miner.md`.

---

## 1. Dado do cliente nunca se perde

**Regra:** toda operação em portal é ADITIVA. Schema, migração, import de planilha, edição de conteúdo estático. Nada é apagado, sobrescrito ou substituído sem confirmação explícita do Gustavo antes de executar.

- Migration: só `CREATE TABLE` e `ADD COLUMN`. `DROP` e `ALTER` destrutivo só com autorização a cada caso.
- Import de planilha ou CSV: tela de conferência antes de gravar. Nunca sobrescrever registro existente em silêncio.
- Conteúdo estático (HTML com dado dentro): acrescentar e atualizar, nunca remover bloco existente sem avisar.
- Banco compartilhado (Supabase MinerOS hospeda vários clientes): inspecionar antes de criar, e nomear com prefixo exclusivo do módulo.

**Origem:** 23/06/2026, Festival Costume Gourmet. Uma função `stripPhotos()` salvava em "modo sem-foto" quando o payload passava de um limite. As 95 fotos dos cards do cronograma foram para o vazio, sem backup no banco. Recuperação só por cache de navegador ou PITR. O Gustavo reforçou a regra com todas as letras durante a migração do módulo de patrocínios.

**Padrão que gera esse erro:** qualquer caminho de código que degrada silenciosamente quando o payload cresce. Se precisar degradar, o certo é falhar e avisar, nunca salvar pela metade.

---

## 2. Deploy de produção é decisão do Gustavo, sempre

**Regra:** `vercel deploy --prod` e `vercel promote` promovem por cima do que está no ar, na hora. Não é preview, não é PR. Só rodar com autorização explícita a cada deploy. Na dúvida, preview.

**Antes de editar qualquer coisa:**
```bash
git fetch origin
git checkout -b <branch> origin/main
```
A `main` de portal recebe commit concorrente (automação diária, outra sessão, outra pessoa). Base velha apaga o que já está publicado.

**Depois de publicar:** conferir a produção com `curl` e procurar o marcador da mudança, e também conferir que o que NÃO deveria mudar continua lá. Nunca dizer "está no ar" sem essa checagem.

**Origem:** 23/06/2026, MinerCRM. Sequência de `vercel --prod` a partir de um branch antigo sobrescreveu a produção. Pior: a produção nem era a `main`, era `design-monocromatico`, e o deploy apagou o módulo Parceiro da ForYou (rota `/parceiros` virou 404 quando deveria dar 307).

**Descobrir qual branch a produção usa antes de deployar. Nunca assumir que main é igual a produção.**

**Conserto quando acontece:** `vercel rollback <url-do-deploy-bom> --yes` restaura o código na hora (banco e RLS não são afetados). Depois de um rollback, o alias fica preso: novos `--prod` buildam mas não promovem sozinhos, é preciso `vercel promote <novo-url> --yes`. Conferir o alias real com `vercel inspect <dominio> | grep url`.

---

## 3. Como cada projeto publica é diferente. Descubra antes

Não existe padrão único. Antes de qualquer entrega, saiba qual dos três é:

| Modo | Como publica | Exemplo |
|---|---|---|
| Push na main | commit e push, a Vercel sobe sozinha | fcg-site, festival-costume-gourmet |
| Só por CLI | push no GitHub NÃO publica, precisa `vercel deploy --prod` | sinobras-eventos-lp |
| Pasta canônica | o deploy tem que sair da pasta completa | portal-accs |

**Origem:** 10/08/2026, LP SINOBRAS. Header corrigido, commit no GitHub, e a produção continuou com o header velho porque aquele projeto sobe por CLI.

---

## 3b. A produção pode estar ADIANTE do git. Confira antes de pushar

**Sintoma:** uma rota que não existe no repositório responde 200 em produção. Uma tabela citada só numa migration não commitada já tem dado real no banco. Um cron que não está no `vercel.json` do git está rodando.

**Causa:** deploy por CLI publica a pasta local, não o commit. Quem deployou sem commitar deixou o git atrás do que está no ar.

**Por que é perigoso:** se o projeto também publica por push, o próximo push da `main` republica a versão velha e **apaga do ar** tudo que nunca foi commitado. O portal cai por um commit que parecia inofensivo.

**Regra:** antes de pushar em qualquer portal, confirme que o git bate com a produção. Uma linha resolve:
```bash
curl -s -o /dev/null -w '%{http_code}\n' https://<dominio>/api/<rota-que-so-existe-no-local>
```
200 numa rota que o git não tem significa que a produção está adiante. Nesse caso, **commitar primeiro, pushar depois**. Nunca o contrário.

**Origem:** 11/08/2026, accs-eventos. 2.590 linhas, 42 rotas novas, 8 migrations e 2 páginas estavam em produção havia dias sem nenhum commit. As tabelas já tinham dado real (`acev_leads_meta_ads` com 6 leads capturados pelo cron). Um push de rotina teria derrubado fila de atendimento, agenda de diretoria, IA e a sincronização do Meta Ads de uma vez.

**Regra irmã:** trabalho que só existe na pasta local não existe. Terminou de deployar, commite.

---

## 4. Deploy parcial derruba o backend inteiro

**Regra:** em portal que tem `/api`, o deploy sai da pasta completa, com `proxy.js` ou `server.js`, `api/all.js`, `vercel.json` e `package.json`. Nunca de uma pasta que contenha só o `index.html`.

**Sintoma:** o portal abre normal e toda chamada `/api/...` responde 404. Na tela: "Erro: HTTP 404" nas seções que dependem de dado.

**Causa:** o `vercel.json` faz rewrite de `/api/(.*)` para `/api/all`, que delega ao Express. Sem esses arquivos, a produção vira site estático e o rewrite aponta para o nada.

**Origem:** 02/06/2026, portal ACCS. Funil por vendedor e Caça Negócio fora do ar.

---

## 5. Pasta `public/` sequestra a raiz do projeto

**Regra:** em portal servido como HTML na raiz, nunca criar uma pasta `public/`. A Vercel auto-detecta ela como diretório de saída, mesmo sem framework definido, e passa a ignorar os HTMLs da raiz.

**Blindagem no `vercel.json`:**
```json
{ "framework": null, "outputDirectory": "." }
```

**Origem:** 29/07/2026, accs-eventos. Mesmo comportamento no template `plataforma-eventos`. Assets ficam fora de `public/`.

---

## 6. PII não mora no que o navegador baixa sozinho

**Regra:** base de clientes, obras, decisores, telefone, e-mail e CNPJ nunca ficam em arquivo servido publicamente (`data/*.js`, JSON solto, HTML inline). Ficam em `api/_data/*.json`, servidos por rota que exige sessão. Deslogado responde 403.

**Como conferir de verdade:** pedir o arquivo antigo pelo navegador e esperar 404 ou 403. Se responder 200, ainda está vazando.

**Origem:** 20/07/2026, portal Normatel. Datasets de 440 KB e 695 KB abertos, mais uma página com 91 e-mails e 178 telefones de decisores embutidos inline no HTML, que escapou da primeira varredura por não estar em `data/*.js`.

**Detalhe que salva tempo:** `<script src>` não executa corpo de resposta 4xx. Para redirecionar quem está deslogado, a rota responde 200 com `location.replace('/login?next=')`, senão a página só mostra "não foi possível carregar".

---

## 7. Todo portal Miner é magic link. Nunca senha compartilhada

**Regra:** acesso por magic link com domínio autorizado. Gate por senha única compartilhada está proibido, mesmo como paliativo enquanto o SMTP não está configurado.

- Cookie HMAC httpOnly e Secure, link com validade curta, rate limit.
- Papel por domínio: `@minerbz.com.br` é admin, o domínio do cliente é membro.
- Fail-open é aceitável enquanto o e-mail não está configurado (`emailReady=false` libera), mas isso é estado temporário, não solução.
- Gate cosmético no front não é gate. O que protege é a rota do servidor.

**Armadilhas já pagas:** link em subpath dando 404, `apikey` obrigatória esquecida na chamada, e o `initApp` derrubando o usuário já autenticado de volta para o login.

**Prova de que funciona:** simular o clique real no navegador. Mudança de login só está pronta depois disso, não depois do commit.

---

## 8. Front: as três que sempre voltam

**Cache de asset.** `/js` e `/css` costumam ir com `max-age=3600`. Corrigiu script, versione a query string (`lp.js?v=iframe1`), senão quem já visitou continua recebendo o arquivo velho por até uma hora e o bug "não morre".

**Página dentro de iframe.** Duas coisas quebram:
1. `X-Frame-Options: SAMEORIGIN` bloqueia. Trocar por `Content-Security-Policy: frame-ancestors 'self' https://dominio-do-cliente https://www.dominio-do-cliente`, com os dois hosts, porque o site do cliente costuma redirecionar para o `www`.
2. `IntersectionObserver` pode nunca disparar dentro de frame, porque a página-mãe não rola. Resultado: só a barra do topo aparece, blocos `[data-reveal]` presos em `opacity: 0`, contadores em zero. Detectar com `window.self !== window.top` e mostrar tudo de cara. **Nenhuma LP que possa rodar em iframe deve depender de observer para revelar conteúdo.**

**Tema injetado por último.** Um CSS de tema com `:root` que define `--bg` e `--text` e é injetado depois de tudo sobrescreve o fundo de qualquer página escura que use os mesmos nomes de variável. Prefixe as variáveis da página nova.

---

## 9. Canal de mensagem é o do cliente, não o cru

**Regra:** na Aço Cearense, toda ação de "enviar ao cliente" passa pela Blip. Nunca link `wa.me`. Canal gerenciado e rastreado é requisito, não preferência.

Vale a leitura geral: cada cliente tem o canal oficial dele (Blip, Omnichat, Suri, Chat.guru). Portal não inventa canal paralelo.

---

## 10. Número de cliente é exato

**Regra:** dado de venda, meta e resultado entra com o valor exato da fonte que o Gustavo passou. Nunca extrapolar mês parcial, nunca estimar para "fechar" a conta, nunca completar série. Mês incompleto é marcado como parcial.

---

## 11. Segredo

- `.env`, `.env.local`, `.env.vercel.local`, tokens de serviço: fora do git, fora do deploy, nunca impressos no chat, nunca movidos para o front.
- Chave que já foi versionada ou servida ao público está comprometida. Remover do arquivo não resolve: tem que ser revogada e trocada na origem.
- Rota de IA no portal precisa de sessão e cota por IP, senão vira consumo de crédito aberto.

---

## 12. Ambiente

- A rede da Aço Cearense bloqueia `github.com` (proxy MITM com certificado próprio). De lá, `git fetch` e `gh api` falham. Vercel e `*.vercel.app` passam.
- Código nunca em iCloud nem em Google Drive. Casa canônica é `~/dev`. Path do CloudStorage dá timeout de leitura.
- Quando existir cópia arquivada de um projeto, ela é só leitura. Editar só a casa canônica.

---

## Checklist de portal novo

Antes de considerar um portal pronto para o cliente ver:

1. Casa canônica em `~/dev`, repositório privado no GitHub, `.vercel` linkado.
2. `.gitignore` cobrindo `.env*` e qualquer arquivo de dado com PII, verificado com `git ls-files | grep -E '(^|/)\.env'`.
3. Auth por magic link com os domínios certos, testado com clique real no navegador.
4. Nenhum dado sensível servido sem sessão, testado pedindo o arquivo deslogado.
5. Modo de publicação documentado no perfil do projeto (push, CLI ou pasta canônica).
6. `vercel.json` explícito: `framework`, `outputDirectory`, rewrite de `/api`, headers de cache e segurança.
7. Favicon e identidade Miner aplicados, subdomínio `*.minerbz.com.br` apontado.
8. Estados de tela honestos: dado real, estrutura pronta sem base ainda, ou pendente com o motivo. Nunca zero falso nem número inventado.
9. Teste ponta a ponta do fluxo principal antes de divulgar, com o registro de teste limpo depois.
10. Perfil do Estaleiro (`.claude/estaleiro/perfil.md`) preenchido, com a zona proibida específica do projeto.

## Checklist de evento novo (Grupo Aço Cearense)

Padrão fixo, detalhado no README do repositório `accs-eventos`: cadastro em `acev_eventos`, landing `sinobras-<evento>-lp` gravando via `sin_lead_insert`, NPS nativo em `/nps?ev=<id>` (nunca SurveyMonkey), QR Codes pela Central de Links, conferência da Central e teste ponta a ponta com uma inscrição e um NPS de teste, limpos depois. Landing e NPS são fonte única no cadastro do evento, nunca link solto no código.

---

## Como manter isto vivo

Este arquivo só serve se crescer com a operação. Quando um portal quebrar por um motivo que ainda não está aqui, ou quando o Gustavo der uma regra nova:

1. Acrescente a regra na seção certa, com **sintoma, causa e data**. Sintoma primeiro, porque é por ele que a próxima pessoa vai procurar.
2. Nunca remova regra existente. Se ficou obsoleta, marque como superada e diga o que a substituiu.
3. Edite a fonte versionada (`~/dev/dev-setup/claude/portais-miner.md`), commite, e rode `./install-skills.sh` para valer nas duas máquinas.
4. Se a regra for específica de um projeto, ela vai para a zona proibida do perfil daquele repositório. Aqui ficam só as que valem para mais de um.
