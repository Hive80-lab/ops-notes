import re, sys
from pathlib import Path

R = Path("/tmp/ops-notes")
SLUG = "security-audit-report-template"
URL = "https://hive80-lab.github.io/ops-notes/" + SLUG + ".html"
TODAY = "2026-09-12"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Security audit report template: the one-page format that gets fixes scheduled | HIVE80 Lab Ops Notes</title>
<meta name="description" content="A one-page security audit report template that gets fixes scheduled instead of shelved: header block, triage scoring rubric, F-numbered findings with evidence and owners, an executive summary that fits on a phone screen, and the handling rules for a document that is itself sensitive.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/security-audit-report-template.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Security audit report template: the one-page format that gets fixes scheduled</h1>
<p><em>Filed under security &middot; pairs with the <a href="small-business-security-audit-checklist.html">45-point audit checklist</a> and the <a href="severity-matrix-3-levels.html">3-level severity matrix</a></em></p>
<p>Most security audit reports fail in the same way: they are thorough, accurate, and unread. Forty pages of findings, no owner on any line, and a critical item buried on page 23 is a report that changes nothing. A small team needs one page that a founder can read in four minutes and act on this week. This is that template &mdash; built to follow the <a href="small-business-security-audit-checklist.html">45-point walkthrough</a>, but it works with any audit.</p>

<h2>1. The header block: scope before opinion</h2>
<p>Every report opens with five lines that stop the two arguments that kill audits ("you looked at the wrong things" and "but that's not in scope"):</p>
<table>
<tr><th>Field</th><th>Example</th></tr>
<tr><td>Scope</td><td>Identity (Google Workspace, GitHub), 14 laptops, office network, 23 SaaS tools, backups (Backblaze + local NAS)</td></tr>
<tr><td>Method</td><td>45-point checklist walkthrough, read-only, evidence by screenshot</td></tr>
<tr><td>Date + auditor</td><td>2026-09-12, internal (or external pair)</td></tr>
<tr><td>Out of scope</td><td>Production code review; the office printer network segment (deferred to next audit)</td></tr>
<tr><td>Headline</td><td>3 criticals, 5 high, 12 hygiene &mdash; first fix due 2026-09-15</td></tr>
</table>

<h2>2. The scoring rubric: three levels, defined by attacker behavior</h2>
<p>Severity is not a feeling. Tie each level to what an attacker would do with it (the same levels as the <a href="severity-matrix-3-levels.html">severity matrix</a>):</p>
<table>
<tr><th>Level</th><th>Definition</th><th>Clock</th></tr>
<tr><td><strong>Critical</strong></td><td>An attacker would use it today, without luck</td><td>Fix within 7 days</td></tr>
<tr><td><strong>High</strong></td><td>An attacker would need luck, opportunity, or a second weakness</td><td>Fix within 30 days</td></tr>
<tr><td><strong>Hygiene</strong></td><td>Compounds over time; no direct path</td><td>Batch quarterly</td></tr>
</table>

<h2>3. The findings section: F-numbers, not paragraphs</h2>
<p>Each finding is one row, numbered F-001 onward. One finding = one sentence of risk + one fix + one name + one date. The format that forces all five fields:</p>
<table>
<tr><th>#</th><th>Finding</th><th>Severity</th><th>Risk in one sentence</th><th>Fix</th><th>Owner</th><th>Due</th></tr>
<tr><td>F-001</td><td>No MFA on the accounting SaaS</td><td>Critical</td><td>One phished password gives full access to company funds</td><td>Enforce TOTP MFA for all 6 users; verify by login test</td><td>Priya</td><td>2026-09-15</td></tr>
<tr><td>F-002</td><td>Ex-employee active on the NAS share</td><td>Critical</td><td>Departed accounts are the quietest way in; nobody is watching them</td><td>Disable account; run the leaver list for the last 12 months</td><td>Dan</td><td>2026-09-15</td></tr>
<tr><td>F-003</td><td>Restore test never run on the NAS backup</td><td>Critical</td><td>A backup that has never restored is a hope, not a control</td><td>Run the 20-minute restore drill; record file name + timing</td><td>Priya</td><td>2026-09-18</td></tr>
<tr><td>F-004</td><td>Router firmware 2 versions behind</td><td>High</td><td>Known CVEs are patched; exposure needs the attacker to reach the LAN</td><td>Update firmware this maintenance window</td><td>Dan</td><td>2026-10-01</td></tr>
<tr><td>F-005</td><td>DMARC at none</td><td>High</td><td>Anyone can send email as the company domain</td><td>Publish DMARC quarantine with weekly reports</td><td>Priya</td><td>2026-09-25</td></tr>
</table>
<p>Rules that keep findings honest: every critical must cite its evidence (a screenshot, a command output, a config export); every fix must be something the named owner can do without buying anything first; no finding shares a row with another finding, even when they share a root cause &mdash; root causes go in the summary.</p>

