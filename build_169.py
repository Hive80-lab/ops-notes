import re, sys
from pathlib import Path

R = Path("/tmp/ops-notes")
SLUG = "security-audit-cost-small-business"
URL = "https://hive80-lab.github.io/ops-notes/" + SLUG + ".html"
TODAY = "2026-09-12"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>How much does a small business security audit cost? (Honest tiers, and what changes the price) | HIVE80 Lab Ops Notes</title>
<meta name="description" content="What a small business security audit actually costs in 2026: the four tiers from free self-audit to penetration test, the five things that drive the price up, what a fixed-fee audit includes versus what it does not, and the cost of skipping it.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/security-audit-cost-small-business.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>How much does a small business security audit cost? Honest tiers, and what changes the price</h1>
<p><em>Filed under security &middot; pairs with the <a href="small-business-security-audit-checklist.html">45-point audit checklist</a> and the <a href="security-audit-report-template.html">one-page report template</a></em></p>
<p>Search for security audit pricing and you get sales pages quoting "it depends" and enterprise reports quoting $50k. Here is the honest map for a company of five to fifty people, including what we charge for the tier we sell and what that tier deliberately does not include.</p>

<h2>1. The four tiers</h2>
<table>
<tr><th>Tier</th><th>Typical cost</th><th>What you get</th><th>Right for</th></tr>
<tr><td><strong>Self-audit</strong></td><td>One day of your time</td><td>A checklist walkthrough with evidence, scored findings (ours is free: <a href="small-business-security-audit-checklist.html">45 points</a>)</td><td>Every team, twice a year, always</td></tr>
<tr><td><strong>Fixed-fee external audit</strong></td><td>A$99&ndash;A$500 one-off</td><td>An outside pair walks the same structure, delivers a prioritized findings report with owners and dates</td><td>Teams that keep deferring the self-audit, or want a second pair of eyes</td></tr>
<tr><td><strong>Consultant / MSP engagement</strong></td><td>A$1,500&ndash;A$5,000</td><td>Days of on-site work, interviews, deeper tooling, sometimes remediation</td><td>Regulated teams, or 50+ seats with real estate complexity</td></tr>
<tr><td><strong>Penetration test</strong></td><td>A$5,000&ndash;A$15,000+</td><td>Simulated attack on your perimeter or apps, exploit narrative, remediation support</td><td>Teams with compliance deadlines or a real adversary model</td></tr>
</table>
<p>The tiers are sequential, not alternatives: a team that has never walked a checklist gets more from a $149 audit than from a $15k pentest it is not ready to act on.</p>

<h2>2. What actually drives the price</h2>
<ul>
<li><strong>Number of identity providers:</strong> one Google Workspace is an afternoon; Google + Microsoft + a code forge + a cloud console is four walks of the same zone.</li>
<li><strong>Estate size:</strong> laptops, phones, NAS boxes, printers &mdash; each device class adds verification time.</li>
<li><strong>Evidence method:</strong> read-only screen-share (fast, cheap) versus agent-based scanning (slower to start, deeper results).</li>
<li><strong>Report depth:</strong> a one-page findings report with owners is hours; a 40-page compliance-style document is days.</li>
<li><strong>Cloud account count:</strong> every AWS/GCP/Azure tenant is its own sweep of buckets, IAM roles, and forgotten test environments.</li>
</ul>

<h2>3. What a fixed-fee audit includes &mdash; and what it does not</h2>
<p>We sell the fixed-fee tier, so here is the honest boundary. Our <a href="small-team-ops-audit-and-runbook-services.html">Small-Team Ops Audit</a> is A$149 and includes: the walkthrough call (90 minutes, read-only screen-share), a numbered findings report in the <a href="security-audit-report-template.html">one-page format</a> with triage, owner and due date per finding, a fix-check spreadsheet, and a follow-up call &mdash; with the guarantee that you get at least ten actionable findings or the fee back.</p>
<p>What A$149 does <strong>not</strong> buy: exploitation attempts (that is the pentest tier), remediation work (we do not touch your systems), compliance certification, or tooling licenses. Any vendor who implies a few hundred dollars buys a pentest is selling you a scan with a logo on it.</p>

