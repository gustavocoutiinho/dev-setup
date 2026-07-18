---
name: crm-modulos
description: Use SEMPRE que precisar ligar/desligar um módulo ou item de menu por empresa no MinerCRM (esconder ou mostrar um bloco ou item do sidebar pra um cliente específico). Dispara com "esconde o módulo <x> da empresa <y>", "liga o menu <z> pro <cliente>", "tira <item> do sidebar da <org>", "controla o que a empresa vê", "matriz de módulos", "/admin/empresas". Controle item a item por org. NÃO é criar a org ([[crm-org]]).
---

# crm-modulos: menu e módulos por empresa no MinerCRM

O painel `/admin/empresas` controla o que cada cliente vê no menu, item a item (onda 1 de um roadmap de 42 funções benchmarkadas). Esta skill é o trilho pra ligar/desligar sem quebrar a retrocompatibilidade que já está no ar.

## Quando disparar
- "Esconde/liga o módulo <x> pra empresa <y>", "controla o que a <org> vê", "matriz de módulos".
- NÃO use pra criar a org do zero ([[crm-org]]).

## Como executar
1. **Modelo**: `org_nav_modules.nav_items jsonb` = mapa `id_do_item → false`. Ausência = ligado (default `{}`). 100% retrocompatível.
2. **Fonte única dos itens**: `lib/nav/managedNavItems.ts` (id/label/grupo/route/core). `Configurações` e `Perfil` são `core`, não desligáveis.
3. **UI**: aba **Módulos** em `app/admin/empresas/EmpresasClient.tsx` = matriz empresas × itens, toggle na célula.
4. **Backend**: `PATCH /api/admin/organizations/[id]/modules` aceita `navItems`, auditado (`org.modules_updated`). Hook `useNavModules` lê `nav_items`.
5. **Gate no menu**: `components/Layout.tsx` filtra (`filteredGroups`). Item desligado só SOME do menu, não trava a rota (decisão de escopo).
6. **Audiência** (todos | gestao) = `org_nav_modules.audience`, tri-state na mesma tela.

## Gotchas
- Staff @minerbz NUNCA é filtrado: vê tudo pra administrar. Só o cliente sente o toggle.
- Desligar item some do menu, mas a rota ainda responde (bloqueio server-side é onda futura).
- Quem vê dentro da empresa (vendedor × gerente) continua automático pelo papel; o toggle só liga/desliga o item.
- Parceiros e WhatsApp Calling seguem gates próprios (`consignment_org_access` / `instance_feature_flags`), fora da matriz.
- Verificação visual em prod depende do login do Gustavo (não logamos por regra).

## O que NÃO fazer
- Não criar coluna nova por módulo: o `nav_items` jsonb resolve.
- Não desligar item `core` (Configurações/Perfil).
- Não tratar o toggle como segurança de rota: é só menu.
- Não inventar tabela de planos/preços: depende de decisão do Gustavo.
