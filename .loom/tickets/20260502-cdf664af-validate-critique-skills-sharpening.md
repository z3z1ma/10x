---
id: ticket:cdf664af
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T09:28:53Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  roadmap:
    - roadmap:bootstrap-the-markdown-first-protocol-corpus
  initiative:
    - initiative:skills-corpus-protocol-sharpening
  research:
    - research:skills-corpus-council-review
  evidence:
    - evidence:skills-corpus-council-review
  plan:
    - plan:skills-corpus-protocol-sharpening
  supersedes:
    - ticket:3uv5l5fh
external_refs: {}
depends_on:
  - ticket:0a1106b6
  - ticket:4e8ebe92
  - ticket:0cd38381
  - ticket:50ded996
  - ticket:1a12d9ff
  - ticket:233cfdeb
  - ticket:795fa0f4
  - ticket:53cf2989
---

# Summary

Run final structural validation, record implementation evidence, perform
mandatory critique, reconcile findings, and update the Loom graph after the
skills corpus sharpening tickets land.

# Context

The council and the plan both require evidence and critique before the broad
protocol-sharpening effort is accepted. Because the work has been split into
smaller Ralph-sized tickets, this final ticket owns the integration-level
validation and critique gate rather than any single implementation slice.

# Why Now

Markdown protocol changes can look harmless while changing operator behavior,
truth ownership, acceptance gates, or packet contracts. The final state needs a
fresh validation record and adversarial review before the initiative claims the
corpus is sharper.

# Scope

- Run the structural validation query set from the plan and affected child tickets
  after implementation edits land.
- Record a new evidence artifact, tentatively
  `evidence:skills-corpus-protocol-sharpening-validation`.
- Run mandatory critique over the combined product-surface diff using at least
  protocol-change, operator-clarity, records-grammar, and routing-safety lenses.
- Resolve critique findings, explicitly accept residual risk, or create linked
  follow-up tickets.
- Update the child tickets' evidence and critique disposition as needed.
- Update `plan:skills-corpus-protocol-sharpening` and
  `initiative:skills-corpus-protocol-sharpening` status summaries.
- Decide whether wiki or retrospective promotion is needed.

# Non-goals

- Do not implement new product-surface scope except for critique fixes.
- Do not close child tickets without their own acceptance dossiers telling the
  truth.
- Do not use this ticket to hide unresolved medium/high critique findings.
- Do not create a release or PR package; ship packaging is a separate route if
  requested later.

# Acceptance Criteria

- ACC-001: Structural validation evidence exists and cites the final source state
  inspected.
- ACC-002: Validation covers skill maps, coverage IDs, packet grammar,
  frontmatter/status values, skill metadata, risk/change class usage, empty skill
  directories, and source-repo leakage.
- ACC-003: Mandatory critique exists and reviews the combined sharpening diff
  against protocol-change, operator-clarity, records-grammar, and routing-safety
  risks.
- ACC-004: All medium/high critique findings are resolved, accepted as risk in a
  ticket-owned decision, or converted into linked follow-up tickets.
- ACC-005: Each child ticket's evidence and critique disposition is updated or has
  a truthful deferral rationale.
- ACC-006: The plan and initiative status summaries truthfully describe what
  landed, what remains, and why the route can continue or stop.
- ACC-007: Wiki/retrospective disposition is explicit.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening#OBJ-005`
- `research:skills-corpus-council-review#CLAIM-009`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening#OBJ-005` | validation evidence pending | mandatory critique pending | open |
| `research:skills-corpus-council-review#CLAIM-009` | `evidence:skills-corpus-council-review` supports need; validation evidence pending | mandatory critique pending | supported_pending_review |

# Execution Notes

This is an integration and review ticket. It should normally start only after the
implementation child tickets have either been accepted or explicitly deferred.

# Blockers

All implementation child tickets in `depends_on` must be accepted, cancelled with
rationale, or explicitly deferred before this ticket can move to active.

# Next Move / Next Route

Wait for implementation child tickets, then record evidence and run critique.

# Ralph Readiness

This is not a normal implementation Ralph ticket. If delegated, compile a critique
or validation packet rather than a code-change Ralph packet.

Bounded iteration:

Validate final diff, record evidence, run critique, and reconcile findings.

Write boundary:

- `.loom/evidence/**`
- `.loom/critique/**`
- `.loom/tickets/**`
- `.loom/plans/skills-corpus-protocol-sharpening.md`
- `.loom/initiatives/skills-corpus-protocol-sharpening.md`
- product-surface files only for critique fixes explicitly tied to findings

Likely verification posture:

Observation-first structural validation plus mandatory critique.

Expected output contract:

- validation evidence record,
- critique record,
- resolved findings or follow-up tickets,
- updated plan/initiative/ticket dispositions.

# Evidence

Expected:

- `git diff --check`
- public skill-map and coverage-ID grep checks
- packet grammar, frontmatter/status, metadata, and risk/change class grep checks
- empty skill-directory and source-repo leakage checks

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale:

This ticket owns the final critique gate for a multi-ticket protocol-authority
sharpening pass.

Required critique profiles:

- protocol-change
- operator-clarity
- records-grammar
- routing-safety

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is mandatory.

# Wiki Disposition

Pending. Decide after critique whether durable understanding should be promoted to
wiki, research, spec, plan, initiative, constitution, evidence, memory, or no
additional layer.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

- `ticket:0a1106b6`
- `ticket:4e8ebe92`
- `ticket:0cd38381`
- `ticket:50ded996`
- `ticket:1a12d9ff`
- `ticket:233cfdeb`
- `ticket:795fa0f4`
- `ticket:53cf2989`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the final validation, critique, and reconciliation slice.
