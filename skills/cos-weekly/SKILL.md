---
name: cos-weekly
description: Use quando o Gustavo for preparar ou processar a weekly do time (o sync geral de ~15 min, não o deep-dive de projeto). Dispara com "prepara a weekly", "monta a pauta da weekly", "processa a weekly", "o que mudou na semana", "consolida a semana do time", "pauta do sync semanal", ou ao fechar a semana e precisar do retrato do que mudou por cliente e por direto.
---

# cos-weekly: preparar e processar a weekly do time

A weekly é um sync geral de time (~15 min): pulso da equipe, alertas transversais, 1-2 decisões que precisam de todos. Não é deep-dive de projeto (isso mora nas weeklies por projeto). Esta skill consolida o que mudou na semana cruzando fontes e processa a saída em ata + tasks.

## Quando disparar
- "prepara/processa a weekly", "o que mudou na semana", "consolida a semana do time".
- Ao fechar a semana e precisar do retrato do que mudou por cliente/direto.

## Como executar
1. **Contexto.** Última weekly em `weeklys/` (`weeklys/2026-Wxx.md`), perfis dos 8 diretos em `team/`, decisões em aberto.
2. **Cruze o que mudou** via [[cruzar-dados]] (Asana tasks por owner, Meta Ads, WhatsApp) num retrato consolidado. Regra de ouro: ferramenta que não respondeu vira "sem dados hoje", nunca número inventado.
3. **Escopo (15 min).** Saúde do time, status de 1-2 frases por direto, alertas transversais (overdue, queda de engajamento, estagnação), reconhecimentos, 1-2 decisões do time todo. Fora: task list por projeto e deep-dive técnico.
4. **Molde e método.** Consistência do `docs/sop/SOP Relatorio Semanal Padrao.md` e `templates/weekly.md`. Diagnóstico, hipótese, recomendação, próximo passo.
5. **Processe.** Registre em `weeklys/YYYY-Wxx.md`, crie tasks Asana dos action items (workspace `1201866314544289`), decisões grandes vão pro Decision Log.

## Gotchas
- Tema que passa de 3 min não expande a weekly: marque "precisa reunião dedicada".
- `SOP Relatorio Semanal Padrao` é o relatório de CLIENTE (sexta 16h, robô Sprint 1), não confundir com a weekly interna do time.
- Direto sem sinal na semana (silêncio incomum) é sinal, não ausência de pauta.

## O que NÃO fazer
- Não virar update cliente por cliente (vira reunião de 3 horas).
- Não reportar métrica de ferramenta que não respondeu.
- Não fechar sem ata: decisão por escrito ou não aconteceu.
