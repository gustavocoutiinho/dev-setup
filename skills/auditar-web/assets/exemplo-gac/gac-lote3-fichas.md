# Lote 3 — fichas técnicas convertidas em tabela HTML

Transcritas das imagens originais em 18/08/2026. Cada bloco vai direto no campo de especificações técnicas do produto no WordPress, substituindo a imagem.
O tema já estiliza `.technical-specifications table`, então não precisa de CSS novo.

**Importante:** as transcrições corrigem erros que estão nas imagens originais. Os erros estão listados no fim deste arquivo, para o time técnico validar antes de publicar.

---

## 1. Vergalhão SI 60 (`/produtos/si-60/`)

A imagem traz duas tabelas, uma do SI 60 e outra do AC 60.

```html
<h3>Vergalhão SI 60</h3>
<table>
  <thead>
    <tr>
      <th>Diâmetro nominal (Ø)<br><small>mm</small></th>
      <th>Massa linear nominal<br><small>kg/m</small></th>
      <th>Tolerância de massa<br><small>%</small></th>
      <th>Limite de escoamento (LE mín.)<br><small>MPa</small></th>
      <th>Limite de resistência (LR mín.)<br><small>MPa</small></th>
      <th>Relação elástica mínima (LR/LE)</th>
      <th>Alongamento mínimo LO = 10 x Ø<br><small>%</small></th>
      <th>Dobramento a 180° (diâmetro do pino)<br><small>mm</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>3,4</td><td>0,071</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>4,2</td><td>0,109</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>5,0</td><td>0,154</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>6,0</td><td>0,222</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
  </tbody>
</table>

<h3>Vergalhão AC 60</h3>
<table>
  <thead>
    <tr>
      <th>Diâmetro nominal (Ø)<br><small>mm</small></th>
      <th>Massa linear nominal<br><small>kg/m</small></th>
      <th>Tolerância de massa<br><small>%</small></th>
      <th>Limite de escoamento (LE mín.)<br><small>MPa</small></th>
      <th>Limite de resistência (LR mín.)<br><small>MPa</small></th>
      <th>Relação elástica mínima (LR/LE)</th>
      <th>Alongamento mínimo LO = 10 x Ø<br><small>%</small></th>
      <th>Dobramento a 180° (diâmetro do pino)<br><small>mm</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>3,4</td><td>0,071</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>3,8</td><td>0,089</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>4,2</td><td>0,109</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>5,0</td><td>0,154</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>6,0</td><td>0,222</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
  </tbody>
</table>
```

---

## 2. CA 60 Bobina (`/produtos/ca60-bobina/`)

```html
<table>
  <thead>
    <tr>
      <th>Diâmetro nominal (Ø)<br><small>mm</small></th>
      <th>Massa linear nominal<br><small>kg/m</small></th>
      <th>Tolerância de massa<br><small>%</small></th>
      <th>Limite de escoamento (LE mín.)<br><small>MPa</small></th>
      <th>Limite de resistência (LR mín.)<br><small>MPa</small></th>
      <th>Relação elástica mínima (LR/LE)</th>
      <th>Alongamento mínimo LO = 10 x Ø<br><small>%</small></th>
      <th>Dobramento a 180° (diâmetro do pino)<br><small>mm</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>3,4</td><td>0,071</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>3,8</td><td>0,089</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>4,2</td><td>0,109</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>5,0</td><td>0,154</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>6,0</td><td>0,222</td><td>± 6</td><td>600</td><td>660</td><td>1,05</td><td>5,0</td><td>5 x Ø</td></tr>
  </tbody>
</table>
<p><small>Disponível em bobinas de 750 kg, 1.000 kg e 2.000 kg. Consulte disponibilidade.</small></p>
```

---

## 3. Telas e Malhas (`/produtos/telas-e-malhas/`)

