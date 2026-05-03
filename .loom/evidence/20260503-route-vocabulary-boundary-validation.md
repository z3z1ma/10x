---
id: evidence:route-vocabulary-boundary-validation
kind: evidence
status: recorded
created_at: 2026-05-03T01:04:17Z
updated_at: 2026-05-03T01:10:01Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:routebd1
  packet:
    - packet:ralph-ticket-routebd1-20260503T010206Z
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
external_refs: {}
---

# Summary

Observation-first validation for `ticket:routebd1`: route-token, status,
child-outcome, `ask_user`, constitution/initiative, and finding/disposition
boundaries were checked before and after normalizing the route vocabulary.

# Procedure

1. Confirmed the packet source fingerprint and working tree with
   `git status --short && git rev-parse HEAD`.
2. Captured before-state searches for route tokens, constitution/initiative
   routing, Ralph child outcomes, `ask_user`, ticket lifecycle states, record
   lifecycle statuses, critique finding states, and ticket-owned finding
   dispositions.
3. Updated route vocabulary and adjacent allowed-token lists to include
   `constitution` and `initiative`; added vocabulary-boundary and `ask_user`
   readiness guidance.
4. Captured after-state searches for the same categories.
5. Ran `git diff --check` after the implementation, ticket, packet, and evidence
   updates.

# Artifacts

## Before observations

- `git status --short && git rev-parse HEAD` returned `HEAD` at
  `772b591c4429d313aab8fd3ae0b09befa57a58d4`, with the parent ticket already
  modified and this Ralph packet untracked from launch/reconciliation setup.
- Route-token search:
  ```bash
  rg -n '`(constitution|initiative|research|spec|plan|ticket|critique|wiki|evidence|memory|acceptance_review|retrospective|ship|ask_user|debug|spike|codebase_atlas|execution_wave|external_reference|oracle)`|next_route|route token|Allowed route|Route vocabulary|loom-(constitution|initiatives)' skills/loom-records/references/route-vocabulary.md skills/loom-workspace/references/routing.md skills/loom-drive/SKILL.md skills/loom-drive/references/drive-loop.md skills/loom-drive/references/continuity-contract.md skills/loom-drive/references/checkpoint-resume-protocol.md skills/loom-drive/references/tranche-decision-protocol.md skills/loom-drive/templates/outer-loop-handoff.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md skills/loom-bootstrap/references/03-outer-loop.md
  ```
  showed `route-vocabulary.md` listed `research`, `spec`, `plan`, and `ticket`
  but not `constitution` or `initiative` as route tokens. Route lists in drive,
  ticket, checkpoint, continuity, readiness, and bootstrap surfaces also omitted
  those tokens.
- Constitution/initiative routing search:
  `rg -n 'constitution|initiative|loom-constitution|loom-initiatives|project identity|strategic framing|strategic outcome' ...`
  showed `skills/loom-workspace/references/routing.md` routed project identity to
  `loom-constitution` and strategic framing to `loom-initiatives` without matching
  route tokens.
- Ralph child-outcome search:
  ```bash
  rg -n '`(continue|stop|blocked|escalate)`|child outcome|outcome|Ralph' ...
  ```
  showed child and drive outcomes in prose, but `route-vocabulary.md` did not
  locally state that child outcomes are non-route recommendations until parent
  reconciliation translates them into a next owner-truth route.
- `ask_user` search:
  `rg -n 'ask_user|ask user|Ask User|user question|decision needed|cannot infer|owner record|low-risk|reversible' ...`
  showed `ask_user` appeared in route lists and drive prose, but the required
  readiness fields were not present consistently: decision needed,
  unsafe-inference reason, and owner record to update after answer.
- Ticket-status, record-status, critique-finding-state, and ticket-owned finding
  disposition searches showed boundary text in `status-lifecycle.md`, ticket
  templates, and `route-vocabulary.md`, but route vocabulary did not include a
  local table separating every relevant category.

## After observations

- The route-token search now shows `constitution` and `initiative` in the
  canonical token table and in touched allowed-token lists in bootstrap, drive,
  continuity, checkpoint, handoff, ticket template, and readiness surfaces.
