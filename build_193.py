#!/usr/bin/env python3
"""ops-notes page #193 — paging policy: what deserves a page. Canonical repo: mirror."""
import re, sys
from pathlib import Path
from datetime import date
import xml.dom.minidom as minidom

R = Path("/Users/haroonqamer/Swarm/hive/state/seo/ops-notes")
SLUG = "paging-policy-what-deserves-a-page"
URL = "https://hive80-lab.github.io/ops-notes/paging-policy-what-deserves-a-page.html"
TODAY = date.today().isoformat()

PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Paging Policy: What Deserves a Page (The Bar for Waking a Human) &mdash; HIVE80lab</title>
<meta name="description" content="A paging policy that protects both uptime and sleep: the three response classes (page, ticket, log), the four-question page test, the rules that make a page worth answering (one symptom per page, symptom not cause, runbook link mandatory, actionable-only), the anti-flap rule that demotes noisy alerts instead of burning out on-call, and a worked example that took a team from 9 pages a week to 2 real ones.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/paging-policy-what-deserves-a-page.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Paging policy: what deserves a page</h1>
<p><em>A page is the most expensive message in your company: it costs sleep, and sleep is what keeps the next incident fixable.</em></p>
<p>Every alerting setup drifts the same way: someone adds an alert because a thing once broke, nobody ever removes one, and within a year the on-call phone is a noise machine that everyone silences &mdash; which means when the real page fires at 2 a.m., it arrives as the eleventh buzz of the night and gets swiped away like the rest. The fix is not better alerting. It is a <strong>paging bar</strong>: a written policy for what deserves a human, what deserves a business-hours read, and what deserves nothing but a log line.</p>

<h2>1. The three response classes &mdash; every alert maps to exactly one</h2>
<ul>
<li><strong>Page</strong> &mdash; a human wakes up now. Reserved for symptoms that are burning customer trust or money while everyone sleeps.</li>
<li><strong>Ticket</strong> &mdash; a human reads it in business hours. This is where most &ldquo;urgent&rdquo; alerts actually belong: capacity trends, certificate expiry with 30 days left, replica lag without customer impact.</li>
<li><strong>Log</strong> &mdash; nobody reads it until someone asks. Fine for noise you are not ready to delete; dishonest only if you call it monitoring.</li>
</ul>
<p>The mapping is written down per alert, not decided by whatever severity the monitoring tool defaulted to. An alert with no assigned class is a ticket by default &mdash; the burden of proof is on the page, because the page spends a human&rsquo;s night.</p>

<h2>2. The four-question page test</h2>
<p>Before any alert earns page status, it must pass all four; three yeses is a ticket with a fast SLA:</p>
<ul>
<li><strong>Does it need a human decision <em>now</em>?</strong> Not &ldquo;soon&rdquo; &mdash; now. Backup age growing is a ticket; backups not <em>running</em> is a page.</li>
<li><strong>Can a human actually fix it now?</strong> If the only action is &ldquo;wait for the vendor&rdquo; or &ldquo;wait for the queue to drain,&rdquo; it is a ticket with a timer, not a page.</li>
<li><strong>Will ignoring it make it worse?</strong> A self-healing blip is a log line. A thing that pages once and burns out if nobody looks is a page.</li>
<li><strong>Are customers feeling it, or about to?</strong> Internal-only degradation with a workaround waits for morning.</li>
</ul>

<h2>3. What a page must carry &mdash; and the anti-flap rule</h2>
<ul>
<li><strong>One page, one symptom.</strong> A page that says &ldquo;CPU &gt; 80%, memory &gt; 85%, disk &gt; 90%, queue &gt; 1000&rdquo; is four pages wearing a trench coat, and it wakes a human to do triage the alert system should have done.</li>
<li><strong>Page on symptom, not cause.</strong> &ldquo;Checkout error rate 4%&rdquo; wakes the right person. &ldquo;iostat latency high&rdquo; wakes whoever happens to know what iostat is.</li>
<li><strong>Runbook link mandatory.</strong> Every page links the runbook for its own symptom. A page without a runbook is a riddle at 2 a.m.; write the link or demote the alert. The <a href="https://hive80-lab.github.io/ops-notes/runbook-template.html">runbook template</a> takes ten minutes per alert.</li>
<li><strong>Anti-flap:</strong> three pages from one alert inside an hour &rarr; the alert is automatically demoted to ticket status pending tuning, and the demotion is announced. The alert is broken, not the on-call &mdash; and saying so out loud is what keeps people trusting the pager.</li>
</ul>

<h2>4. The sleep budget (and the repeat-offender rule)</h2>
<p>Paging volume is a budget, not a weather report: target <strong>under two pages per person per shift</strong>, median, not best week. Two enforcement mechanisms keep it honest:</p>
<ul>
<li><strong>Repeat-offender rule:</strong> any alert that fires at the same hour three weeks running gets tuned or deleted &mdash; an alert that wakes the same person every Wednesday is no longer information, it is a subscription.</li>
<li><strong>Night-page review:</strong> every overnight page gets 60 seconds of review at morning handoff: real or noise? The <a href="https://hive80-lab.github.io/ops-notes/on-call-handover-template.html">handover template</a> carries the count. Three noisy nights in a month means the bar moved &mdash; tighten it.</li>
</ul>
<p>This is the flip side of the <a href="https://hive80-lab.github.io/ops-notes/alert-fatigue-checklist.html">alert fatigue checklist</a>: that page fixes a noisy system; this one decides what the quiet system is allowed to wake you for.</p>

