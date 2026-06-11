---
name: human-upscale
description: Retexturização fotorrealista 8K que mata o "plastic look" típico de imagem gerada por IA — pele cerosa, tecido sintético sem trama, metal liso demais, madeira sem grão, luz "renderizada" em vez de captada. Aplica dois passes em camada - (1) SKIN-TEXTURE-DETAIL - reintroduz poro, peluginha facial, micro-rugas naturais, brilho oleoso pontual em zona-T, vermelhidão sutil em região perinasal e orelhas; (2) HIGH-FIDELITY FABRIC WEAVE - tecidos ganham trama detectável (chambray weave, denim slub, malha jersey costela, couro com grão Cabra/Cromo, lã merino fio cardado), com micro-sombra em cada fio. Preserva 100% da identidade do assunto — silhueta, proporção facial, cor de pele, cor dos olhos, expressão, gesto, paleta da imagem original. Resultado 4× ou 8× linear (input 2k → output 8k ou 16k) com noise grain de filme analógico aplicado por cima (Kodak Portra 400 ou Ilford HP5 simulado) pra reforçar leitura de captura física. Pipeline - 1) detecta áreas (pele/tecido/cabelo/metal/madeira/folhagem) via passes de segmentação; 2) aplica recipe-de-textura específica por tipo de material; 3) re-renderiza luz secundária (subsurface scattering em pele, anisotropic em cabelo/metal); 4) injeta grain final; 5) salva original + 8K + diff side-by-side. Stack - Higgsfield CLI (Nano Banana 2 modo refine/inpaint) ou Magnific/Topaz como fallback se Higgsfield falhar; ffmpeg pra processo em batch; Pillow pra compose side-by-side. Use SEMPRE para "/upscale", "/human-upscale", "mata plastic look", "tira cara de IA", "fotorrealismo 8K", "retexturizar", "pele com poro", "tecido com trama", "imagem de IA parece fake", "imagem gerada precisa de textura", "subir resolução com qualidade", "upscale cinematográfico", "8K fotorrealista", "grain de filme", "Kodak Portra grain", "preservar identidade aumentar resolução", "imagem chapada demais", "rosto liso demais", "tecido sintético demais", "madeira sem grão", "metal renderizado demais", colar imagem gerada por IA pedindo "deixa mais real", "tira cara de Midjourney". NÃO use para gerar imagem nova (→ `/human-image`), nem pra animar (→ `/human-motion`), nem pra montar carrossel (→ `/human-carrossel`).
---

# Human Upscale — Retexturização Fotorrealista 8K

Você mata o "plastic look" típico de IA. Pele de cera vira pele com poro. Tecido sintético vira tecido com trama. Madeira lisa vira madeira com grão. **Preserva 100% da identidade** — silhueta, proporção, cor, expressão, gesto, paleta — e devolve em 8K com grain analógico que reforça leitura de captura real.

## A regra dura

- **Identidade é sagrada.** Você NÃO altera rosto, proporção, expressão, gesto, paleta, framing. Você só **retexturiza** e amplia.
- **Você não cria detalhe ausente** (tatuagem nova, dente novo, anel novo). Só reforça textura do que já existe.
- **Você não muda a luz dramaticamente.** Só re-renderiza camada secundária (subsurface scattering em pele, anisotropic em cabelo/metal) — luz principal e direção ficam.
- **Você não força grain agressivo.** Grain serve à leitura analógica, não à decoração. Default = Kodak Portra 400 sutil.
- **Você não usa Magnific/Topaz sem o usuário saber.** Higgsfield é primário. Fallback é declarado.

## Pré-requisitos

```bash
which higgsfield && higgsfield account status
which ffmpeg
python3 -c "from PIL import Image; print('ok')"
```

Higgsfield CLI logado (email + créditos), `ffmpeg` pra batch, Pillow pra compose side-by-side.

## Pasta de trabalho

```
human-output/human-upscale/{run_slug}/
├── original.jpg          ← input copiado (intocado)
├── upscaled-8k.png       ← output final (4× ou 8× linear)
├── diff-side-by-side.png ← original vs final pra QC visual
├── recipe.json           ← passes aplicados, intensidades, semente
├── prompt-refine.txt     ← prompt enviado ao Higgsfield
└── manifest.json         ← input, decisões, comandos exatos
```

---

## Fluxo

### 1. Leia a imagem de input

```bash
file {imagem-input}
identify {imagem-input}   # se ImageMagick disponível, senão Pillow
```

Olhe direto (você enxerga imagens). Identifique:
- **Assunto dominante**: rosto humano? produto? cenário? híbrido?
- **Tipo de pele** (se houver pessoa): clara/média/escura, com/sem maquiagem visível
- **Materiais visíveis**: tecidos (algodão? denim? seda? couro?), cabelo (liso/cacheado/crespo), metal, madeira, folhagem, vidro
- **Cara de IA presente**: pele cerosa? tecido chapado? olhos com gleam plástico? sombra sem dispersão?
- **Resolução atual**: 1k? 2k? 4k?

### 2. Decida recipe-de-textura

Por tipo de material, recipe específica:

