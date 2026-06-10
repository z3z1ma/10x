# Loom Loop Failure Analysis

Status: completed
Created: 2026-05-10
Updated: 2026-05-10

## Summary

The eval failure was not a single missing sentence. The transcript shows three weak seams in the corpus: vague product work could still collapse into immediate execution, ticket slicing guidance did not force the agent to decompose a multi-outcome product pass, and fresh-context worker handoffs could bypass Ralph by embedding the whole worker contract in `task` prompts.

The strongest fix is to state the desired Loom mechanics directly across the Core surfaces and the playbooks that commonly trigger execution: shape before contract, split before ticket, packet before worker launch, then evidence and audit before closure.

## Question

Where can the current Loom corpus be interpreted in ways that allow agents to skip outer-loop shaping, create oversized tickets, or invoke subagents without on-disk Ralph packets?

## Scope

Covered:

- `using-loom` doctrine and shaping/delegation/proving references.
- Core ticket, plan, Ralph, and audit skills and references.
- Playbook surfaces activated or implicated by the eval: frontend UI, source-driven work, incremental implementation, code review, and idea refinement.
- Public protocol docs that restate Core behavior.
- The committed Dota eval records and the local OpenCode transcript for session `ses_1eac9757bffeq3eku2u7S0Za07`.

Excluded:

- Adapter preload mechanics, because the ordered Core preload files were present and the failure occurred after skill activation.
- Automated evaluator design.
- Changes to the eval app itself.

## Method And Sources

- Inspected the eval workspace records under `evals/dota2/with-loom/.loom/`.
- Queried the local OpenCode database for the session text and `task` prompts.
- Read Core `using-loom`, `loom-tickets`, `loom-plans`, `loom-ralph`, and `loom-audit` skill references.
- Read relevant playbooks: `loom-frontend-ui-engineering`, `loom-source-driven-development`, `loom-incremental-implementation`, `loom-idea-refine`, and `loom-code-review-and-quality`.
- Preserved the observed transcript and record facts in `.loom/evidence/20260510-opencode-session-loop-failures.md`.

## Findings

- The outer-loop doctrine says to shape while intent is fuzzy, but the execution-triggering playbook route can be read as `intent -> contract -> slice -> build` without making operator collaboration the entry gate for broad product-quality requests.
- The frontend playbook lists useful intent fields but does not explicitly route fuzzy product/design requests back through idea refinement or Core shaping before writing specs and tickets.
- Ticket guidance requires "one bounded executable work unit," but the creation references do not give a sharp enough single-closure-claim test for product work that combines stack, data, UI shell, deep analytics, and verification.
- Plan slicing guidance says plans produce child tickets, but it can be strengthened to make child-ticket creation part of the saved plan, not a later execution convenience.
- Ralph guidance describes packet mechanics, but the launcher path does not make the packet file the worker contract before invoking a harness-native subagent.
- Audit correctly requires fresh context and says to route through Ralph, but it does not explicitly say the bounded audit request should be a packet under `.loom/packets/ralph/` that the subagent is pointed at.
- Public docs describe Ralph and audit accurately at a high level, but they do not state the operational packet-before-worker rule as the inner-loop spine.

## Conclusions

- Strengthen Core before playbooks. `using-loom` should make Core routing and playbook composition explicit, so a playbook cannot be read as permission to compress unresolved outer-loop work into execution.
- Strengthen shaping as positive readiness language. Broad adjectives such as "novel," "production feel," "polished," and "whole thing" should lead to operator-shaped direction, quality bar, non-goals, evidence posture, and ticket boundary before implementation.
- Strengthen slicing around closure claims. One ticket should have one bounded closure story; if the work has independent stack, data, UI, feature, review, or verification outcomes, the plan should split them into child tickets before execution.
- Strengthen Ralph around launch mechanics. A Loom worker run should be packet file plus launch; the wrapper prompt should point to the packet path instead of carrying the full work contract.
- Strengthen audit around Ralph. Fresh-context audit should be prepared as a review packet and then recorded as an audit after the worker returns.

## Recommendations

- Update Core `using-loom` references for shaping and delegation.
- Update `loom-tickets` and `loom-plans` slicing references and templates.
- Update `loom-ralph` and `loom-audit` launcher/request guidance.
- Update frontend/source/incremental/review playbooks where they can trigger work or worker handoff.
- Align README, PROTOCOL, ARCHITECTURE, and package READMEs with the packet-before-worker and shape-before-slice posture.

## Related Records

- `.loom/evidence/20260510-opencode-session-loop-failures.md` - observed source for this analysis.
- `.loom/tickets/20260510-core-loop-hardening.md` - implementation plan consuming this research.
