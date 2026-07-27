# Setup das integrações pendentes (levantado em 23/07/2026)

Pesquisa completa (7 agentes, documentação oficial) do processo exato pra fechar as lacunas ❌/⚠️ do [SKILL.md](SKILL.md). Guarda aqui o plano técnico; o [SKILL.md](SKILL.md) mantém só o resumo de status. Tudo na conta gustavo@minerbz.com.br (ou squad@minerbz.com.br onde a nota do vault `google-account-standard-squad` mandar).

## Ordem recomendada (por alavancagem: menor espera + maior valor primeiro)

| # | Integração | Fila de aprovação | Esforço técnico | Acesso por cliente novo depois |
|---|---|---|---|---|
| 1 | **Search Console** | Nenhuma (scope não-sensível desde 2024, minutos) | Baixo, reaproveita projeto GCP do Ads | Automático — a conta já é owner/user de cada propriedade |
| 2 | **Google Ads Basic Access** | Até 5 dias úteis (relatos de atraso por alta demanda) | Baixo, reaproveita projeto GCP | Automático — hierarquia da MCC 857-172-5825 |
| 3 | **Clarity** | Nenhuma (self-service) | Baixo, mas repete por projeto/cliente | Manual — criar 1 projeto por cliente |
| 4 | **TikTok Organic API** | ~2-3 dias úteis (pode esticar 1-4 semanas) | Médio | QR code por conta de cliente (rápido, sem nova revisão) |
| 5 | **Pinterest API v5** | Trial: dias. Standard: dias a semanas + vídeo demo | Médio | OAuth por cliente, ou bridge via `ad_account_id` se o cliente tiver conta de anúncios |
| 6 | **YouTube Data/Analytics** | Verificação de escopo sensível: dias a poucas semanas | Médio, mesmo projeto GCP | Cada cliente precisa logar e autorizar (não existe atalho tipo MCC) |
| 7 | **LinkedIn Community Management API** | Development: 1-4 semanas. Standard: 4 semanas a 3-4 **meses**, às vezes 6 | Alto (vídeo demo, app rejeitado não pode reaplicar) | Cliente precisa te tornar **Administrator** da própria Company Page (não Analyst) — pedido de confiança alto |

Google Ads e TikTok têm a fila mais longa dentre os "vale a pena": valem submissão do formulário o quanto antes, mesmo que o resto do setup técnico termine depois. LinkedIn é o item mais caro/arriscado (meses, pode ser rejeitado e não dá pra reaplicar com o mesmo app) — vale confirmar se algum cliente relevante da carteira realmente usa LinkedIn como canal antes de entrar nessa fila.

## 1. Google Search Console API — ✅ PRONTO (24/07/2026)

Projeto GCP `miner-493616` ("Miner"), API ativada, OAuth consent screen tipo Interno criado, client OAuth "Miner - Search Console e Ads (CLI)" criado. Secrets em `~/.miner-secrets/google-cloud/` no Mac mini (`oauth-client-search-console-ads.json`, `token-search-console.json`, chmod 600, fora de qualquer repo). Token com `refresh_token` válido gerado via `gerar_token_search_console.py`, testado com sucesso via `testar_search_console.py`.

**Achado importante:** a conta `gustavo@minerbz.com.br` só enxerga 2 propriedades no Search Console: `sc-domain:lesalis.com.br` (siteOwner) e `https://risedentalmelbourne.com/` (siteFullUser). **PRLS não aparece** — a nota do vault (`prls-seo.md`) registra que a propriedade PRLS está sob `squad@minerbz.com.br`. Falta repetir o fluxo de consentimento com squad@ (ou pedir pra alguém adicionar gustavo@ como usuário na propriedade PRLS) antes de usar isso no raio-x da PRLS. `lesalis.com.br` não está mapeado em nenhuma memória do vault — investigar o que é antes de reportar dado dele num raio-x.

Passo a passo original (referência, já executado):