- Workspace routing now maps project identity/principles/constraints to route
  token `constitution` and strategic outcome framing to route token `initiative`,
  while preserving `loom-constitution` and `loom-initiatives` as owner/coordinator
  names rather than route values.
- `route-vocabulary.md` now includes a vocabulary-boundaries table separating
  route tokens, ticket lifecycle states, record lifecycle statuses, Ralph child
  outcomes, critique-owned finding states, ticket-owned finding dispositions,
  commands/adapters, and skill display names.
- `route-vocabulary.md` and `status-lifecycle.md` now state that a Ralph child
  outcome such as `continue`, `stop`, `blocked`, or `escalate` is not routing
  truth until the parent reconciles it and translates it into the next
  owner-truth route.
- `ask_user` guidance now requires the decision needed, unsafe-inference reason,
  and owner record to update after answer, while preserving delegated autonomy for
  low-risk reversible assumptions.

## Validation commands and results

Parent follow-up:

- At 2026-05-03T01:10:01Z, parent adjusted `skills/loom-drive/SKILL.md` so
  `constitution` and `initiative` are described as owner-shaping routes instead
  of execution routes.
- `git diff --check` was rerun after this adjustment and passed with no output.

- After route vocabulary search:
  ```bash
  rg -n '`(constitution|initiative|research|spec|plan|ticket|critique|wiki|evidence|memory|acceptance_review|retrospective|ship|ask_user|debugging|spike|codemap|execution_wave|external_reference|oracle)`|next_route|route token|Allowed route|Route vocabulary|loom-(constitution|initiatives)' skills/loom-records/references/route-vocabulary.md skills/loom-workspace/references/routing.md skills/loom-drive/SKILL.md skills/loom-drive/references/drive-loop.md skills/loom-drive/references/continuity-contract.md skills/loom-drive/references/checkpoint-resume-protocol.md skills/loom-drive/references/tranche-decision-protocol.md skills/loom-drive/templates/outer-loop-handoff.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md skills/loom-bootstrap/references/03-outer-loop.md
  ```
  found the new `constitution` and `initiative` route tokens plus aligned touched
  route-token lists. Remaining matches for skill names such as Ralph are ordinary
  prose or owner/coordinator names, not route-field values.
- After constitution/initiative routing search:
  `rg -n 'constitution|initiative|loom-constitution|loom-initiatives|project identity|strategic framing|strategic outcome' skills/loom-records/references/route-vocabulary.md skills/loom-workspace/references/routing.md skills/loom-drive/SKILL.md skills/loom-drive/references/drive-loop.md skills/loom-drive/references/continuity-contract.md skills/loom-drive/references/checkpoint-resume-protocol.md skills/loom-drive/references/tranche-decision-protocol.md skills/loom-drive/templates/outer-loop-handoff.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md skills/loom-bootstrap/references/03-outer-loop.md`
  found explicit route-token mappings for `constitution` and `initiative` and
  owner/coordinator names preserved separately.
- After child-outcome search:
  ```bash
  rg -n '`(continue|stop|blocked|escalate)`|child outcome|outcome|Ralph' skills/loom-records/references/route-vocabulary.md skills/loom-records/references/status-lifecycle.md skills/loom-workspace/references/routing.md skills/loom-drive/SKILL.md skills/loom-drive/references/drive-loop.md skills/loom-drive/references/continuity-contract.md skills/loom-drive/references/checkpoint-resume-protocol.md skills/loom-drive/references/tranche-decision-protocol.md skills/loom-drive/templates/outer-loop-handoff.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md skills/loom-bootstrap/references/03-outer-loop.md
  ```
  found child-outcome boundary guidance in route vocabulary and status lifecycle;
  route tokens `continue` and `stop` remain valid only in route fields after
  parent translation.
