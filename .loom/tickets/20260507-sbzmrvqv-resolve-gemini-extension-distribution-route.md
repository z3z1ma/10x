---
id: ticket:sbzmrvqv
kind: ticket
status: closed
change_class: release-packaging
risk_class: medium
created_at: 2026-05-07T23:04:32Z
updated_at: 2026-05-07T23:25:03Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:loom-install-experience
  plan:
    - plan:split-core-and-playbooks-packages
  spec:
    - spec:core-and-playbooks-package-contract
  research:
    - research:gemini-extension-subdirectory-feasibility
    - research:core-workflow-plugin-split-feasibility
  decision:
    - decision:0008
  ticket:
    - ticket:7h8u6oxp
    - ticket:mbkqbkgq
  evidence:
    - evidence:gemini-extension-local-link-route-check
    - evidence:gemini-root-core-shim-check
  critique:
    - critique:gemini-extension-route-review
external_refs: {}
depends_on:
  - ticket:7h8u6oxp
---

# Summary

Resolve the Gemini distribution route for the core/playbooks split so release
docs and acceptance can either claim a validated Gemini install path or explicitly
defer remote Gemini support.

# Context

`ticket:7h8u6oxp` created package-root Gemini extension skeletons under
`loom-core/` and `loom-playbooks/`, but deliberately did not validate Gemini
runtime distribution. `research:gemini-extension-subdirectory-feasibility` now
rejects the hoped-for one-repository subdirectory extension install path for
current release claims.

The split package plan still needs a Gemini-specific route before public docs can
truthfully describe Gemini install behavior. The route may be a validated remote
distribution mechanism, explicit local package-root linking only, or a documented
deferral until upstream Gemini supports subdirectory extension installs.

# Scope

In:

- Compare the viable Gemini routes named by
  `research:gemini-extension-subdirectory-feasibility`: explicit local package-root
  linking, separate repositories, distribution branches, release/archive packaging,
  or upstream deferral.
- Validate any claimed install route with real Gemini CLI command evidence from a
  clean or temporary Gemini home.
- Preserve evidence showing `gemini extensions install <source>` or
  `gemini extensions link <path>` behavior and `gemini extensions list` output for
  the accepted route.
- Record a ticket-owned route disposition that downstream documentation work can
  use for the Gemini side of `spec:core-and-playbooks-package-contract#ACC-006`.
- If the accepted route is deferral or local-only support, make that explicit for
  downstream public documentation tickets.

Out:

- Publishing Gemini release artifacts.
- Moving this repository into separate Gemini distribution repositories.
- Updating README, INSTALL, ARCHITECTURE, PROTOCOL, examples, or public install
  docs.
- Reintroducing a root Gemini meta-extension that would become a third product
  surface.
- Adding Gemini hooks for static using-Loom preload.
- Changing core/playbook skill membership or non-Gemini harness package surfaces.

Assumptions / decision triggers:

| Assumption or question | Reversible? | Blocks execution? | Disposition |
| --- | --- | --- | --- |
| Gemini remote install support is release-desirable but not required to keep the core/playbooks package split truthful. | yes | no | accepted for this ticket; deferral is a valid outcome |
| `contextFileName` remains the static preload mechanism for core. | yes | no | accepted by current research unless a later dynamic-context ticket changes it |
| A proposed route would require a new repo, branch, or published artifact. | yes | yes for validation claim | record as recommendation/deferral unless the artifact exists and can be tested |
| Upstream Gemini adds documented subdirectory extension install support before this closes. | yes | no | recheck docs/CLI and update evidence before acceptance |

# Acceptance

Owner: spec-owned

Criteria / covered IDs:

- spec:core-and-playbooks-package-contract#ACC-006 — Gemini route disposition only;
  public documentation cleanup remains out of scope for this ticket and must be
  handled by a downstream docs ticket before release acceptance.

Ticket-local criteria, only when no spec owns the reusable contract:

- None - the reusable acceptance contract is owned by
  `spec:core-and-playbooks-package-contract`.

# Current State

Status rationale:

Closed. Local Gemini CLI evidence supported explicit package-root linking and, at
the time, remote/repository-root install deferral. Later `ticket:mbkqbkgq`
superseded the root-core portion by adding a validated Gemini root core shim;
playbook remote install remains unresolved.

