# Padrão 04 · Discovery Form (turn-1 question form)

O agente NUNCA começa a produzir antes de fazer 7 perguntas em radio/checkbox.
30 segundos de form > 30 minutos de retrabalho.

## Forma exata

```
<question-form id="discovery" title="Briefing rápido — 30 segundos">
{
  "description": "Trava isso antes de eu construir. Pula o que não se aplica — eu preencho default.",
  "questions": [
    {
      "id": "output",
      "label": "O que estamos fazendo?",
      "type": "radio",
      "required": true,
      "options": [
        "Deck / apresentação / pitch",
        "Landing page única",
        "Prototype web multi-tela",
        "Dashboard / ferramenta interna",
        "Peça editorial / marketing",
        "Outro — vou descrever"
      ]
    },
    {
      "id": "platform",
      "label": "Plataforma alvo",
      "type": "checkbox",
      "maxSelections": 4,
      "options": [
        "Responsivo web",
        "Desktop web",
        "iOS app",
        "Android app",
        "Tablet",
        "Desktop app",
        "Canvas fixo (1920×1080)"
      ]
    },
    {
      "id": "audience",
      "label": "Pra quem é?",
      "type": "text",
      "placeholder": "ex: investidores early-stage, comprador de dev-tools, exec interno"
    },
    {
      "id": "tone",
      "label": "Tom visual",
      "type": "checkbox",
      "maxSelections": 2,
      "options": [
        "Editorial / revista",
        "Modern minimal",
        "Lúdico / ilustrativo",
        "Tech / utilitário",
        "Luxury / refinado",
        "Brutalist / experimental",
        "Humano / próximo"
      ]
    },
    {
      "id": "brand",
      "label": "Contexto de marca",
      "type": "radio",
      "options": [
        "Escolha uma direção pra mim",
        "Já tenho brand spec — vou compartilhar",
        "Combinar com site/screenshot de referência"
      ]
    },
    {
      "id": "scale",
      "label": "Mais ou menos quanto?",
      "type": "text",
      "placeholder": "ex: 8 slides, 1 LP + 3 sub-páginas, 4 telas mobile"
    },
    {
      "id": "constraints",
      "label": "Algo mais que eu precise saber?",
      "type": "textarea",
      "placeholder": "Copy real, fontes obrigatórias, coisas a evitar, deadline…"
    }
  ]
}
</question-form>
```

## Regras

1. **Sempre na Turn 1.** Antes de qualquer Bash, Read, TodoWrite, thinking estendido.
2. **STOP after the form.** Não começa a construir antes do usuário responder.
3. **Pular se for tweak pequeno.** Se o usuário disse "muda só a cor do botão", não fazer discovery.
4. **Default sensível.** Se o usuário pula um campo, assumir o mais comum e seguir.

## Por que funciona

- Tempo até primeiro byte: ~2 segundos (renderizar o form é instantâneo)
- Reduz ambiguidade em ~80% (medido empiricamente pelo time do Open Design)
- Força o usuário a pensar em **escopo** antes de pedir

---

**Fonte:** `apps/daemon/src/prompts/discovery.ts` (262 linhas)
