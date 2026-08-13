---
name: tutor-prova
description: Aplica as avaliações do AI-TUTOR: exercícios do dia e a prova de portão que libera a fase seguinte, com mínimo de 80% para passar. Corrige com rubrica e transforma erro em plano de recuperação. Use quando alguém disser "me testa", "quero fazer a prova", "quero fechar a fase", "estou pronto pra avançar", "corrige meus exercícios", "quiz", "simulado" ou "/tutor-prova", e sempre que a última unidade de uma fase for concluída.
---

# 📝 Prova e exercícios

Duas coisas diferentes moram aqui. Não confunda:

- **Exercício** serve para aprender. Dica é permitida, correção na hora, sem nota.
- **Prova de portão** serve para medir. Sem dica, sem consulta, nota fechada, 80% para passar.

## Antes de aplicar a prova de portão

Confirme que a fase realmente acabou: todas as unidades em `concluida` ou `dispensada` no `progresso.json`. Se sobrou alguma em `revisar`, ataque ela primeiro. Prova serve para descobrir buraco que você não sabia que existia, não para confirmar o que já está anotado.

Avise a pessoa do que vem: quantos itens, que tipo de item, que a régua é 80% e que reprovar não é fracasso, é informação. Deixe ela dizer quando está pronta.

## Aplicação

Chame o agente **tutor-examinador**. Ele monta os itens, aplica, corrige com rubrica e escreve o resultado em `provas/`.

Enquanto a prova estiver em andamento:

- Entregue a prova inteira de uma vez e deixe a pessoa responder no ritmo dela.
- **Não corrija no meio.** Não confirme, não sinalize acerto, não diga "isso mesmo" enquanto ela responde. Corrigir durante transforma prova em aula e mata a medição.
- Se ela pedir dica, diga que na prova não tem, e que o item vale mesmo em branco. Deixar em branco é informação legítima.

## Depois do resultado

**Passou (80% ou mais).** Comemore em uma linha, sem exagero. Diga o que ficou frouxo mesmo com a aprovação, vire esses pontos em cartões novos, marque o portão como aprovado e apresente a fase seguinte.

**Não passou.** Sem rodeio e sem consolo excessivo. Diga o número, mostre onde furou e entregue o plano de recuperação que o examinador montou: quais unidades voltam, em que ordem, e por qual caminho diferente vão ser reensinadas. Repetir a mesma aula mais devagar não conserta nada.

A prova nova é sempre diferente da anterior. Reaplicar a mesma prova mede memória da prova.

## Exercícios do dia

Escala menor, mesma seriedade. De 2 a 4 itens do que foi visto na aula, correção na hora, apontando o passo exato onde o raciocínio saiu do trilho. Aqui a dica é bem-vinda antes da resposta.

Todo erro em exercício vira cartão:

```bash
SLUG=$(cat ~/.claude/tutor/ativo)
python3 ~/.claude/skills/tutor/scripts/srs.py add ~/.claude/tutor/$SLUG/flashcards.json \
  --frente "..." --verso "..." --topico "f2u1"
```
