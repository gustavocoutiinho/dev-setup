# Entregáveis

Três peças. A planilha é a fonte da verdade, o pacote é o que faz a coisa acontecer, o plano é o que sustenta a conversa com o cliente.

## 1. Planilha de melhorias

Uma linha por ponto, dez colunas:

| Coluna | Conteúdo |
|---|---|
| Nº | Sequencial estável. Nunca renumere: o número vira o nome do item na conversa |
| Melhoria | Título curto, o problema em cinco palavras |
| Descrição | O problema **com a evidência**: o que foi clicado, o que retornou, o valor medido |
| Descrição (ação) | O que fazer |
| Origem do dado | A URL ou o trecho onde ocorre |
| Área | Home, Menu, Catálogo, Página de produto, Formulário, Busca, Mobile, Global, Institucional, Medição |
| Tipo | Conversão, Usabilidade, Acessibilidade, Conteúdo, LGPD, SEO, Performance, Dados, Segurança |
| Prioridade | P0, P1, P2 |
| Solicitado por | Quem pediu |
| Observações | O status real: CONFIRMADO com a prova, DESCARTADO com o motivo, AJUSTADO, RESOLVIDO, ou o que falta |

Regras que evitam retrabalho:

- **Item descartado não some da planilha.** Fica com o motivo. É o que impede alguém reabrir o mesmo falso positivo daqui a três meses.
- **Status é o que está no ar**, não o que está pronto. Enquanto não subiu, é "pronto para publicar".
- **Onde executar e esforço** entram nas observações: painel, snippet, tema, plugin, ferramenta externa.

Para preencher rápido sem digitar célula a célula, monte o TSV, copie via `execCommand('copy')` numa textarea temporária e cole com `cmd+v` na célula inicial. Navegue entre células com `cmd+j` (caixa de nome). Copiar e colar precisam sair na mesma sequência: clipboard do sistema é volátil e outra coisa pode sobrescrever no meio.

## 2. Pacote colável

Um arquivo por lote, com o código já testado no site real e o roteiro de conferência. Estrutura que funcionou:

1. O que o lote resolve, com os números dos itens da planilha.
2. **Snippet de CSS**, com comentário ligando cada regra ao item.
3. **Snippet de JS**, defensivo: verifica se o elemento existe antes de agir, não quebra página onde não se aplica, e não roda duas vezes.
4. **Conteúdo pronto** (tabela HTML, texto de página) quando for caso de painel.
5. **Depois de colar**: onde publicar, qual cache limpar, e o roteiro de conferência página por página.
6. **O que este lote não resolve e por quê.**

Antes de entregar, rode cada trecho no site real e mostre o resultado no relatório: "envio vazio gerou as 7 mensagens de erro", "CEP 60120-000 preencheu Avenida Barão de Studart, Meireles, Fortaleza, CE". Ninguém confia em código que nunca rodou.

Nunca dispare o caminho de sucesso de um formulário em produção durante o teste: cria lead falso no CRM do cliente.

## 3. Plano de onda

Publicado como página no design do cliente, para o interlocutor mandar adiante sem precisar reescrever.

- **Onda 0, fundação:** backup com restauração testada, baseline da métrica que vai provar o ganho, acessos e avais pendentes. Sem isso não se mexe.
- **Onda 1, até 30 dias:** reversível, sem reforma de layout, com o código já pronto.
- **Onda 2, 30 a 60 dias:** o funil de conversão e o catálogo. Janela combinada.
- **Onda 3, 60 a 90 dias:** o que depende de material do cliente e o que diferencia a marca.

Fecha com duas seções que evitam a maior parte do atrito:

- **Quem faz o quê**, separando a Miner, a agência incumbente, o time técnico do cliente, o TI e os fornecedores de ferramenta.
- **A lista única do que está travado**, com cada pedido de insumo escrito de forma que dê para responder em um e-mail. Pedido fatiado em cinco conversas não anda.
