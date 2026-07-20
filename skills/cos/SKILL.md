---
name: cos
description: Use SEMPRE que o trabalho for cadência/gestão de time da Miner (Chief of Staff): preparar/processar 1:1 com um direto, a weekly, a pauta da Cerimônia de segunda 9h, virar transcrição de reunião em action items/tasks no Asana, snapshot de capacity do time, a retrospectiva do mês, ou formalizar um direto novo. Dispara com 'prepara minha 1:1 com o <nome>', 'monta a weekly', 'pauta da cerimônia', 'processa essa reunião', 'como tá a carga do time', 'quem tá sobrecarregado', 'fecha a retro do mês', 'entrou gente nova no time'.
---

# cos: cadência e gestão de time da Miner (Chief of Staff)

A família cobre todo o ritmo de gestão dos 8 diretos: preparar e processar 1:1, weekly, Cerimônia de segunda, virar reunião em tasks, ler capacity, fechar a retro do mês e formalizar quem entra. Sem trilho, conversa vira anotação parada e compromisso do Gustavo se perde. Tudo mora no vault `~/ObsidianVaults/miner`, roda no método diagnóstico → hipótese → recomendação → próximo passo, e fecha com ata (decisão por escrito ou não aconteceu).

## Modos
- **1:1** (`team/<slug>/meetings/`): cadência mensal individual, sobre a pessoa (desenvolvimento, escopo, carga), não status de cliente.
- **weekly** (`weeklys/2026-Wxx.md`): sync geral ~15 min, pulso do time + 1-2 decisões transversais.
- **cerimônia** (`docs/sop/SOP Cerimonia Miner.md`): segunda 9h BRT, 60 min, 9 core (8 diretos + Gustavo), ritmo de empresa.
- **reunião→Asana**: transcrição/áudio vira decisões + action items + tasks com assignee certo (Granola Router).
- **capacity** (`projects/Capacity Map Diretos Miner.md`): snapshot de carga real dos 8 diretos antes de delegar.
- **retro** (`weeklys/YYYY-MM Retrospectiva Mensal.md`): último dia útil, números + executado vs planejado + lições.
- **onboarding de direto** (`team/<Nome>.md`): formaliza pessoa nova pra não virar zona cinza.

## Quando disparar
- "prepara minha 1:1 com o <nome>", "processa o áudio da 1:1"; antes de feedback ou tema sensível com um direto.
- "monta/processa a weekly", "o que mudou na semana", "consolida a semana do time".
- "pauta da cerimônia", "pauta da segunda 9h", "prepara a cerimônia".
- "processa essa reunião", "tira os action items", "cria as tasks da reunião do <cliente>".
- "como tá a carga do time", "quem tá sobrecarregado", "posso pôr mais um cliente no <nome>".
- "fecha a retro do mês", "retro mensal", "o que rolou esse mês".
- "entrou gente nova", "formaliza o <nome>", "onboarding do <nome>", "novo direto começa segunda".

## Como executar
**Comum a todos os modos:**
1. **Contexto primeiro.** Puxe [[obsidianminer]] + `team/<slug>/` (perfil, dev-plan, últimas atas). Slugs: caio-amorim, davi-ribeiro, rafael-castro, raquel-nunes, cecilia-maia, ricardo, ygor-paiva, helia. Nunca invente.
2. **Número vem do vivo.** Contagem e métrica saem do Asana (workspace `1201866314544289`, Time Miner `1206315371746083`) cruzados via [[cruzar-dados]]; ferramenta que não respondeu = "sem dados hoje", nunca número inventado.
3. **Fecha com registro.** Ata/registro no vault, tasks Asana pelo mapping cliente→owner (`context/cos-config.md`; ex: NMTL→Caio, PRLS→Gustavo, TRFT→Rafael, GRBS→ygor), decisão grande no Decision Log, sinal de carga alimenta o modo capacity.

**O que muda por modo:**
- **1:1:** molde `templates/1on1-individual-mensal.md`. Pergunte o foco antes do dado. Action item em 3+ 1:1s seguidas leva flag ⚠️ RECORRENTE. Compromisso do Gustavo não cumprido é sagrado, sempre no bloco Pendências. Salva em `team/<slug>/meetings/YYYY-MM-DD/`.
- **weekly:** consolida o que mudou por cliente/direto (`templates/weekly.md`). Tema que passa de 3 min vira "reunião dedicada", não expande a weekly.
- **cerimônia:** pauta enxuta 3-4 itens (abertura, ronda, decisão transversal, próximos 7 dias). Ronda: Caio, Rafael, Davi, ygor, Cecilia, Ricardo, Raquel, Helia. Item de owner escala pro owner, não vira pedido ao Gustavo. Ata em 24h.
- **reunião→Asana:** Playbook "Granola Router" (Notion `36e12a5d-1b46-81b2-b1d1-e36766ee01fc`). 2+ projetos sem dominante = standalone. Cada action item com dono e prazo confirmado; "Source: Reunião <projeto> YYYY-MM-DD" na descrição da task.
- **capacity:** conte projetos ativos por owner com `get_projects` do Time Miner, não do snapshot velho. Caio ~24 projetos (~70% do volume) é o risco estrutural. Só quem entrega (Read-Only não é carga).
- **retro:** métrica-âncora precisa de início E fim reais do mês (Normatel: números do Histórico, mês explícito, nunca extrapolar snapshot). Compare com o plano do mês anterior; saída vira pauta da 1ª cerimônia do mês seguinte.
- **onboarding:** 5 marcas = user no Asana (não convidado) + nota `team/<Nome>.md` + e-mail @minerbz.com.br + Cerimônia no Calendar + acessos por cliente. Escopo escrito em 2 semanas.

## Gotchas
- **OAuth Granola PENDENTE:** a edge `meeting-router` só sobe quando o OAuth conectar; até lá reunião→Asana é 100% manual. Cobre em [[monitor]].
- Zona cinza é o inimigo (Helia e Yasmim ficaram fora do Asana e viraram ambiguidade): ou formaliza pleno, ou marca "parceira externa", nunca no limbo.
- `SOP Relatorio Semanal Padrao` é o relatório de CLIENTE (sexta 16h, [[relatorio]]), não a weekly interna: não confundir.
- Capacity sai do Asana vivo, nunca do Capacity Map velho. Caio ~70% em toda leitura.
- Score de engajamento só com evidência da conversa; N/A quando não há.

## O que NÃO fazer
- NÃO virar update cliente por cliente (weekly e cerimônia viram reunião de 3h).
- NÃO reportar métrica de ferramenta que não respondeu, nem inventar "~X tasks".
- NÃO criar task sem assignee e sem prazo; NÃO usar gmail pra identidade Miner.
- NÃO fechar nada sem ata: decisão por escrito ou não aconteceu.
