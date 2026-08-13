# Inconsistências do documento-fonte

O manual "Diretrizes da Marca" (Versão 10) tem algumas inconsistências internas, reais, conferidas com zoom nas páginas originais durante a extração. Isso não é erro de leitura: são imprecisões do próprio arquivo entregue pela agência Propeg. Registradas aqui para que ninguém "corrija" um valor que já está certo na skill achando que ela diverge do PDF, e para que, se o Gustavo cruzar esta skill com o PDF original, as diferenças façam sentido.

## Datas de versão divergentes

A maioria das páginas (miolo do documento, p.5 a p.137) traz o carimbo **"VERSÃO 10 › MAR.2025"**. Mas a capa (p.1), a página de citação (p.2), o sumário (p.3) e as duas páginas finais de encerramento (p.138-139) trazem **"VERSÃO 10 › AGO.2025"**. Provável explicação: capa/contracapa foram atualizadas numa revisão posterior sem atualizar o carimbo do miolo. Se precisar citar "a versão do manual" com data, use Ago.2025 (a mais recente) e mencione que o miolo ainda está carimbado Mar.2025.

## Numeração do sumário não bate com o conteúdo real

O sumário da p.3 (e o índice repetido na abertura do capítulo 4, p.47/48) diz que "Estilo fotográfico" começa na **p.83**. Na prática, a seção termina no capítulo "Grafismo" na p.78, e "Estilo fotográfico" já começa na **p.79** (confirmado pelo indicador ativo no menu lateral da própria página). Ou seja, há um desvio de 4 páginas entre o sumário e o conteúdo. Se for procurar algo direto no PDF original por número de página do sumário, desconte essa diferença nessa região do documento.

Também há uma pequena divergência de nome: o sumário da p.3 usa "**Marcas em uso**" (plural); a barra de navegação lateral (presente em toda página) e o título da própria seção (p.126) usam "**Marca em uso**" (singular).

## Regra de área de proteção (clear space) com dois textos diferentes

A definição-mãe da área de proteção (p.34) e a página de pareamento com selos de projeto (p.46) dizem que a margem deve ser "**no mínimo equivalente**" à altura de referência. Já as páginas de pareamento com marcas do Grupo/parceiros (p.39-42, p.45) dizem que a margem deve ser "**menor que**" essa altura, o oposto. A skill trata "no mínimo equivalente" como a regra correta (é a formulação técnica padrão de clear space em qualquer manual de marca); o mais provável é que "menor que" seja erro de digitação nessas páginas específicas.

## Valores de CMYK impossíveis (K acima de 100, ou K que contradiz a cor mostrada)

- **Pantone Cool Gray 7 C** (`#9D9D9C`, p.52): o documento imprime CMYK "C0 M0 Y0 **K500**". K não pode passar de 100. Valor de mercado padrão desse Pantone é K≈50; a skill usa K.50.
- **Pantone 376 C** (`#94C120`, verde-limão vibrante, p.53): o documento imprime CMYK "C50 M0 Y99 **K100**". K100 tornaria a cor quase preta, o que contradiz visualmente o verde-limão claro mostrado na página. A skill usa K.0.

## Pantone duplicado em duas cores diferentes

**Pantone 542 C** aparece atribuído tanto à cor institucional `#6EAFD5` (p.50) quanto à cor secundária `#7DB5DA` (p.53) — dois HEX diferentes, mesmo código Pantone. Registrado como está; não invente um segundo código pra desambiguar.

## Pequena discrepância de conversão HEX→RGB

`#6EAFD5`: a conversão matemática exata seria RGB(110,175,213), mas o documento imprime RGB(109,174,213) (1 unidade a menos em R e G). É a única cor do manual com essa discrepância; as outras 14 cores com código completo batem exatamente. Não é relevante na prática (a diferença é imperceptível), citado só por rigor.

## Textos de tom de voz com pilares trocados

Na p.22 (fechamento do capítulo "Tom de voz"), os textos-descrição dos pilares "Direciona para o futuro" e "Transmite credibilidade" aparecem invertidos em relação ao padrão estabelecido nas p.18/20/21 (o texto que deveria estar em "Transmite credibilidade" aparece em "Direciona para o futuro" e vice-versa). A skill usa a versão das p.18/20/21 como canônica. Ver [marca-e-verbal.md](marca-e-verbal.md).

## Exemplos de nomenclatura marcados como fictícios

Na página de "Diretriz de nomenclatura" (p.10), os exemplos "Aço Cearense Logística" e "SINOBRAS Mineração" (categoria Monolítica) vêm com nota explícita "*EXEMPLOS FICTÍCIOS" no próprio documento. Não são marcas reais do Grupo — não trate como existentes em nenhuma peça.

## Duas marcas citadas sem detalhamento visual

"Rede OCA" e "WMA" aparecem como exemplos reais de marca "endosso distante/independente" (p.10), mas não recebem página, ícone ou paleta própria em nenhum outro trecho das 139 páginas. Se precisar criar algo para elas, confirme com o cliente antes: a skill não tem base para inventar identidade visual pra essas duas.

## Instituto Aço Cearense sem cor de identificação própria

Diferente das outras 3 unidades (Aço Cearense, Sinobras, Florestal Sinobras), o Instituto não recebe uma cor de destaque no sistema de crachás (p.136) nem em nenhuma outra peça — só aparece em versão branca reversa sobre azul-marinho. Não invente uma cor para o Instituto; se for necessário, é uma decisão a validar com o cliente.

## Pequenas inconsistências gramaticais (concordância verbal/nominal)

Várias páginas têm pequenas variações de concordância entre si (ex. "predominantes" vs. "predominante", "Versão secundárias" vs. "Versões secundárias", "sobre o questões" por "sobre as questões", "Criação de **de** selos de projetos" com "de" duplicado). Nenhuma muda o sentido da regra; registradas só por transparência, não são erros da skill.
