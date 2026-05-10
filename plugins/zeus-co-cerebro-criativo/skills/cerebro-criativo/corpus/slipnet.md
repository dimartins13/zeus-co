# SLIPNET — Rede conceitual com pesos (inspirada Copycat / Hofstadter)

> Implementação textual de slipnet — rede de conceitos com pesos de associação. Skill consulta antes de gerar pra **ativar nodes distantes** do briefing, forçando criatividade real.

## Como ler

Cada **node** é um conceito central. Cada **link** é uma conexão com **peso qualitativo**:
- **FORTE** (━━━): associação canônica, ativação automática
- **MÉDIO** (───): associação razoável, requer ponte
- **FRACO** (∙∙∙): associação distante, força slippage criativo
- **OPOSTO** (✕✕✕): polo oposto no espaço — útil pra Break/Reverse

Skill **prefere ativar nodes via links FRACO** (criatividade) sobre FORTE (clichê).

---

## Node: MARCA

```
MARCA
├━━━ identidade
├━━━ comunicação
├━━━ valor
├━━━ logo
├─── narrativa
├─── reputação
├─── distinctiveness
├─── associação semântica
├∙∙∙ devoção (religião)
├∙∙∙ tribo (esporte)
├∙∙∙ DNA (biologia)
├∙∙∙ assinatura (arquitetura) 
├∙∙∙ riff (música)
├∙∙∙ receita (gastronomia)
├∙∙∙ avatar (jogos)
└✕✕✕ commodity
```

## Node: CLIENTE

```
CLIENTE
├━━━ consumidor
├━━━ comprador
├─── usuário
├─── prospect
├─── fã
├∙∙∙ fiel (religião)
├∙∙∙ atleta (esporte)
├∙∙∙ jogador (jogos)
├∙∙∙ hospedeiro (biologia simbionte)
├∙∙∙ comensal (gastronomia)
├∙∙∙ habitante (arquitetura)
├∙∙∙ ouvinte (música)
└✕✕✕ adversário
```

## Node: PRODUTO

```
PRODUTO
├━━━ feature
├━━━ benefício
├━━━ commodity
├─── solução
├─── experiência
├─── serviço
├∙∙∙ ritual (religião)
├∙∙∙ jogada (esporte)
├∙∙∙ órgão (biologia)
├∙∙∙ cômodo (arquitetura)
├∙∙∙ track (música)
├∙∙∙ prato (gastronomia)
├∙∙∙ quest (jogos)
└✕✕✕ vácuo (ausência)
```

## Node: COMPRA

```
COMPRA
├━━━ transação
├━━━ pagamento
├─── decisão
├─── conversão
├∙∙∙ comunhão (religião)
├∙∙∙ gol (esporte)
├∙∙∙ ovo fertilizado (biologia)
├∙∙∙ entrada (arquitetura)
├∙∙∙ drop (música)
├∙∙∙ pedido (gastronomia)
├∙∙∙ unlock (jogos)
└✕✕✕ desistência
```

## Node: COMUNIDADE

```
COMUNIDADE
├━━━ usuários
├━━━ engagement
├─── network effect
├─── retenção
├∙∙∙ congregação (religião)
├∙∙∙ time/torcida (esporte)
├∙∙∙ ecossistema (biologia)
├∙∙∙ vila (arquitetura)
├∙∙∙ cena (música)
├∙∙∙ mesa coletiva (gastronomia)
├∙∙∙ guild (jogos)
└✕✕✕ indivíduo isolado
```

## Node: LANÇAMENTO

```
LANÇAMENTO
├━━━ campanha
├━━━ pre-launch
├─── go-to-market
├─── soft launch
├∙∙∙ rito de passagem (religião)
├∙∙∙ pre-temporada (esporte)
├∙∙∙ eclosão (biologia)
├∙∙∙ inauguração (arquitetura)
├∙∙∙ drop / show ao vivo (música)
├∙∙∙ apresentação chef (gastronomia)
├∙∙∙ release game (jogos)
└✕✕✕ encerramento
```

## Node: CONTEÚDO

```
CONTEÚDO
├━━━ post
├━━━ vídeo
├━━━ artigo
├─── newsletter
├─── podcast
├∙∙∙ sermão (religião)
├∙∙∙ comentário esportivo (esporte)
├∙∙∙ feromônio (biologia)
├∙∙∙ inscrição mural (arquitetura)
├∙∙∙ letra de música (música)
├∙∙∙ menu (gastronomia)
├∙∙∙ briefing missão (jogos)
└✕✕✕ silêncio
```

