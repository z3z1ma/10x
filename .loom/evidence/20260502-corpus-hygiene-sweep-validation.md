---
id: evidence:corpus-hygiene-sweep-validation
kind: evidence
status: recorded
created_at: 2026-05-02T17:19:31Z
updated_at: 2026-05-02T17:27:34Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:wfxfu4zp
  plan:
    - plan:skills-corpus-perfection-council-followup
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  critique:
    - critique:corpus-hygiene-sweep-review
external_refs: {}
---

# Summary

Targeted observation-first validation for the final low-risk corpus hygiene sweep
owned by `ticket:wfxfu4zp`.

# Procedure

- Captured before-state targeted `rg` observations for each scoped hygiene item.
- Applied small product-surface Markdown edits only under the packet write scope.
- Re-ran targeted `rg` observations after edits.
- Ran `git diff --check` after edits.

# Artifacts

## Before Observations

### Claim queries include `OBJ-*`

Command:

```bash
rg -n "status snapshot|status-snapshot|snapshot|REQ-\[0-9\]|ACC-\[0-9\]|CLAIM-\[0-9\]|OBJ-\[0-9\]|REQ-\*|ACC-\*|OBJ-\*|CLAIM-\*" skills README.md PROTOCOL.md ARCHITECTURE.md
```

Relevant result:

```text
skills/loom-workspace/references/status-snapshot.md:117:rg -n 'REQ-[0-9]{3}|ACC-[0-9]{3}|CLAIM-[0-9]{3}' .loom --glob '*.md'
skills/loom-records/references/repair-and-drift.md:44:rg -n 'REQ-[0-9]{3}|ACC-[0-9]{3}|CLAIM-[0-9]{3}' .loom --glob '*.md'
```

Observation: `repair-and-drift.md` and `status-snapshot.md` claim ID scan
recipes omitted `OBJ-*` while other claim-coverage references already described
initiative objectives.

### `.loom/` tree diagrams and path summaries

Commands:

```bash
rg -n "\.loom/(constitution|initiatives|research|specs|plans|tickets|critique|wiki|evidence|packets|memory)|\.loom tree|canonical tree|workspace tree|tree" README.md PROTOCOL.md ARCHITECTURE.md skills/loom-bootstrap/references/02-truth-and-authority.md skills/loom-workspace/references/workspace-tree.md skills/loom-workspace/SKILL.md
rg -n "\.loom/(constitution/(constitution\.md|decisions/|roadmap/)|initiatives/|research/|specs/|plans/|tickets/|packets/(ralph|critique|wiki)/|critique/|wiki/|evidence/|memory/)" skills/loom-records/references/query-and-linking.md
```

Relevant result:

```text
README.md:538:Inside a Loom-enabled project, the runtime tree looks roughly like this:
skills/loom-workspace/references/workspace-tree.md:37:  .loom/constitution/decisions \
skills/loom-workspace/references/workspace-tree.md:38:  .loom/constitution/roadmap \
skills/loom-workspace/references/workspace-tree.md:39:  .loom/initiatives \
skills/loom-workspace/references/workspace-tree.md:40:  .loom/research \
skills/loom-workspace/references/workspace-tree.md:41:  .loom/specs \
skills/loom-workspace/references/workspace-tree.md:42:  .loom/plans \
skills/loom-workspace/references/workspace-tree.md:43:  .loom/tickets \
skills/loom-workspace/references/workspace-tree.md:44:  .loom/critique \
skills/loom-workspace/references/workspace-tree.md:45:  .loom/wiki \
skills/loom-workspace/references/workspace-tree.md:46:  .loom/packets/ralph \
skills/loom-workspace/references/workspace-tree.md:47:  .loom/packets/critique \
skills/loom-workspace/references/workspace-tree.md:48:  .loom/packets/wiki \
skills/loom-workspace/references/workspace-tree.md:49:  .loom/evidence \
skills/loom-workspace/references/workspace-tree.md:50:  .loom/memory/system \
skills/loom-workspace/references/workspace-tree.md:51:  .loom/memory/user
skills/loom-records/references/query-and-linking.md:24:rg -n '\.loom/(constitution/(constitution\.md|decisions/|roadmap/)|initiatives/|research/|specs/|plans/|tickets/|packets/(ralph|critique|wiki)/|critique/|wiki/|evidence/|memory/)' .loom skills
```

