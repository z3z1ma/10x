---
id: evidence:drive-route-gate-grammar-validation
kind: evidence
status: recorded
created_at: 2026-05-03T02:03:31Z
updated_at: 2026-05-03T02:07:36Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:drivegt11
  packet:
    - packet:ralph-ticket-drivegt11-20260503T020045Z
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  critique:
    - critique:drive-route-gate-grammar-review
---

# Summary

Observation-first validation for `ticket:drivegt11`: drive checkpoint critique
gate wording, README memory route wording, memory non-route boundary, and `stop`
route reason requirements were checked before and after the Ralph implementation.

# Supports Claims

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-014`
- `ticket:drivegt11#ACC-001`
- `ticket:drivegt11#ACC-002`
- `ticket:drivegt11#ACC-003`
- `ticket:drivegt11#ACC-004`
- `ticket:drivegt11#ACC-005`

# Procedure

Working tree source version at launch:

```text
$ git rev-parse HEAD
26fdd9eb982a449527d2f93a3f6a5056468b424e

$ git status --short
?? .loom/packets/ralph/20260503T020045Z-ticket-drivegt11-iter-01.md
```

The baseline commit matched the packet fingerprint. The untracked packet was the
active handoff surface supplied for this iteration.

Search scope:

```text
README.md
skills/loom-records/references/route-vocabulary.md
skills/loom-drive/references/checkpoint-resume-protocol.md
skills/loom-drive/references/continuity-contract.md
skills/loom-drive/references/tranche-decision-protocol.md
```

# Before Observations

Baseline before-state searches were reconstructed from commit
`26fdd9eb982a449527d2f93a3f6a5056468b424e`, the packet source fingerprint,
using `git show HEAD:<path> | rg ...` after the implementation diff was present.

Critique gate baseline:

```text
skills/loom-drive/references/checkpoint-resume-protocol.md:95:- Critique gate: mandatory critique is complete, pending as next route, blocking,
skills/loom-drive/references/checkpoint-resume-protocol.md:96:  or not required with rationale according to ticket-owned disposition status;
```

Memory route baseline:

```text
README.md:221:| `memory` | Optional support recall: retrieval cues, preferences, entities, reminders, and hot context |
README.md:244:| Retrieval cue, preference, reminder, or hot context | `memory`, until it deserves promotion |
README.md:566:├── memory/        # optional support recall
```

The same baseline route-vocabulary search returned no `memory` or
`Support-memory` row; the route-vocabulary baseline output below shows only the
pre-existing `stop` and route-boundary matches.

```text
skills/loom-records/references/route-vocabulary.md:44:| `stop` | stop because the objective is satisfied, blocked, unsafe, out of scope, over budget, or awaiting external action |
skills/loom-records/references/route-vocabulary.md:61:| Route tokens | `constitution`, `initiative`, `research`, `ralph`, `critique`, `continue`, `stop` | Use only when a route field asks for the next governed move. Tokens remain Markdown vocabulary, not a runtime enum, schema, validator, command router, skill inventory, or owner layer. |
skills/loom-records/references/route-vocabulary.md:64:| Ralph child outcomes | `continue`, `stop`, `blocked`, `escalate` | A child outcome is not a route token by itself. It becomes routing truth only after the parent reconciles the child output and translates it into the next owner-truth route, such as `ticket`, `research`, `critique`, `ask_user`, `continue`, or `stop`. |
```

Stop route baseline:

```text
skills/loom-drive/references/continuity-contract.md:80:next route: ask_user | workspace_status | records_repair | constitution | initiative | research | spec | plan | ticket | local_edit | ralph | debugging | spike | codemap | evidence | critique | wiki | retrospective | acceptance_review | ship | continue | stop
skills/loom-drive/references/continuity-contract.md:82:reason: <why this follows from current owner truth>
skills/loom-drive/references/continuity-contract.md:128:next route: ask_user | workspace_status | records_repair | constitution | initiative | research | spec | plan | ticket | local_edit | ralph | debugging | spike | codemap | evidence | critique | wiki | retrospective | acceptance_review | ship | continue | stop
skills/loom-drive/references/continuity-contract.md:130:reason: <why this next route follows from the records>
skills/loom-drive/references/tranche-decision-protocol.md:79:| Objective criteria are satisfied and no owner work remains | `stop` |
skills/loom-drive/references/tranche-decision-protocol.md:114:Every route result must name the owner records that changed and the next route or
skills/loom-drive/references/tranche-decision-protocol.md:115:stop condition.
```

Ralph child also reported these before-state observations from the scoped files:

- Checkpoint critique gate allowed mandatory critique to be `not required with
  rationale`.
- README route table used `memory` as a Loom route.
- Route vocabulary had no `memory` route token and no memory non-route
  clarification.
- `stop` route token did not require a local reason/condition; examples lacked a
  stop reason.
- Continuity/tranche drive references had generic stop/route wording but no
  stop-specific reason requirement.

# After Observations

Targeted parent searches after implementation observed:

```text
skills/loom-drive/references/checkpoint-resume-protocol.md:99: - Critique gate: mandatory critique is complete, pending as next route, or
skills/loom-drive/references/checkpoint-resume-protocol.md:100:   blocking according to ticket-owned disposition status; mandatory critique is
skills/loom-drive/references/checkpoint-resume-protocol.md:101:   never `not_required`. Recommended or optional critique may be `not_required`
```

```text
README.md:244: | Retrieval cue, preference, reminder, or hot context | Support recall, not a route token; promote through the owning route if it becomes durable truth |
skills/loom-records/references/route-vocabulary.md:67: | Support-memory surfaces | `memory`, `loom-memory`, retrieval cues, preferences, reminders, hot context | Memory is optional support recall, not canonical project truth. Do not use `memory` as a `next route:` token; route durable truth changes through the owner token that owns them. |
```

```text
skills/loom-records/references/route-vocabulary.md:44: | `stop` | stop because the objective is satisfied, blocked, unsafe, out of scope, over budget, or awaiting external action; recorded stop routes must include a stop reason or condition |
skills/loom-records/references/route-vocabulary.md:106: next route: stop
skills/loom-records/references/route-vocabulary.md:107: stop reason: OBJ-001 and OBJ-002 are satisfied, required evidence is linked, and no owner work remains.
skills/loom-drive/references/tranche-decision-protocol.md:79: | Objective criteria are satisfied and no owner work remains | `stop`, with a recorded stop reason or condition |
skills/loom-drive/references/tranche-decision-protocol.md:115: If the next route is `stop`, record the stop reason or condition.
skills/loom-drive/references/continuity-contract.md:85: When the `next route` is `stop`, the `reason` must state the stop condition,
skills/loom-drive/references/continuity-contract.md:137: When the `next route` is `stop`, the `reason` must state the stop condition,
skills/loom-drive/references/checkpoint-resume-protocol.md:41: If `next route` is `stop`, record a local stop reason or condition next to the
```

# Validation

Command:

```bash
git diff --check
```

Result: passed with no output after implementation and parent reconciliation.

# Limitations

- This evidence records structural searches and diff validation only. Acceptance
  also depends on `critique:drive-route-gate-grammar-review` and ticket-owned
  closure disposition.
- The change intentionally treats memory as support recall rather than adding a
  `memory` route token, so durable truth still routes through canonical owner
  layers.
