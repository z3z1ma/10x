---
id: evidence:sibling-packet-ticket-anchor-validation
kind: evidence
status: recorded
created_at: 2026-05-02T23:09:05Z
updated_at: 2026-05-02T23:18:54Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:sibpkt7
  packet:
    - packet:ralph-ticket-sibpkt7-20260502T230712Z
  critique:
    - critique:sibling-packet-ticket-anchor-review
    - critique:sibling-packet-ticket-anchor-rereview
external_refs: {}
---

# Summary

Observed critique/wiki packet template ticket-anchor wording before and after the
Ralph iteration, then ran `git diff --check`. The after-state shows ticket
anchors are optional in critique/wiki packet targets and parent merge scopes while
preserving ticket-centered examples when a ticket actually owns execution or
follow-through.

# Procedure

1. Confirmed packet source fingerprint commit `4dde3b78a6f032e95a21fc03847d7a403923c42a`
   matched `HEAD`.
2. Captured before-state searches in the targeted critique/wiki packet templates.
3. Edited only the allowed critique/wiki packet templates, ticket, evidence
   record, and Ralph packet.
4. Captured after-state searches in the same targeted templates.
5. Ran `git diff --check`.

# Artifacts

## Before search: ticket refs

Command:

```bash
rg -n 'ticket:<token>|ticket refs?|ticket anchor|ticket-centered|ticket-owned|ticket' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-wiki/templates/wiki-packet.md:23:    - ticket:<token>
skills/loom-wiki/templates/wiki-packet.md:59:Name the originating ticket, critique, research, initiative, or other owner ref
skills/loom-wiki/templates/wiki-packet.md:110:- a substantive rewrite needs critique, ticket disposition, or retrospective
skills/loom-critique/templates/critique-packet.md:6:target: ticket:<token>
skills/loom-critique/templates/critique-packet.md:32:    - ticket:<token>
skills/loom-critique/templates/critique-packet.md:71:The ticket, parent plan or initiative, relevant spec/research/evidence, prior
skills/loom-critique/templates/critique-packet.md:87:`parent_merge_scope` must name the ticket, critique record, evidence record, or
skills/loom-critique/templates/critique-packet.md:94:`ticket:abc123xy` becomes `ticket-abc123xy` in
skills/loom-critique/templates/critique-packet.md:95:`.loom/packets/critique/<UTC compact timestamp>-ticket-abc123xy.md`. When a
skills/loom-critique/templates/critique-packet.md:119:it as review context only; the ticket still owns critique disposition.
skills/loom-critique/templates/critique-packet.md:141:- Did the actual diff or artifact satisfy the ticket, spec, acceptance coverage,
skills/loom-critique/templates/critique-packet.md:173:The parent creates or updates real critique and ticket records during
```

## Before search: `None - rationale`

Command:

```bash
rg -n 'None -|None - <rationale>|None - rationale' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-critique/templates/critique-packet.md:13:    - "<TBD: changed paths under review, or None - no path-specific target>"
skills/loom-critique/templates/critique-packet.md:27:    - "<TBD: critique child write refs, or None - reviewer returns output only>"
skills/loom-critique/templates/critique-packet.md:29:    - "<TBD: critique child write paths, or None - reviewer returns output only>"
skills/loom-critique/templates/critique-packet.md:34:    # or: None - <rationale for no parent record reconciliation>
skills/loom-critique/templates/critique-packet.md:37:    # or: None - <rationale for no parent path reconciliation>
skills/loom-critique/templates/critique-packet.md:89:`None - <rationale>` when no parent merge target exists. Do not leave it empty or
skills/loom-wiki/templates/wiki-packet.md:19:    - "<TBD: wiki page paths the child may modify, or None - rationale>"
skills/loom-wiki/templates/wiki-packet.md:24:    # or: None - <rationale for no parent record reconciliation>
skills/loom-wiki/templates/wiki-packet.md:27:    # or: None - <rationale for no parent path reconciliation>
skills/loom-wiki/templates/wiki-packet.md:62:`None - <rationale>` when no parent merge target exists. Do not leave it empty or
```

## Before search: `parent_merge_scope`

Command:

```bash
rg -n 'parent_merge_scope' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-critique/templates/critique-packet.md:30:parent_merge_scope:
skills/loom-critique/templates/critique-packet.md:87:`parent_merge_scope` must name the ticket, critique record, evidence record, or
skills/loom-critique/templates/critique-packet.md:174:reconciliation; do not leave placeholder IDs in `parent_merge_scope`.
skills/loom-wiki/templates/wiki-packet.md:20:parent_merge_scope:
skills/loom-wiki/templates/wiki-packet.md:60:in `parent_merge_scope.records` when parent reconciliation is expected.
skills/loom-wiki/templates/wiki-packet.md:61:`parent_merge_scope` must name parent reconciliation targets or explicitly say
```

## Before search: packet targets

Command:

```bash
rg -n '^target:|review_target:|# Target Pages|target type|review target|synthesis target|record ref or page slug' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-critique/templates/critique-packet.md:6:target: ticket:<token>
skills/loom-critique/templates/critique-packet.md:7:review_target:
skills/loom-critique/templates/critique-packet.md:9:  summary: <one-line human-readable review target>
skills/loom-critique/templates/critique-packet.md:102:reviewers can inspect the target type, stable reference, diff handle, and changed
skills/loom-wiki/templates/wiki-packet.md:6:target: <record ref or page slug>
skills/loom-wiki/templates/wiki-packet.md:92:# Target Pages
```

## Before search: Ralph-governed wording

Command:

```bash
rg -n 'Ralph-governed|verification_posture|Ralph' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-wiki/templates/wiki-packet.md:71:the synthesis Ralph-governed.
skills/loom-wiki/templates/wiki-packet.md:83:Wiki packets do not use Ralph `verification_posture`. Synthesis quality comes
skills/loom-wiki/templates/wiki-packet.md:90:change context; those fields do not make synthesis a Ralph implementation route.
skills/loom-wiki/templates/wiki-packet.md:124:does not make this wiki packet a Ralph implementation packet.
skills/loom-critique/templates/critique-packet.md:72:Ralph packet output, and acceptance or claim coverage targets that constrain
skills/loom-critique/templates/critique-packet.md:80:the review Ralph-governed.
skills/loom-critique/templates/critique-packet.md:123:Critique packets do not use Ralph `verification_posture`. Review quality comes
skills/loom-critique/templates/critique-packet.md:179:does not make this critique packet a Ralph implementation packet.
```

## After search: ticket refs

Command:

```bash
rg -n 'ticket:<token>|ticket refs?|ticket anchor|ticket-centered|ticket-owned|ticket' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-wiki/templates/wiki-packet.md:6:target: "<TBD: wiki:<slug>, source record ref, ticket:<token>, or synthesis target slug>"
skills/loom-wiki/templates/wiki-packet.md:23:    - "<TBD: ticket:<token> when a ticket owns follow-through, originating owner ref, or None - no additional parent record reconciliation needed>"
skills/loom-wiki/templates/wiki-packet.md:59:Name the originating ticket only when a ticket owns follow-through. Otherwise
skills/loom-wiki/templates/wiki-packet.md:111:- a substantive rewrite needs critique, ticket disposition, or retrospective
skills/loom-critique/templates/critique-packet.md:6:target: "<TBD: ticket:<token>, record ref, review target slug, diff handle, or external summary ID>"
skills/loom-critique/templates/critique-packet.md:33:    - "<TBD: ticket:<token> when a ticket owns execution, owner record ref, or None - no parent record reconciliation needed>"
skills/loom-critique/templates/critique-packet.md:71:The ticket when one owns execution, parent plan or initiative, relevant
skills/loom-critique/templates/critique-packet.md:87:`target` may name `ticket:<token>` when the ticket itself is the review target,
skills/loom-critique/templates/critique-packet.md:89:summary, or handoff package without a ticket anchor. `parent_merge_scope` must
skills/loom-critique/templates/critique-packet.md:90:name the ticket when a ticket owns execution, the critique record, evidence
skills/loom-critique/templates/critique-packet.md:97:`ticket:abc123xy` becomes `ticket-abc123xy` in
skills/loom-critique/templates/critique-packet.md:98:`.loom/packets/critique/<UTC compact timestamp>-ticket-abc123xy.md`. When a
skills/loom-critique/templates/critique-packet.md:122:it as review context only; the ticket still owns critique disposition.
skills/loom-critique/templates/critique-packet.md:144:- Did the actual diff or artifact satisfy the ticket, spec, acceptance coverage,
skills/loom-critique/templates/critique-packet.md:176:The parent creates or updates real critique and ticket records during
```