Observation: the README runtime tree omitted constitution subdirectories and
memory subdirectories and ordered `evidence` before `critique`/`wiki`/`packets`;
the query-and-linking path-shape regex ordered `packets` before
`critique`/`wiki`. The workspace reference already carried the fuller canonical
workspace tree.

### Install-safe template-copy wording

Command:

```bash
rg -n "skills/.*/templates|skills/.*templates|cp skills|from skills/|repo-root skills|source repository|installed bundle|template path" README.md PROTOCOL.md ARCHITECTURE.md skills
```

Relevant result:

```text
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:57:cp skills/loom-tickets/templates/ticket.md ".loom/tickets/<YYYYMMDD>-<token>-<short-slug>.md"
skills/loom-tickets/SKILL.md:93:cp skills/loom-tickets/templates/ticket.md ".loom/tickets/${stamp}-${token}-short-slug.md"
```

Observation: the two copy examples assumed repo-root `skills/...` paths without
first saying to copy from the installed skill package path. Other `skills/...`
mentions found in this sweep were reference/query examples rather than template
copy assumptions.

### `# Non-goals` / `# Out Of Scope` template headings

Command:

```bash
rg -n "^# (Non-goals|Out Of Scope)|^#" skills/*/templates/*.md
```

Relevant result:

```text
skills/loom-initiatives/templates/initiative.md:26:# Out Of Scope
skills/loom-tickets/templates/ticket.md:34:# Non-goals
```

Observation: product templates used both `# Out Of Scope` and `# Non-goals` for
the same bounded-exclusion section.

### Memory `inactive` example status

Command:

```bash
rg -n "inactive|status: (active|inactive|remembered|stale|archived|draft|current)" skills/loom-memory skills/loom-records/references/status-lifecycle.md
```

Relevant result:

```text
skills/loom-memory/templates/entities.md:10:key facts | status: inactive | last: YYYY-MM-DD
```

Observation: the memory entity template used `inactive`, which is outside the
preferred memory support values in `status-lifecycle.md`.

### `external_refs: {}` template convention

Command:

```bash
rg -n "external_refs|External References|external references" skills
```

Relevant result:

```text
skills/loom-tickets/templates/ticket.md:14:external_refs: {}
skills/loom-critique/templates/critique.md:13:external_refs: {}
skills/loom-workspace/templates/workspace.md:14:external_refs: {}
skills/loom-specs/templates/spec.md:12:external_refs: {}
skills/loom-evidence/templates/evidence.md:12:external_refs: {}
skills/loom-research/templates/research.md:12:external_refs: {}
skills/loom-records/references/frontmatter.md:60:Most canonical records may also carry optional `external_refs` when outside
```

Observation: several templates included `external_refs: {}`, while others omitted
it. The common frontmatter reference described `external_refs` as optional but did
not document the template omission convention.

### Ad hoc research link verbs

Command:

```bash
rg -n "links:|supports:|supported_by|depends_on|supersedes|informs|derived_from|constrains|answers|raises|rejects|related|follow_up|uses|blocks|blocked_by|superseded_by|promoted_to" skills/loom-research/references skills/loom-research/templates skills/loom-records/references/semantic-link-usage.md
```

Relevant result:

```text
skills/loom-research/references/research-shape.md:64:Deferred questions are a subset of research, not a separate record kind. When a question matures, promote it into its own research record and link back with `superseded_by` or `promoted_to`.
```

