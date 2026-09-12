#!/usr/bin/env python3
"""ops-notes page #180 — RACI matrix template."""
import re, sys
from pathlib import Path
import xml.dom.minidom as minidom

R = Path("/private/tmp/ops-notes")
SLUG = "raci-matrix-template"
URL = "https://hive80-lab.github.io/ops-notes/raci-matrix-template.html"
TODAY = "2026-09-14"

PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RACI Matrix Template for Small Teams (Stop Asking Who Owns This) &mdash; HIVE80lab</title>
<meta name="description" content="A RACI matrix that fits one page: the four letters defined once with small-team corrections (R is one name, A is a person not a team, C is a short list with an expiry), the five-column table, the four failure modes (two Rs, no A, C-spam, the missing I), the 90-second row test, and three metrics. Worked example: a fifteen-person SaaS that found nine decisions with two owners and six with none &mdash; and cut launch-decision stalls from 11 days to under 24 hours.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/raci-matrix-template.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>RACI matrix template: stop asking who owns this</h1>
<p><em>One page. Every recurring decision in the business, four letters per row, one name per letter. The cure for the meeting that ends with &ldquo;so&hellip; who&rsquo;s actually doing this?&rdquo; Works best next to the <a href="role-permission-matrix-template.html">role-permission matrix</a> (what each role may touch) and the <a href="decision-log-template.html">decision log</a> (what was decided and when).</em></p>
<p>RACI assigns every decision four roles: <strong>R</strong> &mdash; the one person who does the work; <strong>A</strong> &mdash; the one person who owns the outcome and can settle the row (accountable); <strong>C</strong> &mdash; the short list consulted <em>before</em> the decision; <strong>I</strong> &mdash; the short list informed <em>after</em> it. It takes thirty minutes to build and saves an hour a week for as long as the team exists. The template below is tuned for small teams, where the textbook version quietly fails: nobody has one job, so &ldquo;R&rdquo; written as a department means nobody does the work.</p>

<h2>The four letters, defined once</h2>
<table>
<tr><th>Letter</th><th>Means</th><th>The small-team correction</th></tr>
<tr><td>R &mdash; Responsible</td><td>Does the work</td><td><strong>Exactly one name.</strong> Never a team, never &ldquo;marketing&rdquo;. If two people are genuinely both doing it, it is two rows.</td></tr>
<tr><td>A &mdash; Accountable</td><td>Owns the outcome; settles disagreements</td><td><strong>One person, and a person.</strong> On a team under twenty, A and R may be the same human for most rows &mdash; that is not a violation, it is speed.</td></tr>
<tr><td>C &mdash; Consulted</td><td>Gives input before the decision</td><td><strong>Two-way, time-boxed.</strong> A name on C owes an opinion by a date; a C that never answers stops being consulted and becomes an I.</td></tr>
<tr><td>I &mdash; Informed</td><td>Told after the decision</td><td><strong>One-way, batched.</strong> No consent required, no veto. If being informed feels bad, they should have been C &mdash; and C has a deadline.</td></tr>
</table>

<h2>The five-column table</h2>
<p>The whole matrix is one table with five columns and rows you can read in one screen: <strong>decision or deliverable</strong> (a noun phrase a new hire understands), <strong>R (one name)</strong>, <strong>A (one name)</strong>, <strong>C (short list)</strong>, <strong>I (short list)</strong>. One page, twenty to forty rows: the recurring decisions where ownership fog costs real days &mdash; pricing changes, incident severity calls, vendor renewals, publishes, purchases, who approves access grants (that side lives in the <a href="role-permission-matrix-template.html">role-permission matrix</a>; RACI says <em>who decides</em>, the permission matrix says <em>what the hands may touch</em>).</p>

<h2>The four failure modes</h2>
<p>Every broken matrix fails in one of four ways, and each has a one-line tell:</p>
<p><strong>1. Two Rs.</strong> The split-brain row: two names both &ldquo;doing the work&rdquo; means neither does it, and the deadline splits in half instead of the work. Tell: work stalls until one person is embarrassed into it. Fix: pick one R today, move the other to C or I.</p>
<p><strong>2. No A.</strong> The orphan decision: a row with an R and no accountable owner means the decision has no arbiter when the Rs disagree or the C-list deadlocks. Tell: the decision lives in a chat thread until someone senior notices. Fix: A is the person whose budget or queue the decision spends &mdash; usually the row is theirs already.</p>
<p><strong>3. C-spam.</strong> Everyone consulted, nothing ships: the C list is a courtesy list, and every courtesy costs a day of waiting. Tell: &ldquo;waiting on feedback&rdquo; appears in every status update. Fix: C list maxes at three, each with a reply-by date; beyond three, the extras are I.</p>
<p><strong>4. The missing I.</strong> The surprise: someone is ambushed by a decision they were sure they&rsquo;d be told about. Tell: &ldquo;why did I find out from a customer?&rdquo; Fix: walk the list of people downstream of the decision and name them, then trust the <a href="escalation-policy-template.html">escalation policy</a> to route the exceptions.</p>

