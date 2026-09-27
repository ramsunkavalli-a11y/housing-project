# A broad, free starting point

Updated 2026-09-27.

**Owner's direction:** start with comprehensive coverage and free data; accept imperfections. This sets the priority. The source combination below is the recommendation for discussion, not an implemented system or a claim that the owner selected specific providers.

## Recommended foundation

| Role | Starting source | What it gives us | Imperfection to accept |
|---|---|---|---|
| Cover the country with defined areas | U.S. Census TIGER/Line geography | Nationwide statistical geography, with identifiers for joining compatible Census statistics. | Census areas are not necessarily recognizable neighborhoods. Small-area statistics may be uncertain or unavailable. |
| Give areas recognizable names | Overture divisions, primarily sourced from OpenStreetMap | Cities, towns, available neighborhood names, points, and some outlines. | Neighborhood coverage is uneven; names and outlines can be absent or describe different kinds of areas. |
| Give people a concrete place to explore | Overture/OSM street data | Street names and mapped connections for candidate cross streets. | A map connection does not establish that a place is a useful or pleasant starting point. |

Census block groups are a candidate working unit; the choice between block groups, tracts, or a combination belongs in the next component alongside the statistics we need. Match boundary vintages to the corresponding statistical release. Do not assume that the newest map matches every table.

This provides broad geographic coverage without requiring a complete national catalog of named neighborhoods. It does not establish complete housing-market, commute, or amenity data.

## What a person would see

When supported by the evidence: **“Los Feliz, Los Angeles — around Vermont & Franklin.”**

When a neighborhood name is unavailable: **“An area in [town], around [verified cross streets].”** Do not claim a neighborhood name or draw an invented neighborhood outline. If no useful street anchor is available, show the broader place and the limitation.

Statistics retain their actual measurement area. Merely intersecting a Census area with a neighborhood does not make all its statistics neighborhood-specific. Geographic coverage also does not imply enough evidence to recommend a location.

## Keep the first version manageable

Use this combination as the working recommendation. Keep Zillow, WOF, CDND, and local sources as possible later improvements where a demonstrated gap matters. Avoid requiring a hand-curated national merge before testing usefulness.

“Free” means no purchase price for these source datasets. Storage, processing, hosting, and any paid routing/geocoding service can still cost money. Overture divisions and transportation carry ODbL terms and attribution requirements; a free source is not an unrestricted redistribution grant. Use downloadable data with a planned refresh process rather than assuming public demonstration APIs are a production backend.

## Next component

Identify the first useful neighborhood characteristics, the free evidence available for each, and the geographic detail it can honestly support. Then settle the measurement unit and show a worked example before building a national ingestion pipeline.

## Sources

- [Census TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html): boundaries and geographic identifiers; demographic data must be joined separately.
- [Census block-group series metadata](https://catalog.data.gov/dataset/series-information-for-block-group-state-based-tiger-line-shapefiles-current): nationwide geographic coverage and stated CC0 license.
- [Overture divisions guide](https://docs.overturemaps.org/guides/divisions/): free downloads, points versus areas, and explicitly uneven sub-county coverage.
- [Overture attribution and licensing](https://docs.overturemaps.org/attribution/): terms for each theme.
- [Our inspected examples](neighborhood-findings.md): concrete evidence of differences and gaps.
