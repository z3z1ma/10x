---
name: using-loom
description: "Always activate at session start before any response or action, unless this doctrine and references are already preloaded."
---

# using-loom

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply, you ABSOLUTELY MUST
invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This prevents silent scope invention, retroactive tickets, unbounded workers,
unsupported closure claims, and lost recovery context.
</EXTREMELY-IMPORTANT>

Loom is a human-agent control plane. Its durable state is the `.loom/` graph:
Markdown records for judgment, bounded execution, evidence, audit, and reusable
knowledge. Chat shapes the next move; records preserve what future agents need.

## Loop Order

Loom routing comes first. Activation is part of routing: if any Loom skill or
surface might own the next move, invoke the relevant skill before responding,
before asking clarifying questions, before code exploration, before quick checks,
before editing files, before creating tickets, and before launching Ralph. Use
workflow playbooks only after routing identifies the owning surface.

The default sequence is:

```text
shape with the operator -> route durable truth -> slice executable work -> execute
ticket slices through bounded Ralph runs -> preserve evidence -> audit claims ->
reconcile records
```

Ambiguity defaults to shaping, not implementation. Execute only when outcome,
scope, constraints, success criteria, evidence posture, non-goals, and material
system-shape or state implications are clear enough to avoid hidden product or
architecture choices. Otherwise inspect source and records, name the ambiguity,
shape it with the operator, and route the resolved truth before patching,
ticketing, or launching Ralph.

## Session Start

At session start, read this skill and ordered references unless they are already
preloaded with clear source markers.

Read in this order:

1. `references/00-how-loom-thinks.md`
2. `references/01-activation-discipline.md`
3. `references/02-directory-structure.md`
4. `references/03-shaping-with-humans.md`
5. `references/04-delegating-to-workers.md`
6. `references/05-proving-the-work.md`
7. `references/06-staying-safe.md`

After that, load active `Type: Knowledge Preference` records from
`.loom/knowledge/` when that directory exists. Retrieve other knowledge only when
the task, path, tool, error, ticket, or domain makes it relevant.

Then use the relevant Loom skill for the surface you are touching. If multiple
skills may apply, prefer the owning record skill, then any workflow playbook.

## Loom Surfaces

The Loom surfaces are:

- constitution: durable project judgment, policy, principles, constraints, ADRs, roadmap
- tickets: bounded executable work, live state, acceptance, closure posture
- research: investigation, tradeoffs, rejected paths, null results, synthesis
- specs: intended behavior, requirements, scenarios, interfaces, invariants
- plans: multi-ticket strategy, sequencing, rollout, validation, recovery
- evidence: observations, command outputs, reproductions, screenshots, logs, validation
- audit: adversarial review findings and verdicts from Ralph review runs
- knowledge: preferences, procedures, accepted explanations, reusable understanding

Retrospective is a promotion pass, not a surface. Use `loom-retrospective` after
significant work when learning, prevention notes, or reusable context should move
from chat or tickets into the right surface.

## Working Posture

Ask:

- What must be shaped with the operator before execution is honest?
- Am I inferring scope, system-shape, data-model, state-model, or coherence choices?
- Which surface owns the truth I am about to use or change?
- Is the next move still shaping, or is it ticket-ready execution?
- What ticket-owned context bounds this Ralph worker or review run?
- What evidence or audit makes the claim honest?
- What should future agents not have to rediscover?

Tiny, obvious, low-risk work can stay light. Create or update records when they
materially improve future recovery, judgment, execution, review, or reuse.

Red flags that mean stop and route through the relevant skill instead of acting
from habit:

| Rationalization | Loom reality |
| --- | --- |
| "this is simple" | Simple work still needs the right skill check when a Loom surface might own the next move. |
| "this is just a small change" | Small work can stay light only after the right surface is obvious and risk is low. |
| "I need more context first" | Skill invocation comes before clarifying questions, code exploration, or quick checks. |
| "I need to inspect first" | If inspection is part of a likely Loom workflow, invoke that workflow skill first. |
| "I'll create the ticket after" | Ticket-worthy work needs the ticket before execution, not as a retroactive wrapper. |
| "I'll ask the worker directly" | Worker handoff needs ticket-owned durable context and a bounded Ralph launch. |
| "evidence can wait" | Evidence posture is part of honest execution, not cleanup. |
| "audit is overkill" | Risk decides audit posture; convenience does not. |
| "I remember the skill" | Skill text evolves. Load the current relevant skill. |
| "I'll just do this one thing first" | One un-routed action is enough to lose the graph. Check the skill first. |

## Done Means

This skill is complete when the doctrine is loaded and the next move is routed to
the right surface or skill.
