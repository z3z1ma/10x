---
id: evidence:using-loom-rename-validation
kind: evidence
status: recorded
created_at: 2026-05-07T19:32:42Z
updated_at: 2026-05-07T19:35:57Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:usng507a
  spec:
    - spec:opencode-plugin-install-contract
external_refs: {}
---

# Summary

Validation evidence for the `using-loom` entry-skill rename, associated doctrine
and owner-record reconciliation, and OpenCode package surface checks.

# Procedure

Observed at: 2026-05-07T19:32:42Z

Source state: dirty working tree on `repo:root`; unrelated untracked
`examples/00-todo-app` files were intentionally excluded from rename checks.

Procedure:

- Ran stale-name scans for current product surfaces and current owner records.
- Ran `git diff --check` for whitespace errors.
- Ran skill frontmatter validation with a Node one-liner.
- Ran `npm run pack:check` to exercise `node open-loom.mjs --smoke` and
  `npm pack --dry-run`.
- Checked that `skills/loom-bootstrap/**` no longer exists and that
  `skills/using-loom/references/*.md` contains the ordered references.
- Checked that no repository file path remains under `**/loom-bootstrap/**` after
  internal fixture reconciliation.
- Checked the exact old drive objective-state vocabulary was absent.

Expected result when applicable: no stale current entry-skill paths or old
bootstrap-reference wording in product/current owner surfaces; eight ordered
using-Loom references in the OpenCode smoke output; 22 skill frontmatter entries
with names matching directories; no whitespace errors; package dry-run includes
`skills/using-loom`.

Actual observed result: expected results were observed.

Procedure verdict / exit code: pass; all listed commands exited 0.

# Artifacts

Commands and key observations:

```bash
rg -n "loom-bootstrap|skills/loom-bootstrap|bootstrap doctrine|bootstrap skill|bootstrap references|ordered bootstrap|bootstrap-first|bootstrapReference|readOrderedBootstrap|bootstrapResult" --glob '!/.loom/**' --glob '!examples/00-todo-app/**' --glob '!node_modules/**' .
```

Output: no matches.

```bash
rg -n 'loom-bootstrap|skills/loom-bootstrap|bootstrap doctrine|bootstrap skill|bootstrap references|ordered bootstrap|bootstrap-first|bootstrapReference|readOrderedBootstrap|bootstrapResult|seven ordered using-Loom|all seven bootstrap|all seven LOOM_RULE_FILE' .loom/constitution .loom/wiki .loom/initiatives .loom/plans .loom/research .loom/specs
```

Output: no matches.

```bash
git diff --check
```

Output: no whitespace errors.

Skill frontmatter validation output:

```json
{
  "skillCount": 22,
  "hasUsingLoom": true,
  "usingLoomKind": "entry-doctrine"
}
```

`npm run pack:check` key output:

```json
{
  "ok": true,
  "pluginId": "open-loom",
  "usingLoomReferenceCount": 8,
  "firstUsingLoomReference": "skills/using-loom/references/01-core-identity.md",
  "lastUsingLoomReference": "skills/using-loom/references/08-trust-boundaries.md",
  "instructionCount": 8,
  "instructionsAreDeduped": true,
  "skillCount": 22,
  "usingLoomResult": "registered through config.instructions as ordered using-Loom references",
  "skillsResult": "registered through config.skills.paths"
}
```

`npm pack --dry-run` reported package `open-loom@0.1.9`, `total files: 130`, and
included `skills/using-loom/SKILL.md` plus all eight
`skills/using-loom/references/*.md` files. No `open-loom-0.1.9.tgz` artifact was
created in the workspace after the dry run.

File existence checks:

- `skills/loom-bootstrap/**`: no files found.
- `skills/using-loom/references/*.md`: eight files found.
- `**/loom-bootstrap/**`: no files found after final fixture cleanup.

Drive vocabulary check:

```bash
rg -n 'objective criteria: <OBJ-IDs and satisfied \| partial \| open \| blocked>|state: open \| partial \|' skills/loom-drive
```

Output: no matches.

# Raw Artifact Store

- Path: None - command excerpts above are small enough to keep in this record.
- Captured artifacts: None beyond summarized command output.
- Key excerpts / index: See `# Artifacts`.
- Redaction / sensitivity: No secrets or sensitive data observed in captured excerpts.
- Retention / tracking: Record is tracked Markdown evidence.

# Visual / Product Evidence

N/A - this was a protocol/docs/package-surface validation pass, not UI or visual
product work.

# Supports Claims

- ticket:usng507a#ACC-001 — product and current owner surfaces no longer point at
  the deleted entry skill, and OpenCode smoke registers ordered using-Loom paths.
- ticket:usng507a#ACC-002 — plan drift checks found no current product wording
  that reduces plans to sequencing/rollout only.
- ticket:usng507a#ACC-003 — using-Loom doctrine and public surfaces were included
  in product-surface scans after the structured paper/work-product graph framing
  edits.
- ticket:usng507a#ACC-004 — drive vocabulary and package/count follow-up checks
  support the prior audit-finding fixes, with critique still owning final review.
- ticket:usng507a#ACC-005 — structural validation and package checks were run and
  recorded.

# Challenges Claims

None.

# Environment

Commit: dirty working tree; no commit created for this ticket.

Branch: current workspace branch.

Runtime: Node.js and npm from the local development environment; OpenCode package
dry-run through `npm run pack:check`.

OS: macOS / Darwin.

Relevant config: package `open-loom@0.1.9`; OpenCode engine range
`>=1.14.22 <2` in `package.json`.

External service / harness / data source when applicable: npm local dry-run only;
no network marketplace or harness runtime install validation was performed.

# Validity

Valid for: the dirty working tree observed at 2026-05-07T19:32:42Z and the listed
ticket acceptance checks.

Fresh enough for: ticket acceptance review of structural rename, current owner
record reconciliation, OpenCode package dry-run contents, and drive vocabulary
cleanup.

Recheck when: product docs, `skills/`, `open-loom.mjs`, adapter metadata,
current owner records, or package contents change before acceptance or release.

Invalidated by: new stale references, missing `skills/using-loom` files, package
contents changing, or adapter behavior changes not covered by this dry run.

Supersedes / superseded by: None.

# Limitations

- This evidence does not prove Claude, Codex, Gemini, Cursor, or OpenCode runtime
  install behavior outside the local `open-loom` smoke/package dry run.
- Historical closed `.loom` tickets, evidence, critique, and packets still contain
  old entry-skill names as historical observations; this evidence only validates
  product surfaces and current owner records named in the command scopes.
- The evidence does not itself decide acceptance or critique sufficiency.

# Result

The observed structural checks support the entry-skill rename, current owner
record reconciliation, package surface update, and drive vocabulary cleanup.

# Interpretation

The validation supports accepting the implementation shape if critique finds no
remaining blocking issues and the ticket ledger is reconciled. It does not justify
claims about remote plugin marketplaces or harness runtime installs.

# Related Records

- ticket:usng507a
- spec:opencode-plugin-install-contract
