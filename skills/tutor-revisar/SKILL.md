---
name: tutor-revisar
description: Conduz a sessão de revisão espaçada do AI-TUTOR. Puxa os flashcards que vencem hoje, faz uma pergunta de cada vez, avalia a resposta do aluno e reagenda cada cartão pelo motor SM-2. Use quando alguém disser "revisar", "flashcards", "o que eu tenho pra revisar hoje", "me pergunta o que eu já estudei", "revisão do dia" ou "/tutor-revisar".
---

# 🔁 Revisão do dia

A revisão espaçada existe por um motivo só: relembrar pouco antes de esquecer é o que transforma conteúdo visto em conteúdo sabido. Quem revisa três minutos por dia retém mais do que quem estuda três horas no domingo.

## 1. Puxe o que vence

```bash
SLUG=$(cat ~/.claude/tutor/ativo)
python3 ~/.claude/skills/tutor/scripts/srs.py due ~/.claude/tutor/$SLUG/flashcards.json --limite 20
```

Nada vencendo hoje é uma boa notícia, não um problema. Diga isso, mostre o `stats` e siga para a aula.

## 2. Conduza

Um cartão por vez. Sempre nesta sequência:

1. Faça a pergunta da frente. **Nunca mostre o verso junto.**
2. Espere a resposta de verdade. Não responda por ela, não dê a dica antes de ela tentar, não siga em frente sozinho.
3. Mostre o verso e compare com o que ela disse.
4. Diga se acertou e, quando errou, aponte a diferença exata entre a resposta dela e a certa. Uma linha basta.
5. Registre.

A nota é sua, não dela. Julgue pela resposta, não pela confiança com que ela falou:

| Nota | Quando usar |
|---|---|
| `errei` | não lembrou, ou lembrou errado |
| `dificil` | acertou, mas titubeando, incompleto, ou depois de muito tempo |
| `bom` | acertou direito, no tempo natural |
| `facil` | respondeu na hora, sem esforço nenhum |

```bash
python3 ~/.claude/skills/tutor/scripts/srs.py revisar ~/.claude/tutor/$SLUG/flashcards.json --id c0012 --nota dificil
```

Ser generoso na nota parece gentileza e é sabotagem: o cartão volta tarde demais, a pessoa esquece, e ela vai achar que o problema é a memória dela.

## 3. Trate os teimosos

Cartão errado duas vezes ou mais não é problema de memória, é problema de entendimento. Não adianta remoer o mesmo cartão.

Quando encontrar um teimoso:

- Explique o conceito de outro jeito, ali mesmo, em duas ou três linhas.
- Se o cartão estiver ruim (cobra duas coisas, resposta longa demais, ambíguo), reescreva. Crie o cartão novo, melhor, e diga que fez isso.
- Se a lacuna for de conceito e não de memória, marque a unidade como `revisar` no `progresso.json`. O buraco volta como aula, não como cartão.

## 4. Feche

```bash
python3 ~/.claude/skills/tutor/scripts/srs.py stats ~/.claude/tutor/$SLUG/flashcards.json
```

Diga em duas linhas: quantos acertou, o que ficou firme, o que volta amanhã. Se a sessão passou de 15 minutos, pare onde está e deixe o resto para amanhã. Revisão longa demais faz a pessoa fugir da revisão.

Registre a sessão em `progresso.json`:

```json
{"data": "AAAA-MM-DD", "tipo": "revisao", "unidade": "-", "minutos": 8}
```
