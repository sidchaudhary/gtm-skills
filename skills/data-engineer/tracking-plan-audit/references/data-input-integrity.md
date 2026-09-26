# Data Input Integrity

For every skill that computes a number from an export the user pasted: margin, cohorts, returns,
disputes, shipping, inventory, promotions, ad spend, anomalies, benchmarks, catalog.

These checks run **before** the analysis, because each one produces a confident, wrong answer rather
than an obvious error. The output looks fine. That is the problem: a broken input does not announce
itself, it just moves the number, and the number then gets acted on.

Report which checks were run and what they found. Where a check cannot be run because the export
lacks the field, say so and state what it limits the conclusion to. Do not silently proceed.

---

## 1. The partial period

**The single most common false alarm.** A month-to-date or week-to-date bucket compared against
completed periods always looks like a collapse, because it is a shorter period, not a worse one.

- Establish whether the last period in the data is complete. If the export ends mid-period, either
  exclude that bucket or mark it clearly and never include it in a trend read or a
  period-over-period delta.
- Same trap in reverse for a period that has not fully matured: returns, refunds, disputes, and
  churn all arrive weeks after the sale. Recent cohorts look better than older ones purely because
  the bad news has not landed yet.
- Say the comparison explicitly: month-to-date against the same days of the prior month is valid;
  month-to-date against a full prior month is not.

## 2. Time boundaries

- **Ask which timezone the export is in**, and whether every source in the analysis shares it. A
  store's dashboard, its payment provider, and an ad platform commonly use three different
  conventions, and a "day" that starts at a different hour shifts revenue between buckets.
- This is how ROAS gets misattributed: daily spend on the platform's timezone divided by daily
  revenue on the store's timezone, with a shifting overlap. The number is plausible and wrong every
  day.
- For weekly aggregation, confirm which day starts the week. Different tools default differently,
  and a one-day shift moves a weekend into a different bucket.
- Where sources cannot be aligned, aggregate to a period long enough that the boundary stops
  mattering (weekly or monthly), and say why.

## 3. Currency

- Ask whether the export is single-currency. A store selling internationally often exports in the
  customer's presentment currency, so summing the amount column adds different units together.
- If multi-currency, require a converted column or the rate used. Never convert at today's rate for
  historical rows without saying so: the number becomes a mix of trading performance and FX
  movement, and margin work is the place this does the most damage.
- Confirm whether amounts include or exclude tax and shipping. Revenue, margin, and AOV all change
  materially, and exports differ.

## 4. What counts as a row

- **Test and internal orders.** Staff purchases, QA transactions, zero-value orders, and 100%-discount
  orders inflate counts and distort average order value. Ask how they are marked and exclude them.
- **Cancelled and fully refunded orders.** Decide explicitly whether they are in scope, and apply it
  consistently. Counting a cancelled order as revenue and again as a refund double-counts it.
- **Duplicate rows.** Paginated exports and joins produce repeats. Check the row count against a
  known total, or check for duplicate order IDs, before trusting any sum.
- **Line items versus orders.** An export at line-item granularity has one row per product, so
  counting rows counts products, not orders, and per-order averages come out wrong by the average
  basket size.
- **Which date is the row dated by?** Order date, ship date, payment capture, refund date, or
  dispute-filing date. For anything measuring the performance of a sale, date it to the **sale**,
  not to when the consequence was recorded. A dispute filed in March against a January order belongs
  to January.

## 5. Minimum volume before a rate means anything

A rate computed on a tiny denominator is noise wearing the costume of a finding.

- **Always show the denominator** next to any rate. A 33% return rate is one return out of three
  orders, which is not a signal.
- Set and state a floor below which a per-item rate is reported as "insufficient volume" rather than
  as a number. Roughly 30 units for a rough read and closer to 100 for anything driving spend is a
  reasonable default; state whichever floor is used.
- **Rank by absolute impact, not by rate**, when deciding what to act on. The worst rate in a
  catalog is usually a low-volume item, and the money is in a mediocre rate on a high-volume one.
- A long-tail item's rate will always look extreme in both directions. Do not read either tail as a
  finding without volume behind it.

## 6. Completeness of the field, not just the file

- Check for nulls and defaults in the columns the calculation depends on, and count them. A cost
  column that is blank for 30% of SKUs produces a margin figure that quietly describes only the
  other 70%.
- Watch for placeholder values standing in for missing data: `0`, `1`, `9999`, `-1`, and `N/A`
  parsed as a number. A zero cost reads as infinite margin.
- Confirm the export covers the whole period claimed, rather than being truncated by a row limit.
  Many tools cap an export silently.

## 7. Report the checks

Every output includes a short data-integrity note stating:

- The period covered, and whether the final period is complete
- The timezone and, where multiple sources are combined, how they were aligned
- The currency, and whether amounts include tax and shipping
- What was excluded (test orders, cancellations, duplicates) and how many rows that removed
- The volume floor used for per-item rates
- Any field with material missing values, with the share missing
- Which checks could not be run because the export lacks the field, and what that limits the
  conclusion to

If a check fails in a way that undermines the analysis, say the analysis is blocked on the data
rather than producing a number with a caveat attached. A caveat under a confident number gets
skipped; a stated blocker does not.
