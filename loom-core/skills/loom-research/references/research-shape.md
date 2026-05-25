# Research Shape

Research creation is outer-loop work. Create research when a question and its
reasoning are durable enough that future work would be worse without the record.

## Readiness

Create an `active` research record only when:

- the question is clear enough to investigate
- scope is narrow enough to avoid a parking lot
- likely sources, method, experiment, or inspection path are known
- likely downstream consumer is known
- the investigation, rejection, null result, or conclusion should remain available

If not, keep shaping or route to the owning surface.

## Route Elsewhere

Research informs other surfaces. It does not replace them.

Route intended behavior to specs, executable work to tickets, multi-ticket
strategy to plans, durable judgment to constitution, observations to evidence,
adversarial review to audit, and accepted reusable explanation to knowledge.

## Core Sections

Use these unless the record has a strong reason to vary:

- `## Summary`
- `## Question`
- `## Scope`
- `## Method And Sources`
- `## Findings`
- `## Tradeoffs`
- `## Rejected Paths And Null Results`
- `## Conclusions`
- `## Recommendations`
- `## Open Questions`
- `## Related Records`

Research does not use a journal by default. Fold material history into Method,
Findings, Rejected Paths, or Conclusions.

## Section Duties

Summary names what was investigated, why it matters, and the most important
current conclusion or state.

Question names the decision pressure clearly enough to know when the record is
done.

Scope says what is covered and excluded: paths, records, systems, versions,
environments, options, assumptions, and freshness or recheck triggers when they
matter.

Method And Sources explains code inspection, record review, commands,
experiments, external docs, artifacts, operator input, model debate, or peer
comparison. Add provenance or freshness only when it affects trust.

Findings are observed or sourced facts before interpretation. Cite or create
evidence when an observation must survive independently.

Tradeoffs compare meaningful options, strengths, risks, limits, and downstream
consequences. Remove the section if no real comparison exists.

Rejected Paths And Null Results capture dead ends future agents would otherwise
rediscover.

Conclusions state only what the findings justify. Name confidence, assumptions,
versions, environment limits, and recheck triggers when relevant. `completed`
means conclusions are bounded enough to cite; it does not make another surface
accept them.

Recommendations name the next owner: spec, ticket, plan, constitution, evidence,
audit, or knowledge.

Open Questions are honest limits, not a parking lot.

Related Records lists only records or paths that materially constrain or explain
the research.

## Spike, Sketch, Experiment

A spike, sketch, prototype, or experiment belongs in research when its durable
product is a conclusion, comparison, rejection, or null result. Preserve the
question, method, artifact pointers, findings, limits, and downstream route. Omit
throwaway implementation steps.