```html
<table>
  <thead>
    <tr>
      <th rowspan="2">Malhas eletrosoldadas</th>
      <th colspan="2">Espaçamento entre fios<br><small>mm</small></th>
      <th colspan="2">Diâmetro<br><small>mm</small></th>
      <th colspan="2">Dimensões<br><small>m</small></th>
      <th colspan="2">Franja<br><small>mm</small></th>
      <th rowspan="2">Embalagem<br><small>unid.</small></th>
      <th rowspan="2">Peso do fardo<br><small>kg</small></th>
    </tr>
    <tr>
      <th>Longitudinal</th><th>Transversal</th>
      <th>Longitudinal</th><th>Transversal</th>
      <th>Largura</th><th>Comprimento</th>
      <th>Longitudinal</th><th>Transversal</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Malha Leve (EQ45)</td><td>200</td><td>200</td><td>3,4</td><td>3,4</td><td>2</td><td>3</td><td>100</td><td>100</td><td>50</td><td>215</td></tr>
    <tr><td>Malha Média (EQ61)</td><td>150</td><td>150</td><td>3,4</td><td>3,4</td><td>2</td><td>3</td><td>75</td><td>25</td><td>50</td><td>290</td></tr>
    <tr><td>Malha Reforçada (EQ92)</td><td>150</td><td>150</td><td>4,2</td><td>4,2</td><td>2</td><td>3</td><td>75</td><td>25</td><td>50</td><td>445</td></tr>
    <tr><td>Malha Pesada (EQ138)</td><td>100</td><td>100</td><td>4,2</td><td>4,2</td><td>2</td><td>3</td><td>50</td><td>50</td><td>50</td><td>655</td></tr>
    <tr><td>Q61</td><td>150</td><td>150</td><td>3,4</td><td>3,4</td><td>2,45</td><td>6</td><td>75</td><td>25</td><td>25/50</td><td>375,5 / 715</td></tr>
    <tr><td>Q75</td><td>150</td><td>150</td><td>3,8</td><td>3,8</td><td>2,45</td><td>6</td><td>75</td><td>25</td><td>25/50</td><td>890</td></tr>
    <tr><td>Q92</td><td>150</td><td>150</td><td>4,2</td><td>4,2</td><td>2,45</td><td>6</td><td>75</td><td>25</td><td>25/50</td><td>545 / 1090</td></tr>
    <tr><td>Q113</td><td>100</td><td>100</td><td>3,8</td><td>3,8</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>25/50</td><td>662,5 / 1325</td></tr>
    <tr><td>Q138</td><td>100</td><td>100</td><td>4,2</td><td>4,2</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>25/50</td><td>807,5 / 1615</td></tr>
    <tr><td>Q166</td><td>100</td><td>100</td><td>4,6</td><td>4,6</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>25</td><td>967,5</td></tr>
    <tr><td>Q196</td><td>100</td><td>100</td><td>5,0</td><td>5,0</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>25</td><td>1.142,5</td></tr>
    <tr><td>Q238</td><td>100</td><td>100</td><td>5,5</td><td>5,5</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>25</td><td>1.383</td></tr>
    <tr><td>Q283</td><td>100</td><td>100</td><td>6,0</td><td>6,0</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>25</td><td>1.648</td></tr>
    <tr><td>Q385</td><td>100</td><td>100</td><td>7,0</td><td>7,0</td><td>2,45</td><td>6</td><td>50</td><td>25</td><td>15</td><td>1.344</td></tr>
  </tbody>
</table>
<p><small>Outras opções de dimensões sob consulta.<br>
As telas e malhas Q166, Q238 e Q385 não utilizam SI 60 no processo de fabricação.</small></p>
```

---

## 4. Telha Ondulada (`/produtos/telha-ondulada/`)

```html
<table>
  <thead>
    <tr>
      <th>Largura útil<br><small>mm</small></th>
      <th>Altura<br><small>mm</small></th>
      <th>Passo<br><small>mm</small></th>
      <th>Espessura (e)<br><small>mm</small></th>
      <th>Tipo</th>
      <th>Comprimento<br><small>m</small></th>
      <th>Massa linear<br><small>kg/m</small></th>
      <th>Peso</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1125</td><td>17</td><td>78</td><td>0,40</td><td>CC, GA</td><td>Limite máx. 12 m</td><td>3,77</td><td>Sob consulta</td></tr>
    <tr><td>1125</td><td>17</td><td>78</td><td>0,43</td><td>CC, GA</td><td>Limite máx. 12 m</td><td>4,05</td><td>Sob consulta</td></tr>
    <tr><td>1125</td><td>17</td><td>78</td><td>0,47</td><td>CC, GA</td><td>Limite máx. 12 m</td><td>4,43</td><td>Sob consulta</td></tr>
  </tbody>
</table>
<p><small>CC: chapa comum. GA: galvanizada. Pode haver variação de peso nominal de ±5% a ±6%.</small></p>
```

---

## 5. Treliça (`/produtos/trelica/`)

A imagem traz duas tabelas. A segunda é identificada como AC 60 e a primeira está sem título, presumivelmente a linha SI. **Confirmar com o time técnico antes de publicar.**

