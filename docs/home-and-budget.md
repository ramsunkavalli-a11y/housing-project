# Can I find the home I want here within my budget?

Component review, 2026-09-27. **Recommendation: estimate a useful purchase-price range, then compare it with evidence about suitable homes in each area.** Keep those two answers separate. A payment calculation cannot establish that the desired home exists; a low area median cannot establish that the household can buy it.

This is a proposal for discussion before implementation. The research and fictional arithmetic example are complete; no market-data provider, calculator defaults or website changes have been selected.

## Ask four useful questions, with follow-ups only when needed

| Opening question | Follow-up when relevant | What it changes |
|---|---|---|
| What must the home have? | Bedrooms; usable outdoor space; parking; stairs/accessibility; acceptable home types. Separate must-haves from preferences | The homes whose prices are relevant |
| Do you have a purchase-price range, a comfortable monthly amount, or neither yet? | Clarify what the monthly amount includes. Allow a preferred amount and a firm ceiling | The budget comparison; users with a price range can start without a financial interview |
| How much cash can go toward the purchase? | For the monthly-cost route: down payment, closing/moving/initial work, and money to keep untouched. All-cash buyers skip loan questions | Whether the purchase needs more cash than is available |
| What are you flexible about? | For example, smaller yard, different home type, timing, or location. Never change a must-have without the user's choice | Which alternatives to show if the search is tight |

If someone already has a lender quote or a candidate home's costs, use those dated inputs. Otherwise show editable assumptions or leave that portion unassessed. “I don't know yet” should preserve progress. A first-pass neighborhood search need not collect salary, credit score, or every debt; calculating what payment a user wants is different from predicting loan approval. For a group, do not silently average different budgets or erase one person's requirement.

## The answer should be simple

Show the household's needs, estimated purchase range, what drives that range, and whether there is relevant market evidence for the area. Offer these kinds of conclusions:

- **Worth checking:** relevant price evidence overlaps the budget; say whether it is an area estimate, recent sale, or observed listing.
- **Budget may be tight:** the relevant evidence is generally above the planning range or the costs cross the monthly ceiling under plausible assumptions. Keep exceptions visible.
- **A specific option conflicts:** an observed candidate fails an explicit requirement or exceeds the chosen budget under stated costs. That is a conclusion about the candidate, not proof that its whole neighborhood fails.
- **Not enough evidence:** suitable-home prices, important costs or required features remain unverified. Explain the next useful check.

“No matches in the data we checked” is a coverage-limited result. An area median above the budget is not a reason to declare that no affordable home exists.

## A worked example

**Entirely fictional household and prices; these are not Granada Hills or Ames market estimates.** The household wants three bedrooms and usable outdoor space, sets a **$5,000 monthly housing-spending ceiling**, and has **$195,000 cash**. The example uses 20% down, $25,000 for closing/moving/initial costs, and $25,000 retained cash. Twenty percent is an example assumption, not a required down payment.

The monthly estimate includes principal and interest, taxes, insurance, HOA/mortgage insurance where applicable, utilities, and a maintenance allowance. This is broader than the mortgage payment. [CFPB budget guidance](https://www.consumerfinance.gov/owning-a-home/prepare/figure-out-how-much-you-want-to-spend/).

| Hypothetical purchase | Central monthly estimate | Lower-to-higher cost scenarios | Cash needed including retained reserve | Useful conclusion |
|---|---:|---:|---:|---|
| $550,000 | $4,181 | $3,742–$4,819 | $160,000 | Within both limits in the scenarios shown; suitable-home availability still needs evidence |
| $650,000 | $4,787 | $4,313–$5,468 | $180,000 | Cash fits; monthly spending is sensitive to the actual costs |
| $750,000 | $5,392 | $4,885–$6,117 | $200,000 | Central monthly estimate is over budget and this down-payment plan needs $5,000 more cash |

For the $650,000 example, the central monthly breakdown is approximately **$3,287 loan payment + $650 taxes + $250 insurance + $250 utilities + $350 maintenance**. HOA and mortgage insurance are explicitly assumed zero for this fictional scenario, not filled with zero when unknown.

At the central assumptions the monthly ceiling corresponds to about **$685,000** purchase price; the higher-cost scenario reduces it to about **$578,000**. The cash plan independently caps price at **$725,000**. These scenario results illustrate why a single precise “you can afford” number would mislead. The bands are assumption sensitivity, not statistical confidence intervals. [All assumptions and calculations](home-and-budget-evidence.md#fictional-example-calculation).

The next buyer-facing step is concrete: **check whether three-bedroom homes with usable outdoor space are actually plausible around the resulting range.** The calculation itself cannot answer that.

## What a free first version can do

It can explain monthly cost and upfront cash using user inputs, transparent assumptions and public guidance. It can use dated aggregate market evidence for rough area comparisons where coverage and reuse terms support it, and allow the user to refine the calculation with facts about a candidate home. It can distinguish an estimated price range from an observed suitable option.

The source review found public market summaries from Zillow, Redfin and Realtor.com, but did not establish a comprehensive, unrestricted free feed of current homes matching bedrooms, yard and other requirements. Aggregate summaries differ from listing records, and a ZIP code differs from a named neighborhood. Production reuse and agent redistribution need source-specific decisions. [Source review](home-and-budget-evidence.md#market-evidence-and-free-access).

**Proposed first scope:** rough neighborhood affordability screening plus an optional cost check for a candidate price/home. Keep current inventory matching as a separate capability until the evidence source is settled. For Granada Hills and Ames, the existing Census audit alone supports no current claim that the requested home is available within budget.
