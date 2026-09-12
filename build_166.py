import re, sys
from pathlib import Path

R = Path("/tmp/ops-notes")
SLUG = "small-business-security-audit-checklist"
URL = "https://hive80-lab.github.io/ops-notes/" + SLUG + ".html"
TODAY = "2026-09-12"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Small business security audit checklist: the 45-point walkthrough | HIVE80 Lab Ops Notes</title>
<meta name="description" content="A 45-point small business security audit checklist across six zones: identity and access, devices, network, data and backups, vendor and SaaS, incident readiness. Run it in a day, score it, and turn the findings into a one-page fix plan.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/small-business-security-audit-checklist.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Small business security audit checklist: the 45-point walkthrough</h1>
<p><em>Filed under security &middot; pairs with the <a href="server-hardening-checklist-small-teams.html">server hardening checklist</a> and the <a href="mfa-rollout-checklist-small-business.html">MFA rollout checklist</a></em></p>
<p>Most small teams have never run a security audit, and the reason is not laziness &mdash; it is that "audit" sounds like a six-week engagement with consultants in suits. It is not. An audit is a checklist you walk in a day, with evidence for every line, producing a scored list of findings you can fix over the next month. This page is that checklist: 45 points across six zones, a day-long schedule for running it, a scoring rule that forces prioritization, and the one-page report format that makes the results actionable instead of shelved.</p>

<h2>1. What an audit is &mdash; and is not</h2>
<p>Three words get used interchangeably and mean different things:</p>
<table>
<tr><th></th><th>Audit</th><th>Hardening</th><th>Penetration test</th></tr>
<tr><td>Question</td><td>"Where do we stand today?"</td><td>"How do we close these specific gaps?"</td><td>"Can an attacker get in?"</td></tr>
<tr><td>Output</td><td>Scored findings list</td><td>Configuration changes</td><td>Exploit narrative + remediation</td></tr>
<tr><td>Effort</td><td>One day, internal</td><td>Weeks, incremental</td><td>Engagement, external, $10k+</td></tr>
<tr><td>Frequency</td><td>Twice a year</td><td>Continuous</td><td>Annually, or after major change</td></tr>
</table>
<p>An audit is the cheapest of the three and the one that makes the other two possible: you cannot harden what you have not measured, and you should not pay for a pentest until the checklist is mostly green.</p>

<h2>2. The six zones</h2>
<p>Every point below belongs to a zone. The zone framing matters because audits fail when they wander: one person checks "whatever feels risky" and the estate's biggest hole (usually identity) never gets counted. Walk the zones in order &mdash; identity first, because most real breaches start with a credential, not a firewall.</p>
<ol>
<li><strong>Identity &amp; access</strong> &mdash; who can reach what, with what, and since when.</li>
<li><strong>Devices</strong> &mdash; the laptops and phones that hold the data.</li>
<li><strong>Network</strong> &mdash; the perimeter, such as it is in 2026.</li>
<li><strong>Data &amp; backups</strong> &mdash; where the bytes live and whether recovery actually works.</li>
<li><strong>Vendors &amp; SaaS</strong> &mdash; the third parties that hold your data under their names.</li>
<li><strong>Incident readiness</strong> &mdash; what happens in the first hour after something goes wrong.</li>
</ol>

