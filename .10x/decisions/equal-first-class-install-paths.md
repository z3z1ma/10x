Status: active
Created: 2026-06-28
Updated: 2026-06-28

# Equal First-Class Install Paths

## Context

The public README needs to make 10x easy to try while preserving the product
philosophy that the actual surface is Markdown instructions. The Vercel Skills
CLI is useful because it automates placement across many agent harnesses.
Direct copy-paste is equally important because it is more flexible, transparent,
and faithful to the fact that 10x is English text, not a runtime or cloud
marketplace dependency.

The user explicitly corrected earlier README wording that made copy-paste sound
secondary. The intended positioning is that `npx skills add z3z1ma/10x` and
copying the body of `SKILL.md` into an agent instruction file are equal
first-class paths.

## Decision

Present Skills CLI and copy-paste as equal first-class install paths.

The Skills CLI path is for automatic placement across supported harnesses. The
copy-paste path is for maximum control: inspect, fork, splice, adapt, or append
the Markdown wherever an agent reads instructions.

Manual skill-directory cloning remains a variant for harnesses that load skills
from directories, not a third conceptual product surface.

## Authority And Provenance

- User ratified the equal-path positioning in chat on 2026-06-28 after rejecting
  README wording that implied copy-paste was secondary.
- The current README install section is the active public expression of this
  decision.
- The Vercel Skills CLI upstream README supports the broad-harness installer
  claim.
- `SKILL.md` is the canonical instruction artifact; no root package manifest or
  runtime entrypoint defines 10x as software that must be executed.

## Alternatives Considered

- Skills CLI as the recommended path, copy-paste as fallback. Rejected because
  it misrepresents the product surface and undersells the intentional simplicity
  of Markdown instructions.
- Copy-paste as the only emphasized path. Rejected because the Skills CLI is a
  real convenience layer and supports broad harness placement.
- First-class cloud or marketplace integration. Rejected because it would add
  ceremony and imply a runtime/platform dependency where none is needed.

## Consequences

- README copy must state that both install paths are first-class.
- Claims about 70+ agent support must be attributed to the Vercel Skills CLI,
  not to 10x as a runtime.
- Instruction-file installs must tell users to omit YAML frontmatter.
- Skill-directory installs must tell users to keep `SKILL.md` intact.
- Future packaging work should preserve the ability to copy the plain Markdown
  body without installer machinery.

## Evidence And Limits

- The Vercel Skills CLI README says it supports OpenCode, Claude Code, Codex,
  Cursor, and 68 more.
- This repository has no runtime package manifest at the root; the primary
  product artifact is `SKILL.md`.
- `npm` is not installed in the current container, so `npx skills add` was not
  executed locally during README validation.
