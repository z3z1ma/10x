# Ticket Readiness

A ticket is ready when the next governed route can proceed without chat history.

Ralph-ready is stricter: the ticket must also make one bounded implementation
iteration, write boundary, likely verification posture, and expected output
contract legible enough for a fresh worker.

New tickets should normally start as `proposed`. Promote to `ready` only after
this checklist passes.

## Checklist

- the problem is clearly named
- why now is clearly named
- scope and non-goals are separated
- `change_class` and `risk_class` are set in frontmatter for new tickets and for
  tickets being materially updated for readiness, Ralph, critique, acceptance,
  reopening, or closure; normalize legacy tickets when touched or before
  governed execution or acceptance, without treating their prior absence as
  instant non-conformance
- acceptance criteria are concrete enough to guide behavior
- coverage names relevant spec acceptance IDs when the work implements or
  verifies a spec
- relevant upstream artifacts are linked
- the likely evidence path is visible
- critique risk class matches frontmatter `risk_class`; required profiles are
  explicit when review is expected
- the next route is explicit: local edit, Ralph implementation packet, direct
  critique, wiki/retrospective pass, evidence recording, research/spec/plan
  refinement, or ticket acceptance review
- the ticket is small enough to fit one bounded iteration or a short sequence of
  clearly staged iterations

If several of those are missing, do not force Ralph, critique, wiki, or closure.
Refine the ticket first.
