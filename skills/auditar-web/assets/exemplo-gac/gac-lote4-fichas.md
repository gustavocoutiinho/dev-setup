# Lote 4 — mais nove fichas técnicas em HTML

Transcritas em 18/08/2026. Vão direto no campo de especificações do produto, substituindo a imagem.
Com estas, **15 dos 22 produtos** que têm ficha em imagem já estão convertidos.

---

## Telha Trapezoidal (`/produtos/telha-trapezoidal/`)

Hoje é um print de planilha. Colunas de peso vazias na origem.

```html
<table>
  <thead>
    <tr>
      <th>Largura útil<br><small>mm</small></th>
      <th>Largura da crista<br><small>mm</small></th>
      <th>Altura<br><small>mm</small></th>
      <th>Passo<br><small>mm</small></th>
      <th>Canal<br><small>mm</small></th>
      <th>Espessura<br><small>mm</small></th>
      <th>Tipo</th>
      <th>Comprimento<br><small>m</small></th>
      <th>Massa linear<br><small>kg/m</small></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1040</td><td>32</td><td>40</td><td>197</td><td>95</td><td>0,40</td><td>CC / GA</td><td>Limite máx. 12 m</td><td>3,770</td></tr>
    <tr><td>1040</td><td>32</td><td>40</td><td>197</td><td>95</td><td>0,43</td><td>CC / GA</td><td>Limite máx. 12 m</td><td>4,050</td></tr>
    <tr><td>1040</td><td>32</td><td>40</td><td>197</td><td>95</td><td>0,47</td><td>CC / GA</td><td>Limite máx. 12 m</td><td>4,430</td></tr>
  </tbody>
</table>
<p><small>CC: chapa comum. GA: galvanizada. Peso sob consulta.</small></p>
```

## Caixilho (`/produtos/caixilho/`)

```html
<table>
  <thead>
    <tr><th>Espessura (e)<br><small>mm</small></th><th>Tipo</th><th>Largura (b)<br><small>mm</small></th><th>Altura (h)<br><small>mm</small></th><th>Comprimento<br><small>mm</small></th><th>Massa linear<br><small>kg/m</small></th><th>Embalagem<br><small>unid.</small></th><th>Peso<br><small>kg</small></th></tr>
  </thead>
  <tbody>
    <tr><td>1,20</td><td>Fina a frio</td><td>26</td><td>28</td><td>6.000</td><td>0,700</td><td>198</td><td>832</td></tr>
    <tr><td>1,25</td><td>Galvanizado</td><td>26</td><td>28</td><td>6.000</td><td>1,050</td><td>120</td><td>756</td></tr>
    <tr><td>1,50</td><td>Fina a frio</td><td>26</td><td>28</td><td>6.000</td><td>1,270</td><td>120</td><td>914</td></tr>
    <tr><td>1,55</td><td>Galvanizado</td><td>26</td><td>28</td><td>6.000</td><td>1,310</td><td>120</td><td>943</td></tr>
  </tbody>
</table>
<p><small>Pode haver variação de peso nominal de ±5% a ±6%.</small></p>
```

## Barra Redonda (`/produtos/barra-redonda/`)

```html
<table>
  <thead>
    <tr><th>Bitola<br><small>pol.</small></th><th>Bitola<br><small>mm</small></th><th>Comprimento<br><small>mm</small></th><th>Massa linear<br><small>kg/m</small></th></tr>
  </thead>
  <tbody>
    <tr><td>1/4"</td><td>6,35</td><td>6.000</td><td>0,249</td></tr>
    <tr><td>5/16"</td><td>7,94</td><td>6.000</td><td>0,395</td></tr>
    <tr><td>3/8"</td><td>9,53</td><td>6.000</td><td>0,499</td></tr>
    <tr><td>7/16"</td><td>11,11</td><td>6.000</td><td>0,746</td></tr>
    <tr><td>1/2"</td><td>12,70</td><td>6.000</td><td>0,994</td></tr>
    <tr><td>5/8"</td><td>15,88</td><td>6.000</td><td>1,555</td></tr>
    <tr><td>11/16"</td><td>17,46</td><td>6.000</td><td>1,880</td></tr>
    <tr><td>3/4"</td><td>19,05</td><td>6.000</td><td>2,237</td></tr>
    <tr><td>1"</td><td>25,40</td><td>6.000</td><td>3,980</td></tr>
  </tbody>
</table>
<p><small>Peso da embalagem sob consulta. Pode haver variação de peso nominal de ±5% a ±6%.</small></p>
```

