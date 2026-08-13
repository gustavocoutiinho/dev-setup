---
name: tutor-aula
description: Dá a aula do dia do AI-TUTOR. Escolhe a unidade certa do currículo, aquece com o que vence na revisão e conduz o ensino com participação ativa do aluno, fechando com flashcards e exercícios. Use quando alguém disser "vamos estudar", "próxima aula", "continua de onde paramos", "me ensina X", "não entendi isso", "explica de novo", "aula de hoje" ou "/tutor-aula", dentro de um curso já montado pelo AI-TUTOR.
---

# 📚 Aula do dia

## 1. Descubra onde a pessoa está

```bash
SLUG=$(cat ~/.claude/tutor/ativo)
cat ~/.claude/tutor/$SLUG/perfil.md
python3 ~/.claude/skills/tutor/scripts/srs.py stats ~/.claude/tutor/$SLUG/flashcards.json
```

Leia também `curso.md`, `progresso.json` e as duas últimas aulas em `aulas/`.

## 2. Escolha a unidade

Nesta ordem de prioridade:

1. Unidade marcada como `revisar`. Buraco aberto vem antes de conteúdo novo, sempre.
2. Unidade `em_curso`, se a última sessão ficou pela metade.
3. Primeira unidade `pendente` da fase corrente.
4. Se todas as unidades da fase estão fechadas, não comece a fase seguinte: é hora do portão. Chame `tutor-prova`.

Se o aluno pedir um assunto específico, ensine esse assunto, mesmo fora de ordem. Depois avise em uma linha onde ele encaixa no currículo e volte à trilha na próxima sessão.

## 3. Aqueça (2 a 3 minutos)

```bash
python3 ~/.claude/skills/tutor/scripts/srs.py due ~/.claude/tutor/$SLUG/flashcards.json --limite 5
```

Faça de 2 a 3 dessas perguntas de viva-voz, corrija na hora e registre cada resposta:

```bash
python3 ~/.claude/skills/tutor/scripts/srs.py revisar ~/.claude/tutor/$SLUG/flashcards.json --id c0007 --nota bom
```

Se a revisão de hoje for grande (mais de 12 cartões vencendo), não empurre para dentro da aula: faça a sessão de revisão inteira antes, com `tutor-revisar`.

## 4. Dê a aula

Chame o agente **tutor-professor**. Passe para ele: a unidade escolhida, o tempo disponível hoje, o que a pessoa errou no aquecimento e o que os registros anteriores dizem sobre como ela aprende.

O professor conduz a aula toda, com o aluno participando de metade dela, e no fim grava o registro em `aulas/`, cria de 3 a 8 flashcards, deixa de 2 a 4 exercícios e atualiza o `progresso.json`.

## 5. Feche a sessão

Em três linhas, no máximo:

- o que a pessoa passou a conseguir fazer hoje
- o que ficou de exercício
- o que vem na próxima sessão

Se o tempo declarado no perfil acabou e o conteúdo não fechou, pare mesmo assim. Marque a unidade como `em_curso` e continue amanhã. Aula que estoura o tempo combinado é a razão número um de a pessoa parar de aparecer.
