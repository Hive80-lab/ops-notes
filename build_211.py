#!/usr/bin/env python3
"""ops-notes unit #211: penetration-test scope template."""
import re, sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
BASE = "https://hive80-lab.github.io/ops-notes/"
SLUG = "penetration-test-scope-template.html"
TODAY = date.today().isoformat()

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Penetration Test Scope for Small Teams (The Test That Scanned the Wrong Server) &mdash; HIVE80lab Ops Notes</title>
<meta name="description" content="A penetration test scope template for small teams: one page, nine boxes (in-scope targets, out-of-scope, test window with blackout dates, allowed methods, stop conditions, contacts tree, test-account handling, deliverables, retest), rules of engagement signed by both sides, and a fix sprint booked before kickoff. Turns a pentest from an expensive PDF into evidence a deal can close on.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/penetration-test-scope-template.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>Penetration Test Scope for Small Teams</h1>
<p class="lede">A penetration test without a written scope is an invoice with admin rights. The tester decides what gets touched, when, and how hard &mdash; and you find out from an on-call page. Small teams buy pentests rarely and expensively, which is exactly why the scope matters more for them: there is no second test to fix a bad first one. A penetration test scope is not legal boilerplate. It is <strong>one page that decides what evidence you are buying</strong> &mdash; which systems may be attacked, in which window, with what methods, and what everyone does the moment something breaks. Get the page right and the test produces findings you can fix and a report that closes deals; skip it and you have bought a PDF and a story about the night the tester rate-limited your payment provider.</p>

<h2>The one page, written before you shop</h2>
<ol>
<li><strong>Write the three-line intent before contacting any vendor.</strong> Why now (an enterprise security questionnaire, a compliance checkbox, a gut feeling after the last <a href="security-audit-scorecard.html">security audit</a>), what decision the report must support, and who actually reads it. This matters because vendors price and shape the test around it: a questionnaire-answer test is a broad-but-shallow scan plus verification; a pre-deal diligence test is targeted at the systems the customer will inspect. A pentest bought without a named decision becomes a PDF that gets forwarded once and never opened.</li>
<li><strong>One page, nine boxes.</strong> (1) <em>In scope</em> &mdash; exact environments, domains, IPs, repos; say plainly whether prod is in, and if it is, why staging cannot answer the question instead. (2) <em>Out of scope</em> &mdash; payroll, staff laptops, third-party SaaS you do not own. (3) <em>Test window</em> &mdash; dates and hours, plus blackout dates (payroll week, the big launch). (4) <em>Allowed methods</em> &mdash; external web and API testing yes; social engineering of staff only if you consciously agree, in writing, because it tests your people, not your systems. (5) <em>Intensity limits</em> &mdash; no destructive testing, rate caps on authenticated requests, no exfiltrating more data than a proof. (6) <em>Stop conditions</em> &mdash; any customer-data exposure, any data corruption, any on-call page: stop and call, in that order. (7) <em>Contacts tree</em> &mdash; tester &rarr; engagement owner &rarr; on-call engineer &rarr; escalation, with phone numbers, not email. (8) <em>Credentials</em> &mdash; how test accounts get made, where their secrets live, when they expire. (9) <em>Deliverables</em> &mdash; report format, severity scheme, and whether a retest is included or priced separately. Nine boxes is one hour of typing and it is the whole contract.</li>
<li><strong>Rules of engagement, signed by both sides.</strong> The page above is not complete until both parties sign it and it answers the mid-test questions: what happens when the tester finds something serious on day two (an immediate-disclosure channel, not save-it-for-the-report), what happens when you deploy during the window (freeze the in-scope services or notify the tester in channel), and who can call stop. The stop conditions matter more than the start date &mdash; they are what your on-call reads at 2am when test traffic pages, and they point to the same first move as <a href="first-30-minutes-checklist.html">the first 30 minutes</a>: stabilize first, resume later.</li>
<li><strong>You build the guardrails, not the tester.</strong> Dedicated test accounts with capped permissions, a labeled user-agent or source range you can filter for later, and rate limits on the test account itself. Two reasons: your logs stay readable (test traffic is findable and excludeable after the fact, which the <a href="log-retention-policy-template.html">log retention policy</a> should record), and the blast radius of a mistake stays inside accounts built to be hurt. A tester using a founder's real account is a finding about you, not them.</li>
<li><strong>Book the fix sprint before kickoff.</strong> A two-week test gets a two-week fix sprint already on the calendar, owned by whoever owns the code. Findings without scheduled fix time rot into next year's report &mdash; the same finding reappearing in consecutive tests is the tell, and it means the process failed, not the test. The severity scheme from the report feeds straight into the <a href="bug-triage-process-template.html">bug triage process</a>: every finding needs an owner and a date, or it was entertainment.</li>
<li><strong>The retest is half the purchase.</strong> Fixes verified by the same tester within a bounded window (30 days is normal) is what lets you write &ldquo;penetration tested, findings remediated and retested&rdquo; on the customer questionnaire with a straight face. Without the retest you are certifying fixes you never verified &mdash; the pentest version of marking your own homework. Price it at signing; retrofitting a retest later costs more and happens never.</li>
</ol>

