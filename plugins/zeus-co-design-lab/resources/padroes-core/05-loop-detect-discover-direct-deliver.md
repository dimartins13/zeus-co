# Padrão 05 · Loop 4-D (Detect → Discover → Direct → Deliver)

O loop completo do agente, sintetizado. Esta é a "máquina" do Open Design,
adaptada para o DESIGN-LAB (zeus-co-design-lab).

## Fluxo

```
┌─────────────────────────────────────────────────────────────────┐
│  USUÁRIO ENVIA BRIEF                                             │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  DETECT (5s) — orquestrador classifica em 1 de 11 famílias      │
│  Identifica: deck? LP? KV? vídeo? Documento? Prototype?         │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  DISCOVER (30s) — emite <question-form id="discovery">          │
│  7 perguntas em radio/checkbox, sem texto livre se evitável     │
│  STOP aqui até usuário responder                                 │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  DIRECT — direção visual definida:                               │
│  · Brand spec fornecido?  → usar                                 │
│  · Screenshot fornecido?  → extrair tokens com Bash + Read       │
│  · Nenhum dos dois?       → abrir 2º form com as 5 escolas       │
│  Resultado: palette OKLch + font stack + posture cues no :root   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  PLAN — TodoWrite com 5-12 tarefas                               │
│  Cada tarefa = 1 incremento visível                              │
│  Skills + integrações externas no plano                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  DELIVER — produção iterativa, 1 artefato por turn               │
│  · Aciona skill interna (do DESIGN-LAB (zeus-co-design-lab))                            │
│  · Aciona integração externa (Freepik/Higgsfield/Adobe/Gamma)    │
│  · Escreve HTML/PPTX/PDF/MP4 em disco                            │
│  · Emite <artifact> para preview                                 │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  CRITIQUE 5-DIM — antes de fechar:                               │
│  philosophy · hierarchy · detail · function · innovation         │
│  Se alguma < 3, itera; se passa, entrega                         │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
                       ENTREGA FINAL
                  (HTML / PPTX / PDF / MP4 / ZIP)
```

## Particularidades do DESIGN-LAB (zeus-co-design-lab)

1. **Em pt-BR.** Todas as perguntas, mensagens e direções estão traduzidas.
2. **Com integrações nossas.** Freepik/Higgsfield/Adobe/Gamma entram na fase DELIVER conforme a família detectada.
3. **Sem daemon.** Esse loop roda dentro do Claude/Cowork — não precisa do `pnpm tools-dev` do Open Design.
4. **Composável com ZEUS-CO.** Se o brief envolve estratégia + produção visual, o `zeus-co-design-lab-orquestrador` me chama na fase de execução.

---

**Fonte:** `apps/daemon/src/prompts/system.ts` (929 linhas) +
`discovery.ts` + `directions.ts` + `deck-framework.ts`
