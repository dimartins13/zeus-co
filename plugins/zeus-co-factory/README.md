# Zeus-CO — Skill Factory

Meta-skill que constrói **Living Expert Profiles (LEPs)** — agentes virtuais de C-level e specialists para o Zeus-CO do Diego.

## O que é um LEP

Living Expert Profile = skill instalada que representa um profissional sênior de uma função (CEO, CFO, COO, CMO, CCO, CTO, CLO, ou specialist subordinado). LEP tem:

- **CORE.md** — identidade, frameworks, heurísticas, lógica de orquestração
- **LITERATURE.md** — bibliografia em 3 camadas (canônica, viva, casos) + Brasil
- **RADAR.md** — MCPs/tools (instalados, avaliando, wishlist)
- **EVOLUTION.md** — changelog + lições incorporadas
- **WEEKLY_DIGEST.md** — output do cron semanal de atualização
- **templates/** — templates de artefatos canônicos do role

## Princípio fundador

**C-levels NÃO julgam a empresa. C-levels FAZEM a empresa funcionar.**

LEPs são operadores, não auditores. CORE.md sempre usa verbos de execução.

## Como invocar

Diego diz: "cria o CFO", "preciso de um especialista em LGPD", "atualiza literatura do CMO".

Skill Factory roda 5 fases:
1. Pesquisa autônoma (literatura + ferramentas)
2. Mapear skills existentes ao role
3. Autoria (preencher templates)
4. Cron semanal de evolução
5. Teste vivo em empresa real do Diego

## Templates canônicos

Em `skills/lep-builder/_template/` — modelos para cada um dos 5 arquivos do LEP.