<h2>The 90-second test</h2>
<p>Pick any row and ask one question: <strong>if this stalls today, whose name do I call?</strong> Not &ldquo;which team&rdquo;, not &ldquo;who cares most&rdquo; &mdash; whose <em>name</em>. If the answer is one name, the row is alive. If the answer is &ldquo;depends&rdquo;, the row is two rows. If the answer is &ldquo;the founder&rdquo;, the founder is the bottleneck and the row is a delegation waiting to happen &mdash; which is exactly what the founder asked for when they wrote the <a href="standing-orders-delegation-template.html">standing orders</a>.</p>

<h2>Keep it alive</h2>
<p>A matrix reviewed never dies of neglect in one quarter. Three touchpoints keep it breathing: <strong>at every project kickoff</strong>, write the project&rsquo;s rows into the same table (new project, new rows, same five columns); <strong>at every quarterly ops review</strong>, scan for dead names &mdash; anyone who left, changed role, or stopped replying comes off every list; <strong>after every incident or big win</strong>, add the decision everyone had to argue about. The reviewed row that keeps teams honest is the one that changed: &ldquo;A&rdquo; moved from founder to ops lead in March &mdash; that line in the <a href="decision-log-template.html">decision log</a> is what delegation actually looks like.</p>

<h2>Three metrics</h2>
<p>The matrix earns its keep on three numbers, checked monthly: <strong>percent of decisions with a named A</strong> (target: 100% &mdash; an unnamed A is an orphan); <strong>time-to-decision on matrix rows</strong> (the point of the page: it should fall, and stay down); <strong>escalations resolved without owner-hunting</strong> (if people still ask &ldquo;who owns this?&rdquo; in chat, the rows with fog haven&rsquo;t been filled).</p>

<h2>Worked example</h2>
<p>A fifteen-person SaaS product team. Launch decisions had a pattern: eleven days from &ldquo;should we ship&rdquo; to actually deciding, because every launch was a fresh argument about who could say yes. One afternoon with the matrix: forty-one rows &mdash; nine had two Rs, six had no A, the C lists averaged 5.5 names (one row consulted the whole 15-person company channel). They cut every C list to three with a reply-by date, named one A per row, merged the duplicate Rs into one owner with a C. The next month: launch decisions landed in under 24 hours, the founder stopped appearing in four threads a week, and the two rows that still stalled were genuinely two decisions &mdash; split them, and they stopped stalling too.</p>

