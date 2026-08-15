# Run State: Trend, History, and the First Run

Several skills in this pack promise something they cannot deliver from a single run: a trend, a
direction of travel, a "what changed since last time", or a check against what was tried before.
Those all require state that survives between runs, and an agent has none by default.

This file defines where that state lives, what goes in it, and — the part most often missed — how a
skill behaves on the run where no state exists yet.

---

## The state file

One file per concern, in `.agents/`, append-only, human-readable markdown.

| File | Owner | Holds |
|---|---|---|
| `.agents/store-loop-ledger.md` | `the-loop-ledger` | Loop runs, flags, changes, dismissals, verdicts |
| `.agents/gtm-run-state.md` | Whichever skill writes first | Snapshots for trend-bearing skills: pipeline scores, lifecycle stage per account, margin periods, segment memberships |
| `.agents/product-context.md` | `product-context` | Who the business is. Changes rarely. **Not run state.** |

Keep the distinction: `product-context.md` is identity, `gtm-run-state.md` is history. Mixing them
means a positioning change and a weekly score update land in the same file with the same authority.

---

## What a snapshot must contain

A snapshot that cannot be compared is not worth writing. Every entry carries:

- **The date it was taken**, and the period it describes (they are different)
- **The unit of comparison** — account ID, SKU, segment name, deal ID
- **The value**, and the method that produced it
- **The thresholds in force at the time.** This is the one usually omitted and it invalidates
  everything else: if the cut points were recomputed between runs, a stage change may reflect a moved
  threshold rather than a moved customer. Store the thresholds or the comparison is meaningless.
- **What was missing**, so a gap is not mistaken for a change

## Writing the snapshot

Write it **after** delivering the output, and say in the output that it was written. A user who does
not know state is being kept cannot reason about why run 2 differs from run 1.

Append, never rewrite. A snapshot records what was believed on a date. A correction is a new entry
that supersedes, not an edit to the old one.

---

## The first run

**This is the case that must be designed, not discovered.** On the first run there is no prior
snapshot, so every trend-bearing output is empty — and the failure mode is that the skill either
invents a trend or silently omits its headline finding.

The rule: **say plainly that this is a baseline, deliver everything that does not need history, and
name what the next run will add.**

| Wrong | Right |
|---|---|
| Present a first snapshot as a trend | "This is a baseline. Direction of travel is unavailable for every row; the next run will have it." |
| Omit the trend-dependent section | Show the section, marked `baseline — no prior run to compare` |
| Reject or block because history is missing | Deliver, with the standard explicitly capped |
| Emit the entire existing backlog as "new" | Record the backlog as the baseline, and report `n items recorded as pre-existing, not new` |

That last row is specific to delta-reporting loops. A loop whose whole purpose is to show only what
changed will, on run 1, classify everything as changed. It must instead **absorb the current state
as the baseline and say how many items it absorbed**, so the user knows the loop is armed rather than
thinking nothing was wrong.

### First run must never mean automatic rejection

Where a skill's standard requires checking history — a prior revert, a previous override, an earlier
attempt at the same change — the absence of a ledger is **a stated limitation that caps the
standard, not a defect in the proposal.** A checker that rejects everything until a ledger exists can
never approve a first proposal, and the ledger will never be created, so the deadlock is permanent.

Say: *"unverifiable against history — no ledger exists yet"*, apply the remaining checks, and record
the verdict so the second run has something to check against.

---

## State that has gone stale

A snapshot has a useful life too.

- **If the last snapshot is older than the comparison period, say so.** Comparing this week against a
  snapshot from three months ago is not a weekly trend.
- **If the method changed between snapshots, the comparison is invalid.** Say which run changed and
  compare only from there forward.
- **If thresholds were recomputed, movement may be an artefact.** Report threshold changes alongside
  stage changes, or the reader attributes a moved cut point to a moved customer.

---

## Pruning

Append-only files grow, and a state file that exceeds what can be read becomes a state file that is
silently ignored — at which point every skill reading it loses its memory without any error.

- **Roll up entries older than 90 days** into one summary line per unit, keeping the latest value and
  the count of prior observations.
- **Never prune dismissals or reverts.** Those are the entries whose whole value is that they are
  remembered indefinitely; a dismissed seasonal spike re-flagged a year later is the failure the
  ledger exists to prevent.
- **Never prune the current snapshot**, however old, since it is the only comparison point available.
- State the file's size and last prune date when it is read, so growth is visible before it becomes a
  problem.