## Cantoneira (`/produtos/cantoneira/`)

```html
<table>
  <thead>
    <tr><th>Largura da aba (b)<br><small>pol.</small></th><th>Largura da aba (b)<br><small>mm</small></th><th>Espessura (e)<br><small>pol.</small></th><th>Espessura (e)<br><small>mm</small></th><th>Massa linear<br><small>kg/m</small></th></tr>
  </thead>
  <tbody>
    <tr><td>5/8"</td><td>15,87</td><td>1/8"</td><td>3,18</td><td>0,71</td></tr>
    <tr><td>3/4"</td><td>19,05</td><td>1/8"</td><td>3,18</td><td>0,87</td></tr>
    <tr><td>7/8"</td><td>22,22</td><td>1/8"</td><td>3,18</td><td>1,04</td></tr>
    <tr><td>1"</td><td>25,40</td><td>1/8"</td><td>3,18</td><td>1,19</td></tr>
    <tr><td>1.1/4"</td><td>31,75</td><td>1/8"</td><td>3,18</td><td>1,53</td></tr>
    <tr><td>1.1/2"</td><td>38,10</td><td>1/8"</td><td>3,18</td><td>1,84</td></tr>
    <tr><td>2"</td><td>50,80</td><td>1/8"</td><td>3,18</td><td>2,46</td></tr>
    <tr><td>1"</td><td>25,40</td><td>3/16"</td><td>4,76</td><td>1,73</td></tr>
    <tr><td>1.1/4"</td><td>31,75</td><td>3/16"</td><td>4,76</td><td>2,22</td></tr>
    <tr><td>1.1/2"</td><td>38,10</td><td>3/16"</td><td>4,76</td><td>2,69</td></tr>
    <tr><td>2"</td><td>50,80</td><td>3/16"</td><td>4,76</td><td>3,63</td></tr>
    <tr><td>1"</td><td>25,40</td><td>1/4"</td><td>6,35</td><td>2,22</td></tr>
    <tr><td>1.1/4"</td><td>31,75</td><td>1/4"</td><td>6,35</td><td>2,86</td></tr>
    <tr><td>1.1/2"</td><td>38,10</td><td>1/4"</td><td>6,35</td><td>3,50</td></tr>
    <tr><td>2"</td><td>50,80</td><td>1/4"</td><td>6,35</td><td>4,75</td></tr>
    <tr><td>2.1/2"</td><td>63,50</td><td>1/4"</td><td>6,35</td><td>6,01</td></tr>
    <tr><td>3"</td><td>76,20</td><td>1/4"</td><td>6,35</td><td>7,28</td></tr>
    <tr><td>2.1/2"</td><td>63,50</td><td>5/16"</td><td>7,93</td><td>7,42</td></tr>
    <tr><td>3"</td><td>76,20</td><td>5/16"</td><td>7,93</td><td>9,00</td></tr>
    <tr><td>4"</td><td>101,60</td><td>5/16"</td><td>7,93</td><td>12,17</td></tr>
    <tr><td>3"</td><td>76,20</td><td>3/8"</td><td>9,52</td><td>10,68</td></tr>
    <tr><td>4"</td><td>101,60</td><td>3/8"</td><td>9,52</td><td>14,48</td></tr>
  </tbody>
</table>
<p><small>Comprimento padrão de 6.000 mm. Pode haver variação de peso nominal de ±5% a ±6%.</small></p>
```

**Atenção nesta:** na imagem original, duas linhas de espessura 7,93 mm aparecem como **1/16"**, o que está errado, porque 1/16" equivale a 1,59 mm. Corrigi para **5/16"**, que é o valor coerente com 7,93 mm. Uma linha também trazia a largura de 4" como 101,80 mm em vez de 101,60 mm. **Confirmar com o time técnico.**

## Arame Recozido (`/produtos/arame-recozido/`)

```html
<table>
  <thead>
    <tr><th>Diâmetro<br><small>BWG</small></th><th>Diâmetro nominal<br><small>mm</small></th><th>Ovalização máxima<br><small>mm</small></th><th>Massa linear nominal<br><small>kg/m</small></th><th>Limite de resistência à tração<br><small>MPa</small></th><th>Peso por rolo<br><small>kg</small></th><th>Peso da embalagem<br><small>kg</small></th><th>Peso do palete<br><small>kg</small></th></tr>
  </thead>
  <tbody>
    <tr><td>18</td><td>1,25</td><td>0,04</td><td>0,01</td><td>550</td><td>1</td><td>20</td><td>1.000</td></tr>
    <tr><td>18</td><td>1,25</td><td>0,04</td><td>0,01</td><td>550</td><td>35</td><td>35</td><td>1.260</td></tr>
  </tbody>
</table>
<p><small>Outras opções de embalagem sob consulta. Pode haver variação de peso nominal de até ±6%.</small></p>
```

