Status: done
Created: 2026-06-25
Updated: 2026-06-25
Parent: .10x/research/2026-06-23-skill-autoresearch-run.md
Depends-On: .10x/evidence/2026-06-24-skill-authoring-agents-mirror-confounder.md

# Allow Codex Subject Writable Add Dirs

## Scope

Add a narrow live-runner mechanism for experiments that need Codex subject
agents to write to additional harness-native directories inside the subject
workspace, such as `.agents/skills`.

Included:

- Add a `writable_add_dirs` experiment definition field containing relative
  workspace paths.
- Pass those paths to Codex as `--add-dir <workspace>/<relative-path>` in both
  planned and live command argv.
- Reject absolute paths, parent traversal, empty entries, root workspace
  entries, and non-list values.
- Record the configured add dirs in workspace manifests and raw harness
  metadata.
- Add regression coverage for plan generation, unsafe definitions, and actual
  live subprocess argv.

Excluded:

- Broadening the sandbox to `danger-full-access`.
- Changing control-arm `.10x` isolation.
- Changing `SKILL.md`.
- Re-running the `.agents/skills` skill-authoring experiment.

## Acceptance Criteria

- AC-001: A definition with `writable_add_dirs: [".agents/skills"]` produces
  planned Codex argv containing `--add-dir <workspace>/.agents/skills`.
- AC-002: Live execution uses the same add-dir option when spawning Codex.
- AC-003: Unsafe values outside the subject workspace are rejected before a run
  starts.
- AC-004: The runner records the configured add dirs in archived manifests and
  raw harness metadata.
- AC-005: `python3 -m unittest autoresearch.tests.test_run_codex_subject`,
  `python3 -m unittest discover autoresearch/tests`,
  `python3 autoresearch/validate.py`, and `git diff --check` pass.

## Progress and Notes

- 2026-06-25: Reproduced the prior `.agents/skills` confounder with a minimal
  Codex probe: under `workspace-write`, a subject could read
  `.agents/skills/skill-writing-governor/SKILL.md` but could not create
  `.agents/skills/probe-skill/SKILL.md`.
- 2026-06-25: Re-ran the probe with `--add-dir <workspace>/.agents/skills`;
  the write succeeded without requiring broad filesystem access.
- 2026-06-25: Added `writable_add_dirs` parsing and validation to
  `autoresearch/run_codex_subject.py`.
- 2026-06-25: Updated both planned and live Codex argv construction to include
  configured add dirs before the prompt argument.
- 2026-06-25: Added tests proving the plan, live subprocess argv, manifest
  metadata, and unsafe-path rejection behavior.
- 2026-06-25: Verified the focused test file, full autoresearch unit suite,
  contract validator, and diff whitespace check.

## Blockers

None.