<h2>Five traps</h2>
<ul>
<li><strong>The scope the tester writes for you.</strong> The engagement letter arrives with scope already filled in and you sign it because reading it is work. Conflict of interest is structural: the tester's scope covers what is easy to test. You write the nine boxes; you cut what does not serve the named decision; they negotiate. A scope you did not edit is a scope you did not buy.</li>
<li><strong>Scanning production because &ldquo;staging isn't the same.&rdquo;</strong> True and irrelevant &mdash; the answer is a prod window with hours, rate caps, and stop conditions, not an unbounded scan of prod during business hours. The tell that you got this wrong is your payment provider rate-limiting you mid-test while your on-call debugs an outage only the tester knows is a test.</li>
<li><strong>The PDF that lands and dies.</strong> Report arrives, gets forwarded to the channel, gets one &ldquo;nice&rdquo; and zero owners. Sixty days later the same finding is in the new test. The fix is calendar, not culture: fix sprint booked at signing, every finding entering the <a href="post-incident-action-item-tracker.html">action item tracker</a> with a name and a date.</li>
<li><strong>Buying the report, not the retest.</strong> The cheapest part of a pentest is the second look at the fixes. Skipping it means the questionnaire answer &ldquo;remediated&rdquo; is your word, not evidence &mdash; and enterprise buyers increasingly ask for the retest letter, not the report summary.</li>
<li><strong>Compliance theater with a stale in-scope list.</strong> Last year's scope, this year's infrastructure: the new API, the second region, the vendor SSO integration are all outside a boundary written before they existed. The scope is refreshed every engagement against the current <a href="asset-inventory-checklist.html">asset inventory</a>, and cadence follows change volume, not the calendar &mdash; a year of no changes buys a year of grace, a quarter of shipping buys a quarter of testing.</li>
</ul>

<h2>Worked example</h2>
<p>A seven-person B2B SaaS closing its first enterprise customer. The old way: a $9,000 broker pentest, engagement letter signed unread; the tester scanned production during business hours because staging &ldquo;wasn't representative&rdquo;; the payment provider rate-limited the test traffic mid-afternoon, the on-call engineer spent three hours debugging an outage nobody could reproduce, the tester abandoned the remaining tests, and the report landed six weeks later &mdash; forwarded once, no fix sprint, no retest. The enterprise deal stalled anyway: the buyer's questionnaire asked whether findings were retested, and the honest answer was no.</p>
<p>The rerun, next attempt: one-page scope written by the team in an hour and edited by the vendor in a day. In scope: the staging environment and the production API, in a declared window (Tue&ndash;Thu, 9&ndash;17, never during payroll week), with rate caps on the test account and labeled test traffic. Stop conditions in the on-call runbook. Fix sprint booked before kickoff; retest included at signing. Test ran clean, report in ten days: three highs, five mediums. Highs fixed in nine days, retest verified eleven days after the report. The questionnaire's pentest row was answered with the report and the retest letter, and the deal closed the following week. Same $9,000 &mdash; the difference was one page written first.</p>

<h2>Metrics (for the testing program itself)</h2>
<ul>
<li>100% of pentests with a signed one-page scope before kickoff. One test without one is the error budget spent; two is policy.</li>
<li>Findings fixed within the pre-booked fix window. Under ~90% means the fix sprint is fiction and the report is a shelf document.</li>
<li>Retest verification rate: share of findings verified fixed by the tester, not claimed fixed. This is the number that answers customer questionnaires.</li>
<li>Median days from report to first fix merged. Over two weeks means findings and the calendar never met.</li>
<li>Repeat-finding rate across consecutive tests: the same class of finding reappearing is a process gap (the <a href="blameless-post-incident-review-template.html">blameless review</a> asks why the class survived, not who missed it).</li>
</ul>

