# Worked area profiles: methods and evidence

Collected 2026-09-27. Read the [buyer-question review](worked-area-profiles.md) first. This is a small source audit, not proof of nationwide coverage. Estimates below come from actual public records. Following owner feedback, these statistics are retained as background research; their inclusion does not imply a buyer-facing headline, priority or filtering rule.

## Geography and selection

The two OSM intersections were verified as shared road nodes. Their coordinates are recorded separately in [osm-anchors.json](research/worked-areas/osm-anchors.json), under ODbL. The Census coordinate lookup used `Public_AR_Current` and explicit vintage `ACS2024_Current`.

| Example | Longitude, latitude | ACS tract GEOID | ACS block-group GEOID | Selected EPA record |
|---|---|---|---|---|
| Granada Hills | -118.5234289, 34.2649105 | 06037111202 | 060371112022 | 060371112022, OBJECTID 45588 |
| Ames | -93.6122056, 42.0301687 | 19169000900 | 191690009002 | 191690009004, OBJECTID 96499 |

Queries and original-response SHA-256 values are in the [retrieval manifest](research/worked-areas/retrieval-manifest.json). Census map polygons came from `tigerWMS_ACS2024`, layer 8 (tracts) and layer 10 (block groups), with exact GEOID queries. The source-specific records and polygons are in [geographies.json](research/worked-areas/geographies.json).

For Granada Hills, EPA's exact-point spatial query returned an empty result. The rectangle `[-118.524,34.2644,-118.5228,34.2655]` returned three neighboring polygons. We retain all three and highlight the one sharing the selected ACS block-group identifier. This is a documented research selection, not a universal rule for assigning boundary points. Ames' EPA record came from a point query and has a different identifier and footprint from its newer ACS block group. No interpolation or combination of ACS and EPA counts was performed.

## ACS retrieval and definitions

The test ACS data API call returned a “Missing Key” HTML response. Public table downloads worked without registration. Each nationwide pipe-delimited file was streamed until the four target rows were found; only those rows were retained. We used the **2020–2024 five-year ACS**, not a current inventory snapshot. The directory lists the inspected files with modification dates of 2026-01-29. Each retained row includes the original text values and margin fields; API group metadata supplies field labels.

| Table | Universe / subject | What we retained |
|---|---|---|
| B25002 | Housing units | Total, occupied, vacant |
| B25003 | Occupied housing units | Owner/renter occupancy |
| B25024 | Housing units | Units in structure: detached through large buildings and other types |
| B25041 | Housing units | Bedroom categories |
| B25034 | Housing units | Construction-year categories |
| B25077 | Owner-occupied housing units | Median owner-reported value |
| B25064 | Renter-occupied units paying cash rent | Median gross rent |
| B25088 | Owner-occupied housing units | Median selected owner costs, including mortgage-status subgroups |
| B28002 | Households | Internet subscription categories, including overlapping service types |

[Official bulk directory](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/). The [extract](research/worked-areas/acs-extract.json) records each exact file and metadata URL. Value/rent/owner-cost amounts are expressed in 2024 dollars. Owner costs include the applicable mortgage, tax, insurance, utility and related components in the ACS definition; maintenance and a new buyer's loan terms are not established by these medians. Gross rent includes the applicable tenant-paid utility costs. See [ACS subject definitions](https://www.census.gov/programs-surveys/acs/technical-documentation/code-lists.html).

Internet subscription categories overlap. They must not be added together as disjoint categories. Subscription is different from availability, actual speed, service reliability, or affordability at a prospective address.

## Transformations and uncertainty

