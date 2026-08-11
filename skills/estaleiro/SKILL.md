---
name: estaleiro
description: Prepara o Estaleiro neste projeto. Faz as perguntas de onboarding (linguagem, comandos de teste, convenções, o que nunca tocar), grava o perfil em .claude/estaleiro/perfil.md e apaga os arquivos de instalação. Use na primeira vez que o Estaleiro roda num projeto, e sempre que o usuário disser "prepara o estaleiro", "configura o estaleiro", "refaz o onboarding", "atualiza o perfil do projeto" ou "/estaleiro".
---

# Preparar o Estaleiro

Esta skill roda uma vez por projeto. Ela cria o perfil que os cinco agentes (Arquiteto, Construtor, Testes, Revisor, Sentinela) leem antes de trabalhar.

## Passo 1: descobrir sozinho antes de perguntar

Nunca pergunte o que você consegue ver. Antes de abrir a boca, investigue:

- Arquivos de dependência na raiz: `package.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Gemfile`, `composer.json`, `Cargo.toml`, `pom.xml`.
- Scripts declarados (`scripts` do `package.json`, `Makefile`, `justfile`, `taskfile`).
- Framework de teste e onde os testes moram.
- Linter e formatador configurados.
- Se existe repositório git e qual a branch principal.
- Se existe `CLAUDE.md`, `AGENTS.md` ou `CONTRIBUTING.md`, leia. Eles já respondem metade das perguntas.

### Regras de casa já registradas

Se existir `~/.claude/estaleiro/portais-miner.md`, leia antes de perguntar qualquer coisa. É o canônico das armadilhas já pagas em produção (deploy, PII, dado aditivo, auth, cache, iframe, banco compartilhado). Ele vale para todo portal, site e app de cliente.

O perfil do projeto **não copia** essas regras: aponta para elas no cabeçalho e registra só o que é específico deste repositório. Regra em dois lugares vira regra desatualizada em um deles.

Se o projeto for de cliente e a base de conhecimento apontar um checklist aplicável (portal novo, evento novo), confira item por item e registre no perfil o que estiver pendente. Não invente que está tudo certo.

## Passo 2: perguntar só o que faltou

Use a ferramenta de pergunta ao usuário, com no máximo quatro perguntas por vez, sempre com a opção que você detectou como primeira alternativa. Perguntas que valem a pena:

1. **Comando de teste**, se você não conseguiu deduzir com certeza.
2. **Comando de verificação rápida** (lint, typecheck ou build) que deve rodar antes de entregar código.
3. **Nível de rigor**: entregar rápido com teste do essencial, ou teste completo antes de qualquer entrega.
4. **Zona proibida**: pastas, arquivos, tabelas ou ambientes que nenhum agente pode tocar sem autorização explícita (migração de banco, arquivos de produção, `.env`, pastas geradas).

Se a investigação do passo 1 respondeu tudo, mostre o que você encontrou e peça só a confirmação. Onboarding bom é curto.

## Passo 3: gravar o perfil

Escreva `.claude/estaleiro/perfil.md` exatamente neste formato, preenchido com a realidade do projeto:

```markdown
# Perfil do projeto

## Stack
- Linguagem e versão:
- Framework principal:
- Gerenciador de pacotes:

## Comandos
- Instalar dependências:
- Rodar em desenvolvimento:
- Testes:
- Lint / formatador:
- Typecheck ou build:

## Testes
- Framework:
- Onde ficam:
- Convenção de nome de arquivo:

## Convenções
- Estilo de código (o que seguir olhando os vizinhos):
- Padrão de commit:
- Branch principal:

## Zona proibida
Nada aqui é alterado sem autorização explícita do usuário na conversa:
-

## Rigor
- Nível: (rápido | completo)
- O que sempre rodar antes de dizer que terminou:
```

## Passo 4: limpar

Depois do perfil gravado, apague os arquivos de instalação que não servem mais:

- `INSTALAR.md` na raiz do projeto, se existir e se for o do Estaleiro.
- `.claude/estaleiro/perfil.exemplo.md`, se existir.

Confirme o conteúdo antes de apagar qualquer coisa. Nunca apague arquivo que não foi criado pelo Estaleiro.

Se o `.gitignore` do projeto ignorar `.claude/` inteiro, o perfil não viaja com o repositório. Troque a regra por `.claude/*` seguido de `!.claude/estaleiro/`, que mantém `launch.json` e configuração local fora do git e deixa só o perfil entrar. Confira depois com `git check-ignore -v` antes e depois, para provar que nada mais mudou de estado.

Esta skill continua disponível: para refazer o perfil quando o projeto mudar, basta rodar `/estaleiro` de novo.

## Passo 4b: devolver o aprendizado

Isto é o que faz o Estaleiro ficar melhor com o tempo, em vez de repetir os mesmos erros em projeto novo.

Sempre que uma sessão descobrir uma armadilha que vale para mais de um projeto (um deploy que derrubou algo, um comportamento de plataforma que não estava documentado, uma regra nova que o usuário deu), registre no canônico `~/.claude/estaleiro/portais-miner.md`:

1. Escreva **sintoma, causa e data**. Sintoma primeiro, porque é por ele que a próxima pessoa procura.
2. Acrescente. Nunca remova regra existente. Se ficou obsoleta, marque como superada e diga o que a substituiu.
3. Edite a fonte versionada em `~/dev/dev-setup/claude/portais-miner.md`, commite e rode `./install-skills.sh`, para valer nas outras máquinas.
4. Se a armadilha for específica de um projeto só, ela vai para a zona proibida do perfil daquele repositório, não para o canônico.

## Passo 5: apresentar a tripulação

Feche com um resumo curto do perfil gravado e a lista de quem faz o quê, em uma linha cada:

- 🧭 **Arquiteto**: planeja antes de codar. "planeje como fazer X"
- 🔨 **Construtor**: escreve o código. "implementa isso"
- 🧪 **Testes**: prova que funciona. "escreve os testes"
- 🔍 **Revisor**: revisa o diff. "revisa antes de eu salvar"
- 🛡️ **Sentinela**: checagem de segurança. "faz uma revisão de segurança"

E avise que não precisa chamar ninguém pelo nome: linguagem natural já aciona o especialista certo.
