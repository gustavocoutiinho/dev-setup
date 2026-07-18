---
name: prospecta-b2b
description: Use SEMPRE que o trabalho for prospecção B2B ativa, mapear ICP, achar empresas e decisores de um segmento, montar lista de prospects e enriquecer contatos. Usa o Apollo já pago (2535 lead credits + 250k AI credits parados, zero uso) em vez do ZoomInfo sem ICP. Dispara com "quem são os players de <setor>", "monta lista de prospects", "acha o decisor da <empresa>", "prospecção B2B", "mapeia o ICP", "enriquece esses contatos", "quem devo abordar em <região>". Padrão SNBR/Sinobras e Diamantes N/NE.
---

# prospecta-b2b: prospecção B2B por ICP com o que já está pago

A Miner tem Apollo com 2535 lead credits + 2500 dial + 250k AI credits parados (zero uso) e um ZoomInfo sem ICP configurado: ferramenta cara sem operação (anomalia registrada no dossiê). Esta skill vira isso em pipeline, define o ICP, mapeia empresas e decisores, enriquece e entrega lista acionável.

## Quando disparar
- Vai entrar num setor e precisa saber quem são os players e quem decide.
- Precisa de lista de prospects + contato do decisor pra abrir cadência ou proposta.
- NÃO use pra lead inbound de campanha (é [[capta-lead]]) nem pra recorte geográfico de base já existente (é [[lead-regional]]).

## Como executar
1. **Contexto primeiro.** Puxe o segmento no [[obsidianminer]]: já existe case Miner nele? Qual o ICP real (porte, região, stack)? Nunca invente empresa.
2. **Defina o ICP explícito.** Padrão SNBR/Sinobras (frente de aço do onboarding ACCS): mapear ICP, cruzar com quem já converte, analisar histórico de campanhas antes de listar frio. Sem ICP escrito, não gasta crédito.
3. **Use o que está pago.** Apollo é a ferramenta canônica (MCP conectado; stack manda consolidar em Apollo + Clay + Windsor). ZoomInfo está marcado pra desativar (duplica Apollo, B2B brasileiro fraco), não abra operação nova nele.
4. **Enriqueça com parcimônia.** Só os campos necessários (nome, cargo, empresa, canal). Data minimization, não faça extração em massa pra "montar base".
5. **Entregue acionável.** Lista com decisor, gancho e próximo passo, pronta pra virar cadência ou [[proposta-nova]]. Recorte regional (N/NE, DDD, cidades) puxa [[lead-regional]].

## Gotchas
- Apollo e ZoomInfo consomem crédito por chamada, não "teste à toa" (regra do vault). ICP primeiro, busca depois.
- Diamantes (50+ lojas N/NE, modelo revendedora) mostra que o "decisor" às vezes é a rede de revendedoras, não só a matriz: ajuste o ICP ao modelo de canal.
- Prospecção sem operação atrás vira desperdício: se não há cadência nem proposta, PARE e registre no [[radar-bloqueios]].

## O que NÃO fazer
- NÃO fazer scraping ou extração em massa (proibido pelos ToS e sem base legal).
- NÃO abrir operação nova no ZoomInfo, o stack manda consolidar no Apollo.
- NÃO entregar lista crua sem ICP, gancho e decisor.
- NÃO inventar empresa ou contato que a ferramenta não retornou.
