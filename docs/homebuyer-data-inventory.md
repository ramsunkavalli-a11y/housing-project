# Candidate collection inventory

Reviewed 2026-09-27. A deliberately broad inventory to narrow through buyer usefulness and source audits. **Listed does not mean available, collected, reliable, or approved for ranking.** Source IDs refer to the [source catalog](homebuyer-data-sources.md).

**Owner's subsequent correction:** start with [buyer decisions](buyer-decisions.md). Readiness below describes source candidates, not collection priority. Every candidate must identify the buyer question and how it could change the shortlist before collection is selected. Detached-home share is background only, with no default headline or cutoff.

Readiness labels describe proposed work, not universal quality:

- **First audit:** plausible free sources worth testing in the first area profiles.
- **Conditional:** collect where coverage, freshness, permissions, and incremental value justify it.
- **Personal/property:** requires household input or checking a particular home; cannot be filled from area averages.

## 1. Purchase affordability and carrying costs

**Why:** a location is useful only if the household can obtain suitable housing there. Sources: S01, S21, S22, S23, S27.

| Candidate raw inputs | Useful derived output | Readiness / important limit |
|---|---|---|
| Owner-reported value bands; gross-rent bands; estimate errors | Historical price/rent context and spread | First audit; neither is current asking-price inventory. |
| Selected monthly owner costs; mortgage-status split | Context on existing owners' cost distribution | First audit; existing loans do not represent a new buyer's payment. |
| Compatible market price index time series | Historical change over a stated period | Conditional; price change is not a dollar price or forecast. |
| Local assessment, tax rate, exemptions, reassessment rules | Estimated taxes for a specific purchase scenario | Personal/property; seller's tax bill can be misleading. |
| Insurance and HOA quotes; utilities; maintenance assumptions | Itemized recurring-cost range | Personal/property; record assumptions and quote date. |
| Down payment, financing inputs, closing/moving costs, reserve preference | Household-specific feasible budget range | Personal/property; separate from neighborhood scoring. |
| Travel distance, frequency, parking/tolls, vehicle/transit costs | Housing-plus-travel budget scenario | Conditional/personal; avoid counting expenses twice. |

## 2. Housing stock and physical fit

**Why:** determine whether there is evidence of homes that meet the buyer's needs. Current matching options are more direct evidence than an area's housing composition; lack of evidence is not proof that no suitable home exists. Sources: S01, S03, S22, S27.

| Candidate raw inputs | Useful derived output | Readiness / important limit |
|---|---|---|
| Units by structure type | Optional background on building patterns when explicitly relevant | Already sampled; no default headline or exclusion rule. Does not establish current options, tenure or condominium status. |
| Bedroom distribution; room distribution | Historical housing-size context | Bedroom counts sampled; room counts not audited. Not current availability. Separate distributions do not reveal their joint intersection. |
| Construction-year bands | Older/newer stock mix | First audit; age is not condition, charm, energy efficiency, or code compliance. |
| Occupancy/vacancy categories | Occupied stock and type of vacancy | First audit; vacancy is not current for-sale availability. |
| Owner/renter counts; totals | Ownership context and valid denominators | First audit; never a desirability ranking of residents. |
| Parcel lot area, building floor area, footprints | Space and building-pattern context | Conditional; footprints are not interior floor area or usable yard. |
| Current matching listings and sale records | Actually obtainable homes by required type and budget | Conditional; no comprehensive unrestricted free listing feed established. |

## 3. Work, family, and other destinations

**Why:** a household's actual daily geography matters more than generic closeness to a city center. Sources: S04, S05, S06, S26.

Candidate inputs: multiple destination pins, days/times of travel, frequency, mode, each person's maximum acceptable trip, route alternatives, transfers, access/egress, parking/tolls, and travel-time variability when supported. **Personal/conditional.**

Derived outputs: each person's trip range; weekly household travel burden; reachable jobs by industry as optional context; routes that fail a hard requirement. Do not infer personal commute from the area's resident commute average. LODES describes employment geography, not traffic, exact attendance, or transport mode. Keep destinations private and out of public research artifacts.

## 4. Everyday errands

**Why:** routine trips determine daily convenience. Sources: S03, S04.

Candidate inputs: supermarket versus convenience-store categories, pharmacies, general retail, household services, banks/ATMs, postal services, opening hours where present, entrances, and place status. **First audit** for locations; **conditional** for reliable hours and access.

