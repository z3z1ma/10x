Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Target: autoresearch/run_subject.py, autoresearch/report.py, autoresearch/README.md, .10x/specs/10x-autoresearch-loop.md
Verdict: pass

# Autoresearch Instruction Delivery Review

## Target

Review of the instruction-delivery hardening for the live subject runner.

## Findings

No blocking findings.

Minor residual risk:

- OpenCode `--pure` is documented as plugin isolation, not total config or
  built-in-system-prompt isolation. The code and docs now state that limit
  explicitly, and empty `instruction_text` means only no runner-supplied
  instruction layer.
- Codex `developer_instructions` is the closest documented append-like channel
  available to the CLI. The runner intentionally avoids `model_instructions_file`
  because that would replace built-in base instructions and could damage the
  subject harness itself.
- OpenCode uses `OPENCODE_CONFIG` and a saved config artifact only when arm
  instructions are non-empty. A truly empty OpenCode control still relies on
  OpenCode's shipped defaults and authenticated/global environment remaining
  outside runner control; command metadata and docs preserve that boundary.

## Assumptions Tested

- One path remains: all harnesses still flow through `build_plan`,
  `_planned_turns`, `_planned_argv`, `_run_sample`, one `planned_argv`, one
  `live_subject_calls`, and one `harness_artifact_dir` schema.
- Prompt wrapper removal does not erase inspectability because each run writes
  a `.instructions.txt` artifact and records `instruction_delivery` metadata.
- Public argv redaction replaces Codex `developer_instructions=...` with an
  instruction artifact reference, while raw instruction text remains available
  in the instruction artifact.
- OpenCode config is not placed inside the subject workspace, avoiding workspace
  output pollution.
- Empty instructions do not add `developer_instructions`, `--agent`, or
  `OPENCODE_CONFIG`.

## Verdict

Pass. The implementation improves correctness and ergonomics without adding a
second public path. The remaining limits are inherent harness limits and are now
plainly documented.

## Residual Risk

Live model behavior still needs comparative trials. The review only covers
tooling semantics, artifact capture, and static/unit verification.
