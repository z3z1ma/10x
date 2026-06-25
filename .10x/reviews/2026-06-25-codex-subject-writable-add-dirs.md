Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/tickets/done/2026-06-25-allow-codex-subject-writable-add-dirs.md
Verdict: pass

# Codex Subject Writable Add Dirs Review

## Target

Runner change for
`.10x/tickets/done/2026-06-25-allow-codex-subject-writable-add-dirs.md`.

## Findings

- Pass: The implementation preserves `workspace-write` sandboxing and adds only
  explicit `--add-dir` entries derived from definition-owned relative paths.
- Pass: Unsafe paths are rejected before planning or execution, including
  absolute paths, parent traversal, empty entries, root workspace entries, and
  non-list values.
- Pass: The live runner no longer diverges from the dry-run plan; the actual
  subprocess argv test checks the add-dir path relative to the temporary
  execution workspace.
- Minor: The mechanism is definition-level, not per-scenario. This is
  acceptable for the current `.agents/skills` harness need; split per-scenario
  only if a future experiment needs mixed write boundaries in one definition.

## Verdict

Pass. The change is scoped to the known `.agents/skills` harness confounder and
does not weaken control isolation or grant broad filesystem access.

## Residual Risk

Codex may still load `.agents/skills` entries as skills during subject runs.
That is an intended part of testing harness-native skill behavior, but future
experiment records must state the limitation when interpreting results.
