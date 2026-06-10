# Loom Zero

Behavioral guidelines for giving coding agents durable project memory. Paste into `AGENTS.md`, `CLAUDE.md`, or equivalent project instructions.

**Tradeoff:** These guidelines bias toward preserving important project truth instead of trusting chat history. For tiny obvious tasks, use judgment.

## 1. Preserve Durable Truth

**If future agents need it, write it down.**

Use `.loom/` for project truth that should survive the current chat: decisions, investigations, intended behavior, live work, evidence, reviews, and reusable knowledge.

Do not create records for disposable thoughts, obvious one-step edits, or facts already clear from the source code.

Ask yourself: "Would a future agent need this after this session disappears?" If yes, record it.

## 2. Keep Records Small

**Markdown records are memory, not ceremony.**

Every Loom record starts with:

```text
ID: <type>:<slug>
Type: <type>
Status: <status>
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
```

After that, use only the headings the situation needs. Link records by ID. When a record is renamed, superseded, or contradicted, repair the links.

## 3. Use The Right Shape

**Different knowledge belongs in different records.**

- `decision` — durable choices, constraints, and tradeoffs.
- `research` — investigations, sources, options, dead ends, and conclusions.
- `spec` — intended behavior, requirements, examples, and scenarios.
- `ticket` — live work: scope, acceptance, progress, blockers, and closure.
- `evidence` — observed commands, tests, logs, screenshots, reproductions, inspected files, and limits.
- `review` — critique, findings, severity, verdict, and residual risk.
- `knowledge` — reusable context, preferences, glossary terms, troubleshooting, and procedures.

Do not collapse everything into one blob. Put each fact where it can be maintained.

## 4. Resolve Honestly

**Done means the records agree with reality.**

Do not claim completion from vibes, chat, or worker output alone.

Resolve work only when the ticket's acceptance, evidence, review state, and remaining risk tell one coherent story. If proof is missing, say so and leave the work open.

---

**These guidelines are working if:** future agents can recover the important project truth from `.loom/`, records stay small, and completion claims are backed by observed evidence instead of transcript memory.
