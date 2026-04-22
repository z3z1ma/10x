# Review Pass Splitting

Use pass splitting when one reviewer would be likely to miss risks because the
target is large, high risk, or spans multiple kinds of judgment.

## One-Pass Review

Use when:

- target is small
- risk is low or medium
- one reviewer can hold the target and governing context
- no fresh-context transport is available

## Multi-Pass Review

Use for medium or high risk targets when different lenses should stay separate.

Default passes:

1. Correctness and scope
   Check whether the code or artifact satisfies the ticket, spec, and declared
   write boundary.
2. Risk, security, and failure modes
   Check edge cases, assumptions, auth/data/security, performance, and rollback.
3. Operator clarity and follow-through
   Check ticket truth, evidence, critique disposition, wiki disposition, and
   whether the next agent can continue cold.

Each pass may produce its own critique record, or one consolidated critique
record with clearly separated pass sections.

## Packet Use

For packetized implementation review, compile one critique packet per pass when
fresh-context review is warranted.

For direct artifact critique, do not compile packets by default. Use a packet
only when the review is broad, high risk, or needs fresh-context isolation.

## Output

- pass split chosen and why
- critique profiles used
- findings with severity and confidence
- evidence reviewed
- follow-up recommendation
