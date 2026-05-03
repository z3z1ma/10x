---
id: critique:query-recipe-review
kind: critique
status: final
created_at: 2026-05-03T06:00:45Z
updated_at: 2026-05-03T06:00:45Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:queryrc9 diff 477b6fe..working-tree initial review"
links:
  ticket:
    - ticket:queryrc9
  evidence:
    - evidence:query-recipe-validation
  packet:
    - packet:ralph-ticket-queryrc9-20260503T055023Z
external_refs: {}
---

# Summary

Initial mandatory oracle critique for `ticket:queryrc9` after consolidating
Markdown-native graph query recipes.

# Review Target

Current working-tree diff from baseline
`477b6fe7b77dc0752daef13e1b78c7319a8eb115`, covering query/linking guidance,
records skill discovery, bootstrap filesystem/tooling pointer, ticket, evidence,
and Ralph packet records.

Required critique profiles: `operator-clarity`, `records-grammar`, and
`workflow-boundary`.

# Verdict

`changes_required` - two findings block acceptance until resolved or
ticket-dispositioned.

# Findings

## FIND-001: Ticket live ledger is stale after Ralph and evidence

Severity: medium
Confidence: high
State: open

Observation:

The Ralph packet is `consumed` and recommends `review_required`, and evidence has
been recorded, but the ticket still says `status: active`, `Next route: ralph`,
evidence expected, and critique pending.

Why it matters:

Tickets are the live execution ledger. A fresh agent could incorrectly relaunch
Ralph instead of consuming evidence/critique and moving to acceptance review.

References:

- `.loom/tickets/20260503-queryrc9-consolidate-query-recipes.md:4`
- `.loom/tickets/20260503-queryrc9-consolidate-query-recipes.md:92-130`
- `.loom/packets/ralph/20260503T055023Z-ticket-queryrc9-iter-01.md:5`
- `.loom/packets/ralph/20260503T055023Z-ticket-queryrc9-iter-01.md:201-210`
- `.loom/evidence/20260503-query-recipe-validation.md:23-44`
- `.loom/evidence/20260503-query-recipe-validation.md:168-175`

Challenges:

- `ticket:queryrc9#ACC-005`
- ticket/evidence/critique truth-boundary preservation

Required follow-up:

Reconcile `ticket:queryrc9` live state, evidence, critique disposition, claim
matrix, and next route before closure.

## FIND-002: Cold-start recipe under-maps owner graph

Severity: low
Confidence: high
State: open

Observation:

The cold-start query omits `.loom/research` and `.loom/specs`, and matches only
`^links:` rather than nested link targets. For a first map of the active owner
graph, that can hide conditional-but-important governing layers.

Why it matters:

Cold-start recipes are supposed to improve recovery. Under-mapping research,
specs, and typed link targets weakens the operator-clarity claim, even though the
overall Markdown-native direction is sound.

References:

- `skills/loom-records/references/query-and-linking.md:18-27`

Challenges:

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009`
- `ticket:queryrc9#ACC-001`

Required follow-up:

Expand or clarify the cold-start query to include research/spec surfaces and
useful link targets, or explicitly narrow its claim.

# Profile Results

- `operator-clarity`: changes required due `FIND-002`; query recipes are useful
  and discoverable, but cold-start orientation under-maps governing layers.
- `records-grammar`: changes required due `FIND-001`; ticket truth must reflect
  consumed packet, evidence, critique state, and next route.
- `workflow-boundary`: pass for product changes. Recipes remain ordinary-tool
  examples and are not a generated index, schema validator, command wrapper,
  dashboard, MCP dependency, proof-by-query mechanism, or new owner layer.

# Evidence Reviewed

- Working-tree diff from baseline `477b6fe7b77dc0752daef13e1b78c7319a8eb115`
- `git diff --check 477b6fe7b77dc0752daef13e1b78c7319a8eb115`: passed with no
  output
- `ticket:queryrc9`
- `packet:ralph-ticket-queryrc9-20260503T055023Z`
- `evidence:query-recipe-validation`
- `skills/loom-records/references/query-and-linking.md`
- `skills/loom-records/SKILL.md`
- `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`

# Acceptance Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-009`: mostly
  supported; `FIND-002` should be fixed or explicitly accepted.
- `ticket:queryrc9#ACC-001`: partially supported pending `FIND-002` repair.
- `ticket:queryrc9#ACC-002`: supported. Recipes are ordinary-tool examples and
  explicitly not runtime dependencies or proof.
- `ticket:queryrc9#ACC-003`: supported. Stale compiled packets and
  claim/evidence/critique trace recipes are present.
- `ticket:queryrc9#ACC-004`: supported. Evidence records targeted searches and
  `git diff --check`.
- `ticket:queryrc9#ACC-005`: not satisfied while findings remain open.

# Residual Risks

- Manual structural review only; no automated test suite exists.
- Query recipes intentionally produce false positives; operators still must read
  owner records.

# Required Follow-up

1. Reconcile `ticket:queryrc9` live state, evidence, critique disposition, claim
   matrix, and next route.
2. Expand or clarify the cold-start query to include research/spec and useful
   link targets, or explicitly narrow its claim.
3. Re-run structural checks after follow-up.
4. Do not close the ticket until findings are resolved or ticket-owned
   dispositions are recorded.

# Acceptance Recommendation

`follow-up-needed-before-acceptance`
