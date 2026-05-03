---
id: evidence:local-edit-route-validation
kind: evidence
status: recorded
created_at: 2026-05-03T05:43:08Z
updated_at: 2026-05-03T05:43:08Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:localed7
  packet:
    - packet:ralph-ticket-localed7-20260503T054106Z
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
external_refs: {}
---

# Summary

Observed `local_edit` route guidance for `ticket:localed7`, including
appropriateness/write-boundary wording, ticket-owned live-state boundaries,
evidence conditions, escalation triggers, forbidden local-edit interpretations,
and `git diff --check`.

# Procedure

Observed at: 2026-05-03T05:43:08Z

Source state: working tree on `main` based on commit
`b4f205848f5c89b27653ec529b7acd6dc4ec12f6`, after Ralph child output and before
mandatory critique.

Procedure:

- Ran targeted `rg` checks over workspace routing, ticket readiness, and route
  vocabulary references.
- Added the new Ralph packet to the index with intent-to-add and ran
  `git diff --check` so the check covered new packet content and tracked edits.

Procedure verdict / exit code: pass; targeted searches returned expected local
edit guidance and prohibition wording, and `git diff --check` returned no output.

# Artifacts

## Local Edit Appropriateness And Write Boundary

Command:

```bash
rg -n 'local_edit.*cheap|tiny, safe|current context|write boundary|bounded edit|narrow known write boundary' skills/loom-workspace/references/routing.md skills/loom-tickets/references/readiness.md skills/loom-records/references/route-vocabulary.md
```

Output:

```text
skills/loom-records/references/route-vocabulary.md:37:| `local_edit` | execute a tiny, safe, in-context mutation with a named write boundary and no fresh child packet |
skills/loom-records/references/route-vocabulary.md:61:Use `local_edit` for a cheap, bounded edit that is safe to perform in the current
skills/loom-records/references/route-vocabulary.md:64:write boundary and the observation or evidence expected from the edit.
skills/loom-workspace/references/routing.md:31:- tiny, safe, in-context mutation with a narrow known write boundary -> route
skills/loom-workspace/references/routing.md:73:Use `local_edit` only when the next mutation is cheap, bounded, and safe to make
skills/loom-workspace/references/routing.md:74:in the current context: for example, a small wording fix, link repair, record
skills/loom-workspace/references/routing.md:76:write boundary before editing.
skills/loom-tickets/references/readiness.md:63:- For `local_edit`, name the bounded edit, write boundary, why it is cheap and
skills/loom-tickets/references/readiness.md:64:  safe in the current context, expected evidence or observation, and escalation
skills/loom-tickets/references/readiness.md:95:A local-edit-ready ticket should make the write boundary narrow enough that the
```

## Ticket-Owned Live State Boundary

Command:

```bash
rg -n 'does not bypass ticket truth|ticket remains the live|ticket still owns|live execution|acceptance|evidence disposition|critique disposition|next route' skills/loom-workspace/references/routing.md skills/loom-tickets/references/readiness.md skills/loom-records/references/route-vocabulary.md
```

Output excerpt:

```text
skills/loom-workspace/references/routing.md:78:`local_edit` does not bypass ticket truth. When a ticket owns the work, the
skills/loom-workspace/references/routing.md:79:ticket remains the live execution ledger for state, scope, acceptance, evidence
skills/loom-workspace/references/routing.md:80:disposition, and the next route. The edit may be local; reconciliation still
skills/loom-records/references/route-vocabulary.md:67:new owner layer. When a ticket owns the work, the ticket remains the live ledger
skills/loom-records/references/route-vocabulary.md:68:for execution state, acceptance, evidence disposition, critique disposition, and
skills/loom-records/references/route-vocabulary.md:69:the next route. Route tokens only name the next governed move; they do not move
skills/loom-tickets/references/readiness.md:91:around tickets. If a ticket owns the work, the ticket still owns live execution
skills/loom-tickets/references/readiness.md:92:state, scope, acceptance disposition, evidence disposition, critique disposition,
skills/loom-tickets/references/readiness.md:93:and the next route after the edit.
```

## Evidence Conditions

Command:

```bash
rg -n 'Evidence is required|Evidence expectations|targeted text observation|diff review|observations that must persist|route to `evidence`' skills/loom-workspace/references/routing.md skills/loom-tickets/references/readiness.md skills/loom-records/references/route-vocabulary.md
```

Output:

```text
skills/loom-workspace/references/routing.md:89:Evidence is required when the local edit supports a completion, behavior,
skills/loom-workspace/references/routing.md:91:review or targeted text observation may be enough; for behavior or risky changes,
skills/loom-workspace/references/routing.md:92:route to `evidence` and/or `critique` instead of treating the edit itself as
skills/loom-records/references/route-vocabulary.md:77:observations that must persist.
skills/loom-tickets/references/readiness.md:101:Evidence expectations should match the claim being made: structural Markdown
skills/loom-tickets/references/readiness.md:102:cleanup may need only diff review or targeted text observations, while behavior,
```

