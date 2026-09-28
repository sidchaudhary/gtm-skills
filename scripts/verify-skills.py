"""Structural + CTA integrity check for every skill in the pack.
   A. all 96 skills structurally + semantically sound
   B. no skill prints an Intempt block; each ends with a static live-data section
   C. every backticked skill-name reference resolves to a skill directory on disk
Reports per-skill, fails loudly. No sampling."""
import glob, io, os, re, sys, collections

SK = sorted(glob.glob("skills/**/SKILL.md", recursive=True))
ROOT_REFS = {os.path.basename(p) for p in glob.glob("references/*.md")}

# canonical CTA shape
ATTR_RULE = "\u2501" * 10  # heavy horizontal rule used in the attribution block

problems = collections.defaultdict(list)
rows = []

# ---- role -> Blu agent name expected in the CTA ----
ROLE_AGENT = {
    "sdr": "SDR",
    "account-executive": "Account Executive",
    "lifecycle-marketer": "Lifecycle Marketer",
    "brand-designer": "Brand Designer",
    "experimentation-lead": "Experimentation Lead",
    "data-analyst": "Data Analyst",
    "gtm-engineer": "GTM Engineer",
    "store-automation": "GTM Engineer",
    "performance-marketer": "Performance Marketer",
    "data-engineer": "Data Engineer",
    "product-context": None,   # "every agent"
}