<h2>3. The 45 points</h2>
<p>Each line is pass/fail. The evidence rule is absolute: <strong>screenshot or it did not happen</strong>. A point you "believe" is fine is a finding, not a pass.</p>
<h3>Zone 1 &mdash; Identity &amp; access (10 points)</h3>
<ul>
<li><strong>1.1</strong> MFA is enforced (not optional) on every identity provider &mdash; email, code repos, cloud console, accounting.</li>
<li><strong>1.2</strong> No shared logins for any service; if one exists, it is a finding.</li>
<li><strong>1.3</strong> Admin accounts are separate from daily-use accounts for every human.</li>
<li><strong>1.4</strong> A complete list of who has admin rights exists and was reviewed within 90 days (see the <a href="user-access-review-checklist.html">access review checklist</a>).</li>
<li><strong>1.5</strong> Departed employees and ex-contractors have zero active accounts &mdash; check every leaver from the last 12 months.</li>
<li><strong>1.6</strong> Password manager is deployed to 100% of staff, and zero passwords live in browsers, notes files, or spreadsheets.</li>
<li><strong>1.7</strong> Service accounts and API keys are inventoried, owner-named, and rotated on schedule (the <a href="api-key-rotation-checklist.html">key rotation checklist</a> is the pass bar).</li>
<li><strong>1.8</strong> Break-glass account exists: two emergency credentials in a sealed envelope or vault, tested this year.</li>
<li><strong>1.9</strong> Session timeouts: email and cloud consoles log idle sessions out within a day.</li>
<li><strong>1.10</strong> OAuth grants (apps users connected to company data) were reviewed and pruned this quarter.</li>
</ul>
<h3>Zone 2 &mdash; Devices (7 points)</h3>
<ul>
<li><strong>2.1</strong> Full-disk encryption is on for 100% of laptops (FileVault/BitLocker) &mdash; verify, do not assume.</li>
<li><strong>2.2</strong> Screen locks: 5 minutes or less, password required, on every machine.</li>
<li><strong>2.3</strong> OS auto-updates are on everywhere; no device is more than one major version behind.</li>
<li><strong>2.4</strong> An asset inventory exists and matches reality: every laptop, phone, and NAS is on the list (the <a href="it-asset-inventory-template.html">asset inventory template</a> is the format).</li>
<li><strong>2.5</strong> Lost-device response is defined: remote wipe available and someone is authorized to fire it.</li>
<li><strong>2.6</strong> No company data on personal USB drives; when it must travel, it travels encrypted.</li>
<li><strong>2.7</strong> Default passwords on printers, cameras, and NAS boxes have been changed (printers are computers too &mdash; see the <a href="printer-security-checklist.html">printer checklist</a>).</li>
</ul>
<h3>Zone 3 &mdash; Network (6 points)</h3>
<ul>
<li><strong>3.1</strong> The router/firewall firmware is current and the default admin password is gone.</li>
<li><strong>3.2</strong> Guest WiFi is isolated from the corporate network.</li>
<li><strong>3.3</strong> Inbound port-forwards are inventoried; every one maps to a named reason and an owner.</li>
<li><strong>3.4</strong> Remote access runs through a VPN or an identity-aware proxy &mdash; not exposed RDP/SSH (the <a href="vpn-security-checklist.html">VPN checklist</a> is the bar).</li>
<li><strong>3.5</strong> DNS filtering is on for the office network and, ideally, the laptops themselves (the <a href="dns-filtering-checklist.html">DNS filtering checklist</a>).</li>
<li><strong>3.6</strong> Nothing faces the internet that does not need to: check the cloud consoles for public buckets, open databases, forgotten test servers.</li>
</ul>
<h3>Zone 4 &mdash; Data &amp; backups (8 points)</h3>
<ul>
<li><strong>4.1</strong> A written backup schedule exists and covers: file shares, code repos, cloud SaaS exports, and databases.</li>
<li><strong>4.2</strong> Backups run automatically and their success is monitored (a backup nobody checks is a rumor).</li>
<li><strong>4.3</strong> At least one backup copy is offline or immutable &mdash; ransomware cannot reach it.</li>
<li><strong>4.4</strong> A restore test happened in the last 90 days with real evidence: a file restored, timing noted (the <a href="backup-restore-test-checklist.html">restore test drill</a> is the format).</li>
<li><strong>4.5</strong> The recovery point objective is written down: how much data loss is acceptable, in hours.</li>
<li><strong>4.6</strong> The recovery time objective is written down: how long until the business works again.</li>
<li><strong>4.7</strong> Shared drives follow least-privilege: no "everyone" folder holding payroll or contracts (the <a href="file-share-permissions-audit.html">file share permissions audit</a> finds these).</li>
<li><strong>4.8</strong> Sensitive data is enumerated: where customer PII lives, who can export it, and where it leaves.</li>
</ul>
<h3>Zone 5 &mdash; Vendors &amp; SaaS (8 points)</h3>
<ul>
<li><strong>5.1</strong> A SaaS inventory exists: every tool that holds company or customer data, with its owner (the <a href="saas-sprawl-audit-checklist.html">SaaS sprawl audit</a> finds the unknowns).</li>
<li><strong>5.2</strong> Each vendor holding sensitive data has had a lightweight security review (the <a href="vendor-security-review-checklist.html">vendor security review</a> questions).</li>
<li><strong>5.3</strong> Email authentication is correct: SPF, DKIM, DMARC at enforcement (the <a href="email-deliverability-spf-dkim-dmarc-checklist.html">SPF/DKIM/DMARC checklist</a>).</li>
<li><strong>5.4</strong> Vendor access to your systems is via named accounts, not a shared login someone left in a ticket.</li>
<li><strong>5.5</strong> Offboarding data deletion is written into the key vendor contracts, and at least one departing vendor's data was actually deleted this year (the <a href="vendor-offboarding-data-deletion-checklist.html">vendor offboarding checklist</a>).</li>
<li><strong>5.6</strong> Card payments and invoicing flows have the fraud controls on (the <a href="invoice-fraud-bec-prevention-checklist.html">BEC/invoice fraud checklist</a>).</li>
<li><strong>5.7</strong> Cyber insurance requirements are mapped to reality: every attestation the policy assumes is actually true (the <a href="cyber-insurance-requirements-checklist.html">insurance requirements checklist</a>).</li>
<li><strong>5.8</strong> Shadow IT sweep done this quarter: unmanaged tools found and either adopted or retired (the <a href="shadow-it-audit-checklist.html">shadow IT audit</a> is the sweep).</li>
</ul>
<h3>Zone 6 &mdash; Incident readiness (6 points)</h3>
<ul>
<li><strong>6.1</strong> Someone is named on-call for a security incident, and their out-of-band contact path is tested.</li>
<li><strong>6.2</strong> The first-30-minutes plan exists and has been read by more than one person (start with the free <a href="https://hive80lab.gumroad.com/l/first-30-minutes">First 30 Minutes</a> card).</li>
<li><strong>6.3</strong> A one-page incident response plan exists with severity levels and escalation names (the <a href="incident-response-plan-template-small-teams.html">IR plan template</a>).</li>
<li><strong>6.4</strong> Log retention is decided: what is kept, for how long, and where (the <a href="log-retention-policy-small-teams.html">log retention policy</a>).</li>
<li><strong>6.5</strong> A tabletop exercise ran in the last six months, and its failure points produced at least one fix (see <a href="tabletop-exercise-failure-points.html">the tabletop failure points</a>).</li>
<li><strong>6.6</strong> Ransomware recovery is a written sequence, not a hope (the <a href="ransomware-recovery-checklist.html">ransomware recovery checklist</a>).</li>
</ul>

