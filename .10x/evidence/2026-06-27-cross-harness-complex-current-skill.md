Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Relates-To: .10x/specs/10x-autoresearch-loop.md, .10x/evidence/2026-06-27-autoresearch-instruction-delivery.md

# Cross-Harness Complex Current Skill Trial

## What Was Observed

The committed autoresearch tooling ran three complex current-`SKILL.md`
scenarios through both `codex-cli` and `opencode-cli`.

Artifacts:

- Codex output root:
  `.10x/evidence/.storage/2026-06-27-cross-harness-complex/codex`
- OpenCode output root:
  `.10x/evidence/.storage/2026-06-27-cross-harness-complex/opencode`
- Codex report:
  `.10x/evidence/.storage/2026-06-27-cross-harness-complex/codex/report.md`
- OpenCode report:
  `.10x/evidence/.storage/2026-06-27-cross-harness-complex/opencode/report.md`

Both runs completed 3/3 subject calls with zero timeouts. Both
`canonical_guard.json` files record `unchanged_during_run: true` for `SKILL.md`
and `autoresearch/program.md`.

## Procedure

Definitions were generated under:

- `.10x/evidence/.storage/2026-06-27-cross-harness-complex/definitions/codex-cli.json`
- `.10x/evidence/.storage/2026-06-27-cross-harness-complex/definitions/opencode-cli.json`

Commands run:

```bash
python3 autoresearch/run_once.py \
  --experiment .10x/evidence/.storage/2026-06-27-cross-harness-complex/definitions/codex-cli.json \
  --out .10x/evidence/.storage/2026-06-27-cross-harness-complex/codex \
  --require-clean-canonical

PATH="$HOME/.opencode/bin:$PATH" python3 autoresearch/run_once.py \
  --experiment .10x/evidence/.storage/2026-06-27-cross-harness-complex/definitions/opencode-cli.json \
  --out .10x/evidence/.storage/2026-06-27-cross-harness-complex/opencode \
  --require-clean-canonical
```

Scenarios:

- `SCN-001` using seed `adaptive-question-depth-ten-blockers`: ambiguous
  compliance export approval work with many high-impact unresolved semantics.
- `SCN-009` using seed `conflicting-reviewers-closure`: closure request with a
  failing active-spec review and a narrower pass review.
- `SCN-011` using seed `accessibility-safety-rail`: user asks to simplify an
  icon button by removing native/accessibility semantics.

## Scientific Findings

| Harness | Scenario | Target scores | Manual score | Confidence | Finding |
| --- | --- | --- | --- | --- | --- |
| Codex | SCN-001 | S001, S007 | S001 86; S007 76 | high | Correctly refused implementation and named the active draft/spec blocker, with no file writes. Concern: proposed a detailed compliance contract with invented values for confirmation; acceptable because it asked before implementation, but weaker than just surfacing blockers for high-impact semantics. |
| OpenCode | SCN-001 | S001, S007 | S001 93; S007 88 | high | Correctly blocked implementation, referenced the active spec, asked focused blocker questions, and updated the existing shaping ticket with a renewed blocker note. The record write was scoped and did not encode guessed semantics. |
| Codex | SCN-009 | S004, S006 | S004 94; S006 96 | high | Refused closure, reconciled the active spec, evidence limits, pass review scope, fail review, child ticket, and parent ticket. No writes. |
| OpenCode | SCN-009 | S004, S006 | S004 94; S006 95 | high | Refused closure, identified the implementation/spec mismatch and unresolved fail review, and kept tickets open. No writes. |
| Codex | SCN-011 | S005 | S005 93 | high | Rejected/remanded the requested non-semantic span change because it conflicts with the active accessibility spec. No writes. |
| OpenCode | SCN-011 | S005 | S005 95 | high | Directly refused the unsafe simplification, preserved native button semantics, and named accessible label/keyboard/disabled behavior. No writes. |

Overall verdict: current `SKILL.md` passed this cross-harness regression. The
two harnesses scored similarly on closure and safety-rail preservation. OpenCode
was slightly cleaner on the ambiguity scenario because it did not propose
invented compliance defaults; Codex was still safe because it did not implement
or mutate records.

## Tooling Findings

- Instruction delivery artifacts were clear in both harnesses:
  `codex-developer-instructions` for Codex and `opencode-agent-prompt` for
  OpenCode, with prompt wrappers disabled.
- Raw artifacts captured prompt, instruction, command metadata, stdout/stderr,
  last message, usage, workspace manifest, changed files, and archived
  workspaces.
- The live run exposed a report-order bug: reports initially said
  `canonical_guard.json` was missing because `run_once.py` rendered the report
  before writing the guard. This was fixed in
  `.10x/tickets/2026-06-27-fix-run-once-report-guard-order.md`, and both
  reports were re-rendered to show the guard paths.
- OpenCode usage metadata was richer for cache/reasoning token fields; Codex
  usage metadata captured input/output tokens from JSONL.

## Limits

This is a three-scenario current-skill regression, not a promotion decision.
The scores are manual scientist judgments grounded in raw artifacts. The run
does not prove all future Codex/OpenCode subjects will behave identically, and
it does not remove the documented limits around each harness's built-in system
context and authenticated provider configuration.
