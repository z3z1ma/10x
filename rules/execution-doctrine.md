# Execution Doctrine

Loom execution stays reliable by separating parent workflow judgment from child bounded execution.

## Parent and Child Roles

The parent context owns:

- task classification
- skill hydration
- scope resolution
- packet compilation
- allowed write set declaration
- child launch
- post-run validation and reconciliation

The child context owns:

- bounded work inside the packet contract
- direct edits only inside the allowed write set
- verification evidence generation
- explicit continue, stop, blocked, or escalate outcomes

The parent owns workflow judgment.

The child owns bounded execution inside the packet contract.

Read `appendices/worked-example-flow.md` when you want one concrete parent/child flow instead of the abstract rule set.

## Fresh-Context Rule

The following flows SHOULD run in a fresh harness context:

- Ralph execution
- critique
- docs update

Prefer fresh child sessions for packet-consuming work because the packet should carry the bounded contract more reliably than a long saturated transcript.

Read `appendices/harness-invocation-templates.md` when you need the launch shape, prompt shape, or post-return reconciliation checklist.

## Write-Back Rule

Child runs MAY edit canonical records directly only when the packet says they may. Parent-side validation and reconciliation still gate acceptance.

Review-only and diagnostic packets SHOULD return findings or proposed changes instead of mutating canonical records.

If a child returns without durable write-back where durable write-back was required, treat the run as incomplete.

Read `appendices/acceptance-and-packet-playbook.md` when the next parent decision after a child run is still ambiguous.
