Status: recorded
Created: 2026-05-11
Updated: 2026-05-11
Observed: 2026-05-11

# Playbook Corpus Release Review

## Observation

The `loom-playbooks` skill corpus was reviewed in three passes before release:

- pass 1: three independent read-only review lenses over corpus consistency,
  skill clarity, and package-facing metadata
- pass 2: targeted grep checks after the initial patch for stale routing labels,
  stale `using-Loom` capitalization, stale Ralph outcome vocabulary, and safety
  wording regressions
- pass 3: fresh-context read-only review of the patched corpus, followed by a
  targeted fix and re-check for the two returned findings

Verification results observed after the fixes:

- `npm --prefix loom-playbooks run pack:check` passed; smoke reported `ok: true`,
  `doesNotPreloadCoreDoctrine: true`, and `skillCount: 25`; dry-run pack reported
  28 files.
- `npm --prefix loom-core run pack:check` passed; smoke reported `ok: true`,
  `usingLoomFileCount: 7`, and `skillCount: 11`; dry-run pack reported 65 files.
- `git diff --check` passed with no output.
- `claude plugin validate "$PWD/loom-playbooks"` passed.
- `gemini extensions validate "$PWD"`, `gemini extensions validate
  "$PWD/loom-core"`, and `gemini extensions validate "$PWD/loom-playbooks"`
  passed.
- Grep checks found no remaining `## Loom Surfaces`, `Route durable results
  through`, `done_with_concerns`, `needs_context`, `Useful states`, stale
  `using-Loom`, or old secret-check wording under `loom-playbooks`.
- Grep checks found 25 `## Loom Routing` sections, 25 `using-loom` loading
  reminders, and 25 `Common routes use these Loom skills` declarations under
  `loom-playbooks/skills`.

## What This Shows

This supports the claim that the playbook corpus edits landed consistently across
all 25 playbook skills, that package-facing playbook validators still accept the
changed metadata, and that the Core and Playbooks package smoke/pack checks passed
after the corpus review fixes.

## What This Does Not Show

This does not prove every possible harness runtime behavior after installation,
nor does it prove the prose is semantically perfect. It records the review passes,
targeted re-checks, package checks, adapter validators, and grep invariants that
were observed for this release-prep change.
