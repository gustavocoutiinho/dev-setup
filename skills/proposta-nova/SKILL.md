---
name: proposta-nova
description: Use SEMPRE que o Gustavo for montar uma proposta comercial nova pra prospect ou nova frente de cliente, não relatório nem deck de cliente ativo. Trabalha em arquivos *-proposta.html ou *-apresentacao-slides.html em ~/Documents/Claude com deploy *-proposta.vercel.app, seguindo a SOP Proposta Comercial Nova do vault. Dispara com "monta a proposta do <prospect>", "proposta comercial nova", "faz a proposta pra <empresa>", "estrutura o investimento do <cliente>", "prospect X quer proposta". Casos vivos Sabor & Vida, Diamantes, Inox/Sinobras.
---

# proposta-nova: proposta comercial Miner do primeiro contato ao PDF

A Miner fecha proposta o tempo todo (Sabor & Vida, Diamantes, ACCS, Otorhinos). Sem trilho, cada uma sai diferente e alguém esquece a regra de ouro: nome de cliente NUNCA entra no documento. Esta skill monta a proposta seguindo a SOP do vault e a estiliza no KV.

## Quando disparar
- Prospect em qualificação pede detalhe de como a Miner operaria, ou cliente ativo abre nova frente.
- Vai criar ou editar `*-proposta.html` / `*-apresentacao-slides.html` em `~/Documents/Claude`, deploy `*-proposta.vercel.app`.
- NÃO use pra relatório mensal (é [[relatorio-vivo]]) nem deck de cliente ativo sobre a operação dele.

## Como executar
1. **Contexto primeiro.** Puxe o prospect no [[obsidianminer]] (segmento, decisor, diagnóstico, histórico). Nunca invente número.
2. **Siga a SOP.** `docs/sop/SOP Proposta Comercial Nova.md`: qualificação, diagnóstico rápido, estruturação (10 blocos, por que agora, o que entregamos, o que NÃO fazemos, como operamos, quem opera, cronograma, KPIs-âncora, investimento, o que pedimos, risco de não fazer), apresentação, fechamento. Base o texto em `templates/proposta-comercial.md`.
3. **REGRA DE OURO.** Nenhum nome de cliente atual ou passado nem ex-empregador (Romanel) no documento. Sempre genérico ("uma grande empresa nacional do setor", "case Miner em moda feminina"). Números de case entram sem a marca; nomes só em conversa.
4. **Pricing estilo Gustavo.** Nunca mostre valor cheio/total nem "condição especial de pacote". Cada etapa tem preço próprio (metáfora de OBRA, Fundação obrigatória, Estrutura, Instalações, Fachada, Expansão). Ferramentas = 33% sobre o módulo. Setup + mensal; a Miner não é a opção barata.
5. **Minerize e gere PDF.** Estilize via [[minerdesign]] (slides 16:9 KV, fontes/ícones/imagens embutidos), confira slide a slide no preview, exporte PDF com Chrome headless.

## Gotchas
- Diagnóstico antes da proposta: sem ele o cliente não vê valor (anti-padrão da SOP).
- Auditoria como porta de entrada é frente própria, veja [[metodo-auditoria]].
- Estouro de altura em slide 16:9 é o defeito mais comum ao minerizar.

## O que NÃO fazer
- NÃO citar nome de cliente ou case no documento que circula.
- NÃO apresentar valor total nem condição de pacote fechado.
- NÃO enviar a proposta pelo Gustavo, entrega o arquivo/PDF e quem manda é ele.
- NÃO prometer que a Miner desenvolve CRM próprio pro cliente quando o combinado é seleção agnóstica (caso Diamantes).
