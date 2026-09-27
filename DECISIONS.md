# Decisions and open questions

Updated: 2026-09-27

An agreed preference is not necessarily a completed implementation. A proposal is not an approved decision.

## Agreed direction

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

## Proposals to investigate

The owner authorized working through the home-and-budget component. Its [reviewable proposal](docs/home-and-budget.md) separates a household's price/cash scenarios from evidence that suitable homes exist in an area. The proposed first scope is rough area affordability screening plus an optional candidate-home cost check. The fictional scenario, question sequence, defaults and market providers are not approved production choices.

The [Component 2 research sweep](docs/homebuyer-data-review.md) proposes 16 buyer-relevant components and catalogs 28 source entries, including local-source categories and private household inputs. Actual ingestion, feature selection, scoring, and measurement units remain open. Documentation review is not a completed data-coverage audit.

The [Granada Hills/Ames source exercise](docs/worked-area-profiles.md) inspects nine ACS tables, selected EPA records, source boundaries and two public-library locations. Following owner feedback, its statistics are treated as background; the page now shows which practical buyer questions remain unanswered. The [buyer-decision outline](docs/buyer-decisions.md) proposes how to select useful evidence. Its detailed question sequence and collection priorities remain proposals; no filtering thresholds or national source strategy are adopted.

Current working recommendation: [Census geography plus Overture/OSM names and streets](docs/free-starting-point.md). Census provides the nationwide geographic foundation; neighborhood-name coverage remains incomplete. Specific providers and the measurement unit are recommendations, not recorded owner selections.

- Use neighborhood names for recognition and cross streets for specific exploration areas.
- Compare Who's On First and city-defined boundaries with Zillow; inspect Overture/OpenStreetMap for names, boundaries, and street connections.
- Treat Urban Stats as a reference for statistics and presentation. Its neighborhood layer uses archived Zillow data, so it is not an independent boundary source.
- Preserve disagreements between credible sources rather than silently treating one boundary as universally correct.
- Use smaller geographic units for measurement when appropriate; explain the area each measurement describes.

## Open decisions

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
