# Paid Search Mechanics (Google Ads)

The mechanical facts the paid-search skills depend on: asset limits, match-type semantics, the
Quality Score components, conversion-action settings, bid-strategy families, and the order in which
delivery problems have to be diagnosed.

**On staleness.** Google changes limits, strategy names and reporting more often than a reference
file gets updated. Character limits and the match-type rules below are the most stable part of this
document and have held for years. The bid-strategy roster and the reporting columns are the least
stable. Where a number here decides whether something ships - a headline that must fit, a negative
that must not block a real query - verify it against Google's own help pages in the same session.
Never quote a figure from here to a user as current without saying where it came from.

---

## 1. Responsive search ad assets and their limits

A responsive search ad is a pool of assets Google assembles at auction time. Every asset has to read
correctly alone and beside any other, because you do not control the combination.

| Asset | How many | Character limit |
|---|---|---|
| Headline | up to 15, minimum 3 | **30** |
| Description | up to 4, minimum 2 | **90** |
| Display path | 2 fields | **15** each |
| Sitelink link text | - | **25** |
| Sitelink description line | 2 lines | **35** each |
| Callout | - | **25** |
| Structured snippet value | - | **25** |

Counting rules that catch people out:

- **Spaces and punctuation count.** So do emoji, which are also usually disallowed.
- **Double-width characters** (Chinese, Japanese, Korean) count as two, so the practical limit in
  those languages is half.
- A **pinned** asset stops rotating. Pinning headline 1 guarantees the message but throws away most
  of the combinatorial testing the format exists for. Pin only where a legal or brand requirement
  makes the rotation unacceptable, and say that is why.
- **Ad strength** ("Poor" through "Excellent") is a feedback signal about asset diversity, not a
  ranking factor and not a performance guarantee. Do not trade a true claim for a better rating.

## 2. Match types, and the asymmetry that matters

**Positive keywords** match on three types, and all three match *close variants* - misspellings,
singular and plural, stemming, abbreviations, accents, and reordering that preserves meaning:

- **Broad** - may serve on queries related by meaning, not just by word. The widest, and the one that
  relies most on the bidding signal being trustworthy.
- **Phrase** (`"..."`) - the meaning of the phrase must be contained in the query.
- **Exact** (`[...]`) - the query must have the same meaning as the keyword.

**Negative keywords behave differently, and this is where damage happens:**

- Negatives **do not match close variants**. A negative for `free` does not block `frees` or a
  misspelling. Blocking a concept therefore takes several negatives, not one.
- **Negative broad**: every term must appear in the query, in any order. `free trial` blocks
  "trial free software" but not "free software".
- **Negative phrase**: the terms must appear in that order.
- **Negative exact**: only the exact query.
- Negatives have **no close-variant safety net in the other direction either** - a negative that is
  too broad silently removes real demand and leaves no report row saying so. That absence of
  evidence is why a negative gets tested against protected queries *before* it is added, never after.

## 3. Quality Score: a diagnostic, not a KPI

Quality Score is a 1-10 keyword-level estimate, reported historically. It is **not** the number the
auction uses - Ad Rank is computed live from bid, ad and landing-page quality, context, and expected
impact of formats. Chasing the number rather than the component is the classic error.

The three components each report **Below average / Average / Above average**, and the rating is
relative to other advertisers on the same keyword:

| Component | What it actually measures | Where the fix lives |
|---|---|---|
| **Expected click-through rate** | Likelihood of a click when the keyword's query triggers, normalised for position | Ad copy relevance to the query, and offer strength |
| **Ad relevance** | How closely the ad's message matches the query's intent | Ad-group tightness: one intent per ad group |
| **Landing-page experience** | Usefulness, transparency and navigability of the destination | The page, not the ad |

Two rules: **"Below average" on one component beats a low composite score as a work item**, and a
keyword with excellent business results and a mediocre Quality Score is not a problem to solve.

## 4. Conversion actions - what bidding is actually chasing

Bidding optimises the goal it is handed. Every failure below produces confident bidding toward
something nobody wanted.

