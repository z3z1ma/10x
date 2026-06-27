Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Target: .10x/tickets/2026-06-27-simplify-autoresearch-subject-runner.md
Verdict: pass

# Subject Runner Schema Simplification Review

## Target

Cleanup of the live subject runner after OpenCode support: remove duplicate
Codex/OpenCode schema paths, keep one command-building path, and preserve rich
raw data for the scientist.

## Assumptions Tested

- New outputs should not expose both generic and harness-specific field names.
- Compatibility for old artifacts should be read-only and localized.
- Rich data should be comparable across Codex and OpenCode.
- Simplicity should not remove useful raw evidence.

## Findings

No blocking findings.

Minor residual risk: compatibility helpers still contain old field names.

- Assessment: acceptable. They are isolated in report fallback helpers and tests
  that prove old artifacts normalize to the current schema. The runner no
  longer emits those fields.

Minor residual risk: physical artifact directories still use harness names such
as `codex/` and `opencode/`.

- Assessment: acceptable. This is useful filesystem organization, not duplicate
  schema. The in-memory plan has one `artifact_dirs.harness` key and summary has
  one `harness_artifact_dir` field.

Positive finding: raw data richness is preserved and clearer.

- Command metadata records harness, kind, redacted argv, exit code, stdout JSONL
  path, stderr path, last-message path, prompt path, working directory, usage,
  timeout, and isolation metadata.
- Raw artifacts record transcript, tool invocations, changed files, command
  outputs, raw artifact refs, aggregate usage, token aliases, timeout, harness
  metadata, workspace manifest, and archived workspace references.
- OpenCode `part.tokens` and Codex `usage` normalize through the same usage
  path.

## Verdict

Pass.

The live subject runner now has one active path and one active new-run schema.
Legacy names remain only where needed to read older reports/artifacts.

## Residual Risk

Historical records may still mention old field names as facts about older runs.
That is history, not active runner behavior.
