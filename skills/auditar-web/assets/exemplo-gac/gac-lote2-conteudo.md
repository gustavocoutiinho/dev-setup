# Lote 2 — conteúdo e mobile | site Grupo Aço Cearense

Continuação do lote 1. Aqui está o que é trabalho de conteúdo no painel mais um snippet de CSS para mobile.
Levantamento feito em 18/08/2026 varrendo os 39 produtos do catálogo e o sitemap.

---

## 1. Ficha técnica em tabela HTML (itens 24, 25, 26, 67 e 92)

O tema **já tem CSS pronto** para `.technical-specifications table` (cabeçalho em caixa alta, borda entre linhas, padding de 20px). Ou seja, basta trocar o conteúdo do campo de especificações da imagem para a tabela abaixo. Não precisa mexer em código.

### Vergalhão SI50 — HTML pronto

Transcrito da imagem `SI-50.png`, com o erro de grafia corrigido ("escoamento", e não "escoamaneto") e a unidade padronizada (MPa nos dois casos, a imagem escrevia "Mpa" em um deles).

```html
<table>
  <thead>
    <tr>
      <th>Diâmetro nominal (Ø)<br><small>mm</small></th>
      <th>Massa linear nominal<br><small>kg/m</small></th>
      <th>Limite de escoamento (LE mín.)<br><small>MPa</small></th>
      <th>Limite de resistência (LR mín.)<br><small>MPa</small></th>
      <th>Alongamento LO = 10 x Ø<br><small>% mínimo</small></th>
      <th>Dobramento a 180° (diâmetro do pino)<br><small>mm</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>6,3</td><td>0,245</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>8,0</td><td>0,395</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>10,0</td><td>0,617</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>12,5</td><td>0,963</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>16,0</td><td>1,578</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>20,0</td><td>2,466</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>6 x Ø</td></tr>
    <tr><td>25,0</td><td>3,853</td><td>500</td><td>1,08 x LE</td><td>8,0</td><td>6 x Ø</td></tr>
  </tbody>
</table>
<p><small>Disponível em feixes (reto ou dobrado) e em rolos. Consultar disponibilidade.<br>
Pode haver variação de peso nominal de até ±6%. Produto conforme a NBR 7480:2024.</small></p>
```

### Situação das fichas nos 39 produtos do catálogo

| Situação | Quantidade |
|---|---|
| Ficha em imagem, precisa virar tabela | 22 |
| Sem ficha técnica nenhuma | 15 |
| Já em tabela HTML | 0 |

**Com ficha em imagem:** ca60-bobina, si50-bobina, si50, si60-spooler, telas-e-malhas, arame-recozido, tela-coluna, trelica, si-60, fio-maquina, si50-spooler, barra-porta-2, caixilho, perfil-u-enrijecido, perfil-u-simples, barra-redonda, cantoneira, bobina-inox, cumeeira, telha-ondulada, telha-trapezoidal, metalon-retangular.

**Três dessas fichas são print de tela** (item 92), o que é o pior caso porque nem a imagem tem qualidade: `si50-bobina`, `cumeeira` e `telha-trapezoidal` usam arquivos com nome "Captura-de-tela-2025-...".

**Sem ficha nenhuma (item 90):** corte-e-dobra, telas-e-malhas, tela-coluna, si50-spooler, chapa-articulada, lambril-baguetado, lambril-ondulado, telha-trapezoidal, perfil-para-porta-automatica, chapa-galvanizada, chapa-fina-fria, chapa-fina-quente, bobina-slitada, bobininha, metalon-retangular.

Sugestão de ordem de conversão, pelos produtos que a campanha 2026 mais empurra: SI50, Vergalhão SI 60, Telas e Malhas, Corte e Dobra, Telha Trapezoidal, Telha Ondulada, Tubos e Metalons.

---

## 2. Quatro produtos órfãos (item 91)

Estão publicados, estão no sitemap e o Google indexa, mas não aparecem em nenhuma categoria do catálogo:

- `/produtos/bobina-zincalume/`
- `/produtos/bobina-galvanizada/`
- `/produtos/bobina-fina-frio/`
- `/produtos/bobina-fina-quente/`

Quem chega por busca encontra o produto, mas quem navega pelo site nunca chega até ele. Decidir com o cliente: entram em Planos e Derivados ou saem do ar.

---

## 3. Página do produto Chapa Xadrez (item 1)

O banner do hero anuncia o lançamento e não existe página. Rascunho pronto, no tom verbal da marca Aço Cearense (tagline "Qualidade que constrói confiança").

- **Título:** Chapa Xadrez
- **Categoria:** Planos e Derivados
- **Marca:** Aço Cearense
- **Resumo (o texto curto do card):** Chapa de aço com relevo antiderrapante, indicada para pisos, degraus, rampas e estruturas que exigem segurança no piso.
- **Descrição:**

> A Chapa Xadrez é produzida com relevo em losango, que garante aderência e reduz o risco de escorregamento em pisos, degraus, plataformas e rampas.
>
> Une resistência mecânica e acabamento uniforme, o que a torna indicada tanto para uso industrial quanto para estruturas metálicas, mezaninos e áreas de circulação.
>
> Disponível nas espessuras 2,65 mm, 3,00 mm e 4,75 mm.

- **Especificações:** tabela com espessura, largura, comprimento e peso por chapa. **Preciso desses dados com o time técnico**, porque o banner só informa as três espessuras. Não vou inventar largura, comprimento nem norma.
- **Imagem:** ideal usar a foto oficial do produto no mesmo padrão dos outros 39 (fundo branco). A arte do banner serve de referência mas não substitui o packshot.
- **Depois de publicar:** apontar o slide do hero para `/produtos/chapa-xadrez/` em vez de `/orcamento`.

---

## 4. CSS de mobile (itens 61, 62 e 5)

WPCode > novo snippet CSS > Site Wide Header > nome sugerido: `GAC — ajustes mobile`

A estrutura da página de produto é `.product-detail > .container.swiper-gallery` em flex row wrap, com a galeria antes do conteúdo. Por isso, no celular, o nome do produto e o breadcrumb ficam abaixo da dobra.

```css
@media (max-width: 767px) {
  /* Item 61 e 62: conteúdo (nome, marca, CTA) antes da imagem no celular */
  .product-detail .swiper-gallery .products-item { order: -1; }

  /* A imagem deixa de comer a tela inteira */
  .product-detail .swiper-slide img { max-height: 40vh; object-fit: contain; }

  /* Item 5: os números da home não ficam mais cortados pelo header fixo */
  .number-counter-container-value { scroll-margin-top: 90px; }
}
```

---

## 5. Banner de cookies (itens 59, 60 e 71)

O CMP é o **Privally** (`#oPrivallyApp-OptionBar`). O ajuste deve ser feito no painel do Privally, não por CSS, porque alterar o layout do banner por fora pode comprometer o registro de consentimento.

O que pedir lá:
1. Layout do banner no mobile empilhado, um botão por linha, sem sobreposição.
2. "Rejeitar todos" com o mesmo peso visual do "Aceitar todos".
3. Banner não pode capturar cliques do conteúdo abaixo dele.

Teste de aceite: no celular, conseguir recusar os cookies no primeiro toque e, com o banner aberto, conseguir abrir as especificações técnicas de um produto.
