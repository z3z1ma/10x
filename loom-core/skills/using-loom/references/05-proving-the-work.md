# Proving The Work

Claim done only when the graph supports the claim. A passing command, worker
report, or plausible patch is not enough. State exactly what was observed, what
was not observed, and what risk remains.

## Evidence

Evidence records observations: command output, tests, screenshots, reproductions,
logs, manual checks, scans, review artifacts, and validation outputs.

Before claiming a result, ask what evidence would make that exact claim honest.
Use the smallest evidence that is strong enough.

Evidence is claim-scoped: a unit test proves its covered behavior, a reproduction
proves that reproduction, and a typecheck proves type correctness. Worker output
is not evidence unless it points to observed facts.

If evidence is partial, say so. Partial evidence is useful when represented
honestly and dangerous when treated as broader proof than it is.

## Audit

Audit records adversarial review, normally from bounded Ralph. Use audit when
implementation, evidence, or record claims need independent pressure before
another surface relies on them. Tickets normally reach closure through audit.

Audit asks:

- whether the work is actually good
- whether the claims are supported
- whether the implementation matches the intended behavior
- what assumptions remain unproven
- what risks remain
- what evidence is missing
- what must happen before acceptance

Audit sharpens acceptance; it does not grant acceptance automatically.

## Tickets And Closure

Ticket details belong to the ticket skill, but the always-on rule is simple: do
not claim closure unless the ticket, evidence, audit state, and affected records
tell one truthful story.

A closure claim should make clear:

- what changed
- what acceptance criteria were satisfied
- what evidence supports that claim
- what audit challenged and concluded
- what was not verified
- what risks remain
- what follow-up exists, if any

## Knowledge And Retrospective

After significant work, use retrospective to promote reusable learning into the
right surface, especially knowledge for accepted explanations, procedures,
preferences, and retrieval cues. Do not leave important lessons trapped in chat,
tool logs, worker reports, or a closed ticket future agents will not search.

## Honest End State

At the end of meaningful work, be explicit about:

- what changed
- what was verified
- what was not verified
- what risks remain
- what record or surface now owns the durable truth
- what should happen next, if anything

If the work is incomplete, say so. If the evidence is narrow, say so. If the
claim depends on an assumption, say so. Prefer explicit incompleteness to false
closure.