<h2>4. The cost of skipping it</h2>
<p>Three costs, in ascending order of pain:</p>
<ul>
<li><strong>The deferral tax:</strong> every quarter without an audit, the checklist's hygiene items compound &mdash; stale access, untested backups, drifted configurations. The same audit costs more to recover from later because there is more to unwind.</li>
<li><strong>The insurance surprise:</strong> cyber insurance applications ask what you attest to &mdash; MFA everywhere, backups tested, an IR plan. Answering truthfully requires exactly what an audit produces. Overstating on the form is how claims get denied (see the <a href="cyber-insurance-requirements-checklist.html">insurance requirements checklist</a>).</li>
<li><strong>The incident itself:</strong> the first hour of an unpracticed incident is spent deciding who is in charge. The <a href="https://hive80lab.gumroad.com/l/first-30-minutes">free first-30-minutes card</a> exists precisely because most of that cost is preventable with a page of preparation.</li>
</ul>

<h2>5. A rule of thumb for the budget line</h2>
<p>Teams we talk to converge on something simple: budget one fixed-fee audit (A$100&ndash;A$500) per year as the baseline, run the free self-audit six months after it, and hold the pentest budget until a compliance letter or an enterprise customer actually demands one. If an audit's critical findings take more than a month to close, the problem is not the audit budget &mdash; it is that nobody owns the fixes, which is a <a href="delegation-of-authority-template.html">delegation</a> conversation, not a spending one.</p>

<h2>6. Five numbers that tell you the audit paid for itself</h2>
<ul>
<li><strong>Cost per critical closed:</strong> audit fee &divide; criticals closed within 30 days. A$149 &divide; 3 is cheaper than any hour of downtime.</li>
<li><strong>Days-to-first-fix:</strong> from report delivery to the first closed critical. Target: under 7 days.</li>
<li><strong>Restore-test result:</strong> passed or failed &mdash; the single finding that most often separates a bad day from a company-ending one.</li>
<li><strong>Open-criticals trend:</strong> this audit's critical count versus last audit's. Down and to the right is the whole point.</li>
<li><strong>Hours spent:</strong> the walkthrough plus fixes. If a $149 audit saved a single evening of an incident, it paid for itself.</li>
</ul>

<h2>Where this fits</h2>
<p>Price is the last question; the walkthrough is the first. Start with the free <a href="small-business-security-audit-checklist.html">45-point checklist</a>, report in the <a href="security-audit-report-template.html">one-page format</a>, and bring in the outside pair when the criticals will not die &mdash; that is the <a href="small-team-ops-audit-and-runbook-services.html">audit-and-runbook service</a>, and the <a href="https://hive80lab.gumroad.com/l/ljogci">A$149 audit</a> is the whole fixed-fee tier in one purchase.</p>

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
   'security-audit-report-template.html">security audit report template</a>.</p>',
   'security-audit-report-template.html">security audit report template</a>; and if the question is what the outside version costs, the honest tiers are in the <a href="security-audit-cost-small-business.html">security audit cost guide</a>.</p>'),
 "small-team-ops-audit-and-runbook-services.html": (
   '<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start</li>',
   '<li><a href="security-audit-cost-small-business.html">How much does a security audit cost?</a> &mdash; the four tiers, what changes the price, and where a fixed-fee audit fits.</li>\n'),
 "cyber-insurance-requirements-checklist.html": (
   '<li><a href="mfa-rollout-checklist-small-business.html">MFA Rollout Checklist for Small Teams</a></li>',
   '<li><a href="security-audit-cost-small-business.html">How Much Does a Small Business Security Audit Cost?</a> &mdash; the four tiers and the five things that drive the price.</li>\n'),
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

CARD = ('<li><a href="security-audit-cost-small-business.html">How Much Does a Small Business Security Audit '
 'Cost?</a><div class="desc">The honest tiers: free self-audit (one day), fixed-fee external (A$99&ndash;A$500), '
 'consultant engagement (A$1,500&ndash;A$5,000), penetration test (A$5,000+). The five things that drive the '
 'price, what a fixed-fee audit includes versus what it does not, the cost of skipping it (deferral tax, '
 'insurance surprises, the incident itself), a budget rule of thumb, and the five numbers that tell you the '
 'audit paid for itself.</div></li>')
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
line = ('- **NEW: [How Much Does a Small Business Security Audit Cost? (Honest Tiers, and What Changes the Price)]'
 '(https://hive80-lab.github.io/ops-notes/security-audit-cost-small-business.html)** \u2014 the four tiers from '
 'free self-audit to penetration test, the five price drivers, what a fixed-fee audit includes versus what it '
 'does not (said plainly, including by the vendor selling one), the cost of skipping it, and the five numbers '
 'that tell you the audit paid for itself.\n')
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