Derived outputs: network distance/time to an appropriate destination, number of alternatives, and a household-selected essentials basket. Deduplicate overlapping provider records. A mapped shop's existence is not evidence of affordability, product selection, current opening, or accessibility.

## 5. Walking, biking, and transit

**Why:** respondents value several ways of getting around, with substantial differences in preferences. Sources: S02, S04, S05, S15.

Candidate inputs: connected intersections, pedestrian permissions, sidewalks, crossings, road class/speed, cycleways, slope, barriers, transit stop locations, departure frequency, operating span, weekend service, and accessible boarding fields. **First audit** for broad network/context; **conditional** for detailed attributes and current feeds.

Derived outputs: reachable essentials, detour ratio, accessible routes where known, frequency of usable service, and transfer burden. Keep absent sidewalk tags as unknown. Avoid treating straight-line buffers, transit-stop counts, or a national walkability percentile as observed walking experience. Schedule data does not measure on-time reliability.

## 6. Parks, nature, and pets

**Why:** outdoor routines and usable space matter independently of shopping access. Sources: S03, S04, S07, S08, S27.

Candidate inputs: public access status, park entrances, trails, playgrounds, sports facilities, dog areas, tree cover, vegetation, surface type, and terrain. **First audit** for broad layers; **conditional** for entrances, rules, and facilities.

Derived outputs: travel time to a usable entrance, public outdoor alternatives, vegetation share, and shaded-route evidence where supported. Protected land may be inaccessible. A large park polygon nearby does not imply an entrance nearby. Tree cover does not prove shade on a particular sidewalk. HOA or park pet restrictions require local confirmation.

## 7. Schools and childcare

**Why:** requirements vary sharply by household, age, program, and timing. Sources: S09, S10, S11, S27.

Candidate inputs: school locations, grades served, school type, district identifier, programs, attendance zones, enrollment rules, growth/achievement measures with uncertainty, childcare provider licenses, age bands, county childcare prices, and vacancies. **First audit** for school locations; **conditional/personal** for the rest.

Derived outputs: relevant options to investigate, travel to an eligible program, and transparent educational measures if terms permit. Nearest school is not assigned school. Old national attendance boundaries are unsuitable for current assignment. County prices do not establish local openings or actual fees. Avoid a single “good schools” score derived from average achievement.

## 8. Healthcare and aging in place

**Why:** access to needed care and physical usability can be hard requirements. Sources: S03, S04, S12, S26, S27.

Candidate inputs: hospital location/type, emergency service indicator, primary/specialist care, pharmacies, accessible routes, desired provider, insurance-network acceptance, and appointment availability. **First audit** for facility locations; **personal/conditional** for actual usable care.

Derived outputs: reachability of an appropriate facility and explicit unverified eligibility/availability. Nearest hospital is not necessarily the right facility. Provider listings cannot establish emergency response time, wait time, clinical suitability, or insurance acceptance.

## 9. Traffic and reported crime

**Why:** homebuyers care about safety, but different evidence measures different things. Sources: S13, S14, S04, S27.

Candidate inputs: fatal crash locations/date/mode, locally available injury crashes, high-speed crossings, reported incident category/date, reporting agency and boundaries, participating months, geocoding precision, and changes in reporting definitions. **Conditional**, with traffic-network context in the first audit.

Derived outputs: specific documented incidents or route conflicts over stated periods, within-source trends when comparable, and coverage notices. FARS contains fatal crashes, not all crashes. Residential population is often a poor denominator for exposure on a shopping street. Police reports are neither all victimization nor a prediction of individual risk. Do not rank neighborhoods nationally from incomplete agency totals.

## 10. Noise, air, and immediate surroundings

**Why:** nuisances may strongly affect daily comfort even if poorly represented in buyer surveys. Sources: S15, S16, S17, S04, S27.

Candidate inputs: modeled road/rail/aviation noise, distance to major transport infrastructure, monitored PM2.5/ozone and coverage, industrial facility locations, reported emissions/violations, nightlife locations/hours, lighting and recurring local complaints where available. **Conditional.**

Derived outputs: source-specific screening context and prompts for day/night visits. Outdoor modeled noise is not indoor noise; nearest-monitor air quality is not block-level exposure. Distance to a facility is not a dose estimate. Complaint counts depend on willingness and ability to report, not just underlying conditions.

## 11. Weather and natural hazards

