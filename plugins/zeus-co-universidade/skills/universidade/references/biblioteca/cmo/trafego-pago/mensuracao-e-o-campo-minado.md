---
type: conceito
status: auditado
auditoria: aprovada-2026-07-11
confianca: alta
source: Meta Conversion Lift; conceito de incrementalidade / geo-lift
topics: [trafego-pago, mensuracao]
updated: 2026-07-11
---

# Atribuição last-click engana; incrementalidade é a verdade

**TL;DR:** Atribuição last-click credita a conversão ao último toque e superestima canais de fundo de funil. A pergunta certa não é "quem tocou por último", e sim "o que teria acontecido sem o anúncio" — isso é incrementalidade, medida por testes de lift.

Atribuição responde "a qual canal dou o crédito desta venda". Incrementalidade responde "esta venda existiu por causa do anúncio, ou teria acontecido de qualquer forma". São perguntas diferentes, e confundi-las é o erro mais caro do tráfego pago. Last-click, o modelo padrão histórico, dá todo o crédito ao clique final — tipicamente busca de marca e remarketing, que capturam demanda já existente. O resultado é reinvestir onde o retorno aparente é alto mas o incremento real é baixo.

O princípio para o fundador: ROAS de plataforma é um número de contabilidade interna do canal, não de verdade de negócio. Para decidir alocação, a referência é o teste de incrementalidade — Conversion Lift (Meta), experimentos geográficos (geo-lift) ou grupos de controle holdout — que compara expostos versus não-expostos e isola o efeito causal.

Quando aplica: sempre que se compara canais entre si, ou se avalia se cortar/escalar um canal muda a receita total. Especialmente crítico em contas com forte peso de marca e remarketing, onde o autoengano de last-click é maior.

Nuance e limite: testes de lift exigem volume e disciplina — janela, grupo de controle, significância — e nem toda conta tem escala para rodá-los de forma limpa. Na ausência de lift, o segundo melhor é triangular: MMM (marketing mix modeling), dados de plataforma e a métrica de negócio (novos clientes, receita incremental). O ponto doutrinário não é "abandone atribuição", é "não a trate como verdade causal".

## Fontes
- Meta Conversion Lift — metodologia de teste de incrementalidade com grupo de controle
- Conceito de geo-lift / experimentos geográficos — isolamento de efeito causal por região
- Literatura de incrementalidade e holdout testing — distinção entre atribuição e causalidade

## Aplicado em
- (a preencher com cases na construção)
