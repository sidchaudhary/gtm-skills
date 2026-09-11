# GTM Skills

**Your AI go-to-market team.** 90 skills organized around the 8 real jobs on a GTM team, not around tools. Nine of the 90 are store automations that run the others on a schedule, and every skill builds its own product context, so there is nothing to set up first. The old stack was a flat directory. This one is a job description with skills behind it, the same way you'd hand a new hire a role, not a folder of prompts.

Not "write me a cold email." Design the system that decides which message to send, to whom, through which channel, and when.

Built by [Sid Chaudhary](https://linkedin.com/in/sidchaudhary), founder of [Intempt](https://intempt.com).

---

## What Are Skills?

Skills are instructions that make Claude an expert at specific tasks. Instead of starting every conversation from scratch, skills give Claude deep methodology, frameworks, and domain knowledge to work from.

You install them once. Then you just ask for what you need in plain language, the right skill activates automatically.

**You don't need to be technical.** If you can type a sentence, you can use these.

---

## Why the Job Description Is the Right Map

Most AI skill packs are organized around tools. You end up with a folder full of clever prompts and no idea which one to open on a Tuesday morning.

A GTM hire doesn't come with a folder of prompts. They come with a job description. Eight jobs, over and over, every week, forever: Brand Designer, Lifecycle Marketer, Experimentation Lead, Data Analyst, SDR, Account Executive, GTM Engineer, and Performance Marketer.

So that's how this is organized. Eight jobs. Five to thirty skills behind each one, weighted toward wherever the work actually piles up. Every skill maps to something you'd otherwise pay a person to do.

## What's Inside

90 skills across 8 jobs, including 9 store automations that run on a schedule. Every skill researches and builds its own product context, so there is no setup skill to run first. Each skill includes reference materials with real frameworks, benchmarks, and methodology, not generic advice.

### Job 1: Brand Designer (5 skills)

`npx skills add sidchaudhary/gtm-skills/skills/brand-designer`

Builds the on-brand asset and the content around it, so nothing ships off-voice or off-catalog.

| Skill | What You Get |
|-------|-------------|
| **creative-brief** | Creative briefs using 14 proven angles mapped to funnel stages and channels. Includes messaging hierarchy with character limits and exact ad placement specs for every platform. |
| **product-photography** | Photography direction using a composable scene system, 160+ blocks across 10 dimensions (lighting, camera, surface, props, background, color, style, film type, scene, pose). |
| **tone-of-voice** | Analyzes your content samples to extract a reusable voice profile, 6 dimensions rated 1-10, vocabulary rules, sentence patterns, and channel-specific adaptations. |
| **onboarding-video** | Short, conversion-focused onboarding videos built in Remotion for iOS, Android, or web. Maps each beat to a conversion milestone on the path to activation. |
| **hook-writer** | Four scored hook variants for any post draft, each using a distinct psychological framework, with a recommendation and rug-pull check. |

### Job 2: Lifecycle Marketer (7 skills)

`npx skills add sidchaudhary/gtm-skills/skills/lifecycle-marketer`

Runs the flows that fire on their own, welcome, recovery, win-back, so retention isn't a once-a-quarter campaign.

| Skill | What You Get |
|-------|-------------|
| **customer-journey** | Multi-channel automation flows with conditional branching, holdout groups, and channel guardrails. Outputs a complete journey blueprint with node-by-node detail. |
| **customer-segmentation** | Lifecycle segmentation using a 6-stage model (At Risk to Champions) with RFM scoring and behavioral signals. Tells you who to target and why. |
| **email-campaign** | Designs a lifecycle campaign end to end, email, SMS or push, and decides whether it runs once or on a cadence, with deliverability and consent gates. |
| **referral-program** | Designs a customer referral program, trigger moment, two-sided incentive sized against real customer value, tiers, and anti-abuse rules. |
| **churn-reduction** | Cancel flows, dynamic save offers, churn risk scoring, and dunning sequences, the systemic retention layer, not a one-off email. Now also covers delivery-cycle products: pause/skip vs. cancellation, and frequency mismatch as a churn cause. |
| **repeat-purchase-rate** *(new)* | Reviews the post-first-purchase repeat-buy flow, reorder prompts, replenishment timing, second-purchase incentives, and names what's blocking a second order. |
| **promotional-campaigns** *(new)* | Measures the after-the-fact impact of a promotion or discount already run: lift, margin cost, and the post-promo dip, over a stated recovery period. |

### Job 3: Experimentation Lead (9 skills)

`npx skills add sidchaudhary/gtm-skills/skills/experimentation-lead`

Decides what ships and what dies, with a number attached instead of a gut feeling.

| Skill | What You Get |
|-------|-------------|
| **ab-test** | Bayesian A/B test design with Thompson sampling, sample size calculations, guardrails, and exit criteria. Not just "test this," a full statistical brief. |
| **landing-page** | Conversion-optimized landing pages. Outputs deployable HTML + Tailwind CSS, not a wireframe, a working page. |
| **website-personalization** | Rules that map audience segments to content variants. Condition, experience, measurement plan. Priority-ordered with a default fallback. |
| **pricing-strategy** | Value metric selection, tier structure, price points, and price-increase timing, refuses to guess at your churn or conversion numbers. |
| **conversion-funnel** | Diagnoses funnel drop-offs against industry benchmarks, identifies root causes, calculates the math to hit your targets, and prioritizes fixes. |
| **onboarding-flow** | Designs the post-signup activation flow, what happens before the "aha moment," in what order, and how drop-off gets diagnosed. |
| **paid-media-audit** *(new)* | Triages which ad channels, campaigns, or audiences are wasting spend using ROAS, CAC, and spend concentration. |
| **checkout-optimization** *(new)* | A direct UX audit of a checkout flow, form fields, payment coverage, trust signals, step count, from a walkthrough or screenshots. |
| **product-page-optimization** *(new)* | Reviews an existing product detail page and returns a prioritized edit brief, not a new page build. |

### Job 4: Data Analyst (10 skills)

`npx skills add sidchaudhary/gtm-skills/skills/data-analyst`

Explains what moved and why, before anyone has to ask.

| Skill | What You Get |
|-------|-------------|
| **kpi-dashboard** | KPI dashboard specs with metric formulas, visualization types, alert thresholds, and section-by-section layout. Includes 8 templates. |
| **growth-strategy** | Growth strategy recommendations based on your business maturity. Identifies your top 3 growth levers and builds a quarterly plan. |
| **cohort-analysis** | Groups customers by acquisition period and tracks retention or revenue across the periods that follow, as a cohort table. Now also computes a CAC payback window per cohort when acquisition spend is supplied. |
| **benchmark-analysis** | Checks one of your metrics against a stated benchmark source, with an honest confidence read on how solid that comparison actually is. |
| **anomaly-detection** | Flags which points in a metric's recent history are genuinely outside its normal range, using a stated trailing-average method. |
| **contribution-margin** *(new)* | Computes CM1/CM2/CM3 contribution margin for a product, order, or SKU set from the cost and revenue inputs you provide right now. |
| **shipping-cost-analysis** *(new)* | Isolates shipping cost recovery: real carrier cost vs. what's charged, and where a free-shipping threshold sits against median order value. |
| **inventory-planning** *(new)* | SKU-level stockout and overstock risk from sales velocity, on-hand units, and lead time, with stated days-of-cover thresholds. |
| **ecommerce-returns** *(new)* | Groups structured return and RMA reason codes to specific SKUs and surfaces the highest-volume root causes. |
| **weekly-report** *(new)* | One weekly operating readout pulled from performance, traffic, lifecycle, inventory, and support exports, what changed, what didn't, and the 3 next actions. |

### Job 5: SDR (9 skills)

`npx skills add sidchaudhary/gtm-skills/skills/sdr`

Builds and works the list, so outbound isn't a stale spreadsheet from last quarter.

| Skill | What You Get |
|-------|-------------|
| **lead-list** | Builds and qualifies a prospect list from your ICP, every lead scored Hot/Warm/Cold/Skip with cited evidence. |
| **lead-scoring** | Scores an account list against your ICP criteria and returns priority tiers with a one-sentence rationale per account. |
| **intent-data** | Ranks a batch of intent signals into an ordered outreach list, with the signal, the rationale, and a channel per account. |
| **cold-email** | Turns prospect research, a trigger signal, and a value prop into a complete cold email body under 120 words. |
| **cold-email** | Scores five subject line variants against a cold email body and target persona, with a send recommendation. |
| **email-sequence** | Audits a full cold email sequence, diagnoses each email's specific weakness, and rewrites the three worst-performing ones. |
| **inbox-management** | Sorts a batch of replies into Interested/Later/Referred/Objection/Dead/Angry with evidence and the next action for each. |
| **inbox-management** | Processes a full unhandled inbox into Drafted/Escalated/Scheduled/Closed so nothing sits unworked. |
| **list-cleaning** | Dedupes and flags a raw list, wrong titles, stale roles, wrong companies, broken data, before it hits a sequence. |
| **appointment-setting** | Writes the booking message, reschedule, confirmation, and day-before reminder that gets a warm lead onto a calendar. |

### Job 6: Account Executive (7 skills)

`npx skills add sidchaudhary/gtm-skills/skills/account-executive`

Runs the deal from first call to signature, and tells you honestly when it's stalling.

| Skill | What You Get |
|-------|-------------|
| **call-preparation** | Pre-meeting prep and post-meeting coaching, talk ratio analysis, BANT/MEDDIC scoring, specific rewrites. |
| **pipeline-review** | Full pipeline health analysis, stuck deals, risk signals, forecast by category, coverage ratio. |
| **account-plan** | Account engagement plans with buying committee mapping and a 90-day week-by-week action plan per stakeholder. |
| **opportunity-scoring** | Dual-axis scoring (health + intent) with independent trend tracking and full MEDDIC/BANT completeness checks. |
| **win-loss-analysis** | Ranks the real, evidence-backed reasons deals close or die across a batch of closed-won and closed-lost deals. |
| **opportunity-scoring** | Scores an existing account's renewal risk from usage and relationship signals, with the one highest-leverage action. |
| **price-negotiation** | Preps anchor, concession ladder, walk-away point, and calibrated questions for one specific deal negotiation. |
| **objection-handling** | Outputs the five most likely objections for a persona, each with an acknowledgment, response, and follow-up question. |

### Job 7: GTM Engineer (7 skills)

`npx skills add sidchaudhary/gtm-skills/skills/gtm-engineer`

Builds the systems everyone else's work runs on top of.

| Skill | What You Get |
|-------|-------------|
| **lead-management** | Designs the lead-to-opportunity layer, MQL scoring model, routing rules, and speed-to-lead SLAs. |
| **sales-enablement** | One-pagers, ROI calculators, proposal templates, and playbooks mapped to persona and deal stage. |
| **marketing-automation** | Marketing and sales automation workflows, trigger, condition, action, with error handling and retries. |
| **call-notes** | Extracts deal signals, objections, confirmed pain points, and a stakeholder map from a raw sales call transcript. |
| **competitive-analysis** | Deep-dives one competitor's public site into a structured profile, positioning, pricing, weaknesses. |
| **lead-routing** | Designs the actual assignment logic for a qualified lead, round-robin, territory, or score-threshold, with tie-break and fallback rules. |
| **product-launch-checklist** *(new)* | A pre-launch go/no-go checklist for a specific product or campaign launch. |

### Job 8: Performance Marketer (27 skills)

`npx skills add sidchaudhary/gtm-skills/skills/performance-marketer`

Spends money to buy demand, and knows whether it paid back. 16 skills for paid social, 12 for paid
search. Adapted from Kelpi's MIT-licensed [meta-ads-skills](https://github.com/kelpi-ai/meta-ads-skills)
and [google-ads-skills](https://github.com/kelpi-ai/google-ads-skills); see `NOTICE`.

**Read the gate before the tactics.** Paid ads is a loop: a campaign has to earn enough to pay for
the next one. Three questions decide whether to run ads at all. What is a new customer worth in the
first month, cash in hand? What can you afford to pay for one? Can you spend two to three times that
per angle without flinching? If the answers do not work, fix the offer, the price, or the follow-up
first. Ads amplify a working machine; they do not build one, and running them early produces a false
conclusion ("ads don't work for us") that costs you the channel later.

Five rules the skills enforce: the offer is fixed and the angle is the experiment; your ad is the
targeting now, so specificity is the lever; spend enough to see signal before judging; read daily and
act rarely; keep the structure simple. Every skill that touches an account is read-only or drafts a
paused change, and no skill invents a number.

**Paid social (16)**

| Skill | What You Get |
|-------|-------------|
| **brand-kit** | Reads a live site into a working brand kit, offer, proof, voice, colour and type, plus an honest list of what the site never says. |
| **value-proposition** | Mines reviews, threads and tickets for the exact words buyers use, sorted into triggers, pains, outcomes, objections and alternatives, with a source count per theme. |
| **meta-ad-library** | Reads competitors' live ads for the two honest signals the Ad Library gives, variation count and longevity, then maps the white space nobody is running. |
| **value-proposition** | Turns a mined pain into one promise line under 12 words, tested against the one-second rule, the anyone-test, and whether the offer actually keeps it. |
| **ad-angles** | Five or six genuinely different angles for one offer, each a different WHO, PAIN and PROMISE, with what the algorithm learns from each. |
| **ad-copy** | Picks the two best-fit copywriting formulas for the placement and writes both with the structural beats labelled inline. |
| **ad-design** | Turns approved angles into finished on-brand ad images and stages only the human-picked keepers in the account library, with hashes. |
| **meta-audience-targeting** | Sizes what targeting actually remains and returns one verdict, frequently "go broad and fix the message instead". |
| **facebook-ads-campaign** | The whole campaign as a paused draft, one objective, one broad ad set, one ad per angle, blocked if the conversion event is unverified. |
| **product-feed** | Catalog and product sets for dynamic ads, treating each set as a promise, gated on the pixel-to-catalog identifier match. |
| **daily-ad-check** | The read-only daily pass over one ad account, at most five findings ranked by dollars at stake, ending in "No changes were made." |
| **daily-ad-check** | The two-condition fatigue rule, plus a "looks tired, is not" section naming the auction shift or tracking break that is the likelier cause. |
| **scaling-facebook-ads** | Budget rules that scale a winner without resetting learning, ~20% steps, pause rules, spend caps, all drafted for approval. |
| **facebook-ads-audit** | Reads the account by angle, separates platform-attributed numbers from your own, and ends with at most three supported decisions. |
| **meta-pixel** | Audits whether the pixel and server-side events tell the truth, deduplication keys first, since a doubled count is a tracking break until proven otherwise. |

**Paid search (12)**

| Skill | What You Get |
|-------|-------------|
| **search-term-report** | Sorts the queries Google actually bought into keep, review and exclude, business fit first, and states that the report covers reported terms only. |
| **negative-keywords** | Approval-ready negatives at the narrowest useful scope, every row collision-checked against protected searches, because a bad negative leaves no evidence. |
| **keyword-expansion** | Gives a proven query a deliberate keyword, ad group and page, or holds it rather than routing to the homepage by default. |
| **keyword-intent** | Clusters queries by the answer each searcher needs, one promise per cluster, and reports unanswerable intent as a gap. |
| **responsive-search-ads** | A complete responsive search ad validated against every character limit, with a claim ledger tying each line to what the page supports. |
| **google-ads-quality-score** | Names which of the three components is the weak link behind a keyword worth keeping, with no fake cost-saving forecast. |
| **google-ads-conversion-tracking** | Decides whether conversion data can be trusted to bid on, marking every conclusion observed or suspected. |
| **smart-bidding** | Matches bidding to a trusted goal and mature data, asserting no universal conversion minimum, with a rollback and a fair read date. |
| **ppc-reporting** | Five to seven business-led numbers, each with its formula, source, target and caveat. |
| **google-ads-review** | Two complete equal periods compared, movement attributed to real entities, verdict held until conversion delay has elapsed. |
| **google-ads-troubleshooting** | Works the delivery blockers in dependency order and keeps observed blockers separate from suspected causes. |
| **google-ads-change-plan** | Findings turned into an ordered plan where every item has an exact current state, a rollback, and a measurement window. |

**Cross-platform (2)**

| Skill | What You Get |
|-------|-------------|
| **cost-per-acquisition** | One ranked list of why acquisition cost moved across both platforms, each cause marked observed or suspected, including the read neither account gives alone: whether the two are bidding into the same people. |
| **budget-reallocation** | Donors, recipients and three transfer scenarios across both platforms, ranked on marginal rather than average cost, every projected figure labelled as a projection. |

*Not built on purpose: a ROAS forecaster.* Every skill here refuses to invent a number, and
`google-ads-quality-score` explicitly forecasts no cost saving because no reliable conversion from
score to click cost exists. A forecasting skill would contradict the rule that makes the other 29
worth trusting.

### Store Automation (9 skills)

`npx skills add sidchaudhary/gtm-skills/skills/store-automation`

Not a job - a mechanism. The 8 jobs above answer a question once. These run that answer on a
schedule, diff it against the last run, and stop when a gate fails. Built for a Shopify store
where the same margin, stock, feed, and spend checks need doing every morning and get skipped.

Every one of them is read-and-propose by default. None of them will change a price, move a
budget, or edit your catalog without you approving it.

| Skill | What You Get |
|-------|-------------|
| **automation-design** | Turns a recurring store question into a runnable loop: cadence, an objective gate that can fail, a stop condition, and a ceiling. Refuses to emit a loop whose gate can't evaluate false. |
| **automation-ledger** | The state file at `.agents/store-loop-ledger.md` that every loop reads and appends to. What ran, what it flagged, what changed, what to stop flagging. The agent forgets between runs; this doesn't. |
| **daily-sales-report** | The daily exception pass over orders, revenue, and spend. Reports only what moved outside its own trailing band, ranked by dollars at stake, not percentage. |
| **margin-monitoring** | Reruns the contribution-margin stack on a cadence and reports *crossings*: which SKUs went unprofitable since last run, split into losing-before-ads vs losing-only-because-of-ads. |
| **stockout-alerts** | Cross-checks live ad spend against on-hand units and proposes pausing spend on what you can't ship. Matches on the grain the ads target, so a variant ad isn't checked against parent stock. |
| **product-catalog-audit** *(new)* | Audits product catalog completeness (titles, attributes, images, descriptions) at SKU scale, not a sampled spot-check. |
| **product-launch-tracking** | Watches a new product's first weeks against pre-set signal thresholds and a hard test budget, then closes itself. Won't state a verdict on a sample below your minimum. |
| **automation-review** | The checker in a maker-checker pair. Reviews another loop's proposal by trying to refute it, and defaults to reject. Catches gates that could never have failed. |

---

## Quick Start

### Step 1: Install the skills

**Option A, One command** (if you have Claude Code):
```bash
npx skills add sidchaudhary/gtm-skills
```

**Option A2, one job at a time.** Each job section below carries its own install line, so you can
take the pack you actually need and ignore the rest:
```bash
npx skills add sidchaudhary/gtm-skills/skills/performance-marketer
npx skills add sidchaudhary/gtm-skills/skills/sdr
```

**Option B, Git clone:**
```bash
git clone https://github.com/sidchaudhary/gtm-skills.git
cd gtm-skills
```

**Option C, Download ZIP:**
Click the green **Code** button on GitHub, **Download ZIP**, extract to a folder.

---

### Step 2: Pick how you'll use them

<details>
<summary><strong>Claude Code (terminal), recommended</strong></summary>

Claude Code is Anthropic's AI coding assistant that runs in your terminal. Don't let "terminal" scare you, you just type `claude` and start talking.

**What you need:**
- A terminal (Terminal on Mac, PowerShell on Windows)
- A Claude subscription (Pro, Max, or Team) **or** an [Anthropic API key](https://console.anthropic.com/)

**Install Claude Code:** Follow the [getting started guide](https://docs.anthropic.com/en/docs/claude-code/getting-started).

**Then:**
```bash
cd gtm-skills
claude
```

That's it. Start talking. The skills activate automatically.

</details>

<details>
<summary><strong>Claude Cowork (desktop app)</strong></summary>

Claude Cowork is Anthropic's desktop agent. This repo includes a plugin manifest so skills install automatically.

**What you need:**
- Claude Desktop app with Cowork enabled (any paid Claude plan)

**Setup:**
1. Open the Claude Desktop app, switch to the **Cowork** tab
2. Select the downloaded `gtm-skills` folder as your working directory
3. All 78 skills activate automatically

Once set up, just ask for what you need.

</details>

<details>
<summary><strong>Claude.ai (web chat)</strong></summary>

You can use these skills in Claude's web interface using Projects.

**What you need:**
- A Claude account at [claude.ai](https://claude.ai) (Pro, Max, or Team)

**Setup:**
1. Go to [claude.ai](https://claude.ai), **Projects**, **Create a new project**
2. Click **Add content** in the project knowledge section
3. Upload the skill files you want from `skills/<job>/<skill>/`, each folder has a `SKILL.md` file
4. Upload the matching reference files from that same skill folder's `references/` subfolder (each skill ships the references it cites)

> **Tip:** The `.claude-plugin` folder is hidden by default. On Mac, press `Cmd + Shift + .` in Finder to show hidden files.

Start a conversation inside the project and ask for what you need.

**Note:** Unlike Claude Code and Cowork, outputs won't auto-save as files, copy them from the chat.

</details>

---

### Step 3: Your product context (nothing to set up)

There is no setup step. Every skill researches your business itself the first time you run one: it reads your site for positioning, offer, voice and proof, asks at most three things research cannot answer, and saves what it learned to `.agents/product-context.md` so the next skill does not repeat the work.

---

### Step 4: Start working

Tell Claude what you need in plain language:

- *"Design a journey for onboarding new users"* (customer-journey)
- *"Score this deal, here's what I know about it"* (opportunity-scoring)
- *"Build me a landing page for our free trial"* (landing-page)
- *"Prep me for my demo with Acme Corp tomorrow"* (account-plan)
- *"Where's my funnel leaking?"* (conversion-funnel)
- *"What should our growth strategy be this quarter?"* (growth-strategy)
- *"Create a creative brief for LinkedIn ads"* (creative-brief)
- *"Analyze my pipeline, here are my current deals"* (pipeline-review)
- *"Is this quarter's churn rate actually bad?"* (benchmark-analysis)
- *"Who should this inbound lead get routed to?"* (lead-routing)

You don't need to know the skill name. Describe the job and the right one activates.

## The Order to Build Them In

Don't install all 90 on day one. You'll use nine of them and forget the rest.

**Week one:** run `account-plan` and `cold-email` (Account Executive and SDR research plus voice). Those two alone change your reply rate.

**Week two:** add `objection-handling` and `pipeline-review`. Sorting stalled deals and objections is where most pipelines actually leak.

**Week three:** add `lead-list`, `lead-scoring`, and `intent-data`, so you stop working a stale list.

**Week four:** add `customer-journey`, `landing-page`, and `kpi-dashboard`, and let the whole thing run.

## What to Never Hand Over

Three things stay with you, permanently.

**The decision to contact someone.** These skills draft and suggest. You approve. The day that flips is the day you become the thing everyone complains about.

**The price conversation.** Let a skill draft the pricing strategy. Never let it negotiate live with a real customer.

**A bad reply.** When someone is annoyed, a human answers. Every time.

Everything else on this list is fair game, and every hour it takes back is an hour you spend on the calls that close.

---

## How Skills Work Together

Skills are independent, use any one on its own. But they're more powerful together because they share your product context.

```
                    ┌─────────────────────┐
                    │  (your business DNA) │
                    └─────────┬───────────┘
                              │ feeds into everything
     ┌──────────┬─────────────┼─────────────┬──────────┬──────────┐
     ▼          ▼             ▼             ▼          ▼          ▼
 ┌────────┐ ┌────────┐  ┌────────────┐ ┌─────────┐ ┌────────┐ ┌────────┐
 │ Brand  │ │Lifecycle│  │Experiment- │ │  Data   │ │  SDR   │ │Account │
 │Designer│ │Marketer │  │ation Lead  │ │ Analyst │ │        │ │Executive│
 └───┬────┘ └────────┘  └────────────┘ └─────────┘ └────────┘ └────────┘
     │                                                               │
     │  angles, creative                                      ┌──────▼──────┐
     ▼                                                        │ GTM Engineer │
 ┌─────────────┐                                              └─────────────┘
 │ Performance │  buys the demand the other seven convert
 │  Marketer   │
 └─────────────┘
```

**Example flow:** Run `customer-segmentation` to identify at-risk customers, feed that into `customer-journey` to design a retention flow, use `customer-journey` for the email content, set up `ab-test` to test two approaches, track results with `kpi-dashboard`.

**Paid flow:** Run `brand-kit` on your site, mine real language with `value-proposition`, sharpen one line with `value-proposition`, spread it into angles with `ad-angles`, make the images with `ad-design`, and launch a paused draft with `facebook-ads-campaign`. Then read daily with `daily-ad-check` and decide weekly with `facebook-ads-audit`.

---

## What Makes This Different

| | Generic AI prompts | Single-domain skill packs | GTM Skills |
|---|---|---|---|
| **Organized by** | Whatever you ask for | One tool or one domain | The 8 real jobs on a GTM team |
| **Methodology** | None, starts from scratch | Varies | Bayesian testing, lifecycle scoring, composable photography, dual deal scoring, 14 creative angles |
| **Context** | Forgets everything between conversations | Some persistence | Shared product context file, set up once, every skill uses it |
| **Output quality** | Depends on your prompt | Template-driven | Framework-driven with reference data (benchmarks, compliance rules, scoring rubrics) |
| **Cost** | Your Claude subscription | Free or $100+ | Free |

---

## FAQ

**Do I need to be technical?**
No. You need to type sentences. That's it. Claude Code runs in a terminal, but all you do is type `claude` and then talk normally.

**Do I need an API key?**
Not necessarily. Claude Code and Cowork work with a regular Claude subscription (Pro at $20/mo, Max at $100/mo). An API key is only needed if you prefer pay-per-use billing.

**Can I use just one skill?**
Absolutely. Every skill works independently. Use `email-campaign` without ever touching `opportunity-scoring`. The first skill you run builds the shared context file, and every skill after it reads your business out of that file instead of asking again.

**Can my team use this?**
Yes. Share the repo. Each person's context file is local to their machine, so the same skills produce output customized to whoever is using them.

**What if I already use [Klaviyo / HubSpot / Salesforce / etc.]?**
These skills design the *strategy*, what to build, who to target, what to say. You execute in whatever tools you already use. Skills handle the thinking layer; your existing stack handles the doing layer.

**Can I customize the skills?**
Yes. Skills are just Markdown files. Edit any `SKILL.md` or `references/*.md` to match your methodology or add your own frameworks.

**How is this related to Intempt?**
These skills encode methodology developed while building [Intempt](https://intempt.com), a customer engagement platform. The skills are free and work with any stack. If you want to execute the strategies they generate with real customer data, Intempt is the natural next step, but it's not required.

---

## Reference Materials

Each skill is backed by detailed reference documents. These contain the frameworks, benchmarks,
scoring rubrics, and compliance rules that make skill output substantive rather than generic.

**Where they live.** `references/` at the repo root is the canonical, editable copy. Every skill
that cites a reference also ships its own copy at `skills/<job>/<skill>/references/`, because
`npx skills add` installs each skill as a standalone directory: a `Read references/foo.md`
instruction resolves relative to the skill's own folder, so a reference that exists only at the
repo root is unreachable once installed.

Edit the root copy, then run `scripts/sync-references.sh` to push it out to the skills that cite
it. `scripts/check-references.sh` verifies every citation resolves, matches the root copy, and is
actually cited by something, and exits non-zero if not, so it can run in CI.

| Reference | What's Inside |
|-----------|--------------|
| `lifecycle-stages.md` | 6-stage model, RFM scoring tables, behavioral scoring, filter operators |
| `bayesian-testing.md` | Thompson sampling, posteriors, guardrails, sample size formulas |
| `journey-nodes.md` | 12 node types, filter DSL, channel guardrails, holdout methodology |
| `email-templates.md` | HTML constraints, Liquid variables, subject line frameworks, deliverability |
| `sms-push-compliance.md` | Character limits, TCPA/GDPR/CASL, quiet hours, frequency caps |
| `landing-page-patterns.md` | Copy frameworks (PAS/AIDA/BAB), form optimization, Tailwind patterns |
| `personalization-rules.md` | Rule schema, condition types, recommendation algorithms, measurement |
| `outreach-cadences.md` | 4 cadence patterns, personalization layers, compliance, benchmarks |
| `coaching-metrics.md` | Talk ratio, BANT/MEDDIC scoring rubrics, objection categories |
| `deal-scoring.md` | Health + intent scoring, pipeline stages, quadrant analysis |
| `account-lifecycle.md` | Account stages, buying committee roles, multi-threading strategies |
| `creative-angles.md` | 14 angles, funnel mapping, channel performance matrix |
| `scene-composition.md` | 160+ blocks across 10 dimensions, 32 curated presets |
| `ad-placements.md` | Specs for Facebook, Instagram, LinkedIn, TikTok, Pinterest, Google, Email |
| `paid-social-mechanics.md` | Campaign hierarchy, the learning phase, pixel/CAPI deduplication, catalog fields, per-ad fatigue baselines |
| `paid-search-mechanics.md` | RSA asset character limits, negative match-type mechanics, the three Quality Score components, conversion-action settings, bid strategy families, delivery-blocker order |
| `brand-voice-dimensions.md` | 6 voice dimensions, vocabulary profiling, channel adaptations |
| `dashboard-templates.md` | 8 dashboard templates, metric formulas, attribution models |
| `funnel-benchmarks.md` | Conversion benchmarks by industry, drop-off diagnosis framework |
| `workflow-patterns.md` | 7 automation patterns, error handling, integration points |
| `strategy-frameworks.md` | Growth frameworks by maturity, ICE scoring, quarterly planning |
| `prospecting-sources.md` | Data sources by motion, qualification rubric, compliance boundaries |
| `revenue-lifecycle.md` | Lifecycle stage definitions, MQL scoring model, routing logic, speed-to-lead curve |
| `sales-enablement-assets.md` | Sales deck framework, case study brief format, buyer persona card template |
| `competitor-profile-guide.md` | Page-type extraction guide, multi-competitor comparison table format |
| `customer-research-methods.md` | Signal extraction methods, sourcing when no assets exist, evidence-based persona building |
| `pricing-frameworks.md` | Value metric selection, tier structure, pricing research methods, price-increase timing |
| `churn-retention-playbook.md` | Cancel flow design, save-offer strategy, churn health scoring, dunning sequencing |
| `loop-cadence-guide.md` | Signal-speed-to-cadence rule, 9-part loop anatomy, common failure modes |

---

## License

MIT, use freely, modify as needed, no attribution required.

The 28 skills in `skills/performance-marketer/` are adapted from Kelpi's MIT-licensed
[meta-ads-skills](https://github.com/kelpi-ai/meta-ads-skills) and
[google-ads-skills](https://github.com/kelpi-ai/google-ads-skills). Their copyright and permission
notices, and a table mapping every ported skill to its upstream original, are in `NOTICE`.
