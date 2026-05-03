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

What was observed, why it exists, and which claims it supports or challenges.
Do not claim acceptance, closure, critique verdicts, or intended behavior here.

# Procedure

Observed at: <UTC timestamp>
Source state: <commit / branch / relevant record versions / external source version>
Procedure: <commands, manual inspection steps, query, or capture method>
Procedure verdict / exit code: <observed pass/fail/mixed/inconclusive and exit code when applicable>

Include enough context for a future agent to judge freshness without treating this
record as an acceptance decision.

# Artifacts

List files, outputs, screenshots, logs, commands, or observations that matter.
Keep observed artifacts separate from later inference. Link to, name, or excerpt
raw logs when that is enough; full raw logs do not need to be stored inline in
every evidence record.

# Supports Claims

List stable claim or acceptance IDs this evidence supports.

If none apply, write `None - reason`.

# Challenges Claims

List stable claim or acceptance IDs this evidence weakens or falsifies.

If none apply, write `None - reason`.

# Environment

Commit:
Branch:
Runtime:
OS:
Relevant config:

# Validity

Valid for: <claims, source state, and environment this observation can speak to>
Fresh enough for: <claims or review questions; not acceptance or closure>
Recheck when: <source, records, dependencies, environment, procedure, or scope changes>
Invalidated by: <conditions that would make this observation unreliable for the cited claims>
Supersedes / superseded by:

# Limitations

What this evidence does not establish.

# Result

What the evidence actually showed. This should be an observed result, not an
acceptance decision.

# Interpretation

What limited inference is justified, and what conclusion is **not** justified by
this evidence alone.

# Related Records

Link or name the ticket, critique, wiki page, plan, or spec this evidence supports.
