Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Relates-To: .10x/tickets/2026-06-27-add-opencode-autoresearch-harness.md, .10x/specs/10x-autoresearch-loop.md, .10x/research/2026-06-27-opencode-cli-harness-research.md

# OpenCode Autoresearch Harness Evidence

## What Was Observed

OpenCode support was added to the live autoresearch subject runner and verified
with unit tests, validation, CLI help inspection, and a live OpenCode smoke
trial using `openai/gpt-5.5`.

## Procedure

Documentation and local CLI checks:

```bash
$HOME/.opencode/bin/opencode --version
$HOME/.opencode/bin/opencode run --help
$HOME/.opencode/bin/opencode auth list
```

Observed:

- OpenCode version: `1.17.11`.
- `opencode run` supports `--model provider/model`, `--format json`, `--dir`,
  and `--dangerously-skip-permissions`.
- `opencode auth list` reported one OpenAI OAuth credential.
- The local shell did not have `opencode` on `PATH`; empirical runs used
  `PATH="$HOME/.opencode/bin:$PATH"`.

Focused tests:

```bash
python3 -m unittest autoresearch.tests.test_run_subject autoresearch.tests.test_run_once autoresearch.tests.test_report
```

Observed result:

- `Ran 36 tests in 9.137s`
- `OK`

Full verification:

```bash
python3 -m unittest discover autoresearch/tests
python3 autoresearch/validate.py
python3 -m py_compile autoresearch/*.py
```

Observed result:

- `Ran 53 tests in 17.154s`
- `OK`
- `autoresearch contracts valid`
- `py_compile` exited zero.

Dry-run:

```bash
PATH="$HOME/.opencode/bin:$PATH" python3 autoresearch/run_subject.py \
  --experiment .10x/evidence/.storage/2026-06-27-opencode-smoke/experiment.json \
  --dry-run \
  --out .10x/evidence/.storage/2026-06-27-opencode-smoke/EXP-20260627-904-opencode-smoke
```

Observed:

- `harness: opencode-cli`
- `harness_kind: opencode-live-subject`
- `artifact_dirs.opencode` present and `artifact_dirs.codex` absent.
- Planned argv redacted prompt and included `opencode run --model
  openai/gpt-5.5 --format json --dir <workspace>
  --dangerously-skip-permissions`.

Live smoke:

```bash
PATH="$HOME/.opencode/bin:$PATH" python3 autoresearch/run_once.py \
  --experiment .10x/evidence/.storage/2026-06-27-opencode-smoke/experiment.json \
  --out .10x/evidence/.storage/2026-06-27-opencode-smoke/EXP-20260627-904-opencode-smoke
```

Observed final run:

- `run_once.py` exited zero.
- `summary.json` recorded `harness: opencode-cli`,
  `harness_kind: opencode-live-subject`, `samples_written: 1`,
  `live_subject_calls: 1`, and `live_codex_calls: 0`.
- `opencode/*.command.json`, `opencode/*.stdout.jsonl`,
  `opencode/*.stderr`, and `opencode/*.last-message.txt` exist.
- Command exit code was `0`.
- Raw artifact usage included `input_tokens: 16052`, `output_tokens: 106`,
  `reasoning_tokens: 59`, `cache_read_tokens: 30720`,
  `cache_write_tokens: 0`, `total_tokens: 46937`.
- Raw artifact `file_outputs` and workspace manifest `changed_files` both list
  `proof.txt`.
- Archived `proof.txt` contained exactly:
  `opencode autoresearch smoke passed`.
- `report.md` included OpenCode artifact checklist rows for command metadata,
  stdout JSONL, stderr, and last assistant messages.
- `canonical_guard.json` recorded `unchanged_during_run: true`.

The final smoke artifacts are under:

`.10x/evidence/.storage/2026-06-27-opencode-smoke/EXP-20260627-904-opencode-smoke/`

## What This Supports Or Challenges

Supports:

- `run_once.py` can execute OpenCode live subject trials through the same
  scientific loop as Codex.
- OpenCode has artifact parity for the current method: registered plan,
  summary, raw trial, command metadata, JSON stdout, stderr, last assistant
  message, prompts, archived workspace, workspace manifest, report, and
  canonical guard.
- `openai/gpt-5.5` is empirically usable through local OpenCode credentials on
  2026-06-27.
- The runner now starts from a clean workspace on repeated runs to the same
  output directory unless a prior raw artifact or seed workspace is explicitly
  provided.

Challenges / findings handled:

- During empirical rerun, the runner originally reused an existing archived
  workspace when the output directory already existed. That contaminated rerun
  baselines and hid `proof.txt` from `changed_files`. The runner now ignores
  previous output workspaces unless the experiment explicitly supplies prior
  context, and a regression test covers this.
- OpenCode token usage is nested under `part.tokens`, so usage parsing now
  normalizes both Codex-style `usage` and OpenCode-style token events.

## Limits

- OpenCode emitted a stderr warning:
  `[oh-my-opencode-slim] Preset "openai" not found (from config file). Available presets: none`.
  The command still exited zero and used the requested model.
- The runner does not control OpenCode authenticated home state, provider
  configuration, plugins, or system context.
- The raw `.storage` artifacts are intentionally ignored by git; this evidence
  record preserves the claim-supporting paths and observations.
