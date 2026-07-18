---
name: cos-capacity
description: Use quando o Gustavo quiser o snapshot de carga do time (os 8 diretos), ver quem está sobrecarregado, ou antes de delegar/redistribuir cliente. Dispara com "como tá a carga do time", "quem tá sobrecarregado", "capacity do time", "quantos projetos o <fulano> carrega", "posso colocar mais um cliente no <nome>", "snapshot de capacity". Caio carrega ~70% do volume, isso é o risco estrutural.
---

# cos-capacity: snapshot de carga dos 8 diretos

Capacity Map dos 8 diretos. Hoje Caio carrega ~24 projetos Asana (~70% do volume), concentração que é o risco estrutural conhecido. Esta skill dá o retrato de carga real antes de delegar e captura sinal de saturação antes de virar incidente.

## Quando disparar
- "como tá a carga do time", "quem tá sobrecarregado", "posso colocar mais um cliente no <nome>".
- Antes de delegar ou redistribuir cliente; ao ver sinal de saturação de um direto.

## Como executar
1. **Contexto.** `projects/Capacity Map Diretos Miner.md` (retrato atual) + perfis em `team/<slug>/`.
2. **Volume real por owner.** `get_projects` do Time Miner (gid `1206315371746083`, workspace `1201866314544289`), conte projetos ativos por owner via mapping cliente→owner (`context/cos-config.md`). Não estime de cabeça.
3. **Sinais de sobrecarga:** nº de projetos, tasks vencidas, reuniões/semana, cliente que puxa energia (dos 1:1s, [[cos-1on1]]).
4. **Diagnóstico, hipótese, recomendação:** quem está no limite, o que redistribuir, pra quem (quem tem folga real). Reduzir presença operacional direta nos top é meta de 90 dias.
5. **Registre.** Atualize o Capacity Map. Decisão de redistribuição vai pro Decision Log e vira pauta da [[cos-cerimonia]].

## Gotchas
- Caio ~70% do volume é o risco a monitorar em toda leitura de capacity.
- O número vem do Asana vivo (`get_projects`), não do snapshot velho do Capacity Map: sempre reconferir a contagem.
- Conte quem é owner que entrega, não quem só acompanha (Read-Only não é carga real).

## O que NÃO fazer
- Não redistribuir sem ver a folga real do destino (não empurrar do sobrecarregado pro quase-sobrecarregado).
- Não afirmar carga de ninguém sem puxar o número do Asana.
- Não deixar decisão de redistribuição só falada: registre.
