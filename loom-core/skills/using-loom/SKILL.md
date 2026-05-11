---
name: using-loom
description: "Always activate at session start in Loom workspaces before any other work, unless an adapter has already preloaded this doctrine and references."
---

# using-loom

Loom is a human-agent control plane for AI-driven software engineering.

Loom works through two connected loops.

The outer loop keeps the agent and operator shaping the work until the next move is
understood, bounded, and routed into the right durable surface. Those surfaces are
Markdown records written for humans and agents, with directory names for `find` and
stable words, headings, labels, IDs, and refs for `grep`.

The inner loop uses bounded worker packets to run fresh-context or separate-context
work, and fresh-context audit to challenge claims before records rely on them.
Packets carry enough source-linked context, scope, constraints, stop conditions,
and evidence expectations for the worker to act without relying on chat history,
while keeping the relevant records truthful as it works.

Use the Loom surfaces to preserve the shaped work, bounded execution, evidence,
audit, and reusable knowledge that future agents need.

## Loop Order

Loom routing comes first. Use workflow-specific skills only after this doctrine
has established whether the work is still outer-loop shaping or ready for bounded
execution.

The default sequence is:

```text
shape with the operator -> route durable truth -> slice executable work -> execute
bounded tickets or packetized worker runs -> preserve evidence -> audit claims ->
reconcile records
```

When product intent, success criteria, quality bar, scope, evidence posture, or
ticket boundary is unclear, stay in the outer loop. A workflow-specific skill can
add pressure, but it still moves through Loom surfaces and the same loop order.
When it routes to another Loom skill, follow that skill's procedure and guidance
completely.

## Session Start

At the start of a Loom session, read this skill and all references below unless an
adapter has already preloaded the same doctrine with clear source markers. Do not
spend context twice when the doctrine is already present.

Read in this order:

1. `references/how-loom-thinks.md`
2. `references/directory-structure.md`
3. `references/shaping-with-humans.md`
4. `references/delegating-to-workers.md`
5. `references/proving-the-work.md`
6. `references/staying-safe.md`

After that, load active `Type: Knowledge Preference` records from
`.loom/knowledge/` when that directory exists. Retrieve other knowledge only when
the task, path, tool, error, ticket, or domain makes it relevant.

Then use the relevant Loom skill for the surface you are touching.

## Loom Surfaces

Loom records are Markdown files designed to be found, read, and connected with
ordinary `find` and `grep` workflows.

The Loom surfaces are:

- constitution: durable project judgment, policy, principles, constraints, ADRs,
  and roadmap direction
- tickets: the fundamental work unit where executable change is scoped, driven,
  and tracked
- research: investigations, tradeoffs, synthesis, rejected paths, and conclusions
- specs: intended behavior, requirements, scenarios, and interfaces
- plans: operator-shaped strategy for complex changes that exceed one bounded
  ticket, including decomposition, dependencies, validation, and recovery
- evidence: observed facts, outputs, reproductions, screenshots, logs, and
  validation
- audit: fresh-context review of claims, risks, evidence, and implementation shape
- knowledge: preferences, procedures, accepted explanation, reusable
  understanding, and retrieval cues
- packets: bounded contracts for worker handoff

Retrospective is a promotion pass after significant work: decide what learning
should move into the right surface instead of leaving it in chat. Use
`loom-retrospective` for that pass when the work is non-trivial or prevention
follow-up may matter.

## Working Posture

Ask:

- What must be shaped with the operator before execution is honest?
- What surface owns the truth I am about to depend on or change?
- Is this still a human-shaped outer-loop problem, or is it safe to execute?
- What is the next smallest ticket-ready slice, and what makes it complete?
- What packet bounds this worker handoff?
- What evidence or audit would make the claim honest?
- What knowledge should future agents load, retrieve, or not have to rediscover?

Tiny, obvious, low-risk work can stay light. Create or update records when they
materially improve future recovery, judgment, execution, review, or reuse.

## Done Means

This skill is complete when the doctrine is loaded and the next move is routed to
the right surface or skill.
