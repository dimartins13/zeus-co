# Pipeline · Higgsfield

> **Status:** Sem MCP nativo dedicado. Integração via Claude in Chrome ou API direta.

## Quando o DESIGN-LAB (zeus-co-design-lab) aciona o Higgsfield

Higgsfield é o pesado da equipe. Aciona quando:
- **Brand film curto** (15-30s) para campanha
- **Hero shot animado** para LP ou deck premium
- **Vídeo motion** que precisa de qualidade cinematográfica IA
- **Conceito visual experimental** (efeitos que outras ferramentas não fazem)

Não aciona Higgsfield para:
- Vídeo simples / corte de imagem fixa → usar `remotion` ou `fal-video-edit`
- Animação de UI / scroll-trigger → usar `gsap-*`
- Vídeo educativo / explainer → roteiro publicitário + ferramenta mais barata

## Como acionar (3 opções)

### Opção A · Claude in Chrome (interativo, recomendado pra primeira tentativa)

```
1. mcp__claude-in-chrome__navigate → https://higgsfield.ai/
2. Login (se ainda não logado)
3. find + form_input para preencher o prompt do projeto
4. Upload de referência se necessário (mcp__claude-in-chrome__file_upload)
5. Aguardar geração (pode levar 2-5 minutos)
6. Download do MP4 resultante
```

### Opção B · Higgsfield API direta (quando volume justificar)

Higgsfield expõe API REST. Estrutura típica:
```
POST https://api.higgsfield.ai/v1/generate
Headers: Authorization: Bearer <API_KEY>
Body: {
  "prompt": "…",
  "duration": 5,
  "aspect_ratio": "16:9",
  "model": "soul-engine-v2" (ou variação)
}
```
Setup do API key fica em `docs-internos/credenciais.md` (não commitado).

### Opção C · Manual fallback

Para casos onde precisa de iteração visual com humano-na-loop, o agente
gera o prompt detalhado e entrega para o Diego rodar manualmente na UI.

## Limites e custo

- **Custo:** ~$X por geração (verificar saldo mensal antes de rodar)
- **Tempo:** 2-5 min por clip
- **Resolução:** até 1080p, mas vídeo curto (<30s)
- **Estilo:** funciona melhor para cenas atmosféricas, próximas e líricas. Pior para multidões, texto, mãos.

## Pipeline mais comum no Zeus

Para campanha premium → 1 Higgsfield hero (3-5s) + animação GSAP no resto da LP.

Para deck investor → 1 Higgsfield no slide 1 (intro) e slide 8 (visão futuro). 6 slides do meio: foto Freepik.

Para social TikTok/Reels orgânico → Higgsfield gera 3-5 cenas atmosféricas, edição em Remotion.
