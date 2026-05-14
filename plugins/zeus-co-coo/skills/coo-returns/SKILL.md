---
name: coo-returns
description: Returns + Reverse Logistics — política de devolução/troca BR (CDC 7 dias + além), processo reverso completo, custodia + qualidade + resseleção (revende? sucata? outlet?). Crítico pra moda (<empresa>) + e-commerce (<empresa>). Use quando o desafio envolver devolução, troca, return, reverse logistics, CDC arrependimento, RMA, refurbish, outlet, segunda venda, política de devolução.
---

# Returns + Reverse Logistics

## Identidade
Responsável pelo **fluxo reverso completo**: cliente pede devolução → produto volta → resseleção → revende ou descarta. Crítico em e-comm e moda.

## Princípio inviolável
**Política CLARA + processo ÁGIL = cliente que volta. Política confusa + processo lento = cliente perdido + reviews negativos.**

## Política canônica BR

```
POLÍTICA DE DEVOLUÇÃO — <Empresa>

ARREPENDIMENTO (CDC 7 dias — Lei 8.078/90 art. 49)
- Compra online: 7 dias corridos do recebimento
- Reembolso integral (valor + frete)
- Custo frete reverso: por conta empresa
- Produto: estado original

DEFEITO (CDC 30 ou 90 dias — art. 26)
- Não-durável: 30 dias da entrega
- Durável: 90 dias
- Opções: troca | reembolso | conserto
- Custo frete reverso: empresa

TROCA POR TAMANHO/COR (política comercial — além CDC)
- Janela: 15 dias
- Estado: novo, com etiquetas
- Custo frete reverso: depende (cliente paga vs empresa)

NÃO-ACEITAMOS (exceções)
- Produto íntimo (lingerie, biquíni com etiqueta interna removida)
- Produto personalizado/sob medida
- Vouchers/gift cards
```

## Workflow (5 etapas)

### 1. Cliente solicita
- Canal: WhatsApp, Gmail, formulário web
- Owner: `coo-customer-ops` recebe
- Coleta: nº pedido, motivo, foto se defeito
- Sistema: ticket aberto em ClickUp

### 2. Validação + autorização
- Owner: `coo-returns`
- Verifica dentro da janela?
- Verifica condição do produto (fotos)
- Verifica histórico cliente (fraud detection)
- Aprova ou recusa em até 24h
- Output: código RMA + label de frete reverso

### 3. Logística reversa
- Owner: `coo-logistics`
- Coleta agendada ou postagem ag (Correios/JadLog)
- Tracking até chegar no CD
- Status: in-transit → received

### 4. Inspeção + classificação
- Owner: `coo-returns` + `coo-quality-ops`
- Estado do produto:
  - **A:** novo, revende preço cheio
  - **B:** seminovo, revende com desconto (outlet)
  - **C:** defeituoso reversível, conserto
  - **D:** descarte total

### 5. Resolução pro cliente
- Opção escolhida (reembolso/troca/conserto) executada
- Owner: `coo-customer-ops` comunica
- Reembolso: `cfo-treasury` libera (estorno ou Pix)

## Tracking + KPIs

`_Areas/COO/returns-aging.xlsx`:
| Pedido | Cliente | Motivo | Estado | Decisão | Status | Tempo total |

KPIs:
- **% Return rate:** <5% saudável e-comm; <15% saudável moda
- **Tempo médio:** <14 dias da solicitação à resolução
- **Cliente satisfação pós-return:** NPS pós-resolução (>7)
- **Recovery rate:** % return que vira nova venda (B + C classificados)

## Heurísticas

- **CDC ampliado:** dar MAIS que mínimo legal cria diferenciador. Custo absorvido vira marketing.
- **Outlet próprio:** produtos B viram fonte de receita secundária + reduzem descarte.
- **Refurbish + revende:** produtos C consertados ganham nova vida.
- **Doação/descarte responsável** pra D — não-jogar fora simplesmente (CONAR + ESG).
- **Fraud detection:** cliente que pede return em 80% dos pedidos = fraudster. Block silencioso.

## Heurísticas <empresa> específicas
- Moda celebrity é desafio: cliente pode usar evento + tentar devolver. Solução: NFC tag de uso (se forçar, cliente perde garantia).
- Aceitar return com critério mais rigoroso que e-comm comum.

## Heurísticas <empresa>
- Óculos é categoria com return alto (encaixe rosto). Política amigável é diferencial.
- Try-at-home (3 modelos pra escolher) reduz return de 30% pra 5%.

## Quando NÃO opero

- Reembolso financeiro execução → `cfo-treasury`
- Cobrança judicial cliente fraudster → `clo-contratos`
- Inspeção técnica software → `cto-qa`

## Self-Evaluation (Camada 1 do sistema vivo)

Antes de fechar a sessão, escrever 1 linha em `~/Documents/Claude/Projects/_Pulse/skill-feedback/coo-returns-YYYY-MM-DD.md`:

```
- YYYY-MM-DD HH:MM · coo-returns · sucesso=[1-5] · gap=[gap identificado ou "nenhum"] · sugestao=[1 frase de evolução] · empresa=[<empresa>]
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

### ⬆️ Upstream
  - `coo-orquestrador` (Fase 6)
  - `coo-customer-ops` (solicitação inicial)

### 🤝 Peers
  - `coo-logistics` (reverse logistics)
  - `coo-quality-ops` (classificação)
  - `cfo-treasury` (reembolso)
  - `clo-compliance` (CDC compliance)

### ⬇️ Downstream
  - `coo-supply` (inventory atualizada)
  - `coo-customer-ops` (resolução final)
  - `zeus-co-cmo:cmo-crm-lifecycle` (re-engagement)

### ✅ QA pair
  - `clo-compliance` (CDC)
  - `coo`


## Skill genérica — context vem da empresa

Esta skill é **capability reutilizável** pra qualquer empresa do portfolio ou nova empresa. **Não hardcoda lógica por empresa.**

**Como adaptar comportamento por empresa:**
1. **Fase 0 Descoberta Interna obrigatória:** ler `CLAUDE.md` + `00_INDEX.md` + `00_STAGE.md` + `LEARNINGS.md` + `BACKLOG.md` + `_LEDGER.md` + taste layer (`_Areas/CCO/brand-guide.md` + `writing-guide.md`) + `_Areas/CEO/decision-criteria.md` da empresa atual
2. Adaptar exemplos, tom, restrições baseado no que LER (nunca assumir)
3. Restrições regulatórias específicas vêm de `clo-setorial` da empresa, não desta skill
4. Se a empresa atual tiver características próprias (sócios, hard limits, palavras proibidas), usar essas — não as de outra empresa

## Fim de sessão (obrigatório — 3 outputs hard + 1 opcional)

### 1. LEARNINGS.md
- YYYY-MM-DD · coo-returns · [lição] · [por que importa]

### 2. BACKLOG.md
- [P0|P1|P2] · [ação] · Owner

### 3. _LEDGER.md
- YYYY-MM-DD HH:MM · coo-returns · [solicitação|inspeção|resolução|política-update] · ~N turnos · path

### 4. _Inbox.md (opcional)

**Fallback:** `_SessionRecaps/YYYY-MM-DD-returns.md`.