Observation: `research-shape.md` named `superseded_by` and `promoted_to`, which
were not standardized link grammar in `semantic-link-usage.md`.

## After Observations

### Claim queries include `OBJ-*`

Command:

```bash
rg -n "OBJ-\[0-9\]\{3\}|REQ-\[0-9\]\{3\}|ACC-\[0-9\]\{3\}|CLAIM-\[0-9\]\{3\}" skills/loom-records/references/repair-and-drift.md skills/loom-workspace/references/status-snapshot.md
```

Result:

```text
skills/loom-workspace/references/status-snapshot.md:117:rg -n 'OBJ-[0-9]{3}|REQ-[0-9]{3}|ACC-[0-9]{3}|CLAIM-[0-9]{3}' .loom --glob '*.md'
skills/loom-records/references/repair-and-drift.md:44:rg -n 'OBJ-[0-9]{3}|REQ-[0-9]{3}|ACC-[0-9]{3}|CLAIM-[0-9]{3}' .loom --glob '*.md'
```

### `.loom/` tree diagrams and path summaries

Command:

```bash
rg -n "\.loom/(constitution|initiatives|research|specs|plans|tickets|critique|wiki|packets|evidence|memory)|\.loom/\(|Inside a Loom-enabled project" README.md skills/loom-records/references/query-and-linking.md skills/loom-workspace/references/workspace-tree.md skills/loom-bootstrap/references/02-truth-and-authority.md
```

Relevant result:

```text
README.md:538:Inside a Loom-enabled project, the runtime tree looks roughly like this:
skills/loom-records/references/query-and-linking.md:24:rg -n '\.loom/(constitution/(constitution\.md|decisions/|roadmap/)|initiatives/|research/|specs/|plans/|tickets/|critique/|wiki/|packets/(ralph|critique|wiki)/|evidence/|memory/)' .loom skills
```

Manual check: `README.md:540-561` now mirrors the workspace tree ordering and
includes constitution and memory subdirectories.

### Install-safe template-copy wording

Command:

```bash
rg -n "Copy from the installed Loom skill package path|installed Loom skill|cp skills/loom-tickets/templates/ticket.md|skills/.*/templates" skills/loom-bootstrap/references/06-filesystem-and-tooling.md skills/loom-tickets/SKILL.md skills
```

Relevant result:

```text
skills/loom-tickets/SKILL.md:88:A common shell flow copies the ticket template from the installed Loom skill
skills/loom-tickets/SKILL.md:95:cp skills/loom-tickets/templates/ticket.md ".loom/tickets/${stamp}-${token}-short-slug.md"
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:56:Copy from the installed Loom skill package path for the current harness. In a
skills/loom-bootstrap/references/06-filesystem-and-tooling.md:60:cp skills/loom-tickets/templates/ticket.md ".loom/tickets/<YYYYMMDD>-<token>-<short-slug>.md"
```

### `# Non-goals` / `# Out Of Scope` template headings

Command:

```bash
rg -n "^# (Non-goals|Out Of Scope)$" skills/*/templates/*.md .loom/tickets/20260502-wfxfu4zp-run-corpus-hygiene-sweep.md
```

Result:

```text
skills/loom-initiatives/templates/initiative.md:26:# Out Of Scope
.loom/tickets/20260502-wfxfu4zp-run-corpus-hygiene-sweep.md:60:# Out Of Scope
skills/loom-tickets/templates/ticket.md:34:# Out Of Scope
```

### Memory `inactive` example status

Command:

```bash
rg -n "inactive|status: (active|inactive|stale|superseded|retired)" skills/loom-memory/templates/entities.md skills/loom-records/references/status-lifecycle.md
```

Result:

```text
skills/loom-memory/templates/entities.md:7:key facts | status: active | last: YYYY-MM-DD | -> [[related-page-or-record]]
skills/loom-memory/templates/entities.md:10:key facts | status: stale | last: YYYY-MM-DD
```

