---
name: deck-vivo
description: Use quando o Gustavo for atualizar, clonar ou "virar o mês" de um deck HTML da Miner com números chumbados em <span class="num">, ou disser "atualizar deck do mês", "deck vivo", "não quero redigitar número", "fecha o mês do deck", "clona o deck pra o mês novo", "compara com o mês passado", "gera o trimestral desse deck". Extrai os números batidos no HTML pra um JSON de dados por competência; a partir daí os deltas (variação vs mês/período anterior) são CALCULADOS, não digitados, e o mesmo dado gera a versão mensal e a trimestral. Dispara ao abrir/editar qualquer deck-* com valores chumbados.
---

# deck-vivo · separa o dado do esqueleto do deck

## Problema que resolve
Hoje cada deck (`~/dev/decks/deck-*`) tem os números batidos direto no HTML, tipo
`<span class="num">92.833</span>`, `<span class="num">R$1.655</span>`. Virar o mês =
clonar o HTML e redigitar dezenas de números na mão, e todo delta ("+12% vs maio") é
digitado, então erra fácil. A skill separa **dado** (JSON por competência) de
**esqueleto** (HTML). O esqueleto nunca muda; só o JSON muda por mês.

## Quando disparar
- "atualizar deck do mês", "fecha junho do Barney's", "clona pro mês novo".
- Abrir/editar um `deck-*/index.html` ou `deck-*/<mes>.html` com `<span class="num">` chumbado.
- Pedido de comparação mês a mês ou de gerar o trimestral a partir do mensal.

## Como executar
1. **Identificar o deck e as competências.** Decks em `~/dev/decks/deck-<cliente>` (barneys,
   estela, ollis, normatel, otorhinos, festival, lesalis, accs...). Cada mês costuma ser um
   arquivo (`maio.html`, `junho.html`) clonado do molde. Molde de referência: sempre o
   esqueleto do Barney's/junho (regra fixa: dados mudam, esqueleto não).
2. **Extrair os chumbados pra um JSON.** Varra o HTML pelos `<span class="num">` (e blocos
   `.metric`) e monte `dados/<competencia>.json`, ex. `dados/2026-06.json`:
   ```json
   { "competencia": "2026-06", "cliente": "barneys",
     "kpis": { "alcance": 92833, "frequencia": 1.15, "impressoes": 80570,
               "cpm": 16.55, "leads": 192, "faixa_etaria": "25-44" } }
   ```
   Chave = o que o número significa (não a posição). Guarde o número cru (sem `R$`, sem `.`
   de milhar) e formate na renderização.
3. **Deltas passam a ser calculados.** Nunca digite "+12%". O delta vs a competência anterior
   sai de `(atual - anterior) / anterior`, lido de `dados/<mes-anterior>.json`. Se não existe
   mês anterior no JSON, o deck omite o delta (não inventa base).
4. **Renderizar mensal e trimestral do MESMO dado.** O trimestral agrega as 3 competências
   (soma o que soma: leads, investido; média ponderada o que é taxa: CPM, frequência, CTR).
   Paridade obrigatória: o trimestral tem todos os slides do mensal, na mesma ordem (regra do
   relatorio-accs). Slide novo no mensal replica no trimestral.
5. **Validar antes de publicar.** Recalcular um mês já fechado a partir do JSON tem que
   reproduzir o HTML antigo. Conferir totais (soma dos meses = trimestre).
6. Deploy pelo fluxo do deck-kit / exporta-deck (Vercel CLI, `vercel --prod`).

## Gotchas
- **Milhar pt-BR:** `92.833` é 92 mil (ponto = milhar), `1,15` é decimal (vírgula). No JSON
  guarde `92833` e `1.15`; a máscara de exibição é responsabilidade do render, não do dado.
- **Slide numbers não são KPI.** Nos decks, `<span class="num">01</span>` é numeração de tela.
  Ignore os `>0\d<` de sequência; extraia só os que são métrica.
- **Números reais, não snapshot velho** (regra Normatel): a competência é explícita no JSON;
  não extrapole um mês pro outro nem reaproveite valor de outro período.
- **Ilustrativo vs real:** decks com números ilustrativos (ex. Festival) devem marcar
  `"origem": "ilustrativo"` no JSON pra não serem tratados como fechados.

## NÃO fazer
- Não redigitar número já presente no HTML: extraia.
- Não digitar delta/variação: calcule do JSON.
- Não editar o esqueleto pra "encaixar" o mês; o esqueleto é fixo, só o JSON muda.
- Não misturar clientes/competências no mesmo JSON.
