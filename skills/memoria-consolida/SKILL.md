---
name: memoria-consolida
description: Use SEMPRE que a memória do vault Miner precisar de faxina: nota duplicada, fato espalhado em vários lugares, MEMORY.md desalinhado do que existe em memory/. Dispara com "consolida a memória", "limpa o vault", "tem nota duplicada?", "organiza a memória", "unifica isso no vault", "isso já não está anotado?". Fonte única, sem duplicação: atualiza a nota certa em vez de criar outra.
---

# memoria-consolida: faxina e unificação da memória do vault

A memória do Gustavo vive em `~/ObsidianVaults/miner/memory/` (uma nota por fato, lida via symlink), com `MEMORY.md` como índice de uma linha por nota. O princípio é fonte única sem duplicação (foi unificada em 17/06). Esta skill mantém isso: acha duplicata, funde no lugar certo, corrige o índice.

## Quando disparar
- "consolida/limpa/organiza a memória", "tem nota duplicada?", "unifica isso".
- Depois de uma rodada grande de captura, quando muita coisa nova entrou.

## Como executar
1. **Leia o índice** `memory/MEMORY.md` e cruze com os arquivos reais em `memory/` (via [[obsidianminer]]).
2. **Ache duplicata/sobreposição:** dois arquivos sobre o mesmo cliente/tema, ou fato repetido.
3. **Funde no arquivo canônico** (o mais completo), preservando `**Why:**` e `**How to apply:**` de feedback/project. Linka relacionados com `[[nome]]`.
4. **Delete o duplicado** e ajuste o `MEMORY.md` (uma linha, com o gancho certo).
5. **Frontmatter correto:** `type: user|feedback|project|reference`. Datas relativas viram absolutas.
6. **Não invente:** se dois fatos conflitam, marque a divergência, não escolha por conta própria.

## Gotchas
- Nota recente sobre carteira/estado SOBREPÕE o diretório antigo do vault (ex: clientes-ativos-jul2026 manda sobre companies/). Respeite a mais recente.
- MEMORY.md nunca guarda conteúdo, só o índice de uma linha. Não jogue fato lá dentro.

## O que NÃO fazer
- NÃO criar nota nova quando já existe uma pro tema: atualize a existente.
- NÃO apagar memória sem confirmar que o fato foi preservado no canônico.
- NÃO reescrever fato que virou verdade histórica sem marcar a data.