<h2>Where this fits</h2>
<p>The RACI matrix is the <em>decisions</em> layer. It sits next to three siblings: the <a href="role-permission-matrix-template.html">role-permission matrix</a> is the <em>access</em> layer (who may touch what); the <a href="incident-severity-matrix-template.html">incident severity matrix</a> is the <em>incident</em> layer (who declares what, who leads); the <a href="change-freeze-calendar-template.html">change-freeze calendar</a> is the <em>timing</em> layer (when decisions pause). Own all four and the question &ldquo;who owns this?&rdquo; has one answer everywhere in the company &mdash; for the rest of the estate, book the <a href="small-team-ops-audit-and-runbook-services.html">small-team ops audit &amp; runbook service</a>.</p>
</main>
</body>
</html>
'''

KIT = '''<aside class="kit"><h2>Live from the HIVE80lab kit</h2><ul><li><a href="security-audit-scorecard.html">Security Audit Scorecard</a> &mdash; free, 45 checks scored live in your browser, nothing uploaded.</li><li><a href="https://hive80lab.gumroad.com/l/ljogci">Small-Team Ops Audit</a> &mdash; prioritized findings + fix plan, five-day turnaround &mdash; $149</li><li><a href="https://hive80lab.gumroad.com/l/hkljh">Custom Incident Runbook</a> &mdash; built from your estate, delivered in 48h &mdash; $249</li><li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free one-page incident quick-start checklist</li><li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; $14 incident response for small teams</li><li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; $27 advanced incident pack for the on-call rotation</li></ul><p class="hint">20% off any paid kit with code <strong>HIVE20</strong> at checkout.</p></aside>'''

PAGE = PAGE.replace("</main>\n</body>", KIT + "\n</main>\n</body>")

# reciprocal backlinks into 3 existing pages
RECIP = {
 "role-permission-matrix-template.html": (
   '<li><a href="employee-offboarding-checklist.html">Employee offboarding checklist</a> &mdash; revoke access the day it changes',
   '<li><a href="raci-matrix-template.html">RACI matrix template</a> &mdash; who decides, one name per letter; this page handles what each role may touch.</li>\n'),
 "decision-log-template.html": (
   '<li><a href="after-action-report-template.html">After-action report template</a>',
   '<li><a href="raci-matrix-template.html">RACI matrix template</a> &mdash; one accountable name per decision before it needs logging.</li>\n'),
 "incident-severity-matrix-template.html": (
   '<li><a href="on-call-rotation-schedule-template.html">On-call rotation schedule</a>',
   '<li><a href="raci-matrix-template.html">RACI matrix template</a> &mdash; the severity call is just a row: one A who declares, one R who leads.</li>\n'),
}
for fname, (anchor, block) in RECIP.items():
    p = R / fname
    if not p.exists():
        print(f"recip {fname}: FILE MISSING, skip"); continue
    t = p.read_text()
    if SLUG in t:
        print(f"recip {fname}: already linked, skip"); continue
    if anchor not in t:
        print(f"recip {fname}: anchor NOT FOUND, skip"); continue
    p.write_text(t.replace(anchor, block, 1))
    print(f"recip {fname}: injected")

(R / (SLUG + ".html")).write_text(PAGE)
print("page written:", SLUG + ".html", len(PAGE), "bytes")

sp = R / "sitemap.xml"
s = sp.read_text()
entry = f'<url><loc>{URL}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
if URL not in s:
    s = s.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + entry, 1)
    sp.write_text(s)
minidom.parseString(sp.read_text())
n = sp.read_text().count("<loc>")
print(f"sitemap XML-valid, {n} urls, newest-first ok={sp.read_text().split('<url>')[1].count(SLUG)==1}")

CARD = ('<li><a href="raci-matrix-template.html">RACI Matrix Template for Small Teams</a>'
 '<div class="desc">One page that ends &ldquo;who owns this?&rdquo;: the four letters defined once with '
 'small-team corrections (one R, A is a person, C lists max three with a reply-by date), the five-column '
 'table, the four failure modes &mdash; two Rs, no A, C-spam, the missing I &mdash; the 90-second row test, '
 'and three metrics. Worked example: fifteen-person SaaS, nine decisions with two owners and six with none, '
 'launch stalls cut from 11 days to under 24 hours.</div></li>')
ip = R / "index.html"
i = ip.read_text()
if SLUG not in i:
    marker = "<ul>\n<li><a href=\""
    pos = i.find(marker)
    i = i[:pos] + "<ul>\n" + CARD + "\n" + i[pos+len("<ul>\n"):]
    ip.write_text(i)
i2 = ip.read_text()
first_card = i2.find('<li><a href="')
print("index: TOP card order ok=", 0 <= i2.find(SLUG) - first_card < 500)

rp = R / "README.md"
r = rp.read_text()
line = ('- **NEW: [RACI Matrix Template for Small Teams]'
 '(https://hive80-lab.github.io/ops-notes/raci-matrix-template.html)** \u2014 the one page that stops '
 '\u201cwho owns this?\u201d: four letters defined with small-team corrections, the five-column table, four '
 'failure modes (two Rs / no A / C-spam / missing I), the 90-second row test, and a worked example that cut '
 'launch stalls from 11 days to under 24 hours.\n')
if SLUG not in r:
    anchor = r.index("- **NEW:")
    r = r[:anchor] + line + r[anchor:]
    rp.write_text(r)
first_new = [l for l in (R/"README.md").read_text().splitlines() if l.startswith("- **NEW")][0]
print("README top:", first_new[:70])

broken = 0; checked = 0
for f in sorted(R.glob("*.html")):
    t = f.read_text()
    for href in re.findall(r'href="([^"#]+\\.html)"', t):
        checked += 1
        if href.startswith("http"):
            continue
        if not (R / href).exists():
            broken += 1; print(f"  BROKEN in {f.name}: {href}")
print(f"linkcheck: {checked} internal links, {broken} broken")
sys.exit(1 if broken else 0)