| Material detectado | Recipe |
|---|---|
| **Pele facial** | poro visível em zona-T, peluginha periférica (têmpora, mandíbula, lábio superior se masculino), micro-rugas em pés-de-galinha e linha de expressão, brilho oleoso sutil em testa/nariz, vermelhidão perinasal e nas orelhas |
| **Pele de corpo (braço, ombro, mão)** | foliculação visível, grão fino, sombra de pelo periférico, veia sutil onde anatomia pede |
| **Cabelo liso** | fio individual visível em borda, anisotropic specular ao longo do comprimento, fly-aways naturais |
| **Cabelo cacheado/crespo** | definição de cacho com micro-frizz, brilho difuso (não specular), volume com sombra interna |
| **Algodão / chambray / linho** | trama detectável (chambray weave), fios irregulares, micro-pilling discreto |
| **Denim** | slub characteristic, twill diagonal visível, desgaste de ponto (whisker, honeycomb) se houver |
| **Couro** | grão de Cabra ou Cromo (textura natural irregular), micro-poro, brilho difuso não uniforme |
| **Malha jersey / lã** | costela ou fio cardado visível, profundidade entre laços, micro-sombra |
| **Seda / cetim** | sheen direcional anisotropic forte, micro-rugas onde pano cai, baixa rugosidade |
| **Madeira** | grão na direção da fibra, nó ocasional, oleamento se acabamento, micro-imperfeição |
| **Metal escovado** | escovação direcional, anisotropic, micro-arranhão se mate; specular forte se polido |
| **Metal pintado/lacado** | clear coat sutil, orange peel discreto |
| **Folhagem** | veia da folha, micro-imperfeição (corte, mordida de inseto), reflectância variável |
| **Vidro** | dust/smudge sutil em superfície, refração consistente, double-reflection onde houver |

### 3. Monte o prompt-refine (inglês, declarativo)

Estrutura — **um parágrafo por aspecto**, igual ao prompt-spine de `human-image`:

```
PRESERVE: identity, facial proportion, skin tone, eye color, expression, gesture, framing, color palette, lighting direction.

ENHANCE TEXTURE: skin shows visible pores in T-zone with subtle oily sheen, faint vellus hair on temples and jawline, gentle redness on nose wings and ear rims, micro-wrinkles around eyes and mouth corners. Fabric shows detectable chambray weave with irregular threads, micro-pilling on collar edges. Hair shows individual strand definition at silhouette edge, anisotropic specular along length, occasional fly-aways.

LIGHTING SECONDARY: re-render subsurface scattering on skin (warm bounce through ears, nose tip, fingertips). Anisotropic specular on hair and brushed metal. Soft contact shadows where skin meets fabric.

GRAIN: Kodak Portra 400 emulation, fine grain, subtle red shift in midtones, retained shadow detail.

OUTPUT: 8K (7680 × 4320 ou proporcional ao aspect ratio do input), PNG, sRGB.
```

### 4. Dispara

```bash
higgsfield refine \
  --input original.jpg \
  --prompt-file prompt-refine.txt \
  --strength 0.3 \
  --preserve-identity true \
  --output upscaled-8k.png \
  --model nano_banana_2
```

`strength 0.3` é o ponto onde retexturização aparece e identidade fica intacta. Acima de 0.5 começa a deformar rosto.

**Fallback se Higgsfield falhar:** declare ao usuário e proponha Magnific (subscription do usuário) ou Topaz Photo AI (one-shot). Não silencia.

### 5. Compose diff side-by-side

```python
from PIL import Image
orig = Image.open("original.jpg")
final = Image.open("upscaled-8k.png").resize(orig.size)
side = Image.new("RGB", (orig.width * 2 + 20, orig.height), "white")
side.paste(orig, (0, 0))
side.paste(final, (orig.width + 20, 0))
side.save("diff-side-by-side.png")
```

### 6. QC visual obrigatório antes de entregar

Olhe os dois lado a lado:

- [ ] Silhueta facial idêntica?
- [ ] Cor de pele idêntica (não esquentou nem esfriou)?
- [ ] Olhos: cor + posição + tamanho idênticos?
- [ ] Expressão idêntica (boca, sobrancelhas)?
- [ ] Tecido: trama apareceu sem alterar cor/silhueta?
- [ ] Grain visível mas não dominante?
- [ ] Sem artefato em borda (especialmente cabelo/orelha/dedo)?

Se qualquer item falhar: **re-roda com strength menor** (0.25 → 0.2) e prompt enxuto. Não entrega cara mudada.

### 7. Entregue + próximo passo

> "Pasta em `human-output/human-upscale/2026-06-02-retrato-X/`. Diff side-by-side em `diff-side-by-side.png`. Quer outra variação (grain mais forte / mais sutil), ou rola próxima?"

---

## Quando NÃO usar esta skill

- Gerar imagem **nova** (sem input visual) → `/human-image`
- **Animar** imagem → `/human-motion` (motion) ou `/human-cinematic` (live action / ad)
- Imagem com **assunto trocado** (mudar pessoa, mudar produto) → não é upscale, é geração; manda pra `/human-image` com referência
- **Foto real** (não gerada por IA) — pode até passar daqui, mas com strength muito baixo (0.15); só faz se a foto tem ruído chroma, blur ou compressão pesada

## Anti-padrões

- **Strength alto demais (>0.5).** Identidade vira outra pessoa.
- **Grain Kodak Portra empilhado com grain HP5.** Escolha um. Grain duplo vira ruído digital, não analógico.
- **Aumentar res sem retexturizar.** É só upscale dumb (waifu, bicubic). Não entrega "mata plastic look".
- **Forçar pele com 5 imperfeições onde input só tem 1.** Não é "mais real" — é caricatural.
- **Aplicar recipe de tecido em cima de plástico ou cerâmica.** Detecte material correto primeiro.

## Próximo passo

Cole a imagem (ou caminho) + 1 frase de intent. Eu olho, monto recipe, e te mostro o prompt-refine antes de disparar — você OK, eu rodo.
