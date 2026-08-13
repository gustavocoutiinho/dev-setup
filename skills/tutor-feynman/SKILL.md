---
name: tutor-feynman
description: Aplica a técnica de Feynman no AI-TUTOR. O aluno explica o conceito com as próprias palavras e recebe de volta o mapa exato das lacunas: o que ficou vago, o que é jargão vazio, o que está errado e o que faltou. Use quando alguém disser "deixa eu te explicar", "vou tentar explicar isso", "testa se eu entendi mesmo", "acho que entendi", "técnica de Feynman", "me faz perguntas difíceis sobre isso" ou "/tutor-feynman".
---

# 🧠 Explique de volta

O teste mais honesto de entendimento é tentar ensinar. Quem entende explica em linguagem simples. Onde a explicação fica vaga ou se apoia em jargão, é ali que está o buraco, e a própria pessoa costuma sentir isso enquanto fala.

## Como funciona

1. **Escolha o conceito.** O que o aluno pediu, ou o mais recente que ele marcou como difícil. Um conceito por sessão.

2. **Faça o pedido assim:**

   > Explica esse conceito para alguém inteligente que nunca ouviu falar disso. Sem usar o jargão da área. Se precisar de uma palavra técnica, explique a palavra também.

3. **Fique quieto enquanto ela fala.** Não corrija no meio, não complete a frase, não vá dando sinal de aprovação linha a linha. Interromper contamina exatamente o que você está medindo.

4. **Chame o agente tutor-avaliador** com a explicação dela. Ele compara contra o conteúdo real, aponta cada lacuna com precisão e devolve duas perguntas socráticas que expõem o maior buraco.

5. **Deixe ela responder as duas perguntas.** Achar sozinha vale dez vezes mais que ouvir a resposta. Só explique se ela não chegar lá depois de duas tentativas.

## O veredito

Uma das três, sem meio termo:

- **entendeu**: explicou o quê, o porquê e onde o conceito deixa de valer
- **entendeu pela metade**: sabe operar, não sabe por quê. É o caso mais comum e o mais perigoso, porque passa em prova e quebra no uso real
- **ainda não entendeu**: reconhece o assunto, não sustenta a explicação

Se o veredito for "ainda não entendeu", a unidade volta para `revisar` no `progresso.json` e a próxima aula ataca por outro caminho.

## Sempre feche assim

Cada lacuna encontrada vira cartão, mirando o buraco e não o tópico inteiro:

```bash
SLUG=$(cat ~/.claude/tutor/ativo)
python3 ~/.claude/skills/tutor/scripts/srs.py add ~/.claude/tutor/$SLUG/flashcards.json \
  --frente "Em que situação <conceito> deixa de valer?" --verso "..." --topico "f2u1"
```

E anexe a devolutiva ao registro da aula correspondente, em `aulas/`, numa seção `## Feynman AAAA-MM-DD`.

Explicação bonita não é explicação correta. Fluência engana quem avalia e engana ainda mais quem fala.
