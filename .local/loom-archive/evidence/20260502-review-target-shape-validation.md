---
id: evidence:review-target-shape-validation
kind: evidence
status: recorded
created_at: 2026-05-02T20:19:52Z
updated_at: 2026-05-02T20:30:02Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:revtgt7x
  packet:
    - packet:ralph-ticket-revtgt7x-20260502T201800Z
    - packet:ralph-ticket-revtgt7x-20260502T202813Z
external_refs: {}
---

# Summary

Observed before and after `review_target` grammar references while aligning
direct critique records with scalar target handles and critique packets with a
structured review-target mapping. Repair iteration 2 added a legacy compatibility
boundary for older consumed critique packets with `kind` plus `diff` only.

# Procedure

Ran the required observation-first searches before and after the grammar edits:

```bash
rg -n "review_target|Review Target|review target" \
  "skills/loom-critique/templates/critique.md" \
  "skills/loom-critique/templates/critique-packet.md" \
  "skills/loom-critique/SKILL.md" \
  "skills/loom-critique/references/critique-lens.md" \
  "skills/loom-records/references/frontmatter.md" \
  "skills/loom-records/references/packet-frontmatter.md" || true
```

Ran structural diff validation:

```bash
git diff --check
```

Repair iteration 2 also ran targeted compatibility observations:

```bash
rg -n "review_target|legacy|newly compiled|new critique packet authoring" \
  "skills/loom-records/references/packet-frontmatter.md" \
  "skills/loom-critique/templates/critique-packet.md"
```

```bash
rg -n -C 4 "review_target:|kind:|diff:|summary:|ref:|paths:" \
  ".loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md" \
  ".loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md"
```

# Artifacts

## Before `review_target` search

```text
skills/loom-critique/templates/critique-packet.md:7:review_target:
skills/loom-critique/templates/critique-packet.md:84:Do not conflate this encoded packet name with the structured `review_target`
skills/loom-critique/templates/critique-packet.md:85:frontmatter field. `review_target` names the artifact, diff, PR, branch, commit,
skills/loom-critique/templates/critique-packet.md:139:Stop or return `blocked` if the declared `review_target`, source fingerprint,
skills/loom-critique/templates/critique.md:11:review_target: <record ref | code change target>
skills/loom-critique/templates/critique.md:20:# Review Target
skills/loom-critique/references/critique-lens.md:144:Use `skills/loom-records/references/change-class.md` when the review target
skills/loom-critique/SKILL.md:65:1. choose the review target
skills/loom-critique/SKILL.md:102:- the review target is explicit
skills/loom-records/references/packet-frontmatter.md:29:# change_class, risk_class, iteration, verification_posture, review_target
skills/loom-records/references/packet-frontmatter.md:112:- `review_target` is critique-family grammar. Critique templates include it so a
skills/loom-records/references/packet-frontmatter.md:156:derive packet IDs or filenames from the structured `review_target` field by
skills/loom-records/references/packet-frontmatter.md:157:default; `review_target` describes the artifact, diff, PR, branch, commit, or
skills/loom-records/references/frontmatter.md:47:- critique records may add `review_target`
```

## After `review_target` search

