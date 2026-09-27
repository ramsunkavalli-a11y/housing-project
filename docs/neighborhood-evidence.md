# Neighborhood comparison: evidence and methods

Inspection date: **2026-09-27**. Companion to the [plain-language findings](neighborhood-findings.md). All examples concern public geographic data; no household or property-search information is included.

## Scope and method

This was a purposive comparison of five named examples in four cities, not a random sample or national quality test. Source coverage counts below use different units.

Downloaded Zillow's EPA archive and selected CDND files; read their geometries using GDAL/pyogrio. Examined WOF GeoJSON records and source metadata. Queried Overture divisions release **2026-09-23.1**. Converted source coordinates to WGS84, then calculated polygon areas and intersections in equal-area **EPSG:6933** using Shapely and pyproj. All selected polygons passed Shapely's validity check. This does not prove geographic accuracy.

Overlap means intersection area divided by union area (IoU). It measures geometric agreement, not correctness, freshness, or confidence. Report areas are rounded; ratios use unrounded values. The illustration uses local UTM projections (EPSG:32611 and 32616), north up, with a separate scale for each panel.

The companion [inspection manifest](research/inspection-manifest.json) records input hashes, source IDs, calculated areas, overlaps, and public cross-street checks. [Overture SQL](research/overture-divisions.sql) preserves the actual queries. Raw source polygons are not included in this repository.

## Zillow archive

