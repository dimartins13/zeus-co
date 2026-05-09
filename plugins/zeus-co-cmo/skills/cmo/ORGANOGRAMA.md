# ORGANOGRAMA — Departamento Marketing (CMO)

> Departamento Marketing **NÃO PRECISA** de subordinados próprios no Zeus-CO.
> Diego já tem o plugin `ag-zeus-mkt` com **25 specialists profissionais** que constituem o time de marketing completo.
>
> CMO LEP do Zeus-CO **orquestra** o ag-zeus-mkt. Quando Diego invoca CMO, o CMO chama o specialist certo.

## Estrutura completa do departamento

```
zeus-co-cmo (este plugin — orquestrador estratégico)
    │
    ├── DIREÇÃO ──────────────────────────────────────
    │   ├── ag-zeus-mkt:cmo-marketing            (Chief — eu mesmo)
    │   ├── ag-zeus-mkt:diretor-marketing        (Diretor tático)
    │   ├── ag-zeus-mkt:estrategista-marketing
    │   ├── ag-zeus-mkt:planejamento-estrategico
    │   └── ag-zeus-mkt:marketing-estrategico
    │
    ├── ANÁLISE & DADOS ─────────────────────────────
    │   ├── ag-zeus-mkt:analista-marketing
    │   ├── ag-zeus-mkt:business-intelligence
    │   ├── ag-zeus-mkt:investigar-performance
    │   └── ag-zeus-mkt:simular-volume
    │
    ├── BRANDING & POSICIONAMENTO ───────────────────
    │   ├── ag-zeus-mkt:branding
    │   ├── ag-zeus-mkt:comportamento-consumidor
    │   ├── ag-zeus-mkt:tendencias-criativas-br
    │   └── ag-zeus-mkt:pesquisa-mercado
    │
    ├── CRIAÇÃO ─────────────────────────────────────
    │   │  (cross com CCO LEP — esses specialists ficam no domain do CCO)
    │   ├── ag-zeus-mkt:diretor-criacao
    │   ├── ag-zeus-mkt:publicidade-criativa
    │   ├── ag-zeus-mkt:copywriting
    │   ├── ag-zeus-mkt:direcao-de-arte-ia
    │   ├── ag-zeus-mkt:roteiro-publicitario
    │   └── ag-zeus-mkt:producao-entrega
    │
    ├── CANAIS & ATIVAÇÃO ───────────────────────────
    │   ├── ag-zeus-mkt:digital-marketing
    │   ├── ag-zeus-mkt:social-media-conteudo
    │   ├── ag-zeus-mkt:growth-performance
    │   ├── ag-zeus-mkt:funil-conversao
    │   ├── ag-zeus-mkt:midia-planejamento
    │   ├── ag-zeus-mkt:martech-implementacao
    │   ├── ag-zeus-mkt:trade-marketing-varejo
    │   └── ag-zeus-mkt:pr-comunicacao-corporativa
    │
    ├── CX & PRICING ───────────────────────────────
    │   ├── ag-zeus-mkt:cx-experiencia-cliente
    │   └── ag-zeus-mkt:estrategia-pricing
    │
    └── QA ─────────────────────────────────────────
        └── ag-zeus-mkt:verificador-factual
```

## Total: 25 specialists já existentes + CMO LEP (Zeus-CO) = **26 capabilities marketing**

## Quando CMO LEP é invocado, ele:

1. Identifica intent (estratégia / canal / criação / análise)
2. Decide qual specialist do `ag-zeus-mkt` ativar
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

- ag-zeus-mkt já tem 25 skills de qualidade (Diego pediu pra adaptar das skills do amigo originalmente — funcionou)
- Duplicar = manter 2 versões = drift = caos
- Diego confirmou em sessões anteriores: ag-zeus-mkt = "departamento operacional"
- Token economy: skills carregadas só quando invocadas, sem overhead

## Decisão arquitetural

CMO Department é o **único Chief que orquestra plugin externo**. Os outros 6 Chiefs (CFO, COO, CEO, CCO, CTO, CLO) têm subordinados internos.

CCO faz **híbrido**: 3 subordinados próprios (Brand Guardian, Content Strategist, Creative Ops) + delega criação executiva ao ag-zeus-mkt criação.

## Manutenção

Quando ag-zeus-mkt for atualizado/expandido pelo Diego (ou amigo), este ORGANOGRAMA.md deve ser revisado.
