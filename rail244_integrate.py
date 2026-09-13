#!/usr/bin/env python3
"""#244 integration: two pages (customer-complaint-response-template,
open-restaurant-incident-response-system-checklist) — index TOP cards, sitemap
inserts, README NEW entries, reciprocal backlinks (4 pages each). Idempotent."""
import io, datetime

BASE = "https://hive80-lab.github.io/ops-notes/"
TODAY = datetime.date.today().isoformat()

PAGES = {
    "customer-complaint-response-template": dict(
        card_title="Customer Complaint Response Template: The Reply That Turns an Angry Customer into a Regular",
        card_desc=("A five-line reply a small business can send within the hour: acknowledge fast, restate the "
                   "problem in their words, own what happened, fix it with a date, make it right &mdash; the hour "
                   "rule for the first reply (a named human, a deadline, not the full answer), the five lines "
                   "filled in not paraphrased, the four traps (silence, the defensive paragraph, the "
                   "compensation-first reflex, the reply that reads like a legal memo). Worked example: a bakery "
                   "whose $70 make-good on a botched 25th-anniversary cake turned a one-star review into a public "
                   "update &mdash; and grew the Friday standing order by two dozen."),
        readme=("the five-line reply sent within the hour: the hour rule (the first reply is the promise of an "
                "answer, not the answer &mdash; received, read, owned, deadline), the five lines (their name and "
                "thanks, the problem restated in their words, ownership without excuses, the fix with a date, the "
                "make-good that costs less than the silence), the public-channel rule (one visible reply, then "
                "take it private), and the four traps that turn a recoverable complaint into a lost customer. "
                "Worked example: the bakery whose $70 same-day make-good earned a public update &mdash; and two "
                "dozen extra pastries on the Friday standing order &mdash; against $3,800/year walking to the "
                "franchise across the road if it had been lost."),
        backlink=("Related pages get the complaint-path twin: the "
                  "<a href=\"customer-complaint-response-template.html\">customer complaint response template</a> "
                  "is the reply side of the same contract."),
    ),
    "open-restaurant-incident-response-system-checklist": dict(
        card_title="Open-Restaurant Incident Response System Checklist: The Three-Day Playbook That Turns Accidents into Fixes",
        card_desc=("A three-day incident-response playbook for restaurants that are open when it happens: Day 1 "
                   "stabilize and measure, Day 2 investigate root cause, Day 3 diagnose and fix &mdash; with the "
                   "four-to-do lists (process, tool, people, data), the decision tree, and the third-day cleanup "
                   "that prevents relapse. Worked example: a twelve-site group that halved an 8% operational "
                   "accident rate in one quarter by taking improvisation out of the response &mdash; zero added "
                   "headcount."),
        readme=("the three-day runbook for incidents while the doors are open (Day 1 stabilize and measure, Day 2 "
                "investigate root cause, Day 3 diagnose and fix), the four-to-do lists (process, tool, people, "
                "data), the decision tree, and the third-day cleanup that stops the relapse; honest, zero-fluff. "
                "Worked example: the twelve-site restaurant group that halved an 8% accident rate in one quarter "
                "with a laminated card per station &mdash; not one extra hire."),
        backlink=None,  # filled below per target page voice
    ),
}

def read(p): return io.open(p, encoding="utf-8").read()
def write(p, s): io.open(p, "w", encoding="utf-8").write(s)

ok, fail = [], []

# ---- 1) index.html TOP cards (customer first) ----
idx = read("index.html")
anchor = "<h1>Ops notes</h1>\n"
cards = ""
for slug, m in PAGES.items():
    cards += ('<li><a href="' + slug + '.html">' + m["card_title"] + '</a><div class="desc">' + m["card_desc"] + '</div></li>\n')
if "customer-complaint-response-template" in idx and "open-restaurant-incident-response-system-checklist" in idx:
    ok.append("index: both present, skipped")
elif anchor in idx:
    write("index.html", idx.replace(anchor, anchor + cards, 1))
    ok.append("index: 2 TOP cards inserted")
else:
    fail.append("index: anchor missing")

