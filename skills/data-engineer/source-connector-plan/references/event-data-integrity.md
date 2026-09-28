# Event Data Integrity

For every skill that reads event exports, identifiers, source samples or delivery counts: tracking
plans, source mapping, identity, streams, lake exports and privacy requests.

These checks run **before** any design or count, because each one produces a confident, wrong answer
rather than an obvious error. Report which checks ran and what they found. Where a check cannot run
because the input lacks the field, say so and state what it limits the conclusion to.

Count with a script or a formula, never by reading rows by eye. Show the count and the rule that
produced it.

---

## 1. The open window

A window, day or batch that has not closed reads as missing data. Drop the last period if it is
incomplete, and say you did. Compare only closed windows.

## 2. Test and internal traffic

Staging, QA, developer builds, internal test workspaces and employee accounts inflate volume and add
events nobody planned. Split them out by a source, environment or email-domain column. If there is no
such column, say production and test traffic could not be separated.

## 3. Duplicate rows

A paginated or re-run export repeats rows. Check for the same key (event and day, record id, event
id) appearing twice before counting anything.

## 4. Identifier normalisation

`Ann@Acme.com`, `ann@acme.com ` and `ann@acme.com` are one person and three strings. Lowercase and
trim emails, and strip `www` and paths from domains, before matching or counting. Say what you
normalised and how many values it changed.

## 5. Placeholder and shared values

One value shared by many records is either a placeholder (`anonymous`, `unknown`, `null`, an empty
string, `test@test.com`) or a shared inbox. Both join unrelated people. Count every value that
appears on more than a handful of records and name which kind it is. Generic placeholders may be
shown as they are. Any real address found in the data is masked (`s***@acme.com`).

## 6. Types as sent, not as named

A field called `revenue` can arrive as a number on one platform and a string on another. Read the
type from the data, per source, not from the field name or the plan.

## 7. Time zones

Mixed UTC and local timestamps move events across day boundaries and make a real drop look like a
shift. State which zone the export uses before comparing days.

## 8. Personal data

Never copy an email, phone number, name or credential from the input into the output. Report the
field and the count, with the value masked. Flag any credential for rotation without repeating it.
