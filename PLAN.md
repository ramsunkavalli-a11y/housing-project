# Purchase-focused project plan

Updated: 2026-10-02

**Primary objective: help the owner purchase a suitable home with clear evidence and understandable tradeoffs.** Possible public distribution comes later. The owner's preference is to follow work through Git.

The workflow below is a proposed sequence for applying the existing research to the purchase. It does not select a new application architecture, market-data provider, scoring formula, lender, or property.

## Next milestone

Prepare a dated comparison of a few realistic candidates with explicit requirements, itemized cost scenarios, supporting evidence, and the unknowns most likely to change the decision. Actual household and candidate records belong in a private workspace; the proposed home is the existing private [next-house-hunt repository](https://github.com/ramsunkavalli-a11y/next-house-hunt).

| Order | Work | Reviewable output | What counts as progress |
|---|---|---|---|
| 1 | Reconcile existing purchase context | One current purchase brief: requirements, preferences, financial boundaries, regular destinations and schedules | Existing records reviewed; changed or unconfirmed inputs identified instead of starting the interview over |
| 2 | Refresh candidate evidence | A dated candidate list with source links, status, relevant home features, and unresolved requirements | Current candidates separated from historical examples; incomplete search coverage made explicit |
| 3 | Compare costs and financing | Itemized monthly spending, cash due, retained reserve, and comparable financing scenarios | Actual quotes separated from assumptions; unknown costs kept visible |
| 4 | Check daily life and consequential risks | Relevant trips, school/program eligibility where needed, usable outdoor space, services, condition and insurance questions | Address-level evidence and visit/document checks replace broad proxies where the decision requires them |
| 5 | Build the shortlist | Side-by-side reasons, supported conflicts, missing evidence, and next actions | Scoring inputs are traceable; unresolved requirements remain unresolved; sensitivity shows what could change the order |
| 6 | Support a purchase decision | Comparable offer/cost scenarios and a due-diligence record | Questions, documents, dates, responsible parties, and decision reasons remain easy to follow |
| 7 | Learn from the outcome | A short record of what helped, failed, or changed the decision | Reusable methods improved using the actual experience; public examples use fictional or appropriately cleared information |

Research and comparison do not authorize contacting third parties, submitting offers, committing funds, or changing repository visibility.

## Evidence required for a serious candidate

- Requirements: pass, supported conflict, or unresolved, with the relevant source or observation.
- Costs: financing, purchase-specific taxes, insurance, applicable dues and mortgage insurance, utilities, maintenance, and known initial work. Unknown is not zero.
- Cash: down payment, transaction/prepaid costs, moving and initial work, applicable documented credits, and money retained afterward. Keep cash paid separate from retained reserves.
- Travel: home-to-destination direction, actual schedule and mode, source/date, and reliability limits. Generic off-peak or reverse-direction routes cannot establish a peak commute.
- Property and daily life: user-relevant amenities, school assignment/eligibility where applicable, usable space, condition, restrictions, hazards, and insurance evidence.
- Decision: why the candidate is worth investigating, what is unresolved, and which next check could alter the conclusion.

A weighted score summarizes supported preference judgments. Keep hard requirements and evidence completeness visible alongside it. Do not fill an unknown with an average or publish a precise final ranking that depends on an unresolved material input. Any change to the owner's existing scoring rules remains a proposal until agreed.

## Working through Git

1. Read the current brief and decision record before starting a task.
2. Make one focused change on a branch; use a clear commit message.
3. Open a pull request describing the resulting behavior or document change and relevant checks.
4. Record meaningful decisions and their reasons; label proposals and incomplete checks accurately.
5. Keep the current milestone and outstanding questions visible in the private purchase records.

Routine research, documentation, and corrections can proceed within the authorized task. Major implementation decisions still need a concrete explanation before adoption.

## Current status

- [x] Review the public research and existing private house-hunt context.
- [x] Record the owner's purchase-first direction and preference for Git.
- [ ] Reconcile the current private brief and identify stale or unconfirmed inputs.
- [ ] Refresh serious candidates and their decision-changing evidence.
- [ ] Prepare the first current comparison under the proposed workflow.
- [ ] Record what changed the shortlist and the next purchase decisions.

Documenting a workflow does not mean those purchase checks have been performed.

## Research already completed

The earlier neighborhood comparison, literature sweep, candidate inventory, source catalog, two-place ACS/EPA audit, and fictional budget example remain available through the [README](README.md). They establish limited research results, not current market coverage or household fit.

[Home-and-budget research](docs/home-and-budget.md) remains useful for the cost categories and distinction between a workable budget and observed suitable homes. Its prices, rates, and allowances are fictional. [Buyer decisions](docs/buyer-decisions.md) remain the test for collecting additional evidence.

## Deferred public-distribution work

Keep these as future possibilities, outside the active purchase milestone:

- Nationwide data ingestion and a universal neighborhood-boundary strategy.
- Generalized intake, group matching, and validated public scoring defaults.
- Public website, external agent access, hosting, and operational refresh services.
- Public-data redistribution design, broader evaluation, launch experiments, and revenue.

Source terms still apply to research and private use now; public-display and redistribution questions need resolution if that distribution is pursued. Broad coverage and free data were earlier product priorities; local usefulness now determines what evidence to obtain.