<h2>4. Running it in one day</h2>
<table>
<tr><th>Time</th><th>Zone</th><th>Notes</th></tr>
<tr><td>09:00&ndash;10:30</td><td>Identity &amp; access</td><td>Needs admin consoles open; pull the leaver list first.</td></tr>
<tr><td>10:45&ndash;12:00</td><td>Devices</td><td>Walk the office; remote staff answer a 7-line form.</td></tr>
<tr><td>13:00&ndash;14:00</td><td>Network</td><td>Router config + cloud console sweep.</td></tr>
<tr><td>14:00&ndash;15:15</td><td>Data &amp; backups</td><td>Do a live single-file restore during the audit &mdash; it is the fastest evidence in the whole exercise.</td></tr>
<tr><td>15:30&ndash;16:30</td><td>Vendors &amp; SaaS</td><td>SaaS inventory export + the vendor questions.</td></tr>
<tr><td>16:30&ndash;17:00</td><td>Incident readiness</td><td>Read the plan aloud; call the on-call phone once.</td></tr>
<tr><td>17:00&ndash;18:00</td><td>Score + report</td><td>Triage findings, write the one-pager (below), set fix dates.</td></tr>
</table>
<p>Two-person version: one person walks the checklist, one runs the consoles. A solo auditor self-deceives twice as fast.</p>

<h2>5. Scoring and the one-page report</h2>
<p>Score every point 0 (fail), 1 (partial), 2 (pass). Zone scores out of 20 give you the shape of the problem; the total out of 90 gives you the trend to beat next audit. But the number that matters is the <strong>critical count</strong>:</p>
<ul>
<li><strong>Critical</strong> = an attacker would use it this month (no MFA on email, working backup never restore-tested, public storage bucket, shared admin login). Fix within 7 days.</li>
<li><strong>High</strong> = attacker would need luck. Fix within 30 days.</li>
<li><strong>Hygiene</strong> = matters at audit time, not at midnight. Batch quarterly.</li>
</ul>
<p>The report is one page, three columns: <em>Finding &rarr; Risk in one sentence &rarr; Fix + date + owner</em>. No vulnerability scores, no essay. The report exists to get fixes scheduled, and the <a href="server-hardening-checklist-small-teams.html">hardening checklist</a> is where the fixes go to die properly &mdash; each finding becomes a line there.</p>

<h2>6. When to bring in an outside pair</h2>
<p>Run the internal audit first &mdash; always. It is cheap, it teaches the team the estate, and it removes the findings you never needed help to see. Outside help earns its fee in exactly two situations:</p>
<ul>
<li><strong>The critical count stays above eight after your own fixes</strong>, or the fixes need sequencing you do not have time to design. That is what a prioritized external audit is for: findings ranked, fix plan attached, five-day turnaround (we run one &mdash; the <a href="https://hive80lab.gumroad.com/l/ljogci">Small-Team Ops Audit</a>, fixed fee, no lock-in).</li>
<li><strong>The fear is incidents, not compliance</strong>: an audit finds gaps, but the artifact a small team actually uses at 2am is a runbook. Where the audit says "incident readiness is the weak zone", a done-for-you incident runbook built from your findings beats a 40-page policy PDF (see the <a href="https://hive80lab.gumroad.com/l/hkljh">Custom Incident Runbook</a>, 48-hour delivery).</li>
</ul>
<p>Everything else on this checklist is deliberately self-serve. The gap between a checklist and an engagement is usually just sequencing.</p>

