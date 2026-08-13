# OCA lab: cores, tipografia, patterns e KV

Fonte: "Apresentação OCA_2025_FINAL_13.01.26.pdf". Páginas-chave em `assets/img/paginas/`.

## Cores (p.16-18)

### Institucionais (o gradiente, p.17, asset `cores-gradiente-institucional.png`)

O slide oficial de cores mostra um único degradê com as duas pontas marcadas:

| Cor | HEX | Papel |
|---|---|---|
| Azul-claro | `#6EAFD5` | ponta clara do gradiente (esquerda) |
| Navy | `#223564` | ponta escura do gradiente (direita) |

- São **as mesmas cores institucionais do Grupo Aço Cearense** (Pantone 542 C e 534 C respectivamente; valores completos na skill accsdesign).
- A diferença do OCA está no **uso em degradê**: `linear-gradient(90deg, #6EAFD5, #223564)`, claro à esquerda e escuro à direita, no sentido da leitura. É assim no logo padrão, nos fundos e nos patterns.
- Não inverta o sentido no logo padrão.

### Cores de apoio (p.18, asset `cores-apoio.png`)

O doc traz o círculo cromático e justifica cada apoio:

| Papel | Cor | HEX | RGB | Pantone | CMYK |
|---|---|---|---|---|---|
| **Análoga** | Verde-água | `#55C0B3` | 85, 192, 179 | 3258 C | 63, 0, 37, 0 |
| **Complementar** | Coral | `#FF5C60` | 255, 92, 96 | 184 C | 0, 76, 51, 0 |

- Ambas **já pertencem à paleta secundária do Grupo Aço Cearense** (lá chamadas de turquesa e coral), então o OCA continua 100% dentro do sistema de cores do grupo.
- Uso: versões secundárias do logo, brindes (caneca/envelope verde-água, caderno coral), gola/punho de uniforme, nome no crachá, acentos em pattern (gradiente azul->coral nas letras cropadas).
- Nunca dominam peça institucional; o azul sempre presente.

### Fundos escuros (aplicações, p.31-39)

Wallpapers, letreiros e telas usam fundos azul-profundo/metal escuro **sem hex documentado**. Derive do navy (ex. `#101A32`) ou use foto/textura escura com wash azul, e trate como derivado (não oficial).

## Tipografia (p.13-15)

### Famílias (p.14, asset `tipografia-eurostile-herokid.png`)

O slide declara o par: **"EUROSTILE and HEROKID"**.

- **Eurostile**: a principal. Sans-serif geométrica de formas quadradas com cantos arredondados (a mesma família visual do lettering do logo). Mostrada em regular e bold, caixa alta e baixa, com numerais. Serve títulos e corpo.
- **Herokid**: display bold de impacto, em caixa alta (o slide mostra o cartaz típico de pesos pesados). É **a mesma display do Grupo Aço Cearense** (ver accsdesign), o que reforça o parentesco.

### Hierarquia aprovada (p.15, asset `tipografia-pares.png`)

O slide mostra 4 combinações de título + corpo, que se resumem a 2 pares:

1. **Itálico**: título em Eurostile itálico caixa alta + corpo em itálico.
2. **Reto**: título em Eurostile bold caixa alta + corpo regular.

Regra prática: títulos SEMPRE caixa alta; escolha o par (itálico ou reto) e mantenha na peça inteira; corpo com entrelinha confortável.

### Fallbacks de protótipo

Eurostile e Herokid são fontes licenciadas. Para protótipo/web sem os arquivos:

- Eurostile -> **Oxanium** (Google Fonts, corpo e títulos, vários pesos) ou **Michroma** (Google Fonts, só 1 peso, ótima pra título curto com efeito Extended).
- Herokid -> **Big Shoulders Display** ou **Anton** (mesmos fallbacks da accsdesign).
- Peça os arquivos reais ao Gustavo para material oficial final e avise quando entregar algo em fallback.

## Patterns (p.45-49)

Duas famílias oficiais:

1. **Pattern de logo repetido** (p.46-47, assets `pattern-logo-azul.png` e `pattern-logo-verde.png`): o "OCA lab" completo, em outline tom sobre tom (navy translúcido), repetido em grade regular com linhas alternadas rotacionadas 90°. Fundos: gradiente `#6EAFD5 -> #223564` (versão azul) ou `#223564 -> #55C0B3` (versão verde-água). Uso: envelopes, canecas, fundos de crachá, texturas de área grande.
2. **Pattern de letras cropadas** (p.48-49, assets `pattern-letras-cropadas.png` e `pattern-letras-coral.png`): as letras "OCA" gigantes, tom sobre tom, cortadas pelas bordas da peça (sangram pra fora, nunca cabem inteiras). Versão azul (gradiente institucional) e versão **azul-claro -> coral**. Uso: capas, ecobag, caderno, fundos hero.

Regra comum: pattern é sempre **tom sobre tom de baixo contraste** (textura, não protagonista); o conteúdo por cima precisa continuar legível.

## KV oficial (p.50-51, asset `kv-oficial.png`)

Estrutura do key visual do rebranding:

- **Esquerda**: colagem de fotografias em molduras de **paralelogramo/facetas diagonais** (mesma linguagem de grafismo diagonal do grupo): vergalhões/aço, solda robótica, tecnologia (mulher com tablet/tela futurista com acento coral), painel navy com malha 3D, bobina de arame, textura verde-água. Protagonista em primeiro plano: pessoa real de capacete branco com prancheta/tablet (gente de verdade trabalhando, padrão do grupo).
- **Direita**: área branca com o **logo OCA lab grande em gradiente**.
- **Rodapé direito**: pílula outline com a URL **grupoacocearense.com.br** + logo **Grupo Aço Cearense** navy (endosso institucional).
- Fundo geral branco; o peso visual escuro fica na colagem.

É a mesma gramática do KV do grupo (facetas diagonais + rodapé com pílula de URL + logo), com o logo do OCA como herói. Para KV de campanha nova: manter colagem diagonal à esquerda (ou topo), logo em gradiente em área limpa, endosso do grupo no rodapé.

## Universo visual (capa e separadores, p.1, 6, 11-13, 16, 30, 45)

Os separadores da apresentação definem a fotografia "de marca" do OCA:

- Macro de **superfícies metálicas escuras**: malha hexagonal de aço, túnel de anéis, ondas de metal líquido, leque de lâminas.
- **Hexágono** como forma recorrente (malha da capa, base do holograma).
- **Neon ciano/azul** e glow sobre escuro (telas, hologramas, bordas de botão).
- Tecnologia + indústria juntas: VR, robótica, telas, sempre com o aço presente.
- Fotos de pessoas: wash azul, contexto de trabalho/tecnologia, sem pose de banco de imagem.
