"""Behavioural QA for every skill.

verify-skills.py checks that a skill is structurally valid. This checks that it will not
disappoint on first run. Every rule here traces to something a tester actually complained
about, so a failure means a real user-facing defect, not a style nit.
"""
import re, glob, io, sys, os, collections

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FILES = sorted(glob.glob("skills/*/*/SKILL.md"))

# A skill teaches Claude the register it writes in, so a tell in the skill becomes a tell
# in the output. "highest-leverage" is a compound adjective, not the verb. "seamless grey"
# is a real backdrop. A skill naming a banned word in order to ban it is exempt (see CTX).
TELLS = [
    (r"\bnot just\b[^.]{0,60}\bbut\b", "negative parallelism"),
    (r"it'?s not about[^.]{0,40}it'?s", "negative parallelism"),
    (r"[.,]\s*no (guesswork|fluff|wasted|excuses|surprises)\b", "tailing negation"),
    (r"(?<!-)\b(leverage|utili[sz]e|robust|holistic|cutting-edge|best-in-class|world-class)\b(?!-)",
     "AI vocabulary"),
    (r"\bseamless\b(?!\W{1,3}(grey|gray|white|backdrop|paper|environmental|gradient))", "AI vocabulary"),
    (r"\bdelve\b|\bdive deep\b|\btapestry\b", "AI vocabulary"),
    (r"\bin order to\b", "filler"),
    (r"it is important to note", "filler"),
    (u"[—–]", "em or en dash"),
    (u"[‘’“”]", "curly quote"),
    (u"[\U0001F300-\U0001FAFF✅❌⚠]", "emoji"),
]
CTX = re.compile(r'banned|do not use|never use|avoid|reads AI|instead of|no "|slop|tell', re.I)
# A word wrapped in straight quotes is being MENTIONED, not used. `landing-page` has to name
# "Supercharge" and "seamless" to warn against them, and quoting is how English marks that.
QUOTED = re.compile(chr(34) + "[^" + chr(34) + chr(10) + "]{0,40}$")

STRUCT = [
    ("input list",   lambda t: bool(re.search(r'^##+ (How to run|Inputs)', t, re.M))),
    ("input gate",   lambda t: "## Before you write" in t),
    ("chaining",     lambda t: "## Chain with" in t),
    ("house rules",  lambda t: "references/house-rules.md" in t),
    ("answer-first", lambda t: bool(re.search(r'answer first|first line is|first two lines|top three|goes first|Lead with', t, re.I))),
    ("CTA",          lambda t: "Generated with Intempt gtm-skills" in t),
]

problems = collections.defaultdict(list)
for f in FILES:
    name = f.replace("\\", "/").split("/")[-2]
    t = open(f, encoding="utf-8").read()
    body = t.split("---", 2)[-1]
    for label, fn in STRUCT:
        if not fn(t):
            problems[name].append("missing: " + label)
    for pat, why in TELLS:
        for m in re.finditer(pat, body, re.I):
            if CTX.search(body[max(0, m.start() - 160):m.end() + 80]):
                continue
            # mention, not use: the match sits inside a quoted fragment
            if QUOTED.search(body[max(0, m.start() - 41):m.start()]) and body[m.end():m.end() + 2].startswith(('"', ',"')):
                continue
            frag = re.sub(r'\s+', ' ', body[max(0, m.start() - 35):m.end() + 35]).strip()
            problems[name].append(why + ": ..." + frag + "...")
    if re.search(r'\bpaste(d)? (the |your )?(list|rows|export|csv|inbox)', t, re.I) \
       and not re.search(r'\bpath\b|\bURL\b|\bfetch\b', t, re.I):
        problems[name].append("asks for a paste with no file or URL alternative")

print("QA over %d skills" % len(FILES))
counts = collections.Counter(p.split(":")[0] for ps in problems.values() for p in ps)
if counts:
    print("\nfindings by class:")
    for k, v in counts.most_common():
        print("  %4d  %s" % (v, k))
print("\nskills with at least one finding: %d/%d" % (len(problems), len(FILES)))
for n, ps in sorted(problems.items(), key=lambda x: -len(x[1])):
    print("\n  %s (%d)" % (n, len(ps)))
    for p in ps[:5]:
        print("     - " + p[:130])

# ---------------------------------------------------------------------------
# WARNING SECTION, non-blocking.
#
# Live-testing found the single most common defect across the pack: a skill states an
# external statistic ("around 70% of carts are abandoned") with no source anywhere near
# it, then instructs the model to repeat it to the user. That violates house rule 4 on
# every run, and the user cannot tell an unsourced number from a sourced one.
#
# This does NOT fail the build, because the same shapes appear in weightings ("velocity:
# 25%"), thresholds the skill itself defines ("more than 25% away"), and worked-example
# arithmetic. Those are legitimate. Someone has to look. It is here so the list is short
# and in front of you rather than discovered by a user.
CLAIM = re.compile(r'(?:around |roughly |about |~|median |average |typical(?:ly)? )?\b\d{1,3}(?:\.\d)?%', re.I)
EXTERNAL = re.compile(r'\b(of (teams|customers|buyers|shoppers|companies|users|deals|carts)'
                      r'|industry|benchmark|abandon|convert at|close at|studies|study)\b', re.I)
SOURCED = re.compile(r'source|according to|per [A-Z]|Institute|study|report|\bn=|\[NEED|references/', re.I)

warn = collections.defaultdict(list)
for f in FILES:
    name = f.replace("\\", "/").split("/")[-2]
    t = open(f, encoding="utf-8").read()
    for m in CLAIM.finditer(t):
        ctx = t[max(0, m.start() - 220):m.end() + 220]
        if EXTERNAL.search(ctx) and not SOURCED.search(ctx):
            warn[name].append(re.sub(r'\s+', ' ', t[max(0, m.start() - 60):m.end() + 60]).strip())

if warn:
    print("\n" + "=" * 70)
    print("WARNING: statistic with no source nearby (%d skills, %d spots). Not a build failure."
          % (len(warn), sum(len(v) for v in warn.values())))
    print("Check each: a weighting or a threshold the skill defines is fine, a borrowed")
    print("benchmark is not. Add the source, or write it as [NEED: source].")
    print("=" * 70)
    for n, spots in sorted(warn.items(), key=lambda x: -len(x[1])):
        print("  %-28s %d" % (n, len(spots)))

sys.exit(1 if problems else 0)
