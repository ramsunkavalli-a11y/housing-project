# Worked profiles: Granada Hills and Ames

Research snapshot: **27 September 2026**. Granada Hills replaces Los Feliz at the owner's request. These examples explain the data component; they do not select a neighborhood winner or a production architecture.

**Free data can already describe the housing someone might find. It cannot yet establish that a suitable home is available, affordable today, or convenient for that household.** The useful first result is a description with evidence and follow-up questions.

We extracted **nine ACS tables, 212 estimates and their associated margin fields across four statistical areas**, plus selected EPA accessibility measures, two verified intersections, and two public-library address locations. The [methods and full comparison](worked-area-methods.md) retain definitions, calculations, sources, and gaps.

## Start with recognizable places

| Example | Exploration starting point | Main statistical area | Smaller-area check |
|---|---|---|---|
| Granada Hills, Los Angeles | [Chatsworth Street & Zelzah Avenue](https://www.openstreetmap.org/node/122720323) | Los Angeles County tract 1112.02; 1.87 km² land | Block group 2; 0.73 km² land |
| Old Town vicinity, Ames | [Douglas Avenue & 9th Street](https://www.openstreetmap.org/node/2624861615) | Story County tract 9; 3.87 km² land | Block group 2; 0.39 km² land |

The names make the examples recognizable. The intersection is a starting point for exploration. The statistics refer to the specific Census areas shown below, **not all of Granada Hills or the exact Old Town neighborhood**. An intersection can sit on an area boundary; the opposite side of the road may have a different statistical record. Granada Hills' commercial corridor is also described by the [Old Granada Village business district](https://www.granadahillsbid.com/).

![Statistical areas around the two exploration starting points](assets/worked-area-geographies.png)

Source boundaries: U.S. Census Bureau ACS 2024 geography and EPA's 2021 SLD release. Intersection locations: © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), [ODbL](https://opendatacommons.org/licenses/odbl/1-0/). These examples cover two built-up settings, not a national urban/rural validation.

## What a buyer could read

**Granada Hills example:** “The selected tract is mostly detached homes. Three-bedroom homes are the largest bedroom category, and much of the housing dates from the mid-20th century. The historical home-value estimate is about $817,000. Check current listings for the home size and price you need, then verify condition, insurance, and your actual trips.”

**Ames example:** “The selected tract has a mix of detached homes and units in smaller multi-unit buildings. About half the housing predates 1940. The historical home-value estimate is about $221,000. The public library's address is close to the exploration starting point, but walking conditions and home-specific costs still need checking.”

These statements describe available evidence, not resident demographics or a universal quality score. The historical values are owner-reported estimates for occupied homes, **not asking prices or a budget recommendation**.

## The evidence behind those descriptions

All figures in this table describe the **tracts**, using **2020–2024 ACS five-year estimates**. Percentages include approximate 90% margins of error in **percentage points**; dollar margins are published 90% margins. Financial amounts are in 2024 dollars. The full table contains 21 displayed measures per area.

| Measure | Granada Hills example tract | Ames example tract | Why it matters |
|---|---:|---:|---|
| Detached homes | 85.5% ± 9.0 | 60.0% ± 6.5 | Physical housing type someone might find |
| Three or more bedrooms | 68.0% ± 14.2 | 49.2% ± 6.0 | Space needs; not available inventory |
| Built before 1940 | 7.4% ± 3.1 | 54.6% ± 8.0 | Prompts condition and renovation questions |
| Median owner-reported home value | $816,500 ± $48,702 | $221,300 ± $10,161 | Historical cost context |
| Median gross monthly rent | $2,971 ± $365 | $914 ± $54 | Context for renting before buying |
| Median monthly owner costs, with mortgage | $3,387 ± $445 | $1,444 ± $208 | What existing owners reported; not a new mortgage quote |
| Median monthly owner costs, no mortgage | $1,053 ± $328 | $625 ± $129 | Recurring costs remain after a mortgage is paid |
| Households subscribing to cable/fiber/DSL | 85.4% ± 11.6 | 81.0% ± 8.2 | Subscription context; not address-level service availability |

Sources: ACS tables B25024, B25041, B25034, B25077, B25064, B25088, B28002. [Official downloadable tables](https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/); [saved evidence and calculations](research/worked-areas/README.md).

One extra limitation matters: these separate tables do not reveal how many homes are **both detached and three-bedroom**. Multiplying the two percentages would impose an unsupported independence assumption. A suitable cross-tabulation is needed before creating that combined housing-type filter.

## Where simple filtering would go wrong

**1. “At least 60% of homes should have three or more bedrooms.”** The Granada Hills tract estimate is 68%, but the approximate interval is 54%–82%. That evidence straddles the threshold. A proposed filter should mark this uncertain, rather than assert a pass. This is an artificial area-preference example, not an adopted cutoff rule. Someone needing one three-bedroom home should not be excluded merely because most nearby homes have fewer bedrooms.

**2. “Use the smallest area because it is more accurate.”** The Granada Hills block-group estimate for three-plus bedrooms is 50.1% ± 21.8 points. The Ames block-group detached-home estimate is 53.3% ± 22.2 points. The smaller area is more local, but its uncertainty is wider for these measures. Moving to a tract changes the place being described; it does not repair the smaller-area estimate.

**3. “The walkability score tells us where daily life is easier.”** EPA's older selected records show 17.7/20 for Granada Hills and 13.2/20 for Ames. But the Ames record has missing transit-related values, its transit rank is 1, and its old block-group boundary is south of the newer Census block group. The scores alone cannot settle this comparison. Keep the components and confirm actual routes. [EPA methodology](https://www.epa.gov/sites/default/files/2021-06/documents/national_walkability_index_methodology_and_user_guide_june2021.pdf).

**4. “Nearby means walkable.”** The [Granada Hills Branch Library](https://www.lapl.org/branches/granada-hills), 10640 Petit Avenue, is about **2.36 km straight-line** from our starting point. The [Ames Public Library](https://www.amespubliclibrary.org/branch/ames-public-library), 515 Douglas Avenue, is about **0.45 km straight-line** away. Those distances use Census address estimates, not verified entrances. No walking times, nearest-library claim, or route accessibility claim follows from them.

**5. “Missing means none.”** The EPA point query at Chatsworth/Zelzah returned no polygon; a small surrounding rectangle returned three. Ames has `-99999` transit fields, which may mean missing feed coverage or other source conditions. Neither result proves the absence of transit or built-environment data. [EPA field documentation](https://www.epa.gov/system/files/documents/2023-10/epa_sld_3.0_technicaldocumentationuserguide_may2021_0.pdf).

## What this suggests collecting first

For discussion, the strongest demonstrated first collection is **housing distributions, cost context, source geography, and uncertainty together**. Retain the detail; show a household only the characteristics relevant to its answers.

Then add **current destination locations and actual routes**. The library example shows the structure, but it is not an amenity-coverage audit. Grocery options, parks, healthcare, school/program access, and household destinations need their own evidence.

Keep **hazards, insurance, current purchase costs, and property checks visible as unresolved** until collected. This example has not audited them; its missing components are listed in the [methods](worked-area-methods.md#coverage-of-the-broad-inventory). No site deployment, scoring formula, or nationwide collection choice follows from these two examples.
