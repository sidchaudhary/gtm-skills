# Missing Input Protocol

What to do when a required input, source, or field is not available. This is the single most common
way a skill in this pack produces a confidently wrong answer: not by reasoning badly, but by filling
a hole silently.

The rule underneath all of it: **an absent input is a finding, not an inconvenience.** It gets
reported with the same prominence as a result, because the user cannot judge an output without
knowing what it was missing.

---

## The four responses, and how to choose

Every missing input resolves to exactly one of these. Pick deliberately; do not default.

| Response | When | What it looks like |
|---|---|---|
| **Block** | The output would be unsafe, non-compliant, or actively misleading without it | Return no deliverable. State the one input needed and why it gates everything. |
| **Withhold** | The overall output is sound but one figure or field would be fabricated | Deliver everything else. Print `withheld — <field> missing` where the number would go. Never a placeholder that reads like a value. |
| **Degrade** | A weaker but still honest version exists | Deliver it, name the tier explicitly ("terciles not quintiles, because n=140"), and say what the stronger version would need. |
| **Assume** | A conventional default exists and the answer is not sensitive to it | State the assumption inline at the point of use, not in a footnote. |

**Never a fifth option.** Do not proceed as if the input were present, do not guess a number, and do
not omit the field silently so the gap is invisible.

### Blocking is rare and specific

Block only for: a suppression or consent gate, a compliance field required for lawful sending, an
irreversible action, or a case where every possible value of the missing input changes the
recommendation. Everything else degrades or withholds. A skill that blocks on anything convenient
becomes a skill users stop running.

---

## Required output fields with no input

If a required section of the output format depends on an input the skill never asks for, that is a
defect in the skill, not a problem with the user's data. Two obligations:

1. **Print the field with `not supplied` and say what it would change.** A Coverage Ratio row that
   silently disappears reads as an oversight; one that says `not supplied — needs your quota target,
   which decides whether this pipeline is thin or healthy` is useful.
2. **Ask for it.** Once, specifically, at the end. Not as a generic "let me know if you have more
   data."

---

## Failed fetches and unreachable sources

A source that could not be retrieved is different from a source that returned nothing, and both are
different from a source that was never tried. Record which.

- **State the failure and the URL.** `plausible.io/pricing returned 404` is auditable; "pricing
  information was limited" is not.
- **A substitute source is labelled as one.** If a number came from a third party rather than from
  the company's own page, say so at the point the number appears, not only in a sources list. The
  reader will otherwise treat it as first-party.
- **Never let a substitute inherit the authority of the original.** Third-party pricing may be
  stale, tier names may be renamed, and the discrepancy is invisible in the output.
- **Say what the failure cost.** If the unfetched page was the one that would have answered the
  question the output most needs, that is the headline, not a footnote.

---

## Absent versus zero versus not-applicable

These three are routinely collapsed and they mean opposite things.

| State | Meaning | Handling |
|---|---|---|
| **Zero** | Measured, and the value is nought | Use it |
| **Absent** | Not measured, value unknown | Withhold anything derived from it; exclude the row from any ranking by an absolute amount |
| **Not applicable** | The field cannot apply to this row | Exclude from denominators, state the exclusion count |

A cost column of `0` and a cost column that is blank produce the same arithmetic and opposite
truths. A blank cost read as zero yields infinite margin, and the affected row usually ranks first.

---

## Derived versus observed

When a list, pattern, or profile is built from what is *absent* rather than what is present, label
it. The two look identical in an output and support completely different decisions.

- A banned-word list built from words found in the copy is **observed**.
- The same list built because the copy was clean and a default set was applied is **derived**.

Write which. `derived — none of these appeared in the samples; applied as a default set` costs one
line and prevents a user from believing their writers have a habit they do not have.

---

## Volume and sample floors

Percentages on small denominators are the most persuasive wrong output an agent produces, because
they are formatted identically to reliable ones.

- **State n next to every rate.** Always, not only when it is small.
- **Name the minimum that would support the claim** rather than asserting the sample is adequate.
- Where n is below that minimum, either withhold the rate and give the raw counts, or degrade to a
  coarser cut and say so.
- **A cohort, segment, or band below the floor is still shown** — it is not deleted — but it is
  marked, and it is excluded from any ranking or conclusion.

---

## Staleness

Every input has an age, and for some the age matters more than the content.

- **Record the date of every input**, including exports and pasted data.
- **Say what the input's useful life is** where it is short: inventory on hand and live ad spend
  decay in a day, a competitor's pricing page in months, a firmographic record in a year.
- **Where an input is past its useful life, treat the analysis as historical rather than current**,
  and say which. A seven-day-old stock figure cannot support a decision about today's stock.

---

## What this looks like in an output

One short block, near the top if it changes how the whole output should be read, otherwise at the
end:

> **Not supplied:** quota target (Coverage Ratio withheld) · COGS for 1 of 4 SKUs (excluded from the
> ranking, not merely percentage-withheld) · suppression list (**this list is not safe to send**).
> **Stale:** inventory export dated 7 days ago, against a signal that moves daily — treat the cover
> figures as historical.

Three lines, and the reader now knows exactly how much weight the output carries.
