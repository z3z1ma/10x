# Ralph Language Consolidation Checks

ID: evidence:20260513-ralph-language-consolidation-checks
Type: Evidence Dossier
Status: recorded
Created: 2026-05-13
Updated: 2026-05-13
Observed: 2026-05-13

## Summary

Validation for `ticket:20260513-ralph-language-consolidation`: targeted skill-corpus and doc scans, package smoke/pack checks, Markdown whitespace checks, and source-diff inspection after consolidating audit and worker language around Ralph.

## Observations

- Observation: targeted term scan of `loom-core/skills` found no stale context-shape terminology matches.
  - Procedure/source: `grep` tool over `/loom-core/skills`, include `*.md`, pattern `fresh-context|fresh context|Fresh-Context|separate-context|separate context|fresh or separate|fresh worker|fresh reviewer|fresh agent|fresh pass|same-context`.
  - Actual result: no files found.
- Observation: targeted term scan of `loom-playbooks/skills` found no stale context-shape terminology matches.
  - Procedure/source: `grep` tool over `/loom-playbooks/skills`, include `*.md`, pattern `fresh-context|fresh context|Fresh-Context|separate-context|separate context|fresh or separate|fresh worker|fresh reviewer|fresh agent|fresh pass|same-context`.
  - Actual result: no files found.
- Observation: targeted term scans of current human-facing docs found no stale context-shape terminology in `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, or package README files.
  - Procedure/source: `grep` tool over repository Markdown docs, include-specific scans for `README.md`, `PROTOCOL.md`, and `ARCHITECTURE.md`, pattern `fresh-context|fresh context|Fresh-Context|separate-context|separate context|fresh or separate|fresh worker|fresh reviewer|fresh agent|fresh pass|same-context`.
  - Actual result: no files found for the scanned non-historical docs.
- Observation: Core smoke check passed.
  - Procedure/source: `npm --prefix loom-core run smoke` from repository root.
  - Actual result: JSON output reported `"ok": true`, `usingLoomFileCount: 7`, `instructionCount: 7`, `skillCount: 11`, and deduped instructions.
- Observation: Playbooks smoke check passed.
  - Procedure/source: `npm --prefix loom-playbooks run smoke` from repository root.
  - Actual result: JSON output reported `"ok": true`, `doesNotPreloadCoreDoctrine: true`, `skillCount: 25`, and deduped skill paths.
- Observation: Core package check passed.
  - Procedure/source: `npm --prefix loom-core run pack:check` from repository root.
  - Actual result: smoke passed and `npm pack --dry-run` reported tarball contents for `@z3z1ma/open-loom-core@0.2.1`.
- Observation: Playbooks package check passed.
  - Procedure/source: `npm --prefix loom-playbooks run pack:check` from repository root.
  - Actual result: smoke passed and `npm pack --dry-run` reported tarball contents for `@z3z1ma/open-loom-playbooks@0.2.1`.
- Observation: Markdown diff whitespace check passed.
  - Procedure/source: `git diff --check` from repository root.
  - Actual result: no output.
- Observation: source-diff inspection showed the changed audit and worker guidance now routes substantive review through Ralph review packets and records the returned adversarial judgment in audit.
  - Procedure/source: `git diff -- loom-core/skills loom-playbooks/skills .loom/tickets/20260513-ralph-language-consolidation.md` and manual inspection of the relevant diff sections.
  - Actual result: `loom-audit` now uses `Ralph Review Requirement`, `loom-ralph` describes audit use as adversarial review, Core routing references point audit review to Ralph-backed review, and playbooks that mention delegated review or audit point through Ralph/audit without context-shape terminology.

## Artifacts

- Tool output from `npm --prefix loom-core run smoke` - Core smoke passed with `ok: true`.
- Tool output from `npm --prefix loom-playbooks run smoke` - Playbooks smoke passed with `ok: true`.
- Tool output from `npm --prefix loom-core run pack:check` - Core smoke and dry-run pack passed.
- Tool output from `npm --prefix loom-playbooks run pack:check` - Playbooks smoke and dry-run pack passed.
- Tool output from `git diff --check` - no output.

## What This Shows

- `ticket:20260513-ralph-language-consolidation#ACC-001` - supports - targeted scans found none of the stale context-shape terms in shipped Core or Playbooks skill Markdown after the edit.
- `ticket:20260513-ralph-language-consolidation#ACC-002` - supports - source-diff inspection found `loom-audit` now describes substantive audit as a Ralph review packet whose returned adversarial judgment is recorded in audit.
- `ticket:20260513-ralph-language-consolidation#ACC-003` - supports - source-diff inspection found affected playbooks route delegated review/audit through Ralph and audit without centering context-shape terminology.
- `ticket:20260513-ralph-language-consolidation#ACC-004` - supports - targeted scans found no stale context-shape terminology in the non-historical docs that restate Core worker or audit semantics.

## What This Does Not Show

This evidence does not prove historical `.loom` records or eval records avoid the stale terms. It does not replace a semantic audit of every possible wording implication, though the ticket acceptance explicitly waives separate audit for this terminology-only slice when grep evidence and diff inspection show no behavior expansion beyond Ralph-centered wording.

## Related Records

- `ticket:20260513-ralph-language-consolidation` - consuming ticket.
