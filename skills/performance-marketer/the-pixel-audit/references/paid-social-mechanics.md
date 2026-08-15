# Paid Social Mechanics (Meta)

The mechanical facts the paid-social skills depend on: account structure, the learning phase, event
tracking and deduplication, catalog requirements, lead-form mechanics, and why fatigue baselines
have to be per-ad.

**On staleness.** Meta changes delivery, targeting options and reporting faster than any reference
file. Structure, the learning-phase concept, and event deduplication are stable. Targeting options,
objective names and specific thresholds are not - interest categories were retired, exclusion options
were removed, and delivery moved toward reading the ad itself rather than the audience selection.
Where a number here would decide a spend, verify it against Meta's own documentation in the same
session, and say where the figure came from. Never present a threshold from this file as a current
platform guarantee.

---

## 1. Structure, and why simple wins at small budgets

Three levels, each owning different decisions:

| Level | Owns |
|---|---|
| **Campaign** | The objective, and the budget when campaign-level budget is on |
| **Ad set** | Audience, placements, the optimisation event, schedule, and the budget when ad-set budget is on |
| **Ad** | The creative - copy, image or video, format, destination |

The optimisation event lives at the **ad set**, which is why two ad sets optimising for different
events cannot be compared as though they were the same test.

**Budget fragmentation is the small-budget failure.** Every ad set needs its own volume of
optimisation events to leave learning. Splitting a modest budget across many ad sets gives each one
too little signal, so none of them ever stabilises. One campaign, one broad ad set, and several
genuinely different ads is the structure that concentrates signal rather than diluting it.

**Delivery reads the creative.** With interest-based micro-targeting reduced, the specificity of the
ad itself is the main aiming mechanism left. A generic ad gives the system nothing to aim with. This
is why an angle is a targeting decision, not just a copy decision, and why "my ad went to the wrong
people" is usually a message problem wearing a targeting costume.

## 2. The learning phase

An ad set is in learning while delivery is still unstable. It exits once it accumulates enough
optimisation events in a rolling window - the commonly cited figure is around 50 in 7 days, and it
should be treated as an order of magnitude rather than a promise.

**Significant edits restart learning.** Roughly: changes to targeting, the optimisation event, the
creative, or large budget or bid moves. Minor edits generally do not. This is the mechanism behind
the whole "read daily, act rarely" discipline - frequent edits keep resetting the clock, so the ad
set never gets to a stable state and every result is measured mid-learning.

**"Learning limited"** means the ad set is not getting enough weekly events to stabilise at all. The
fixes are structural (consolidate ad sets, widen the audience, choose an event that happens more
often), not creative.

**Scaling implication.** A large budget jump is a significant edit. Incremental steps - the widely
used rule of thumb is around 20% and no more than once a day - are an attempt to add budget without
tripping the reset. The number is a convention, not a published threshold; treat it as the
conservative default and say so.

## 3. Pixel, Conversions API, and deduplication

Two paths report the same events: the browser pixel and the server-side Conversions API. Running both
improves coverage where browsers block the pixel, and **creates double counting unless deduplication
is configured correctly.**

- **Deduplication key**: the pair of `event_name` and `event_id`. Both paths must send the *same*
  `event_id` for the *same* user action. A missing or mismatched `event_id` means one purchase
  counted twice, and every downstream number inflated.
- **Standard events** - `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`,
  `Lead`, `CompleteRegistration`, `Subscribe` and others - carry known semantics and can be used for
  optimisation. Custom events can be tracked but need custom conversions defined to optimise toward.
- **Event match quality** scores how well the customer information sent with server events resolves
  to a person. Low match quality degrades both attribution and optimisation, quietly.
- **`fbp` and `fbc`** are the browser and click identifier cookies. Forwarding them with server
  events is usually what lifts match quality most.