## After search: `None - rationale`

Command:

```bash
rg -n 'None -|None - <rationale>|None - rationale' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-critique/templates/critique-packet.md:13:    - "<TBD: changed paths under review, or None - no path-specific target>"
skills/loom-critique/templates/critique-packet.md:27:    - "<TBD: critique child write refs, or None - reviewer returns output only>"
skills/loom-critique/templates/critique-packet.md:29:    - "<TBD: critique child write paths, or None - reviewer returns output only>"
skills/loom-critique/templates/critique-packet.md:33:    - "<TBD: ticket:<token> when a ticket owns execution, owner record ref, or None - no parent record reconciliation needed>"
skills/loom-critique/templates/critique-packet.md:34:    # or: None - <rationale for no additional parent record reconciliation>
skills/loom-critique/templates/critique-packet.md:36:    - "<TBD: .loom/critique/<slug>.md, other owner path, or None - no parent path reconciliation needed>"
skills/loom-critique/templates/critique-packet.md:37:    # or: None - <rationale for no parent path reconciliation>
skills/loom-critique/templates/critique-packet.md:92:explicitly say `None - <rationale>` when no parent merge target exists. Do not
skills/loom-wiki/templates/wiki-packet.md:19:    - "<TBD: wiki page paths the child may modify, or None - rationale>"
skills/loom-wiki/templates/wiki-packet.md:23:    - "<TBD: ticket:<token> when a ticket owns follow-through, originating owner ref, or None - no additional parent record reconciliation needed>"
skills/loom-wiki/templates/wiki-packet.md:24:    # or: None - <rationale for no parent record reconciliation>
skills/loom-wiki/templates/wiki-packet.md:26:    - "<TBD: .loom/wiki/<slug>.md, other owner path, or None - no parent path reconciliation needed>"
skills/loom-wiki/templates/wiki-packet.md:27:    # or: None - <rationale for no parent path reconciliation>
skills/loom-wiki/templates/wiki-packet.md:63:explicitly say `None - <rationale>` when no parent merge target exists. Do not
```

## After search: `parent_merge_scope`

Command:

```bash
rg -n 'parent_merge_scope' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-wiki/templates/wiki-packet.md:20:parent_merge_scope:
skills/loom-wiki/templates/wiki-packet.md:61:ref in `target` and `parent_merge_scope.records` when parent reconciliation is
skills/loom-wiki/templates/wiki-packet.md:62:expected. `parent_merge_scope` must name parent reconciliation targets or
skills/loom-critique/templates/critique-packet.md:30:parent_merge_scope:
skills/loom-critique/templates/critique-packet.md:89:summary, or handoff package without a ticket anchor. `parent_merge_scope` must
skills/loom-critique/templates/critique-packet.md:177:reconciliation; do not leave placeholder IDs in `parent_merge_scope`.
```

## After search: packet targets

Command:

```bash
rg -n '^target:|review_target:|# Target Pages|target type|review target|synthesis target|record ref or page slug' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-critique/templates/critique-packet.md:6:target: "<TBD: ticket:<token>, record ref, review target slug, diff handle, or external summary ID>"
skills/loom-critique/templates/critique-packet.md:7:review_target:
skills/loom-critique/templates/critique-packet.md:9:  summary: <one-line human-readable review target>
skills/loom-critique/templates/critique-packet.md:87:`target` may name `ticket:<token>` when the ticket itself is the review target,
skills/loom-critique/templates/critique-packet.md:105:reviewers can inspect the target type, stable reference, diff handle, and changed
skills/loom-wiki/templates/wiki-packet.md:6:target: "<TBD: wiki:<slug>, source record ref, ticket:<token>, or synthesis target slug>"
skills/loom-wiki/templates/wiki-packet.md:93:# Target Pages
```

## After search: Ralph-governed wording

Command:

```bash
rg -n 'Ralph-governed|verification_posture|Ralph' 'skills/loom-critique/templates/critique-packet.md' 'skills/loom-wiki/templates/wiki-packet.md'
```

Output:

