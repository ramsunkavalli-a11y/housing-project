# First investigation: names, boundaries, and cross streets

Status: record-level comparison and mapped cross-street checks performed on 2026-09-27. Read the [findings](neighborhood-findings.md) and [evidence](neighborhood-evidence.md). Local usefulness review, owner discussion, and source adoption remain pending.

## Purpose

Determine whether available sources can give a home seeker a recognizable place name and a useful area to explore. Do this before choosing a national dataset or building a matching engine.

## Proposed sample

These are research examples, not approved launch markets or claims about anyone's residence. They can be changed if another place would make local review easier.

| Place | Suggested area to inspect | Why include it? |
|---|---|---|
| Los Angeles, California | Los Feliz and Sherman Oaks | Compare familiar neighborhood names, larger boundaries, and smaller exploration areas. |
| Pasadena, California | Bungalow Heaven and adjacent streets | Inspect a recognizable local name and differences between neighborhood, historic-district, and municipal definitions. |
| Chicago, Illinois | Lincoln Square and nearby named areas | Check how neighborhood names relate to larger official community areas. |
| Ames, Iowa | City-wide name and boundary inventory first | Test coverage outside the large-city focus of CDND. Do not assume neighborhood records exist. |

## Steps

1. **Gather small extracts.** Inspect Zillow's archive, Who's On First, CDND, and Overture/OpenStreetMap where each has records. Record source IDs, release dates, geometry type, links, and terms. Record absence explicitly.
2. **Compare the places.** Do names and aliases make sense? Is the outline a neighborhood, a planning area, a historic district, or an association boundary? Are there gaps, duplicates, overlaps, or point-only records?
3. **Inspect cross streets.** Select two or three candidate exploration points per covered neighborhood. Verify that the streets physically connect, the label is unambiguous, and the point has a useful relationship to the area. Do not turn a highway overpass into an intersection or assume a geometric center is a good starting point.
4. **Show simple examples.** Present a neighborhood name, alternative names if needed, a map outline or clearly labeled approximate area, suggested cross streets, and a short explanation of what the outline means.
5. **Review with local knowledge.** Ask whether the names and suggested starting points are useful. Local feedback supplements source evidence; it does not automatically settle every disputed boundary.
6. **Recommend a source strategy.** Explain the strongest source for each role, the gaps, maintenance effort, and reuse limitations. Discuss this before adopting it for implementation.

## Comparison worksheet

Create one row for each source/place pair. Use `not inspected`, `not found in this release`, and `uncertain` instead of filling gaps with guesses.

| Place | Source / record ID / release | Names and aliases | Point or boundary? | Boundary purpose | Useful cross streets | Gaps or disagreement | Reuse terms verified? | Assessment |
|---|---|---|---|---|---|---|---|---|
| Results | See the linked findings, evidence tables, and inspection manifest. | | | | | | | |

Possible assessments: usable as-is; usable with explanation; names only; needs local correction; unsupported. These are qualitative research judgments, not an invented accuracy score.

## What counts as complete?

- Each sample place has an inspection result, including explicit gaps.
- The report distinguishes neighborhood-name coverage from polygon coverage.
- Examples show how cross streets clarify an area without pretending to define its entire boundary.
- Source provenance, dates, and applicable reuse terms are recorded; unresolved terms stay unresolved.
- A recommendation explains which roles each source should fill and what remains uncertain.

This small sample can expose failures and guide a pilot. It cannot establish nationwide completeness or accuracy.

## Presentation example — fictional

**Maplewood, Example City**

Start exploring around **Oak Street & Third Avenue**.

This marks a starting point within the area under consideration. The neighborhood outline comes from a named source; any walking-access area is a separate calculation. Actual homes may differ in commute, noise, school assignment, and access.

Do not display fine-grained claims just because the map has fine-grained points. A neighborhood-wide housing statistic remains a neighborhood-wide statistic.
