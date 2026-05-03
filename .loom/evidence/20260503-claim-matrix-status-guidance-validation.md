---
id: evidence:claim-matrix-status-guidance-validation
kind: evidence
status: recorded
created_at: 2026-05-03T02:14:37Z
updated_at: 2026-05-03T02:14:37Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:claimmx5
  packet:
    - packet:ralph-ticket-claimmx5-20260503T021312Z
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  critique:
    - critique:claim-matrix-status-guidance-review
---

# Summary

Observation-first validation for `ticket:claimmx5`: the ticket template claim
matrix now locally points to the canonical claim status vocabulary while preserving
claim coverage as the owner of status meanings.

# Supports Claims

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-007`
- `ticket:claimmx5#ACC-001`
- `ticket:claimmx5#ACC-002`
- `ticket:claimmx5#ACC-003`
- `ticket:claimmx5#ACC-004`

# Procedure

Working tree source version at launch:

```text
$ git rev-parse HEAD
2170a7c298b221f04dcfd0d23263f5c68a83b60e

$ git status --short
?? .loom/packets/ralph/20260503T021312Z-ticket-claimmx5-iter-01.md
```

The baseline commit matched the packet fingerprint. The untracked packet was the
active handoff surface supplied for this iteration.

Search scope:

```text
skills/loom-tickets/templates/ticket.md
skills/loom-records/references/claim-coverage.md
```

# Before Observations

Baseline ticket template search at commit
`2170a7c298b221f04dcfd0d23263f5c68a83b60e`:

```text
skills/loom-tickets/templates/ticket.md:64:List qualified claim or acceptance IDs. If none apply, write `None - reason`.
skills/loom-tickets/templates/ticket.md:71:# Claim Matrix
skills/loom-tickets/templates/ticket.md:74:write `None - reason` when no claim matrix applies yet.
```

The same baseline template search had no local `supported_pending_review` or
`challenged` match near the claim matrix table; status values appeared only later
in unrelated critique disposition examples.

Baseline claim coverage search:

```text
skills/loom-records/references/claim-coverage.md:125:Use this status vocabulary:
skills/loom-records/references/claim-coverage.md:127:- `open` — no sufficient support or challenge has been reconciled yet
skills/loom-records/references/claim-coverage.md:128:- `supported` — evidence supports the claim and required review is complete or not required
skills/loom-records/references/claim-coverage.md:129:- `supported_pending_review` — evidence supports the claim but required critique or acceptance review remains
skills/loom-records/references/claim-coverage.md:130:- `challenged` — evidence or critique currently challenges the claim
skills/loom-records/references/claim-coverage.md:131:- `accepted_risk` — the claim has a known challenge or limitation accepted by the ticket owner
skills/loom-records/references/claim-coverage.md:132:- `superseded` — the claim reference has been replaced by a successor
```

# After Observations

Targeted parent searches after implementation observed:

```text
skills/loom-tickets/templates/ticket.md:71: # Claim Matrix
skills/loom-tickets/templates/ticket.md:73: Use only real claim, evidence, and critique references. Remove this table or
skills/loom-tickets/templates/ticket.md:74: write `None - reason` when no claim matrix applies yet.
skills/loom-tickets/templates/ticket.md:75: Use the canonical status vocabulary from
skills/loom-tickets/templates/ticket.md:76: `skills/loom-records/references/claim-coverage.md`: `open`, `supported`,
skills/loom-tickets/templates/ticket.md:77: `supported_pending_review`, `challenged`, `accepted_risk`, or `superseded`.
```

Claim coverage remained the canonical vocabulary owner and was unchanged by the
Ralph child.

# Validation

Command:

```bash
git diff --check
```

Result: passed with no output after implementation and parent reconciliation.

# Limitations

- This evidence records structural searches and diff validation only. Acceptance
  also depends on `critique:claim-matrix-status-guidance-review` and ticket-owned
  closure disposition.
