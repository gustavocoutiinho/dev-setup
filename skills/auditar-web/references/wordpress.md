# Playbook: WordPress de terceiro

A maioria dos sites institucionais de cliente é WordPress mantido por outra agência. Este é o caminho que funciona sem virar o site do avesso.

## Antes de tudo: como o site responde

`curl` costuma voltar 403 em site sério (Akamai, Cloudflare). Não conclua que o site está fora do ar: **abra pelo Chrome real**. Se precisar do HTML, use `fetch` de dentro da página, que herda a sessão e passa pelo WAF.

Cabeçalhos valem uma olhada rápida: HSTS, `x-content-type-options`, `referrer-policy`, `permissions-policy` e CSP. No GAC, os quatro primeiros estavam bem configurados e só o CSP era fraco. Não invente problema onde não há.

## Sem acesso ao admin, dá pra descobrir

| O quê | Como |
|---|---|
| Tema e plugins | Caminhos em `/wp-content/themes/<tema>/` e `/wp-content/plugins/` nos assets da página |
| Todos os produtos publicados | `/<cpt>-sitemap.xml` ou `/wp-sitemap.xml` |
| Se é Contact Form 7 | `form.wpcf7-form` e os campos `_wpcf7*` |
| Se posta em CRM externo | `action` do form. Salesforce Web-to-Lead tem `oid`, `retURL`, `lead_source` e campos `00N...` |
| Ferramenta de consentimento | Prefixo dos ids do banner (ex.: `oPrivallyApp-` é Privally) |
| Tradução | `trp-` é TranslatePress; `hreflang` mostra os idiomas |
| Cache | `LSCWP_CTRL` na barra do admin é LiteSpeed |

## Com acesso ao admin

Confirme antes de tocar: versão do núcleo, atualizações pendentes, plugin de snippet disponível (WPCode, Code Snippets), plugin de backup, e se existe ambiente de homologação. Confirme também **qual conta está ativa**, tanto no WordPress quanto no Google, antes de qualquer gravação.

Cuidado com a lista de posts: os links de ação da linha (`Editar`, `Clonar`, `Lixeira`) ficam colados e só aparecem no hover. Clicar por coordenada erra o alvo e cria rascunho duplicado. Use referência de elemento, ou filtre a lista e use ação em massa.

## Onde encaixar a correção

Ordem de preferência, da mais segura para a menos:

1. **Conteúdo pelo painel** (campo de texto, ACF, item de menu). Reversível, não some em atualização.
2. **Snippet de CSS/JS pelo WPCode**, site wide. Aditivo, desligável num clique, sobrevive à atualização do tema.
3. **Configuração do plugin** (formulário, consentimento, cache).
4. **Child theme.**
5. **Tema do fornecedor**: só com a outra agência dentro da conversa. Editar direto significa perder a correção na próxima atualização, e a culpa sobra pra Miner.

## O que o tema já costuma resolver sozinho

Antes de escrever CSS novo, procure a regra existente. No GAC, o tema já tinha estilo pronto para `.technical-specifications table`: a ficha em imagem podia virar tabela HTML só trocando o conteúdo, sem uma linha de código.

Procure assim:

```js
for (const ss of document.styleSheets) { try { for (const r of ss.cssRules) if (/palavra-chave/.test(r.cssText)) console.log(r.cssText) } catch(e){} }
```

## Armadilhas específicas já pagas

- **Acordeão que não abre por `.click()` no bloco.** O handler pode estar no ícone. No GAC era o `span` da seta.
- **Campo sem `id`** não tem label associado. Dá pra criar o `id` e amarrar o label por JS, mas o certo é corrigir no template.
- **Select de UF abrindo na primeira opção** (AC). Paliativo por JS resolve na hora; o definitivo é editar o campo no formulário.
- **Formulário postando direto no CRM** não tem hook de plugin: validação e enriquecimento precisam ser client-side, antes do submit.
- **Cache em duas camadas.** Depois de publicar, limpe o do plugin e peça purge do CDN. Sem isso a mudança sobe e ninguém vê, e a conclusão errada é que não funcionou.
