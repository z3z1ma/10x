---
id: ticket:routebd1
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T00:56:36Z
updated_at: 2026-05-03T01:15:20Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  plan:
    - plan:skills-corpus-residual-protocol-sharpening-pass
  research:
    - research:skills-corpus-residual-audit-synthesis
  packet:
    - packet:ralph-ticket-routebd1-20260503T010206Z
  evidence:
    - evidence:route-vocabulary-boundary-validation
  critique:
    - critique:route-vocabulary-boundary-review
external_refs: {}
depends_on: []
---

# Summary

Normalize route vocabulary boundaries, constitution/initiative routing, child
outcome translation, and `ask_user` decision grammar.

# Context

Council finding `NC2-003` and older audit actions 2 and 8 found that current route
guidance does not fully settle constitution/initiative route-token handling,
vocabulary boundaries, child-outcome translation, and `ask_user` fields.

# Why Now

Route fields are copied into tickets, drive checkpoints, and handoffs. If route
tokens blur with statuses, child outcomes, or user-question posture, fresh agents
can record false next-route truth.

# Scope

- Decide whether `constitution` and `initiative` are canonical route tokens or are
  reached through existing shaping/escalation routes.
- Add or clarify a vocabulary-boundaries table across route tokens, ticket states,
  record statuses, child outcomes, critique finding states, and ticket finding
  dispositions.
- Clarify that a child outcome is not a route token until the parent translates it.
- Make `ask_user` fields explicit: decision needed, why the agent cannot infer it
  safely, and owner record to update after answer.

# Out Of Scope

- Do not create a runtime enum, command router, schema, validator, or new owner
  layer.
- Do not turn every skill name into a route token.
- Do not weaken delegated autonomy by requiring user prompts for low-risk,
  reversible choices.

# Acceptance Criteria

- ACC-001: Constitution/initiative routing is either added to canonical route
  tokens or explicitly documented as intentionally reached through existing
  shaping/escalation routes.
- ACC-002: Route vocabulary distinguishes route tokens from ticket statuses,
  record statuses, child outcomes, critique finding states, and ticket-owned
  finding dispositions.
- ACC-003: `ask_user` guidance names decision needed, unsafe-inference reason, and
  owner record update target.
- ACC-004: Evidence records before/after route/vocabulary searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-001`
- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-002`
- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-003`
- `ticket:routebd1#ACC-001`
- `ticket:routebd1#ACC-002`
- `ticket:routebd1#ACC-003`
- `ticket:routebd1#ACC-004`
- `ticket:routebd1#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-001` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-002` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-003` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `ticket:routebd1#ACC-001` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `ticket:routebd1#ACC-002` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `ticket:routebd1#ACC-003` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `ticket:routebd1#ACC-004` | `evidence:route-vocabulary-boundary-validation` | `critique:route-vocabulary-boundary-review` | supported |
| `ticket:routebd1#ACC-005` | `critique:route-vocabulary-boundary-review` | oracle critique passed with no findings | supported |

# Execution Notes

Likely touched surfaces include route vocabulary, status lifecycle boundary
wording, workspace/drive routing references, and ticket route snippets if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:promdisp2`.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:route-vocabulary-boundary-validation` and oracle critique
`critique:route-vocabulary-boundary-review` support closure with no findings.

# Evidence

Recorded: `evidence:route-vocabulary-boundary-validation` captures before/after
searches for route tokens, child outcomes, `ask_user`, constitution/initiative
routing, status/finding vocabulary, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: route vocabulary shapes operator decisions and can corrupt live
next-route truth if ambiguous.

Required critique profiles:

- routing-safety
- operator-clarity
- records-grammar

Findings:

`critique:route-vocabulary-boundary-review` - no findings; mandatory oracle
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Route vocabulary and owner-boundary guidance were promoted directly into the
  touched route vocabulary, status lifecycle, drive, workspace, ticket, and
  bootstrap guidance.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product guidance itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched route vocabulary and routing guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T01:15:20Z
Basis: Ralph packet `packet:ralph-ticket-routebd1-20260503T010206Z`; evidence
`evidence:route-vocabulary-boundary-validation`; oracle critique
`critique:route-vocabulary-boundary-review` with no findings.
Residual risks: validation is structural Markdown review; no runtime validator is
intentionally added.

# Dependencies

None.

# Journal

- 2026-05-03T00:56:36Z: Created from council finding `NC2-003` and older audit
  actions 2 and 8.
- 2026-05-03T01:02:06Z: Moved to `active` and compiled
  `packet:ralph-ticket-routebd1-20260503T010206Z` for route vocabulary boundary
  cleanup.
- 2026-05-03T01:04:17Z: Ralph child completed the bounded route vocabulary
  boundary cleanup, recorded `evidence:route-vocabulary-boundary-validation`, and
  moved the ticket to `review_required` with next route `critique` for mandatory
  oracle profiles `routing-safety`, `operator-clarity`, and `records-grammar`.
- 2026-05-03T01:10:01Z: Parent reconciled Ralph output, marked
  `packet:ralph-ticket-routebd1-20260503T010206Z` consumed, and made one
  scope-preserving drive wording adjustment before oracle critique.
- 2026-05-03T01:15:20Z: Mandatory oracle critique
  `critique:route-vocabulary-boundary-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
