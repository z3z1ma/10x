# Acting On Tickets

Use this when acting from, resuming, updating, blocking, reviewing, or closing a
ticket.

The ticket is the executable work unit and live state ledger. Treat it as the
source of scope, acceptance, current state, related records, and journal truth.
Use ticket-owned Ralph runs for bounded implementation, review, inspection, and
audit slices that act on the ticket.

## First Move

Read the whole ticket before editing code or records.

If the ticket has `## Related Records`, read or already know those records before
acting. If a related record is unavailable, stale, or contradicts the ticket, stop
and surface the problem instead of guessing.

If repo changes are involved, inspect the current workspace state before editing:

```bash
git status --short
```

## Preflight Check

Before execution, check:

* `Status:` is `open` or `active`, unless the user explicitly asked to inspect,
  review, unblock, cancel, or close it
* `Risk:` still fits the work
* scope is narrow enough to act
* `ACC-*` criteria are concrete enough to verify
* Current State does not name a blocker that prevents this step
* related records needed for execution have been read
* evidence and audit expectations are understood
* the likely write boundary is consistent with the ticket
* the next Ralph run can express the bounded execution or review slice from ticket
  context

Before launching or consuming the first worker run, set `Status: active` and
update `Updated:`.

## During Work

Stay inside the ticket boundary.

Ticket execution uses bounded Ralph runs. For each implementation, focused review,
source-inspection, or audit slice, use `loom-ralph`. The ticket and linked records
should already say what files and records may change, what evidence is expected,
what stop conditions apply, and what output must be reconciled.

When the current session performs the work instead of launching another worker,
the current session is still acting inside the ticket-owned Ralph boundary. Keep
the ticket inspectable as the durable execution contract when the result will
affect ticket state, evidence, audit, or closure.

Do not batch unrelated cleanup, opportunistic refactors, nearby fixes, unrelated
record edits, or extra features into the ticket. If nearby work is valuable, create
or propose a separate ticket.

Update the ticket when future continuation would be worse without the note. That
usually means:

* material progress
* material code or record change
* blocker discovered
* assumption changed
* scope pressure appeared
* acceptance changed
* evidence gathered
* audit or review result recorded
* status changed
* closure reached

Do not turn the journal into a transcript. Record the material path.

## Ambiguity Routing

If material ambiguity appears, do not silently invent scope.

Use this routing:

* behavior ambiguity goes to specs
* sequencing ambiguity goes to plans
* evidence, feasibility, or tradeoff uncertainty goes to research
* durable policy or precedent goes to constitution
* reusable accepted explanation goes to knowledge
* adversarial review findings go to audit
* operator-owned decisions go to the operator

Set `Status: blocked` when the work cannot proceed safely. Record the concrete
blocker in Current State and append a journal entry.

Low-risk reversible assumptions may remain inside the ticket only when they do not
change scope, acceptance, or external behavior. Record them.

## Scope Or Acceptance Changes

Do not casually rewrite scope or acceptance during execution.

A scope or acceptance change is allowed only when it makes the ticket more
truthful. When changing either:

* update `Updated:`
* revise Current State
* append a Journal entry explaining why the change was needed
* preserve old context when losing it would make the work hard to audit
* route to spec, plan, research, or operator decision if the change is material

If the ticket has become two work units, split rather than widening it.

## Evidence

Gather evidence proportional to the claim.

Evidence can include:

* tests run and their outcome
* commands run and their outcome
* manual verification performed
* files inspected
* diffs reviewed
* acceptance criteria checked
* reason verification was not possible or not appropriate

Do not claim verification that did not happen. If evidence is missing, say so in
Current State or Journal and leave the status honest.

## Review State

Set `Status: review` when the implementation or record work appears complete but
audit, verification, or acceptance review is still the next honest move.

Use `review` instead of `closed` when:

* tests or validation have not been run
* acceptance needs an explicit check
* audit expectations remain
* risk warrants another pass
* the work may be complete but the ticket does not yet tell a trustworthy story

Use review state for the Ralph audit pass instead of closing directly from the
implementation state.

## Closure

Close only when:

* every `ACC-*` criterion is satisfied or revised with authority before closure
* unsatisfied acceptance is handled by a non-closed status, cancellation,
  authorized scope change, or follow-up work instead of hidden inside closure
* evidence named in Acceptance exists or its absence is justified
* audit has happened, or the ticket explains why a separate audit would not add
  useful trust
* Current State accurately describes the final state
* Journal records the material path to closure
* known residual risk is named rather than hidden

Set `Status: closed` only when the ticket tells one truthful story.

Set `Status: cancelled` when the work should not proceed. Record why, who or what
made that decision, and what related work remains if any.
