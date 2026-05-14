# ORGANOGRAMA — Departamento Marketing (CMO)

> Departamento Marketing **NÃO PRECISA** de subordinados próprios no Zeus-CO.
> Diego já tem o plugin `zeus-co-cmo + zeus-co-marketing + zeus-co-cco` com **31 specialists profissionais (CMO + CCO + Marketing)** que constituem o time de marketing completo.
>
> CMO LEP do Zeus-CO **orquestra** o ecossistema ZEUS-CO. Quando Diego invoca CMO, o CMO chama o specialist certo.

## Estrutura completa do departamento

```
zeus-co-cmo (este plugin — orquestrador estratégico)
    │
    ├── DIREÇÃO ──────────────────────────────────────
    │   ├── zeus-co-cmo:cmo            (Chief — eu mesmo)
    │   ├── zeus-co-cmo:cmo-estrategia-marketing        (Diretor tático)
    │   ├── zeus-co-cmo:cmo-estrategia-marketing
    │   ├── zeus-co-cmo:cmo-estrategia-marketing
    │   └── zeus-co-cmo:cmo-estrategia-marketing
    │
    ├── ANÁLISE & DADOS ─────────────────────────────
    │   ├── zeus-co-cmo:cmo-marketing-ops-martech
    │   ├── zeus-co-cmo:cmo-marketing-ops-martech
    │   ├── zeus-co-cmo:cmo-marketing-ops-martech
    │   └── zeus-co-cmo:cmo-pesquisa-insights
    │
    ├── BRANDING & POSICIONAMENTO ───────────────────
    │   ├── zeus-co-cmo:cmo-branding
    │   ├── zeus-co-cmo:cmo-pesquisa-insights
    │   ├── zeus-co-cmo:cmo-pesquisa-insights
    │   └── zeus-co-cmo:cmo-pesquisa-insights
    │
    ├── CRIAÇÃO ─────────────────────────────────────
    │   │  (cross com CCO LEP — esses specialists ficam no domain do CCO)
    │   ├── zeus-co-cco:cco-orquestrador
    │   ├── zeus-co-cco:cco-art-director
    │   ├── zeus-co-cco:cco-copy-master
    │   ├── zeus-co-cco:cco-art-director
    │   ├── zeus-co-cco:cco-storytelling
    │   └── zeus-co-cco:cco-creative-ops
    │
    ├── CANAIS & ATIVAÇÃO ───────────────────────────
    │   ├── zeus-co-cmo:cmo-growth-performance
    │   ├── zeus-co-cco:cco-content-strategist
    │   ├── zeus-co-cmo:cmo-growth-performance
    │   ├── zeus-co-cmo:cmo-growth-performance
    │   ├── zeus-co-cmo:cmo-growth-performance
    │   ├── zeus-co-cmo:cmo-marketing-ops-martech
    │   ├── zeus-co-marketing:retail-media
    │   └── zeus-co-cmo:cmo-comunicacao-pr
    │
    ├── CX & PRICING ───────────────────────────────
    │   ├── zeus-co-cmo:cmo-crm-lifecycle
    │   └── zeus-co-cmo:cmo-product-marketing
    │
    └── QA ─────────────────────────────────────────
        └── zeus-co-cmo:cmo-pesquisa-insights
```

## Total: 25 specialists já existentes + CMO LEP (Zeus-CO) = **26 capabilities marketing**

## Quando CMO LEP é invocado, ele:

1. Identifica intent (estratégia / canal / criação / análise)
2. Decide qual specialist do `zeus-co-cmo + zeus-co-marketing + zeus-co-cco` ativar
3. Passa contexto da empresa ao specialist
4. Sintetiza resposta + Próximos Movimentos
5. Atualiza LEARNINGS.md da empresa

## Mapeamento intent → specialist

| Diego diz | CMO LEP chama |
|---|---|
| "estratégia de marketing pra X" | `:estrategista-marketing` ou `:planejamento-estrategico` |
| "GTM Q3" | `:cmo-marketing` (eu) + `:funil-conversao` |
| "growth do 2ndStreet" | `:growth-performance` + `:analista-marketing` |
| "criar peça de campanha" | `:publicidade-criativa` + `:copywriting` + `:direcao-de-arte-ia` |
| "calendário social" | `:social-media-conteudo` |
| "CAC tá alto, investiga" | `:analista-marketing` + `:investigar-performance` |
| "mídia paga Meta/Google" | `:midia-planejamento` + `:growth-performance` |
| "pricing pra TarjaPreta" | `:estrategia-pricing` + cross CFO |
| "PR pro lançamento" | `:pr-comunicacao-corporativa` |
| "tendência criativa BR" | `:tendencias-criativas-br` |
| "brand foundation" | `:branding` + cross CCO LEP |

## Por que NÃO duplicar como subordinados zeus-co-cmo-*

- ZEUS-CO tem 25 skills de qualidade (Diego pediu pra adaptar das skills do amigo originalmente — funcionou)
- Duplicar = manter 2 versões = drift = caos
- Diego confirmou em sessões anteriores: ZEUS-CO = "departamento operacional"
- Token economy: skills carregadas só quando invocadas, sem overhead

## Decisão arquitetural

CMO Department é o **único Chief que orquestra plugin externo**. Os outros 6 Chiefs (CFO, COO, CEO, CCO, CTO, CLO) têm subordinados internos.

CCO faz **híbrido**: 3 subordinados próprios (Brand Guardian, Content Strategist, Creative Ops) + delega criação executiva ao ecossistema ZEUS-CO criação.

## Manutenção

Quando ecossistema ZEUS-CO for atualizado/expandido pelo Diego (ou amigo), este ORGANOGRAMA.md deve ser revisado.
