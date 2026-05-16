# Proving The Work

Claim done only when the graph supports the claim.

A command passed, a child worker said `done`, or a patch looks plausible is not
enough. Records and evidence should support the exact claim being made.

Make claims that are honest about what was observed, what was not observed, and
what risk remains.

## Evidence

Evidence records observations: command output, tests, screenshots, reproductions,
logs, manual observations, scans, review artifacts, or other validation outputs.

Before claiming a result, ask what evidence would make that exact claim honest.
Use the smallest evidence that is strong enough.

Evidence is claim-scoped. A passing unit test supports the behavior covered by
that test. A successful manual reproduction supports that reproduction. A clean
typecheck supports type correctness, not product correctness. A worker report is
not evidence unless it points to observed facts.

If evidence is partial, say so. Partial evidence is useful when represented
honestly. It becomes dangerous when treated as broader proof than it is.

## Audit

Audit records adversarial review, normally returned from a bounded Ralph review
run.

Use audit to turn implementation, evidence, and record claims into a reviewable
closure story. Tickets normally reach closure through audit; plans and other
surfaces use audit when their claims need independent pressure.

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

Tickets are Loom's fundamental unit of executable work. They scope the change,
drive code-facing execution, and keep the live state of that work honest.

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

Close tickets when the graph supports the closure claim.

## Knowledge And Retrospective

When significant work teaches something future agents should reuse, run a
retrospective promotion pass.

Move the learning into the right surface, especially knowledge when the result is
accepted explanation, reusable understanding, procedure, preference, or retrieval
cue.

Do not leave important lessons trapped in chat, tool logs, worker reports, or a
closed ticket whose title future agents will not search.

## Honest End State

At the end of meaningful work, be explicit about:

- what changed
- what was verified
- what was not verified
- what risks remain
- what record or surface now owns the durable truth
- what should happen next, if anything

If the work is incomplete, say so. If the evidence is narrow, say so. If the
claim depends on an assumption, say so.

Prefer explicit incompleteness to false closure.
