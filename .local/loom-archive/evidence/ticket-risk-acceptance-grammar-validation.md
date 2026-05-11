---
id: evidence:ticket-risk-acceptance-grammar-validation
kind: evidence
status: recorded
created_at: 2026-05-02T10:11:03Z
updated_at: 2026-05-02T10:11:03Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  tickets:
    - ticket:50ded996
  packets:
    - packet:ralph-ticket-50ded996-20260502T095614Z
  critique:
    - critique:ticket-risk-acceptance-grammar-review
  plan:
    - plan:skills-corpus-protocol-sharpening
external_refs: {}
---

# Summary

Structural validation for ticket `change_class` / `risk_class`, critique finding
disposition, accepted-risk, follow-up conversion, and acceptance-gate grammar
added under `ticket:50ded996`.

# Procedure

The parent reviewed the Ralph child output, routed oracle findings and nits back
through the fixer, reconciled ticket wording, and ran targeted structural checks
on the final diff.

Commands and searches performed:

```text
git diff --check
git diff --stat
Grep new/materially-updated/legacy ticket classification boundary in loom-tickets
Grep risk_class and change_class alignment in change-class.md
Grep accepted_risk, converted_to_follow_up, superseded by evidence, linked follow-up tickets, and FIND references in loom-tickets
Grep compatible finding disposition examples in loom-critique
```

# Artifacts

Observed product files changed:

- `skills/loom-tickets/templates/ticket.md`
- `skills/loom-tickets/references/readiness.md`
- `skills/loom-tickets/references/acceptance-gate.md`
- `skills/loom-records/references/change-class.md`
- `skills/loom-critique/references/finding-format.md`
- `skills/loom-critique/templates/critique.md`

Observed outputs:

```text
git diff --check
-> no output

git diff --stat
-> 7 files changed, 101 insertions(+), 25 deletions(-)

Grep ticket classification boundary
-> found new/materially-updated ticket requirement and legacy normalization wording in readiness and acceptance gate guidance

Grep change-class alignment
-> found change_class/risk_class examples and lifecycle-boundary wording in change-class.md

Grep ticket disposition grammar
-> found accepted_risk, converted_to_follow_up, superseded by evidence, linked follow-up tickets, and critique:example-review#FIND-001 examples

Grep critique compatibility
-> found accepted_risk, converted_to_follow_up, critique:example-review#FIND-001, and linked follow-up ticket wording in critique surfaces
```

# Supports Claims

- `ticket:50ded996` ACC-001
- `ticket:50ded996` ACC-002
- `ticket:50ded996` ACC-003
- `ticket:50ded996` ACC-004
- `ticket:50ded996` ACC-005
- `initiative:skills-corpus-protocol-sharpening#OBJ-002`
- `initiative:skills-corpus-protocol-sharpening#OBJ-005`
- `research:skills-corpus-council-review#CLAIM-006`
- `research:skills-corpus-council-review#CLAIM-009`

# Challenges Claims

None observed.

# Environment

Commit: `8351b5a34c2b131c31ea982494f978892936eb71` plus the current working-tree
diff for `ticket:50ded996` before commit.

Branch: `main`

Runtime: OpenCode parent session with Ralph fixer subagent and oracle critique
subagent.

OS: darwin

Relevant config: repository has no automated test suite; validation is structural
and manual per `AGENTS.md`.

# Validity

Valid for: the working tree after `packet:ralph-ticket-50ded996-20260502T095614Z`
and oracle critique pass `ses_217d5c9afffeUkQlhpn2xyHftA`.

Recheck when: ticket template/readiness/acceptance guidance, critique finding
disposition grammar, or change/risk class taxonomy changes.

# Limitations

This evidence validates structural consistency of ticket-scoped grammar changes.
It does not normalize every legacy ticket; the accepted grammar says legacy
tickets are normalized when touched or before governed execution/acceptance.

# Result

Ticket guidance now requires `change_class` and `risk_class` for new or materially
updated tickets, treats frontmatter `risk_class` as canonical, keeps critique
finding dispositions ticket-owned, includes follow-up conversion, and preserves
fail-closed acceptance over missing evidence, missing mandatory critique, and
unresolved medium/high findings.

# Interpretation

The observations support acceptance of `ticket:50ded996` when combined with
`critique:ticket-risk-acceptance-grammar-review`. Evidence does not itself close
the ticket; the ticket acceptance decision owns closure.

# Related Records

- `ticket:50ded996`
- `packet:ralph-ticket-50ded996-20260502T095614Z`
- `critique:ticket-risk-acceptance-grammar-review`
- `plan:skills-corpus-protocol-sharpening`
