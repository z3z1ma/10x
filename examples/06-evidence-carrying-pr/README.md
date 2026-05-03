# 06 - Evidence-Carrying PR

## Starting `.loom` Slice

- `constitution:main`
- accepted spec with acceptance IDs
- release-packaging ticket in `ready`
- package evidence and critique are required before acceptance

## Operator Request

"Prepare the PR body for this release-packaging ticket using Loom records."

## Expected Flow

1. read constitution and the ticket's scoped claims
2. inspect covered spec acceptance IDs
3. package the PR summary from Loom records
4. record package evidence
5. run critique on the package
6. promote wiki explanation only if the packaging workflow is reusable
7. leave ticket closure to acceptance

## Expected Artifacts

- PR body or handoff package
- package evidence record
- critique/finding disposition summary
- residual risks and follow-ups
- no new truth owner

## Expected Final State

- PR text is a projection of Loom truth and package evidence
- ticket remains the execution ledger
- external package does not close the ticket

## Common Wrong Behavior

- writing a PR narrative from chat memory
- omitting critique findings or accepted risks
- treating the PR body as the acceptance decision
- copying live ticket state into an external issue tracker as canonical truth