```text
skills/loom-wiki/templates/wiki-packet.md:72:the synthesis Ralph-governed.
skills/loom-wiki/templates/wiki-packet.md:84:Wiki packets do not use Ralph `verification_posture`. Synthesis quality comes
skills/loom-wiki/templates/wiki-packet.md:91:change context; those fields do not make synthesis a Ralph implementation route.
skills/loom-wiki/templates/wiki-packet.md:125:does not make this wiki packet a Ralph implementation packet.
skills/loom-critique/templates/critique-packet.md:80:the review Ralph-governed.
skills/loom-critique/templates/critique-packet.md:126:Critique packets do not use Ralph `verification_posture`. Review quality comes
skills/loom-critique/templates/critique-packet.md:182:does not make this critique packet a Ralph implementation packet.
```

## Validation command

Command:

```bash
git diff --check
```

Result: passed with no output.

Parent reconciliation check at `2026-05-02T23:11:23Z`:

- `git diff --check` passed with no output.
- Scoped ticket claim statuses use canonical `supported_pending_review`
  vocabulary.
- `packet:ralph-ticket-sibpkt7-20260502T230712Z` frontmatter is `status:
  consumed` with parent merge notes.

Finding remediation at `2026-05-02T23:15:30Z`:

- `critique:sibling-packet-ticket-anchor-review#SIBPKT7-FIND-001` was addressed
  by replacing empty `parent_merge_scope.paths` in the Ralph packet with the
  concrete paths the parent reconciles.
- `critique:sibling-packet-ticket-anchor-review#SIBPKT7-FIND-002` was addressed
  by clarifying that critique path-set reviews use existing structured
  `review_target` fields: closest existing `kind`, unavailable scalar fields set
  to `none`, and reviewed paths listed under `review_target.paths`.

Oracle re-review at `2026-05-02T23:18:54Z` confirmed both prior findings resolved
and found no new findings.

# Supports Claims

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-007`
- `ticket:sibpkt7#ACC-001`
- `ticket:sibpkt7#ACC-002`
- `ticket:sibpkt7#ACC-003`
- `ticket:sibpkt7#ACC-004`

# Challenges Claims

None - the observations did not challenge a scoped claim.

# Environment

Commit: `4dde3b78a6f032e95a21fc03847d7a403923c42a` plus scoped uncommitted
changes for `ticket:sibpkt7`.
Branch: `main`.
Runtime: Markdown corpus; no app runtime or automated test suite.
OS: macOS/Darwin.

# Validity

Valid for: the targeted critique/wiki packet template changes, parent
reconciliation, and ticket/evidence updates made during
`packet:ralph-ticket-sibpkt7-20260502T230712Z`.
Recheck when: either targeted packet template, this ticket, evidence record, or
Ralph packet changes again before acceptance.

# Limitations

- Does not itself establish `ticket:sibpkt7#ACC-005`; oracle critique and
  ticket-owned acceptance are recorded separately.
- Does not validate historical critique/wiki packets outside the targeted
  templates.
- Does not close the ticket or own the acceptance decision.

# Result

The targeted critique/wiki packet templates now make ticket anchors optional and
explicit while preserving ticket-centered examples where a ticket owns execution
or follow-through.

# Interpretation

- Critique packet `target` is no longer hard-coded to `ticket:<token>` and now
  allows record, slug, diff, or external-summary targets.
- Wiki packet `target` now names wiki, source-record, ticket, or synthesis targets
  rather than a vague record/page placeholder.
- `parent_merge_scope` examples now say when ticket refs are appropriate and show
  `None - <rationale>` patterns for absent parent merge targets.
- Critique/wiki packet templates still explicitly avoid Ralph `verification_posture`
  and Ralph-governed semantics.

# Residual Risks

- This is structural Markdown evidence. Oracle critique reviewed owner-boundary,
  records-grammar, and operator-clarity before ticket acceptance.

# Related Records

- `initiative:skills-corpus-template-grammar-safety-pass`
- `plan:skills-corpus-template-grammar-safety-pass`
- `ticket:sibpkt7`
- `packet:ralph-ticket-sibpkt7-20260502T230712Z`
- `critique:sibling-packet-ticket-anchor-review`
- `critique:sibling-packet-ticket-anchor-rereview`
