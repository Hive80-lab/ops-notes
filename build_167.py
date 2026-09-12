import re, sys
from pathlib import Path

R = Path("/tmp/ops-notes")
SLUG = "small-team-ops-audit-and-runbook-services"
URL = "https://hive80-lab.github.io/ops-notes/" + SLUG + ".html"
TODAY = "2026-09-12"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Two fixed-fee ops services for small teams: the $149 audit and the $249 runbook | HIVE80 Lab Ops Notes</title>
<meta name="description" content="Fixed-fee, no-retainer services for small teams: a prioritized security and ops audit with a fix plan in five days ($149), and a done-for-you custom incident runbook delivered in 48 hours ($249).">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/small-team-ops-audit-and-runbook-services.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Two fixed-fee services for small teams: a security audit and a custom incident runbook</h1>
<p><em>Fixed fee. No retainer, no lock-in, no software to install. If we do not deliver at least ten actionable findings (audit) or a runbook you would actually use at 2am (runbook), you get your money back.</em></p>
<p>This site publishes 160+ free ops checklists because most small teams can self-serve. Two situations keep coming up where self-serve stalls, and they are the only two things we sell as a service: <strong>knowing where you stand</strong> (the audit) and <strong>surviving the 2am call</strong> (the runbook).</p>

<h2>Service 1 &mdash; Small-Team Ops Audit: $149, five business days</h2>
<p>A prioritized findings report for your estate: identity and access, devices, network, data and backups, vendor and SaaS exposure, and incident readiness &mdash; the same <a href="small-business-security-audit-checklist.html">45-point structure we publish</a>, run by someone whose full-time job is noticing what owners stop seeing.</p>
<h3>What you get</h3>
<ul>
<li><strong>A numbered findings list, each with three lines:</strong> the finding, the risk in one plain sentence, and the fix with a suggested date and owner. No vulnerability-score essay, no 40-page PDF.</li>
<li><strong>Triage you can act on:</strong> every finding is critical / high / hygiene, so the first week of fixes is already sequenced.</li>
<li><strong>A 90-minute walkthrough call</strong> where we look at your consoles together &mdash; you keep the recording.</li>
<li><strong>A fix-check spreadsheet</strong> with the findings pre-loaded, so progress is a column, not a memory.</li>
</ul>
<h3>How it runs</h3>
<ol>
<li><strong>Intake (20 minutes):</strong> a short questionnaire about your stack &mdash; identity provider, devices, cloud accounts, backups, vendors. No agents installed, no credentials shared.</li>
<li><strong>Walkthrough (90 minutes):</strong> a video call where you screen-share the consoles and we walk the checklist together. Everything stays read-only.</li>
<li><strong>Report (5 business days):</strong> the one-page report plus the fix-check spreadsheet, delivered by email. One 30-minute follow-up call included.</li>
</ol>
<p><strong>Guarantee:</strong> if the report does not contain at least ten actionable findings, the fee comes back in full. <strong>Price: A$149, fixed.</strong> <a href="https://hive80lab.gumroad.com/l/ljogci">Buy the Small-Team Ops Audit</a> (checkout takes two minutes; the intake form arrives immediately).</p>

<h2>Service 2 &mdash; Custom Incident Runbook: $249, 48 hours</h2>
<p>A runbook is what the on-call person actually opens at 2am: one page per incident type, written for <em>your</em> stack, with your names, your tools, and your escalation path &mdash; not generic prose. We build it from your estate and deliver it in 48 hours.</p>
<h3>What you get</h3>
<ul>
<li><strong>First-30-minutes page per incident type</strong> (service down, data suspected lost/exfiltrated, account compromised, vendor outage): what to check, what to contain, who to call, in what order.</li>
<li><strong>Escalation ladder with names and numbers,</strong> including the out-of-band path when your main channel is the thing that is down.</li>
<li><strong>Communication templates:</strong> the first status page line, the customer email, the internal update &mdash; pre-written so nobody drafts under adrenaline (the templates follow our <a href="incident-communication-templates.html">incident communication templates</a>).</li>
<li><strong>Recovery sequence with verification steps,</strong> including the checks that prove the incident is actually over.</li>
<li><strong>Printable + digital formats:</strong> a PDF built for a printed binder, plus a plain-text version that lives in your wiki.</li>
</ul>
<h3>How it runs</h3>
<ol>
<li><strong>Intake (20 minutes):</strong> your stack, your incident history, who is on-call, where things live.</li>
<li><strong>Draft (48 hours):</strong> the runbook arrives, built from your answers and one clarification thread if needed.</li>
<li><strong>Drill (30 minutes, optional):</strong> a call where we walk one incident type against the runbook and fix what trips.</li>
</ol>
<p><strong>Price: A$249, fixed.</strong> <a href="https://hive80lab.gumroad.com/l/hkljh">Buy the Custom Incident Runbook</a> (intake form arrives on checkout).</p>

<h2>Which one do you need?</h2>
<table>
<tr><th>The sentence you just said out loud</th><th>What that means</th><th>Order</th></tr>
<tr><td>"Honestly, I don't know where we stand."</td><td>You need the audit</td><td><a href="https://hive80lab.gumroad.com/l/ljogci">Ops Audit &mdash; $149</a></td></tr>
<tr><td>"I lie awake wondering who handles a 2am outage."</td><td>You need the runbook</td><td><a href="https://hive80lab.gumroad.com/l/hkljh">Custom Runbook &mdash; $249</a></td></tr>
<tr><td>"Both, and we want it to fit together."</td><td>Audit first &rarr; runbook built from its findings</td><td>Both links, in that order</td></tr>
</table>
<p>The combined path is deliberately sequential: the audit's critical findings become the runbook's first chapters, so the $249 document is aimed at your actual weaknesses instead of a generic worst-case list.</p>