```text
skills/loom-critique/templates/critique.md:11:review_target: <scalar record ref, path, PR, branch, commit, diff range, or target summary>
skills/loom-critique/templates/critique.md:20:# Review Target
skills/loom-critique/templates/critique.md:23:`review_target` field for a direct critique record is intentionally a scalar,
skills/loom-critique/templates/critique-packet.md:7:review_target:
skills/loom-critique/templates/critique-packet.md:9:  summary: <one-line human-readable review target>
skills/loom-critique/templates/critique-packet.md:87:Do not conflate this encoded packet name with the structured `review_target`
skills/loom-critique/templates/critique-packet.md:88:frontmatter field. Critique packet `review_target` is a mapping so fresh-context
skills/loom-critique/templates/critique-packet.md:145:Stop or return `blocked` if the declared `review_target`, source fingerprint,
skills/loom-records/references/packet-frontmatter.md:29:# change_class, risk_class, iteration, verification_posture, review_target
skills/loom-records/references/packet-frontmatter.md:112:- `review_target` is critique-family grammar. Direct critique records use the
skills/loom-records/references/packet-frontmatter.md:117:### Critique Packet `review_target`
skills/loom-records/references/packet-frontmatter.md:122:review_target:
skills/loom-records/references/packet-frontmatter.md:124:  summary: <one-line human-readable review target>
skills/loom-records/references/packet-frontmatter.md:134:scalar fields rather than leaving the review target ambiguous. Keep `summary`
skills/loom-records/references/packet-frontmatter.md:177:derive packet IDs or filenames from the structured `review_target` field by
skills/loom-records/references/packet-frontmatter.md:178:default; `review_target` describes the artifact, diff, PR, branch, commit, or
skills/loom-critique/references/critique-lens.md:38:Use the family-appropriate `review_target` shape when recording that target:
skills/loom-critique/references/critique-lens.md:149:Use `skills/loom-records/references/change-class.md` when the review target
skills/loom-critique/SKILL.md:65:1. choose the review target and record it in the family-appropriate shape
skills/loom-critique/SKILL.md:73:## Review Target Grammar
skills/loom-critique/SKILL.md:75:- Direct critique records use scalar `review_target` frontmatter: one
skills/loom-critique/SKILL.md:77:  target summary. Put longer target explanation in the `# Review Target` body
skills/loom-critique/SKILL.md:79:- Critique packets use structured `review_target` frontmatter because a bounded
skills/loom-critique/SKILL.md:113:- the review target is explicit
skills/loom-records/references/frontmatter.md:47:- critique records may add scalar `review_target`; critique packets use the
skills/loom-records/references/frontmatter.md:50:### Critique `review_target`
skills/loom-records/references/frontmatter.md:52:Direct critique records use a scalar `review_target` frontmatter value:
skills/loom-records/references/frontmatter.md:55:review_target: <record ref | path | PR | branch | commit | diff range | concise target summary>
skills/loom-records/references/frontmatter.md:63:Critique packets may use structured `review_target` frontmatter because packets
```

## `git diff --check`

```text
No output; command exited successfully.
```

## Repair compatibility wording search

```text
skills/loom-critique/templates/critique-packet.md:7:review_target:
skills/loom-critique/templates/critique-packet.md:71:This template describes new critique packet authoring; older consumed critique
skills/loom-critique/templates/critique-packet.md:72:packets may retain the legacy-compatible `review_target` mapping documented in
skills/loom-critique/templates/critique-packet.md:90:Do not conflate this encoded packet name with the structured `review_target`
skills/loom-critique/templates/critique-packet.md:91:frontmatter field. Critique packet `review_target` is a mapping so fresh-context
skills/loom-critique/templates/critique-packet.md:148:Stop or return `blocked` if the declared `review_target`, source fingerprint,
skills/loom-records/references/packet-frontmatter.md:29:# change_class, risk_class, iteration, verification_posture, review_target
skills/loom-records/references/packet-frontmatter.md:112:- `review_target` is critique-family grammar. Direct critique records use the
skills/loom-records/references/packet-frontmatter.md:117:### Critique Packet `review_target`
skills/loom-records/references/packet-frontmatter.md:122:review_target:
skills/loom-records/references/packet-frontmatter.md:131:For newly compiled critique packets, `kind` and `summary` are required. Use
skills/loom-records/references/packet-frontmatter.md:138:`diff` in this mapping. Treat those as understandable legacy support artifacts,
skills/loom-records/references/packet-frontmatter.md:183:derive packet IDs or filenames from the structured `review_target` field by
skills/loom-records/references/packet-frontmatter.md:184:default; `review_target` describes the artifact, diff, PR, branch, commit, or
skills/loom-records/references/packet-frontmatter.md:306:for legacy compatibility when the packet does not say otherwise. New packet
```

## Targeted historical critique packet observation

```text
.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md-5-status: consumed
.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md-6-target: ticket:6uy1rx20
.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md:7:review_target:
.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md:8:  kind: code_change
.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md:9:  diff: open-loom working tree changes
.loom/packets/critique/20260425T201112Z-ticket-6uy1rx20-open-loom-review.md-10-mode: review
.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md-5-status: consumed
.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md-6-target: ticket:vairivh8
.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md:7:review_target:
.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md:8:  kind: code_change
.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md:9:  diff: staged changes for protocol hardening pass
.loom/packets/critique/20260422T091030Z-ticket-vairivh8-protocol-hardening-review.md-10-mode: review
```

# Supports Claims

- `initiative:skills-corpus-council-precision-pass#OBJ-007`
- `ticket:revtgt7x#ACC-001`
- `ticket:revtgt7x#ACC-002`
- `ticket:revtgt7x#ACC-003`
- `ticket:revtgt7x#ACC-004`
- `critique:review-target-shape-review#REVTGT7X-CRIT-001` repair observation

# Challenges Claims

None - the observations did not falsify the targeted acceptance claims.

# Environment

Commit: b7c076f5105c2c241ac3b7ec932eb6f8a165c86f
Branch: main
Runtime: Markdown record/template edits with shell validation
OS: darwin
Relevant config: none

# Validity

Valid for: current working tree diff for `ticket:revtgt7x` implementation and repair prior to mandatory re-critique.
Recheck when: critique/frontmatter templates or guidance change again.

# Limitations

This evidence records structural search output and whitespace validation. It does
not replace the mandatory oracle critique for `records-grammar` and
`operator-clarity`, and it does not close `ticket:revtgt7x`.

# Result

The after-state search shows explicit scalar direct-critique grammar,
structured critique-packet grammar, and a concise legacy compatibility boundary
for older consumed critique packets with `kind` plus `diff` only. Targeted
historical observation confirms the named older packets are consumed and use that
legacy shape. `git diff --check` passed with no output.

# Interpretation

The observations support ACC-001 through ACC-004 and the targeted repair for
`REVTGT7X-CRIT-001` pending mandatory re-critique. They do not by themselves
prove ACC-005 or ticket closure readiness.

# Related Records

- `ticket:revtgt7x`
- `packet:ralph-ticket-revtgt7x-20260502T201800Z`
- `packet:ralph-ticket-revtgt7x-20260502T202813Z`
