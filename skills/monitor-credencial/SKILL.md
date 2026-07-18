---
name: monitor-credencial
description: Use SEMPRE que uma credencial, token ou OAuth tiver prazo de validade se aproximando, pra avisar ANTES de vencer, não no dia em que quebrou. Automatiza o aviso por prazo (o token Meta de 60d expira 22/08 e derruba todos os relatórios vivos; 7 credenciais P1 pendentes; OAuth de validade curta). O [[radar-bloqueios]] LISTA o que trava; esta calcula os dias que faltam e cobra a renovação a tempo. Dispara com "o que tá pra vencer", "quando expira o token", "me avisa antes de vencer", "prazo de credencial", "o token Meta ainda tá vivo?", "quantos dias até vencer".
---

# monitor-credencial: avisa o vencimento antes de o sistema cair

Credencial não manda recado quando vai expirar: o sistema só quebra no dia. O caso quente é o **token Meta Ads (usuário, 60 dias) que expira 22/08/2026 ~11:47**: quando ele morre, o `meta-ingestor` retorna 503 e **todos os relatórios vivos param**. O [[radar-bloqueios]] mantém a lista de bloqueios; esta skill é a parte automática, calcula quantos dias faltam pra cada credencial e cobra com antecedência.

## Quando disparar
- Rotina de prazo (encaixa no daily-briefing) ou "o que tá pra vencer / quando expira o token".
- Ao ver credencial com data de validade (token 60d, OAuth de sessão curta, chave temporária).
- Gustavo pediu aviso de vencimento ou "o token ainda tá vivo?".

## Como executar
1. **Leia as fontes de validade.** Token Meta em `~/.meta-ads/current_token.txt` (expira 22/08; renova com `bash ~/.meta-ads/refresh.sh <token novo>`). Cópia do token no cofre do MinerOS (`vault.secrets` `meta_access_token`). As **7 credenciais P1** (Meta, Google Ads, Asana PAT, Drive OAuth, Webhook HDTS, HubSpot Private App, Kinbox API). OAuth pendentes de validade limitada: Granola, Box, Gong.
2. **Calcule os dias até vencer** e ordene por urgência. Avise com folga (o lembrete Meta já existe: Asana `1215969231104109` e evento 21/08, ambos 1 dia antes; esta skill cobra a partir de ~15 dias).
3. **Aponte a ação exata** ao Gustavo (é dele): rodar o `refresh.sh`, reautenticar o OAuth.
4. **Avise** DM Slack / WhatsApp / daily-brief e **registre** no vault. Ao renovar, reagende o próximo vencimento (o token novo vence de novo em ~60d).

## Gotchas
- **Não há auto-renovação do token Meta** (regra da Meta, testada): refresh devolve a mesma data, é manual a cada ~60d.
- **O cofre não sincroniza sozinho:** o `refresh.sh` atualiza `~/.claude.json` + `current_token.txt`, mas NÃO o `vault.secrets` do MinerOS. Re-sincronizar a cópia do cofre depois de renovar, senão o ingestor segue com o token velho.
- Sem prazo na nota, marque "validade desconhecida, confirmar", não invente data.

## O que NÃO fazer
- NÃO renovar token nem clicar OAuth por conta própria: credencial é do Gustavo ([[radar-bloqueios]]).
- NÃO dar por resolvido sem confirmar que o token novo funciona.
- NÃO avisar só no dia: o valor é a antecedência.
