# Decisions and open questions

Updated: 2026-10-02

An agreed preference is not necessarily a completed implementation. A proposal is not an approved decision.

## Current direction — 2026-10-02

| Item | Direction | Origin |
|---|---|---|
| Primary objective | Focus primarily on the owner's home purchase. | Owner's explicit direction on 2026-10-02. |
| Possible later use | Consider public distribution of the model in the future; it is not the current deliverable. | Owner's stated possibility, not a launch commitment. |
| Work visibility | Work through Git so changes and progress are easy to follow. | Owner's explicit preference on 2026-10-02. |

This direction supersedes the earlier emphasis on a broad first release, national collection, and traction. Earlier research and still-useful principles remain available; unresolved provider or implementation choices have not become approved through this change.

## Proposed purchase workflow

Use the existing private [next-house-hunt repository](https://github.com/ramsunkavalli-a11y/next-house-hunt) for household inputs, actual candidates, financing evidence, and purchase records. Keep reusable methods, public research, and fictional examples here. This repository arrangement and the detailed [purchase workflow](PLAN.md) are recommendations prepared for review, not an instruction to migrate or publish private records.

Next proposed milestone: a current, evidence-supported comparison of a few realistic candidates, including total costs, cash needs, regular trips, property questions, and next actions. Existing candidate scores and listing snapshots need an evidence/freshness review before reuse. No revised weights, thresholds, provider, lender, offer, or property choice is adopted here.

Private records should settle the active purchase questions: which requirements and financial inputs are current; which homes remain viable; what evidence supports their costs and daily-life fit; and which unresolved check could change the decision. Keep the actual answers private.

## Earlier direction and continuing principles — 2026-09-27

| Item | Direction | Origin |
|---|---|---|
| Working process | Understand components before major decisions are made and built. | Owner's explicit instruction. |
| Place presentation | Favor named neighborhoods and cross streets. | Owner's stated preference. |
| Data complexity | The data layer may be complex if its presentation makes sense. | Owner's explicit instruction. |
| Group conflict | Saying the choices are too different to find a shared fit is acceptable. | Owner's explicit instruction. |
| Initial ambition | Build a useful first version and see whether it gains traction. | Owner's stated objective. |
| Starting data priority | Favor broad coverage and free data; accept documented imperfections. | Owner: “comprehensive, but free, but may not be perfect.” |
| Data inventory breadth | Start with many potentially useful components, then narrow; relevance to homebuyers is the test. | Owner's request for another literature sweep on raw data and components to collect. |
| Buyer usefulness | Collect a field only when its buyer question and potential effect on the shortlist are clear. Detached-home share is not a default headline or exclusion rule. | Owner rejected the statistics-led example and agreed to the buyer-decision principle. |
| Worked example | Use Granada Hills instead of Los Feliz; retain Ames as the comparison. | Owner's correction while the authorized worked profiles were in progress. |
| Audience | Support home seekers and, eventually, AI agents. | Owner's stated objective. |
| Repository | Use ramsunkavalli-a11y/housing-project for project plans. | Owner supplied the repository and requested setup. |

## Earlier research proposals — retained as background

The owner authorized working through the home-and-budget component. Its [reviewable proposal](docs/home-and-budget.md) separates a household's price/cash scenarios from evidence that suitable homes exist in an area. The proposed first scope is rough area affordability screening plus an optional candidate-home cost check. The fictional scenario, question sequence, defaults and market providers are not approved production choices.

The [Component 2 research sweep](docs/homebuyer-data-review.md) proposes 16 buyer-relevant components and catalogs 28 source entries, including local-source categories and private household inputs. Actual ingestion, feature selection, scoring, and measurement units remain open. Documentation review is not a completed data-coverage audit.

The [Granada Hills/Ames source exercise](docs/worked-area-profiles.md) inspects nine ACS tables, selected EPA records, source boundaries and two public-library locations. Following owner feedback, its statistics are treated as background; the page now shows which practical buyer questions remain unanswered. The [buyer-decision outline](docs/buyer-decisions.md) proposes how to select useful evidence. Its detailed question sequence and collection priorities remain proposals; no filtering thresholds or national source strategy are adopted.

Earlier working recommendation: [Census geography plus Overture/OSM names and streets](docs/free-starting-point.md). Census provides the nationwide geographic foundation; neighborhood-name coverage remains incomplete. Specific providers and the measurement unit are recommendations, not recorded owner selections.

- Use neighborhood names for recognition and cross streets for specific exploration areas.
- Compare Who's On First and city-defined boundaries with Zillow; inspect Overture/OpenStreetMap for names, boundaries, and street connections.
- Treat Urban Stats as a reference for statistics and presentation. Its neighborhood layer uses archived Zillow data, so it is not an independent boundary source.
- Preserve disagreements between credible sources rather than silently treating one boundary as universally correct.
- Use smaller geographic units for measurement when appropriate; explain the area each measurement describes.

## Deferred geography and public-product decisions

These questions are retained for future product work and do not block a local purchase comparison. Source terms must still be respected for any use now.

The [2026-09-27 sample findings](docs/neighborhood-findings.md) support a proposed separation between recognizable names, attributed outlines, exploration starting points, and measurement geography. This is evidence for discussion, not an adopted source strategy. In particular, Lincoln Square's inspected outlines range from approximately 0.53 to 6.63 km².

1. Which sources work well enough in the proposed sample places?
2. Should uncovered areas use cross-street-based exploration areas, named towns, or an explicit coverage gap?
3. Does a cross-street label represent a starting point, a walking area, or a recommended residential pocket?
4. How should we show alternate neighborhood names and uncertain boundaries?
5. What geographic coverage is enough for the first release?
6. What data may be displayed, cached, downloaded, or returned to external agents under each source's terms?

## Status distinctions to preserve

- **No shared fit:** known requirements conflict with available choices.
- **Insufficient evidence:** the data cannot establish whether a choice fits.
- **Outside coverage:** this location has not been supported or evaluated.

These outcomes must not be silently substituted for one another.

## Future decision entry

Date:

Component:

Decision and reason:

Evidence or example reviewed:

Tradeoff accepted:

What would cause us to reconsider:
