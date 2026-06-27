Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Target: .10x/tickets/2026-06-27-add-opencode-autoresearch-harness.md
Verdict: pass

# OpenCode Autoresearch Harness Review

## Target

Implementation adding OpenCode as a live autoresearch subject harness, including
runner changes, report changes, tests, docs, research, and smoke evidence.

## Assumptions Tested

- A future scientist should still have one primary loop command:
  `autoresearch/run_once.py`.
- Harness support should be a small command/event/artifact boundary, not a new
  controller or alternate method.
- Codex runs should remain backward-compatible for existing artifacts and tests.
- OpenCode should be empirically verified against the current CLI, not inferred
  from memory.
- Re-running an experiment to the same output directory should not silently use
  stale archived workspace state.

## Findings

No blocking findings.

Minor risk: OpenCode uses `--dangerously-skip-permissions`.

- Assessment: acceptable for this harness because each run happens in a private
  temporary workspace and the limitation is written into control isolation,
  docs, knowledge, research, and evidence.
- Residual risk: OpenCode authenticated home state and provider configuration
  remain outside complete runner control, like Codex authenticated home state.

Minor risk: the lower-level runner was renamed from `run_codex_subject.py` to
`run_subject.py`.

- Assessment: correct cleanup. Active code, tests, README, and template now use
  the neutral name. Legacy markdown markers still load existing experiment
  records.
- Residual risk: an old direct command using `run_codex_subject.py` would fail,
  but `run_once.py` is the canonical command and active docs no longer point to
  the old file.

Minor risk: OpenCode JSON event schema may evolve.

- Assessment: acceptable. The runner preserves raw stdout JSONL verbatim and
  uses tolerant extraction for assistant text and normalized usage. If parsing
  misses a future field, the raw artifact still contains the source event.

Positive finding: empirical testing found and fixed a pre-existing rerun
contamination issue.

- Repeated runs to the same output root previously copied the archived workspace
  as a starting state when no prior raw artifact existed.
- This violated clean-room expectations and could hide changed files.
- The branch was removed and a regression test now proves repeated no-prior
  runs start clean.

## Verdict

Pass.

The implementation preserves the scientist-led autoresearch method, keeps
`run_once.py` as the one-shot loop command, gives OpenCode artifact parity, keeps
Codex compatibility, records current OpenCode CLI evidence, and includes a live
OpenCode smoke trial with `openai/gpt-5.5`.

## Residual Risk

- OpenCode itself must be installed on `PATH` for future unprefixed runs.
- OpenCode provider/model access can change after 2026-06-27.
- The subject CLI's authenticated home state is not hermetic; scientists must
  inspect command artifacts and workspace manifests before recording verdicts.
