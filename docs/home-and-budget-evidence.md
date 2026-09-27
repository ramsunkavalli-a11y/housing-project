# Home and budget: evidence and calculation notes

Reviewed 2026-09-27. [Read the component explanation first](home-and-budget.md). Source availability and published documentation were reviewed; no commercial market feed was imported or approved. All worked-example finances are fictional.

## What to collect and why

| Input | Job in the answer | Required handling |
|---|---|---|
| Home requirements and acceptable alternatives | Identify relevant candidate homes and meaningful price comparisons | Distinguish requirement, preference and unknown; a three-bedroom area series does not establish yard or parking availability |
| User's price range or monthly preference/ceiling | Anchor the search in the user's budget | Preserve which kind of budget was supplied; do not imply a monthly check was performed for a price-only answer |
| Cash and chosen retained reserve | Check down payment plus transaction and initial costs | Keep retained cash separate from cash paid at closing; identify contingent funds such as proceeds from another sale |
| Loan amount, note rate, term and applicable mortgage insurance | Estimate scheduled financing costs | Use a dated quote if supplied; otherwise label assumptions. APR is not the amortization note rate |
| Purchase-specific taxes and assessments | Account for location-dependent recurring costs | Use the applicable jurisdiction and purchase scenario, not automatically the seller's old bill |
| Insurance, including applicable additional coverage | Account for premium and availability | A scenario dollar allowance is not evidence that coverage is obtainable |
| HOA/condo dues and known assessments | Capture building-specific costs | Unknown is not zero; avoid double-counting services included in dues |
| Utilities and maintenance/repair allowance | Show broader housing spending | Explain allowances, distinguish ongoing upkeep from known immediate work, and keep assumptions editable |
| Price evidence with date, geography, home category and coverage | Compare the planning range with the area or candidate home | Keep list price, sale price, modeled typical value and historical Census value distinct |

For future agent access, preserve the same inputs, assumptions, dates, evidence level, unresolved fields and reasons as the human answer. An agent should not turn “area price context” into “a matching home exists.” This is an information requirement, not an API design. Household financial inputs belong in a private session, not this public repository.

## Monthly cost and cash are separate checks

Monthly housing spending = principal and interest + property taxes/assessments + insurance + applicable mortgage insurance + HOA/condo dues + utilities + maintenance allowance. Annual amounts are converted to monthly amounts. Do not add escrow payments again if their underlying taxes and insurance are already included. Travel costs can be assessed later, with a clear budget definition to avoid counting them twice.

Cash required = down payment + closing/prepaid/initial escrow amounts + moving and planned immediate work − applicable documented credits + retained reserve. The retained reserve stays with the buyer. Distinguish cash due before/at closing from the amount they want available afterward; handle deposits and prepaid periods without duplicate charges. No loan eligibility determination is made.

