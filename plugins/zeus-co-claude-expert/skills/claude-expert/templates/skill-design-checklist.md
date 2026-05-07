# Skill Design Checklist — {Nome da Skill}

> Antes de criar/atualizar skill. Garante que skill é eficiente em tokens E descobrível.

**Skill proposta:** {nome}
**Plugin owner:** {zeus-co-X}
**Justificativa de existência:** {por que precisa existir vs usar tool/MCP/hook existente}

---

## 1. Decisão arquitetural (ANTES de criar)

- [ ] Verificar se MCP existente já cobre — se sim, NÃO criar skill duplicada
- [ ] Verificar se hook resolve (caso seja determinístico/obrigatório)
- [ ] Verificar se subagent é melhor (caso seja pesquisa pesada com output isolável)
- [ ] Confirmar que SKILL é a forma certa: metodologia/conhecimento que Claude precisa SABER

## 2. Frontmatter

- [ ] `name`: kebab-case, único no workspace
- [ ] `description`:
  - [ ] Curta o suficiente pra ser carregada (200-400 chars ideal)
  - [ ] **Específica sobre QUANDO usar** (não só o que faz)
  - [ ] Inclui frases-gatilho do usuário ("Use SEMPRE que..." + lista de phrases)
  - [ ] "Pushy" — Claude sub-triggers por padrão, força com instrução explícita

## 3. Body (SKILL.md)

- [ ] **<500 linhas** ideal (regra Anthropic)
- [ ] Carrega apenas o necessário pra "saber operar a skill"
- [ ] Detalhes complexos vão pra arquivos secundários referenciados
- [ ] Templates ficam em `templates/`, não inline
- [ ] Scripts ficam em `scripts/`, executados sem load de contexto
- [ ] References em `references/`, carregados sob demanda

## 4. Progressive disclosure (3 níveis)

- [ ] **Nível 1 (sempre):** name + description
- [ ] **Nível 2 (quando ativada):** SKILL.md body
- [ ] **Nível 3 (sob demanda):** templates, scripts, references citados

## 5. Eficiência de tokens

- [ ] Sem repetição entre SKILL.md e templates/
- [ ] Sem comentários de código verbosos no SKILL.md
- [ ] Sem exemplos longos inline (use template referenciado)
- [ ] Linguagem direta, sem floreio

## 6. Activation testing

- [ ] Testar 3-5 phrases do usuário que devem ativar a skill
- [ ] Verificar que NÃO ativa em phrases não relacionadas (false positive)

## 7. Cron de evolução (se LEP)

- [ ] Cron semanal/mensal que atualiza LITERATURE/RADAR
- [ ] Modelo Haiku (não desperdiçar Sonnet/Opus em maintenance)

## 8. Documentação

- [ ] EVOLUTION.md inicializado v0.1.0
- [ ] LITERATURE.md com fontes (se LEP)
- [ ] RADAR.md (se LEP)

## Próximos Movimentos

1. Implementar com checklist completo
2. Testar activation 3-5 phrases
3. Adicionar a EVOLUTION.md changelog
