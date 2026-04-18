---
id: plan:bootstrap-core-workflow-backlog
kind: plan
status: active
created_at: 2026-04-04T23:57:49Z
updated_at: 2026-04-17T23:58:42Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:prove-core-loom-workflow
  spec:
    - spec:minimum-proven-core-workflow-surface
  ticket:
    - ticket:1ypcbj0m
    - ticket:zomng8h3
    - ticket:vyypge85
---

# Purpose / Big Picture

Turn the repository's rewritten but still partly unreconciled workflow surfaces
into one proven core operator path.

This plan sequences three increments: first prove one bounded Ralph -> critique
-> wiki slice, then reconcile the active wrapper and instruction surfaces to the
proved path, then tighten validation and query guidance around the exercised
workflow.

# Progress

- 2026-04-04: created `initiative:prove-core-loom-workflow`,
  `spec:minimum-proven-core-workflow-surface`, this plan, and three linked
  backlog tickets.
- 2026-04-17: reconciled the governing constitutional layer to the rewrite and
  identified that the active workflow chain and repo instruction surfaces still
  needed the same treatment.
- No workflow proof has landed yet; the backlog remains framed and ordered.

# Surprises & Discoveries

- The rewrite changed more than the product prose: it also changed the
  canonical vocabulary and record grammar, which means dogfooded records and
  wrapper commands can become misleading if they are not reconciled.
- Optional command wrappers may still be useful, but they can no longer be
  treated as part of the protocol core or as a required milestone.
- The most important near-term gap is still proof of the main path, not more
  auxiliary surfaces.

# Decision Log

- 2026-04-04: prioritize one real proof flow before expanding commands or
  validation so later additions are informed by observed workflow behavior.
- 2026-04-04: keep the next backlog bounded to three tickets instead of opening
  a wide umbrella of speculative follow-ups.
- 2026-04-17: reframe the command follow-up as optional wrapper evaluation and
  reframe the validation follow-up around visible guidance rather than helper
  scripts.

# Outcomes & Retrospective

This plan is still pre-execution.

Its current value is strategic: another agent can see the intended route,
understand why the sequence is ordered this way, and identify which tickets own
the live work.

# Context and Orientation

`constitution:main` now says the next durable direction is to reconcile the
remaining active examples to the template-first rewrite, exercise real Ralph,
critique, and wiki flows, and tighten validation and query guidance only where
they mechanize published rules.

The repository already has the rule set, skill bundle, templates, and a small
set of optional wrapper commands. The missing proof is the actual operator path:
one ticket, one packet, one critique pass, one truthful wiki/evidence decision,
and one reconciliation pass that future agents can trust.

# Milestones

1. Durable record chain in place and reconciled to the rewrite.
2. One end-to-end proof flow executed and reconciled.
3. Optional wrapper and instruction surfaces judged against the proved path.
4. Validation and query guidance tightened around the exercised path.

# Plan of Work

Start with one small, low-risk proof target inside `repo:root` so the workflow
can be exercised without widening scope or inventing new architecture. Use that
proof to decide what, if any, wrapper commands are still worth keeping, then
harden validation and query guidance only after the concrete flow reveals where
operators still need sharper support.

# Concrete Steps

1. Advance `ticket:1ypcbj0m` on one small shipped change that benefits the Loom
   bundle.
2. Keep the execution packet bounded and explicit about scope, trust boundary,
   and allowed writes.
3. Reconcile the execution outcome into the ticket, critique surface, wiki
   disposition, and any needed evidence.
4. Use that proved path to scope the smallest honest wrapper-command posture in
   `ticket:zomng8h3`, including the possibility that no new wrappers are
   justified.
5. Reconcile repo instruction surfaces so they describe the actual rewrite-era
   workflow rather than the retired script-era model.
6. Use observed workflow failures and ambiguities to scope `ticket:vyypge85`.
7. Run the smallest honest structural and manual validation after each landed
   slice.

# Validation and Acceptance

- frontmatter, links, and statuses should remain coherent for the initiative,
  spec, plan, tickets, and any proof-flow artifacts
- proof-flow work should include the smallest honest checks for the changed
  surfaces, such as `git diff -- .loom`, targeted `rg` queries for linked IDs,
  and manual inspection of changed rules, skills, templates, or wrappers
- acceptance should follow the normal Loom order: scope, evidence, canonical
  reconciliation, critique need, and wiki need

# Idempotence and Recovery

Each milestone is resumable because the strategy lives here while live progress
stays in the linked tickets.

If the proof slice fails or blocks, the next actor should update `ticket:1ypcbj0m`
instead of rewriting the plan. If wrapper or validation follow-up proves
unnecessary after the proof slice, close or cancel those tickets explicitly
rather than quietly letting them drift.

# Artifacts and Notes

- Governing initiative: `initiative:prove-core-loom-workflow`
- Governing spec: `spec:minimum-proven-core-workflow-surface`
- Primary execution ticket: `ticket:1ypcbj0m`
- Optional wrapper follow-up: `ticket:zomng8h3`
- Validation/query follow-up: `ticket:vyypge85`

# Interfaces and Dependencies

- Product surfaces likely touched by this plan: `rules/`, `skills/`, optional
  `commands/`, and related `references/` and `templates/` material
- Canonical reconciliation surfaces likely touched by the proof slice:
  `.loom/tickets/`, `.loom/critique/`, `.loom/wiki/`, `.loom/packets/`, and
  `.loom/evidence/`

# Linked Tickets

- `ticket:1ypcbj0m` - exercise one end-to-end proof flow
- `ticket:zomng8h3` - evaluate optional wrapper commands
- `ticket:vyypge85` - harden packet, scope, and workspace validation/query guidance

# Risks and Open Questions

- the first proof target may still be too large unless deliberately constrained
- wrapper design may sprawl unless grounded in the proved path
- validation changes may get ahead of the doctrine if the team is not careful
- the repo still needs later decisions about packet defaults, critique policy,
  and the right amount of shared query guidance

# Revision Notes

- 2026-04-04: created the plan to turn the current prioritization into one
  bounded proof slice followed by command and validation hardening.
- 2026-04-17: reconciled the plan to the rewrite-era model where wrappers are
  optional, YAML frontmatter is canonical, and `wiki`/`packets`/`evidence`
  replace `docs`/`runs`/`verification`.
