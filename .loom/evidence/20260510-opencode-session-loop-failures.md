# OpenCode Session Loop Failure Observations

Status: recorded
Created: 2026-05-10
Updated: 2026-05-10
Observed: 2026-05-10

## Observation

The OpenCode session `ses_1eac9757bffeq3eku2u7S0Za07` was inspected through the local OpenCode SQLite database and the committed eval records under `evals/dota2/with-loom/.loom/`.

Observed session facts:

- The initial operator request was broad product work: "Lets build a warcraft 3 inspired website based on this API ... We want it to feel like being in a video game ... novel web experience. Use loom."
- The assistant replied that the work was ticket-sized and proceeded toward implementation before product-quality direction, success criteria, evidence expectations, or ticket decomposition were shaped with the operator.
- After the operator challenged that framing, the assistant created spec, research, plan, ticket, evidence, and audit records and completed a static MVP, then returned it as complete.
- The operator later clarified that the goal was a production-feel app and that Loom's outer loop should have asked shaping questions before locking scope and closure.
- The assistant then shaped a Campaign Map direction with the operator but created one oversized production ticket, later cancelled after the operator challenged ticket slicing.
- The eventual eval records show a corrected split into stack foundation, summary data foundation, Campaign Map shell, hero deep territories, match battle reports, and production verification tickets.
- The session used harness-native `task` subagents for source summaries and fresh-context review. No `.loom/packets/ralph/*.md` packets were created in the eval workspace, and task prompts carried the worker contract directly.

## Procedure

Commands and inspections used:

- Queried `/Users/alexanderbutler/.local/share/opencode/opencode.db` for text parts and task-tool prompts for session `ses_1eac9757bffeq3eku2u7S0Za07`.
- Read committed eval records under `evals/dota2/with-loom/.loom/`, including the active spec, plan, initial static ticket, broad cancelled ticket, and audit records.
- Checked `evals/dota2/with-loom/.loom/packets/` via glob; no Markdown Ralph packets were present.

## What This Shows

- Supports `.loom/research/20260510-loom-loop-failure-analysis.md`: the failure modes were observable in a real eval transcript and committed eval records.
- Supports `.loom/tickets/20260510-core-loop-hardening.md`: the corpus needs clearer positive guidance for shaping, slicing, and packetized worker handoff.

## What This Does Not Show

- It does not prove every harness, model, or adapter would fail the same way.
- It does not identify hidden model reasoning beyond the persisted transcript parts and records.
- It does not evaluate the final app's product quality.

## Related Records

- `.loom/research/20260510-loom-loop-failure-analysis.md` - synthesizes these observations into protocol hardening recommendations.
- `.loom/tickets/20260510-core-loop-hardening.md` - consumes the observations for implementation slices.