# ---- 2) sitemap.xml: insert both at top, newest first ----
sm = read("sitemap.xml")
ins = ""
for slug in PAGES:
    ins += (f'<url><loc>{BASE}{slug}.html</loc><lastmod>{TODAY}</lastmod>'
            f'<changefreq>weekly</changefreq><priority>0.8</priority></url>')
present = [sl for sl in PAGES if sl in sm]
if len(present) == 2:
    ok.append("sitemap: both present, skipped")
else:
    hdr_end = sm.index("?>") + 2
    write("sitemap.xml", sm[:hdr_end] + ins + sm[hdr_end:])
    ok.append("sitemap: inserted %d urls" % (2 - len(present)))

# ---- 3) README.md NEW entries ----
rm = read("README.md")
if "customer-complaint-response-template" in rm and "open-restaurant-incident-response-system-checklist" in rm:
    ok.append("README: both present, skipped")
else:
    e = ""
    e += ("- **NEW: [Customer Complaint Response Template (The Reply That Turns an Angry Customer into a "
          "Regular)](" + BASE + "customer-complaint-response-template.html)** &mdash; " + PAGES["customer-complaint-response-template"]["readme"] + "\n")
    e += ("- **NEW: [Open-Restaurant Incident Response System Checklist (The Three-Day Playbook That Turns "
          "Accidents into Fixes)](" + BASE + "open-restaurant-incident-response-system-checklist.html)** &mdash; "
          + PAGES["open-restaurant-incident-response-system-checklist"]["readme"] + "\n")
    write("README.md", e + rm)
    ok.append("README: 2 NEW entries at top")

# ---- 4) reciprocal backlinks ----
def add_link(fname, sentence, label):
    s = read(fname)
    if "customer-complaint-response-template.html" in s and "open-restaurant-incident-response-system-checklist.html" not in sentence:
        pass  # guard below checks per-target
    tgt = "customer-complaint-response-template.html" if "customer-complaint-response-template.html" in sentence else "open-restaurant-incident-response-system-checklist.html"
    if tgt in s:
        ok.append(f"{label}: already linked, skipped")
        return
    # prefer appending inside the last Related <em> paragraph
    tail_needle = "</em></p>\n\n</main>"
    if tail_needle in s:
        s = s.replace(tail_needle, " " + sentence + "</em></p>\n\n</main>", 1)
        write(fname, s)
        ok.append(f"{label}: sentence appended to Related")
        return
    # else insert a fresh Related paragraph before </main>
    i = s.rfind("</main>")
    if i == -1:
        fail.append(f"{label}: no </main>")
        return
    s = s[:i] + "<p><em>Related: " + sentence + "</em></p>\n\n" + s[i:]
    write(fname, s)
    ok.append(f"{label}: new Related paragraph")

CL = ("the <a href=\"customer-complaint-response-template.html\">customer complaint response template</a> is the "
      "written reply that turns the same angry customer into a regular &mdash; the phone version gets you heard "
      "first, the written one has to prove a human read it")
OR = ("the <a href=\"open-restaurant-incident-response-system-checklist.html\">open-restaurant incident response "
      "system checklist</a> is the three-day playbook for the accident that happens while the doors are open")

add_link("voicemail-greeting-script.html", OR + ".", "voicemail->openrestaurant")
add_link("chargeback-response-template.html", OR + ".", "chargeback->openrestaurant")
add_link("missed-call-text-back-setup.html", OR + ".", "missedcall->openrestaurant")
add_link("negative-review-response-playbook.html",
         ("the <a href=\"open-restaurant-incident-response-system-checklist.html\">open-restaurant incident "
          "response system checklist</a> is the floor-side playbook when the complaint is only the visible part "
          "of an operational accident"), "negreview->openrestaurant")
add_link("incident-post-mortem-template.html", CL + ".", "postmortem->customer")
add_link("staffing-shortage-coverage-plan.html", CL + ".", "staffing->customer")
add_link("shift-handover-log-template.html", CL + ".", "handover->customer")
add_link("delayed-opening-notice-template.html", CL + ".", "delayed->customer")

print("OK:");  [print("  +", m) for m in ok]
if fail:
    print("FAIL:"); [print("  -", m) for m in fail]