## Node: DECISÃO

```
DECISÃO
├━━━ escolha
├━━━ deliberação
├─── trade-off
├─── julgamento
├∙∙∙ profecia (religião)
├∙∙∙ pênalti (esporte)
├∙∙∙ seleção natural (biologia)
├∙∙∙ projeto arquitetônico (arquitetura)
├∙∙∙ mixagem (música)
├∙∙∙ ordem do menu (gastronomia)
├∙∙∙ build / strategy (jogos)
└✕✕✕ paralisia
```

## Node: PREÇO

```
PREÇO
├━━━ valor monetário
├━━━ pricing
├─── posicionamento
├─── elasticidade
├∙∙∙ ofertório (religião)
├∙∙∙ cachê (esporte)
├∙∙∙ custo energético (biologia)
├∙∙∙ cota condominial (arquitetura)
├∙∙∙ ingresso (música)
├∙∙∙ couvert (gastronomia)
├∙∙∙ moeda do jogo (jogos)
└✕✕✕ gratuidade
```

## Node: ERRO

```
ERRO
├━━━ bug
├━━━ falha
├─── churn
├─── feedback negativo
├∙∙∙ pecado (religião)
├∙∙∙ falta (esporte)
├∙∙∙ mutação maligna (biologia)
├∙∙∙ rachadura (arquitetura)
├∙∙∙ nota desafinada (música)
├∙∙∙ queimado (gastronomia)
├∙∙∙ game over (jogos)
└✕✕✕ perfeição
```

## Node: CRESCIMENTO

```
CRESCIMENTO
├━━━ aquisição
├━━━ revenue
├─── escala
├─── tração
├∙∙∙ multiplicação (religião)
├∙∙∙ campeonato (esporte)
├∙∙∙ proliferação celular (biologia)
├∙∙∙ verticalização (arquitetura)
├∙∙∙ tour mundial (música)
├∙∙∙ rede de franquias (gastronomia)
├∙∙∙ level up (jogos)
└✕✕✕ estagnação
```

## Como skill usa o slipnet

### Em geração — ativação de nodes distantes

1. Identifica node central do briefing (ex: "lançamento" pra TarjaPreta)
2. Lista links **FRACO** (∙∙∙) — domínios distantes
3. Para cada link fraco, puxa léxico correspondente em `corpus/lexicons/`
4. Gera ideia mapeando: "lançamento como [rito de passagem / pre-temporada / eclosão / etc]"
5. Cada mapping vira candidata Bend ou input pra Blend

### Em stress-test — checagem de distância

Após gerar ideia, skill verifica:
- A ideia ativa qual node?
- Qual link foi usado pra chegar nela?
- Se FORTE (━━━): ideia óbvia, baixa originalidade
- Se MÉDIO (───): aceitável, mas pode melhorar
- Se FRACO (∙∙∙): boa originalidade
- Se OPOSTO (✕✕✕): Break interessante, validar viabilidade

### Em expansão — adicionando nodes ao slipnet

Cada uso aprovado pelo Diego pode **adicionar novos nodes ou links** ao slipnet. Aprendizagem viva da skill. Exemplo: se Diego validar "campanha TarjaPreta como liturgia", o link "lançamento ∙∙∙ liturgia" se fortalece pra próximas invocações (vira ───).

## Padrão de links FRACO mais ricos (alto retorno criativo)

Os links **mais valiosos pra criatividade** são os ∙∙∙ que CONECTAM dimensões aparentemente opostas:

- MARCA ∙∙∙ devoção (religião) — usado por: Apple, Liquid Death
- PRODUTO ∙∙∙ ritual (religião) — usado por: brindes carnaval, Hare Krishna mantras  
- COMPRA ∙∙∙ unlock (jogos) — usado por: SaaS gamificado
- LANÇAMENTO ∙∙∙ eclosão (biologia) — usado por: lançamentos com "incubação" pública
- CRESCIMENTO ∙∙∙ multiplicação (religião) — usado por: viral marketing missional
- COMUNIDADE ∙∙∙ ecossistema (biologia) — usado por: plataformas dev (GitHub)

Skill prioriza estes em geração de Bend/Blend.

## Princípio inviolável do slipnet

**Skill SEMPRE ativa pelo menos 2 nodes via links FRACO (∙∙∙) em qualquer geração.** Sem isso, vira recombinação dentro do óbvio, não criatividade neuro.
