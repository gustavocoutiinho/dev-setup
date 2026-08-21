---
name: auditar-web
description: Use SEMPRE que precisar auditar um site que NÃO é da Miner e que a Miner não vai executar sozinha: site institucional de cliente feito por outra agência, portal de terceiro, e-commerce de prospect. Entrega diagnóstico de UX e conversão com evidência item a item, planilha de melhorias, pacote de código pronto pra colar e plano de execução por onda, separando quem faz o quê. Dispara com "analisa o site do <cliente>", "auditoria de UX", "pontos de melhoria do site", "o que tem de errado no site deles", "manda pra agência arrumar", "o Ricardo já viu a parte técnica, falta a de UX", "avalia o site do prospect", "quero uma análise pra mandar pro cliente". NÃO é criar do zero ([[criar-web]]), consertar portal nosso ([[conserta-web]]), faxina de deploy ([[faxina-web]]) nem segurança ([[blindar]]).
---

# auditar-web: diagnóstico de site de terceiro com prova, planilha e pacote colável

Auditar site que a Miner não construiu e não controla. O cliente é dono, outra agência mantém, e a Miner entra como quem enxerga o problema e entrega o caminho. O produto final não é uma lista de opiniões: é achado com evidência, planilha rastreável, código pronto pra colar e um plano por onda que diz quem faz o quê.

Caso fundador: **site institucional do Grupo Aço Cearense** (ago/2026), WordPress mantido pela elleven, com 143 pontos mapeados, 8 falso positivo descartados na validação e 15 fichas técnicas convertidas. O retrato técnico daquele site está na memória `site-gac-stack`.

## A regra que define esta skill

**Valide antes de listar.** Screenshot mente. Transição de 0,3s congelada vira "menu transparente", carrossel virtualizado vira "produto não existe no HTML", carregamento em andamento vira "imagem quebrada". Na auditoria do GAC, 8 dos 51 primeiros achados eram artefato de captura, incluindo dois P0. Se tivesse entregado sem validar, a Miner teria proposto corrigir coisa que funciona, na frente do cliente e da agência que mantém o site.

Toda afirmação da entrega precisa de uma destas provas: leitura do HTML servido (`fetch` + `DOMParser`), teste de interação real, medição de cor computada, ou consulta ao sitemap. Nunca só "vi na tela".

## Modos

- **diagnóstico** (padrão): varre, valida, prioriza e entrega a lista com evidência.
- **pacote executável**: transforma os achados em CSS/JS colável e conteúdo pronto, sem depender de acesso de escrita.
- **plano de onda**: organiza em ondas com responsável e dependência, pra virar conversa de projeto com o cliente.

## Como executar

1. **Contexto antes da varredura.** Carregue o cliente com [[obsidianminer]]: quem decide, o que já existe, qual campanha está rodando, quais personas a mídia segmenta. Auditoria sem isso vira lista genérica de checklist.
2. **Varra o site pelo navegador, não por curl.** Site sério está atrás de WAF (o do GAC está em Akamai, curl volta 403). Use o Chrome real. Passe por: home, catálogo, página de produto, formulário de conversão, contato, busca, busca vazia, 404, e o mesmo caminho no mobile.
3. **Valide cada achado** com o roteiro de [references/metodo.md](references/metodo.md). Só sobe pra lista o que tiver prova.
4. **Levante os seletores reais** antes de escrever qualquer correção. Classe de botão, id de campo, estrutura do acordeão, nome da variável de cor. Correção escrita com seletor chutado não cola.
5. **Monte a planilha** no padrão de [references/entregaveis.md](references/entregaveis.md): número, melhoria, problema com evidência, ação, página, área, tipo, prioridade, solicitante, status.
6. **Gere o pacote colável** (CSS + JS + conteúdo), testado no site real antes de entregar. Ver [references/wordpress.md](references/wordpress.md) quando for WordPress.
7. **Feche com o plano de onda** e a lista única do que está travado esperando insumo do cliente. Pedido fatiado em cinco conversas não anda.

## Regras duras

- **Nada de verde sem estar no ar.** Item só é marcado como concluído depois de verificado no site publicado. Enquanto não subiu, o status é "pronto para publicar".
- **Não invente dado técnico.** Bitola, norma, medida e prazo saem do cliente. Se a ficha original tem erro, aponte e peça aval, não corrija sozinho no ar.
- **Tabela grande em imagem não se transcreve.** Acima de ~25 linhas em corpo pequeno, peça a planilha original. Errar bitola de aço é pior do que demorar.
- **Aditivo e reversível primeiro.** CSS e JS em snippet (WPCode e equivalentes), nunca edição direta do tema de outra agência: a próxima atualização apaga e a culpa sobra pra Miner.
- **Formulário é receita.** Mudança em campo de conversão vai em janela combinada, com baseline levantado antes e teste de ponta a ponta com envio real depois.
- **Trate a agência incumbente como par, não como réu.** O relatório separa o que a Miner executa do que é da outra agência, sem adjetivo sobre o trabalho dela.

## Referências

- [references/metodo.md](references/metodo.md) — as 8 armadilhas de falso positivo, o roteiro de validação e o que sempre checar.
- [references/wordpress.md](references/wordpress.md) — playbook de WordPress de terceiro: o que dá pra ver sem admin, como levantar seletor, onde encaixar snippet.
- [references/entregaveis.md](references/entregaveis.md) — formato da planilha, do pacote colável e do plano de onda.

Material visual pro cliente passa pela skill de design dele ([[accsdesign]], [[saoluizdesign]], [[ocadesign]] etc.). O plano de onda do GAC foi publicado como artifact nesse padrão.