1. Confirmar qual conta é owner/user de cada propriedade-alvo (padrão do vault: squad@minerbz.com.br).
2. Reaproveitar o projeto Google Cloud "Miner - GA" (mesmo do Google Ads).
3. Ativar "Search Console API" em APIs & Services > Library.
4. OAuth consent screen: se `minerbz.com.br` é Workspace, usar tipo **Internal** (zero fricção). Scope `webmasters.readonly` é NÃO sensível — sem fila de verificação.
5. Criar OAuth Client ID, rodar o consentimento **uma vez** logado como squad@/gustavo@, publicar o app ("In production") pra o refresh token não expirar em 7 dias.
6. Testar `sites.list` (deve listar toda propriedade que a conta já vê) e `searchanalytics.query`.
- Lib: Python `google-api-python-client`; Node `@googleapis/searchconsole` (dá pra reaproveitar o pacote `googleapis` genérico se a Miner já usa em alguma edge function).
- Guardar a credencial como secret no Supabase (padrão `miner_api_credentials`/`{enc}` da skill [[integra]]), não em `.env` versionado.

## 2. Google Ads API (Basic Access) — ⏳ pedido enviado (24/07/2026)

Basic Access Application submetido oficialmente para o developer token da MCC "Miner - GA" (857-172-5825), projeto GCP `miner-493616` (346541077547), contato gustavo@minerbz.com.br. Google confirmou recebimento: revisão em até 5 dias úteis, sem garantia de prazo (pode pedir mais informação). Documento de design anexado: `~/.miner-secrets/google-cloud/miner-google-ads-api-design.rtf`. Capability marcada: **Reporting** apenas (a ferramenta é só leitura via GAQL; não marcar Account/Campaign Creation/Management — isso contradiria a descrição escrita e é motivo de reprovação).

Falta ainda (pode ser feito sem esperar a aprovação, só não vai retornar dado real de conta de produção até o Basic sair):
- Adicionar o scope `https://www.googleapis.com/auth/adwords` na OAuth consent screen do projeto `miner-493616` (hoje só tem `webmasters.readonly` do client "Miner - Search Console e Ads (CLI)", que já existe e pode ser reaproveitado)
- Gerar refresh token via `google-ads-python` (`generate_user_credentials.py`) ou script equivalente ao usado no Search Console
- Montar o `google-ads.yaml` com developer_token + client_id + client_secret + refresh_token + login_customer_id (8571725825)

Passo a passo original (referência):

1. No API Center da MCC "Miner - GA" (ads.google.com/aw/apicenter): revelar o developer token (pede reautenticação de senha).
2. No menu do Access level, "Apply for Basic Access": nome da empresa, URL do site, categoria "reporting/agência", aceitar termos.
3. Opcional pra acelerar: completar "brand verification" do projeto GCP (piloto desde 07/07/2026, reduz revisão de dias pra horas).
4. Em paralelo (não depende do Basic sair): criar OAuth consent screen tipo Desktop no mesmo projeto GCP, scope `https://www.googleapis.com/auth/adwords` (sensitive scope). **Manter em modo Testing com test users cadastrados** (evita a fila de App Verification de 3-5 dias — suficiente pro uso 100% interno da Miner).
5. Criar OAuth Client ID tipo "Desktop app", gerar refresh token com o script oficial `generate_user_credentials.py` (repo `googleads/google-ads-python`) — o Gustavo loga e clica "Permitir" uma única vez.
6. Reunir developer_token + client_id + client_secret + refresh_token + login_customer_id (8571725825, sem hífen) num `google-ads.yaml`.
7. Testar `list_accessible_customers` assim que o Basic sair.
- Lib recomendada: `google-ads-python` (oficial). Não existe pacote npm oficial da Google (diferente do `meta-ads-mcp` que a Miner já usa). Existe MCP server oficial `github.com/googleads/google-ads-mcp` (Python via pipx, só leitura — bate com o caso de uso).
- Basic Access dá 15.000 operações/dia, suficiente pra carteira atual.

## 3. Microsoft Clarity + Data Export API — ✅ instalado em 3 sites (24/07/2026)

Zero fila, mas repete por cliente (cada projeto tem token e URL próprios). Login gustavo@minerbz.com.br em clarity.microsoft.com.

**Regra pra qualquer integração nova daqui pra frente: sempre conectar em conta/GTM/projeto que já existe antes de criar um novo** (pedido explícito do Gustavo 24/07 — vale pra Clarity, GTM, Google Ads, qualquer coisa).

