# What to collect, and how to make it useful to homebuyers

Research sweep: **2026-09-27**. Component 2. Recommendations for discussion; no national data pipeline, feature weights, or product implementation authorized by this document.

**Recommendation: build a broad evidence inventory, preserve the underlying measurements, and expose only the few that matter to a particular household.** Collecting many useful variables does not require asking every user many questions or producing one giant neighborhood score.

Read the [candidate collection inventory](homebuyer-data-inventory.md), [source catalog](homebuyer-data-sources.md), and [research notes](homebuyer-literature.md) for the supporting detail.

## What the literature changes about the plan

1. **The desired home and the desired area must both be feasible.** Residential-choice research separates dwelling attributes, accessibility, surroundings, and household constraints. A neighborhood with attractive amenities but little of the desired housing type is a weak recommendation. Our proposed collection therefore includes housing mix, bedrooms, age, and ownership costs alongside place attributes. [Schirmer et al., 2014](https://www.jtlu.org/index.php/jtlu/article/view/740).
2. **The household's destinations matter.** Buyer surveys identify friends/family, employment, shopping, and other destinations. We should allow several private destination pins, visit frequencies, and travel modes. A generic distance to downtown misses this. Survey averages are prompts for questions, not universal weights. [NAR 2025 generational report](https://www.nar.realtor/sites/default/files/2025-04/2025-home-buyers-and-sellers-generational-trends-04-01-2025.pdf).
3. **Access is more useful than raw amenity counts.** The travel literature supports measuring reachable destinations and network structure. A supermarket across a freeway may be geographically close but inconvenient. Routing must respect actual connections, modes, entrances, and time of day. This is a product inference, not evidence that a particular travel-time cutoff suits everyone. [Ewing and Cervero, 2010](https://doi.org/10.1080/01944361003766766), [Boeing, 2025](https://arxiv.org/abs/2505.00736).
4. **Buyers' observed choices are constrained.** What someone purchased reflects available stock and budget as well as preferences. Stated-preference surveys have hypothetical-choice and wording limitations. Use both kinds of evidence, then test the tool with actual home seekers. [Bruch and Mare, 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3591474/).
5. **Risk and recurring costs deserve first-class treatment.** Flood-information experiments show that risk information can change search and purchase behavior. Hazard exposure and insurance availability belong in the inventory even when affordable property-specific quotes are unavailable. This does not make regional hazard estimates insurance quotes. [NBER working paper 33119](https://www.nber.org/papers/w33119).
6. **Some important things cannot be measured reliably at national neighborhood scale.** Actual school assignment, childcare vacancies, noise inside a home, utility bills, parking, building condition, and insurance quotes often require local or property-level verification. Keep them in the product's scope as explicit unknowns or follow-up checks.

## Broad collection scope

The inventory covers 16 components, with multiple candidate measurements per component. These are candidate observations, not 16 equally weighted scores.

| Component | Buyer question |
|---|---|
| 1. Purchase affordability and carrying costs | Can we afford the type of home we need, including recurring costs? |
| 2. Housing stock and physical fit | Does this area have the kind of home we want? |
| 3. Work, family, and other destinations | Does daily life work for every member of the household? |
| 4. Everyday errands | Can we reach groceries, pharmacies, and routine services conveniently? |
| 5. Walking, biking, and transit | Can we move around in the ways we want? |
| 6. Parks, nature, and pets | Can we access the outdoor activities that matter to us? |
| 7. Schools and childcare | Are relevant programs reachable and actually available to us? |
| 8. Healthcare and aging in place | Can we reach needed care and manage daily activities? |
| 9. Traffic and reported crime | What specific safety evidence and reporting gaps exist? |
| 10. Noise, air, and immediate surroundings | What might make day-to-day living uncomfortable? |
| 11. Weather and natural hazards | What exposure and climate tradeoffs should we understand? |
| 12. Internet and essential services | Can we work from home and obtain dependable services? |
| 13. Built character and space | Does the physical setting match our preferences? |
| 14. Market conditions and change | How difficult is buying here, and what changes are documented? |
| 15. Recreation, culture, and social routines | Can we continue the activities and relationships we value? |
| 16. Property-specific constraints | What must be checked before this becomes a viable home purchase? |

## A practical free starting collection

**First broad batch:** Census ACS/TIGER housing and cost context; EPA Smart Location Database (SLD); Overture names, places, and transportation; USGS land cover and protected areas; NCES school locations; CMS hospital locations; NOAA climate context; FEMA/USFS hazard context. The [source catalog](homebuyer-data-sources.md) explains differences in geography, availability, and readiness. This batch is a proposal for a small audit before a national import.

SLD is a particularly useful shortcut: more than 90 measures already assembled, with the current version dated 2021. Use it as an older baseline, not a claim about current transit or businesses. Its geography requires careful alignment with newer Census data. [EPA documentation](https://www.epa.gov/smartgrowth/smart-location-mapping).

**Next, where demand warrants it:** current agency transit feeds, local crime and crash records, broadband data, air/noise layers, childcare directories, local taxes and permits, and property-market sources whose reuse rights are clear. Valuable data may still be too uneven or expensive to maintain nationally at first.

**Collect from the user, privately:** destinations, schedules, total budget, desired home type, mobility needs, school/program requirements, and tradeoffs. Ask about needs directly rather than infer them from household demographics.

## How to use the raw data

### 1. Keep observations separate from judgments

Preserve source records and dates; derive understandable measures; apply household preferences last. A source's existence-confidence score is not a rating of a shop. A high density is not inherently good or bad. “Quiet” cannot be inferred just from few restaurants.

Every derived measure should retain: identifier, plain-language definition, unit, numerator/denominator or calculation, source IDs and releases, observation period, original geography, output geography, uncertainty, missing-data reason, transformation version, and applicable reuse terms. These are proposed requirements, not a database choice.

### 2. Use different geographic units for different questions

- Keep statistical estimates on their supported Census units initially. Display their extent when explaining them.
- Compute access over a travel network from several plausible residential starting points. An uninhabited geometric center can misrepresent an area.
- Summarize raster hazards or land cover over a stated area; distinguish land-area exposure from exposure of mapped homes.
- Keep school assignments, tax parcels, utility areas, and hazard boundaries in their own geographies.

Where a crosswalk is necessary, match weighting to the quantity: housing-unit weights for housing counts, for example. Area weighting assumes uniform distribution and can be particularly poor around parks, industrial land, or water. Weighting creates estimates; it does not create new observations. [NHGIS crosswalk methods](https://www.nhgis.org/geographic-crosswalks).

### 3. Prefer distributions and components to a lone average

Retain bedroom categories, structure types, rent/value bands, and travel-time ranges. Recompute a share from summed compatible counts; do not average percentages with unequal denominators. Do not average neighborhood medians and call the result a larger area's median. Preserve published estimates, margins of error, and annotations; distinguish missing/suppressed values from zero. [Census ACS accuracy guidance](https://www2.census.gov/programs-surveys/acs/tech_docs/accuracy/MultiyearACSAccuracyofData2024.pdf).

Example: if two compatible areas have 20 of 100 and 90 of 300 homes in a category, the combined share is 110/400 = **27.5%**, not the unweighted average of 20% and 30%. This is a fictional arithmetic example, not a geographic interpolation method.

### 4. Make accessibility answer a real question

For each destination category, candidate measures include nearest reachable destination, alternatives within user-relevant travel times, opening/service hours, and route limitations. Keep the underlying results so thresholds can change. A pharmacy, a supermarket, and an emergency department should not be interchangeable points in an amenity total.

For commutes, retain each person's destination and schedule. Show per-person results and the household tradeoff; an average can conceal one unacceptable commute. Free-flow driving time is not rush-hour time. A scheduled transit itinerary is not a reliability measurement. Resident commute statistics and LODES job flows are context, not predictions of a user's trip. [Census LODES methods](https://www2.census.gov/ces/wp/2014/CES-WP-14-38.pdf), [GTFS](https://gtfs.org/documentation/schedule/reference/).

### 5. Keep evidence quality separate from preference fit

Use understandable flags such as current/older, direct/proxy/modelled, supported/uncertain/missing. Do not turn a missing grocery record into “no groceries,” an unmapped flood area into “no flood risk,” or a missing crime submission into zero crime. Prefer reviewable ranges or “cannot determine” when a threshold falls within substantial uncertainty. No arbitrary confidence cutoff is approved here.

### 6. Reduce features after measuring usefulness

For each candidate, ask: can it change a buyer's decision; does it add information beyond existing measures; is its coverage usable; is it stable enough; can we explain it; and what does maintaining it cost?

Audit redundancy before ranking. Density, intersection count, retail density, and a composite walkability index may repeat the same signal. Retain the raw components, but avoid giving them four votes in a single score. Compare shortlists with and without feature groups, vary reasonable thresholds, and check whether the reasons remain understandable.

Pilot with home seekers who have different needs and locations. Track useful shortlist changes, incorrect exclusions, misunderstood explanations, corrected source records, and voluntary visit/save decisions. Clicks alone are weak evidence of homebuyer value. These evaluation methods are proposals, not a validated model.

## How the broad inventory becomes a simple result

**Fictional example:** an area contains many three-bedroom homes, has two groceries reachable on foot, and gives one partner a longer commute. Show those three facts first if they matter to that household. Keep climate, internet, school, and other evidence available; elevate it only when relevant or when a material limitation affects the recommendation.

Do not use residents' race, ethnicity, religion, national origin, or household composition as desirability features. Do not translate affluent residents into “better neighborhood,” high raw test scores into school quality, or demographic resemblance into personal fit. Measure requested services and physical conditions directly.

## Recommended next artifact

Before collecting everything nationally, make **one worked area profile** with a generous subset from the inventory. Show each measure's raw source, transformation, buyer-facing wording, and gaps. Include an urban and a less-dense example when checking whether the measures generalize. Then select a collection batch and return to the question layer. This sweep expands the candidates; it does not commit us to displaying or scoring them all.
