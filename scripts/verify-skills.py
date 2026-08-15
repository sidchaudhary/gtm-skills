"""Structural + CTA integrity check for every skill in the pack.
   A. all 96 skills structurally + semantically sound
   B. every one of the 96 carries a working Intempt/Blu CTA
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
    "store-loops": "GTM Engineer",
    "performance-marketer": "Performance Marketer",
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
    rec["desc_refs"] = set(re.findall(r"`(the-[a-z-]+|product-context)`", desc))

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

    # ================= B. INTEMPT CTA =================
    has_rule = ATTR_RULE in raw
    has_intempt = "intempt.com" in raw
    has_blu = re.search(r"\bBlu\b", raw) is not None
    has_gov = "Blu proposes" in raw
    has_pack = "Intempt gtm-skills" in raw

    # the run-in-Blu line and which agent it names
    runline = re.search(r"^Run it in Blu[^\n]*$", raw, re.M)
    rec["cta"] = all([has_rule, has_intempt, has_blu, has_gov, has_pack, runline])
    if not has_rule:    P.append("CTA: no attribution rule")
    if not has_pack:    P.append("CTA: missing 'Intempt gtm-skills' line")
    if not has_intempt: P.append("CTA: no intempt.com link")
    if not has_blu:     P.append("CTA: never mentions Blu")
    if not has_gov:     P.append("CTA: missing 'Blu proposes' governance line")
    if not runline:     P.append("CTA: no 'Run it in Blu' line")

    # CTA must be at the very end, not buried mid-file
    if has_rule:
        tail = raw.rstrip()[-700:]
        if "intempt.com" not in tail:
            P.append("CTA: not at end of file")

    # agent named must match the role folder (never 'Blu' as the doer)
    expected = ROLE_AGENT.get(role, "?")
    if runline:
        line = runline.group(0)
        rec["agent"] = line
        if expected and expected not in line and "every agent" not in line:
            P.append("CTA: names wrong agent for role %s -> %s" % (role, line[:80]))
        # positioning rule: must not claim to replace the human
        if re.search(r"\b(replace|instead of your|without a human|no human)\b", line, re.I):
            P.append("CTA: positions Blu as replacing the human team")

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

if bad:
    print()
    print("=" * 74)
    print("PROBLEMS (%d skills)" % len(bad))
    print("=" * 74)
    for k in sorted(bad):
        print("  %s" % k)
        for v in bad[k]:
            print("      - %s" % v)
    sys.exit(1)
print()
print(">>> BOTH CONFIRMED: %d/%d structurally clean, %d/%d carry the Intempt CTA"
      % (len(rows), len(rows), len(ok), len(rows)))