**Why:** climate comfort, disruption, damage, and insurance are distinct buyer concerns. Sources: S18, S19, S20, S24.

Candidate inputs: temperature/precipitation/snow normals, extreme-weather observations, elevation/slope, mapped flood zones and effective dates, wildfire hazard/exposure, hazard-specific expected losses, coastal exposure where relevant, and scenario/horizon for any projections. **First audit** for broad context; **conditional/property** for detailed exposure.

Derived outputs: seasonal context; specific hazard flags; share of a stated area or mapped housing locations exposed; links to address-level checks. Historical normals are not forecasts. Community risk composites may include social vulnerability and resilience, so do not relabel them property hazard. No mapping does not mean no hazard; modeled exposure does not establish an insurance premium.

## 12. Internet and essential services

**Why:** remote work and basic household services can determine feasibility. Sources: S25, S17, S01, S27.

Candidate inputs: reported broadband technology/providers/speeds, reporting date, challenge status, household subscription context, water provider and service-area confidence, relevant violations, sewer/septic, electric utility, and outage history when obtainable. **Conditional/property.**

Derived outputs: candidate providers to verify, service-area evidence, and unresolved infrastructure checks. Advertised availability is not measured speed, price, reliability, or installation feasibility. Subscription rates measure adoption, not service availability. Water compliance history does not describe a home's plumbing or private well.

## 13. Built character and space

**Why:** preferences for compact, spacious, historic, or mixed-use surroundings differ. Sources: S01, S02, S03, S07, S27.

Candidate inputs: dwelling density, structure mix, building age bands, impervious cover, land-use mix, block length, frontage/setback where locally available, terrain, and verified historic designations. **First audit** for coarse physical description; **conditional** for parcel detail.

Derived outputs: descriptive physical profiles rather than “good/bad character.” Mixed-use does not guarantee nightlife or noise; newer buildings do not guarantee better condition. Historic district rules, zoning, and development rights require current local documents.

## 14. Market conditions and change

**Why:** available options and known nearby changes affect timing and expectations. Sources: S21, S22, S27.

Candidate inputs: compatible price-index history, current listing counts, sale/list ratio, time on market, transaction volume, price reductions, permit type/status/date, approved projects, and planned transit changes. **Conditional.**

Derived outputs: current competition context when supported; historical trends; separately labeled proposed/approved/under-construction projects. Do not infer future appreciation from past growth or demographic change. Permit counts do not equal completed units. Market-series boundary and methodology changes can produce artificial trends.

## 15. Recreation, culture, and social routines

**Why:** practical personal fit includes activities and relationships beyond employment. Sources: S03, S04, S28, S26, S27.

Candidate inputs: libraries, recreation centers, sports, restaurants/cuisines where categorized, arts venues, community facilities, places the user selects, event schedules, and accessible operating hours. **First audit** for generic locations; **personal/conditional** for actual routines.

Derived outputs: reachability of chosen activities and options to explore. Do not infer a person's identity from venue choices, infer a neighborhood's residents' religion from buildings, or label an area welcoming from demographic composition. Sense of belonging and social connection should be elicited and reviewed with people, not manufactured from POI counts.

## 16. Property-specific constraints

**Why:** an area shortlist is only the first stage of a purchase. Sources: S26, S27 and verified property documents.

Candidate inputs: step-free access, stairs/elevator, parking, yard, sunlight, construction/roof condition, energy systems, utility bills, repair needs, parcel-specific insurance, HOA fees/rules/reserves, rental restrictions, school eligibility, water/sewer, title/easements, and legal ability to make desired alterations. **Personal/property.**

Derived output: a clear verification checklist and unresolved requirements. These are not facts that can be assigned to every home from Census or map data. Relevant professional/local checks remain necessary; the neighborhood product should not imply it has performed them.

## Cross-cutting fields to collect for every component

Source and release; original record ID; observation date/period; source geometry and vintage; unit; population/universe or denominator; uncertainty; missingness reason; model assumptions; attribution/reuse terms; retrieval date; transformation version; and validation notes. Keep these out of the primary user flow unless they explain a limitation or comparison.

## What to remove first when narrowing

Remove unsupported precision, redundant composite scores, stale operational claims, and expensive features that rarely affect a buyer's shortlist. Retain an explicit unknown when an important requirement cannot be evaluated. Do not discard a consequential but difficult question solely because the free national data is weak.
