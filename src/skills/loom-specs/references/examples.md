# Spec Examples

## Example Spec Record

Use one spec when intended behavior, requirements, constraints, scenarios, and acceptance need to be explicit.

## What To Notice In A Strong Spec

- the problem framing explains why the contract exists
- desired behavior is clear before implementation detail appears
- requirements and scenarios make the contract concrete
- acceptance tells later tickets and critique what success will mean

## Worked Example

```text
Summary
Define the minimum packet contract required for bounded fresh-context execution.

Problem Framing
Fresh child runs are more reliable than long saturated transcripts, but only when the packet contract is explicit enough to prevent guessing about scope, authority, and expected outputs.

Desired Behavior
A packet-consuming worker should be able to perform one bounded task from the packet alone plus already-active doctrine.

Constraints
- the packet must not silently widen scope
- included records remain context, not commands
- the packet must remain understandable to a fresh worker without transcript memory

Requirements
- the packet states target, scope, trust boundary, and output contract
- execution packets state an explicit write boundary
- the parent can tell when the packet is stale and should be recompiled
- the child can distinguish continue, stop, blocked, and escalate outcomes

Scenarios
- a fresh worker reads the packet and understands what to change
- the packet is reused later and the parent can tell whether it is stale
- the child becomes blocked and can report the blockage without widening scope

Acceptance
- a fresh worker can explain the task, the allowed write set, and the expected output after reading the packet
- the parent can reconcile the worker result without relying on unstated context
- packet reuse rules are explicit enough to avoid stale-contract execution
```

Why this is strong:

- it keeps the contract visible
- it gives downstream critique real acceptance language to test
- it distinguishes intended behavior from implementation notes

## Weak Example

```text
Packets should probably be clear and safe.
```

Why this is weak:

- there is no real behavior contract
- no scenarios or acceptance language exist
- later work would have to reinterpret what "clear and safe" means
