# Núcleo Cinematográfico — Decisões físicas

> Cérebro do sistema. Esse núcleo é **idêntico** independentemente do destino — só muda o formato de entrega.

## Princípios de prompt visual

### Descreva física, não adjetivos

Nano Banana 2 entende **linguagem narrativa natural**, não keywords. Parágrafos descritivos > listas de palavras-mágicas.

**NUNCA use:** `cinematic`, `epic`, `beautiful`, `dramatic`, `stunning`, `moody`, `ethereal`, `perfect composition`, `gorgeous`, `breathtaking`, `masterpiece`, `award-winning`, `best quality`, `4k`, `8k`, `hyperrealistic`, `ultra detailed`.

**SEMPRE descreva:** posição de câmera, lente, abertura, ISO, comportamento de luz, direção da sombra, curva tonal, saturação, textura de superfície.

Cinema real é levemente imperfeito. Assimetria, foco que dissolve, bordas tocadas, luz não-balanceada. **Imperfeição controlada** separa "renderizado" de "filmado".

### Os 6 pilares

Toda imagem precisa responder, em ordem narrativa:

1. **Sujeito + ação** — o que é, o que acontece
2. **Ambiente + hora + condição** — onde, quando, sob qual atmosfera
3. **Câmera + lente + posição** — modelo, focal, T-stop, altura, ângulo
4. **Luz** — fonte motivada, Kelvin, direção, comportamento de sombra
5. **Pele, figurino, textura** — materiais e como reagem à luz
6. **Post / formato** — stock de filme, grão, halation, curva tonal

Tudo que não carrega peso visual deve ser cortado.

### Ângulos inusitados são obrigatórios

A imagem precisa ser **impactante**, não genérica:
- Estilo artístico, pouco convencional
- Iluminação e composição nada comuns
- Ângulo inusitado: low-angle, floor-level, hip-level, high-angle vertical, POV oblíquo, intercepted framing
- Zero texto na imagem (letras, números, logos, watermarks)

Traduza em **decisões físicas**, NÃO em adjetivos.

---

## Câmeras — apenas DUAS opções

Trave o sistema. Negue qualquer outra.

### IMAX MK IV 65mm (ISO 250)
Cenas contemplativas, grandes, ritualísticas, retratos densos, escala, silêncio.

**Lentes coerentes:**
- Zeiss Makro-Planar 65mm T2.2 — close-ups, retratos, rituais, objetos
- Hasselblad/Zeiss 80mm T2.2 — medium-wide, interiores, composições calmas
- Zeiss Otus 85mm T2.5 — retratos densos
- Leica Summilux-C 40mm T1.4 — wide natural

### ARRI Alexa 35 (ISO 800)
Cenas narrativas, urbanas, noturnas, dinâmicas, com movimento.

**Lentes coerentes (Canon K35 rehoused, T1.5 spherical):**
- Canon K35 24mm T1.5 — wide dinâmico
- Canon K35 35mm T1.5 — narrativa padrão, handheld **(default)**
- Canon K35 55mm T1.5 — retrato urbano
- Canon K35 85mm T1.8 — close-up

**Em dúvida: Alexa 35 + K35 35mm.**

---

## POST BEHAVIOR — assinatura visual crítica

Carrega a assinatura visual. **Nunca genérico, nunca template, nunca repetir o mesmo stock por hábito.**

### Por FORMATO (preferido pela concisão):
- IMAX 65mm → `65mm film grain structure`
- Alexa 35 → `35mm film grain structure`

### Por STOCK específico (quando o look pede):

| Look | Stock |
|---|---|
| Neon tungsten noite urbana | Kodak Vision3 500T 5219 |
| Diurno natural, verde/folha | Kodak Vision3 250D 5207 |
| Pastel urbano, interiores mistos | Fuji Eterna 500T 8573 |
| Preto e branco alto contraste | Kodak Double-X 5222 |
| Print final, skin tones ricos | Kodak 2383 print |
| 16mm indie/documental | Kodak 7219 ou 7222 B&W |

**Grão sempre VISÍVEL.** Use `visible`, `tactile`, `organic`, `heavy`, `coarse`, `prominent`. **Nunca** `subtle`, `fine`, `barely visible`.

**Nunca** sprocket holes, film borders, film strip frames, frame numbers. Imagem full-bleed.

---

## Formato de entrega — Nano Banana 2

Em inglês, parágrafos por aspecto, começando em `CAMERA:` e terminando em `MOOD & ART DIRECTION:`.

### Regras de formato

- **SEM** "## Abordagem", **SEM** preamble em português
- **SEM** "## Prompt Final", **SEM** header de seção
- **SEM** SCENE HEADER em CAPS no topo (ex: "EXT. LOCAL — NIGHT —")
- **SEM** bloco de proibições em CAPS no final (NO TEXT, NO WATERMARK)
- **SEM** markdown (##, **, -, bullets, numeração)
- **SEM** parágrafo "Inspired by [diretor] in [filme]" — só a linha final genérica
- **SEM** HEX codes, **SEM** COLOR ROLE MAPPING, **SEM** W3C anchors
- **SEM** emojis, **SEM** perguntas, **SEM** meta-comentários

Cada parágrafo abre com um header contextual em CAPS seguido de dois pontos.

### Parágrafos obrigatórios (nesta ordem)

```
CAMERA: corpo, ISO, posição.
LENS: modelo, focal, T-stop, distância, foco.
LIGHT: fonte motivada, Kelvin, direção, comportamento de sombra, IRE aproximado.
SUBJECT: posição corporal, ângulos, estado físico. Intercepted.
FOREGROUND: zona próxima, textura, dissolução do foco.
MIDGROUND: zona do sujeito, comportamento do foco.
BACKGROUND: profundidade, bokeh.
WARDROBE TONAL BEHAVIOR: material, comportamento sob luz.
MAKEUP SURFACE PHYSICS: textura de pele real, suor, oleosidade, poros.
POST BEHAVIOR: formato ou stock, grão visível, halation, curva, saturação, midtone priority.
COMPOSITIONAL GEOMETRY: peso visual, assimetria, intrusion, terços quebrados.
MOOD & ART DIRECTION: Composition and art direction inspired in the work of award-winning directors.
```

### Limite

Output total: **NO MÁXIMO 1.500 caracteres**, mire em 1.200–1.450. Corte adjetivos. Preserve decisões físicas.

### Com imagem de referência

Leia mood, stock, cor, hora — preserve identidade do sujeito. Em fluxo Nano Banana 2 com referência, use `@img1` no parágrafo `SUBJECT:`.

---

## Comando de render

Sem referência:

```bash
higgsfield generate create nano_banana_2 --prompt "$PROMPT" --aspect_ratio "4:5" --resolution "2k"
```

Com referência:

```bash
higgsfield generate create nano_banana_2 --prompt "$PROMPT" --image "$REF_UUID" --aspect_ratio "4:5" --resolution "2k"
```

**Regra global:** render real sempre em `higgsfield generate create nano_banana_2`. Não trocar de modelo como fallback. Se falhar, ajustar prompt/refs/login/aspect ratio/resolução e tentar novamente.

---

## Inspiração (USO INTERNO — nunca citar)

Roger Deakins, Bradford Young, Hoyte van Hoytema, Christopher Doyle, Robbie Ryan, Darius Khondji, Emmanuel Lubezki, Greig Fraser. Use a **filosofia**, não o visual.

A única referência permitida no output:

```
Composition and art direction inspired in the work of award-winning directors.
```
