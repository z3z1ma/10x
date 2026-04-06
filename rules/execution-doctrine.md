# Execution Doctrine

Loom execution stays reliable by separating parent workflow judgment from child bounded execution. Both roles operate on the corpus with standard file tools. Helper CLIs enter only for deterministic scaffolding and structural validation.

## Parent and Child Roles

The parent context owns:

- task classification and skill selection
- scope resolution
- reading and searching the corpus directly
- packet compilation and allowed-write-set declaration
- child launch
- post-run validation, reconciliation, and ticket-ledger update

The child context owns:

- bounded work inside the packet contract
- edits only inside the allowed write set
- verification evidence generation
- an explicit continue, stop, blocked, or escalate outcome

Both roles read records, search references, and edit files with the same standard tools. The parent does this to prepare and reconcile. The child does this to execute the bounded task. Neither role needs a special CLI layer for ordinary corpus work.

Read `appendices/worked-example-flow.md` for one concrete parent/child flow.

## Fresh-Context Rule

These flows SHOULD run in a fresh harness context:

- Ralph execution
- critique
- docs update

Prefer fresh child sessions for packet-consuming work because the packet should carry the bounded contract more reliably than a long saturated transcript.

Read `appendices/harness-invocation-templates.md` for launch shapes, prompt conventions, and post-return reconciliation.

## Write-Back Rule

Child runs MAY edit canonical records directly only when the packet says they may. Parent-side validation and reconciliation still gate acceptance.

Review-only and diagnostic packets SHOULD return findings or proposed changes instead of mutating canonical records.

If a child returns without durable write-back where durable write-back was required, treat the run as incomplete.

Read `appendices/acceptance-and-packet-playbook.md` when the next parent decision after a child run is ambiguous.