<h2>4. The executive summary: four sentences</h2>
<p>Written last, read first. Four sentences, no jargon:</p>
<ol>
<li><strong>Where we stand:</strong> "We walked a 45-point audit across identity, devices, network, data, vendors, and incident readiness."</li>
<li><strong>What we found:</strong> "3 criticals (accounting MFA, departed-employee access, untested backups), 5 high, 12 hygiene."</li>
<li><strong>What happens next:</strong> "Criticals are scheduled with named owners for the week of 15 Sep; highs are scheduled within 30 days."</li>
<li><strong>What we need:</strong> "Two hours of Priya's week and one firmware window. Nothing else."</li>
</ol>
<p>If the summary needs more than four sentences, the findings section is doing the summary's job and both will be ignored.</p>

<h2>5. Handling rules: the report is itself a security artifact</h2>
<p>A list of every weakness in the company, in writing, is exactly what an attacker wants. Treat the report accordingly:</p>
<ul>
<li><strong>Store it</strong> where payroll lives &mdash; same access list, same encryption &mdash; not in the shared drive everyone can read.</li>
<li><strong>Share the full report</strong> with the people who own fixes. Everyone else gets the executive summary only.</li>
<li><strong>Retire findings, not the report:</strong> when a fix lands, mark the F-number fixed with a date &mdash; the remaining open items are next audit's starting list.</li>
<li><strong>Never email the full report</strong> to a contractor or vendor; give them their own findings, nothing more.</li>
<li><strong>Re-audit cadence:</strong> the full walkthrough twice a year; the open-findings list reviewed monthly in ten minutes.</li>
</ul>

<h2>6. When the report is better written by someone else</h2>
<p>Internal audits catch what insiders stop seeing less of; external audits catch what insiders never saw at all. The honest trigger: if you have run the 45-point checklist yourself and the critical count still sits above eight, or if nobody in the team owns the fixes, bring in an outside pair &mdash; that is exactly what the <a href="small-team-ops-audit-and-runbook-services.html">Small-Team Ops Audit service</a> delivers: this report format, filled from your estate, with the fixes sequenced, in five business days. And when the report says the incident-readiness zone is weak, the follow-on is a <a href="https://hive80lab.gumroad.com/l/hkljh">done-for-you runbook</a> built from the findings.</p>

<h2>Where this fits</h2>
<p>The report is the output; the walkthrough is the <a href="small-business-security-audit-checklist.html">45-point checklist</a>; the severity levels are the <a href="severity-matrix-3-levels.html">3-level matrix</a>; the fixes land in the <a href="server-hardening-checklist-small-teams.html">hardening checklist</a> and the <a href="patch-management-checklist.html">patch management checklist</a>. When the incident-readiness findings need a plan rather than a fix, the <a href="incident-response-plan-template-small-teams.html">IR plan template</a> is the next page.</p>

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
   'that is the <a href="small-team-ops-audit-and-runbook-services.html">audit-and-runbook service</a>.</p>',
   'that is the <a href="small-team-ops-audit-and-runbook-services.html">audit-and-runbook service</a>; and the report the walkthrough produces has its own format &mdash; see the <a href="security-audit-report-template.html">security audit report template</a>.</p>'),
 "severity-matrix-3-levels.html": (
   '<li><a href="ops-starter-kit-landing.html">Ops Starter Kit &mdash; Incident Response for Small Teams ($14)</a></li>',
   '<li><a href="security-audit-report-template.html">Security Audit Report Template</a> &mdash; the one-page format that turns an audit into scheduled fixes.</li>\n'),
 "mfa-rollout-checklist-small-business.html": (
   '<li><a href="dns-filtering-checklist.html">DNS Filtering Checklist</a></li>',
   '<li><a href="security-audit-report-template.html">Security Audit Report Template</a> &mdash; one page, five fields per finding, owners and dates.</li>\n'),
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

CARD = ('<li><a href="security-audit-report-template.html">Security Audit Report Template '
 '(The One-Page Format That Gets Fixes Scheduled)</a><div class="desc">Most audit reports are thorough, '
 'accurate, and unread. This one-page format changes that: a five-line header block that kills scope '
 'arguments, a three-level rubric defined by attacker behavior (criticals in 7 days), F-numbered findings '
 'with evidence, risk-in-one-sentence, fix, owner and due date, a four-sentence executive summary, and the '
 'handling rules for a document that is itself a security artifact.</div></li>')
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
line = ('- **NEW: [Security Audit Report Template (The One-Page Format That Gets Fixes Scheduled)]'
 '(https://hive80-lab.github.io/ops-notes/security-audit-report-template.html)** \u2014 the report format that '
 'follows the 45-point walkthrough: scope-first header block, three-level rubric defined by attacker behavior, '
 'F-numbered findings with evidence + risk sentence + fix + owner + due date, a four-sentence executive summary, '
 'and handling rules for a document that is itself sensitive.\n')
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
