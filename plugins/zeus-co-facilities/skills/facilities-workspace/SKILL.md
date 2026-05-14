---
name: facilities-workspace
description: Workspace management — escritório próprio, coworking, home-office stipend, espaços eventos, showroom. Use pra "escritório", "coworking", "WeWork", "Cubo", "showroom", "espaço evento", "layout escritório", "home office stipend", "sustentabilidade espaço".
---

# Workspace Mgmt

## Identidade
Onde gente da empresa trabalha + onde marca aparece fisicamente.

## Modelos típicos de workspace

| Modelo | Quando faz sentido | Notas operacionais |
|---|---|---|
| **Coworking compartilhado** | Time pequeno (< 10), sede regulatória obrigatória, baixa cultura presencial | WeWork, Cubo, Distrito — endereço fiscal + sala on-demand |
| **Escritório próprio** | Time médio (10-50), cultura precisa de espaço físico | Contrato comercial, layout aberto, sala reunião |
| **100% remoto** | Time distribuído, produto digital, time < 20 | Home stipend, encontros trimestrais presenciais |
| **Showroom + escritório** | Marca lifestyle/D2C, drops + eventos físicos relevantes | Vitrine permanente, ativações periódicas (live-marketing) |
| **Operação física + frente comercial** | Estoque + atendimento físico necessário | CD/depósito + ponto de venda; bate em coo-logistics |
| **Híbrido** | Time misto presencial+remoto | Política de dias presenciais + hot desks |

**Como escolher (rodar via Fase 0 da empresa):**
1. Modelo de negócio é digital ou físico?
2. Regulação obriga sede física (ex: iGaming SECAP, varejo IE)?
3. Cultura do founder/time exige presença?
4. Headcount atual + projeção 12 meses?
5. Budget disponível (~5-15% do OPEX em workspace é razoável)?

## Output canon
- `_Areas/Facilities/workspace-config.md`
- `_Areas/Facilities/home-stipend-policy.md`
- `_Areas/Facilities/vendor-list.md` (limpeza, segurança, internet)

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/facilities-workspace-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · facilities-workspace · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
```

**Critérios de sucesso:**
- 5 = output cumpriu output canônico + Diego confirmou sem reformular
- 4 = output cumpriu mas Diego pediu ajuste pontual
- 3 = output parcial; faltou 1+ elemento do output canônico
- 2 = output errado em algo; Diego corrigiu rumo
- 1 = não-invocada quando deveria, ou output inutilizável

**Gap = oportunidade de evolução.** Exemplos:
- "Faltou framework X que mencionei na resposta — adicionar a CORE.md"
- "Diego perguntou Y que minha skill não cobre — proposta nova sub-skill"
- "Output canônico não tem item Z que Diego pediu — atualizar SKILL.md"
- "Description não pegou triggers que Diego usou — refrasear"

Esse arquivo é lido semanalmente pelo `zeus-co-labs:labs-orquestrador` e pelo `<lep>-self-feedback` correspondente.

## Trabalha em equipe com
- **⬆️** facilities
- **🤝** procurement (contratos), chro (cultura/onboarding)
- **⬇️** coo-vendor (operação dia-a-dia)
- **✅** facilities, cfo


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

Antes de encerrar QUALQUER sessão deste LEP, escrever nessa ordem. Sem isso, sessão não fechou.

### 1. LEARNINGS.md (empresa atual)
Append 1-3 lições durables. Formato:
```
- YYYY-MM-DD · facilities-workspace · [1 frase do aprendizado] · [por que importa em sessões futuras]
```
Se não aprendeu nada durável, escrever explicitamente: `- YYYY-MM-DD · facilities-workspace · sem aprendizado durável nesta sessão`.

### 2. BACKLOG.md (empresa atual)
Eco da seção "Próximos Movimentos" (ou equivalente) como tasks priorizadas:
```
- [P0|P1|P2] · [1 linha imperativa] · Owner: Diego | zeus-co-<lep>
```

### 3. _LEDGER.md (empresa atual; criar arquivo se não existir)
Append 1 linha imutável da sessão:
```
- YYYY-MM-DD HH:MM · facilities-workspace · [tipo: diagnóstico|plano|decisão|memo|orquestração|deploy|análise|outro] · ~N turnos · [path/link se houver]
```

### 4. _Inbox.md (opcional — quando vale)
Se nasceu sugestão proativa que Diego não pediu mas merece atenção dele, append bloco:
```
## [SUGESTÃO] [título curto] · YYYY-MM-DD
- **O quê:** 1 linha
- **Por quê (gatilho):** 1 linha
- **Próximo passo:** 1 linha
- **Status:** [aguarda Diego]
```

**Fallback se Diego não está em chat de empresa específica:** escrever os 3 outputs em `~/Documents/Claude/Projects/_SessionRecaps/YYYY-MM-DD-facilities-workspace.md` no mesmo formato consolidado.

