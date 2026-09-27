# Simple project plan

Updated: 2026-09-27

**Now: Component 2 — select evidence around practical buyer decisions.** The owner rejected the detached-home-percentage emphasis and agreed that every collected field needs a buyer question and a plausible effect on the shortlist. Start with the [buyer-decision outline](docs/buyer-decisions.md). Geography implementation decisions remain open.

Starting priority agreed: **broad coverage, free source data, acceptable imperfections**. The [working recommendation](docs/free-starting-point.md) is Census geography plus Overture/OSM names and streets. The [home-and-budget component](docs/home-and-budget.md) now defines a proposed useful answer and its evidence gaps. Review that scope before selecting sources or building ingestion.

| Order | Component | Question to settle | Reviewable result before implementation |
|---|---|---|---|
| 1 | Neighborhood identity | What place are we recommending, and where should someone start exploring? | Compare names, boundaries, and cross streets in several sample places. |
| 2 | Data and evidence | Which buyer decision could this evidence change, and can we support that conclusion? | Buyer question → decision → required evidence → understandable answer and remaining gaps. Include source quality and cost. |
| 3 | Questions | Which answer would meaningfully narrow or change the suggestions? | A short branching interview illustrated with fictional users; no fixed question count assumed. |
| 4 | Individual and group decisions | How do requirements, preferences, disagreements, and no-fit outcomes work? | Worked examples of a good fit, a compromise, a true conflict, and insufficient data. |
| 5 | Affordability and commute | How do we estimate feasible costs and travel to actual destinations? | Transparent examples showing assumptions, ranges, and what needs address-level checking. |
| 6 | Results and human review | Can someone understand why an area fits and what to verify in person? | A sample shortlist with reasons, limitations, cross streets, and a visit checklist. |
| 7 | Website and agent access | How can people and agents ask the same questions and receive consistent answers? | A proposed user journey and example request/response, with data-sharing rights checked. |
| 8 | Traction and revenue | Does the tool help enough that people return, share, or pay? | One small launch experiment, a success measure, and a proposed revenue test. |

## First checklist

- [x] Record the product principles and separate agreements from proposals.
- [x] Inspect Urban Stats's neighborhood source and survey alternative resources.
- [x] Write a small, reproducible neighborhood-comparison plan.
- [x] Inspect usable records and boundaries for the sample places.
- [x] Compare names, geographic extent, gaps, and mapped cross-street connections: [findings](docs/neighborhood-findings.md).
- [x] Document applicable source terms and unresolved questions for these research outputs: [evidence](docs/neighborhood-evidence.md).
- [x] Prepare the comparison and proposed source strategy for review.
- [ ] Review names and the usefulness of candidate cross streets with local knowledge.
- [ ] Discuss the source strategy and the meaning of a recommendation with the owner.
- [ ] Resolve remaining reuse questions for the proposed product, including Zillow if selected.
- [ ] Record the agreed strategy, including how to handle uncovered areas.
- [x] Begin Component 2 research at the owner's request, without treating open geography choices as approved.

## Component 2 checklist

- [x] Review residential-choice literature, buyer surveys, and measurement guidance: [literature notes](docs/homebuyer-literature.md).
- [x] Assemble a broad buyer-relevant [candidate inventory](docs/homebuyer-data-inventory.md) before narrowing it.
- [x] Identify free-source candidates, access methods, geographic limitations, and unresolved terms: [source catalog](docs/homebuyer-data-sources.md).
- [x] Explain how raw observations become useful comparisons: [review](docs/homebuyer-data-review.md).
- [x] Proceed with a worked example at the owner's request; use Granada Hills instead of Los Feliz, with Ames as the comparison.
- [x] Audit nine ACS tables and selected EPA fields/geographies for these two examples, documenting dates, uncertainties, and reuse conditions.
- [x] Produce [worked profiles](docs/worked-area-profiles.md) and [methods](docs/worked-area-methods.md), including a smaller-area sensitivity check. Both examples are built-up settings; rural generalization remains untested.
- [x] Record the owner's correction: practical buyer decisions lead; detached-home share is not a default headline or filter.
- [x] Reframe the examples and add a buyer-question-to-evidence outline.
- [x] Prepare the home-and-budget explanation: conditional questions, monthly/cash checks, source review and verified fictional example.
- [ ] Discuss the proposed rough area screening and optional candidate-home cost check with the owner.
- [ ] Select a collection batch and measurement geography based on that evidence.

The broad inventory is not a commitment to collect or score every candidate. The worked examples add small public extracts and a calculation script, not a national ingestion service or application.

## For every component

Keep the explanation short: what it does, the main options, one realistic example, the recommendation and its tradeoff, and what is still unknown. Record meaningful decisions in [DECISIONS.md](DECISIONS.md). Routine research and document maintenance can proceed while larger product decisions remain open.

## Not selected yet

Data provider, launch geography, question count, matching formula, map service, database, hosting, framework, payment model, and public launch date.
