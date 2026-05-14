# Skills Detalhadas INDEX — Quick Lookup

> 51 skills upstream do Open Design curadas, organizadas em 11 categorias.
> Orquestrador puxa on-demand quando uma das 12 skills planas precisa de detalhe.

## Mapping skill plana → skills detalhadas a puxar

### `design-lab-deck` puxa:
- `deck-slides/slides` — base abstrata pra slides
- `deck-slides/pptx` — Anthropic native, export PPTX
- `deck-slides/pptx-generator` — gerador estruturado
- `deck-slides/nanobanana-ppt` — pattern alternativo
- `deck-slides/frontend-slides` — HTML/React slides
- **Cross**: pode chamar `marketing-creative/ad-creative` se for sales deck

### `design-lab-landing-page` puxa:
- `web-artifacts/frontend-design` — React/HTML LP
- `web-artifacts/artifacts-builder` — base builder
- `web-artifacts/web-artifacts-builder` — Anthropic native
- `prototipagem/faq-page` — sub-component
- `prototipagem/login-flow` — sub-component
- **Cross**: `marketing-creative/copywriting` pra copy + `marketing-creative/paywall-upgrade-cro` se pricing

### `design-lab-magazine-editorial` puxa:
- `templates-editoriais/after-hours-editorial-template` — moderno editorial
- `templates-editoriais/digits-fintech-swiss-template` — Swiss-style
- `templates-editoriais/editorial-burgundy-principles-template` — premium editorial
- `templates-editoriais/field-notes-editorial-template` — magazine pocket-size
- `templates-editoriais/swiss-creative-mode-template` — Swiss design system
- **Cross**: `creative-direction/creative-director` pra direção

### `design-lab-email-html` puxa:
- `marketing-creative/copywriting` — body + subject
- `marketing-creative/marketing-psychology` — gatilhos psicológicos
- `marketing-creative/paywall-upgrade-cro` — upgrade emails
- **Cross**: nenhuma específica de email no upstream — usa templates web ajustados

### `design-lab-social-carousel` puxa:
- `marketing-creative/ad-creative` — copy + hook
- `marketing-creative/copywriting` — captions
- `marketing-creative/competitive-ads-extractor` — análise concorrentes
- `marketing-creative/marketing-psychology` — engagement triggers
- **Cross**: `zeus-co-marketing:instagram-carousel-builder` (skill especializada existente fora deste plugin)

### `design-lab-poster-key-visual` puxa:
- `creative-direction/creative-director` — direção visual macro
- `creative-direction/design-consultation` — input estratégico
- `creative-direction/design-review` — QA visual
- `creative-direction/brainstorming` — geração de conceitos
- `creative-direction/plan-design-review` — checklist review
- `image-generation/imagegen` — geração base
- **Cross**: `marketing-creative/ad-creative` pra headline

### `design-lab-motion-frames` puxa:
- `animation-motion/gsap-core` — GreenSock base
- `animation-motion/gsap-react` — GSAP em React
- `animation-motion/gsap-scrolltrigger` — scroll-driven
- `animation-motion/gsap-timeline` — timelines complexas
- `animation-motion/flutter-animating-apps` — mobile motion

### `design-lab-image-generation` puxa:
- `image-generation/imagegen` — base abstrata
- `image-generation/imagen` — Google Imagen
- `image-generation/sora` — OpenAI Sora (image mode)
- `image-generation/fal-generate` — Fal.ai pipeline
- `image-generation/replicate` — Replicate models
- `image-generation/enhance-prompt` — prompt engineering

### `design-lab-video-generation` puxa:
- `video-generation/fal-kling-o3` — Kling video
- `video-generation/fal-video-edit` — video editing
- `video-generation/remotion` — Remotion React-based video

### `design-lab-design-system` puxa:
- `design-system-tools/color-expert` — paleta science
- `design-system-tools/design-md` — DESIGN.md generator
- `design-system-tools/screenshots-marketing` — marketing screens
- `design-system-tools/web-design-guidelines` — guidelines builder

### `design-lab-orquestrador` (cross-cutting):
- `creative-direction/brainstorming` — antes de qualquer escolha
- `creative-direction/design-consultation` — fase descoberta
- `prototipagem/design-brief` — brief estruturado
- `creative-direction/plan-design-review` — review final
- **Plus**: usa `documents/doc/docx/pdf` quando precisa exportar deliverable formato específico

### `design-lab-discovery` (entry point novo brief):
- `prototipagem/design-brief` — formulário brief canônico
- `creative-direction/design-consultation` — descoberta input
- `creative-direction/brainstorming` — ideação inicial

## Skills sem categoria mas úteis cross-cutting

- `marketing-creative/domain-name-brainstormer` — naming (cross com `zeus-co-naming-domain`)
- `prototipagem/release-notes-one-pager` — release one-pager (cross com publisher)

## Quando NÃO puxar skill detalhada

- Brief curto (< 3 perguntas) → skill plana é suficiente, não puxa detalhada
- Diego pede output rápido → pula puxar skill detalhada, usa pattern da skill plana
- Skill detalhada upstream depende de runtime deles (daemon, Express) → adapta logicamente, não importa código

## Como o orquestrador decide

```python
# Pseudo
def decide_skills_a_puxar(brief, skill_plana_alvo):
    # 1. Skill plana sempre é o entry point
    skills = [skill_plana_alvo]
    
    # 2. Olha mapping acima (skill plana → detalhadas)
    skills.extend(mapping[skill_plana_alvo])
    
    # 3. Se brief crítico, adiciona QA
    if brief.is_critical or brief.client_facing:
        skills.append("creative-direction/design-review")
        skills.append("creative-direction/plan-design-review")
    
    # 4. Cross com ZEUS-CO se aplicável
    if brief.envolve_brand:
        skills.append("zeus-co-cco:cco-brand-guardian")  # externo
    if brief.envolve_copy:
        skills.append("zeus-co-cco:cco-copy-master")  # externo
    
    return skills
```