Shares use compatible counts within the same table and geography. For numerator X, denominator Y, and p = X/Y, the displayed percentage is 100p. For sums of mutually exclusive categories, approximate numerator MOE is the square root of the sum of squared component MOEs. The approximate percentage MOE is `100 × sqrt(MOE_X² − p² × MOE_Y²) / Y`; a negative radicand uses the ratio fallback with a plus sign. These are 90% approximations, not replicate-weight calculations. They omit covariance details and nonsampling error. Intervals are clipped to 0–100 for display, which does not guarantee nominal coverage near the bounds. [Census accuracy guidance](https://www2.census.gov/programs-surveys/acs/tech_docs/accuracy/MultiyearACSAccuracyofData2024.pdf) and [statistical calculation instructions](https://www.census.gov/programs-surveys/acs/technical-documentation/code-lists.html).

Example: Granada tract detached share = 1,701 / 1,990 × 100 = **85.48%**. Its input MOEs are 328 and 321; the approximation gives **9.01 percentage points**. The result is rounded to 85.5% ± 9.0 points. Published medians are copied; they are not averaged or constructed from these shares.

The Granada smaller block group's B25088 mortgage-free cost MOE is `-333333333`, an open-interval median indicator. Preserve that raw code and mark its numeric uncertainty unavailable; do not turn it into a huge negative error bar or present the median as an ordinary precise value. The derivation marks this result `median_open_interval`. [Census annotation reference](https://www.census.gov/data/developers/data-sets/acs-1year/notes-on-acs-estimate-and-annotation-values.html).

The accompanying `derive.py` recomputes 17 percentage measures and four cost/value measures for each of the four ACS areas. It is a research script for this extract, not a complete parser for all Census special values. The 212 source estimates are 53 table cells × 4 geographies; derived measures overlap and are not 21 independent scoring signals.

## Full ACS comparison

Tract columns provide larger-area background. Block groups are a locality/uncertainty check. Percentages use approximate 90% MOEs in percentage points; money uses published 90% MOEs in 2024 dollars.

| Measure | Granada tract | Ames tract | Granada block group | Ames block group |
|---|---:|---:|---:|---:|
| Detached homes | 85.5% ± 9.0 | 60.0% ± 6.5 | 93.1% ± 13.1 | 53.3% ± 22.2 |
| Attached single-unit homes | 1.2% ± 1.7 | 1.1% ± 1.2 | 0.0% ± 2.8 | 0.0% ± 2.7 |
| Units in 2â€“4-unit buildings | 1.0% ± 1.5 | 21.6% ± 6.7 | 4.0% ± 5.1 | 26.1% ± 15.6 |
| Units in buildings with 5+ units | 12.0% ± 3.6 | 16.2% ± 5.2 | 2.8% ± 4.9 | 20.5% ± 10.0 |
| Zero or one bedroom | 8.4% ± 3.7 | 13.4% ± 4.8 | 12.9% ± 9.9 | 9.9% ± 11.8 |
| Two bedrooms | 23.6% ± 5.3 | 37.4% ± 9.2 | 37.0% ± 15.1 | 45.1% ± 22.3 |
| Three bedrooms | 48.7% ± 13.9 | 31.9% ± 5.0 | 18.0% ± 7.4 | 34.7% ± 12.5 |
| Four or more bedrooms | 19.3% ± 7.6 | 17.3% ± 4.9 | 32.1% ± 23.6 | 10.4% ± 11.2 |
| Three or more bedrooms | 68.0% ± 14.2 | 49.2% ± 6.0 | 50.1% ± 21.8 | 45.1% ± 14.2 |
| Built before 1940 | 7.4% ± 3.1 | 54.6% ± 8.0 | 4.8% ± 4.3 | 40.0% ± 22.7 |
| Built 1940â€“1969 | 74.8% ± 11.9 | 23.4% ± 7.7 | 81.2% ± 24.9 | 29.1% ± 16.1 |
| Built 1970â€“1999 | 14.2% ± 5.0 | 16.5% ± 5.0 | 13.9% ± 6.4 | 27.7% ± 13.5 |
| Built 2000 or later | 3.6% ± 2.4 | 5.5% ± 3.9 | 0.0% ± 4.9 | 3.2% ± 6.2 |
| Owner-occupied share of occupied homes | 61.0% ± 14.0 | 55.6% ± 5.9 | 62.8% ± 23.7 | 47.9% ± 14.0 |
| Vacant share of housing units | 1.0% ± 1.6 | 10.2% ± 5.9 | 0.0% ± 2.8 | 22.1% ± 24.8 |
| Households subscribing to cable/fiber/DSL | 85.4% ± 11.6 | 81.0% ± 8.2 | 76.2% ± 18.8 | 76.7% ± 16.5 |
| Households with cellular-only subscriptions | 9.0% ± 5.4 | 6.5% ± 4.1 | 16.6% ± 15.8 | 4.5% ± 7.1 |
| Median owner-reported home value | $816,500 ± $48,702 | $221,300 ± $10,161 | $790,400 ± $136,789 | $225,500 ± $8,658 |
| Median gross monthly rent | $2,971 ± $365 | $914 ± $54 | $2,658 ± $402 | $859 ± $70 |
| Median monthly owner costs, with mortgage | $3,387 ± $445 | $1,444 ± $208 | $3,424 ± $659 | $1,286 ± $730 |
| Median monthly owner costs, no mortgage | $1,053 ± $328 | $625 ± $129 | Open-interval median; MOE unavailable | $579 ± $274 |

## EPA built-environment context

The 2021 Smart Location Database has mixed source vintages. Its guide identifies 2019 TIGER boundaries; the `GEOID20` alias says 2018 and does not mean 2020 Census geography. Housing inputs here are labeled 2018 and employment inputs 2017. Transportation sources also have their own vintages. [Guide and source-year table](https://www.epa.gov/system/files/documents/2023-10/epa_sld_3.0_technicaldocumentationuserguide_may2021_0.pdf).

| Published field | Granada selected EPA block group | Ames selected EPA block group | Interpretation |
|---|---:|---:|---|
| Ac_Land | 181.23 acres | 130.38 acres | Source polygon's land area |
| D1A | 3.45 | 3.79 | Housing units per acre of unprotected land, older baseline |
| D1C | 8.67 | 18.75 | Jobs per acre of unprotected land, older baseline |
| D3B | 201.33 | 183.28 | Weighted pedestrian-oriented intersection density per square mile |
| D4A | 520.35 meters | Missing (`-99999`) | Population-weighted centroid to nearest modeled transit stop; not from our intersection |
| D4C | 1.00 | Missing (`-99999`) | Aggregate peak-period hourly frequency near the block group, not a specific route's headway |
| NatWalkInd | 17.67 / 20 | 13.17 / 20 | Older composite; hold out of household ranking in this example |

The retained adjacent Granada records range from 3.45 to 9.87 housing units per unprotected acre and from 15.33 to 17.67 on the walkability index. That variation is an additional reason not to represent the whole named neighborhood with one intersection's selected record.

Source `-99999` values are treated as unavailable in this report, not numeric measurements. Their precise reason is not separately identified in the returned record. D5AR/D5BR are retained for inspection but not translated into a household commute or a cross-mode comparison; their source models need separate review. No workplace SLC score or resident demographic fields are used.

## Two destination checks

The libraries' official pages supply public addresses; Census `locations/onelineaddress` supplies interpolated address coordinates. Calculate great-circle distance from each verified intersection with a spherical Earth radius of 6,371.0088 km. Results: Granada Hills **2.355 km**, Ames **0.448 km**, rounded to 2.36 and 0.45 km. These are selected destinations, not an exhaustive nearest-facility search. No route, entrance, opening-time fit, disability access, or current capacity was measured.

## Coverage of the broad inventory

| Candidate component | This sample's status | Remaining evidence |
|---|---|---|
| Purchase affordability / carrying costs | Historical context only | Current inventory, tax treatment, insurance, financing, household inputs |
| Housing stock / physical fit | Nine-table extract includes distributions and uncertainty | Joint type/bedroom/cost combinations; current homes for sale |
| Work / family / other destinations | Not measured | Private pins, modes, schedules, reliable travel times |
| Everyday errands | Not measured | Current grocery/pharmacy records and routes |
| Walking / biking / transit | Older EPA context only | Current networks, crossings, sidewalks, GTFS, service reliability |
| Parks / nature / pets | Not measured | Land cover, entrances, access rules and routes |
| Schools / childcare | Not measured | Programs, assignment, capacity, costs and routes |
| Healthcare / aging in place | Not measured | Relevant care and practical accessibility |
| Traffic / reported crime | Not measured | Comparable incident data and reporting coverage |
| Noise / air / surroundings | Not measured | Appropriate modeled/measured exposures and local checks |
| Weather / natural hazards | Not measured | NOAA, FEMA, wildfire layers and property-level follow-up |
| Internet / essential services | Subscription context only | Address-level offers, reliability, utilities and water |
| Built character / space | Housing age/mix and older density | Lots, trees, slopes, usable outdoor space, condition |
| Market conditions / change | Not measured | Dated listing/sales/trend source with usable terms |
| Recreation / culture / social routines | One library address per area | User-relevant destinations, access and hours |
| Property-specific constraints | Not measured | Title, permits, condition, restrictions, insurance and inspections |

“Not measured” here is unfinished sample work, not evidence that free data does not exist. The [broader source catalog](homebuyer-data-sources.md) remains the collection backlog. Neither example establishes performance in rural areas, Alaska, Hawaii, or territories.

## Reuse and verification

The published extract contains Census statistical/geographic data and selected EPA published geospatial outputs. EPA's [geospatial terms](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers#terms) describe public-domain status by default, with exceptions for third-party material. We do not redistribute proprietary street/transit inputs underlying EPA's calculations. OSM-derived anchor records are kept in a separate attributed ODbL file. Library web pages are cited for factual addresses; their page contents and images are not republished. No Zillow boundary files or household data are included.

Checks: four target rows in each of nine tables; compatible category totals; all 84 derived results regenerated; numeric missing-value handling inspected; source URLs/IDs retained; report values reconciled with extracts; map labels and boundary distinctions visually reviewed. This is a two-place research check, not a production data-quality certification.
