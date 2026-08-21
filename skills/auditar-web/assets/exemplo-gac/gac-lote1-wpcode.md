# Lote 1 de correções — site Grupo Aço Cearense

Código pronto para colar no WPCode. Tudo testado na página real em 18/08/2026, com os seletores do tema "Aço Cearense".
Nada aqui edita o tema, então uma atualização do tema não derruba as correções, e é possível desligar tudo com um clique no WPCode.

Resolve os itens da planilha: 27, 32, 33, 41, 42, 43, 46, 47, 52, 57, 66, 68, 70 e 87 (parcial).

---

## Snippet 1 — CSS

WPCode > Add Snippet > Add Your Custom Code > tipo **CSS Snippet** > Location: **Site Wide Header** > nome sugerido: `GAC — contraste de botões (AA)`

```css
/* Itens 43, 52 e 68: #7DB5DA com texto branco dá ~2,2:1 e reprova AA.
   #102D69 é o mesmo azul do botão primário do header, com contraste ~12:1. */
.button.button-light-blue { background-color: #102D69; }
.button.button-light-blue:hover { background-color: #0B2A50; }

/* Mensagem de erro do formulário (item 70) */
.gac-erro { display:block; color:#C0392B; font-size:12px; margin-top:6px; }
.gac-invalido { border-color:#C0392B !important; }

/* Bloco do produto no orçamento (item 33) */
.gac-produto-selecionado{
  width:100%; background:#F5F5F5; border:1px solid #102D69; border-radius:12px;
  padding:16px 20px; margin:0 0 20px; font-size:14px; color:#102D69;
}
```

---

## Snippet 2 — JavaScript

WPCode > Add Snippet > Add Your Custom Code > tipo **JavaScript Snippet** > Location: **Site Wide Footer** > nome sugerido: `GAC — lote 1 UX`

```javascript
(function () {
  'use strict';
  var WHATS = '558540111616';

  function ready(fn){ if(document.readyState!=='loading'){fn();} else {document.addEventListener('DOMContentLoaded',fn);} }

  /* ---------- 1. Página de produto ---------- */
  function paginaProduto() {
    var h1 = document.querySelector('h1');
    if (!h1 || !/\/produtos\//.test(location.pathname)) return;
    var nome = h1.textContent.trim();
    var marcaEl = [].slice.call(document.querySelectorAll('p,span,div')).filter(function (e) {
      return e.children.length === 0 && /^Marca:/i.test(e.textContent.trim());
    })[0];
    var marca = marcaEl ? marcaEl.textContent.replace(/Marca:\s*/i, '').trim() : '';

    /* Item 33 e 87: leva o produto para o formulário de orçamento */
    [].slice.call(document.querySelectorAll('a[href*="/orcamento"]')).forEach(function (a) {
      if (a.closest('header') || a.closest('footer')) return;
      var u = new URL(a.href, location.origin);
      u.searchParams.set('produto', nome);
      if (marca) u.searchParams.set('marca', marca);
      a.href = u.toString();
    });

    /* Item 32: WhatsApp já abre falando do produto */
    var wa = document.querySelector('a[href*="wa.me"]');
    if (wa) {
      var msg = 'Olá! Tenho interesse no produto ' + nome + (marca ? ' (' + marca + ')' : '') + '. Pode me passar um orçamento?';
      wa.href = 'https://wa.me/' + WHATS + '?text=' + encodeURIComponent(msg);
    }

    /* Item 27: especificações técnicas abertas por padrão.
       O handler do tema está no span da seta, não no bloco inteiro. */
    var seta = document.querySelector('.technical-specifications-item-top span');
    var cont = document.querySelector('.technical-specifications-item-content');
    if (seta && cont && parseInt(getComputedStyle(cont).height, 10) === 0) seta.click();
  }

  /* ---------- 2. Formulário de orçamento ---------- */
  function orcamento() {
    var f = document.getElementById('orcamento');
    if (!f) return;

    /* Item 42 e 66: o campo Rua não tem id nem label associado */
    var street = f.querySelector('[name="street"]');
    if (street && !street.id) {
      street.id = 'street';
      var lb = street.parentNode.querySelector('label');
      if (lb && !lb.getAttribute('for')) lb.setAttribute('for', 'street');
    }

    /* Item 33: mostra o produto escolhido e leva junto na mensagem */
    var qs = new URLSearchParams(location.search);
    var produto = qs.get('produto'), marca = qs.get('marca');
    var msg = f.querySelector('[name="00N5e00000g0sGF"]');
    if (produto) {
      var first = f.querySelector('#first_name');
      if (first) {
        var wrap = first.closest('div');
        var box = document.createElement('div');
        box.className = 'gac-produto-selecionado';
        box.innerHTML = '<strong>Produto de interesse:</strong> ' + produto + (marca ? ' <span style="opacity:.7">(' + marca + ')</span>' : '');
        wrap.parentNode.insertBefore(box, wrap);
      }
      if (msg && msg.value.indexOf('Produto de interesse') === -1) {
        msg.value = 'Produto de interesse: ' + produto + (marca ? ' | Marca: ' + marca : '') + '\n' + msg.value;
      }
    }

    /* Item 41: CEP preenche endereço (ViaCEP).
       Mapeamento conferido: street=Rua, 00N5e00000g0sGH=Bairro, city=Cidade, state_code=UF */
    var zip = f.querySelector('#zip');
    if (zip) {
      zip.addEventListener('blur', function () {
        var cep = (zip.value || '').replace(/\D/g, '');
        if (cep.length !== 8) return;
        fetch('https://viacep.com.br/ws/' + cep + '/json/')
          .then(function (r) { return r.json(); })
          .then(function (d) {
            if (d.erro) return;
            var bairro = f.querySelector('[name="00N5e00000g0sGH"]');
            if (street && !street.value) street.value = d.logradouro || '';
            if (bairro && !bairro.value) bairro.value = d.bairro || '';
            var city = f.querySelector('#city'); if (city && !city.value) city.value = d.localidade || '';
            var uf = f.querySelector('#state_code'); if (uf && !uf.value) { uf.value = d.uf; uf.dispatchEvent(new Event('change', { bubbles: true })); }
          })
          .catch(function () {});
      });
    }

    /* Item 40 e 70: validação visível antes de postar no Salesforce */
    var REQ = [
      ['first_name', 'Informe o nome'],
      ['last_name', 'Informe o sobrenome'],
      ['00N5e00000g0sFl', 'Informe o CPF ou CNPJ'],
      ['email', 'Informe um e-mail válido'],
      ['phone', 'Informe o telefone'],
      ['mobile', 'Informe o WhatsApp'],
      ['state_code', 'Selecione o estado']
    ];
    function limpa(el) { el.classList.remove('gac-invalido'); var p = el.parentNode.querySelector('.gac-erro'); if (p) p.remove(); }
    function erro(el, txt) { limpa(el); el.classList.add('gac-invalido'); var m = document.createElement('small'); m.className = 'gac-erro'; m.textContent = txt; el.parentNode.appendChild(m); }
    f.addEventListener('submit', function (ev) {
      var falhou = null;
      REQ.forEach(function (p) {
        var el = f.querySelector('[name="' + p[0] + '"]');
        if (!el) return;
        var v = (el.value || '').trim();
        var ok = v !== '' && (p[0] !== 'email' || /.+@.+\..+/.test(v));
        if (!ok) { erro(el, p[1]); if (!falhou) falhou = el; } else { limpa(el); }
      });
      if (falhou) { ev.preventDefault(); falhou.scrollIntoView({ behavior: 'smooth', block: 'center' }); falhou.focus(); }
    }, true);
    [].slice.call(f.querySelectorAll('input,select,textarea')).forEach(function (el) {
      el.addEventListener('input', function () { limpa(el); });
      el.addEventListener('change', function () { limpa(el); });
    });
  }

  /* ---------- 3. Fale Conosco ---------- */
  function faleConosco() {
    var s = document.querySelector('form.wpcf7-form select[name="estado"]');
    if (!s) return;
    /* Item 46 e 47: abria com AC selecionado e gerava lead com UF errada */
    if (!s.querySelector('option[value=""]')) {
      var op = document.createElement('option');
      op.value = ''; op.textContent = 'Selecione o estado'; op.disabled = true; op.selected = true;
      s.insertBefore(op, s.firstChild);
    }
    if (!s.dataset.gacTouched) { s.value = ''; s.required = true; s.dataset.gacTouched = '1'; }
  }

  /* ---------- 4. Busca sem resultado ---------- */
  function busca() {
    /* Item 57: paliativo até corrigir a string no tema ou no TranslatePress */
    [].slice.call(document.querySelectorAll('h1,h2,h3,p,div')).forEach(function (e) {
      if (e.children.length === 0 && /Nenhum ítem encontrado/.test(e.textContent)) {
        e.textContent = e.textContent.replace('Nenhum ítem encontrado', 'Nenhum item encontrado');
      }
    });
  }

  ready(function () { paginaProduto(); orcamento(); faleConosco(); busca(); });
})();
```