## Fio Máquina (`/produtos/fio-maquina/`)

```html
<table>
  <thead>
    <tr>
      <th rowspan="2">Bitola<br><small>mm</small></th>
      <th colspan="3">Diâmetro<br><small>mm</small></th>
      <th rowspan="2">Ovalização máxima<br><small>mm</small></th>
      <th colspan="3">Massa linear<br><small>kg/m</small></th>
    </tr>
    <tr><th>Nominal</th><th>Mínimo</th><th>Máximo</th><th>Nominal</th><th>Mínima</th><th>Máxima</th></tr>
  </thead>
  <tbody>
    <tr><td>5,5</td><td>5,5</td><td>5,2</td><td>5,8</td><td>0,50</td><td>0,186</td><td>0,168</td><td>0,196</td></tr>
    <tr><td>6,3</td><td>6,3</td><td>6,0</td><td>6,6</td><td>0,50</td><td>0,245</td><td>0,221</td><td>0,257</td></tr>
    <tr><td>6,5</td><td>6,5</td><td>6,2</td><td>6,8</td><td>0,50</td><td>0,260</td><td>0,234</td><td>0,273</td></tr>
    <tr><td>7,0</td><td>7,0</td><td>6,7</td><td>7,3</td><td>0,50</td><td>0,302</td><td>0,272</td><td>0,317</td></tr>
    <tr><td>8,0</td><td>8,0</td><td>7,7</td><td>8,3</td><td>0,50</td><td>0,395</td><td>0,356</td><td>0,415</td></tr>
    <tr><td>9,0</td><td>9,0</td><td>8,6</td><td>9,4</td><td>0,65</td><td>0,499</td><td>0,449</td><td>0,524</td></tr>
    <tr><td>9,5</td><td>9,5</td><td>9,1</td><td>9,9</td><td>0,65</td><td>0,556</td><td>0,500</td><td>0,584</td></tr>
    <tr><td>10,0</td><td>10,0</td><td>9,6</td><td>10,4</td><td>0,65</td><td>0,617</td><td>0,555</td><td>0,648</td></tr>
    <tr><td>12,0</td><td>12,0</td><td>11,6</td><td>12,4</td><td>0,65</td><td>0,888</td><td>0,799</td><td>0,932</td></tr>
    <tr><td>12,5</td><td>12,5</td><td>12,1</td><td>12,9</td><td>0,65</td><td>0,963</td><td>0,867</td><td>1,011</td></tr>
  </tbody>
</table>
<p><small>Pode haver variação de peso nominal de até ±6%.</small></p>
```

**Atenção:** na imagem, as três últimas colunas estão rotuladas como "diâmetro (mm)", mas os valores são de **massa linear em kg/m**. Corrigido acima.

## Tela para Coluna (`/produtos/tela-coluna/`)

