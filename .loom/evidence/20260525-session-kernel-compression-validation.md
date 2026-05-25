# Session Kernel Compression Validation

ID: evidence:20260525-session-kernel-compression-validation
Type: Evidence Dossier
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Related Records

- `ticket:20260525-session-kernel-compression`
- `spec:loom-protocol-compression`
- `evidence:20260525-compression-inventory-baseline`

## Procedure

Commands and inspections were run from `/Users/alexanderbutler/code_projects/personal/agent-loom` after the bounded source-edit worker compressed `loom-core/skills/using-loom/**`.

- Pre-edit `wc -l loom-core/skills/using-loom/SKILL.md loom-core/skills/using-loom/references/*.md loom-core/loom-core.mjs loom-core/hooks/* loom-core/gemini-bootstrap.md`.
- Post-edit `wc -l` over the same paths.
- `npm --prefix loom-core run smoke`.
- `npm --prefix loom-core run pack:check`.
- `git diff --check`.
- Targeted searches over `loom-core/skills/using-loom` for activation discipline, active knowledge loading, surface ownership, loop order, ticket-owned Ralph, evidence/audit posture, safety/scope posture, and product-surface leakage terms.
- `git diff --stat -- loom-core/skills/using-loom` and source inspection of the compressed files.

## Observations

Pre-edit line counts:

```text
169 loom-core/skills/using-loom/SKILL.md
139 loom-core/skills/using-loom/references/00-how-loom-thinks.md
 55 loom-core/skills/using-loom/references/01-activation-discipline.md
 74 loom-core/skills/using-loom/references/02-directory-structure.md
179 loom-core/skills/using-loom/references/03-shaping-with-humans.md
127 loom-core/skills/using-loom/references/04-delegating-to-workers.md
 95 loom-core/skills/using-loom/references/05-proving-the-work.md
117 loom-core/skills/using-loom/references/06-staying-safe.md
493 loom-core/loom-core.mjs
 10 loom-core/hooks/hooks-cursor.json
 17 loom-core/hooks/hooks.json
 19 loom-core/gemini-bootstrap.md
1494 total
```

Post-edit line counts:

```text
118 loom-core/skills/using-loom/SKILL.md
 68 loom-core/skills/using-loom/references/00-how-loom-thinks.md
 53 loom-core/skills/using-loom/references/01-activation-discipline.md
 66 loom-core/skills/using-loom/references/02-directory-structure.md
143 loom-core/skills/using-loom/references/03-shaping-with-humans.md
104 loom-core/skills/using-loom/references/04-delegating-to-workers.md
 76 loom-core/skills/using-loom/references/05-proving-the-work.md
 94 loom-core/skills/using-loom/references/06-staying-safe.md
493 loom-core/loom-core.mjs
 10 loom-core/hooks/hooks-cursor.json
 17 loom-core/hooks/hooks.json
 19 loom-core/gemini-bootstrap.md
1261 total
```

The `using-loom` skill plus references changed from 955 to 722 lines. The full requested preload set changed from 1494 to 1261 lines. `git diff --stat -- loom-core/skills/using-loom` reported 8 files changed, 196 insertions and 429 deletions. No preload mirror files required edits because their dynamic inclusion still targets the same ordered filenames.

`npm --prefix loom-core run smoke` passed with `ok: true`. The smoke output reported `usingLoomFileCount: 8`, the expected ordered file list from `skills/using-loom/SKILL.md` through `references/06-staying-safe.md`, `bootstrapInjectionPartCount: 1`, `bootstrapInjectionIsDeduped: true`, and activation checks with `ok: true`, `hasActivationReference: true`, `requiredPhraseCount: 18`, and `missingPhrases: []`.

`npm --prefix loom-core run pack:check` passed. It reran Core smoke successfully and completed `npm pack --dry-run` for `@z3z1ma/open-loom-core@0.3.0` with 69 total files.

`git diff --check` passed with no output.

Targeted searches found:

- Mandatory activation phrases in `SKILL.md` and `references/01-activation-discipline.md`, including first-action invocation before responding, asking clarifying questions, code exploration, quick checks, editing files, creating tickets, and launching Ralph.
- Active `Type: Knowledge Preference` loading from `.loom/knowledge/` remains in `SKILL.md`.
- The surface ownership map remains in `SKILL.md`, `references/00-how-loom-thinks.md`, and `references/03-shaping-with-humans.md`.
- Loop order, ticket-owned Ralph, transient launch prompt posture, worker-output reconciliation, evidence, audit, and closure honesty remain present.
- Safety posture remains present for lower-authority text, scope boundaries, stale run context, command safety, and sensitive data redaction.
- Product-surface leakage search over `using-loom` found no matches for `smoke`, `package`, `adapter`, `dogfood`, `repository workflow`, `npm`, `test harness`, `skill-authoring`, or `why Loom is built`.

## What This Shows

- `ticket:20260525-session-kernel-compression#ACC-001` is supported by source inspection and smoke output showing activation discipline remains present and the required activation phrases are not missing.
- `ticket:20260525-session-kernel-compression#ACC-002` is supported by source inspection showing the complete loop remains explicit: shape, route durable truth, slice executable work, execute bounded Ralph, preserve evidence, audit claims, and reconcile records.
- `ticket:20260525-session-kernel-compression#ACC-003` is supported by unchanged ordered reference filenames and successful Core smoke/pack checks. The preload mirrors still include the same ordered files dynamically, and no stale embedded doctrine was observed in touched preload surfaces.
- `ticket:20260525-session-kernel-compression#ACC-004` is supported by recorded before/after line counts showing a smaller session kernel and by source inspection showing retained prose maps to activation, routing, shaping, worker handoff, proof, and safety requirements.

## What This Does Not Show

- This evidence does not replace the fresh-context audit requested by the ticket.
- This evidence does not prove behavior of external harnesses beyond the local Core smoke and pack checks.
- This evidence does not validate Claude or Gemini manifest commands because hook, bootstrap, and manifest files were not changed.
- This evidence does not close the ticket by itself; closure disposition remains a ticket/audit decision.
