---
id: ticket:9bgilfwy
kind: ticket
status: complete_pending_acceptance
change_class: documentation-explanation
risk_class: medium
created_at: 2026-04-30T16:39:37Z
updated_at: 2026-04-30T16:43:49Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  roadmap:
    - roadmap:bootstrap-the-markdown-first-protocol-corpus
  evidence:
    - evidence:skills-only-example-reconciliation
  critique:
    - critique:skills-only-example-reconciliation-review
external_refs: {}
depends_on: []
---

# Summary

Reconcile stale examples so golden fixtures teach the current skills-only product
boundary instead of command-wrapper surfaces.

# Context

Oracle reviewed Loom as feature-complete for its current skills-only,
anti-runtime identity but flagged stale example drift: example 03 still includes a
command-wrapper shipping fixture, and examples 02/06 still mention `/loom-accept`
as if a command is part of the core route.

# Why Now

Examples are not canonical project truth, but they teach future operators how the
protocol should feel. Stale examples make command wrappers look like product
surfaces after the corpus moved to skills as the only product surface.

# Scope

- Remove the example 03 `after/commands/loom-ship.md` fixture.
- Update example 03 packet, evidence, and README wording to point at the shipping
  skill surface rather than a command wrapper.
- Update example 02 and 06 command-style acceptance wording to route through
  ticket acceptance review instead.
- Update examples index wording if needed so adapter fixtures do not imply
  command wrappers are part of the product surface.
- Record structural validation evidence.

# Non-goals

- Do not rewrite all examples or add new golden traces in this pass.
- Do not change adapter transport behavior unless it directly implies command
  wrappers are canonical product truth.
- Do not add or remove Loom skills.

# Acceptance Criteria

- ACC-001: Core examples no longer include a command-wrapper fixture as an
  expected product output.
- ACC-002: Core examples no longer tell operators to invoke `/loom-*` commands as
  the core route for acceptance or shipping.
- ACC-003: Example 03 still demonstrates a feature route through spec, ticket,
  Ralph, evidence, and the `loom-ship` skill.
- ACC-004: Example 06 still demonstrates a PR package that leaves closure to the
  ticket acceptance gate.
- ACC-005: Targeted searches show no stale `/loom-*` command route in core
  examples, excluding adapter/harness command names that are not Loom commands.

# Coverage

Covers:

- ACC-001
- ACC-002
- ACC-003
- ACC-004
- ACC-005

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| ACC-001 | evidence:skills-only-example-reconciliation | critique:skills-only-example-reconciliation-review | supported |
| ACC-002 | evidence:skills-only-example-reconciliation | critique:skills-only-example-reconciliation-review | supported |
| ACC-003 | evidence:skills-only-example-reconciliation | critique:skills-only-example-reconciliation-review | supported |
| ACC-004 | evidence:skills-only-example-reconciliation | critique:skills-only-example-reconciliation-review | supported |
| ACC-005 | evidence:skills-only-example-reconciliation | critique:skills-only-example-reconciliation-review#FIND-001 resolved | supported |

# Execution Notes

Use a local edit. The scope is limited to example fixture surfaces and ticket
evidence.

# Blockers

None.

# Next Move / Next Route

Ticket acceptance review.

# Ralph Readiness

None - local edit is the selected route.

# Evidence

Recorded:

- evidence:skills-only-example-reconciliation

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:

Examples shape operator behavior, but this pass removes stale surfaces rather
than changing canonical protocol doctrine.

Required critique profiles:

- operator-surface

Findings:

critique:skills-only-example-reconciliation-review#FIND-001 was low severity and
resolved.

Disposition status: completed

Deferral / not-required rationale:

None.

# Wiki Disposition

Not required. This is example fixture reconciliation, not accepted explanation
that needs a new wiki page.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

None.

# Journal

- 2026-04-30T16:39:37Z: Created from operator request to reconcile stale examples
  with the skills-only product boundary.
- 2026-04-30T16:40:28Z: Completed local example edits and recorded
  evidence:skills-only-example-reconciliation; recommended critique is the next
  route before acceptance.
- 2026-04-30T16:43:49Z: Ran recommended operator-surface critique, resolved
  critique:skills-only-example-reconciliation-review#FIND-001 by harmonizing
  example 03 common wrong behavior, and moved ticket to
  `complete_pending_acceptance`.
