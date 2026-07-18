---
name: guarda-ia
description: Adiciona rate-limit / cota por usuário por dia em qualquer endpoint que chama IA (hoje nenhum tem contagem), pra fechar abuso de crédito antes que um loop ou um usuário torre o saldo. Dispara ao ver rota/edge/handler que chama ai-json (ou OpenAI/Anthropic) sem nenhuma contagem, ou quando o Gustavo disser "coloca limite na IA", "trava a cota", "alguém pode abusar disso", "quantas chamadas por usuário", "protege o crédito", "rate limit na IA". Limite configurável; conta por usuário no Supabase.
---

# Guarda de IA (cota por usuário/dia)

Nenhum endpoint de IA da Miner conta chamada. Um loop no front, um usuário curioso ou um script torram o crédito do proxy sem ninguém ver. Esta skill põe um **rate-limit por usuário por dia** na frente de qualquer chamada de IA (o proxy `ai-json` no Supabase minercrm `stpstwsqtuubpxvvexte`, ou uma chamada direta legada), com limite configurável.

## Quando disparar
- Handler/edge/rota que chama IA e **não** incrementa nem checa contador antes.
- Endpoint de IA aberto por ação do usuário (botão "analisar", "gerar", "resumir") sem teto.
- Gustavo pediu limite/cota/proteção de crédito.

## Estratégia
Contador **por usuário por dia** numa tabela do Supabase minercrm (o mesmo projeto do ai-json). Uma linha por `(user_id, dia)`; incrementa a cada chamada; bloqueia ao passar do limite. Limite vem de env/config (`AI_DAILY_LIMIT`, default sugerido 50), pra ajustar sem deploy de código.

```sql
-- aditivo: tabela nova, não mexe em nada existente
create table if not exists public.ai_usage_daily (
  user_id uuid not null,
  dia date not null default current_date,
  used int not null default 0,
  primary key (user_id, dia)
);
alter table public.ai_usage_daily enable row level security;
-- escrita só via service_role (edge), leitura do próprio usuário se precisar exibir saldo
```

## Como executar
1. **Ache os pontos sem guarda**: `grep -rniE "ai-json|openai\.com|anthropic\.com|functions/v1" <repo>` e veja quais não checam cota antes.
2. **Crie a tabela** (SQL acima) via migração aditiva no minercrm. Não altere tabela existente.
3. **Envelope a chamada** com checagem + incremento atômico (roda no server/edge com service_role, nunca no client):
   ```ts
   async function comCota(userId: string, fn: () => Promise<any>) {
     const limite = Number(Deno.env.get("AI_DAILY_LIMIT") ?? "50");
     // incrementa e devolve o novo total, atômico
     const { data, error } = await supabase.rpc("ai_bump_usage", { p_user: userId });
     if (error) throw error;
     if (data > limite) {
       return { ok: false, error: "limite_diario", used: data, limite };
     }
     return await fn(); // só aqui chama o ai-json
   }
   ```
   `ai_bump_usage` é um upsert `used = used + 1` retornando o novo `used` (função SQL `security definer`). Assim a contagem é atômica e não dá corrida.
4. **Chame o ai-json dentro do `fn`** (mesmo contrato de sempre: POST `.../functions/v1/ai-json?key=miner_ai_9f2c7b41` com `{system, user, model?, temperature?}` → `{ok, data, usage}`).
5. **Devolva erro claro** ao passar do teto (HTTP 429 ou `{ok:false, error:"limite_diario"}`), pro front mostrar "limite diário atingido" em vez de quebrar.
6. **Teste**: force o limite baixo (`AI_DAILY_LIMIT=2`), dispare 3 vezes, confirme que a 3ª barra e que o contador zera no dia seguinte. Só então deploy com ok do Gustavo.

## Gotchas
- **Identifique o usuário de verdade** (JWT/`auth.uid()` do Supabase). Sem user confiável, o limite não vale nada; não confie em id vindo do client.
- Incremente **antes** de chamar o modelo (ou de forma atômica), senão duas abas passam juntas.
- Um dia = `current_date` no timezone certo. Se a operação é BR, fixe America/Sao_Paulo pra não virar meia-noite UTC.
- `usage` que o ai-json devolve serve pra logar custo real, não pra contar cota (a cota é por chamada).
- Rate-limit é aditivo: não muda a resposta de sucesso, só bloqueia excesso.

## O que NÃO fazer
- Não contar no client (localStorage/estado): burla em 1 F5.
- Não hardcodar o limite no código: use env/config pra ajustar sem deploy.
- Não bloquear silencioso: sempre retorne motivo (`limite_diario`) e o teto.
- Não abrir a tabela pra escrita via client; incremento só via service_role/edge.
