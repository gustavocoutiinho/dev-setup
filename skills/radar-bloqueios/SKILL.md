---
name: radar-bloqueios
description: Mantém vivo o radar das credenciais e decisões pendentes que travam sistemas da Miner (os itens marcados [VC] no plano), avisa ANTES de prazos vencerem (ex: token Meta expira 22/08, que derruba todos os relatórios vivos) e destrava o item assim que o Gustavo resolve. Use SEMPRE que aparecer pendência de credencial, prazo de token/chave, ou a pergunta "o que falta", "o que depende de mim", "o que tá travado", "quais bloqueios", "o que vence", "destrava o item X". Fonte da lista: ~/Documents/Claude/plano-modulos-e-skills.md e o vault Obsidian (~/ObsidianVaults/miner), onde as notas marcam pendências.
---

# radar-bloqueios — o que trava, o que vence, o que já dá pra destravar

Isto não é skill de execução: é um **radar**. Muitos sistemas da Miner estão a uma credencial ou decisão do Gustavo de funcionar (marcados **[VC]** no plano). O radar mantém essa lista viva, cobra na hora certa (principalmente prazos de token) e, quando o Gustavo resolve, destrava e aponta o próximo passo de execução.

## Quando disparar
- "o que falta / o que depende de mim / o que tá travado / quais bloqueios / o que vence".
- Ao ver um `[VC]` no plano, uma nota do vault marcando pendência, ou um prazo de token/chave.
- Quando o Gustavo disser "resolvi X", "girei a chave", "renovei o token" (aí é destravar).

## Como executar
1. **Leia as fontes.** `~/Documents/Claude/plano-modulos-e-skills.md` (itens `[VC]` no Módulo 8 e espalhados) e o vault via `obsidianminer` (notas de memória marcam BLOQUEIO/pendência, ex: `project_relatorios_vivos` = WINDSOR_API_KEY; `ads-mcp-servers-setup` = token Meta 60d; `mineros-hardening-jul26` = PAT a revogar).
2. **Monte o radar** (um item por linha): id/assunto, o que trava, o que o Gustavo precisa fazer (a credencial/decisão), o sistema impactado, e o prazo se houver. Ordene por urgência: **prazo quente primeiro**.
3. **Prazos quentes.** Marque com destaque qualquer credencial com validade. Hoje o mais crítico é o **token Meta que expira 22/08** (item 108): derruba todos os relatórios vivos. Avise com antecedência, não no dia. Se houver `refresh.sh`/rotina de renovação, aponte-a.
4. **Destrave quando o Gustavo resolver.** Ao ele confirmar que resolveu um item (girou a chave, renovou o token, decidiu), marque como destravado no radar e diga qual skill/execução agora pode rodar (ex: token renovado → `relatorio-vivo` volta a puxar; chave girada → `dado-vivo`/`ia-unificada` daquele portal seguem).
5. **Confirme antes de dar como resolvido.** "Resolvi" só vira destravado depois de checar que a credencial de fato funciona (token válido, chave aceita). Não risque item no boca a boca.
6. **Registre.** Atualize a nota de radar/pendências no vault com a data, pra a lista não se perder entre sessões. Aditivo: não apague o histórico do que estava travado.

## Gotchas
- Prazo de token não perdoa: perder o 22/08 quebra relatório de vários clientes de uma vez. Trate como o item mais quente até renovar.
- Alguns `[VC]` são decisão, não credencial (ex: escolher qual project é canônico). Deixe claro o que exatamente é pedido pro Gustavo, senão o item fica parado.
- Credencial pode "voltar a travar": token renovado vence de novo em 60d, chave girada quebra blobs antigos. Ao destravar, agende o próximo vencimento no radar.
- Nota de memória reflete o que era verdade quando escrita. Antes de cobrar, confirme que o bloqueio ainda existe (a credencial pode já ter sido resolvida).

## O que NÃO fazer
- NÃO executar a ação bloqueada por conta própria: entrar com senha/credencial, girar chave ou renovar token é do Gustavo. O radar cobra e prepara, não faz login por ele.
- NÃO inventar prazo. Se a nota não diz a validade, marque "prazo desconhecido, confirmar".
- NÃO dar item como destravado sem confirmar que a credencial funciona.
- NÃO deixar o radar só na conversa: persista no vault pra sobreviver à sessão.
