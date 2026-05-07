# DAILY ALERT — {Data}

> Só dispara se há P0. Caso contrário, cron loga "varredura silenciosa, sistema saudável" e não notifica.

**Cron:** `pulse-daily` 8h
**Modelo recomendado:** Haiku (operação leve recorrente)

---

## ⚠️ ALERTAS P0 ({N})

### 1. {Empresa} — {Tipo de alerta}

- **O quê:** {descrição em 1 frase}
- **Desde:** {quando começou / há N dias}
- **Impacto se ignorar:** {1 frase}
- **LEP responsável:** {qual}
- **Ação imediata sugerida:** {1 frase imperativa}

### 2. ...

---

## 📋 Append em INBOX.md raiz

```markdown
## 🚨 [YYYY-MM-DD HH:MM] Daily Pulse — {N} P0 alertas

- **{Empresa 1}**: {alerta} → {ação imediata}
- **{Empresa 2}**: {alerta} → {ação imediata}

Detalhes em `~/.claude/plugins/marketplaces/zeus-co/plugins/zeus-co-pulse/skills/pulse/WEEKLY_DIGEST.md`
```

---

*Se 0 alertas: append simples "Pulse Diário {data}: 0 P0. Sistema saudável." e não pingar.*
