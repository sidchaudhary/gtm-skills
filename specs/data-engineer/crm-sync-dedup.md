# Spec: crm-sync-dedup

**Role:** GTM Engineer (`skills/gtm-engineer/crm-sync-dedup`), moved from Data Engineer 2026-09-28
**Status:** ready to build. The destination side runs on an export today.
**Build order:** proposed third. Recommend moving it to second, ahead of `identity-merge-audit`,
because it needs nothing the platform does not already give and it catches the same damage one
step later, where it costs money.

## The job the user actually has

"A segment is about to push into HubSpot and I know the list is dirty, but not how dirty."

The push happens through reverse ETL or a native destination, and it is one-way and hard to undo.
What goes wrong is predictable:

- Rows that already exist in the destination arrive as creates, so the destination gains
  duplicates and the rep sees two records for one buyer.
- A field the sales team edited by hand gets overwritten by a staler value from the source, and
  nobody can tell afterwards which side was right.
- Rows fail the destination's own validation (a required field empty, a picklist value that does
  not exist, a string over the field length) and the sync reports a partial success that nobody
  reads.
- Someone who unsubscribed is in the list, because suppression lives in a different system from
  the segment.

The user wants the list checked before it leaves, with a count per problem and a go or fix-first
verdict. Not a data quality essay.

This is not a destination-configuration skill. Field mapping and connector setup are a different
job. This reads one specific outbound list against one specific destination object.

## Inputs, and what happens when they are missing

House rule 7 binds on the two big ones: take the file or the URL and read it. Nobody is pasting
4,000 rows into a chat window.

| Input | Required | Missing response |
|---|---|---|
| The outbound list, as a path or URL | Yes | **Block.** There is nothing to audit |
| The destination object and its match key (contact on email, account on domain, lead on external id) | No | **Assume** email for contacts and domain for accounts, stated inline at the point of use, and report how many rows lack the assumed key |
| A recent export of the destination's existing records | No | **Degrade.** Dedupe within the outbound list only. Say in the first two lines that the create-against-update split did not run, because for most users that split is the whole reason they asked |
| Suppression and consent state for the rows | Yes | **Block.** This is a push that leads to a send. `references/missing-input-protocol.md` names a suppression or consent gate as one of the four cases where blocking is correct, and this is that case |
| The date of each export | No | **Withhold** the staleness section rather than guessing an age. A field conflict cannot be resolved without knowing which side is newer |
| Field-level freshness expectations (which fields the destination owns and the source must not overwrite) | No | **Degrade.** Report every conflict as a conflict, and say that without an ownership rule the skill cannot say which side should win |

Two protocol rules do real work here:

- **Not applicable is not missing.** A contact-only field on an account row is excluded from the
  denominator with the exclusion count stated. Counted as missing, it turns a clean list into a
  fake completeness problem.
- **Absent is not zero.** A blank numeric field read as zero is the specific failure that makes a
  bad row rank first in any list sorted by value.

## The output artifact

One pre-push report, offered as a file at `.agents/crm-sync-precheck.md`.

1. **The verdict, first two lines.** Go, or fix these two things first. With the row counts.
2. **Duplicate clusters inside the outbound list**, each with a survivor and the reason it wins.
3. **Create against update**, counted against the destination export, with the rows that would
   create a second record for an existing person listed separately, because those are the
   expensive ones.
4. **Field conflicts** where both sides changed since the last sync, showing both values, both
   dates, and which side is newer. No recommendation where ownership was not supplied.
5. **Rows that will fail destination validation**, grouped by the rule they break, so one fix
   clears a group.
6. **Rows blocked by consent or suppression**, listed, and stated as removed from the push rather
   than flagged in it.
7. **What was not checked.** Short, near the top if it changes how the whole report should be read.

Nothing is written to the CRM. The skill produces the corrected list and the report, and the push
stays a human action.

## What it would need from the Intempt platform

The outbound side is already reachable: `list_segments` and `list_users` supply the list without an
export, and `list_users` paginates.

The destination side is not reachable from the registry. There is no destinations domain and no CRM
domain among the 13, so an agent cannot read what HubSpot or Salesforce already holds. Note the
wording: `console-v2/packages/api/src/routes/` does contain `destinations` and `hubspot` routes, so
the capability may exist in the product and simply not be exposed to the CLI or MCP. Report it as
not reachable from the registry, not as absent from the platform.

What would make this a one-command skill instead of a two-export skill:

1. A read of the destination's existing records for the match key in the outbound list, so the
   create-against-update split runs without asking the user for a second export.
2. The last successful sync timestamp per destination, which is what turns a field difference into
   a resolvable conflict.

**Next:** run `tracking-plan-audit` if the conflicts trace back to two events writing the same
attribute, which is the usual cause of a field that changes on both sides.
