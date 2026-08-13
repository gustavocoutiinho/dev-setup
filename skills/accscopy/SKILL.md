---
name: accscopy
description: Escreve e revisa QUALQUER copy/texto para o cliente Aço Cearense/ACCS/Grupo Aço Cearense/Sinobras (Miner), incluindo headline e legenda de anúncio (Meta/Google/LinkedIn), post orgânico, roteiro de vídeo, e-mail comercial, proposta, ficha de produto, release, script de WhatsApp/vendedor, texto de KV/deck/relatório, ou qualquer peça que precise soar "com a cara" verbal do cliente. Cobre as 3 marcas com atuação comercial ativa (Aço Cearense B2B, SINOBRAS, Grupo Aço Cearense) e conhece a fundo o catálogo de produtos (specs técnicas reais) e a estrutura de campanhas digitais 2026 (funil, personas, tom por marca, copy já aprovada). Use SEMPRE que o Gustavo pedir para escrever, revisar, ajustar ou gerar copy/texto/legenda/headline/roteiro em nome desse cliente, mesmo que ele não cite a skill pelo nome, diga só "escreve o texto pra Aço Cearense/Sinobras" ou peça pra "minerizar o texto" do cliente. É irmã da skill accsdesign (que cuida do visual); quando a peça for visual e verbal junto (KV, deck, post), use as duas.
---

# accscopy

Escreve copy em nome do Grupo Aço Cearense (cliente Miner, alias ACCS: Aço Cearense, SINOBRAS, SINOBRAS Florestal, Instituto Aço Cearense, Grupo Aço Cearense). O trabalho é gerar texto novo (headline, legenda, e-mail, roteiro, descrição de produto) que soe como se o próprio time de marketing do cliente tivesse escrito, calibrado pelo tom de voz real da marca e pela copy que ela já aprovou e está rodando em campanha.

Esta skill é irmã da [[accsdesign]] (identidade visual do mesmo cliente): aquela cuida de cor, tipografia, grafismo e layout; esta cuida do texto. Nunca misture o design system de outro cliente aqui, e nunca invente uma voz nova quando a marca já tem uma documentada.

## Qual caminho seguir

Antes de escrever, decida três coisas:

1. **Qual marca**: Aço Cearense (aços planos, B2B), SINOBRAS (aços longos) ou Grupo Aço Cearense (institucional/corporativo) são as 3 com estrutura de campanha digital ativa (ver [references/campanhas-digitais.md](references/campanhas-digitais.md)). SINOBRAS Florestal e Instituto Aço Cearense não têm campanha própria hoje: se pedirem copy pra elas, use o tom geral do grupo em [references/tom-de-voz.md](references/tom-de-voz.md). Se o Gustavo não especificar a marca e o contexto não deixar óbvio, pergunte antes de escrever — o tom e a tagline mudam de verdade entre elas.
2. **Qual produto ou tema**: se a copy fala de um produto específico (vergalhão, telha, tubo, chapa...), confira a especificação técnica real em [references/catalogo-produtos.md](references/catalogo-produtos.md) antes de escrever. Copy técnica errada (bitola errada, norma errada) quebra o pilar de credibilidade que sustenta toda a voz da marca.
3. **Qual formato**: anúncio de campanha (headline curta + persona), copy institucional/manifesto (mais longa, corrida), ficha de produto (técnica + um parágrafo de venda), ou texto solto (e-mail, script, post orgânico). O formato muda o tamanho e a estrutura, não o tom.

## Fonte da verdade

Três documentos-fonte, cada um com uma referência dedicada:

- [references/tom-de-voz.md](references/tom-de-voz.md) — o resumo operacional do tom de voz, taglines, pilares, palavras proibidas e glossário de atributos por produto. A fonte completa e canônica desse capítulo vive em `~/.claude/skills/accsdesign/references/marca-e-verbal.md` (skill irmã) — **leia aquele arquivo inteiro antes de qualquer copy institucional ou de manifesto**, o resumo aqui é só o operacional do dia a dia.
- [references/campanhas-digitais.md](references/campanhas-digitais.md) — plano de mídia 2026: papel de cada marca no funil, diferença de tom entre as 3 marcas, personas ("humanização por segmento"), formatos por canal, e uma coleção grande de copy real já aprovada pelo cliente (headlines por produto × persona) pra usar como calibração.
- [references/catalogo-produtos.md](references/catalogo-produtos.md) — o catálogo de produtos completo (SINOBRAS Aços Longos + Aço Cearense Aços Planos): especificação técnica de cada item, aplicações, copy institucional já aprovada, e uma lista de inconsistências/oportunidades de diferenciação encontradas no documento original.