Status por cliente:
- **PRLS** (prls.com.br, projeto `xrh00nz2xd`) — app "Microsoft Clarity: AI Insights" instalado via Shopify App Store (conta admin logada, loja `prlsteste`), modo "Clarity only" (não "Brand Agents" — isso ligaria um chatbot de IA na loja, fora do escopo pedido). Confirmado "Instalado com êxito usando Shopify".
- **Le Salis** (lesalis.com.br, projeto `xrgz7epb03`) — mesma receita, também Shopify (loja `lesalis`). O rádio "Clarity only" no wizard tem um bug de clique via automação (iframe não responde a clique sintético); Gustavo mesmo selecionou na tela dele.
- **Normatel** (normatel.com.br, projeto `xrhbsh7rv7`) — **não é Shopify, é Wake Commerce/fbits**. `normatel.fbits.app` é só o painel ADMIN, não o site (aprendido na hora, corrigi a URL do projeto depois). Instalado via conexão OAuth ao Google Tag Manager já existente do cliente: conta "Normatel Home Center", contêiner "E-Commerce" (achado na lista de contas do GTM que a conta Google já tinha acesso — não foi preciso criar nada novo). Confirmado "Instalado com êxito usando Google Tag Manager".
- **Miner (minerbz.com.br)** — projeto criado automaticamente no primeiro login, ainda sem snippet instalado (é o site institucional da própria Miner, baixa prioridade).
- **Normatel Premium** (normatel-premium.vercel.app, projeto `xrjvm8x42s`) — CRM interno da Miner pra ARD Grupo (repo `gustavocoutiinho/crm-normatel`, não confundir com o site institucional `normatel.com.br` já coberto acima). Instalado direto no código-fonte: `next/script` (`strategy="afterInteractive"`) no `<head>` do `src/app/layout.tsx`. Branch `add-microsoft-clarity`, PR aberto: github.com/gustavocoutiinho/crm-normatel/pull/1 — **não mergeado ainda, pendente aprovação do Gustavo** (é deploy de produção de um CRM que ele usa, não mergeei sozinho).
- **Bloqueado — Clínica OTHN** (clinicaotorhinos.com.br, projeto `xrjpksbzcz` criado, setor Saúde e Bem-estar) — não tem GTM detectado; tentei `/wp-admin/` e `/wp-admin/plugins.php` e ambos caem na página 404 do tema (sem sessão logada nem tela de login do WordPress). Preciso que o Gustavo confirme se a Miner tem credencial de admin desse WordPress, ou instale o plugin oficial "Microsoft Clarity" ele mesmo com o Project ID `xrjpksbzcz`.
- **Bloqueado — Hidrotintas** (hidrotintas.com.br, projeto `xrjtbd033c` criado, setor CPG) — site usa GTM (`GTM-KZMW6XD9`), mas esse contêiner não está entre os que a conta `gustavo@minerbz.com.br` tem acesso no Gerenciador de Tags do Google (mesma lista de sempre: Brusinhas, Emilio Ribas, RCL Mentoring, Cidadão do Brasil, Casa de Pedra, Artefapi, Normatel Home Center, Butcher's, Carbone, Thais Ferreira, Aura By AL, Rise Dental Melbourne, 4YOU). Preciso que o cliente adicione gustavo@minerbz.com.br como usuário do contêiner `GTM-KZMW6XD9`, ou que o Gustavo cole o snippet manual (Project ID `xrjtbd033c`) direto no site.
- **Costume Saudável = Festival Costume Gourmet** (confirmado por agente de pesquisa no vault, 24/07/2026: `clientes-ativos-jul2026.md` e `project_relatorios_vivos.md` chamam o mesmo cliente/evento de "Costume Saudável" ou "FVCG"). URL pública correta: `costumegourmet.minerbz.com.br` (site institucional/vendas, React/Vite, source em `~/dev/sites/fcg-site`, sem git — deploy só via `vercel deploy --prod --yes`; ver [[festival-site-fcg]]). **Não confundir** com `festival.minerbz.com.br`, que é o portal interno do time com gate de login ([[festival-gate-stack]]). Projeto Clarity criado (`xrjy7k660c`, setor Restaurantes e Alimentação). Snippet já inserido em `~/dev/sites/fcg-site/index.html` (dentro do `<head>` estático, antes do `</head>`) — **falta rodar `vercel deploy --prod --yes` pra ir ao ar**; não rodei sozinho porque é o site público ao vivo do festival, pedi confirmação do Gustavo antes.
- **URLs confirmadas pelo Gustavo em 24/07/2026** (respondeu direto no chat, exceto Porão que ficou pendente):
  - **Aço Cearense** (`grupoacocearense.com.br`, projeto `xrk6we5ruv`, setor Serviços B2B) — site tem GTM (`GTM-K2JCVFD7`), mas não está entre os contêineres que `gustavo@minerbz.com.br` acessa (mesma lista de sempre). Bloqueado, precisa acesso.
  - **Ju Omakase** (`juomakase.com.br`, projeto `xrk85zo6vz`, setor Restaurantes e Alimentação) — site **sem GTM detectado**. Instalação só via snippet manual no código/CMS do restaurante — precisa saber quem administra o site.
  - **ForYou** (`foryouessential.com.br`) — **já tem Clarity rodando**, projeto "[4YOU] E-commerce", só que em conta Microsoft diferente de `gustavo@minerbz.com.br` (não aparece na lista de projetos dela; a conta Google `gustavo@minerbz.com.br` tem acesso ao contêiner GTM `foryouessential.com.br` dentro da conta GTM "4YOU", mas o Clarity que usa esse contêiner pertence a outra conta Microsoft). **Não criei projeto novo** (cheguei a criar e apaguei, pra não duplicar/quebrar a instalação existente ao reconectar o GTM). Falta o Gustavo indicar quem tem acesso a esse Clarity (provável squad@minerbz.com.br ou conta própria do time ForYou) pra pegar o token de Data Export de lá.
  - **Mercadinhos São Luiz** (`mercadinhossaoluiz.com.br`, projeto `xrkaqceo4j`, setor Varejo) — e-commerce, GTM `GTM-PL2TJT6N` sem acesso da conta Miner. Bloqueado.
  - **Mercadão São Luiz** (`mercadaosaoluiz.com.br`, projeto `xrkbx7y7z3`, setor Varejo) — site institucional (Wix), GTM `GTM-TRFP8PZL` sem acesso da conta Miner. Bloqueado. **Confirmado que é entidade diferente de Mercadinhos São Luiz** (domínios e GTMs distintos, apesar do nome parecido), então valeu criar os dois projetos separados.
  - **Porão** — não veio na resposta do Gustavo (ele mandou 5 URLs pros outros 6 itens, Porão ficou de fora). Ainda sem projeto Clarity, sem confirmar antes de criar.
- **Pendente separado**: Luxo Natural (luxonatural.com.br) e DLT (estilodlt.com.br) — descobertas por acaso na lista "Suas lojas" do Shopify da mesma conta admin; nenhuma delas tinha sido mapeada no vault antes disso, nem estavam na lista de 10 clientes pedida pelo Gustavo — não criar projeto sem ele confirmar que quer.

Passo a passo (referência):
1. "New project" por cliente (sem limite de projetos numa conta).
2. Instalar snippet: Shopify tem app oficial na App Store ("Microsoft Clarity: AI Insights") — instala, escolhe "Clarity only", ativa toggle "Clarity JS" na config do tema. Se o site já tem GTM, mais simples: Settings > Integrações > Gerenciador de tags do Google > conectar na conta/contêiner existente (cria e publica a tag automaticamente, sem mexer no código do site).
3. Site estático sem GTM (Vercel/HTML puro): copiar o `<script>` gerado pro `<head>` do layout raiz, redeploy.
4. Settings > Data Export > "Generate new API token" (só Admin do projeto; token só aparece uma vez, guardar como secret) — ainda não feito pra nenhum dos 3.
5. Consumir: `GET https://www.clarity.ms/export-data/api/v1/project-live-insights?numOfDays=1&dimension1=...` com `Authorization: Bearer <token>`.

**Limitação que muda o uso no raiox:** rate limit de **10 requisições/dia por projeto**, cada chamada só cobre 1-3 dias (sem histórico retroativo via API), retenção de gravação 30 dias / dado agregado 9 meses. Serve bem pro raiox mensal (poucas chamadas), não serve pra dashboard em tempo real. Existe MCP server oficial da Microsoft (`github.com/microsoft/clarity-mcp-server`) — vale avaliar em vez de escrever wrapper próprio.

**Gotcha de automação:** o wizard "How would you like to set up Clarity?" dentro do app Shopify roda num iframe que bloqueia clique sintético no radio button (`left_click` via extensão não registra) — precisa de clique humano real nessa etapa específica.

## 4. TikTok Organic API (Accounts API, dentro da TikTok API for Business)

Não confundir com Marketing API (ads) nem Display API (login de app consumidor).

1. Criar/usar o Business Center da Miner (business.tiktok.com).
2. Em business-api.tiktok.com/portal, criar conta de desenvolvedor vinculada ao Business Center, criar um App (nome, política de privacidade real, redirect URI).
3. Solicitar o produto **Organic API > Accounts API** (não pedir Marketing API junto — atrasa a revisão).
4. Submeter pra revisão (~2-3 dias úteis, pode esticar 1-4 semanas).
5. Aprovado: gerar URL de autorização, autorizar o App contra o próprio Business Center da Miner.
6. Por cliente: Business Center > Accounts > "Add a TikTok account" > "Link an existing account", permissão **"Manage account"** (não "Deliver ads only"), gera QR code → cliente escaneia pelo app do TikTok no celular e aprova. Se a conta do cliente for pessoal, precisa virar Business primeiro.
7. Repetir só o passo 6 pra cada cliente novo — não repete revisão da TikTok.
- SDK oficial: `tiktok/tiktok-business-api-sdk` (Python, Node, Java, PHP, Go).
- Rate limit exato da Accounts API não confirmado na doc pública (SPA em JS); conferir dentro do portal antes de desenhar frequência de sync.

## 5. Pinterest API v5 — ❌ descartado (decisão do Gustavo, 24/07/2026)

Travou logo no início: não existe conta Pinterest Business da Miner (nem vinculada ao Google da Miner), e criar conta é ação que exige o Gustavo (não é algo que se automatiza). Perguntado, ele decidiu não ter interesse em seguir. Não criar conta nem retomar sem pedido explícito.

Passo a passo original (referência, não executado):

1. Conta Pinterest Business (não pessoal) da Miner, aceitar Developer Terms em developers.pinterest.com.
2. "Connect app": nome, descrição, redirect URI → pedido de acesso **Trial** (revisão diária, aprovação rápida).
3. Implementar OAuth 2.0 Authorization Code (`pinterest.com/oauth`), scopes `user_accounts:read,pins:read,boards:read` (não existe scope `analytics:read`).
4. Trial já chama endpoints reais de analytics, mas limite de 1.000 req/dia por app.
5. Pra produção multi-cliente: pedir upgrade **Standard access**, anexando vídeo do fluxo OAuth completo.
6. Acesso por cliente: (a) direto — cliente loga e autoriza o app da Miner (repete por cliente, token dura ~30d / refresh ~60d, precisa rotina de renovação); ou (b) bridge — cliente convida a Miner como Partner no Business Manager dele com papel sobre a `ad_account_id`, daí um único token da Miner cobre todos que convidaram, mas exige que o cliente tenha (ou crie) uma conta de anúncios, mesmo sem gastar.
- Não há SDK oficial único; referência: `pinterest/api-quickstart` (Python/Node) e a spec OpenAPI em `pinterest/api-description`.

## 6. YouTube Data API v3 + YouTube Analytics API — ❌ descartado (decisão do Gustavo, 24/07/2026)

APIs chegaram a ser ativadas no projeto `miner-493616`, mas o Gustavo decidiu não ter interesse em seguir (nem no YouTube, nem no Pinterest). Não criar projeto GCP novo nem retomar sem pedido explícito. Motivo técnico que ficou registrado caso reconsidere: o projeto "Miner" está com Público-alvo OAuth = Interno (só @minerbz.com.br consente), e o YouTube exige Externo (donos de canal de cliente, fora do domínio) — mudar pra Externo arriscava adicionar fila de verificação nos fluxos que já funcionam (Search Console, Google Ads), por isso a recomendação era projeto GCP dedicado, não mexer no existente.

Passo a passo original (referência, não executado):

Mesmo projeto GCP do Ads/Search Console.

1. Habilitar "YouTube Data API v3" e "YouTube Analytics API" (+ "YouTube Reporting API" opcional pra export em lote).
2. OAuth consent screen tipo External (quem consente são os clientes, fora do domínio Miner), scopes `youtube.readonly` + `yt-analytics.readonly` (sensíveis — fila de verificação de dias a poucas semanas pra sair do modo Testing).
3. Enquanto não verificado: cadastrar manualmente até 100 "test users" (emails dos clientes) pra já testar com dado real; token expira a cada 7 dias nesse modo.
4. **Importante:** o papel "Manager/Editor/Viewer" das Permissões de Canal do YouTube Studio **não** libera a API (é só pra UI). O cliente precisa logar direto no fluxo OAuth da Miner (link "conectar seu canal") ou, se o canal for Brand Account, adicionar a conta da Miner como "Owner" da Brand Account pelo fluxo clássico de gerenciamento de conta Google.
5. Sem nenhuma autorização do cliente, só dá pra puxar estatística pública básica (inscritos se não ocultos, views, nº de vídeos) via API key; retenção/watch time/demografia/receita nunca são públicos.
- Quota: 10.000 units/dia por projeto (search.list custa 100/chamada, leitura de canal custa 1) — folgado pro uso de leitura, apertado se usar busca em massa.
- Lib: `google-api-python-client` ou `googleapis/google-api-nodejs-client`.

## 7. LinkedIn Community Management API — ⏳ Development Tier solicitado (24/07/2026)

App "Miner Reporting" criado em developer.linkedin.com/apps (Client ID começa com `869op2bewxw...`), vinculado e verificado com a LinkedIn Company Page **Miner.bz** (verificação irreversível, confirmada pelo Gustavo como Page Admin). E-mail comercial `gustavo@minerbz.com.br` confirmado via código de 6 dígitos. Formulário oficial de Development Tier Access (Qualtrics, linkado a partir do botão "Access request form" que substitui "Request access" depois que a empresa é verificada) submetido 100% pelo Gustavo (a razão social exata é algo só ele tem/sabe, não estava no vault).

**Aviso importante do próprio formulário:** vai chegar um e-mail de "Microsoft Vetting Services" no e-mail comercial pra verificação adicional — Gustavo precisa ficar de olho nisso, LinkedIn pode pedir documentação extra e isso atrasa a decisão. Notificação da decisão também vem por e-mail.

**Próximos passos depois que o Development Tier for aprovado** (1-4 semanas segundo a pesquisa original): testar o fluxo OAuth 3-legged com um usuário admin de Company Page, depois pedir o upgrade pra Standard Tier (exige vídeo demo do fluxo funcionando — esse sim é o item caro, pode levar de 4 semanas a 3-4 meses, às vezes até 6, e se for rejeitado não dá pra reaplicar com o mesmo app).

Passo a passo original (referência, já em andamento):

1. Confirmar Super Admin da LinkedIn Company Page da Miner.
2. Criar app em developer.linkedin.com/apps, vincular à Page da Miner, verificar (Super Admin abre link de verificação, até 30 dias de prazo).
3. Solicitar produto **Community Management API**. Se aparecer travado, criar app novo dedicado (app com outros produtos vinculados trava o pedido).
4. Preencher **Development Tier**: e-mail comercial (não pessoal, reprova automático), razão social, site, política de privacidade, caso de uso.
5. Aprovado (1-4 semanas): já dá pra testar, mas com 500 chamadas/app/24h e 100/membro/24h.
6. Pedir upgrade **Standard Tier**: precisa de vídeo (até 5 min) mostrando o fluxo OAuth completo e as estatísticas sendo exibidas de verdade. Revisão: 4 semanas a 3-4 meses (às vezes 6). **Rejeitado não pode reaplicar com o mesmo app** — recomeça do zero.
7. Por cliente: o Super Admin da Company Page do CLIENTE precisa entrar em "Manage admins" e adicionar um funcionário da Miner com papel **Administrator** (Analyst não basta pra Follower/Page/Share Statistics). Isso não tem atalho de API — é sempre manual, do lado do cliente, por definição um pedido de confiança alto.
8. Esse funcionário da Miner faz o consentimento OAuth; a partir daí `organizationAcls` lista todas as Pages que ele administra.
- Sem SDK oficial obrigatório: REST puro + Postman collection oficial da LinkedIn.

## Gotchas gerais

- Nenhuma dessas integrações tem um passo que eu (Claude) possa completar sozinho sem o Gustavo: toda vez que aparece "login humano" na lista acima, é senha/2FA/clique de consentimento que só ele faz — eu posso navegar até ali via computer-use/browser, nunca além.
- TOS/formulário de app review em nome da Miner (TikTok, LinkedIn, Pinterest) representa a empresa perante essas plataformas: confirmar o texto antes de submeter, não só o clique.
- Guardar toda credencial resultante como secret encriptado (padrão `{enc}` do Supabase, skill [[integra]]), nunca em `.env` versionado nem em log de chat.