- **Primary vs secondary.** Primary actions count in the `Conversions` column and **are what bid
  strategies optimise toward**. Secondary actions report into `All conversions` and are observational.
  A page view left as primary will drown a demo request that happens fifty times less often.
- **Count: Every vs One.** `Every` suits ecommerce, where a repeat purchase is a repeat conversion.
  `One` suits lead gen, where one person submitting a form five times is one lead. `Every` on a lead
  form is a common and expensive misconfiguration.
- **Duplicate counting.** Two actions can record the same event - a thank-you-page action and an
  imported CRM action for the same submission. Both primary means the account is double-counting and
  bidding on inflated volume.
- **Conversion window.** Click-through windows run 1-90 days. A long window inflates recent-looking
  performance and delays the point at which a period can be judged.
- **Conversion delay** is the lag between click and conversion. **A period is not final until the
  delay has passed.** Judging a week two days after it closed, on a business with a fourteen-day
  consideration cycle, reliably produces a wrong verdict.
- **Attribution model** determines how credit is split across the path. Data-driven is the default
  where volume supports it. Changing the model changes historical numbers, which makes any
  before-and-after comparison across the change invalid.
- **Value accuracy.** Value-based bidding is only as good as the values sent. Static placeholder
  values make target-return bidding meaningless while looking perfectly healthy.

## 5. Bid strategy families

| Family | Optimises for | Needs |
|---|---|---|
| Manual CPC | Nothing automatically | Hands-on management |
| Maximize clicks | Click volume within budget | Almost nothing - a volume strategy, not an outcome one |
| Maximize conversions (optional target CPA) | Conversion count | A trustworthy primary action and enough recent volume |
| Maximize conversion value (optional target ROAS) | Conversion value | Accurate, varying values - not a flat placeholder |
| Target impression share | Visibility at a chosen position | A reason that visibility is the goal |

- **There is no universal conversion threshold** that makes a smart strategy safe. Volume matters,
  but so do conversion quality, delay, value accuracy, budget pressure and how recently the account
  changed. Any skill quoting a hard "you need N conversions per month" is overstating a rule of thumb.
- **The learning period** follows a significant change - strategy, target, or a large budget move.
  Performance during it is not evidence. Judge after it, and after the conversion delay.
- **Change one major variable at a time.** A strategy switch made alongside a budget increase cannot
  be attributed to either.

## 6. Delivery blockers, in dependency order

Diagnose in this order. A finding at a lower level is meaningless while a higher one is unresolved,
and reporting them flat as a list of "possible causes" is how a diagnosis becomes a guess.

1. **Account status** - suspended, billing failure, payment method expired. Nothing below matters.
2. **Campaign status and status reason** - paused, ended, pending start, removed. The status *reason*
   is the useful field: "Limited by budget", "Bid strategy learning", "Low search volume".
3. **Policy: disapprovals and limited approvals.** An ad limited rather than disapproved still serves,
   but narrowly, which looks like a delivery mystery rather than a policy state.
4. **Budget** - daily budget exhausted, shared budget starved by a sibling campaign.
5. **Ad Rank thresholds** - bid or quality too low to clear the reserve for the query.
6. **Destination** - landing page down, redirect loop, final URL mismatched to the display URL,
   destination blocked by robots or geography.
7. **Conversion tracking** - a tag that stopped firing turns "conversions fell" into a reporting
   artefact rather than a delivery problem. Check before concluding anything about performance.

Keep **observed** blockers (a disapproval you can see) separate from **suspected** causes (rank
pressure you inferred). Flattening the two into one confident narrative is the most common way this
diagnosis misleads.

## 7. What the search-terms report does not show

The report omits queries with very low activity, and has done since 2020. So:

- A search-term review covers **reported terms, not every search that served**. Say so in the output.
- The spend total of exclude candidates is a share of **the rows in the report**, not of account
  spend, unless total account spend was supplied separately.
- A keyword can accumulate cost through queries that never appear individually in the report.
