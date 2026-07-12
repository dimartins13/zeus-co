# zeus-co-universidade

A **Universidade Zeus-CO**: a skill que faz os especialistas consultarem a biblioteca de conhecimento (fonte + princípio + case) antes de opinar.

## Arquitetura (importante) — lê ao vivo, NÃO carrega cópia
A biblioteca **vive no Vault do Diego**, não dentro deste plugin:
```
/Users/diegomartins/Documents/Claude/Vault/20-biblioteca/
```
A skill `/universidade` lê esse caminho **ao vivo** (Cowork e Claude Code têm acesso ao filesystem via Bash). Assim o cérebro é **único e vivo**: qualquer edição no Obsidian — feita pelo Diego, pelo Claude Code ou por outputs do Cowork — aparece na hora, sem cópia e sem sync. Este plugin carrega só a *instrução*, não o *conteúdo*.

> Requer filesystem: funciona no **Cowork** e no **Claude Code**. No Claude.ai web (sem acesso a arquivos) a skill avisa que não consegue ler a biblioteca.

## Faculdades (no Vault)
- **CMO** — marketing, growth, tráfego pago, publicidade (técnicas + swipe + cases), branding.
- **CFO** — finanças de fundador: unit economics, runway/Default Alive, viabilidade, cap table, tributário BR.
- **CEO** — estratégia, PMF, liderança, sócios & governança.

## Estado
v1 **auditada** (não validada): ~109 fichas, aguardando o aval final do Diego (`auditado`→`validado`). Framework: `Vault/00-PROJETO-Universidade-Zeus-CO.md`.
