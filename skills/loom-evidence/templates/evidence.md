---
id: evidence:<slug>
kind: evidence
status: recorded
created_at: <UTC timestamp>
updated_at: <UTC timestamp>
scope:
  kind: repository
  repositories:
    - repo:root
links: {}
external_refs: {}
---

# Summary

What was observed, why this record exists, and which claims it supports or challenges.
Evidence records observations; they do not decide acceptance, closure, policy, or critique verdicts.

# Procedure

Observed at: <UTC timestamp>
Source state: <commit / branch / relevant record versions / external source version>
Procedure: <commands, manual inspection steps, query, screenshot, or capture method>
Expected result when applicable: <expected behavior, output, state, or artifact>
Actual observed result: <observed behavior, output, state, artifact, mismatch, or inconclusive result>
Procedure verdict / exit code: <pass/fail/mixed/inconclusive and exit code when applicable>

# Artifacts

Files, outputs, screenshots, logs, commands, paths, or observations that matter.
Separate raw observations from later interpretation.

# Visual / Product Evidence

Use for UI, UX, product-shape, or design-quality claims; otherwise write `N/A`.

- Baseline artifact:
- After artifact:
- Viewport / environment:
- Primary user task checked:
- What improved:
- What still looks weak:
- What this evidence does not prove:

# Supports Claims

List stable claim or acceptance IDs this evidence supports. For partial support,
name the observed portion and the untested or limited portion. If none apply,
write `None - reason`.

# Challenges Claims

List stable claim or acceptance IDs this evidence weakens or falsifies. If none
apply, write `None - reason`.

# Environment

Commit:
Branch:
Runtime:
OS:
Relevant config:
External service / harness / data source when applicable:

# Validity

Valid for: <claims, source state, and environment this observation can speak to>
Fresh enough for: <claims or review questions; not acceptance or closure>
Recheck when: <source, records, dependencies, environment, procedure, or scope changes>
Invalidated by: <conditions that would make this observation unreliable>
Supersedes / superseded by:

# Limitations

What this evidence does not establish, including untested scenarios,
environments, source states, adjacent claims, or critique questions.

# Result

The observed result in plain language, including expected-versus-actual mismatch when applicable.

# Interpretation

The limited inference justified by the observation, and the conclusion that is
not justified by this evidence alone.

# Related Records

Relevant ticket, spec, plan, research, initiative, decision, evidence, critique,
wiki, packet, ship package, or support artifact refs.
