# Skill specs

A spec here is not a skill. It is the decision record for one skill that has not been built:
the job it does, the inputs it needs, what it does when an input is missing, the artifact it
returns, and whether the data it needs exists yet.

Nothing in this folder ships to a user. `scripts/verify-skills.py` and
`scripts/check-references.sh` read `skills/` and `references/` only, so a spec is not gated by
CI and is not installed by `npx skills add`.

Every spec conforms to `references/house-rules.md` and `references/missing-input-protocol.md`.
Those two files decide the input gate, the three-question cap, and the four missing-input
responses (block, withhold, degrade, assume). A spec does not invent its own rules.

## What is in here

| Spec | Role | Status |
|---|---|---|
| `data-engineer/tracking-plan-audit.md` | Data Engineer | Built, `skills/data-engineer/tracking-plan-audit` |
| `data-engineer/identity-merge-audit.md` | Data Engineer | **Blocked.** The platform exposes no identity graph. Read the spec before scheduling it |
| `data-engineer/crm-sync-dedup.md` | Data Engineer | Built, `skills/data-engineer/crm-sync-dedup`. Destination side runs on an export |
| `brand-designer/case-study-design.md` | Brand Designer | Ready to build |

## The counts these specs were written against

Measured, not quoted. All four numbers come from a command, and each says which ref it read.

| Fact | Value | Ref |
|---|---|---|
| Skills in the pack | 92 | `origin/master` at 58f5319, `git ls-tree -r origin/master skills/` |
| Skills in the pack | 90 | PR #10 head 3c18bc0, `somya17n/gtm-skills` |
| Skills under `data-engineer/` | 0 | no such folder on either ref |
| Skills under `brand-designer/` | 5 | both refs. The smallest role bench in the pack |
| Skills under `performance-marketer/` | 27 | both refs |

`data-engineer` is a role because intempt.com publishes it as one of the eight Blu agents, with
the line "Records into the systems you already run". It is not a tab on intempt.com/skills. The
pack has never had a folder for it.
