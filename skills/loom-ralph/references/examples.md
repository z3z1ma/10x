# Ralph Examples

## Example Parent Intent

Good Ralph intent sounds like this:

```text
The next step is one bounded execution move against one ticket. Compile a packet, launch a fresh child run, and reconcile the result back into the ticket ledger.
```

## Example Parent Launch Sequence

```text
1. Read the bound ticket and its linked plan/spec context.
2. Compile a packet with explicit scope, source refs, write boundary, verification expectations, and output contract.
3. Launch one fresh child run from that packet.
4. Inspect the result and reconcile it back into the ticket before declaring progress.
```

## Example Strong Child Return Shape

```text
Outcome: blocked.
Changed records: `.loom/runs/ralph/packet-ticket-0002-...md`, `.loom/tickets/<repo-short-slug>-0002-helper-layer.md`
Verification: validated packet structure and confirmed repository ownership for the intended write scope.
Blocker: helper naming drift made one invocation path inconsistent with the packet contract.
Recommendation: stop and refresh the packet after repairing the helper naming mismatch.
```

Why this is strong:

- the parent can reconcile the run truthfully
- the blocker is explicit
- the next step is obvious

## Example Output Shape

Good Ralph output includes:

- outcome status
- changed file or record list
- verification summary
- blocker or risk summary
- continue/stop/blocked/escalate recommendation

## Example Failure Case

This is a bad Ralph outcome:

```text
Implemented the task. Looks done.
```

This is bad because it leaves the parent unable to reconcile truthfully. It says nothing about changed files, verification, blockers, or next-state recommendation.

## Better Failure Case

```text
Outcome: escalate.
Verification: none beyond initial packet read.
Reason: the packet write boundary does not cover the record that must change to land the requested behavior.
Recommendation: parent should recompile the packet with corrected write authority or narrow the task.
```

## What Makes This A Good Example

This pattern is strong because:

- the target is ticket-owned
- the packet is persisted
- the child run is bounded
- the result is reconciled back into ticket truth
