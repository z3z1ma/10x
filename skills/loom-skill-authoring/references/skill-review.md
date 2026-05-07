# Skill Review

Use skill review when a skill change affects how future agents route, execute,
verify, critique, accept, or close work.

Skill review is not a new layer. It routes through evidence and critique when the
change deserves durable support or pressure-testing.

## Review Questions

Ask:

- does the skill own one coherent subsystem or workflow route
- does it duplicate an existing owner skill
- does the description name broad ordinary activation triggers, aliases, and
  common coding-task phrases without becoming a shortcut for the full workflow
- does the skill body say what it owns and does not own
- are references immediate vs conditional for a reason
- are templates present only when the skill owns an artifact shape
- does the skill preserve Loom's owner-layer boundaries
- does it depend on a hidden runtime, helper, command wrapper, or harness feature
  as the true source of behavior
- does the skill include red flags or common rationalizations when agents are
  likely to skip the discipline under pressure
- does verification require evidence rather than a feeling that the prose reads well

## Pressure Scenarios

Use pressure scenarios when a skill enforces discipline that agents may skip under
pressure, such as test-first work, verification before completion, root-cause
debugging, critique gates, or destructive-operation confirmation.

A useful pressure scenario combines realistic temptations:

- time pressure
- sunk cost
- a tempting shortcut
- authority or social pressure
- fatigue or desire to finish
- ambiguity about whether the rule applies

The scenario should force a concrete choice. Record whether the skill makes the
correct choice obvious enough without adding a hidden runtime.

Prefer direct prompt-shaped scenarios over academic questions. Good scenarios look
like real user pressure: "skip formalities and just start", "I already know what
this means", "the tests are failing; fix it fast", or "the child said done". The
review should check whether the skill causes the agent to load the right owner
route, ask the right blocker, or refuse the shortcut.

Baseline testing without the skill is useful when proportional because it reveals
the exact rationalization to close. It is not a new required harness; structural
review plus a written pressure scenario is honest for small edits when no live
agent trial was run.

For substantial skill changes, use a red/green/refactor pressure pass when
proportional:

- RED: write one prompt-shaped scenario where the current skill would likely let
  an agent skip the intended discipline or route to the wrong owner
- GREEN: edit the smallest skill surface that makes the correct choice obvious
- REFACTOR: remove duplicate wording, hidden runtime assumptions, or over-broad
  activation introduced while fixing the scenario

This is a review method, not a required test harness or new record kind. Preserve
the scenario in evidence or critique only when the ticket needs durable support.

## Evidence And Critique

For low-risk skill edits, a diff review and targeted `rg` check may be enough.

For medium or high-risk skill edits, create or update critique when the review
should persist. Create evidence when validation output, pressure-scenario results,
or structural checks should remain citable by a ticket or future critique.

Do not claim a skill is proven because it reads well. Claim only what was
actually validated.

## Common Findings

- activation too broad, causing ceremony or skill spam
- activation too narrow, causing missed routing
- body repeats doctrine that belongs in bootstrap
- workflow creates a shadow ledger outside tickets or owner records
- reference is mandatory even though only rare users need it
- template permits placeholder IDs or vague completion claims
- skill tells agents to skip critique, evidence, or ticket reconciliation
- skill reads as a reference article but does not tell the agent what to do
- skill has no anti-rationalization guidance for a discipline agents commonly skip
- skill change is accepted because the prose sounds good, without a structural
  check, pressure scenario, evidence record, or critique proportionate to the risk
