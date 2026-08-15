# Chart Form and Accessibility

For any skill that specifies how a number gets displayed: dashboards, scorecards, stat tiles,
report visuals, KPI rows.

A dashboard spec that names chart types without form reasoning or accessibility rules produces
dashboards that are read wrong. The failure is quiet: the chart renders, everyone nods, and the
number they took away was not the number in the data.

This is written for **specs**, not for rendering. It says which form to ask for and which
constraints the spec must state, so whoever builds it has no room to guess.

---

## 1. Pick the form from the question, not from a menu

Choose by what the viewer needs to do with the number.

| The question | Form | Notes |
|---|---|---|
| How has this changed over time? | Line | One line per series, four series maximum before it becomes unreadable |
| How does this compare across categories? | Horizontal bar, sorted by value | Sorted beats alphabetical almost always. Horizontal fits long labels. |
| What is the current value against a target? | Scorecard with target delta, or a bullet bar | **Not a gauge.** See section 2. |
| Where do people fall out of a sequence? | Funnel, with step-to-step conversion shown as well as absolute counts | Absolute-only funnels hide the worst step |
| How does behaviour differ by join date? | Cohort heatmap | Needs a stated colour scale and a legend with real values |
| What is the composition of a whole? | Stacked bar, or a single bar with labels | Only if the parts genuinely sum to a meaningful whole |
| Is there a relationship between two measures? | Scatter | Say what a single point represents |
| What are the underlying records? | Table, sorted, with the sort column named | A table is a legitimate answer, not a fallback |
| Direction of travel, in a tile | Sparkline plus the current value and the delta | Sparklines carry shape, never precise values |

Two rules that resolve most disputes:

- **If the viewer's next action is comparison, use position or length.** Human comparison of angle,
  area, and colour intensity is poor. Bars and lines beat pies and bubbles for anything where "is
  this bigger" matters.
- **If the number is a single value that only matters against a threshold, do not draw it.** Write
  it, with the threshold and the gap.

---

## 2. Forms to avoid, and what to specify instead

| Avoid | Why | Specify instead |
|---|---|---|
| **Gauges and speedometers** | Enormous space for one number, hard to read precisely, and the arc implies a range that is usually arbitrary | Scorecard: value, target, delta, and direction |
| **Pie and donut beyond 2-3 slices** | Angle comparison is unreliable, and small slices are unreadable | Sorted horizontal bar |
| **Dual-axis charts** | The crossover point is an artefact of two independently chosen scales, so the chart can be made to show correlation or none at all. The reader cannot tell which. | Two stacked charts sharing an x-axis, or index both series to 100 at a baseline date |
| **3D anything** | Perspective distorts the encoding it is decorating | The 2D form |
| **Radar / spider** | Area depends on the arbitrary order of the axes | A sorted bar per dimension, or a table |
| **Word clouds** | Size encodes frequency, which is the least interesting property of a word | Ranked list with counts |
| **Stacked area for more than 3 series** | Only the bottom series has a flat baseline, so the rest cannot be read | Small multiples, one line each |

If a stakeholder specifically asks for one of these, say what it will cost in readability and offer
the alternative. Do not silently substitute; the spec should record the decision.

---

## 3. Axis and scale integrity

- **Length-encoded forms start at zero.** Bars and areas encode magnitude by length, so a truncated
  baseline exaggerates differences. Non-negotiable for bars.
- **Position-encoded forms may truncate**, and lines usually should, since forcing zero can flatten
  the movement that matters. When a line axis does not start at zero, the spec must say so, so the
  build does not silently pick either.
- **State the aggregation.** Daily, weekly, or monthly changes what the chart appears to say.
  Weekly bucketing removes weekday seasonality; daily reintroduces it as noise.
- **Name the comparison period explicitly.** "vs previous period" is ambiguous when the current
  period is partial. Specify whether the current bucket is included, and if a partial bucket is
  shown, require it to be visually marked.