- After `ask_user` search:
  `rg -n 'ask_user|ask user|Ask User|user question|decision needed|cannot infer|owner record|low-risk|reversible|unsafe-inference' skills/loom-records/references/route-vocabulary.md skills/loom-workspace/references/routing.md skills/loom-drive/SKILL.md skills/loom-drive/references/drive-loop.md skills/loom-drive/references/continuity-contract.md skills/loom-drive/references/checkpoint-resume-protocol.md skills/loom-drive/references/tranche-decision-protocol.md skills/loom-drive/templates/outer-loop-handoff.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md skills/loom-bootstrap/references/03-outer-loop.md`
  found the readiness fields in route vocabulary, checkpoint guidance, ticket
  template/readiness guidance, and drive guidance; it also found explicit autonomy
  preservation for low-risk reversible assumptions.
- After ticket-status search:
  ```bash
  rg -n '`(proposed|ready|active|blocked|review_required|complete_pending_acceptance|closed|cancelled)`|ticket state|ticket status|live execution state' skills/loom-records/references/status-lifecycle.md skills/loom-records/references/route-vocabulary.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md .loom/tickets/20260503-routebd1-normalize-route-vocabulary-boundaries.md
  ```
  found ticket lifecycle states in the non-route boundary table and readiness
  warnings, not as next-route values.
- After record-status search:
  ```bash
  rg -n '`(draft|active|accepted|deprecated|superseded|archived|proposed|ready|compiled|consumed|abandoned)`|record status|lifecycle status|status lifecycle' skills/loom-records/references/status-lifecycle.md skills/loom-records/references/route-vocabulary.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md .loom/tickets/20260503-routebd1-normalize-route-vocabulary-boundaries.md
  ```
  found lifecycle statuses in `status-lifecycle.md` and the non-route boundary
  table, not as route values.
- After critique-finding-state search:
  ```bash
  rg -n '`(open|resolved|withdrawn|accepted_risk|converted_to_follow_up|superseded)`|finding state|finding status|critique finding' skills/loom-records/references/status-lifecycle.md skills/loom-records/references/route-vocabulary.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md .loom/tickets/20260503-routebd1-normalize-route-vocabulary-boundaries.md .loom/critique
  ```
  found critique-owned finding states separated from ticket-owned dispositions.
- After ticket-owned finding disposition search:
  ```bash
  rg -n '`(resolved|accepted_risk|superseded|converted_to_follow_up|withdrawn)`|finding disposition|ticket-owned disposition|critique disposition|Critique Gate|Critique' skills/loom-records/references/status-lifecycle.md skills/loom-records/references/route-vocabulary.md skills/loom-tickets/templates/ticket.md skills/loom-tickets/references/readiness.md .loom/tickets/20260503-routebd1-normalize-route-vocabulary-boundaries.md
  ```
  found ticket-owned finding dispositions documented as separate from critique
  finding states and route tokens.
- `git diff --check`: passed with no output.

# Supports Claims

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-001`
- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-002`
- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-003`
- `ticket:routebd1#ACC-001`
- `ticket:routebd1#ACC-002`
- `ticket:routebd1#ACC-003`
- `ticket:routebd1#ACC-004`

# Challenges Claims

None observed.

# Environment

Commit: `772b591c4429d313aab8fd3ae0b09befa57a58d4`
Branch: `main`
Runtime: Markdown structural validation and ripgrep searches
OS: macOS / darwin
Relevant config: no runtime/helper dependencies added; no git config mutation

# Validity

Valid for: the current working tree diff for `ticket:routebd1` after parent
reconciliation.

Recheck when: route vocabulary, route-bearing templates, ticket readiness,
drive/checkpoint guidance, status lifecycle guidance, or critique disposition
grammar changes.

# Limitations

This evidence supports structural vocabulary alignment and `git diff --check`. It
does not replace mandatory oracle critique for `ticket:routebd1#ACC-005`.

# Result

The structural validation supports `ticket:routebd1#ACC-001` through
`ticket:routebd1#ACC-004` pending mandatory oracle critique. The ticket should
route next to `critique` with profiles `routing-safety`, `operator-clarity`, and
`records-grammar`.

# Related Records

- `ticket:routebd1`
- `packet:ralph-ticket-routebd1-20260503T010206Z`
- `initiative:skills-corpus-residual-protocol-sharpening-pass`
