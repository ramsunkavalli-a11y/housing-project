# Neighborhood resources and literature

Reviewed: 2026-09-27. Targeted desk research, not a systematic literature review or an empirical nationwide coverage audit. Counts below are provider or paper claims and use different definitions.

## Source shortlist

| Source | Verified finding | Candidate role | Unresolved issue |
|---|---|---|---|
| [Zillow archive via EPA](https://catalog.data.gov/dataset/neighborhoods-us-2017-zillow-segs) | Approximately 17,000 neighborhoods in more than 650 cities; dataset dated 2017. | Historical baseline and comparison. | Age, current local accuracy, and original reuse terms. A recent catalog check is not a refreshed boundary dataset. |
| [City-Defined Neighborhood Dataset, 2025](https://www.nature.com/articles/s41597-025-05329-6) | Reports 20,635 neighborhoods in 206 cities; cleaned geographic files and Census-block connections. Includes neighborhood association/council definitions; separately releases HOA files. Inspected dataset version 1 is marked CC0 1.0. | Locally sourced boundaries. | Geographic gaps, differences in scale and purpose, and source-specific cleanup. The sample found unusable name values in one LA file and numeric community codes in Chicago. |
| [Who's On First](https://whosonfirst.org/download/) | Downloadable place records, names, hierarchies, and point or polygon geometries, including alternate geometries. | Neighborhood identity and broader name catalog. | Source age, point-only records, local coverage, and attribution requirements. |
| [Overture divisions](https://docs.overturemaps.org/guides/divisions/) | Separate place points, area polygons, and boundary lines; includes neighborhood subtypes. | Names and available boundaries with source metadata. | Actual U.S. neighborhood coverage; a point record does not guarantee an area polygon. |
| [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Tag:place%3Dneighbourhood) | Neighborhoods can be points or areas; guidance favors points when borders are unclear. | Local names, street/path detail, and supporting features. | Uneven completeness and ambiguous boundaries. |
| [Local government data](https://www.nyc.gov/site/doh/health/neighborhood-health/nyc-neighborhood-health-atlas.page) | Governments publish geographic units for different purposes; NYC NTAs are statistical areas assembled from tracts. | City-specific corroboration and improvements. | Official does not necessarily mean the same area a home seeker has in mind. |
| [Simplemaps](https://simplemaps.com/data/us-neighborhoods) | Advertises 31,896 entries in 738 cities; polygons for over 29,000 neighborhoods in 293 cities. Free tier lacks polygons; polygon package listed at $2,999. | Packaged paid comparison option. | Counts and prices can change; paid license prohibits public database redistribution. Agent-facing use needs checking. |
| [Precisely](https://www.precisely.com/data-guide/products/neighborhood-boundaries/), [ATTOM](https://cloud-help.attomdata.com/article/478-boundary), [LiveBy](https://liveby.com/) | Providers offer commercial neighborhood/boundary products. | Later alternatives if open-data maintenance is too costly. | Suitable coverage, pricing, and contract rights not verified. |

CDND download reference: [Harvard Dataverse DOI](https://doi.org/10.7910/DVN/02NP1O). Follow-up inspection verified the dataset's stated CC0 1.0 license in version 1 metadata. See the [record-level evidence](neighborhood-evidence.md) for inspected files, dates, source-specific reuse terms, and unresolved Zillow metadata.

## Urban Stats: useful reference, same Zillow boundary source

The [Urban Stats neighborhood definition](https://github.com/kavigupta/urbanstats/blob/8725a3c586ce557d724a8faa7f8cfd8d03191585/urbanstats/geometry/shapefiles/shapefiles/neighborhoods.py) explicitly loads Zillow's neighborhood shapefile and credits the 2017 EPA archive. It is not an independent replacement boundary dataset.

Its value for this project is the approach to calculating and presenting statistics, organizing geography, and recording source credits. For example, its [housing-age calculation](https://github.com/kavigupta/urbanstats/blob/8725a3c586ce557d724a8faa7f8cfd8d03191585/urbanstats/statistics/collections/housing_year_built.py) uses ACS categories. This code inspection does not validate every calculation or establish a supported public data API.

The repository carries an [AGPL-3.0 code license](https://github.com/kavigupta/urbanstats/blob/8725a3c586ce557d724a8faa7f8cfd8d03191585/LICENSE). Code reuse, source-data reuse, and access to its hosted service are separate questions.

## Literature and product implications

| Research | Finding or contribution | Implication for this project |
|---|---|---|
| [Coulton et al., 2001 — Mapping Residents' Perceptions of Neighborhood Boundaries](https://onlinelibrary.wiley.com/doi/pdf/10.1023/A%3A1010303419034) | Resident-drawn neighborhoods differed from Census-defined areas and produced different social indicators. Pilot study. | Do not equate a Census tract with a locally recognized neighborhood. |
| [Ansolabehere et al., 2025 — City-Defined Neighborhood Boundaries in the United States](https://www.nature.com/articles/s41597-025-05329-6) | Collects municipal definitions at scale and compares them with Census-based proxies. | A city-sourced alternative exists, but its units still vary in scale and purpose. |
| [Measuring and Modeling Neighborhoods, 2024](https://www.cambridge.org/core/journals/american-political-science-review/article/measuring-and-modeling-neighborhoods/13D284E0CF76458F597B70F2242C23EA) | Uses map-drawing surveys in Miami, New York City, and Phoenix to model subjective neighborhoods. | Allow alternative names and uncertainty rather than treating all boundaries as universal. |
| [Bae, Wileden and Talen, 2024 — Chicago resident drawings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.COSIT.2024.26) | Crowdsourced over 5,000 responses about Chicago neighborhoods. | Local contributions are feasible, but sampling and verification matter. |
| [Visokay et al., preprint revised 2026 — Neighborhood claims in Craigslist ads](https://arxiv.org/abs/2506.00634) | Chicago listings show conflicting definitions, border ambiguity, and claims to distant desirable neighborhoods. | Listing language can suggest aliases but should not alone determine geography. |

These studies support careful geographic modeling. They do not validate this product, a specific matching formula, or the claim that cross-street recommendations improve home-buying outcomes.

## Cross streets

[Overture transportation](https://docs.overturemaps.org/guides/transportation/) provides roads and connection points and documents intersection-geocoding use. Its [connectivity rules](https://docs.overturemaps.org/guides/transportation/segments-and-connectors/) distinguish connected roads from lines that merely cross on a map. [OSMnx](https://osmnx.readthedocs.io/en/stable/) is another resource for working with OpenStreetMap street networks.

Proposed interpretation: a cross-street pair is a specific exploration anchor. A neighborhood outline, a walking-access area, and an individual home's surroundings are distinct geographic objects. Do not imply that one anchor represents every property.

## Reuse checks before adoption

Consult [Who's On First licenses](https://www.whosonfirst.org/docs/licenses/), [Overture attribution and licenses](https://docs.overturemaps.org/attribution/), and [Simplemaps terms](https://simplemaps.com/data/license). Overture divisions and transportation use ODbL. Check the exact releases and intended display, caching, download, and agent-response behavior. An openly accessible file or GitHub repository is not by itself a blanket commercial-use grant.

## Provisional recommendation

Compare Who's On First and CDND for names and boundaries; Overture/OpenStreetMap for geographic and street detail; Zillow as a baseline; and Urban Stats as a statistics reference. Choose a strategy only after the [sample comparison](neighborhood-comparison.md), local review, and applicable terms checks.