- **Say which direction is good.** For churn, CAC, and refund rate, down is good. Any conditional
  formatting or delta colour must follow the metric's own polarity, not a global "green is up" rule.
  This is the single most common dashboard defect: a churn tile turning red because churn fell.
- **Percentages need their denominator on the chart.** A conversion rate without the base count
  cannot be sanity-checked, and small denominators produce wild rates.

---

## 4. Accessibility, stated as spec requirements

- **Never encode meaning in colour alone.** Colour is redundant reinforcement. Every series needs a
  second channel: a direct label, a shape, a dash pattern, or a position. Roughly one in twelve men
  has a colour vision deficiency, and a red-versus-green status column is unreadable to them.
- **Status needs a text or icon channel too.** "Red / amber / green" is a label as much as a colour,
  so the spec must include the word or the icon.
- **Require a colourblind-safe categorical set.** Do not put red and green adjacent in the same
  categorical scale. Test the intended set against deuteranopia before it ships.
- **Contrast minimums.** Text and any essential graphic against its background at WCAG AA at
  minimum. Thin light-grey gridlines on white commonly fail, and axis labels are text.
- **Sequential scales run in one direction.** Use a diverging scale only when there is a real,
  meaningful midpoint (zero change, target). A diverging scale with an arbitrary midpoint invents a
  boundary in the data.
- **Label directly, in preference to a legend.** A legend forces the reader to hold a colour-to-name
  mapping in memory while looking somewhere else. Label the line at its end.
- **Never rely on hover for meaning.** Anything essential must survive without a pointer: touch
  devices, keyboard use, screenshots, and printouts all lose the tooltip.
- **Give every chart a text answer.** A one-line takeaway next to the chart is what most viewers
  read, and it is the only version available to a screen reader.

---

## 5. Theme

Specify colours as **semantic tokens**, never as raw hex in a spec: `--series-1`, `--positive`,
`--negative`, `--grid`, `--surface`, `--text`. The brand's actual palette comes from the design
system, and where the product's primary colour is recorded in `.agents/product-context.md`, the
spec references it rather than restating a value that will drift.

State that the chart must be legible in both light and dark. A spec that assumes one and gets
rendered in the other produces unreadable gridlines and invisible axis text, and the pattern that
fails most reliably is a hardcoded near-white surface with light-grey lines.

---

## 6. Stat tiles and KPI rows

The row everyone actually reads, and the one most often underspecified. Each tile states:

1. **Label** — plain language, no internal jargon or system field name.
2. **Value** — with units, and rounded to a precision someone would actually say out loud.
   `$48.2k` beats `$48,231.77` in a tile.
3. **Delta** — the number, the period it compares against, and its polarity per section 3.
4. **Shape** — a sparkline, if trend matters. Optional, and useless if it has no baseline context.
5. **Freshness** — when the data last updated. A stale tile is read as current, which is worse than
   a tile that is visibly missing.
6. **A definition the viewer can reach.** If two people in the company would compute this number
   differently, the tile needs its formula one click away.

Four to six tiles per row. Past that nothing is prominent, which defeats the purpose of a summary
row.

---

## 7. Check before returning a spec

1. Does every metric's form follow from the question the viewer is answering, rather than being
   picked off a list?
2. Is every avoided form from section 2 absent, and where a stakeholder asked for one, is the
   trade-off recorded rather than silently substituted?
3. Do all length-encoded charts start at zero, and does every truncated line axis say so explicitly?
4. Does every metric state its aggregation granularity and its comparison period, with partial
   current buckets marked?
5. Does every metric declare which direction is good, so no delta or conditional format can turn a
   churn improvement red?
6. Does every rate show its denominator?
7. Does every series carry a non-colour channel, and does every status carry text or an icon?
8. Are colours specified as semantic tokens rather than hex, with the brand colour referenced from
   `.agents/product-context.md` rather than restated?
9. Is the spec explicit that charts must be legible in both light and dark?
10. Does every chart have a one-line text takeaway that does not depend on seeing it?
11. Does nothing essential live only in a tooltip?
12. Does every stat tile carry label, value with units, delta with period and polarity, freshness,
    and a reachable definition?
