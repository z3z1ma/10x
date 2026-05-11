---
id: research:grill-diagnose-gap-analysis
kind: research
status: concluded
created_at: 2026-05-07T14:57:22Z
updated_at: 2026-05-07T15:04:00Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:grill507
  ticket_related:
    - ticket:engdisc7
external_refs:
  matt_grill_with_docs: https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md
  matt_diagnose: https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md
---

# Question

How much gap remains between Matt Pocock's `grill-with-docs` / `diagnose` skills
and Loom's current spec, plan, and debugging guidance?

# Sources

Direct source reads from the local peer clone:

Observed `mattpocock-skills` local clone HEAD on 2026-05-07:
`70141119e9fe47430b62b93bcf166a73e6580048`.

- `mattpocock-skills:skills/engineering/grill-with-docs/SKILL.md:8-13` - the core loop is relentless interview, each design-tree branch, one question at a time, recommended answer for each question, and codebase-first answers when available.
- `mattpocock-skills:skills/engineering/grill-with-docs/SKILL.md:18-52` - domain awareness starts by looking for existing context and decisions; files are created lazily only when there is something real to write.
- `mattpocock-skills:skills/engineering/grill-with-docs/SKILL.md:56-70` - challenge glossary conflicts, sharpen fuzzy terms, discuss concrete edge scenarios, and cross-reference user claims against code.
- `mattpocock-skills:skills/engineering/grill-with-docs/SKILL.md:72-86` - resolved terms are captured inline, implementation trivia is excluded from domain language, and ADRs are offered only for hard-to-reverse, surprising, tradeoff-backed decisions.
- `mattpocock-skills:skills/engineering/diagnose/SKILL.md:10-16` - debugging starts by reading domain glossary/ADRs and treats feedback-loop construction as the core skill.
- `mattpocock-skills:skills/engineering/diagnose/SKILL.md:18-51` - feedback loops include tests, HTTP/CLI/browser scripts, trace replay, throwaway harnesses, fuzz/stress loops, bisection, differential loops, and human-in-the-loop scripts; no hypothesis phase without a credible loop.
- `mattpocock-skills:skills/engineering/diagnose/SKILL.md:65-89` - diagnosis uses ranked falsifiable hypotheses, one variable per probe, targeted instrumentation, and measurement-first performance work.
- `mattpocock-skills:skills/engineering/diagnose/SKILL.md:91-117` - fixes use a correct regression seam, rerun the original loop, clean instrumentation, and route architectural prevention after the fix.

Compared Loom surfaces:

- `skills/loom-specs/SKILL.md`
- `skills/loom-specs/references/spec-shape.md`
- `skills/loom-specs/templates/spec.md`
- `skills/loom-plans/SKILL.md`
- `skills/loom-plans/references/plan-shape.md`
- `skills/loom-plans/references/slicing.md`
- `skills/loom-plans/templates/plan.md`
- `skills/loom-debugging/references/systematic-debugging.md`

# Findings

## Spec Gap

Loom has `Problem Pressure Check`, options, non-goals, boundary tiers, and decision
points. That is useful but too static. It does not yet make grilling a required
creation discipline when behavior is fuzzy: inspect code/docs first, ask one
material question at a time, recommend an answer, challenge terminology conflicts,
invent concrete scenarios that probe boundaries, and capture resolved language or
durable decisions in the owner layer.

## Plan Gap

Loom plans mention decomposition and ticket slices, but the activation description,
opening definition, template order, and `plan-shape` framing still over-emphasize
sequencing, rollout, milestones, and waves. The primary plan job should be to turn
high-level work into detailed execution units that can become tickets. Sequencing
and waves organize those units; they are not the plan's center of gravity.

## Debugging Gap

Loom debugging is closer to Matt's diagnose loop than spec/plan guidance is, but
it still under-states domain orientation and the aggressive feedback-loop menu.
It should be clearer that no root-cause phase starts without a credible loop or an
explicit record of why no loop can yet exist.

# Decisions

- Bake grilling into `loom-specs` instead of creating a separate grill skill,
  because the durable output is intended behavior and acceptance.
- Bake planning grill/decomposition into `loom-plans` instead of `loom-workspace`,
  because the durable output is execution strategy and ticket-ready units.
- Keep domain language and ADR capture routed to Loom's existing wiki/spec/
  constitution/research owners, not Matt's specific `CONTEXT.md` layout.
- Tighten debugging reference only where the diagnose gap remains; do not duplicate
  the entire external skill.

# Recommendations

- Add a `Spec Grilling Pass` section to spec guidance and template.
- Add a `Planning Grilling Pass` and `Execution Units / Ticket Slices` emphasis to
  plan guidance and template.
- Reframe `loom-plans` frontmatter and top-level copy around decomposition into
  ticket-ready units.
- Expand debugging feedback-loop construction and domain-orientation language.

# Linked Work

- `ticket:grill507`