```html
<table>
  <thead>
    <tr>
      <th rowspan="2">Tela para coluna</th>
      <th colspan="2">Barra longitudinal (Vergalhão SI50)</th>
      <th>Fio transversal (SI60)</th>
      <th colspan="3">Dimensões do estribo<br><small>cm</small></th>
      <th rowspan="2">Peças por fardo<br><small>unid.</small></th>
      <th rowspan="2">Peso por peça<br><small>kg</small></th>
    </tr>
    <tr><th>Bitola<br><small>mm</small></th><th>Comprimento<br><small>m</small></th><th>Bitola<br><small>mm</small></th><th>Largura</th><th>Comprimento</th><th>Espaçamento</th></tr>
  </thead>
  <tbody>
    <tr><td>8,0 mm (7x14) 3,5 m</td><td>8,0</td><td>3,5</td><td>4,20</td><td>7</td><td>14</td><td>20</td><td>50</td><td>6,4</td></tr>
    <tr><td>8,0 mm (7x17) 3,5 m</td><td>8,0</td><td>3,5</td><td>4,20</td><td>7</td><td>17</td><td>20</td><td>50</td><td>7,2</td></tr>
    <tr><td>8,0 mm (7x14) 4 m</td><td>8,0</td><td>4,0</td><td>4,20</td><td>7</td><td>20</td><td>20</td><td>50</td><td>7,4</td></tr>
    <tr><td>8,0 mm (7x17) 4 m</td><td>8,0</td><td>4,0</td><td>4,20</td><td>7</td><td>27</td><td>20</td><td>50</td><td>7,2</td></tr>
    <tr><td>10,0 mm (7x14) 3,5 m</td><td>10,0</td><td>3,5</td><td>4,20</td><td>7</td><td>14</td><td>20</td><td>50</td><td>9,4</td></tr>
    <tr><td>10,0 mm (7x17) 3,5 m</td><td>10,0</td><td>3,5</td><td>4,20</td><td>7</td><td>17</td><td>20</td><td>50</td><td>9,5</td></tr>
    <tr><td>10,0 mm (7x14) 4 m</td><td>10,0</td><td>4,0</td><td>4,20</td><td>7</td><td>20</td><td>20</td><td>50</td><td>10,8</td></tr>
    <tr><td>10,0 mm (7x17) 4 m</td><td>10,0</td><td>4,0</td><td>4,20</td><td>7</td><td>27</td><td>20</td><td>50</td><td>10,9</td></tr>
    <tr><td>8,0 mm (7x14) 6 m</td><td>8,0</td><td>6,0</td><td>4,20</td><td>7</td><td>27</td><td>20</td><td>50</td><td>10,9</td></tr>
    <tr><td>8,0 mm (7x17) 6 m</td><td>8,0</td><td>6,0</td><td>4,20</td><td>7</td><td>14</td><td>20</td><td>50</td><td>11,0</td></tr>
    <tr><td>8,0 mm (6x20) 6 m</td><td>8,0</td><td>6,0</td><td>4,20</td><td>6</td><td>17</td><td>20</td><td>50</td><td>11,2</td></tr>
    <tr><td>8,0 mm (7x27) 6 m</td><td>8,0</td><td>6,0</td><td>4,20</td><td>7</td><td>20</td><td>20</td><td>50</td><td>16,8</td></tr>
    <tr><td>8,0 mm (6x20) 6 m</td><td>8,0</td><td>6,0</td><td>4,20</td><td>7</td><td>27</td><td>20</td><td>50</td><td>11,3</td></tr>
    <tr><td>10,0 mm (7x14) 6 m</td><td>10,0</td><td>6,0</td><td>4,20</td><td>7</td><td>20</td><td>20</td><td>50</td><td>16,2</td></tr>
    <tr><td>10,0 mm (7x17) 6 m</td><td>10,0</td><td>6,0</td><td>4,20</td><td>7</td><td>27</td><td>20</td><td>50</td><td>16,4</td></tr>
    <tr><td>10,0 mm (7x20) 6 m</td><td>10,0</td><td>6,0</td><td>4,20</td><td>7</td><td>20</td><td>20</td><td>50</td><td>16,1</td></tr>
    <tr><td>10,0 mm (7x27) 6 m</td><td>10,0</td><td>6,0</td><td>4,20</td><td>7</td><td>27</td><td>20</td><td>50</td><td>16,5</td></tr>
  </tbody>
</table>
<p><small>Dimensões especiais sob consulta. Pode haver variação de peso nominal de até ±6%.</small></p>
```

**Atenção:** o nome da linha e as dimensões do estribo se contradizem em várias linhas. Por exemplo, "8,0 mm (7x14) 6 m" aparece com comprimento de estribo 27, e "8,0 mm (7x17) 6 m" com 14. Há também duas linhas "8,0 mm (6x20) 6 m" com valores diferentes. **Transcrevi fielmente, mas isso precisa de revisão do time técnico antes de publicar.**

## Vergalhão SI 50 Spooler (`/produtos/si50-spooler/`)

```html
<table>
  <thead>
    <tr><th>Diâmetro nominal (Ø)<br><small>mm</small></th><th>Massa linear nominal<br><small>kg/m</small></th><th>Tolerância de massa<br><small>%</small></th><th>Limite de escoamento (LE mín.)<br><small>MPa</small></th><th>Limite de resistência (LR mín.)<br><small>MPa</small></th><th>Alongamento LO = 10 x Ø<br><small>% mínimo</small></th><th>Dobramento a 180°<br><small>mm</small></th></tr>
  </thead>
  <tbody>
    <tr><td>10,0</td><td>0,617</td><td>± 6</td><td>500</td><td>540</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>12,5</td><td>0,963</td><td>± 6</td><td>500</td><td>540</td><td>8,0</td><td>3 x Ø</td></tr>
    <tr><td>16,0</td><td>1,578</td><td>± 5</td><td>500</td><td>540</td><td>8,0</td><td>3 x Ø</td></tr>
  </tbody>
</table>
<p><small>Disponível em spooler de 1.500 kg e 2.300 kg. Pode haver variação de peso nominal de até ±6%.</small></p>
```

