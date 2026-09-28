# Audit Findings Discipline

For every skill that inspects something and returns findings: checkout, product pages, catalogs,
feeds, onsite search, citability, launch readiness.

These skills are already careful about **evidence**, separating what was confirmed from what was
inferred, refusing to invent values, declining to promise a conversion lift. This file covers what
happens to a finding *after* it is written, which is where audits usually stop being useful:

- An audit is a snapshot with no stated expiry, so it gets cited months later against something that
  has changed.
- Findings are ranked by severity alone, so the list starts with the expensive items and stalls.
- All the fixes ship at once with no before-measurement, so nothing is attributable and the next
  audit starts from the same place.

---

## 1. An audit is dated, and it expires

Every audit output carries:

- **Audited on**, the date, and for anything fetched, the date fetched.
- **What was actually inspected**, the specific pages, SKUs, queries, or feed rows, and on which
  device or variant. "The checkout" is not a scope; "mobile Safari, guest checkout, one product in
  cart, UK address" is.
- **Re-audit trigger**, the event that makes this audit stale rather than a fixed interval. A
  checkout audit expires on any change to the checkout, the payment methods, or the shipping rules.
  A feed audit expires on a channel policy update or a catalog restructure. A citability audit
  expires when the page is rewritten or the site's robots policy changes.

State plainly that findings not acted on within the re-audit window need re-verifying before they are
worked. A stale finding is worse than a missing one, because it gets fixed with confidence and the
fix lands on something that already moved.

---

## 2. Rank by severity **and** effort, and say which is which

A single ranked list conflates two different questions and produces a list nobody finishes. Every
finding carries both:

- **Severity**, what it costs if left alone. Prefer a mechanism over an adjective: "blocks approval
  on this channel", "no payment method for this market", "the page never answers the price question".
- **Effort**, the honest cost to fix: a copy change, a template change, a config change, or an
  engineering ticket. If it is unknown, say unknown rather than guessing low.

Group the output so the sequence is obvious:

| Group | Severity | Effort | What it means |
|---|---|---|---|
| **Do now** | High | Low | Ship this week. Anything here that is still open at the next audit is a process problem, not a backlog problem. |
| **Plan** | High | High | Needs a ticket, an owner, and a date. Do not let it sit in a list with copy tweaks. |
| **Cheap wins** | Low | Low | Batch them. Individually marginal, collectively worth one pass. |
| **Leave** | Low | High | Name it and explicitly park it, so the next audit does not rediscover it as if it were new. |

**Never present a flat ranked list without effort.** A list whose first three items each need
engineering is a list that does not get started.

---

## 3. Make the fixes attributable

An audit's value is realised only if someone can tell afterwards whether it worked. Two things
routinely prevent that, and both are cheap to avoid.

**Capture the baseline before anything changes.** For each finding that has a measurable
consequence, name the metric and its current value, or state that it is not currently measured. A
finding whose metric is not instrumented has a prerequisite: instrument it first. That is itself a
recommendation, and often the highest-value one in the audit.

**Sequence the fixes rather than shipping them together.** Five simultaneous changes produce one
unattributable movement, so nothing is learned and the same debate repeats at the next audit. In
priority order:

1. Ship the single highest-severity, lowest-effort fix on its own, with its baseline recorded.
2. Batch the cheap wins together, individually too small to measure, and that is fine, so long as
   nobody later claims a specific one caused the change.
3. Give each high-effort item its own measurement window.

Where traffic is too low for anything to be measurable, **say so** rather than implying
attribution is available. In that case the honest framing is that these are changes made on
judgment and evidence, not experiments, and the audit should say which.

**Do not promise a lift.** Naming the mechanism ("this removes a required field that has no
downstream use") is defensible. A percentage is not, and a predicted number quoted back later is how
an audit loses credibility.

---

## 4. Close the loop

Every audit ends with what the next one needs:

- **What was parked**, and why, so it is not rediscovered as new.
- **What could not be verified**, and the specific data or access that would settle it.
- **What to check first next time**, based on what was shipped from this audit.

An audit that does not reference the previous one produces the same top-five findings indefinitely.

---

## 5. Check before returning

1. Does the output carry an audit date, the exact scope inspected (including device or variant), and
   a re-audit trigger stated as an event rather than an interval?
2. Does every finding carry both severity and effort, with unknown effort stated rather than guessed?
3. Are findings grouped so the sequence is obvious, rather than presented as one flat ranked list?
4. Is there a named baseline metric and current value for every finding with a measurable
   consequence, or an explicit note that it is not instrumented and that instrumenting it comes
   first?
5. Does the output say which fix to ship alone, which to batch, and why, rather than handing over a
   list to be shipped at once?
6. Where traffic is too low for attribution, is that stated instead of implying the changes can be
   measured?
7. Is every parked item named as parked, and every unverifiable item named with what would settle it?
8. Is no conversion lift promised anywhere, with mechanisms described instead of predicted numbers?