<h2>7. Five numbers to track after the audit</h2>
<ul>
<li><strong>Criticals open &gt; 7 days:</strong> target zero. This is the only audit number a founder needs to see.</li>
<li><strong>Restore-test success:</strong> last drill passed, with the file name and timing recorded.</li>
<li><strong>MFA coverage:</strong> percentage of human accounts with MFA enforced &mdash; target 100%, no exceptions list.</li>
<li><strong>Leaver-offboarding completeness:</strong> departed staff with zero active accounts, checked against every leaver.</li>
<li><strong>Findings fixed per month:</strong> velocity beats completeness; a shrinking backlog is the trend that matters.</li>
</ul>

<h2>Where this fits</h2>
<p>The audit is the snapshot; the daily work lives in the <a href="patch-management-checklist.html">patch management checklist</a> and the <a href="password-manager-rollout-small-business.html">password manager rollout</a>. The findings feed the <a href="server-hardening-checklist-small-teams.html">hardening checklist</a> and the <a href="file-share-permissions-audit.html">file share permissions audit</a>. When an audit finding is "we would not survive Tuesday", the <a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> is the shortest path from zero to a working incident response &mdash; and the audit's criticals become its first chapter.</p>

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

# --------------------------------------------------- internal-link pre-verify
INT = set(re.findall(r'href="([a-z0-9-]+\.html)"', PAGE))
missing = [h for h in sorted(INT) if not (R / h).exists()]
if missing:
    print("ABORT: internal targets missing on disk:", missing); sys.exit(1)
print(f"internal links pre-verified: {len(INT)} distinct targets, 0 missing")

# --------------------------------------------------- RECIP (verified anchors)
RECIP = {
 "server-hardening-checklist-small-teams.html": (
   '<li><a href="wifi-security-checklist.html">',
   '<li><a href="small-business-security-audit-checklist.html">Small Business Security Audit Checklist</a> &mdash; the 45-point walkthrough that turns these controls into a scored, prioritized report.</li>\n'),
 "mfa-rollout-checklist-small-business.html": (
   '<li><a href="dns-filtering-checklist.html">DNS Filtering Checklist</a></li>',
   '<li><a href="small-business-security-audit-checklist.html">Small Business Security Audit Checklist</a> &mdash; 45 points, six zones, one day, a one-page report.</li>\n'),
 "shadow-it-audit-checklist.html": (
   '<li><a href="vendor-security-review-checklist.html">Vendor Security Review Checklist</a></li>',
   '<li><a href="small-business-security-audit-checklist.html">Small Business Security Audit Checklist</a> &mdash; the whole-estate walkthrough that finds what point-fixes miss.</li>\n'),
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
    p.write_text(t.replace(anchor, block + anchor, 1))
    print(f"recip {fname}: injected")

# --------------------------------------------------- page
(R / (SLUG + ".html")).write_text(PAGE)
print("page written:", SLUG + ".html", len(PAGE), "bytes")

# --------------------------------------------------- sitemap
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

# --------------------------------------------------- index card
CARD = ('<li><a href="small-business-security-audit-checklist.html">Small Business Security Audit Checklist '
 '(The 45-Point Walkthrough)</a><div class="desc">A security audit is a checklist you walk in a day, with '
 'evidence for every line &mdash; not a six-week engagement. Six zones (identity and access, devices, network, '
 'data and backups, vendors and SaaS, incident readiness), 45 pass/fail points, a day-long schedule, the '
 'screenshot-or-it-did-not-happen evidence rule, triage scoring that forces prioritization (criticals fixed in '
 '7 days), the one-page report format, and the two cases where outside help pays for itself &mdash; plus the '
 'five numbers to track after.</div></li>')
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

# --------------------------------------------------- README
rp = R / "README.md"
r = rp.read_text()
line = ('- **NEW: [Small Business Security Audit Checklist (The 45-Point Walkthrough)]'
 '(https://hive80-lab.github.io/ops-notes/small-business-security-audit-checklist.html)** \u2014 an audit is a '
 'checklist you walk in a day, with evidence for every line: six zones, 45 pass/fail points, the '
 'screenshot-or-it-did-not-happen rule, a one-day schedule, triage scoring (criticals fixed within 7 days), '
 'the one-page finding-risk-fix report, and the two cases where an outside pair earns its fee.\n')
if SLUG not in r:
    anchor = r.index("- **NEW:")
    r = r[:anchor] + line + r[anchor:]
    rp.write_text(r)
first_new = [l for l in (R/"README.md").read_text().splitlines() if l.startswith("- **NEW")][0]
print("README top:", first_new[:70])

# --------------------------------------------------- linkcheck
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