## Escalation Triggers

Command:

```bash
rg -n 'Escalate|escalation trigger|route to `ralph`|`spec`|`research`|`critique`|implementation-sized|ambiguous|risky|behavior-defining|protocol-authority' skills/loom-workspace/references/routing.md skills/loom-tickets/references/readiness.md skills/loom-records/references/route-vocabulary.md
```

Output excerpt:

```text
skills/loom-workspace/references/routing.md:83:Escalate away from `local_edit` when the change is implementation-sized, needs a
skills/loom-workspace/references/routing.md:84:fresh-context handoff, has ambiguous intended behavior, depends on missing
skills/loom-workspace/references/routing.md:86:Route those cases to `ralph`, `spec`, `research`, `critique`, or another owner
skills/loom-workspace/references/routing.md:90:validation, or protocol-authority claim. For purely structural cleanup, a diff
skills/loom-workspace/references/routing.md:91:review or targeted text observation may be enough; for behavior or risky changes,
skills/loom-records/references/route-vocabulary.md:72:Escalate from `local_edit` to the route that owns the missing truth when the work
skills/loom-records/references/route-vocabulary.md:73:becomes ambiguous, risky, behavior-defining, protocol-authority-changing, or too
skills/loom-records/references/route-vocabulary.md:75:implementation slice, `spec` for intended behavior, `research` for missing
skills/loom-records/references/route-vocabulary.md:76:evidence or tradeoffs, `critique` for adversarial review, and `evidence` for
skills/loom-tickets/references/readiness.md:65:  trigger if the edit proves ambiguous, risky, behavior-defining, or too large.
skills/loom-tickets/references/readiness.md:98:review, route to `ralph`, `spec`, `research`, `critique`, or the appropriate
skills/loom-tickets/references/readiness.md:103:validation, completion, protocol-authority, or risky claims need observed
```

## Forbidden Local-Edit Interpretations

Command:

```bash
rg -n 'loom-local-edit|bypass mode|command wrapper|new owner layer|replacement for Ralph|replace Ralph|Ralph replacement' skills/loom-workspace/references/routing.md skills/loom-tickets/references/readiness.md skills/loom-records/references/route-vocabulary.md
```

Output:

```text
skills/loom-records/references/route-vocabulary.md:6:Route tokens are not a runtime enum, command router, or new owner layer. They are
skills/loom-records/references/route-vocabulary.md:66:`local_edit` is not a `loom-local-edit` skill, command wrapper, bypass mode, or
skills/loom-records/references/route-vocabulary.md:67:new owner layer. When a ticket owns the work, the ticket remains the live ledger
```

Observed result: matches are route-boundary/prohibition wording, not new local-edit
skill, command wrapper, bypass mode, owner layer, or Ralph replacement.

## Full Diff Whitespace Check

Command:

```bash
git add -N ".loom/packets/ralph/20260503T054106Z-ticket-localed7-iter-01.md" && git diff --check
```

Output:

```text
```

Exit status: pass; no whitespace errors were reported.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008`
- `ticket:localed7#ACC-001`
- `ticket:localed7#ACC-002`
- `ticket:localed7#ACC-003`
- `ticket:localed7#ACC-004`

# Challenges Claims

None - no challenged claims were observed.

# Environment

Commit: `b4f205848f5c89b27653ec529b7acd6dc4ec12f6` plus uncommitted
ticket-scoped working-tree changes

Branch: `main`

Runtime: none; Markdown corpus only

OS: macOS / Darwin

Relevant config: no app runtime or automated test suite

# Validity

Valid for: the listed files observed at 2026-05-03T05:43:08Z.

Fresh enough for: mandatory critique and ticket acceptance review for
`ticket:localed7`.

Recheck when: workspace routing, ticket readiness, route vocabulary, ticket
criteria, or critique findings change before closure.

Invalidated by: later edits that make `local_edit` bypass ticket truth, remove
escalation triggers, weaken Ralph boundaries, or introduce a local-edit skill,
owner layer, command wrapper, or bypass mode.

Supersedes / superseded by: None.

# Limitations

This evidence does not prove operators will choose `local_edit` correctly;
mandatory critique and ticket-owned acceptance decide sufficiency.

# Result

The observed local-edit route changes are Markdown-only, make the lightweight edit
route explicit, and stay within the declared write scope.

# Interpretation

The observations support the ticket's structural claims, pending critique.

# Related Records

- `ticket:localed7`
- `packet:ralph-ticket-localed7-20260503T054106Z`
- `initiative:skills-corpus-context-integrity-hardening-pass`
