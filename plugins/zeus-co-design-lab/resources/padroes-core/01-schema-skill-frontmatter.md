# Padrão 01 · Schema do SKILL.md (frontmatter `od:`)

Toda skill do Open Design segue um YAML frontmatter padronizado. Importei o schema
aqui porque ele é compatível com o nosso padrão de skills do ZEUS-CO — vale a
pena alinhar os campos.

## Schema completo

```yaml
---
name: nome-kebab-case
description: |
  Descrição em 1-3 linhas. Quando a skill é acionada, o que ela faz,
  e quais palavras-chave disparam.
triggers:
  - "frase ou palavra-chave 1"
  - "frase ou palavra-chave 2"
od:                                      # bloco específico do Open Design
  mode: design-system | prototype | deck | image | video | template | audio | utility
  platform: desktop | mobile | universal
  scenario: planning | production | post-production
  category: marketing-creative | creative-direction | slides | documents | …
  upstream: "https://github.com/autor/repo-original"   # se vier de outro autor
  preview:
    type: html | iframe | static
    entry: arquivo-preview.html
    reload: debounce-100
  design_system:
    requires: true | false
    generates: true | false
    sections: [color-palette, typography, layout, components, motion, voice, brand, anti-patterns]
  inputs:
    - name: brief
      type: string
      required: true
      description: "…"
zeus:                                    # bloco específico do Zeus-Lab (NOSSO)
  tipo: skill | orquestrador-vertical | utility
  pai: zeus-co-design-lab | design-lab-orquestrador
---

# Corpo em Markdown — instruções para o agente
```

## Por que importa

- **Determinístico:** o orquestrador lê `od:mode` e `zeus:tipo` e roteia certo.
- **Atribuível:** `od:upstream` preserva a linhagem da skill.
- **Composável:** `design_system.requires/generates` declara dependências entre skills.

## Compatibilidade com ZEUS-CO

Skills do Zeus que ainda não têm `od:` block continuam funcionando.
Skills novas do Zeus-Lab devem ter **os dois blocos** (`od:` e `zeus:`)
para serem descobríveis por ambos os orquestradores.

## Exemplo real

Ver `skills/creative-direction/creative-director/SKILL.md` — esse é um
exemplo limpo com `upstream: https://github.com/smixs/creative-director-skill`.

---

**Fonte:** `apps/daemon/src/skills.ts` (parser do Open Design)
