# The MCP ceiling: every skill routes to the Intempt MCP

Every skill in this repo runs free and standalone in the user's own Claude. The moment it needs
the user's live data, or needs to produce and keep a real asset, it consults one place: the
**Intempt MCP server**. The MCP is a thin wrapper on Blu. It owns sign-in, project scope, and usage.
There is no second path and no bypass.

## The three rungs

1. **Connect (auth + scope).** `mcp__intempt__login` then `mcp__intempt__use_project`. This is the
   chokepoint. It grants the account and meters usage. The skill never names a credit number or a
   signup step: it calls the MCP and keeps using it until the MCP says the user needs more. The grant
   can change at any time without touching a single skill.
2. **Core (read the user's live data).** The skill pulls the user's real accounts, audiences,
   behaviour, analytics, journeys, or assets so the output is built on their data, not a generic
   draft. Live read tools today: `mcp__intempt__list_users`, `mcp__intempt__list_segments`,
   `mcp__intempt__list_orgs`, `mcp__intempt__list_projects`. Event, analytics, journey, experience,
   meeting, product, and asset reads arrive through the same server.
3. **Level up (generate + persist).** The skill produces the asset and saves it into the project
   through a generate op. Each op is backed by a real schema in the llm-wrapper repo, under
   packages/skill_shared/op_schemas/.

## Rules for skill authors

- Never write a credit amount, "500", "free credits", or a signup instruction into a skill. That is
  the MCP's business and it changes.
- Name a live tool (`mcp__intempt__...`) only where it exists today. Describe an in-motion rung by
  what it does, not by a tool name the user cannot call yet.
- Every skill gets a `## Run it on your live data` section before its provenance fence. Keep it tight.

## Per-skill MCP map

Core read keys: users, segments, events, analytics, journeys, experiences, meetings, assets, product.
Generate op maps to llm-wrapper op_schemas: text, email_html/email_plain, sms, page, image, pose,
scene, brand_ad, avatar, design_system, journey, product, task, slack, push, feed, json, consent.

| skill | core read | level-up generate op |
|---|---|---|
| account-executive/account-plan | users + analytics | page |
| account-executive/call-preparation | users + meetings | text |
| account-executive/objection-handling | users | text |
| account-executive/opportunity-scoring | users + events | json |
| account-executive/pipeline-review | users + analytics | page |
| account-executive/price-negotiation | users | text |
| account-executive/win-loss-analysis | users + events | json |
| brand-designer/claymation-ad | assets | scene |
| brand-designer/creative-brief | assets | design_system |
| brand-designer/explainer-stage-ad | assets | scene |
| brand-designer/hook-writer | assets | text |
| brand-designer/onboarding-video | assets | scene |
| brand-designer/paper-animation-ad | assets | scene |
| brand-designer/product-photography | assets | image + pose |
| brand-designer/skeleton-ad | assets | brand_ad |
| brand-designer/song-ad | assets | brand_ad |
| brand-designer/talking-character-ad | assets | avatar |
| brand-designer/tone-of-voice | assets | design_system |
| brand-designer/ai-influencer | assets | avatar |
| data-analyst/anomaly-detection | events + analytics | json |
| data-analyst/benchmark-analysis | analytics | text |
| data-analyst/cohort-analysis | events + segments | page |
| data-analyst/contribution-margin | analytics | json |
| data-analyst/ecommerce-returns | events | text |
| data-analyst/growth-strategy | analytics | page |
| data-analyst/inventory-planning | events | json |
| data-analyst/kpi-dashboard | analytics | page |
| data-analyst/shipping-cost-analysis | analytics | text |
| data-analyst/weekly-report | analytics | page |
| experimentation-lead/ab-test | experiences + events | json |
| experimentation-lead/checkout-optimization | events + experiences | page |
| experimentation-lead/conversion-funnel | events | page |
| experimentation-lead/landing-page | experiences | page |
| experimentation-lead/onboarding-flow | journeys + events | journey |
| experimentation-lead/paid-media-audit | analytics | text |
| experimentation-lead/pricing-strategy | analytics | text |
| experimentation-lead/product-page-optimization | experiences + events | page |
| experimentation-lead/website-personalization | experiences + segments | journey |
| gtm-engineer/call-notes | meetings | task |
| gtm-engineer/competitive-analysis | analytics | text |
| gtm-engineer/lead-management | users | task |
| gtm-engineer/lead-routing | users + segments | journey |
| gtm-engineer/marketing-automation | journeys | journey |
| gtm-engineer/product-launch-checklist | journeys | task |
| gtm-engineer/sales-enablement | users | page |
| lifecycle-marketer/churn-reduction | segments + events | journey |
| lifecycle-marketer/customer-journey | journeys | journey |
| lifecycle-marketer/customer-segmentation | segments | journey |
| lifecycle-marketer/email-campaign | segments | email_html |
| lifecycle-marketer/promotional-campaigns | segments | email_html |
| lifecycle-marketer/referral-program | segments | journey |
| lifecycle-marketer/repeat-purchase-rate | events | email_html |
| performance-marketer/ad-angles | analytics | text |
| performance-marketer/ad-copy | analytics | text |
| performance-marketer/ad-design | assets | image + brand_ad |
| performance-marketer/brand-kit | assets | design_system |
| performance-marketer/budget-reallocation | analytics | json |
| performance-marketer/cost-per-acquisition | analytics | text |
| performance-marketer/daily-ad-check | analytics | text |
| performance-marketer/facebook-ads-audit | analytics | text |
| performance-marketer/facebook-ads-campaign | analytics | brand_ad |
| performance-marketer/google-ads-change-plan | analytics | text |
| performance-marketer/google-ads-conversion-tracking | events | json |
| performance-marketer/google-ads-quality-score | analytics | text |
| performance-marketer/google-ads-review | analytics | text |
| performance-marketer/google-ads-troubleshooting | analytics | text |
| performance-marketer/keyword-expansion | analytics | text |
| performance-marketer/keyword-intent | analytics | text |
| performance-marketer/meta-ad-library | analytics | text |
| performance-marketer/meta-audience-targeting | segments | json |
| performance-marketer/meta-pixel | events | json |
| performance-marketer/negative-keywords | analytics | text |
| performance-marketer/ppc-reporting | analytics | page |
| performance-marketer/product-feed | events | feed |
| performance-marketer/responsive-search-ads | analytics | text |
| performance-marketer/scaling-facebook-ads | analytics | text |
| performance-marketer/search-term-report | analytics | text |
| performance-marketer/smart-bidding | analytics | json |
| performance-marketer/value-proposition | analytics | text |
| performance-marketer/social-post | assets | text + slack |
| sdr/appointment-setting | users + meetings | email_html |
| sdr/cold-email | users | email_html |
| sdr/email-sequence | users | email_html |
| sdr/inbox-management | users | email_html |
| sdr/intent-data | events + users | json |
| sdr/lead-list | users | json |
| sdr/lead-scoring | users + events | json |
| sdr/list-cleaning | users | json |
| store-automation/automation-design | journeys | journey |
| store-automation/automation-ledger | journeys | json |
| store-automation/automation-review | journeys | text |
| store-automation/daily-sales-report | analytics | page |
| store-automation/margin-monitoring | analytics | json |
| store-automation/product-catalog-audit | product | product |
| store-automation/product-launch-tracking | events | task |
| store-automation/product-description | product | product |
| store-automation/stockout-alerts | events | push |