for p in SK:
    d = os.path.dirname(p)
    name = os.path.basename(d)
    role = os.path.basename(os.path.dirname(d))
    raw = io.open(p, encoding="utf-8").read()
    P = problems[name]
    rec = {"name": name, "role": role}

    # ================= A. STRUCTURE =================
    # 1. frontmatter
    if not raw.startswith("---\n"):
        P.append("no frontmatter")
        fm, body = "", raw
    else:
        parts = raw.split("---", 2)
        fm, body = parts[1], parts[2]

    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    fmname = m.group(1).strip().strip("\"'") if m else None
    if not fmname:
        P.append("no name:")
    elif fmname != name:
        P.append("name mismatch: fm=%s dir=%s" % (fmname, name))

    m = re.search(r"^description:\s*(.+(?:\n\s{2,}.+)*)$", fm, re.M)
    desc = " ".join(m.group(1).split()) if m else ""
    rec["desc_len"] = len(desc)
    if not desc:
        P.append("no description:")
    elif len(desc) < 60:
        P.append("description too short (%d chars) - weak routing" % len(desc))
    elif "One sentence" in desc or "what this skill does" in desc:
        P.append("PLACEHOLDER description")
    # routing: a description needs an invocation trigger and a disambiguating boundary
    if desc and not re.search(r"\bUse (when|for|to|after|before|if|daily|weekly|as )\b|\bRun this first\b",
                              desc, re.I):
        P.append("no invocation trigger - will not auto-route")
    if desc and not re.search(r"\b(Boundary|Pairs with|differs from|Not for)\b", desc, re.I):
        P.append("no boundary clause - may collide with a neighbouring skill")
    rec["desc_main"] = re.split(r"Boundary:", desc)[0]
    # Any backticked slug counts as a cross-reference. Skill names lost the `the-` prefix in the
    # keyword rename, so this can no longer key off it. Non-skill slugs landing in the set are
    # harmless: it is only ever tested for membership of another skill's name.
    rec["desc_refs"] = set(re.findall(r"`([a-z][a-z0-9-]{2,})`", desc))

    # 2. body sections
    heads = re.findall(r"^##+ (.+)$", body, re.M)
    rec["words"] = len(body.split())
    if rec["words"] < 250:
        P.append("body thin (%dw)" % rec["words"])
    allheads = re.findall(r"^#{2,4} (.+)$", body, re.M)
    has_proc = any(re.match(r"(Process|How to run|How it works|Steps|Workflow|Modes?|Mode [A-Z]|Pick the mode|Classification|What you make)", h) for h in allheads)
    has_numbered = len(re.findall(r"^#{0,4}\s*\d+\. ", body, re.M)) >= 3
    if not (has_proc or has_numbered):
        P.append("no process/steps section")
    if not any("uality check" in h or "erify" in h for h in heads) \
       and "verify:" not in body and "Before returning" not in body:
        P.append("no quality-check / verify gate")

    # 3. numbered steps monotonic *within each section*
    cur, seen, bad = None, [], []
    for line in body.split("\n"):
        if re.match(r"^##+ ", line):
            seen, cur = [], line
            continue
        mm = re.match(r"^(\d+)\. ", line)
        if mm:
            n = int(mm.group(1))
            if n in seen:
                bad.append("%s: step %d twice" % ((cur or "top")[:40], n))
            seen.append(n)
    if bad:
        P.append("duplicate steps -> " + "; ".join(bad[:3]))

    # 4. references resolve, on disk, and match root byte-for-byte
    cited = sorted(set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", raw)))
    rec["refs"] = len(cited)
    for c in cited:
        local = os.path.join(d, "references", c)
        if not os.path.exists(local):
            P.append("cites missing ref: %s" % c)
        elif c not in ROOT_REFS:
            P.append("ref not in root: %s" % c)
        else:
            a = io.open(local, "rb").read()
            b = io.open(os.path.join("references", c), "rb").read()
            if a != b:
                P.append("ref DRIFT vs root: %s" % c)

    # 5. no leaked personal names / local paths / TODOs
    for pat, label in [
        (r"\bSomya\b", "leaks name Somya"),
        (r"\bSid(dharth|chaudhary)?\b", "leaks name Sid"),
        (r"C:\\\\|/Users/|Desktop[/\\\\]Work|AppData|/home/\w+/", "leaks local path"),
        (r"\bTODO\b|\bFIXME\b|\bXXX\b", "TODO/FIXME left in"),
    ] + ([] if name == "product-context" else [(r"\[NEEDS INPUT\]", "unfilled [NEEDS INPUT]")]):
        if re.search(pat, raw):
            P.append(label)

    # ================= B. LIVE-DATA SECTION, NOT PROMOTION =================
    # The skill must never print an Intempt block into its output. The only product
    # mention allowed at file level is a static section for the installer, last in the file.
    printed = ATTR_RULE in raw or "Generated with Intempt gtm-skills" in raw
    live = re.search(r"^## Running it on live data\n(.*)\Z", raw, re.M | re.S)
    tracked = ("https://www.intempt.com/signup?utm_source=gtm-skills&utm_medium=agent-skill"
               "&utm_campaign=gtm-skills&utm_content=%s&utm_term=blu" % name)
    body = live.group(1) if live else ""
    has_link = ("- Free account: " + tracked) in body
    has_mcp = "claude mcp add intempt -- npx -y @intempt-technologies/mcp" in body
    has_gov = "Blu proposes, you approve." in body
    has_guard = "Do not add it to your output" in body
    rec["cta"] = bool(live) and has_link and has_mcp and has_gov and has_guard and not printed
    if printed:      P.append("CTA: prints an Intempt block into the output")
    if not live:     P.append("CTA: no final '## Running it on live data' section")
    if not has_link: P.append("CTA: live-data section lacks the tracked link for utm_content=%s" % name)
    if not has_mcp:  P.append("CTA: live-data section lacks the MCP install command")
    if not has_gov:  P.append("CTA: live-data section lacks 'Blu proposes, you approve.'")
    if not has_guard: P.append("CTA: live-data section lacks the do-not-output guard")
    if re.search(r"^## ", body, re.M):
        P.append("CTA: live-data section is not the last section")

    sig_line = ("⚡ Made with gtm-skills · run it on live data free: "
                "https://www.intempt.com/skills?s=%s" % name)
    sig = re.search(r"^## Signature\n(.*?)(?=^## )", raw, re.M | re.S)
    sig_body = sig.group(1) if sig else ""
    if not sig:
        P.append("SIG: no '## Signature' section")
    else:
        if sig.end() != (live.start() if live else -1):
            P.append("SIG: signature section is not directly before the live-data section")
        if ("```\n" + sig_line + "\n```") not in sig_body:
            P.append("SIG: signature line is missing or not for s=%s" % name)
        if "finished deliverable" not in sig_body or "Never add a second" not in sig_body:
            P.append("SIG: signature section lacks the deliverable-only and one-line rules")
    if raw.count("Made with gtm-skills") != 1 or raw.count("⚡") != 1:
        P.append("SIG: signature appears more than once, or a stray one exists")
    rec["cta"] = rec["cta"] and bool(sig)

    expected = ROLE_AGENT.get(role, "?")
    agent_line = re.search(r"^- Blu, the ([A-Za-z ]+), can run it for you\.", body, re.M)
    if agent_line:
        rec["agent"] = agent_line.group(0)
        if expected and expected != agent_line.group(1) and "every agent" not in agent_line.group(0):
            P.append("CTA: names wrong agent for role %s -> %s" % (role, agent_line.group(1)))
    elif expected:
        P.append("CTA: live-data section does not name the Blu agent")

    rows.append(rec)

# ---- routing collisions: high-overlap description pairs need a mutual boundary ----
import itertools
STOP = set(("the a an and or for to of in on with when use this that it its from than rather not is are "
            "be as by at into out only per each every uses using boundary skill skills user users what "
            "which who how does do").split())
TOK = {r["name"]: {w for w in re.findall(r"[a-z]{4,}", r.get("desc_main", "").lower()) if w not in STOP}
       for r in rows}
REFS = {r["name"]: r.get("desc_refs", set()) for r in rows}
collisions = []
for a, b in itertools.combinations(sorted(TOK), 2):
    u = TOK[a] | TOK[b]
    j = len(TOK[a] & TOK[b]) / len(u) if u else 0
    if j >= 0.22 and b not in REFS[a] and a not in REFS[b]:
        collisions.append((j, a, b))
        problems[a].append("routing collision with %s (%.0f%% overlap, no mutual boundary)" % (b, j * 100))

# ---- C. every backticked skill-name reference must resolve to a skill on disk ----
# REFS above is built from the backticked slugs in a description and was used for one thing only:
# suppressing a routing-collision warning when two skills name each other. Nothing checked that
# the slug named a skill that exists. So a reference to a deleted skill did not merely go
# unnoticed, it actively satisfied that guard. This resolves every backticked skill-name
# reference, in every SKILL.md and every root reference file, against the directories on disk.
SKILL_NAMES = {os.path.basename(os.path.dirname(p)) for p in SK}

# Backticked lowercase hyphenated slugs that are code identifiers rather than skill references.
# Closed list, so a newly dangling skill name cannot hide in it. Every entry is asserted to still
# occur below: an entry that stops matching is a stale exemption and fails the check, so this
# cannot quietly grow into a hole.
NON_SKILL_SLUGS = {"v-html"}

# Matches `some-skill` and the slash-command form `/gtm:some-skill`. Requires at least one hyphen,
# which is what every skill directory in this pack has, and keeps single-word code tokens out.
SLUG_RE = re.compile(r"`(?:/gtm:)?([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`")

xref_scanned = sorted(SK) + sorted(glob.glob("references/*.md"))
xref_seen = collections.Counter()
dangling = []
for xp in xref_scanned:
    for ln, line in enumerate(io.open(xp, encoding="utf-8").read().split("\n"), 1):
        for slug in SLUG_RE.findall(line):
            xref_seen[slug] += 1
            if slug not in SKILL_NAMES and slug not in NON_SKILL_SLUGS:
                dangling.append((xp, ln, slug))
stale_exemptions = sorted(s for s in NON_SKILL_SLUGS if not xref_seen[s])

# ================= REPORT =================
bad = {k: v for k, v in problems.items() if v}
print("=" * 74)
print("A. STRUCTURAL / SEMANTIC INTEGRITY")
print("=" * 74)
print("skills audited      : %d" % len(rows))
print("clean               : %d" % (len(rows) - len(bad)))
print("with problems       : %d" % len(bad))
w = sorted(r["words"] for r in rows)
dl = sorted(r["desc_len"] for r in rows)
print("body words          : min %d / median %d / max %d" % (w[0], w[len(w) // 2], w[-1]))
print("description chars   : min %d / median %d / max %d" % (dl[0], dl[len(dl) // 2], dl[-1]))
print("skills citing refs  : %d of %d" % (sum(1 for r in rows if r["refs"]), len(rows)))
print("routing: with trigger + boundary, and 0 unguarded collisions")
print("  naming a neighbour : %d of %d" % (sum(1 for n in REFS if REFS[n]), len(rows)))
print("  unguarded pairs    : %d" % len(collisions))

print()
print("=" * 74)
print("B. INTEMPT CTA COVERAGE")
print("=" * 74)
ok = [r for r in rows if r["cta"]]
print("full CTA (rule + pack line + intempt.com + Blu + governance + run-line): %d of %d"
      % (len(ok), len(rows)))
byrole = collections.Counter()
for r in rows:
    if r["cta"]:
        byrole[r["role"]] += 1
tot = collections.Counter(r["role"] for r in rows)
for role in sorted(tot):
    print("  %-22s %d/%d" % (role, byrole[role], tot[role]))

print()
agents = collections.Counter()
for r in rows:
    if "agent" in r:
        mm = re.search(r"the ([A-Z][A-Za-z ]+?) does", r["agent"])
        agents[mm.group(1) if mm else "other"] += 1
print("Blu agent named in CTA:")
for a, c in agents.most_common():
    print("  %-22s %d" % (a, c))

print()
print("=" * 74)
print("C. CROSS-REFERENCE RESOLUTION")
print("=" * 74)
# A check that scanned nothing is a failure, not a pass.
if not xref_scanned:
    print("files scanned       : 0")
    print("FAIL: scanned no files. The glob is wrong or the tree is empty.")
    sys.exit(1)
print("files scanned       : %d (%d SKILL.md + %d root references)"
      % (len(xref_scanned), len(SK), len(xref_scanned) - len(SK)))
print("skill names on disk  : %d" % len(SKILL_NAMES))
print("backticked refs seen : %d in %d distinct slugs"
      % (sum(xref_seen.values()), len(xref_seen)))
print("dangling references  : %d in %d files"
      % (len(dangling), len({f for f, _, _ in dangling})))

if stale_exemptions:
    print()
    print("STALE EXEMPTIONS in NON_SKILL_SLUGS (no longer occur anywhere, delete them):")
    for s in stale_exemptions:
        print("  - %s" % s)

if dangling:
    print()
    print("DANGLING: a backticked name that matches no skill directory.")
    print("Every one of these reads to the user as a skill they can run, and none of them exist.")
    byslug = collections.defaultdict(list)
    for f, ln, s in dangling:
        byslug[s].append("%s:%d" % (f, ln))
    for s in sorted(byslug, key=lambda k: -len(byslug[k])):
        print("  `%s` -> %d reference(s) in %d file(s)"
              % (s, len(byslug[s]), len({x.rsplit(":", 1)[0] for x in byslug[s]})))
        for loc in byslug[s]:
            print("        %s" % loc)

if dangling or stale_exemptions:
    print()
    print("C FAILED: %d dangling reference(s), %d stale exemption(s)"
          % (len(dangling), len(stale_exemptions)))

if bad:
    print()
    print("=" * 74)
    print("PROBLEMS (%d skills)" % len(bad))
    print("=" * 74)
    for k in sorted(bad):
        print("  %s" % k)
        for v in bad[k]:
            print("      - %s" % v)
if bad or dangling or stale_exemptions:
    sys.exit(1)
print()
print(">>> ALL THREE CONFIRMED: %d/%d structurally clean, %d/%d end with a static live-data section and print nothing promotional, "
      ">>> %d/%d backticked references resolve"
      % (len(rows), len(rows), len(ok), len(rows),
         sum(xref_seen.values()), sum(xref_seen.values())))
