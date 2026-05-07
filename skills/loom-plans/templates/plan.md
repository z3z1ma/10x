---
id: plan:<slug>
kind: plan
status: active
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: repository
  repositories:
    - repo:root
links: {}
---

# Purpose

Why this plan exists and what sequencing problem it solves.

# Strategy

The overall route or approach. Explain the tradeoff, not just the order.

# Strategy Snapshot

Current strategic picture only. Do not use this as a progress log; live state belongs in tickets.

# Workstreams

Major streams or phases of execution strategy.

# Milestones

Execution-sequencing checkpoints. Do not use these as ticket progress state.

# Sequencing

Why the order looks this way. Name dependencies, risk ordering, and fail-fast choices.

# Claim / Acceptance Coverage

Map upstream initiative objectives, spec acceptance IDs, and ticket-local criteria
into downstream tickets. Tickets own live coverage state, evidence disposition,
and acceptance decisions.

| Source claim / acceptance ID | Downstream ticket | Coverage expectation | Evidence / critique expectation | Notes |
| --- | --- | --- | --- | --- |
| <TBD or None - reason> | <ticket:<token> or proposed> | <what must be covered> | <expected evidence/review> | <notes> |

# Ticket Slices

Each slice should be small enough for one focused implementation/review loop.

| Ticket | Purpose | Likely write scope | Dependencies | Verification / critique posture |
| --- | --- | --- | --- | --- |
| <TBD> | <bounded outcome> | <paths or records> | <depends_on or none> | <test-first, observation-first, critique profiles> |

# Execution Waves

Optional. Use only when same-wave tickets can run independently or when sequential
waves need explicit dependency boundaries.

| Wave | Tickets | Independent because | Write-scope / shared-state check | Parent reconciliation |
| --- | --- | --- | --- | --- |
| <TBD or None - no wave needed> | <tickets> | <non-overlap rationale> | <contention check> | <merge/validation path> |

# Confidence Review

Name the plan sections most likely to mislead downstream work. Fix them here or
route them to the owner layer that can resolve them.

- Requirements / claim trace:
- Decision rationale / rejected alternatives:
- File, record, test, evidence, and critique scope:
- Cross-boundary risks:
- Open questions that would change behavior, acceptance, or risk:

# Risks And Loopbacks

What could break or distort the plan, and which owner layer should receive new
truth if execution discovers the plan is wrong.

# Evidence Strategy

How work under this plan should generally be evidenced, validated, and reviewed.

# Plan Readiness Review

- Claim coverage:
- Ticket-sized slices:
- Likely write scopes:
- Parallel / wave independence:
- Evidence and critique expectations:
- Stop / loopback conditions:

# Exit Criteria

What must be true before the plan can be considered complete or retired.

# Completion Basis

When `status: completed`, explain which exit criteria were met and where any
remaining execution truth lives.