Documentos originais (se precisar checar algo que as referências não cobrem, ou se o Gustavo mandar uma versão atualizada):
- `~/Downloads/ESTRUTURA CAMPANHAS DIGITAIS - AÇO - GRUPO - SINOBRAS.pdf` (58 páginas)
- `~/Downloads/Catálogo_açocearense (1).pdf` (35 páginas)
- `~/Downloads/BRAND GUIDELINES 1920x1080px ACO CEARENSE - AF.pdf` (139 páginas, mesma fonte usada pela `accsdesign`)

Se qualquer um desses três não estiver mais em Downloads, ou se o Gustavo mencionar uma versão nova, peça o arquivo atualizado antes de assumir que esta skill ainda reflete a versão certa.

## O essencial em uma tela

**Tagline-mãe**: "Nossa gente dá liga. Nossa liga constrói o futuro." **Tagline Aço Cearense**: "Qualidade que constrói confiança." **Tagline SINOBRAS**: "Pode construir. Pode confiar."

**Tom por marca**: Aço Cearense foge do regionalismo cearense como driver, prioriza tradição/segurança/proximidade/confiança. SINOBRAS prioriza indústria nacional/tecnologia/qualidade certificada/rastreabilidade, com linha própria pra construtoras e grandes obras. Grupo Aço Cearense é institucional puro: reputação, ESG, marca empregadora.

**Fórmula de headline de produto validada pelo cliente**: `[PRODUTO EM CAIXA ALTA]. [Mensagem de 5-10 palavras endereçada à persona/contexto]. [Tagline da marca]`. Exemplos e a lista completa de personas (Revendedor, Construtora, Engenheiro Civil, Mestre de Obras, Serralheiro etc.) estão em [references/campanhas-digitais.md](references/campanhas-digitais.md).

**Nunca**: superlativo de superioridade (único, imbatível, líder absoluto), jargão técnico gratuito, gíria, formalidade rebuscada, termo ambíguo (liga pesada, chapa quente), palavra que não representa o setor (luxo, premium, artesanal), sigla pública (nunca IAC/GAC, escreva por extenso), ou travessão.

**Sempre**: credibilidade via conformidade normativa real (NBR, SAE/ABNT) puxada do catálogo, nunca inventada; atributo certo por produto (ver glossário em `marca-e-verbal.md`); calibre pela copy real já aprovada antes de inventar um tom novo do zero.

## Como executar

1. Identifique marca, produto/tema e formato (ver "Qual caminho seguir"). Se faltar informação essencial (qual marca, qual persona, qual canal), pergunte — não adivinhe uma marca errada, o tom muda de verdade entre elas.
2. Leia [references/tom-de-voz.md](references/tom-de-voz.md) e, se for peça institucional/manifesto, o `marca-e-verbal.md` completo da `accsdesign`.
3. Se a copy envolve produto, confira a especificação real em [references/catalogo-produtos.md](references/catalogo-produtos.md) — não invente bitola, norma ou aplicação.
4. Se a copy é de campanha/anúncio, puxe a estrutura de persona e a copy real já aprovada em [references/campanhas-digitais.md](references/campanhas-digitais.md) como ponto de partida, adaptando ao pedido específico em vez de repetir literalmente (a menos que o Gustavo peça pra reusar uma peça existente).
5. Escreva. Aplique as regras duras de vocabulário (seção acima) e o pilar de tom certo pra marca.
6. Releia em voz alta mentalmente: soa como o exemplo real de copy on-brand documentado, ou soa genérico/vendedor demais? Se soar genérico, é sinal de que fugiu do tom.
7. Se a peça também precisa de tratamento visual (KV, post, deck), acione a `accsdesign` na sequência ou junto.

## Referência viva

Contexto do cliente (stakeholders, projetos ativos, portal, stack, cadência de reuniões): nota `Aço Cearense` no vault Obsidian (skill `obsidianminer`) e memórias `project_portal_accs`, `project_campanhas_aco_sinobras`, `project_contexto_accs`. O Portal de Eventos ACCS (`accs-eventos.minerbz.com.br`) já cobre Construnordeste e Concrete Show 2026 citados na estrutura de campanhas: se a copy for para um desses eventos, confirme no vault se o calendário mudou antes de assumir as datas daqui.