[EPA download](https://edg.epa.gov/data/PUBLIC/OEI/ZILLOW_NEIGHBORHOODS/Zillow_Neighborhoods.zip), [catalog](https://catalog.data.gov/dataset/neighborhoods-us-2017-zillow-segs). The catalog dates the dataset to 2017; a 2026 catalog check is not a 2026 boundary release.

Read layer `ZillowNeighborhoods_GeoDD` in `ZillowNeighborhoods.gdb`: **17,057 records**. Exact State/City field counts: CA/Los Angeles **98**, CA/Pasadena **9**, IL/Chicago **228**, IA/Ames **18**. These are record counts, not proof that every part of each city is covered.

| Name | RegionID | Area km² |
|---|---|---:|
| Los Feliz | 274359 | 6.8206 |
| Sherman Oaks | 27080 | 25.6333 |
| Lincoln Square | 269591 | 0.5652 |
| Historic Old Town, Ames | 764180 | 0.1958 |

Pasadena's nine names: East Central, South Arroyo, South East, North East, Mid Central, North Central, South, North Arroyo, West Central. Bungalow Heaven is absent from this exact city-tagged inventory.

Ames's 18 names: Edwards, Oak-Riverside, Meeker North, Allenview, Top-O-Hollow, Sunrise Addition, North Old Town, Stone Brooke, Bloomington Heights, Northridge, College Creek/Old Ames, Westside, Oak-Wood-Forest, Kate Mitchell, Brookside, South Campus Area, Historic Old Town, Somerset Village.

**Reuse unresolved:** the catalog's machine-readable license is CC0, but its narrative calls for Zillow attribution under an unspecified Creative Commons license. The original terms/version were not established. This report provides calculated comparisons and record identifiers; the figure does not draw Zillow polygons. Confirm the original terms before adopting the archive for display, redistribution, or agent-facing geometry.

## City-Defined Neighborhood Dataset (CDND)

[Dataset DOI](https://doi.org/10.7910/DVN/02NP1O), [version metadata](https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/02NP1O), [research paper](https://www.nature.com/articles/s41597-025-05329-6). Inspected version 1, released **2025-03-20**, with dataset license **CC0 1.0**. This verifies the dataset's stated license; it is separate from the article's license. Original municipal collection dates can precede publication.

| Download | Dataverse file ID | Records / selected record | Finding |
|---|---:|---|---|
| [LosAngelesCA_onm_cleaned.zip](https://dataverse.harvard.edu/api/access/datafile/11001337) | 11001337 | 114; `nbhd=Los Feliz`, FID 57; `nbhd=Sherman Oaks`, FID 83 | Areas 6.7959 and 23.7471 km². |
| [LosAngelesCA_nha_cleaned.zip](https://dataverse.harvard.edu/api/access/datafile/11001363) | 11001363 | 99 | Only name field `nha`; all values `00:00:00.000` in both pyshp and GDAL readers. No name-based joins used. |
| [PasadenaCA_nha_cleaned.zip](https://dataverse.harvard.edu/api/access/datafile/11001126) | 11001126 | 84; Bungalow Heaven Neighborhood Association, FID 20 | Area 0.9153 km²; association boundary, not assumed identical to a historic district. |
| [ChicagoIL_onm_cleaned.zip](https://dataverse.harvard.edu/api/access/datafile/11001258) | 11001258 | 77; `nbhd=4`, FID 5 | Area 6.6287 km². Names require a community-area code join. |
| [city_list.tab](https://dataverse.harvard.edu/api/access/datafile/11000942) | 11000942 | City inventory | Ames is not listed. |

FID is the zero-based feature identifier returned by the shapefile reader, not an enduring external place ID. Chicago's [official data query](https://data.cityofchicago.org/resource/igwz-8jzy.json?%24select=community%2Carea_numbe&%24where=area_numbe%3D4) returned `community=LINCOLN SQUARE, area_numbe=4`.

## Who's On First (WOF)

Inspected [U.S. repository revision c4e4f9b](https://github.com/whosonfirst-data/whosonfirst-data-admin-us/tree/c4e4f9b2233c4b29a6f7124278b635e270d0b87d). Selected records were filtered by hierarchy/location to exclude identically named places elsewhere.

| Record | Shape / area | Source and status |
|---|---|---|
| [Los Feliz 85868353](https://github.com/whosonfirst-data/whosonfirst-data-admin-us/blob/c4e4f9b2233c4b29a6f7124278b635e270d0b87d/data/858/683/53/85868353.geojson) | Polygon; 6.8284 km² | `src:geom=mz`; `mz:is_current=1`. |
| [Sherman Oaks 85848285](https://github.com/whosonfirst-data/whosonfirst-data-admin-us/blob/c4e4f9b2233c4b29a6f7124278b635e270d0b87d/data/858/482/85/85848285.geojson) | MultiPolygon; 22.4954 km² | `lacity`: certified neighborhood council boundaries; current=1. |
| [Lincoln Square 85869419](https://github.com/whosonfirst-data/whosonfirst-data-admin-us/blob/c4e4f9b2233c4b29a6f7124278b635e270d0b87d/data/858/694/19/85869419.geojson) | MultiPolygon; 0.5331 km² | `zolk`; current=-1 means unknown, not confirmed current. |
| [Ontario 85839623, Ames](https://github.com/whosonfirst-data/whosonfirst-data-admin-us/blob/c4e4f9b2233c4b29a6f7124278b635e270d0b87d/data/858/396/23/85839623.geojson) | Point | `mz`; current=-1. Located through Ames locality ID 85943339. |

No Bungalow Heaven record was located by the exact-name code search. That is a search result, not an exhaustive absence claim. The Ames hierarchy search likewise establishes the presence of Ontario, not a complete inventory.

Reuse is source-specific. See [WOF licenses](https://www.whosonfirst.org/docs/licenses/) and source definitions for [mz](https://github.com/whosonfirst/whosonfirst-sources/blob/main/sources/mz.json), [lacity](https://github.com/whosonfirst/whosonfirst-sources/blob/main/sources/lacity.json), and [zolk](https://github.com/whosonfirst/whosonfirst-sources/blob/main/sources/zolk.json). The last identifies Kevin Zolkiewicz's Chicago Neighborhoods Map and CC BY 3.0 US. WOF's original work being CC0 does not erase underlying attribution requirements.

## Overture and OpenStreetMap

[Release catalog](https://stac.overturemaps.org/catalog.json), [divisions documentation](https://docs.overturemaps.org/guides/divisions/), [attribution](https://docs.overturemaps.org/attribution/). Inspected release **2026-09-23.1**, then the catalog's latest. Queries selected U.S. neighborhood/macrohood/microhood records in specified coordinate windows and, except Ames, matching names. Windows filter `bbox.xmin/ymin`; they are not exhaustive city-polygon intersection tests.

| Area record | Overture ID | Area km² | Upstream geometry |
|---|---|---:|---|
| Los Feliz | a039d2c3-51e3-4702-b7f2-04453e2c98cc | 6.8445 | [OSM way 260858785](https://www.openstreetmap.org/way/260858785), version 18 |
| Los Feliz Neighborhood Council District | b1e64776-4f7d-4701-a000-02d793dbe9c8 | 24.1157 | [OSM relation 17307354](https://www.openstreetmap.org/relation/17307354), version 2 |
| Sherman Oaks Neighborhood Council District | 026ed56c-654c-4453-8831-a0ca9d7a64b0 | 22.4594 | [OSM relation 18194737](https://www.openstreetmap.org/relation/18194737), version 4 |
| Lincoln Square | 56efc7ff-0cf6-4fa7-9955-4f370095302b | 6.6275 | [OSM relation 10115240](https://www.openstreetmap.org/relation/10115240), version 10 |

All four selected area records derive from OSM. They cannot count as four independent confirmations of OSM.

Bungalow Heaven point ID `8357e8d1-8909-48c1-a9e0-d53047f02276` derives from [OSM node 4773917663](https://www.openstreetmap.org/node/4773917663), version 2, with a 2017 source update. A new Overture release does not mean every underlying record was recently revised.

The Ames query found six points: Schilletter-University Village, Somerset, Frederiksen Court, Richardson Court, Union Drive, Iowa State Center. It found no area records in that query. This is not a claim that Ames has no neighborhoods or that OSM has none outside the queried categories/windows.

## Selected geometric comparisons

| Pair | Intersection / union | Interpretation |
|---|---:|---|
| Los Feliz: CDND vs WOF | 98.26% | Close outlines in this sample. |
| Los Feliz: CDND vs Zillow | 88.72% | Similar total area does not imply the same boundary. |
| Sherman Oaks: WOF vs Overture council | 99.47% | Consistent with WOF's council-boundary source. |
| Lincoln Square: CDND vs Overture | 99.72% | Both match the larger community-area scale. |
| Lincoln Square: Zillow vs WOF | 93.44% | Both describe a much smaller area. |
| Lincoln Square: CDND vs WOF | 8.04% | Same name, markedly different geographic scope. |

## Cross-street checks

Checked live OSM extracts on the inspection date. Each listed pair has road ways sharing an actual OSM node, rather than merely crossing as drawn lines. Coordinate-in-polygon checks used WGS84 and `covers`; this allows points on a boundary. These are candidate exploration points, not locally endorsed recommendations.

| Example | Street pair and public map evidence | Relationship to inspected outlines |
|---|---|---|
| Los Feliz | [Vermont Avenue & Franklin Avenue](https://www.openstreetmap.org/node/20842309) | Within all four neighborhood-source outlines and the larger Overture council outline. |
| Los Feliz | [Hillhurst Avenue & Franklin Avenue](https://www.openstreetmap.org/node/1718185213) | Same. |
| Sherman Oaks | [Ventura Boulevard & Van Nuys Boulevard](https://www.openstreetmap.org/node/269588234) | Within Zillow, CDND, WOF, and Overture council outlines. |
| Sherman Oaks | [Ventura Boulevard & Woodman Avenue](https://www.openstreetmap.org/node/269571031) | Same. |
| Bungalow Heaven | [North Holliston Avenue & East Mountain Street](https://www.openstreetmap.org/node/13309148079) | Within CDND association outline, near its eastern edge. |
| Bungalow Heaven | [North Michigan Avenue & East Mountain Street](https://www.openstreetmap.org/node/123129442) | Within CDND association outline. |
| Lincoln Square | North Lincoln Avenue & West Leland Avenue: [node A](https://www.openstreetmap.org/node/260227530), [node B](https://www.openstreetmap.org/node/262077533) | Both within smaller Zillow/WOF and larger CDND/Overture outlines. Two mapped connections mean the label needs a selected map pin. |
| Lincoln Square | [North Western Avenue & West Leland Avenue](https://www.openstreetmap.org/node/157729865) | Within all four inspected outlines. |
| Ames / Old Town vicinity | [Douglas Avenue & 9th Street](https://www.openstreetmap.org/node/2624861615) | Within Zillow Historic Old Town. |
| Ames / Old Town vicinity | [Clark Avenue & 9th Street](https://www.openstreetmap.org/node/161132195) | Outside all 18 inspected Zillow Ames polygons. Do not label it inside Historic Old Town on that evidence. |

This illustrates why exploration anchors must retain their relationship to a boundary. The neighborhood name alone does not establish containment. A connected road node also does not establish pedestrian access or desirable conditions.

LA and Chicago records came from small Overpass queries. Pasadena and Ames Overpass calls returned timeouts/rate limits; small direct OSM map API extracts supplied the final checks. An attempted remote Overture transportation scan did not finish within the research session and was stopped. This is an access/performance finding, not missing-street evidence. Production access costs, service policies, travel routing, and refresh schedules remain untested.

## Figure and reuse

The figure uses Overture/OSM geometry for Los Feliz, its council district, and the larger Lincoln Square outline; WOF/Zolk geometry for the smaller Lincoln Square outline. It simplifies presentation, not geographic meaning. Credits: **Overture Maps Foundation; © OpenStreetMap contributors; Who's On First; Kevin Zolkiewicz, Chicago Neighborhoods Map**.

Source terms: [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/), [OpenStreetMap copyright and attribution](https://www.openstreetmap.org/copyright), [WOF licenses](https://www.whosonfirst.org/docs/licenses/), [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/). Record links above identify the source geometries; the manifest records the inspected releases. The figure is an attributed visual comparison, not a grant of unrestricted rights to the underlying databases. Agent-facing downloads or a combined production database need a separate review of their actual design and applicable terms.

## Remaining work before adoption

- Review the proposed geographic model with the owner; source choice remains open.
- Obtain local feedback on names and candidate starting points.
- Resolve Zillow's inconsistent license metadata if the archive is to be used in the product.
- Test coverage in a chosen launch area and inspect additional source files; these five examples do not establish national reliability.
- Define a practical update and access process once the launch scope is agreed.
