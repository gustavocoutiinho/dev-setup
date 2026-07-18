---
name: cos-1on1
description: Use SEMPRE que o Gustavo for preparar (ou processar depois) uma 1:1 com um dos 8 diretos (Caio, Davi, Rafael, Raquel, Cecilia, Ricardo, ygor, Helia), a cadência mensal individual. Dispara com "prepara minha 1:1 com o <nome>", "me ajuda com a individual do <nome>", "o que levar pra 1:1 do <fulano>", "processa o áudio da 1:1", "monta a pauta da individual", e antes de qualquer conversa de desenvolvimento ou feedback com um direto.
---

# cos-1on1: preparar a 1:1 do direto com pauta e sinais

A 1:1 é a cadência mensal individual com cada direto. É sobre a pessoa (desenvolvimento, escopo, carga, próximos 30 dias), não update operacional cliente por cliente. Sem preparo, vira conversa solta e compromisso do Gustavo se perde. Esta skill monta o briefing e, depois, processa o áudio em ata + tasks.

## Quando disparar
- "prepara minha 1:1 com o <nome>", "processa o áudio da 1:1 do <fulano>".
- Antes de conversa de desenvolvimento, feedback ou tema sensível com um direto.
- Foco é pessoa. Task-level e bypass de projeto são a weekly de projeto, não aqui.

## Como executar
1. **Contexto primeiro.** Puxe [[obsidianminer]] + `team/<slug>/` (perfil, dev-plan, última 1:1 em `team/<slug>/meetings/`). Slugs: caio-amorim, davi-ribeiro, rafael-castro, raquel-nunes, cecilia-maia, ricardo, ygor-paiva, helia. Nunca invente.
2. **Objetivo antes do dado.** Pergunte o foco (acompanhar entregas / desenvolvimento / tema sensível / check-in). O dado serve à intenção, não o contrário.
3. **Colete.** Tasks Asana do direto (workspace `1201866314544289`, mapping cliente→owner em `context/cos-config.md`), pendências da última 1:1, sinais de engajamento.
4. **Recorrência.** Action item que aparece em 3+ 1:1s seguidas leva flag ⚠️ RECORRENTE com abordagem sugerida.
5. **Briefing em blocos** (molde `templates/1on1-individual-mensal.md`): Pendências (status real + compromissos meus não cumpridos), Pauta, Provocações, Coaching de abordagem. Diagnóstico, hipótese, recomendação, próximo passo.
6. **Salve** em `team/<slug>/meetings/YYYY-MM-DD/`. Sinal de carga vai pro [[cos-capacity]]; decisão grande vai pro Decision Log.

## Gotchas
- Compromisso meu não cumprido é sagrado: sempre no bloco Pendências, sem suavizar.
- Score de engajamento só com evidência da conversa, N/A quando não há. Nunca fabricar.
- 1:1 muito recente (<7 dias): briefing leve, foco no "algo mudou desde a última?".

## O que NÃO fazer
- Não montar o briefing antes de saber o foco do Gustavo.
- Não despejar lista de tasks de cliente (isso é [[cos-weekly]] ou weekly de projeto).
- Não deixar a 1:1 sem ata: verbal não conta, decisão por escrito ou não aconteceu.
