---
id: evidence:route-vocabulary-validation
kind: evidence
status: recorded
created_at: 2026-05-02T19:05:00Z
updated_at: 2026-05-02T19:15:17Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:rtvocab1
  initiative:
    - initiative:skills-corpus-council-precision-pass
  critique:
    - critique:route-vocabulary-review
external_refs: {}
---

# Summary

Observation-first validation for `ticket:rtvocab1`: route-token drift was checked
before and after normalizing shared route vocabulary across Loom records, drive,
tickets, workspace guidance, and route-bearing templates.

# Procedure

1. Checked source fingerprint and working tree before edits:
   `git status --short && git rev-parse HEAD`.
2. Captured before-state route-token drift with:
   `rg -n '(next route|next_route|next-route|ask_user|ask-user|ask user|acceptance_review|acceptance review|Ralph|acceptance \||\| acceptance|continue \||ask user)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'`.
3. Added shared owner surface
   `skills/loom-records/references/route-vocabulary.md` and aligned direct route
   examples in drive, ticket, and workspace surfaces.
4. Captured after-state route fields and drift checks with:
   `rg -n '(next route:|Route:|proposed next route:|Route Decision Priority|route-vocabulary)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'`,
   `rg -n '(ask-user|ask user|workspace/records repair|acceptance / stop|Ralph implementation packet|ticket acceptance review|local edit \||Ralph \||acceptance \|)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'`,
   and
   `rg -n '(review_required|complete_pending_acceptance|acceptance_review|ask_user|local_edit|ralph)' 'skills/loom-records/references/route-vocabulary.md' 'skills/loom-tickets/references/readiness.md' 'skills/loom-workspace/references/status-snapshot.md' --glob '*.md'`.
5. Ran `git diff --check` after the record and evidence updates.

# Artifacts

## Before observations

- Source fingerprint check returned modified ticket and untracked packet already
  present from parent launch, with `HEAD` still at
  `86b74e39009eb4eeec4722bec9799f4bbc12705b`.
- Before-state search showed route-like values split across styles:
  - `checkpoint-resume-protocol.md` used `ask_user` with title-case `Ralph` and
    route value `acceptance` in a `next route:` list.
  - `continuity-contract.md` used a shorter `next route:` list that omitted
    implementation/evidence/retrospective/acceptance-review tokens.
  - `outer-loop-handoff.md` used hyphenated `ask-user`.
  - `tranche-decision-protocol.md` used prose table values such as `ask user`,
    `workspace/records repair`, `local edit`, `Ralph`, and `acceptance / stop`.
  - `ticket.md` and `readiness.md` used phrase-style route examples such as
    `Ralph implementation packet`, `direct critique`, and `ticket acceptance review`.
- Before-state search also showed many ordinary prose mentions of Ralph,
  acceptance, and ticket lifecycle statuses that were not themselves active route
  values.

## After observations

- `skills/loom-records/references/route-vocabulary.md` now owns lowercase
  `snake_case` route-token grammar and the canonical route token table.
- Direct route-value fields and examples now use shared tokens such as
  `ask_user`, `workspace_status`, `records_repair`, `local_edit`, `ralph`, and
  `acceptance_review` in drive, ticket, and workspace surfaces.
- After-state route-field search showed route-vocabulary links from
  `loom-records`, `loom-drive`, `loom-tickets`, and `loom-workspace` surfaces.
- Drift-variant search still returned ordinary prose/status matches:
  `Ralph implementation packets` in packet-frontmatter guidance, ticket status
  machine values `review_required` and `complete_pending_acceptance`, semantic
  link prose, and route-vocabulary definitions. These are not active `next route:`
  or `Route:` values.
- Status/route separation search showed explicit guidance that ticket lifecycle
  statuses such as `review_required` and `complete_pending_acceptance` are not
  next-route values.

## Validation commands and results

- `rg -n '(next route:|Route:|proposed next route:|Route Decision Priority|route-vocabulary)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'`:
  found canonical route fields/lists and references to
  `skills/loom-records/references/route-vocabulary.md`.
- `rg -n '(ask-user|ask user|workspace/records repair|acceptance / stop|Ralph implementation packet|ticket acceptance review|local edit \||Ralph \||acceptance \|)' 'skills/loom-records' 'skills/loom-drive' 'skills/loom-tickets' 'skills/loom-workspace' --glob '*.md'`:
  remaining matches are ordinary prose, packet-frontmatter guidance, semantic-link
  prose, ticket state-machine statuses, and route-vocabulary definitions; no
  remaining active route-value example was observed using the old drift forms.
- `rg -n '(review_required|complete_pending_acceptance|acceptance_review|ask_user|local_edit|ralph)' 'skills/loom-records/references/route-vocabulary.md' 'skills/loom-tickets/references/readiness.md' 'skills/loom-workspace/references/status-snapshot.md' --glob '*.md'`:
  confirmed explicit status/route separation and canonical route tokens.
- `git diff --check`: passed with no output.

# Supports Claims

- `initiative:skills-corpus-council-precision-pass#OBJ-001`
- `ticket:rtvocab1#ACC-001`
- `ticket:rtvocab1#ACC-002`
- `ticket:rtvocab1#ACC-003`
- `ticket:rtvocab1#ACC-004`

# Challenges Claims

None observed.

# Environment

Commit: `86b74e39009eb4eeec4722bec9799f4bbc12705b`
Branch: `main`
Runtime: Markdown structural validation and ripgrep searches
OS: macOS / darwin
Relevant config: no runtime/helper dependencies added; no git config mutation

# Validity

Valid for: the current working tree diff for `ticket:rtvocab1` at the recorded
source fingerprint.
Recheck when: route vocabulary, route examples, ticket lifecycle statuses,
checkpoint/resume guidance, or command/adapter surfaces change.

# Limitations

This evidence supports structural route vocabulary alignment. It does not replace
mandatory oracle critique for the high-risk protocol-authority change, and it
does not satisfy `ticket:rtvocab1#ACC-005` by itself.

# Result

The shared route vocabulary exists and direct route-bearing examples were aligned
to it. Route tokens are documented as separate from ticket lifecycle statuses,
record lifecycle statuses, command names, and adapter invocation surfaces.

# Interpretation

The evidence supports `ticket:rtvocab1#ACC-001` through `ticket:rtvocab1#ACC-004`
pending mandatory critique. It does not justify closing the ticket because oracle
critique remains required for `ticket:rtvocab1#ACC-005`.

# Related Records

- `ticket:rtvocab1`
- `packet:ralph-ticket-rtvocab1-20260502T190248Z`
- `initiative:skills-corpus-council-precision-pass#OBJ-001`
- `critique:route-vocabulary-review`