---

## Depois de colar

1. Publicar os dois snippets no WPCode com o toggle **Active**.
2. Limpar o cache do LiteSpeed e pedir purge do Akamai, senão a mudança sobe e ninguém vê.
3. Conferir nesta ordem:
   - `/produtos/si50/` → especificações já abertas, botão do WhatsApp com o nome do produto, botão "Solicite um orçamento" levando `?produto=Vergalhão SI50&marca=SINOBRAS`.
   - `/orcamento/?produto=Teste` → bloco "Produto de interesse" acima do campo Nome e a mensagem já preenchida.
   - `/orcamento/` → digitar um CEP e sair do campo, o endereço preenche sozinho. Clicar em Enviar com tudo vazio, devem aparecer as 7 mensagens de erro.
   - `/fale-conosco/` → o campo Estado abre em "Selecione o estado".
4. Fazer **um envio real de teste** no orçamento e confirmar que o lead chegou no Salesforce com a mensagem trazendo o produto. Depois excluir o lead de teste.

## O que este lote não resolve, e por quê

- **Item 24 (ficha técnica em imagem):** o tema já tem CSS pronto para `.technical-specifications table`, então basta trocar o conteúdo do campo de especificações de imagem para tabela HTML, produto a produto. É trabalho de conteúdo no painel, não de código.
- **Itens 59, 60 e 71 (banner de cookies no mobile):** o CMP é o **Privally**. O ajuste deve ser feito no painel do Privally, não por CSS, porque mexer no layout do banner por fora pode comprometer o registro de consentimento.
- **Item 46 em definitivo:** o paliativo por JS resolve na hora, mas o certo é editar o campo `estado` no Contact Form 7 e colocar "Selecione o estado" como primeira opção.
- **Itens 37, 38 e 73 (reduzir campos e tirar CPF/CNPJ obrigatório):** dependem de decisão comercial do cliente.
