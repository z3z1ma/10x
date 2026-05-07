# Outer Loop

This is an ordered reference for the `using-loom` skill.

The outer loop is Loom's scoping and framing engine.

Its job is to make the work small enough, clear enough, and honest enough that the inner loop can execute without guessing.

## The Outer Loop Questions

Before you compile a packet, start coding, or choose a downstream route, answer these questions:

1. what durable problem or opportunity exists
2. what layer currently owns it
3. what larger strategic frame constrains it
4. what evidence is missing
5. what behavior is still fuzzy
6. whether this is small enough for a ticket or complex enough to need planning
7. what is the next bounded ticket-sized step

If you cannot answer those, you are not ready for the inner loop yet.

## Backbone Progression

The default progression is:

`constitution -> initiative -> plan -> ticket`

Use it like this:

- update **constitution** when principles, identity, or hard constraints changed
- create or refine an **initiative** when the outcome is strategic and cross-cutting
- create **research** when the work needs investigation before committing
- create a **spec** when intended behavior is unclear or acceptance is fuzzy
- create a **plan** when complex change needs high-level planning before tickets
- create a **ticket** when one bounded execution owner is needed

Not every task needs every layer.
But every non-trivial task should be explainable against this model.

## Ticket Readiness Standard

A ticket is ready only when it makes the next governed move obvious enough that a fresh worker or reviewer does not need transcript context to begin.

Ralph-ready is a stricter subset of ticket-ready: the ticket must also name one
bounded implementation iteration, write boundary, likely verification posture,
and expected output contract.

A ready ticket should make all of these legible:

- why this work matters now
- what is in scope
- what is out of scope
- what acceptance means
- what artifacts constrain the work
- what evidence the parent will expect
- which blockers, evidence gaps, critique gaps, acceptance gaps, or journal facts
  a fresh agent should inspect before continuing
- whether packaging or handoff is needed, without treating shipping as ticket
  closure

If the ticket cannot do that, keep working in the outer loop.

## When To Add Research

Add or update research when:

- you are making decisions from weak evidence
- multiple options exist and the tradeoffs matter
- you are about to encode assumptions into a spec or plan
- an implementation discovery should remain citable

A research record should end the need to rediscover the same reasoning later.

## When To Add A Spec

Add or update a spec when:

- the intended behavior is under-specified
- acceptance criteria are vague
- different plausible implementations would lead to materially different outcomes
- critique or wiki will need one stable behavior source later

Specs turn "I think we mean X" into "the project currently intends X".

## When To Add A Plan

Add or update a plan when:

- the change is complex enough that jumping straight to tickets would force the
  agent to guess the shape of the work
- one ticket is not enough
- the order of work matters
- rollout strategy matters
- there are dependencies or phases that future tickets should inherit

Plans are for planning. They own the high-level shape of complex change:
decomposition, sequencing, dependencies, phases, rollout, milestones, execution
waves, and strategy that future tickets should inherit. Once the plan is clear,
create tickets that go into the bounded execution detail for each planned slice.
Plans are not live execution ledgers.

## Decomposition Rule

The outer loop should keep decomposing until the next step is bounded enough to fit one of these shapes:

- one tiny local execution step with no packet
- one `ralph` implementation packet
- one workflow-coordinator pass such as `debugging`, `spike`, `codemap`, or
  `ship`
- one critique pass
- one wiki pass
- one owner-layer refinement or review pass

If the current state needs operator input, workspace repair, records repair,
evidence preservation, continuation, or stop, handle that need directly in the
owner layer instead of forcing another implementation pass.

If the next step still feels like "do the whole feature", it is not decomposed enough.

## Loopback From Ralph

The inner loop is allowed to discover that the outer loop was incomplete.

When Ralph returns with:

- ambiguous behavior
- missing evidence
- missing strategy
- missing constraints
- ticket too wide
- scope unexpectedly larger than expected

the parent should go back outward instead of forcing execution through ambiguity.

Typical loopbacks:

- Ralph -> research when evidence or tradeoffs are missing
- Ralph -> spec when intended behavior is ambiguous
- Ralph -> plan when the high-level execution shape or sequencing is wrong
- Ralph -> ticket refinement when the execution owner is too wide or stale
- Ralph -> initiative when objective or autonomy framing was missing
- Ralph -> constitution in rare architectural or policy cases

## Consult Constitution Before Deciding

Before making a non-trivial architectural or policy choice, check whether the constitution subsystem already speaks to it.

Constitution, decision records, and roadmap records are precedent, not history. Re-deriving a choice the project already made wastes work and risks contradicting accepted policy.

Practical checks at the start of outer-loop work:

- `rg -n '^id:' .loom/constitution` to list the current constitutional surface
- `find .loom/constitution/decisions -name '*.md' | sort` to scan prior decisions
- `rg -n '<topic>' .loom/constitution` to see whether this topic already has policy

If prior constitutional truth applies, inherit it. If the new work contradicts it, treat that as a loopback into the constitution subsystem — either amend the policy explicitly or change the work, not silently both.

## Strategic Restraint

The outer loop should clarify the work without over-architecting it.

Do not create records just to satisfy bureaucracy.
Create them because a future agent would genuinely need them.

The right question is not "can I make another artifact?"
The right question is "what artifact would reduce ambiguity, improve safety, or preserve understanding here?"