CFPB distinguishes the loan payment from the total payment and describes the other purchase and ownership costs. These documents supply the cost categories, not the fictional dollar assumptions below. [Total payment explanation](https://www.consumerfinance.gov/ask-cfpb/on-a-mortgage-whats-the-difference-between-my-principal-and-interest-payment-and-my-total-monthly-payment-en-1941/), [budget guidance](https://www.consumerfinance.gov/owning-a-home/prepare/figure-out-how-much-you-want-to-spend/).

For Granada Hills, California's reassessment rules are a concrete reason not to reuse an existing owner's tax bill as a new buyer's estimate. A change in ownership can trigger a new assessed value, subject to applicable exclusions. The actual parcel's taxes and assessments still need checking. [California BOE guidance](https://www.boe.ca.gov/proptaxes/faqs/changeinownership.htm).

## Fictional example calculation

All values in this section are teaching assumptions, not quotes, forecasts, local rates or observed market prices. The household's $5,000 ceiling covers the monthly categories in this document. Total cash is $195,000. A 20% down payment, $25,000 combined transaction/moving/initial costs and $25,000 retained reserve are assumed for each candidate price.

| Assumption | Lower-cost scenario | Central scenario | Higher-cost scenario |
|---|---:|---:|---:|
| Fixed note rate | 6.0% | 6.5% | 7.0% |
| Loan term | 30 years | 30 years | 30 years |
| Annual property tax as fraction of price | 1.1% | 1.2% | 1.4% |
| Monthly insurance allowance | $150 | $250 | $400 |
| Monthly utilities allowance | $200 | $250 | $350 |
| Monthly maintenance allowance | $250 | $350 | $500 |
| Monthly HOA / mortgage insurance | $0 / $0 | $0 / $0 | $0 / $0 |

The tax percentages are simplified assumptions, not jurisdictional formulas. Costs move together here solely to show sensitivity; the endpoints are not probabilities, worst-case guarantees or observed local ranges. Zero HOA and mortgage insurance describe this particular fictional loan/home. Lower down payments, other loan products, all-cash purchases and properties with fees need different calculations. Fixed maintenance allowances here are not recommended amounts for all properties.

For a fixed amortizing loan: principal L = price − down payment; monthly rate r = annual note rate / 12; n = term in months. Payment = `L × r / (1 − (1+r)^(-n))`; at zero rate, use `L/n`. Add the other monthly components once. Display rounded dollars but compare unrounded values.

With this example's fixed 20% down and linear tax assumption, the central monthly-price limit is $685,209, the lower-cost limit $770,164, and the higher-cost limit $577,893. The independent cash limit is ($195,000 − $25,000 − $25,000) / 0.20 = $725,000. Thus the lower-cost scenario would be limited by cash to $725,000, while the central and higher-cost scenarios are limited by monthly spending. Do not apply this simplified algebra unchanged to tiered taxes, financed fees, other loan products or fixed-dollar down payments.

See [saved fictional inputs/results](research/home-budget/scenarios.json) and [reproducible arithmetic](research/home-budget/calculate.py). Verification covers amortization through an independent month-by-month balance recurrence, the zero-rate case, scenario ordering and the cash cap. The script supports this teaching example only.

## Market evidence and free access

| Source reviewed | What it offers for this question | Limits and current disposition |
|---|---|---|
| [Zillow Research](https://www.zillow.com/research/data/) | Modeled typical-value series, including bedroom and home-type categories; separate listing/market aggregates | Model values are not suitable homes for sale. Exact geography/category coverage still needs a file audit. Do not infer that separate bedroom/type series supply their joint combination |
| [Zillow terms](https://www.zillow.com/corporate/terms-of-use/) | Section 4C permits certain non-personal uses and attributed derivatives of defined Local-Info Aggregate Data | This is a specific permission, not a blanket prohibition or unrestricted license. Applicability to the intended Research downloads, commercial matching service and raw agent responses remains unresolved; no production reliance selected |
| [Redfin Data Center](https://www.redfin.com/news/data-center/downloads/) and [methods](https://www.redfin.com/news/data-center/methodology/) | Downloadable market measures such as sale prices, inventory and listing measures | Useful aggregate context, not a confirmed property-level matching feed. Exact local coverage and automated commercial/agent reuse were not established in this review; [terms](https://www.redfin.com/about/terms-of-use) distinguish licensed listing content |
| [Realtor.com Research library](https://www.realtor.com/research/data/) | Monthly market aggregates down to ZIP codes; the page requests attribution and a link for use | Its stated all-home coverage pools home categories. A ZIP-wide median does not answer a three-bedroom-with-yard query. Product/API redistribution rights remain to confirm for the intended use; do not equate research aggregates with raw listings |
| [Existing Census extract](research/worked-areas/README.md) | Already inspected public historical housing/value/cost context | No current availability or new-buyer payment claim; do not mechanically inflate its median into today's price of a requested home |
| [Freddie Mac PMMS methodology](https://www.freddiemac.com/research/insight/20221103-freddie-macs-newly-enhanced-mortgage-rate-survey) | A possible dated rate benchmark | Based on a specified conventional/conforming borrower/loan profile; not an individual quote. Published rates were not used as the fictional example's assumptions |
| User-supplied candidate facts or an authorized listing feed | An actual price and home attributes can support a more direct candidate check | Retain source/date and whether details were verified. User input does not create permission to scrape or republish a provider's content. No nationwide unrestricted free matching feed has been established here |

The reviewed sources are candidates, not a finding that the product needs paid data. The usable free version can provide transparent budget scenarios and qualified area context while progressively improving the market evidence. If only broad historical data is available, label that context and leave current suitable-home availability unresolved.

## Proposed evidence rules

Use a dated matching listing or appropriately comparable recent transaction as stronger evidence than a broad area aggregate, while keeping sale versus asking price distinct. A modeled category-level value may support a rough price comparison if its geography/category and method fit. Historical Census context alone should not generate a current affordability verdict.

Keep the conclusions independent: a property can fit the monthly budget but need too much cash; fit both budgets but lack a required feature; meet the home requirements but have unverified insurance; or appear suitable in an incomplete listing sample. Report what was checked. A zero result from incomplete coverage cannot establish that an entire neighborhood has no fit.

No universal price-band thresholds, freshness cutoffs, income rules or scoring weights were validated or selected in this review. Those are implementation decisions to evaluate after reviewing the proposed scope.
