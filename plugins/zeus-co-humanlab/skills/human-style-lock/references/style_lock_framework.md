# Style Lock Framework — os 7 componentes em detalhe

Framework de decodificação: imagem de referência → padrão de estilo replicável. Cada componente: **o que olhar** → **como descrever** (termos que geradores entendem) → exemplos de vocabulário.

---

## 1. Paleta

**O que olhar:** quais cores dominam a área da imagem; quais aparecem como secundárias; existe 1 cor de acento que pontua; saturação geral (viva ou lavada); brilho (high-key claro ou low-key escuro); contraste entre cores (complementares brigando ou análogas harmônicas).

**Como descrever:** dominante + secundárias + acento, com adjetivo de saturação e contraste.

**Vocabulário:** `muted earth tones` · `vibrant saturated cyan + warm yellow accents` · `monochromatic teal` · `pastel wash, low contrast` · `high contrast complementary orange-blue` · `desaturated except for red accent` · `nuanced whites, warm grays`.

## 2. Iluminação

**O que olhar:** luz dura (sombras de borda nítida) ou suave (transição gradual); de onde vem (cima/lado/contra/baixo); temperatura — quente (~3200K tungstênio, golden hour) vs neutra (~5500K daylight) vs fria (~7000K+ sombra/azulada); 1 fonte ou várias; sombras densas ou abertas.

**Como descrever:** qualidade + direção + temperatura + comportamento das sombras.

**Vocabulário:** `soft diffused light from upper left, ~5500K` · `hard directional sidelight, deep shadows` · `golden hour backlight, warm rim light` · `single practical source, motivated low-key` · `flat overcast light, open shadows` · `harsh on-camera flash, hard falloff` · `chiaroscuro, single window light`.

## 3. Composição

**O que olhar:** enquadramento (wide/medium/close/macro); regra usada (terços, simetria central, diagonal, moldura natural); profundidade (camadas FG/MG/BG ou plano único); onde o olho cai primeiro (ponto focal); equilíbrio (cheio vs respiro).

**Como descrever:** enquadramento + regra + profundidade + ponto focal.

**Vocabulário:** `centered symmetrical composition` · `rule of thirds, subject left, negative space right` · `low angle wide shot, strong foreground element` · `tight close-up, shallow layered depth` · `flat lay, overhead grid` · `dutch angle, diagonal tension`.

## 4. Textura

**O que olhar:** grão visível (filme analógico) ou limpo digital; nitidez geral (crisp ou soft/dreamy); acabamento das superfícies (matte fosco ou glossy reflexivo); ruído/imperfeição proposital.

**Como descrever:** grão + nitidez + acabamento.

**Vocabulário:** `visible film grain, Portra 400` · `clean digital, razor sharp` · `soft dreamy diffusion, slight halation` · `matte finish, no specular highlights` · `glossy, wet-look reflections` · `gritty texture, analog imperfections`.

## 5. Lente/câmera

**O que olhar:** compressão de perspectiva (tele achata, wide distorce); DOF (fundo derretido f/1.4 ou tudo em foco f/16); distorção/vinheta de lente; look de formato (35mm filme, médio formato, digital limpo, anamórfico com flare horizontal e bokeh oval).

**Como descrever:** lente + abertura + formato/filme. Modelos reais puxam o look — vocabulário completo de câmera/lente na biblioteca canônica §10 (Cinema Shot).

**Vocabulário:** `85mm f/1.4, melted bokeh background` · `28mm wide, slight barrel distortion` · `anamorphic, oval bokeh, horizontal flare` · `shot on ARRI Alexa 35` · `vintage Helios 44-2, swirly bokeh` · `medium format look, creamy falloff`.

## 6. Mood/atmosfera

**O que olhar:** que emoção a imagem dá na primeira olhada (tensão, calma, nostalgia, energia, luxo, melancolia); gênero estético reconhecível (editorial de moda, documental, cyberpunk, brutalist, cottagecore, Y2K, minimalismo nórdico).

**Como descrever:** emoção + gênero estético.

**Vocabulário:** `moody and contemplative, neo-noir` · `energetic, urban streetwear editorial` · `serene, Scandinavian minimalism` · `nostalgic, 90s film snapshot` · `opulent, dark luxury` · `raw documentary immediacy`.

## 7. Pós (pós-produção)

**O que olhar:** color grading reconhecível (teal-orange, bleach bypass, cross-process, sépia); vinheta; efeitos (halation, bloom, light leak, glitch, dupla exposição).

**Como descrever:** grade + efeitos.

**Vocabulário:** `teal-orange blockbuster grade` · `lifted blacks, faded film look` · `heavy vignette, edge darkening` · `halation on highlights` · `light leak warm edge` · `clean neutral grade, true-to-life color`.

---

## Síntese — montar a receita

Ordem da frase: **mood → paleta → luz → composição → lente → textura → pós**. Exemplo completo:

> "Moody urban streetwear editorial: desaturated concrete grays with a single red accent, hard directional sidelight ~4300K with deep shadows, low-angle medium shot with strong negative space above, 35mm f/2 with subtle barrel distortion, visible film grain and matte finish, lifted blacks with faded film grade."

Token MJ compacto da mesma receita:
`urban streetwear editorial, desaturated grays + red accent, hard sidelight deep shadows, low angle negative space, 35mm f/2, film grain matte, lifted blacks faded grade --sref <img>`

## Teste de validação

Render com sujeito DIFERENTE da referência. O estilo segurou se os 7 componentes sobreviveram à troca de assunto. Componentes que mais escapam: **iluminação** (gerador volta pro soft default) e **textura** (gerador volta pro digital limpo). Se escapou: reforce o componente no início da receita e re-teste 1×.

## Quebra-consistência (checklist QA antes de entregar)

- [ ] Algum componente descrito de forma vaga ("luz bonita", "cores legais")?
- [ ] A receita mistura moods ("serene" + "energetic")?
- [ ] Focou em paleta e esqueceu luz/textura/composição?
- [ ] Os termos estão em inglês técnico de foto/design (o que geradores entendem)?