<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="https://hive80-lab.github.io/ops-notes/vendor-security-review-checklist.html">vendor security review checklist</a> is the questionnaire the pentest report answers; the <a href="https://hive80-lab.github.io/ops-notes/security-audit-preparation-checklist.html">security audit preparation checklist</a> is where the scope and the last report are standing inputs; the <a href="https://hive80-lab.github.io/ops-notes/api-key-leak-response-runbook.html">API key leak runbook</a> is what the on-call runs when test traffic turns out to be something worse; and the <a href="https://hive80-lab.github.io/ops-notes/incident-response-drill-schedule-template.html">incident drill schedule</a> keeps the stop-conditions muscle warm between tests.</em></p>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
"""

def main():
    root = ROOT
    page = root / SLUG
    if page.exists():
        print("ABORT: page exists:", SLUG); sys.exit(1)
    page.write_text(PAGE, encoding="utf-8")
    print("page written:", SLUG, len(PAGE), "bytes")

    # --- sitemap: insert at TOP (newest-first) ---
    sm = root / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    entry = ("<url><loc>" + BASE + SLUG + "</loc><lastmod>" + TODAY +
             "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    marker = 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    assert marker in s, "sitemap marker missing"
    s = s.replace(marker, marker + entry, 1)
    sm.write_text(s, encoding="utf-8")
    print("sitemap url inserted at TOP; total urls:", s.count("<url>"))

    # --- index: insert card before current TOP card ---
    ix = root / "index.html"
    t = ix.read_text(encoding="utf-8")
    card = ('<li><a href="' + SLUG + '">Penetration Test Scope for Small Teams: The Test That Scanned the Wrong Server</a>'
            '<div class="desc">A pentest without a written scope is an invoice with admin rights &mdash; the tester decides what gets touched and you find out from an on-call page. One page, nine boxes: in-scope environments, out-of-scope, a window with blackout dates, allowed methods, intensity limits, stop conditions, a contacts tree with phone numbers, test-account handling, deliverables plus a retest. Rules of engagement signed by both sides, guardrails you build (test accounts, labeled traffic, rate caps), the fix sprint booked before kickoff, and the retest priced at signing instead of never. The five traps (the scope the tester writes for you, unbounded prod scans, the PDF that lands and dies, buying the report not the retest, stale in-scope lists) and the seven-person SaaS whose $9,000 test rate-limited its own payment provider &mdash; then closed an enterprise deal on the rerun, same budget, one page written first.</div></li>')
    anchor = '<li><a href="software-license-register-template.html">'
    assert anchor in t, "index anchor missing"
    t = t.replace(anchor, card + anchor, 1)
    ix.write_text(t, encoding="utf-8")
    print("index card inserted at TOP")

    # --- README: NEW line at top ---
    rd = root / "README.md"
    r = rd.read_text(encoding="utf-8")
    line = ('- **NEW: [Penetration Test Scope for Small Teams (The Test That Scanned the Wrong Server)]('
            + BASE + SLUG + ')** &mdash; a pentest without a written scope is an invoice with admin rights; one page, nine boxes '
            '(in-scope, out-of-scope, window with blackout dates, allowed methods, intensity limits, stop conditions, contacts tree, '
            'test accounts, deliverables + retest), rules of engagement signed by both sides, guardrails you build, fix sprint booked '
            'before kickoff; the five traps (the tester-written scope, unbounded prod scans, the PDF that lands and dies, report '
            'without retest, stale in-scope lists); worked example: $9,000 test rate-limited its own payment provider mid-scan, rerun '
            'same budget with a one-page scope closed the enterprise deal the first one stalled.\n')
    rd.write_text(line + r, encoding="utf-8")
    print("README NEW line added at top")

    # --- reciprocal backlinks x3 ---
    def add_related(fname, sentence):
        p = root / fname
        t = p.read_text(encoding="utf-8")
        if SLUG in t:
            print("backlink already present:", fname); return
        anchor2 = '<p><em>Related:'
        if anchor2 in t:
            idx = t.rfind('</em></p>')
            t = t[:idx] + sentence + t[idx:]
        else:
            idx = t.rfind('</main>')
            t = t[:idx] + '<p><em>Related: ' + sentence.strip() + '</em></p>\n' + t[idx:]
        p.write_text(t, encoding="utf-8")
        print("backlink added:", fname)

    add_related("vendor-security-review-checklist.html",
                'the <a href="' + BASE + SLUG + '">penetration test scope</a> is the evidence that answers this checklist\'s hardest rows &mdash; tested, remediated, retested.')
    add_related("security-audit-preparation-checklist.html",
                'the <a href="' + BASE + SLUG + '">penetration test scope</a> is one of the standing inputs the audit gathers &mdash; a scoped test with a retest letter beats a shelf PDF.')
    add_related("api-key-leak-response-runbook.html",
                'the <a href="' + BASE + SLUG + '">penetration test scope</a> stop conditions are what the on-call reads when test traffic pages &mdash; and what tells them it is not a leak.')

    # --- linkcheck: every relative href exists ---
    broken = []
    total = 0
    for f in root.glob("*.html"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'href="([^"#]+?\.html[^"]*)"', t):
            href = m.group(1)
            if href.startswith("http"):
                continue
            path = href.split("#")[0].split("?")[0]
            if not path:
                continue
            total += 1
            if not (root / path).exists():
                broken.append((f.name, path))
    print("linkcheck: relative html hrefs:", total, "broken:", len(broken))
    for b in broken[:10]:
        print("  BROKEN:", b)

    # --- sitemap XML well-formedness ---
    import xml.dom.minidom as md
    md.parseString(sm.read_text(encoding="utf-8"))
    print("sitemap XML valid")

if __name__ == "__main__":
    main()