```html
<h3>Treliça SI</h3>
<table>
  <thead>
    <tr>
      <th>Designação NBR 14859-3</th>
      <th>Código</th>
      <th>Altura (H)<br><small>mm</small></th>
      <th>Banzo superior (Ø)<br><small>mm</small></th>
      <th>Diagonal sinusóide (Ø)<br><small>mm</small></th>
      <th>Banzo inferior (Ø)<br><small>mm</small></th>
      <th>Peso linear<br><small>kg/m</small></th>
      <th>Peças por fardo<br><small>unid.</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>TR SI-8SL (Super Leve)</td><td>TR 8634</td><td>80</td><td>6,0</td><td>3,4</td><td>4,2</td><td>0,632</td><td>50-100</td></tr>
    <tr><td>TR-SI-8L (Pesada)</td><td>TR 8644</td><td>80</td><td>6,0</td><td>4,2</td><td>4,2</td><td>0,735</td><td>50-100</td></tr>
    <tr><td>TR-SI-8M</td><td>TR 8645</td><td>80</td><td>6,0</td><td>4,2</td><td>5,0</td><td>0,825</td><td>100</td></tr>
    <tr><td>TR-SI-12M</td><td>TR 12645</td><td>120</td><td>6,0</td><td>4,2</td><td>5,0</td><td>0,886</td><td>80</td></tr>
    <tr><td>TR-SI-12R</td><td>TR 12646</td><td>120</td><td>6,0</td><td>4,2</td><td>6,0</td><td>1,016</td><td>100</td></tr>
  </tbody>
</table>

<h3>Treliça AC 60</h3>
<table>
  <thead>
    <tr>
      <th>Designação NBR 14859-3</th>
      <th>Código</th>
      <th>Altura (H)<br><small>mm</small></th>
      <th>Banzo superior (Ø)<br><small>mm</small></th>
      <th>Diagonal sinusóide (Ø)<br><small>mm</small></th>
      <th>Banzo inferior (Ø)<br><small>mm</small></th>
      <th>Peso linear<br><small>kg/m</small></th>
      <th>Peças por fardo<br><small>unid.</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>TR SI-8SL (Super Leve)</td><td>TR 8634</td><td>80</td><td>6,0</td><td>3,4</td><td>4,2</td><td>0,632</td><td>50-100</td></tr>
    <tr><td>TR-SI-8LL (Leve)</td><td>TR 8634</td><td>80</td><td>6,0</td><td>3,8</td><td>4,2</td><td>0,660</td><td>50</td></tr>
    <tr><td>TR-SI-8L (Pesada)</td><td>TR 8644</td><td>80</td><td>6,0</td><td>4,2</td><td>4,2</td><td>0,735</td><td>50-100</td></tr>
    <tr><td>TR-SI-8M</td><td>TR 8645</td><td>80</td><td>6,0</td><td>4,2</td><td>5,0</td><td>0,825</td><td>100</td></tr>
    <tr><td>TR-SI-12M</td><td>TR 12645</td><td>120</td><td>6,0</td><td>4,2</td><td>5,0</td><td>0,886</td><td>80</td></tr>
    <tr><td>TR-SI-12R</td><td>TR 12646</td><td>120</td><td>6,0</td><td>4,2</td><td>6,0</td><td>1,016</td><td>100</td></tr>
  </tbody>
</table>
<p><small>Pode haver variação de peso nominal de até ±6%.</small></p>
```

---

## Erros encontrados nas fichas originais

Todos já corrigidos nas transcrições acima, mas precisam do aval do time técnico:

1. **SI-50.png:** cabeçalho escrito "LIMITE DE ESCOAMANETO" e a unidade aparece como "MPa" em uma coluna e "Mpa" na outra.
2. **Tela-Ondulada.png:** o arquivo do produto **Telha** Ondulada se chama "Tela". Na tabela, "massa linear" aparece com unidade **mm** (o correto é kg/m) e "comprimento" com unidade **unid.** (o correto é m). A coluna de peso está preenchida com traços.
3. **Trelica.png:** "banzo inferior" com unidade **m** (o correto é mm) e "peças/fardo" com unidade **mm** (o correto é unidades). A primeira tabela está sem título.
4. **AC-60.png:** é a ficha do produto **SI 60**, mas o arquivo tem nome de AC 60 e contém as duas tabelas. Vale checar se o mesmo conteúdo não está duplicado na página do CA 60.
5. **CA-60-Bobina.png:** a imagem tem só 650x308 px, então fica ilegível quando ampliada no celular.
6. **Três fichas são print de tela:** SI50 Bobina, Cumeeira e Telha Trapezoidal.

## Onde isso entra na planilha

Itens 24, 25, 26, 67, 90 e 92. As cinco fichas deste arquivo mais a do SI50 (lote 2) cobrem 6 dos 22 produtos que hoje têm ficha em imagem.
