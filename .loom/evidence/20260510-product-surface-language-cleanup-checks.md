# Product Surface Language Cleanup Checks

Status: recorded
Created: 2026-05-10
Updated: 2026-05-11
Observed: 2026-05-10 to 2026-05-11

## Observations

Observed checks after product-surface language cleanup and the follow-up public-doc wording fixes.

Command checks from `/Users/alexanderbutler/code_projects/personal/agent-loom` on 2026-05-11:

- `npm --prefix loom-core run smoke` - passed with `ok: true`, `usingLoomFileCount: 7`, `instructionCount: 7`, and `skillCount: 11`.
- `npm --prefix loom-playbooks run smoke` - passed with `ok: true`, `doesNotPreloadCoreDoctrine: true`, and `skillCount: 25`.
- `npm --prefix loom-core run pack:check` - passed; dry-run pack completed with 65 files.
- `npm --prefix loom-playbooks run pack:check` - passed; dry-run pack completed with 28 files.
- `git diff --check` - passed with no output.

Search checks:

- Grep over `loom-core/skills` for package-boundary terms such as `Core Dependency`, `Use loom-core first`, `Core routing`, `Core loop`, `through Core`, and `bypassing Core` returned no files.
- Grep over `loom-playbooks/skills` for the same package-boundary terms returned no files.
- Grep over `loom-core/skills` for eval-shaped terms such as `stack foundation`, `summary API`, `map shell`, `deep analytics`, `Campaign Map`, `OpenDota`, `MVP`, and `production feel` returned no files.
- Grep over `loom-playbooks/skills` for the same eval-shaped terms returned no files.
- `rg` over public docs (`README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `INSTALL.md`, `loom-core/README.md`, and `loom-playbooks/README.md`) for package-boundary operational wording such as `Core records`, `results still land in Core`, `truth still lives in Core`, `route through Core`, `routes over Core`, and `over Core` returned no output.
- `rg` over the same public docs plus shipped skill directories for the eval-shaped terms returned no output.

## What This Shows

- Supports `.loom/tickets/done/20260510-product-surface-language-cleanup.md#ACC-001`: shipped skill bodies no longer contain the searched package-boundary guidance terms.
- Supports `.loom/tickets/done/20260510-product-surface-language-cleanup.md#ACC-002`: shipped skill bodies no longer contain the searched eval-shaped terms.
- Supports `.loom/tickets/done/20260510-product-surface-language-cleanup.md#ACC-003`: package and Markdown checks passed after cleanup.
- Supports the ticket's single closure claim for the searched public-doc wording terms after the two review findings were patched.

## What This Does Not Show

- It does not prove every possible synonym for package-boundary leakage is absent.
- It does not prove live agent behavior improves.
- It does not treat internal dogfood `.loom/`, `evals/`, or maintainer docs as shipped skill bodies.
- It does not replace fresh-context review of the final patched wording.

## Related Records

- `.loom/tickets/done/20260510-product-surface-language-cleanup.md` - ticket supported by this evidence.
