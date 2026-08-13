---
name: tutor-midia
description: Gera mídia de apoio quando um conceito não entra pelo texto no AI-TUTOR: explicador visual em SVG ou HTML, mapa mental, e material-fonte pronto para virar podcast em áudio ou vídeo no NotebookLM. Use quando alguém disser "faz um áudio disso", "queria ouvir isso caminhando", "me mostra um desenho", "explicador visual", "mapa mental", "faz um vídeo disso", "não estou entendendo por texto" ou "/tutor-midia".
---

# 🎧 Mídia de apoio

Nem todo conceito entra do mesmo jeito. Um diagrama resolve em cinco segundos o que três parágrafos não resolvem, e áudio transforma a caminhada com o cachorro em quinze minutos de revisão.

Isto é complemento, não substituto. Ninguém aprende de verdade só ouvindo. A mídia serve para desatar um nó específico ou para manter contato com o conteúdo fora do horário de estudo.

## Escolha o formato pelo problema

| O problema | O formato |
|---|---|
| conceito espacial, fluxo, relação entre partes | explicador visual (SVG ou HTML local) |
| a pessoa não vê como os assuntos se conectam | mapa mental |
| ela quer revisar fora do computador | podcast em áudio |
| assunto que precisa de narrativa e tempo | vídeo |

## Explicador visual e mapa mental: você mesmo faz

Não dependem de conta nenhuma. Gere um arquivo autocontido em `~/.claude/tutor/<slug>/midia/` e abra:

```bash
SLUG=$(cat ~/.claude/tutor/ativo)
open ~/.claude/tutor/$SLUG/midia/<nome>.html
```

Regras do desenho: um conceito por figura, rótulo em português, nada de decoração que não explique, e legível no escuro e no claro. Para mapa mental, o centro é o conceito-âncora e cada ramo é uma pergunta que aquele ramo responde.

## Áudio e vídeo: material-fonte mais NotebookLM

O NotebookLM gera o resumo em áudio (dois apresentadores conversando sobre o material) e o resumo em vídeo. Ele pede uma conta Google, e é a única parte do AI-TUTOR que depende de login. É opcional: o tutor funciona inteiro sem isso.

**Passo 1. Monte o material-fonte.** Salve em `~/.claude/tutor/<slug>/midia/AAAA-MM-DD-<tema>.md`. Qualidade do áudio é qualidade da fonte, então escreva um documento de verdade, não um apanhado de tópicos:

- o conceito explicado do zero, na linguagem que a pessoa entende
- as analogias que já funcionaram com ela, tiradas dos registros em `aulas/`
- os erros que ela cometeu neste tema, e por que são erros
- de 3 a 5 perguntas que o material precisa responder
- o que fica de fora, para o áudio não se perder

**Passo 2. Leve ao NotebookLM.**

1. Abra `https://notebooklm.google.com` e faça login.
2. Crie um caderno novo, com o nome do curso.
3. Em Adicionar fontes, escolha o arquivo `.md` que você acabou de gerar.
4. Para áudio: em Studio, gere o Resumo em áudio. Dá para personalizar o foco antes de gerar, e vale colar ali as perguntas do passo 1.
5. Para vídeo: em Studio, gere o Resumo em vídeo.
6. Para mapa mental: o próprio NotebookLM tem essa opção a partir das fontes.
7. Baixe o resultado e guarde em `~/.claude/tutor/<slug>/midia/`.

Guie a pessoa por esses passos e espere ela confirmar cada um. Se o botão estiver com outro nome (a interface muda com frequência), descreva o que ele faz em vez de insistir no rótulo exato.

**Passo 3. Feche o ciclo.** Mídia que não vira estudo é entretenimento. Depois que ela ouvir ou assistir, pergunte o que ficou, e o que ela disser vira cartão:

```bash
python3 ~/.claude/skills/tutor/scripts/srs.py add ~/.claude/tutor/$SLUG/flashcards.json \
  --frente "..." --verso "..." --topico "<unidade>"
```

Registre a sessão em `progresso.json` com `"tipo": "midia"`.
