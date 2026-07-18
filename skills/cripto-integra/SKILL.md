---
name: cripto-integra
description: Use SEMPRE que uma integração de cliente falhar por credencial que não decripta, ou quando for rotacionar/re-encriptar os blobs {enc} guardados. Dispara com "a integração do <cliente> não conecta", "erro bearer_token e endpoint são obrigatórios", "o token não decripta", "re-encripta as credenciais", "a chave de integração mudou", "conserta a credencial da ForYou/PRLS/Maresia". Também quando "conectado" mas o sync falha como se não tivesse token. Regrava o blob com a chave atual, sem trocar a chave sem migrar.
---

# cripto-integra: rotacionar/re-encriptar credenciais {enc}

Quando a chave de encriptação de integrações muda, os blobs `{enc}` gravados antes **param de decriptar** e a integração falha como se não tivesse credencial, mesmo aparecendo "conectada". Esta skill diagnostica isso e regrava o blob com a chave atual, sem cair na armadilha de trocar a chave sem migrar os dados.

## Quando disparar
- "a integração do <cliente> não conecta", erro `bearer_token e endpoint são obrigatórios` (ou equivalente do provider) com credencial "conectada".
- "o token não decripta", "re-encripta as credenciais", "a chave de integração mudou".
- Sync/teste falha como se não houvesse token.

## Como executar
1. **Confirme que é a chave, não o adapter.** O `integrations.credentials` do minercrm (`stpstwsqtuubpxvvexte`) guarda `{enc: base64(salt|iv|tag|cipher)}`, AES-256-GCM, chave = `scrypt(INTEGRATIONS_ENCRYPTION_KEY, 'integrations-salt-v1', 32)` (`lib/integrations/encryption.ts`). Teste decrypt local antes de tocar em código.
2. **Se falhar** ("Unsupported state or unable to authenticate data"): a chave rotacionou (mudou entre 09/06 e 03/07). Blobs antigos são lixo.
3. **Regrave com a chave atual:** `vercel env pull` pega a `INTEGRATIONS_ENCRYPTION_KEY` de prod, um script de ~20 linhas espelhando `encryption.ts` gera o blob novo, `UPDATE integrations SET credentials = jsonb_build_object('enc', ...)`. Padrão já aplicado no Stalker (03/07).
4. **Pendentes conhecidos** (blob pré-rotação): ForYou Olist, PRLS Bling, ForYou Suri, Maresia Suri.
5. Credencial de MCP multi-tenant é outra tabela (`miner_api_credentials`, MinerOS, padrão [[mcp-kit]]): lá o token costuma ser plano; o `{enc}` é do minercrm.

## Gotchas
- **NUNCA troque `INTEGRATIONS_ENCRYPTION_KEY` sem migrar os blobs existentes**: foi o que gerou essa dor toda.
- Debugar adapter/API antes de testar o decrypt é começar no lugar errado.
- Token que trafegou por chat/print/log: rotacione na origem mesmo assim ([[varredura-segredos]]).
- Fechar credencial/segredo exposto no banco é [[supabase-hardening]].

## O que NÃO fazer
- NÃO reescrever o provider achando que é bug de código.
- NÃO logar nem expor a chave ou o token em claro.
- NÃO trocar a chave de encriptação sem plano de migração.