## Vergalhão SI 60 Spooler (`/produtos/si60-spooler/`)

```html
<table>
  <thead>
    <tr><th>Diâmetro nominal (Ø)<br><small>mm</small></th><th>Massa linear nominal<br><small>kg/m</small></th><th>Tolerância de massa<br><small>%</small></th><th>Limite de escoamento (LE mín.)<br><small>MPa</small></th><th>Limite de resistência (LR mín.)</th><th>Alongamento LO = 10 x Ø<br><small>% mínimo</small></th><th>Dobramento a 180°<br><small>mm</small></th></tr>
  </thead>
  <tbody>
    <tr><td>3,40</td><td>0,071</td><td>± 6</td><td>600</td><td>1,05 x LE</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>3,80</td><td>0,089</td><td>± 6</td><td>600</td><td>1,05 x LE</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>4,20</td><td>0,109</td><td>± 6</td><td>600</td><td>1,05 x LE</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>5,00</td><td>0,154</td><td>± 6</td><td>600</td><td>1,05 x LE</td><td>5,0</td><td>5 x Ø</td></tr>
    <tr><td>6,00</td><td>0,222</td><td>± 6</td><td>600</td><td>1,05 x LE</td><td>5,0</td><td>5 x Ø</td></tr>
  </tbody>
</table>
<p><small>Disponível em rolos de 200 kg, 500 kg e 1.000 kg, e em spooler de 750 kg, 1.000 kg e 2.000 kg.</small></p>
```

---

## Sete fichas que eu não transcrevo por imagem, e por quê

Estas têm entre 30 e 60 linhas em corpo muito pequeno dentro do PNG. Transcrever bitola de tubo ou de perfil a partir de imagem comprimida tem risco real de erro, e erro de bitola em ficha de aço é grave.

| Produto | Tamanho da imagem | O que peço |
|---|---|---|
| Metalon Retangular | 1160 x 2949 px, ~60 linhas | Planilha original |
| Bobina e Slitter Inox | 1160 x 2415 px, ~60 linhas | Planilha original |
| Perfil U Simples | ~34 linhas | Planilha original |
| Perfil U Enrijecido | ~30 linhas | Planilha original |
| SI50 Bobina | print de tela | Planilha original |
| Cumeeira | print de tela | Planilha original |
| Barra Porta | não avaliada nesta rodada | Planilha original |

Com a planilha em mãos eu converto as sete em minutos, sem risco de transcrição.

---

## Erros técnicos encontrados até agora (item 93 da planilha)

1. **SI50:** cabeçalho "ESCOAMANETO" e unidade escrita "MPa" numa coluna e "Mpa" na outra.
2. **SI50 Spooler:** o mesmo "ESCOAMANETO", e a tabela de embalagem traz "peso" com unidade **mm** e "comprimento" com **kg/m**, invertidos.
3. **SI60 Spooler:** mesma inversão de peso e comprimento.
4. **Telha Ondulada:** massa linear em **mm** e comprimento em **unid.**, arquivo nomeado "Tela" em vez de "Telha", coluna de peso com traços.
5. **Treliça:** banzo inferior em **m** e peças por fardo em **mm**. Primeira tabela sem título.
6. **Vergalhão SI 60:** ficha salva como `AC-60.png`, contendo duas tabelas.
7. **CA 60 Bobina:** imagem em 650x308 px, ilegível ampliada.
8. **Cantoneira:** duas linhas com espessura **1/16"** onde o valor em mm (7,93) indica **5/16"**, e largura de 4" como 101,80 mm em vez de 101,60 mm.
9. **Fio Máquina:** três colunas de **massa linear** rotuladas como "diâmetro".
10. **Arame Recozido:** cabeçalho "LIMETE DE RESISTÊNCIA", e as duas linhas são idênticas em bitola, mudando só a embalagem.
11. **Tela para Coluna:** nome da linha e dimensões do estribo se contradizem em várias linhas, e há duas linhas "8,0 mm (6x20) 6 m" com valores diferentes.

Nada disso é visível hoje porque o dado está preso dentro de imagem. Ao virar tabela, o conteúdo passa a ser revisável, pesquisável e lido por leitor de tela.
