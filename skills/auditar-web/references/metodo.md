# Método: validar antes de listar

As 8 armadilhas abaixo foram pagas na auditoria do site do Grupo Aço Cearense (ago/2026). Todas geraram achado errado que só caiu porque foi validado antes da entrega.

## As armadilhas de falso positivo

| O que parecia | O que era | Como validar |
|---|---|---|
| Menu suspenso transparente, texto ilegível | Transição de 0,3s capturada no meio. O dropdown tem fundo sólido | Hover, esperar 2s, só então capturar. Ou ler a regra CSS do estado aberto |
| Nenhum banner do hero é clicável | Os 4 slides têm link. A árvore de acessibilidade não expõe slide fora da viewport | `fetch` da página e contar `a[href]` dentro do bloco do carrossel |
| Só 4 produtos existem no HTML | Os 43 estão no HTML, o carrossel só esconde visualmente | Contar no HTML servido, não no DOM renderizado |
| Cards de produto são links sem nome | Todos têm texto e imagem com alt | Filtrar links sem `textContent`, sem `aria-label` e sem `img[alt]` |
| Imagens não carregam | Carregam, mas devagar no primeiro acesso | Checar se há `src` e `data-src`, e recarregar com cache limpo |
| Contador mostra números errados | Animação em andamento. Estabiliza no valor certo e não reinicia | Ler o valor após 5s e depois de rolar pra fora e voltar |
| Itens de menu de 1º nível não clicáveis | Todos têm `href` | Ler os `href` dos filhos diretos do nav |
| Integração de CRM desconhecida | O formulário posta direto no Salesforce Web-to-Lead | Ler `action` e os `name` dos campos do form |

## Roteiro de validação

Rodar tudo no navegador real, na página servida, antes de qualquer afirmação:

```js
// estrutura da página, sem depender do que a tela mostra
const d = new DOMParser().parseFromString(await fetch(url,{cache:'reload'}).then(r=>r.text()),'text/html');

// links sem nome acessível de verdade
[...d.querySelectorAll('a')].filter(a => !a.textContent.trim() && !a.getAttribute('aria-label') && !a.querySelector('img[alt]:not([alt=""])'));

// campos sem label associado
[...d.querySelectorAll('input,select,textarea')].filter(e => !e.id || !d.querySelector(`label[for="${e.id}"]`));

// contraste real do botão
const c = getComputedStyle(document.querySelector('.botao')); // bg + color, calcular a razão

// o que existe publicado vs o que é navegável
const slugs = [...(await fetch('/produtos-sitemap.xml').then(r=>r.text())).matchAll(/\/produtos\/([a-z0-9-]+)\//g)].map(m=>m[1]);
```

**Cuidado com id que começa com número** (campo do Salesforce, tipo `00N5e00000g0sFl`): `querySelector('#00N...')` lança erro de seletor inválido. Use `[name="..."]` ou `getElementById`.

## O que sempre checar, mesmo que ninguém peça

- **Sitemap contra catálogo navegável.** No GAC apareceram 4 produtos publicados e indexados que não estavam em categoria nenhuma. Quem vem do Google acha, quem navega não.
- **Conteúdo técnico preso em imagem.** Tabela de especificação em PNG não é lida por leitor de tela, não indexa, não copia e some no celular. E esconde erro: 11 erros de unidade e grafia estavam invisíveis dentro das imagens do GAC.
- **Print de tela publicado como ficha.** Nome de arquivo tipo `Captura-de-tela-2025-...` denuncia.
- **O caminho do CTA principal ponta a ponta.** Clicar de verdade e ver se o contexto sobrevive. No GAC, o botão da página do produto levava a um formulário que não sabia qual produto era.
- **Enviar o formulário vazio** para ver se a validação existe e é visível.
- **O banner de consentimento no mobile**, tentando recusar. Se recusar não funciona no primeiro toque, é problema de uso e de LGPD.
- **Estado inicial de select de UF.** Abrir em "AC" gera lead sujo em silêncio.
- **Contagem de itens no admin contra o que aparece no site**, quando houver acesso.

## Prioridade

- **P0**: quebra receita, gera dado errado ou impede uso (CTA que perde contexto, formulário sem validação, banner que bloqueia toque, lead sem origem).
- **P1**: atrapalha decisão ou credibilidade (ficha em imagem, contraste, catálogo sem filtro, ausência de prova técnica).
- **P2**: polimento e ganho marginal.

Prioridade alta demais em tudo é o mesmo que não priorizar. No GAC, 24 P0 de 135 itens foi o equilíbrio que segurou a conversa.
