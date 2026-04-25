# Ticket Readiness

A ticket is ready when the next governed owner can act without chat history.

Ralph-ready is stricter: the ticket must also make one bounded implementation
iteration, write boundary, likely verification posture, and expected output
contract legible enough for a fresh worker.

New tickets should normally start as `proposed`. Promote to `ready` only after
this checklist passes.

## Checklist

- the problem is clearly named
- why now is clearly named
- scope and non-goals are separated
- `change_class` is set when it would affect evidence, critique, or packet posture
- acceptance criteria are concrete enough to guide behavior
- coverage names relevant spec acceptance IDs when the work implements or
  verifies a spec
- relevant upstream artifacts are linked
- the likely evidence path is visible
- critique risk class and required profiles are explicit when review is
  expected
- the next owner is explicit: local edit, Ralph, critique, wiki, evidence,
  research/spec/plan refinement, or acceptance review
- the ticket is small enough to fit one bounded iteration or a short sequence of
  clearly staged iterations

If several of those are missing, do not force Ralph, critique, wiki, or closure.
Refine the ticket first.
