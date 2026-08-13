---
name: concorrentes
description: Extrai o retrato público de perfis concorrentes no Instagram (seguidores, cadência, mix de formatos, engajamento, posts campeões, dia e horário de publicação) e monta o benchmark contra o cliente. Três fontes em cascata: Graph API business_discovery, endpoint público e MCP Sociality.io. Use SEMPRE que o Gustavo disser "espia o concorrente", "analisa esses perfis", "benchmark do <cliente>", "compara com os concorrentes", "quanto o concorrente posta", "o que o concorrente está postando", "extrai os dados desses @", "preenche o concorrentes.json", ou passar uma lista de @ do Instagram para analisar.
---

# 🔭 Benchmark de concorrente no Instagram

Extrai o que é público de qualquer perfil e transforma em comparação útil contra o cliente. Só coleta dado público: alcance, impressões, salvamentos, stories e demografia do concorrente não existem para terceiros em fonte nenhuma, então nunca prometa isso.

## O comando

```bash
python3 ~/.claude/skills/concorrentes/scripts/espiar.py <handles...> [opções]
```

Aceita `@fulano`, `fulano` ou a URL inteira do perfil. Grava um JSON por perfil mais um `_consolidado.json` em `~/.claude/concorrentes/<data>/`, e imprime o resumo legível.

```bash
# o básico
python3 ~/.claude/skills/concorrentes/scripts/espiar.py leroymerlinbrasil obramax acalmateriais

# lendo os concorrentes já cadastrados de um cliente no motor de decks
python3 ~/.claude/skills/concorrentes/scripts/espiar.py --cliente NMTL

# lista em arquivo, mais posts, saída em outra pasta
python3 ~/.claude/skills/concorrentes/scripts/espiar.py --arquivo lista.txt --posts 30 --saida ~/Documents/benchmark
```

Opções que importam: `--posts` (quantos posts recentes analisar, padrão 25), `--fonte auto|graph|publico`, `--fuso` (padrão -3, horário de Brasília), `--pausa` (segundos entre perfis, padrão 2).

## As três fontes, e o estado real de cada uma

O script tenta na ordem e só desiste quando todas falham. O motivo de cada falha aparece no relatório, nunca um erro genérico.

**1. Graph API, `business_discovery`.** A oficial e a mais estável. **Hoje está bloqueada:** o token em `~/.meta-ads/current_token.txt` (app "Miner Ads", usuário, não expira) tem `instagram_basic` e `pages_read_engagement`, mas **não tem `instagram_manage_insights`**, e o endpoint exige as três. O erro é `(#10) Application does not have permission for this action`. Regerar o token com esse escopo destrava, e vale a pena: é a única fonte que não quebra sozinha.

**2. Endpoint público.** É o que o site do Instagram usa para montar o perfil. Não precisa de token e funciona para a maioria dos perfis. Traz cerca de 12 posts recentes. **Quebra em algumas contas business**, com a mensagem `Asset asset://laser.provider/ig_business_category_subvertical has been deleted`. Isso não é rate limit e não adianta repetir: acontece por conta, é do lado da Meta, e vem desde 30/07/2026. Confirmado hoje na `normatel.homecenter`, que continua caindo.

**3. MCP Sociality.io.** Não está no script porque é MCP, você chama direto. É a única que tem **série histórica de seguidores** e marca **post impulsionado** (`is_promoted`, com a quebra entre orgânico e pago). Plano Starter é grátis, com 1.000 créditos únicos.

```
social_competitors_list                 lista quem já está rastreado
social_competitors_create   url=...     começa a rastrear um perfil novo
social_competitor_stats_list            seguidores por dia, semana ou mês
social_competitor_posts_list            posts com curtidas, comentários, views, is_promoted
```

**Gotcha confirmado:** o campo `engagement_rate` do Sociality vem **dez vezes maior** que a taxa sobre seguidores. Medido em três posts: 1.112 interações em 46.257 seguidores dá 2,40% e o campo diz 24,1. Divida por dez, ou recalcule a partir de `engagement_count` e `followers_count`. Nunca jogue esse campo cru num slide.

Cadastrar concorrente novo consome crédito e mexe na conta do Gustavo. **Peça autorização antes de rodar `social_competitors_create`.** E lembre: a série só começa na data do cadastro, não retroage.

## Regras de leitura, para o benchmark não mentir

**Mediana antes de média.** Um viral sozinho destrói a média. No teste real, o Leroy Merlin teve mediana de 290 interações por post e média de 17.156, por causa de um único post com 202 mil. O script calcula as duas e crava um `aviso_outlier` quando a média passa de três vezes a mediana. Para comparar o dia a dia, use a mediana. A média só serve para falar de alcance de pico.

**Taxa de engajamento é sobre seguidores.** Interações divididas por seguidores. Comparar perfis de tamanhos muito diferentes pela taxa é justo; comparar por número absoluto de curtidas não é.

**Cadência é estimada pelos posts que voltaram.** Com 12 posts recentes de uma conta que posta todo dia, a janela é de duas semanas. Diga o período analisado junto do número, que o script já traz em `periodo_analisado`.

**Fuso.** Os carimbos vêm em UTC e o script converte para o fuso que você passar. O padrão é Brasília. Sem isso, "o concorrente posta às 20h" vira mentira por três horas.

**Nunca adivinhe o @.** Handle errado gera benchmark contra a conta errada, e o resultado parece perfeitamente plausível. Confirme cada perfil antes: nome, foto, bio e número de seguidores compatíveis com a marca. Se não deu para confirmar, colete assim mesmo e marque no relatório que o handle não foi verificado.

## Ligando no motor de decks

Os decks já têm o slide `s_concorrentes`, alimentado por `~/dev/decks/deck-normatel-junho/_src/concorrentes_fetch.py` a partir de `_src/concorrentes.json`. Esse arquivo está com array vazio em todos os 20 clientes desde 30/07, porque nenhum `@` foi confirmado.

Depois de validar os handles, preencha o cliente e o benchmark passa a rodar sozinho no cron das 6h30:

```json
"NMTL": ["leroymerlinbrasil", "obramax", "acalmateriais"]
```

Referências que já estavam no vault, ainda sem `@` confirmado: Barney's e Estela contra Outback, Porpino, Cabana e NBS; Normatel contra Leroy Merlin, Potiguar, Ferreira Costa, Obramax e Acal.

## O que sai no JSON

`perfil` traz seguidores, quantas contas segue, total de posts, bio, site, foto, e pela fonte pública também verificado, se é conta business e a categoria.

`posts` traz, por publicação: link, tipo (reels, carrossel, post, vídeo), data em UTC e no fuso local, legenda, curtidas, comentários, views quando houver, interações e taxa de engajamento.

`resumo` traz posts analisados, período, cadência por semana e por mês, mix de formatos, publicações por dia da semana e por hora, mediana e média de engajamento, os três posts campeões e o aviso de outlier quando existir.

## O que nenhuma fonte entrega

Alcance, impressões, salvamentos, visitas ao perfil e cliques no link do concorrente. Stories. Lista de quem segue. Demografia da audiência. Quanto ele gasta em mídia (a Meta Ad Library mostra que o anúncio existe, não o valor). Histórico anterior ao início do rastreio. E qualquer coisa de conta pessoal, privada ou com restrição de idade.

Se alguém pedir esses números, diga que não existem para terceiros em vez de estimar. Estimativa em slide de cliente vira fato na reunião seguinte.