Blockers:

- None for this route-disposition ticket.
- One-repository subdirectory remote install remains unsupported by current Gemini
  docs and CLI `0.34.0`; that blocks any downstream claim that root install
  includes playbooks or discovers subdirectory extensions.

Execution notes:

- Use local execution or a bounded spike; Ralph is optional unless the validation
  work expands into packaging artifacts.
- Use a temporary Gemini home for command probes so user-local Gemini state is not
  mutated.
- Keep any release-distribution mechanism as a recommendation unless the exact
  install source exists and a real `gemini extensions install <source>` command is
  observed.
- Do not use `gemini skills install --path` as evidence for extension package
  support; the research rejects that as insufficient.

Continuation note:

No action remains for this route-disposition ticket. Downstream public docs should
describe local package-root linking and remote deferral unless a new remote source
is validated.

# Evidence

Disposition: sufficient

Records:

- evidence:gemini-extension-local-link-route-check

Gaps / limits:

- Evidence supports local package-root linking for `loom-core` and
  `loom-playbooks`.
- `evidence:gemini-root-core-shim-check` now supersedes repository-root install
  rejection for core-only install in the later source state.
- No remote Gemini playbooks install route has been validated.
- Interactive Gemini session context ordering remains unvalidated beyond
  `gemini extensions list` showing the core context file.
- Existing public docs still contain stale root Gemini install guidance; this
  ticket records the route disposition for downstream docs but does not update
  `INSTALL.md`.

# Review And Follow-Through

Critique policy: mandatory
Critique rationale: Gemini install guidance is an operator-facing release surface;
wrong claims would mislead users about how to install the split packages.
Critique disposition: completed

Required critique profiles:

- operator-surface
- package-metadata

Findings:

- No open findings in `critique:gemini-extension-route-review`.

Promotion disposition: deferred
Promotion / deferral rationale: The durable explanation belongs in downstream
public install documentation and final release packaging notes after Codex and
remaining release posture work settle.

Promoted / deferred:

- Deferred to the plan's public documentation and release-posture units.

Wiki disposition: not_required

# Acceptance Decision

Required before closure when acceptance, accepted risk, or operator provenance
needs to be explicit.

Accepted by: OpenCode agent
Accepted at: 2026-05-07T23:07:49Z
Basis: `evidence:gemini-extension-local-link-route-check` supported explicit local
package-root linking and repository-root install rejection for Gemini CLI `0.34.0`
at that source state;
`critique:gemini-extension-route-review` recommends no critique blockers for this
route-disposition slice.
Residual risks: Public docs still contain stale non-Gemini split instructions and
must be updated before release acceptance. Remote Gemini playbooks install remains
deferred. Interactive Gemini context ordering is not validated beyond
`gemini extensions list` showing the core context file.

# Dependencies

`ticket:7h8u6oxp` is the hard prerequisite because it created the package-root
Gemini extension skeletons this ticket validates or defers.

# Journal

- 2026-05-07T23:04:32Z: Created as the Gemini follow-up ticket after research
  rejected one-repository subdirectory extension install support for current
  release claims.
- 2026-05-07T23:06:08Z: Recorded
  `evidence:gemini-extension-local-link-route-check`; ticket now uses a
  local-link-supported / remote-deferred Gemini route pending mandatory critique.
- 2026-05-07T23:07:30Z: Tightened acceptance wording after checking `INSTALL.md`;
  this ticket owns the Gemini route disposition, not public docs cleanup.
- 2026-05-07T23:07:49Z: Mandatory critique
  `critique:gemini-extension-route-review` passed with no findings; closed this
  route-disposition ticket with public docs and remote-install support deferred to
  downstream release/documentation work.
- 2026-05-07T23:08:28Z: Clarified blockers as downstream remote-claim blockers,
  not blockers for this closed route-disposition ticket.
- 2026-05-07T23:25:03Z: Reconciled later `ticket:mbkqbkgq` and
  `evidence:gemini-root-core-shim-check`; repository-root core install is now
  validated by the Gemini shim, while remote playbook install remains unresolved.
