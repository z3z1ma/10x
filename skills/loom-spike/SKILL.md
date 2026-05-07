---
name: loom-spike
description: "Run bounded spike or sketch investigations. Use when prototyping a data model, state machine, API shape, integration, performance idea, or several UI/product variants before committing to implementation."
compatibility: Markdown-native, script-free Loom protocol.
metadata:
  skill_kind: workflow
---

# loom-spike

Spikes and sketches are research-shaped workflows.

They are useful when the project needs bounded discovery before commitment.

## What This Workflow Coordinates

- spike experiment framing
- sketch variant framing
- throwaway write-scope discipline
- evidence and null-result capture
- downstream routing after discovery

## Use This Skill When

- a technical question needs a bounded experiment
- a design question needs a few concrete variants
- a throwaway prototype should inform a spec, plan, ticket, or wiki page
- rejected paths and null results should remain citable

## Do Not Use This Skill When

- the intended behavior is already clear enough for a normal ticket
- the work needs production-quality implementation
- the artifact should become accepted explanation without critique or evidence

## Spike Flow

`question -> experiment matrix -> bounded throwaway child write scope -> evidence -> conclusions/null results -> downstream route`

Pick the branch before writing throwaway work:

- logic/state prototype when the question is about state transitions, data shape,
  API feel, or business rules;
- UI/product sketch when the question is about what a page, flow, affordance, or
  layout should feel like;
- technical experiment when the question is about feasibility, integration,
  performance, migration, or failure mode.

If the branch is ambiguous and the answer would change the artifact shape, ask a
focused question or record a reversible assumption before continuing.

If the spike only reads, compares, sketches, or records observations, research
and evidence may be enough. If the spike writes throwaway code, changes source
files, generates prototype artifacts, or makes other non-record repository
mutations, create or tighten a ticket and use a Ralph packet with explicit
cleanup expectations.

Ordinary Loom record updates that preserve research, evidence, spec, or wiki truth
are not throwaway prototype mutations by themselves; route them through their
owning skills. The ticket/Ralph branch is for throwaway code, source-tree changes,
generated prototype artifacts, or other non-record repository mutations.

Throwaway prototypes should answer one explicit question. Keep them obviously
temporary, runnable through one existing project command where practical, free of
production persistence by default, and instrumented enough to show the relevant
state after each action or variant switch. Skip polish, broad error handling, and
abstractions unless they are required to answer the question.

Record:

- question
- method
- experiment matrix
- child write scope and cleanup expectation
- run command or inspection method for throwaway artifacts when a prototype is
  created
- evidence gathered
- conclusions
- null results or rejected paths
- recommended downstream owner

Use a variant or experiment matrix when comparing options:

| Variant / hypothesis | Artifact or probe | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |

## Sketch Flow

`design question -> 2-3 variants -> screenshots or artifacts -> critique -> accepted wiki/spec updates`

Sketches are the Loom adaptation of visual brainstorming. Use them when seeing a
mockup, diagram, state flow, layout comparison, or spatial relationship would
make a decision more honest than text alone.

Record:

- design question
- variants
- screenshots, prototypes, or other artifacts
- critique findings
- accepted behavior or explanation
- downstream spec, wiki, or ticket recommendation

UI/product variants should be structurally different: different layout,
information hierarchy, interaction model, or primary affordance. Variants that
only change color, copy, or spacing are tweaks, not sketch exploration.

If a harness or local tool helps produce visual artifacts, treat that tool as
transport. It does not become a Loom layer. Preserve durable outputs in evidence
and route accepted behavior or explanation to spec or wiki.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I can just implement the first plausible idea." | Spikes exist when the first plausible idea may be wrong; compare enough variants or hypotheses to learn. |
| "This prototype is useful, so we should keep it." | The answer is worth keeping. Throwaway scaffolding should be deleted, absorbed deliberately, or clearly contained. |
| "Persistence makes the prototype more realistic." | Persistence is usually the thing being tested; otherwise it creates cleanup risk and accidental dependency. |
| "Three UI variants that share the same layout are enough." | Sketch variants must disagree structurally or they will not reveal product direction. |
| "No evidence is needed because it was exploratory." | Exploration produces observations, rejected options, null results, and downstream recommendations worth preserving. |

## Red Flags

- prototype branch does not match the question being answered
- throwaway code writes production data or becomes a hidden dependency
- prototype has no clear question, run path, visible state, or cleanup expectation
- variants differ only cosmetically
- conclusions live only in chat or screenshots with no research/evidence link
- cleanup or downstream route is unspecified

## Verification

- [ ] Question and chosen branch are explicit.
- [ ] Variant/experiment matrix records strengths, weaknesses, and decisions when options were compared.
- [ ] Evidence preserves artifacts or observations.
- [ ] Accepted behavior routes to spec; accepted explanation routes to wiki.
- [ ] Throwaway code is deleted, absorbed, or explicitly contained.
- [ ] Spikes that write throwaway code, source-tree changes, generated prototype
  artifacts, or other non-record repository mutations reconcile ticket state,
  evidence, critique disposition, and cleanup outcome before downstream work relies
  on the result.

## Done Means

- research owns conclusions and null results
- evidence owns observed artifacts
- any accepted behavior is routed to spec
- any accepted explanation is routed to wiki
- throwaway code is removed or explicitly contained
- if the spike wrote throwaway code, changed source files, generated prototype
  artifacts, or made other non-record repository mutations, the owning ticket
  tells the truth about state, evidence, review disposition, and cleanup

## Read In This Order

Read immediately for spike or sketch work:

1. `skills/loom-research/SKILL.md` when recording experiment method,
   conclusions, rejected options, or null results.
2. `skills/loom-evidence/SKILL.md` when preserving screenshots, logs,
   artifacts, or observed outputs.

Then read conditionally:

3. `skills/loom-tickets/SKILL.md` and `skills/loom-ralph/SKILL.md` when the
   spike or sketch writes throwaway code, changes source files, generates
   prototype artifacts, or makes other non-record repository mutations.
4. `skills/loom-critique/SKILL.md` when variants or experiment conclusions need
   adversarial review.
5. `skills/loom-specs/SKILL.md` when accepted behavior should become a contract.
6. `skills/loom-wiki/SKILL.md` when accepted explanation should become reusable.
