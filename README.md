# Housing Project

Help an individual, couple, or group find places to consider for a new home through useful questions, understandable evidence, and honest tradeoffs.

**Current stage: research and component planning.** Start with the buyer's decision, then select evidence that can change their shortlist. Census plus Overture/OSM remains a source proposal; no application architecture has been selected.

## Start here

**Start here: [the buyer decisions the tool must support](docs/buyer-decisions.md).** Suitable homes and total cost, regular trips, everyday conveniences, surroundings, dealbreakers, and specific places to explore. Every proposed data field must earn its place by supporting one of these decisions.

**Research checkpoint: [Granada Hills and Ames](docs/worked-area-profiles.md).** The source audit provides background but leaves important buyer questions unanswered. Detailed housing statistics remain in the [methods](docs/worked-area-methods.md); they are not the proposed result page.

New research: [what to collect and how to use it](docs/homebuyer-data-review.md), with a [16-component inventory](docs/homebuyer-data-inventory.md), [28-source catalog](docs/homebuyer-data-sources.md), and [literature notes](docs/homebuyer-literature.md). Start broad, then narrow by usefulness to homebuyers.

1. [Simple plan](PLAN.md) — the order of work and what each component must explain.
2. [Decisions](DECISIONS.md) — agreed preferences, proposals, and unresolved choices.
3. [Neighborhood findings](docs/neighborhood-findings.md) — actual records, a boundary comparison, and the proposal to review next.
4. [Evidence and methods](docs/neighborhood-evidence.md) — source IDs, licenses, calculated areas, and cross-street checks.
5. [Neighborhood sources and literature](docs/neighborhood-sources.md) — the broader resource survey.

## Product principles

- Explain each component before committing to major implementation decisions.
- Complex data is acceptable; the explanation to a home seeker should be simple.
- Collect a field only when its buyer question and potential effect on the shortlist are clear. Availability alone is not a reason to collect or display it.
- Use named neighborhoods and cross streets to make recommendations actionable.
- Distinguish hard requirements from preferences and missing evidence.
- A group may have no shared fit. Explain the conflict instead of forcing a recommendation.
- Aim for a useful first release; state its coverage and limitations honestly.
- Eventually serve both people and AI agents using consistent evidence and calculations.
- Explore revenue after establishing usefulness; no business model has been chosen.

## How work progresses

Research → a concrete example → discuss the tradeoffs → record the decision → implement that agreed component.

The neighborhood comparison, literature sweep, and initial source audit are documented. The owner has corrected the emphasis toward practical buyer decisions. The next proposed component review is whether someone can find a suitable home within their budget, including what free evidence can and cannot establish. Local review and some reuse questions remain open. The [neighborhood investigation plan](docs/neighborhood-comparison.md) records the earlier scope; research does not commit the project to a provider, nationwide launch, or technology stack.

This public repository contains project planning and public research. Personal house-hunt records, household finances, private addresses, and credentials do not belong here.
