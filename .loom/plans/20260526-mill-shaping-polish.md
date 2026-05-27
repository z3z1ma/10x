# Shaping Sessions Production Polishing

ID: plan:20260526-mill-shaping-polish
Type: Plan
Status: open
Created: 2026-05-26
Updated: 2026-05-26
Risk: high - P0 and P1 issues mean the feature is non-functional in its current state; needs deep backend+frontend alignment work

## Summary

Adversarial audit of the shaping sessions implementation revealed critical issues
that prevent basic use. The feature was implemented as 5 tickets but never
validated end-to-end. This plan fixes all blocking issues and adds the polish
needed to differentiate this from a simple chat interface.

Issues found (from audit):

**P0 (broken, can't function):**
- Proposal/staged-record flow: schema mismatch between backend block format and
  frontend expectations, wrong API routes in ProposalCard, staged records never
  sync to frontend store

**P1 (major gaps):**
- Branch UI/schema mismatch (parser emits {id,label}, UI reads branch.name)
- Sessions can't resume after refresh (no hydration, no URL persistence)
- Exploration state invisible (events not handled in frontend)
- No-config harness path unsafe (advance crashes if no harness configured)
- Advance hides failures and returns empty on explore
- Commit git rollback incomplete

**P2 (differentiation from chat):**
- No loading/thinking UX during advance
- No progressive materialization feel
- Timeline feels like a flat message list, not a building subgraph
- Need visual richness that makes this NOT look like chat

## Related Records

- `spec:mill-shaping-sessions` - behavioral contract
- `plan:20260526-mill-shaping-sessions` - original implementation plan

## Strategy

Two parallel tracks:

**Track A (generalist):** Fix all backend issues (P0 schema alignment, P1 harness
safety, advance error handling, commit rollback, exploration events). This makes
the engine actually work end-to-end.

**Track B (frontend-expert):** Fix all frontend issues (ProposalCard API routes,
store sync, session resume, exploration indicators, branch UI, loading states).
Then do the visual differentiation pass that makes this feel novel.

## Execution Units

### Unit: Backend End-to-End Fix

Ticket: ticket:20260526-mill-shaping-backend-fix

Fix ALL backend issues in one pass:
- Align proposal block schema with what frontend expects
- Add safe harness-missing error path
- Fix advance to surface errors clearly and return blocks on explore
- Fix commit git rollback (git reset on failure)
- Publish exploration events through the standard block_added channel
- Add integration test that simulates full session lifecycle with echo harness

### Unit: Frontend End-to-End Fix + Differentiation

Ticket: ticket:20260526-mill-shaping-frontend-fix

Fix ALL frontend issues and add the visual richness that differentiates from chat:
- Fix ProposalCard API routes to match real endpoints
- Add staged record state sync (refetch or handle events)
- Add session resume on refresh (persist sessionId, hydrate from GET)
- Handle exploration_start/complete events (show indicators)
- Fix branch UI to use correct schema
- Add loading/thinking states during advance
- Add error display inline
- Visual differentiation: progressive materialization animation, richer block
  cards, clearer phase indicators, exploration visualization

## Current State

Plan created. P0 fix is critical path. Both tickets can execute in parallel since
they touch different file sets (backend vs frontend).

## Journal

- 2026-05-26: Created plan after adversarial audit. Operator confirmed basic smoke
  test fails with 400 error (now fixed) and no agent response (advance not called,
  now fixed). Deeper audit revealed schema mismatches and missing state sync.