<h2>5. Worked example</h2>
<p>An 8-person SaaS, two-person on-call rotation. 41 alerts, 19 of them paging, 9 pages per week median, and the on-call had taken to muting the phone after midnight &mdash; which is how a real cache-layer outage waited 40 minutes for a customer email. The re-bar took one afternoon: 19 paging alerts &rarr; 6 (4 with fresh runbook links, 2 demoted for being unfixable at night), 11 moved to ticket with SLAs, the rest deleted. Six weeks later: 1.4 pages per shift median, 100% of pages had runbook links, and the repeat-offender rule had already killed the &ldquo;CPU &gt; 80%&rdquo; alert that had never once correlated with anything. The next real page &mdash; a certificate chain break &mdash; got answered in three minutes, because the phone still meant something.</p>

<h2>6. Metrics</h2>
<ul>
<li>Pages per person per shift: <strong>median &le; 2</strong> &mdash; above that, the bar is broken, not the on-call.</li>
<li>Pages actionable (fix existed and was done): <strong>&ge; 95%</strong>.</li>
<li>Pages with a runbook link: <strong>100%</strong> &mdash; binary, checked in the monthly sweep.</li>
<li>Repeat pages within 24h: <strong>&lt; 5%</strong> &mdash; a repeat page means the first response did not hold, and that is an incident question, not an alert question.</li>
</ul>

<h2>Where this fits</h2>
<p>The paging bar sits between three siblings: the <a href="https://hive80-lab.github.io/ops-notes/incident-severity-matrix-template.html">incident severity matrix</a> decides who leads once a page is answered; the <a href="https://hive80-lab.github.io/ops-notes/oncall-escalation-path-tiers.html">escalation path tiers</a> decide who is woken second; the <a href="https://hive80-lab.github.io/ops-notes/alert-fatigue-checklist.html">alert fatigue checklist</a> prunes the volume that never should have paged at all. For the estate behind the alerts &mdash; runbooks, access, the audit nobody has time for &mdash; book the <a href="small-team-ops-audit-and-runbook-services.html">small-team ops audit &amp; runbook service</a>.</p>

<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $29</li>
</ul>

<p><em>Related: the <a href="https://hive80-lab.github.io/ops-notes/alert-fatigue-checklist.html">alert fatigue checklist</a> prunes alert volume, the <a href="https://hive80-lab.github.io/ops-notes/oncall-escalation-path-tiers.html">escalation path tiers</a> decide who gets woken next, and the <a href="https://hive80-lab.github.io/ops-notes/incident-severity-matrix-template.html">severity matrix</a> decides who leads once they are awake.</em></p>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
'''

RECIP = {
 "alert-fatigue-checklist.html": (
   '<li><a href="runbook-template.html">Runbook Template (Free, Copy-Paste)</a></li>',
   '<li><a href="runbook-template.html">Runbook Template (Free, Copy-Paste)</a></li>\n<li><a href="paging-policy-what-deserves-a-page.html">Paging policy: what deserves a page</a> &mdash; the bar for waking a human, with the anti-flap rule that demotes noisy alerts instead of burning out on-call.</li>\n'),
 "oncall-escalation-path-tiers.html": (
   '</main>',
   '<p class="related">The tiers decide <em>who</em> is woken; the <a href="paging-policy-what-deserves-a-page.html">paging policy</a> decides whether anyone is woken at all &mdash; the four-question page test keeps the pager reserved for symptoms that burn customer trust.</p>\n</main>'),
 "incident-severity-matrix-template.html": (
   '</main>',
   '<p class="related">The severity matrix runs after the page lands; the <a href="paging-policy-what-deserves-a-page.html">paging policy</a> decides what merits the page in the first place &mdash; four questions, every alert, or the pager becomes noise.</p>\n</main>'),
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

CARD = ('<li><a href="paging-policy-what-deserves-a-page.html">Paging Policy: What Deserves a Page</a>'
 '<div class="desc">The bar for waking a human: the three response classes (page, ticket, log), the four-question '
 'page test, what every page must carry (one symptom, symptom not cause, runbook link, actionable), the anti-flap '
 'rule that demotes noisy alerts automatically, and the sleep budget. Worked example: 8-person SaaS, 9 pages a week '
 'and a muted phone &mdash; re-barred to 6 paging alerts, 1.4 pages per shift, and the next real page answered in 3 minutes.</div></li>')
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
line = ('- **NEW: [Paging Policy: What Deserves a Page]'
 '(https://hive80-lab.github.io/ops-notes/paging-policy-what-deserves-a-page.html)** \u2014 the bar for waking a '
 'human: three response classes, the four-question page test, runbook-link mandatory, the anti-flap demotion rule, '
 'and the sleep budget (median \u2264 2 pages/shift). Worked example: 19 paging alerts re-barred to 6, and a pager '
 'people trust again.\n')
if SLUG not in r:
    anchor = r.index("- **NEW:")
    r = r[:anchor] + line + r[anchor:]
    rp.write_text(r)
first_new = [l for l in (R/"README.md").read_text().splitlines() if l.startswith("- **NEW")][0]
print("README top:", first_new[:70])

broken = 0; checked = 0
for f in sorted(R.glob("*.html")):
    t = f.read_text()
    for href in re.findall(r'href="([^"#]+\.html)"', t):
        checked += 1
        if href.startswith("http"):
            continue
        if not (R / href).exists():
            broken += 1; print(f"  BROKEN in {f.name}: {href}")
print(f"linkcheck: {checked} internal links, {broken} broken")
sys.exit(1 if broken else 0)