<h2>What we do not sell</h2>
<ul>
<li><strong>No retainers.</strong> Fixed fee, defined scope, done.</li>
<li><strong>No software or agents.</strong> Nothing is installed on your machines.</li>
<li><strong>No system changes.</strong> We do not touch your configs; we tell you what to change and you or your contractor make the change.</li>
<li><strong>No upsell ladder.</strong> The free checklists on this site cover everything the services do not cover; nothing here requires buying anything else.</li>
</ul>

<h2>Questions people ask first</h2>
<ul>
<li><strong>Do you see our data?</strong> No. The walkthrough is read-only screen-share on your side; nothing is uploaded, stored, or shared. The report is written from what is on the call. An NDA is available on request before intake.</li>
<li><strong>We're all Mac / all Windows / mixed. Does it matter?</strong> No &mdash; the checklist structure is platform-agnostic and the fixes name the platform-specific control (FileVault, BitLocker, and so on).</li>
<li><strong>Can you just do the fixes for us?</strong> Not as part of these two services &mdash; that is an MSP relationship and a different business. What you get is the sequenced plan; most teams clear the criticals in under a week with it.</li>
<li><strong>What if we disagree with a finding?</strong> The follow-up call exists for exactly that. Findings are evidence-based; if we cannot show you the evidence, it does not ship in the report.</li>
<li><strong>Refunds?</strong> Audit: at least ten actionable findings or your money back. Runbook: if it would not survive a read-through by your on-call person, tell us within 7 days and it comes back to you revised or refunded.</li>
</ul>

<h2>Where this fits</h2>
<p>The free versions of both documents live on this site: the <a href="small-business-security-audit-checklist.html">45-point audit checklist</a> you can run yourself, and the <a href="incident-response-plan-template-small-teams.html">incident response plan template</a> plus the free <a href="https://hive80lab.gumroad.com/l/first-30-minutes">First 30 Minutes</a> card. The services exist for the teams that would rather have an outside pair run it &mdash; and for the audit's findings to turn into a runbook that names your servers, your tools, and your people.</p>

<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; full incident-response kit for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ljogci">Small-Team Ops Audit</a> &mdash; prioritized findings + fix plan, five-day turnaround &mdash; $149</li>
<li><a href="https://hive80lab.gumroad.com/l/hkljh">Custom Incident Runbook</a> &mdash; done-for-you, built from your estate, 48h &mdash; $249</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $29</li>
</ul>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
"""

INT = set(re.findall(r'href="([a-z0-9-]+\.html)"', PAGE))
missing = [h for h in sorted(INT) if not (R / h).exists()]
if missing:
    print("ABORT: internal targets missing on disk:", missing); sys.exit(1)
print(f"internal links pre-verified: {len(INT)} distinct targets, 0 missing")

RECIP = {
 "small-business-security-audit-checklist.html": (
   "&mdash; and the audit's criticals become its first chapter.</p>",
   ' If you would rather have an outside pair run the walkthrough and write the fix plan, that is the <a href="small-team-ops-audit-and-runbook-services.html">audit-and-runbook service</a>.</p>'),
 "ops-starter-kit-landing.html": (
   '<h2>Free companions</h2><ul>',
   '<h2>Free companions</h2><ul>\n<li><a href="small-team-ops-audit-and-runbook-services.html">Small-Team Ops Audit &amp; Custom Runbook Services</a> &mdash; fixed-fee, no retainer: prioritized findings in five days, a 2am runbook in 48 hours.</li>'),
 "incident-response-plan-template-small-teams.html": (
   '<li><a href="visitor-log-template.html">Visitor Log Template for Small Offices</a></li>',
   '<li><a href="small-team-ops-audit-and-runbook-services.html">Small-Team Ops Audit &amp; Custom Runbook Services</a></li>\n'),
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

import xml.dom.minidom as minidom
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

CARD = ('<li><a href="small-team-ops-audit-and-runbook-services.html">Two Fixed-Fee Services: The Small-Team Ops '
 'Audit and the Custom Incident Runbook</a><div class="desc">The only two things we sell as a service, for the two '
 'situations where self-serve stalls: knowing where you stand (a prioritized findings report with a fix plan, '
 'five-day turnaround, A$149, at least ten actionable findings or your money back) and surviving the 2am call '
 '(a done-for-you incident runbook built from your actual stack, delivered in 48 hours, A$249). No retainer, no '
 'agents, no system changes, no upsell ladder.</div></li>')
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
line = ('- **NEW: [Two Fixed-Fee Services for Small Teams: The Ops Audit and the Custom Incident Runbook]'
 '(https://hive80-lab.github.io/ops-notes/small-team-ops-audit-and-runbook-services.html)** \u2014 the only two '
 'things we sell as a service: a prioritized security/ops audit (A$149, five business days, numbered findings '
 'with risk + fix + owner, at least ten actionable findings or your money back) and a done-for-you custom '
 'incident runbook (A$249, 48-hour delivery, first-30-minutes pages per incident type, escalation ladder, '
 'comms templates, printable + wiki formats). How it runs, which one you need, what we do not sell, and the '
 'five questions people ask first.\n')
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
