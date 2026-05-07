# CLAUDE.md — Template Otimizado

> CLAUDE.md ideal: <200 linhas, princípios + ponteiros, NÃO conteúdo inline detalhado.
> Lembrar: cada token aqui é cobrado em CADA turno. 5K tokens × 200 turnos = 1M tokens cobrados.

---

# {Nome do projeto/workspace}

> {1 frase descrevendo o que esse workspace contém. NÃO repetir conteúdo de outros docs.}
>
> Detalhes em [`{master-doc}.md`](./master-doc.md).

## Identidade do operador
{2-3 linhas — quem usa, qual perfil, papel}

## Princípios invioláveis (5 max)

1. **{princípio}** — {1 linha}
2. **{princípio}** — {1 linha}
3. **{princípio}** — {1 linha}
4. **{princípio}** — {1 linha}
5. **{princípio}** — {1 linha}

## Estrutura (mapa de ponteiros, NÃO conteúdo)

- [`MASTER.md`](./MASTER.md) — visão completa
- [`STATUS.md`](./STATUS.md) — estado atual
- `pasta-x/` — {1 linha}
- `pasta-y/` — {1 linha}

## Como começar qualquer chat
1. {ler X automático}
2. {se em pasta de subprojeto → ler Y}
3. {ativar skill correta para intent}

---

## Anti-padrões pra CLAUDE.md (NÃO fazer)

- ❌ Repetir documentação de framework / linguagem (já está no treinamento do Claude)
- ❌ Listar todos os arquivos do projeto (use `ls`/`find` quando precisar)
- ❌ Colar todas as decisões históricas (use ponteiro pra DECISIONS.md)
- ❌ Templates inline de código (use pasta `templates/`)
- ❌ Frases de cortesia ("por favor", "obrigado", "se possível") — Claude já entende
- ❌ Repetir mesma instrução de formas diferentes — escolha 1 redação clara
- ❌ Ler arquivo grande "automaticamente" no início — pull on demand

## Padrão de tamanho

| Tamanho CLAUDE.md | Custo/turno | Custo/mês (200 turnos) |
|---|---|---|
| 100 linhas (~1K tokens) | R$ 0.005 | R$ 1 |
| 500 linhas (~5K tokens) | R$ 0.025 | R$ 5 |
| 2000 linhas (~20K tokens) | R$ 0.10 | R$ 20 |

(Valores aproximados Sonnet, sem cache.)

**Meta: ≤200 linhas.**

## Próximos Movimentos

1. Auditar CLAUDE.md atual com `wc -l`
2. Mover detalhe inline pra docs externos referenciados
3. Re-medir tokens após enxugamento
