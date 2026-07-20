---
name: prospeccao
description: Use SEMPRE que o trabalho for ganhar cliente novo: montar proposta comercial pra prospect (regra: "empresa do setor", sem nome de cliente) ou prospecção B2B ativa (ICP, achar empresas/decisores, enriquecer via Apollo já pago). Dispara com "monta a proposta do <prospect>", "proposta comercial nova", "quem são os players de <setor>", "monta lista de prospects", "acha o decisor", "mapeia o ICP", "enriquece esses contatos".
---

# prospeccao: ganhar cliente novo, da proposta ao pipeline B2B

Toda frente de novo cliente na Miner passa por aqui: ou você monta a proposta comercial que fecha o prospect, ou prospecta ativo (define ICP, acha empresas e decisores, enriquece). Sem trilho, cada proposta sai diferente e alguém esquece a regra de ouro (nome de cliente nunca entra no documento), e a prospecção queima crédito sem ICP. Esta skill cobre os dois modos.

## Modos
- **proposta comercial**: monta a proposta pra prospect ou nova frente, no KV, sem nome de cliente no papel.
- **prospecção B2B**: define ICP, mapeia players e decisores de um setor, enriquece contatos com o que já está pago (Apollo).

## Quando disparar
- "monta a proposta do <prospect>", "proposta comercial nova", "estrutura o investimento", prospect em qualificação quer detalhe de como a Miner operaria.
- "quem são os players de <setor>", "monta lista de prospects", "acha o decisor", "mapeia o ICP", "enriquece esses contatos".
- NÃO use pra relatório mensal de cliente ativo (é [[relatorio]]), nem pra lead inbound de campanha ou recorte de base existente (é [[crm]]).

## Como executar
**Comum:** puxe o contexto no [[obsidianminer]] (segmento, decisor, diagnóstico, histórico, case Miner no setor). Nunca invente número nem empresa. Se falta credencial ou decisão, PARE e registre no [[monitor]].

**Modo proposta comercial**
1. Siga a SOP `docs/sop/SOP Proposta Comercial Nova.md`: qualificação, diagnóstico rápido, 10 blocos (por que agora, o que entregamos, o que NÃO fazemos, como operamos, quem opera, cronograma, KPIs-âncora, investimento, o que pedimos, risco de não fazer). Base o texto em `templates/proposta-comercial.md`.
2. **REGRA DE OURO:** nenhum nome de cliente atual/passado nem ex-empregador (Romanel) no documento. Sempre genérico ("uma grande empresa nacional do setor", "case Miner em moda feminina"). Números de case sem a marca; nomes só em conversa.
3. **Pricing estilo Gustavo:** nunca valor cheio/total nem "condição de pacote". Cada etapa tem preço próprio (metáfora de OBRA: Fundação obrigatória, Estrutura, Instalações, Fachada, Expansão). Ferramentas = 33% sobre o módulo. Setup + mensal; a Miner não é a opção barata.
4. Trabalha em `*-proposta.html` / `*-apresentacao-slides.html` em `~/Documents/Claude`, deploy `*-proposta.vercel.app`. Minerize via [[minerdesign]] (slides 16:9), confira slide a slide no preview, exporte PDF com Chrome headless. Auditoria como porta de entrada é frente própria ([[metodo]]).

**Modo prospecção B2B**
1. **Defina o ICP explícito** (porte, região, stack) antes de gastar crédito. Padrão SNBR/Sinobras (frente de aço do onboarding ACCS): cruze com quem já converte e o histórico de campanhas.
2. **Use o que está pago:** Apollo é canônico (MCP conectado; 2535 lead credits + 2500 dial + 250k AI credits parados, zero uso). ZoomInfo está marcado pra desativar (duplica Apollo, B2B brasileiro fraco), não abra operação nova nele.
3. **Enriqueça com parcimônia** (só nome, cargo, empresa, canal): data minimization, sem extração em massa.
4. **Entregue acionável:** lista com decisor, gancho e próximo passo, pronta pra virar cadência ou a proposta acima.

## Gotchas
- Diagnóstico antes da proposta: sem ele o cliente não vê valor (anti-padrão da SOP).
- Estouro de altura em slide 16:9 é o defeito mais comum ao minerizar.
- Diamantes (50+ lojas N/NE, modelo revendedora) mostra que o "decisor" às vezes é a rede, não a matriz: ajuste o ICP ao modelo de canal. E o combinado com Diamantes é seleção agnóstica de CRM, a Miner não desenvolve CRM próprio pra ele.
- Apollo/ZoomInfo consomem crédito por chamada: ICP primeiro, busca depois. Prospecção sem cadência nem proposta atrás vira desperdício, PARE e registre no [[monitor]].

## O que NÃO fazer
- NÃO citar nome de cliente ou case no documento que circula, nem mostrar valor total/pacote fechado.
- NÃO enviar a proposta pelo Gustavo: entrega o arquivo/PDF, quem manda é ele.
- NÃO fazer scraping nem abrir operação nova no ZoomInfo (o stack manda consolidar no Apollo).
- NÃO entregar lista crua sem ICP, gancho e decisor; NÃO inventar empresa/contato que a ferramenta não retornou.
