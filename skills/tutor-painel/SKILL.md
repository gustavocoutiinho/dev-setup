---
name: tutor-painel
description: Mostra o progresso do aluno no AI-TUTOR. Gera o painel.html visual com a árvore de habilidades, as barras por fase, a ofensiva de dias estudados e o estado da memória, e lê esse retrato em voz alta, dizendo o que está firme, o que está travado e o que fazer em seguida. Use quando alguém disser "como estou indo", "meu progresso", "painel", "quanto falta", "árvore de habilidades", "resumo do curso" ou "/tutor-painel".
---

# 📊 Painel de progresso

## 1. Gere

```bash
SLUG=$(cat ~/.claude/tutor/ativo)
python3 ~/.claude/skills/tutor/scripts/painel.py ~/.claude/tutor/$SLUG --abrir
```

O painel é um arquivo local, autocontido, que abre no navegador. Fica em `~/.claude/tutor/<slug>/painel.html` e é regravado a cada geração.

## 2. Leia o painel para a pessoa

O número sozinho não ensina nada. Depois de abrir, diga em no máximo cinco linhas:

- **Onde ela está**: fase, percentual, o que já consegue fazer que não conseguia no começo. Sempre em termos de capacidade, não de conteúdo coberto.
- **A ofensiva**: dias seguidos de estudo. Se quebrou, sem sermão. Constância se recupera estudando hoje, não se justificando.
- **O que está travado**: unidades em `revisar` e os cartões teimosos. Esse é o item mais útil do painel inteiro.
- **A memória**: quantos cartões já estão firmes e quantos vencem hoje.
- **O próximo passo concreto**: a unidade da próxima sessão, ou o portão que está esperando.

## 3. Diga a verdade sobre o ritmo

Se o currículo tem 30 unidades, a pessoa fez 4 em três semanas e o prazo dela é dois meses, a conta não fecha. Diga o número e ofereça a saída: aumentar o tempo diário, cortar fase para uma versão essencial, ou esticar o prazo. Deixar a pessoa descobrir isso sozinha na última semana é o pior desfecho possível.

O contrário também vale. Se ela está indo mais rápido do que o currículo previa, o curriculista pode adensar as fases seguintes em vez de deixá-la em marcha lenta.

## Quando o painel estiver quase vazio

Nos primeiros dias, não force um relatório de nada. Diga onde o curso começa, o que a primeira fase destrava, e vá dar aula.
