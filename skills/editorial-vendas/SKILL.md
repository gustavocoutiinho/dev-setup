---
name: editorial-vendas
description: Use quando o trabalho for montar ou atualizar a linha editorial de um cliente com foco em VENDAS e não em alcance, pautas que puxam pipeline calibradas pelos deals e comportamento reais. Vem da task MGTC "Compartilhar Linha Editorial Focada Em Vendas" (Mig-Tech) e análogas, HubSpot deals + GA4 viram drafts no Asana. Dispara com "linha editorial do <cliente>", "pauta que vende", "conteúdo focado em vendas", "o que postar pra gerar deal", "calendário editorial de vendas".
---

# editorial-vendas: linha editorial puxada por deal, não por alcance

Conteúdo bonito que não move pipeline é vaidade. Esta skill monta a linha editorial de um cliente a partir do que vende de verdade: cruza deals do HubSpot com comportamento no GA4, vira prompt de IA e sai como drafts prontos no Asana. Origem: automação "Linha editorial MGTC" (Mig-Tech, SaaS B2B), task "Compartilhar Linha Editorial Focada Em Vendas".

## Quando disparar
- Cliente precisa de pauta ou calendário editorial amarrado a vendas, não a curtidas.
- Já existe HubSpot com deals e GA4 do cliente pra ler o que converte.
- NÃO use pra SEO de e-commerce e descrição de produto (é [[seo-blog]]) nem pra definir o tom da marca (é [[marca-manual]], que alimenta esta).

## Como executar
1. **Contexto primeiro.** Puxe o cliente no [[obsidianminer]] e o tom em [[marca-manual]]. MGTC = Mig-Tech (HubSpot conta 46374576, GA4 MigTech, lead Caio).
2. **Leia o que vende.** HubSpot: quais deals fecham, por qual estágio, com qual objeção. GA4: quais páginas e conteúdos precedem a conversão. O sinal de pauta vem daí, não de achismo.
3. **Prompt de IA.** Transforme o dump (deals + GA4) num prompt via IA da Miner (ai-json), no tom do [[marca-manual]]. Peça pautas por etapa de funil (topo, meio, fundo) com ângulo de venda.
4. **Drafts no Asana.** Gere os rascunhos de conteúdo como tasks no projeto do cliente (padrão da automação), prontos pra revisão humana antes de publicar.
5. **Feche o loop.** Marque quais pautas viraram deal pra recalibrar o próximo ciclo.

## Gotchas
- Foco em vendas não é só fundo de funil: sem topo, o pipeline seca. Distribua por etapa.
- HubSpot precisa de OAuth conectado antes de ler deals, se cair registre no [[radar-bloqueios]].
- Draft de IA é rascunho, não publicação: revisão humana obrigatória.

## O que NÃO fazer
- NÃO medir sucesso por alcance ou engajamento quando o pedido é vendas.
- NÃO publicar direto, entrega draft no Asana e quem aprova ou posta é o time/cliente.
- NÃO inventar tema sem lastro nos deals e no GA4.
- NÃO rodar IA por chave solta, passa por ai-json.
