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
| Audience | Support home seekers and, eventually, AI agents. | Owner's stated objective. |
| Repository | Use ramsunkavalli-a11y/housing-project for project plans. | Owner supplied the repository and requested setup. |

## Proposals to investigate

- Use neighborhood names for recognition and cross streets for specific exploration areas.
- Compare Who's On First and city-defined boundaries with Zillow; inspect Overture/OpenStreetMap for names, boundaries, and street connections.
- Treat Urban Stats as a reference for statistics and presentation. Its neighborhood layer uses archived Zillow data, so it is not an independent boundary source.
- Preserve disagreements between credible sources rather than silently treating one boundary as universally correct.
- Use smaller geographic units for measurement when appropriate; explain the area each measurement describes.

## Open decisions

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
