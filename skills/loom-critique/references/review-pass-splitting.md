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

1. Acceptance and scope compliance
   Check whether the actual diff or artifact satisfies the ticket, spec,
   acceptance coverage, and declared write boundary. Look for missing requested
   behavior and extra unrequested behavior before judging polish.
2. Implementation quality and maintainability
   Check separation of concerns, naming, test shape, real-behavior coverage,
   YAGNI/DRY tradeoffs, and fit with existing patterns.
3. Risk, security, and failure modes
   Check edge cases, assumptions, auth/data/security, performance, migration,
   rollback, and operational hazards.
4. Operator clarity and follow-through
   Check ticket truth, evidence, critique disposition, retrospective / promotion
   disposition, wiki-specific disposition when applicable, and whether the
   next agent can continue cold.

Each pass may produce its own critique record, or one consolidated critique
record with clearly separated pass sections.

When splitting into two broad passes, run acceptance/spec compliance before code
quality. First decide whether the target built the right thing, stayed in scope,
and has enough evidence. Then decide whether it is well-built. A polished
implementation of the wrong behavior is still a finding, not a quality pass.

## Packet Use

For packetized implementation review, compile one critique packet per pass when
fresh-context review is warranted.

If the harness supports subagents or multiple fresh reviewers, the parent may
launch independent passes in parallel with one critique packet per pass. If not,
run them sequentially as distinct fresh-context passes with narrow prompts. The
transport is flexible; the pass boundaries are not.

Never let a child report substitute for review. Reviewers inspect the actual
diff, changed files, records, tests, and evidence. A child report is a source to
check, not proof.

For direct artifact critique, do not compile packets by default. Use a packet
only when the review is broad, high risk, or needs fresh-context isolation.

## Review Loop Stalls

Review/fix loops should converge. They are stalling when:

- the same medium/high finding reappears after a fix attempt;
- each fix exposes a new owner-layer, scope, behavior, or evidence gap;
- feedback remains unclear after one focused clarification attempt;
- review comments are being implemented mechanically without resolving the
  challenged claim;
- the ticket cannot disposition findings without changing the spec, plan,
  research, or scope.

When a review loop stalls, stop treating the next action as another patch. Route
the blocker to the owner that can resolve it:

- unclear intended behavior -> spec or ticket acceptance refinement
- insufficient evidence -> evidence or debugging/spike route
- repeated implementation shape failure -> plan, codemap, research, or architecture
  critique
- disputed policy or authority -> constitution or protocol critique
- out-of-scope but real issue -> follow-up ticket with `converted_to_follow_up`
- accepted residual risk -> ticket acceptance decision with provenance

For high-risk work, two unsuccessful fix/review rounds on the same finding should
normally trigger escalation to the parent ticket or operator decision before a
third implementation attempt. Record the ticket-owned disposition before closure;
do not let an endless critique loop become the live ledger.

## Output

- pass split chosen and why
- critique profiles used
- findings with severity and confidence
- evidence reviewed
- follow-up recommendation
- stalled-loop assessment when repeated findings or unclear feedback affected the
  review
