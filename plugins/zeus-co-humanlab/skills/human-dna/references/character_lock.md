# Character Lock — personagem/mascote consistente cross-cena

Método pra criar e manter **personagem ou mascote de marca** que permanece idêntico em qualquer pose, cena ou peça. Entra no DNA quando a marca tem (ou vai ter) personagem recorrente — mascote, avatar, personagem de campanha. Fonte: biblioteca canônica de IA criativa §6 (`zeus-co-humanlab/resources/biblioteca-ia-criativa.md`).

---

## A hierarquia de consistência (nesta ordem, sempre)

A consistência vem de **travar na ordem certa**. Quem trava cor antes de silhueta perde o personagem na terceira geração.

### 1º — Trava a SILHUETA (a âncora)

Forma da cabeça, orelhas, proporção torso/membros. Teste duro: a silhueta preta pura, sem detalhe interno, tem que ser **reconhecível em 2D** e **legível como ícone pequeno** (favicon, sticker 32px). Se a silhueta não identifica o personagem sozinha, volte antes de prosseguir.

### 2º — Cor/material MÍNIMOS

Paleta limpa (3-4 cores máx), pouca textura, toon shading. **1 cor de acento da marca** — e só nos acessórios, nunca espalhada. Quanto menos cor, mais reproduzível.

### 3º — Acessórios destacáveis que NÃO alteram a silhueta

Cachecol, coleira, boné, headset — itens que você troca por campanha/sazonalidade **sem quebrar a identidade**, porque a silhueta continua a mesma. É a camada de variação segura.

### 4º — Pose default + biblioteca de expressões intercambiáveis

1 pose canônica (a "pose de registro") + expressões intercambiáveis (sorriso, piscada, curioso, surpreso). Varia expressão e pose mantendo TODO o resto travado.

---

## Criação por atributos estruturados

Primeiro personagem: descrever por atributos, nunca por vibe solta — Tipo · Função · Personalidade · Aparência (cabelo, roupa peça-a-peça, acessórios) · Estilo visual.

> "A confident teenage protagonist in 3D style on white background, short curly hair, royal blue oversized hoodie, beige cargo pants, neon green sneakers, headphones around neck, playful expression, vibrant palette, soft lighting, stylized animation aesthetic, Pixar-inspired."

## Variação mantendo identidade (o prompt-chave)

> "Crie uma variação do personagem seguindo as características e o estilo de ilustração **de forma idêntica**, mas agora [virado de perfil pra esquerda / andando numa rua ao entardecer / segurando o produto X]."

A locução "de forma idêntica" + mudar SÓ pose/cena é o que trava a identidade. Sempre gere variações **a partir da imagem do personagem como referência**, nunca só por texto.

## O que registrar no DNA.md (seção Personagem, quando existir)

- Silhueta: descrição verbal + imagem da silhueta preta de registro
- Paleta do personagem (com a cor de acento da marca apontada)
- Acessórios canônicos vs. acessórios sazonais permitidos
- Pose default + lista de expressões aprovadas
- Prompt de registro (o atributo-estruturado completo) + prompt de variação
- UUIDs/paths das imagens de referência aprovadas (pra usar como ref em toda geração futura)

## Quebra-consistência (evitar)

- Gerar variação sem passar a imagem de referência (só texto = personagem deriva)
- Trocar acessório QUE ALTERA silhueta (capuz levantado, asa nova, mochila grande)
- Espalhar a cor de acento pro corpo do personagem
- Mudar estilo de render entre peças (3D numa, flat noutra)