### `external_refs: {}` template convention

Command:

```bash
rg -n "external_refs|Templates may omit|Omitted means" skills/loom-records/references/frontmatter.md skills --glob "templates/*.md"
```

Relevant result:

```text
skills/loom-records/references/frontmatter.md:60:Most canonical records may also carry optional `external_refs` when outside
skills/loom-records/references/frontmatter.md:61:systems request, mirror, package, or help navigate the work. Templates may omit
skills/loom-records/references/frontmatter.md:62:`external_refs` when outside references are uncommon for that record kind. Omitted
skills/loom-records/references/frontmatter.md:63:means no external references are declared; add `external_refs: {}` or a populated
```

### Ad hoc research link verbs

Command:

```bash
rg -n "superseded_by|promoted_to|shared semantic link guidance|links:|Semantic Link Usage" skills/loom-research/references skills/loom-research/templates skills/loom-records/references/semantic-link-usage.md
```

Relevant result:

```text
skills/loom-research/references/research-shape.md:66:successor in `links:` or body prose using the shared semantic link guidance.
```

Observation: no `superseded_by` or `promoted_to` matches remain in the scoped
research surfaces.

### Diff whitespace validation

Command:

```bash
git diff --check
```

Result: exit 0, no output.

Additional untracked-record whitespace checks, because `git diff --check` does
not include untracked files before staging:

```bash
git diff --check --no-index /dev/null .loom/evidence/20260502-corpus-hygiene-sweep-validation.md; rc=$?; if [ "$rc" -eq 1 ]; then exit 0; else exit "$rc"; fi
git diff --check --no-index /dev/null .loom/packets/ralph/20260502T171547Z-ticket-wfxfu4zp-iter-01.md; rc=$?; if [ "$rc" -eq 1 ]; then exit 0; else exit "$rc"; fi
```

Result: both exit 0 after normalizing the no-index difference exit code; no
whitespace warnings were emitted.

# Supports Claims

- `ticket:wfxfu4zp#ACC-001`
- `ticket:wfxfu4zp#ACC-002`
- `ticket:wfxfu4zp#ACC-003`
- `initiative:skills-corpus-perfection-council-followup#OBJ-007`

# Challenges Claims

None - the targeted searches did not surface a challenge to the scoped hygiene
claims. `ticket:wfxfu4zp#ACC-004` is reviewed separately by
`critique:corpus-hygiene-sweep-review`.

# Environment

Commit: `08b42ba43a7df97e49008fb56803e977bc55dd6d`
Branch: `main`
Runtime: Markdown/file edits only; no app runtime or test suite
OS: macOS Darwin
Relevant config: Existing worktree included the parent ticket activation diff and
untracked Ralph packet before child edits.

# Validity

Valid for: the working tree after this hygiene sweep and parent/oracle critique
reconciliation.

Recheck when: README, protocol architecture notes, bootstrap references,
workspace tree references, record grammar references, ticket templates, research
references, memory templates, or claim-query recipes change.

# Limitations

- This evidence is structural/search validation, not oracle critique.
- It does not prove every possible prose phrase in the corpus is stylistically
  uniform; it covers the scoped council hygiene items only.
- It does not close `ticket:wfxfu4zp`; critique and acceptance are ticket-owned
  follow-through recorded separately.

# Result

All scoped hygiene findings were resolved or documented with targeted product
surface edits. `git diff --check` passed with no output.

# Interpretation

The observations support `ticket:wfxfu4zp` hygiene acceptance when consumed with
the separate oracle critique. They do not by themselves satisfy `ACC-004` because
critique is not an evidence-owned decision.

# Related Records

- `ticket:wfxfu4zp`
- `plan:skills-corpus-perfection-council-followup`
- `initiative:skills-corpus-perfection-council-followup`
- `critique:corpus-hygiene-sweep-review`