- **Aggregated Event Measurement** limits how many conversion events a verified domain can optimise
  for and requires them to be ranked in priority order. Events below the cut are still recorded but
  behave differently for opted-out traffic. Domain verification is the prerequisite.

**The audit rule:** a purchase count that suddenly doubles is far more often a deduplication break
than a doubling of sales. Check the tracking before believing the result, in either direction.

## 4. Attribution windows and modelled conversions

- The common default is **7-day click, 1-day view**. Changing the window changes reported results
  without anything about the business changing.
- **View-through conversions** credit an impression with no click. They are legitimate for some
  businesses and pure flattery for others; report them separately from click-through, never merged.
- Some reported conversions are **modelled** - statistically estimated to fill gaps left by opted-out
  users, not individually observed. A modelled figure cannot be reconciled row-by-row against a CRM,
  and trying to is a common source of wasted afternoons.
- **Platform-reported return is not incremental return.** The platform grades its own homework. An
  honest read states what the platform claims, what it cannot know, and what would need a holdout
  test to establish.

## 5. Catalog and product sets

Dynamic ads pull live product data from a catalog. The catalog is the dependency; a broken one
automates showing people the wrong thing.

Fields that are effectively required for a product to serve: `id`, `title`, `description`,
`availability`, `condition`, `price`, `link`, `image_link`, and `brand`. `sale_price`,
`item_group_id` (for variants) and `google_product_category` matter for merchandising and grouping.

- **`item_group_id` is the variant grain.** An ad targeting a variant must be checked against that
  variant's stock, not the parent product's. Checking a variant ad against parent-level stock is how
  spend continues on a sold-out size.
- **A product set is a filter over the catalog**, and each set is really a different promise: best
  sellers, under fifty, new arrivals, a seasonal range. Treating sets as angles rather than as
  folders is what makes dynamic ads work.
- **Order of operations is fixed**: tracking verified first, catalog second, product sets third,
  retargeting last. Building retargeting on an unverified pixel produces confident targeting of the
  wrong people.

## 6. Lead forms

- **Form type is the volume/quality dial.** The "more volume" style optimises for completion; the
  "higher intent" style adds a review step before submission. The review step reliably reduces
  volume and reliably raises quality.
- **Question types**: prefilled contact fields, short answer, multiple choice, conditional questions,
  and appointment requests. **A single custom qualifying question filters more junk than any
  targeting setting**, because it costs the submitter effort that a bot or an idle browser will not
  spend.
- The real cost of a bad lead is the follow-up time it burns, which is why trading volume for
  qualification is usually correct for service businesses and usually wrong for high-volume ecommerce.
- Forms should be **drafted and reviewed before publishing**: a live form collecting the wrong fields
  produces leads that cannot be actioned, and the fields cannot be changed retroactively for records
  already captured.

## 7. Fatigue - and why the baseline must be per-ad

**Frequency** is average impressions per person in a date range. It rises fastest on small audiences
and high budgets.

The two-condition rule the skills use - frequency above roughly 4.0 **and** click-through down about
30% **against that ad's own earlier baseline** - exists to cut false alarms. Each half alone is a
bad test:

- Frequency alone flags every long-running ad in a small market, including profitable ones.
- A click-through drop alone can be seasonality, an auction shift, a tracking break, or a landing
  page that went down.

**The baseline must be the ad's own history, never another ad's and never the account average.**
Creative formats have structurally different click-through rates, so comparing across ads
manufactures fake fatigue in the lower-rate format and hides real fatigue in the higher-rate one.

**Fatigue scales with spend more than with elapsed time.** A small budget reaching a large audience
fatigues slowly; the same creative at ten times the spend fatigues in a fraction of the days. Advice
framed in calendar time ("refresh every 30 days", "20 new ads a month") is spend-level advice in
disguise.

Before concluding fatigue, rule out: a tracking break, a landing page or checkout failure, a
seasonal shift, a competitor's budget arriving in the auction, and a recent significant edit that
put the ad set back into learning.
