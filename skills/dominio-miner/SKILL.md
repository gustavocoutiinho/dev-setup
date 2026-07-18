---
name: dominio-miner
description: Use SEMPRE que for apontar um domínio ou subdomínio *.minerbz.com.br pra um projeto Vercel da Miner. Dispara com "aponta o domínio", "cria o subdomínio <x>.minerbz.com.br", "põe no domínio da Miner", "configura o DNS", "coloca num subdomínio". Padroniza o apontamento e mantém a URL antiga viva.
---

# dominio-miner: subdomínio *.minerbz.com.br no padrão

Cada projeto Miner que vai pro ar ganha um subdomínio `<slug>.minerbz.com.br` (ex: festival.minerbz.com.br, portal.minerbz.com.br). Esta skill padroniza o apontamento e evita quebrar URL que já circula.

## Quando disparar
- "aponta domínio", "cria o subdomínio X.minerbz.com.br", "configura DNS do projeto", "coloca no domínio da Miner".

## Como executar
1. **Slug no padrão.** O subdomínio segue o mesmo `tipo-cliente` do projeto (GitHub/Vercel/`~/dev`).
2. **DNS.** Registro A do subdomínio apontando pra Vercel (`76.76.21.21`), ou CNAME conforme o painel pedir.
3. **Adiciona o domínio no projeto Vercel** e aguarda o SSL provisionar.
4. **Confirma no ar** ([[deploy-miner]]): abre `https://<slug>.minerbz.com.br` e valida o certificado + conteúdo.
5. **URL antiga viva.** Se já existia uma URL divulgada, mantém funcionando (redirect se preciso), nunca quebra link que o cliente usa.

## Gotchas
- Propagação de DNS e SSL leva minutos: não conclua antes do certificado válido.
- Trocar o domínio de um projeto sem manter o antigo derruba links já compartilhados.

## O que NÃO fazer
- NÃO apontar domínio sem confirmar o SSL e o conteúdo no ar.
- NÃO matar a URL antiga que o cliente já usa.
- NÃO fugir do padrão `*.minerbz.com.br` sem motivo.
