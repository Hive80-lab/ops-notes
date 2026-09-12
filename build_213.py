#!/usr/bin/env python3
"""ops-notes unit #213: data breach notification checklist."""
import re, sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
BASE = "https://hive80-lab.github.io/ops-notes/"
SLUG = "data-breach-notification-checklist.html"
TODAY = date.today().isoformat()

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Data Breach Notification for Small Teams (The 72 Hours You Spend Deciding Who to Tell) &mdash; HIVE80lab Ops Notes</title>
<meta name="description" content="A data breach notification checklist for small teams: the notification map drawn in peacetime (regulator, customers, partners, insurer, counsel, PSP, employees), what every notice contains, the five traps (waiting for perfect facts, one letter for everyone, silent log edits, telling customers before insurer, one-and-done notices), and the parallel-track rule &mdash; notification is a legal clock, not a writing assignment.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/data-breach-notification-checklist.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<h1>Data breach notification for small teams &mdash; the 72 hours you spend deciding who to tell</h1>
<p>A breach has two clocks running at once: the fix clock and the notification clock. Teams are built for the first and improvise the second &mdash; so the engineers contain the incident while the founders draft letters, and the letters go out late, wrong, or to the wrong audiences. Notification is not writing. It is a <strong>map with names and clocks on it, drawn in peacetime</strong>: who must hear what, within how many hours, from which owner, in which order. Regulators count from awareness, not from certainty; contracts often beat the law; and a notification record done right becomes evidence &mdash; in the next deal's questionnaire, the insurer's file, and the customer's trust.</p>

<h2>The notification map, drawn before you need it</h2>
<ol>
<li><strong>Regulators and supervisory authorities.</strong> GDPR: notify within 72 hours of awareness unless the breach is unlikely to risk rights and freedoms; record every breach anyway (the 72-hour clock starts at awareness, and &ldquo;we were still investigating&rdquo; is not an extension). US state breach laws: thresholds, formats, and AG-notice rules vary by state of residency &mdash; the map names which states your customers live in today. If you serve EU customers without an EU establishment, the lead-supervisory-authority question gets answered now, not during the incident.</li>
<li><strong>Affected customers and users.</strong> Named owner, template, and channel chosen in peacetime (email plus a status page update beats a blog post nobody reads). The notice says what they should <em>do</em>, not just what happened.</li>
<li><strong>Partners and processors, both directions.</strong> Downstream: your vendors whose data or systems touched the breach (contract clocks are often 24&ndash;48 hours and start on <em>your</em> awareness). Upstream: customers whose contract promises notification on their timetable &mdash; usually shorter than the law's. This row is why the <a href="vendor-security-review-checklist.html">vendor security review</a> asks for incident-notification terms before signing.</li>
<li><strong>Cyber insurer and counsel &mdash; before any external word.</strong> Policies routinely require prompt notice and approved counsel; the customer letter sent before the carrier is looped in can void coverage. This is the first call, not the last.</li>
<li><strong>Banks and payment providers.</strong> If card or payment data may be touched, the PSP and acquiring bank have their own clocks and their own idea of &ldquo;prompt.&rdquo;</li>
<li><strong>Employees &mdash; with a line to hold.</strong> Everyone gets one paragraph: what is public, what is not, and that all external questions route to one named spokesperson. The well-meaning engineer's LinkedIn thread is a second incident.</li>
<li><strong>Status page and support macros.</strong> The public single source of truth, updated on a stated cadence, with support armed to link it instead of improvising.</li>
<li><strong>The notification log.</strong> One row per notice: audience, owner, channel, sent-at, letter version. This log is the artifact every future questionnaire, audit, and insurer call asks for (the <a href="security-questionnaire-answer-bank.html">answer bank</a> keeps the freshest answers one folder away).</li>
</ol>

<h2>What every notification contains</h2>
<ul>
<li><strong>What happened, in plain language.</strong> No topology, no CVEs, no internal codenames &mdash; answer the control, not the architecture (the same rule the answer bank uses).</li>
<li><strong>What data and when.</strong> Categories (not dumps), the window it was accessible, and honest uncertainty marked as uncertainty with a date it will be resolved.</li>
<li><strong>What you have done and what they should do.</strong> The reader's next action first: rotate this, watch that, call this number.</li>
<li><strong>How to reach a human</strong> and <strong>when the next update lands.</strong> A dated next-update commitment converts &ldquo;we'll keep you posted&rdquo; into something you can be held to &mdash; which is the point.</li>
</ul>

<h2>The five traps</h2>
<ul>
<li><strong>Waiting for perfect facts.</strong> The clock does not pause for the investigation to finish. Notice what you know when you know it; the second letter (&ldquo;what we now know&rdquo;) is normal and expected &mdash; the missing first letter is what regulators fine and customers remember.</li>
<li><strong>One letter for everyone.</strong> The regulator needs facts and timelines, the customer needs actions, the partner needs contract-language, the insurer needs the incident narrative. Four audiences, four documents from one fact base &mdash; never one text forwarded four times.</li>
<li><strong>Editing the logs.</strong> The instinct to &ldquo;tidy up&rdquo; the audit trail before sharing turns an incident into spoliation. Preserve everything, write down what you changed and why, and let the <a href="blameless-post-incident-review-template.html">blameless review</a> sort causes later.</li>
<li><strong>Customers before insurer and counsel.</strong> Empathy says tell everyone immediately; the policy says the carrier approves the words. Empathy loses the coverage; the carrier approves the words.</li>
<li><strong>Notification as one-and-done.</strong> The first letter is the contract; the updates are the product. A breach handled with weekly dated updates ends with more trust than the quiet quarters before it &mdash; a breach with one letter and silence ends with churn you cannot measure until renewal.</li>
</ul>

<h2>Worked example</h2>
<p>A twelve-person B2B SaaS. A contractor's reused password led to a support mailbox containing exports for ~400 customer records. Detection to severity call: 40 minutes (the <a href="incident-severity-matrix-template.html">severity matrix</a> rated it P1 &mdash; customer data, external access). Hour 6: counsel and the cyber carrier engaged, words pending approval. Hour 41: regulator notice filed with the facts then known, marked as preliminary. Day 2: customer notice sent &mdash; what happened, what categories of data, the window, the rotations required, a named contact, and a dated next update; partners notified inside their 48-hour contract lane the same morning; status page carried the public version, support armed with one macro. Weekly dated updates until closure, five in total; the final one carried the <a href="after-action-report-template.html">after-action</a> summary and the fixes (mailbox rule changes, contractor offboarding wired into the <a href="employee-offboarding-checklist.html">offboarding checklist</a>, a <a href="user-access-review-checklist.html">quarterly access review</a>).</p>
<p>The cost: two accounts churned. The return: three months later a procurement security review asked &ldquo;describe your breach-notification process with evidence&rdquo; &mdash; the answer was the log, the letters, and the timeline, pasted in ten minutes. The deal closed. The difference between an incident and a liability is usually not the breach; it is whether the notification map existed before the attacker did.</p>

<h2>Metrics (for the notification program itself)</h2>
<ul>
<li>Time from detection to severity call (target: under one hour &mdash; the clock starts here, and it is the only number fully in your control).</li>
<li>Time from awareness to regulator notice where required (median, and 100% inside the legal window; near-misses logged as process gaps, not luck).</li>
<li>Notification log completeness: 100% of notices have an audience, an owner, a channel, a timestamp, and a version.</li>
<li>Next-update commitment met rate: 100% &mdash; a missed dated update costs more trust than the breach itself.</li>
<li>Contract-notification adherence: zero partners learning about your incident from the news or from their own logs.</li>
</ul>

<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="https://hive80-lab.github.io/ops-notes/incident-severity-matrix-template.html">incident severity matrix</a> is what decides when the notification clocks start; the <a href="https://hive80-lab.github.io/ops-notes/ransomware-recovery-checklist.html">ransomware recovery checklist</a> runs in parallel &mdash; fix and notify are two tracks with one command; the <a href="https://hive80-lab.github.io/ops-notes/phishing-response-checklist-small-teams.html">phishing response checklist</a> is the runbook for the credential-theft breaches behind most notifications; and the <a href="https://hive80-lab.github.io/ops-notes/security-questionnaire-answer-bank.html">security questionnaire answer bank</a> is where the notification log and letters live as evidence for the next deal.</em></p>
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
    card = ('<li><a href="' + SLUG + '">Data Breach Notification for Small Teams: The 72 Hours You Spend Deciding Who to Tell</a>'
            '<div class="desc">A breach runs two clocks at once &mdash; the fix clock and the notification clock &mdash; and teams are built for the first. The notification map, drawn in peacetime: regulators (GDPR 72 hours from awareness, state laws by residency), affected customers, partners with contract clocks shorter than the law, insurer and counsel before any external word, banks and PSPs, one-paragraph employee lines, a status page on a stated cadence, and a notification log with one row per notice. What every notice contains (plain language, categories not dumps, the reader\'s next action first, a dated next update). The five traps (waiting for perfect facts, one letter for everyone, editing the logs, customers before the carrier, one-and-done notices) and the twelve-person SaaS whose breach log and letters closed a procurement review three months later.</div></li>')
    anchor = '<li><a href="security-questionnaire-answer-bank.html">'
    assert anchor in t, "index anchor missing"
    t = t.replace(anchor, card + anchor, 1)
    ix.write_text(t, encoding="utf-8")
    print("index card inserted at TOP")

    # --- README: NEW line at top ---
    rd = root / "README.md"
    r = rd.read_text(encoding="utf-8")
    line = ('- **NEW: [Data Breach Notification for Small Teams (The 72 Hours You Spend Deciding Who to Tell)]('
            + BASE + SLUG + ')** &mdash; a breach runs two clocks, the fix clock and the notification clock; the notification map drawn in '
            'peacetime (regulator 72h from awareness, customers, partners with contract clocks, insurer+counsel first, PSPs, employee lines, '
            'status page, notification log), what every notice contains (plain language, categories not dumps, the reader\'s next action first, '
            'dated next update), the five traps (waiting for perfect facts, one letter for everyone, log edits, customers before the carrier, '
            'one-and-done notices); worked example: 12-person SaaS, P1 at 40 minutes, regulator at 41h, letters day 2, five dated updates &mdash; '
            'and the log closed a procurement review three months later.\\n')
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

    add_related("incident-severity-matrix-template.html",
                'the <a href="' + BASE + SLUG + '">data breach notification checklist</a> is what a P1 hands off &mdash; the severity call starts the clocks, the map says who they belong to.')
    add_related("ransomware-recovery-checklist.html",
                'the <a href="' + BASE + SLUG + '">data breach notification checklist</a> runs in parallel with recovery &mdash; fix and notify are two tracks under one commander.')
    add_related("after-action-report-template.html",
                'the <a href="' + BASE + SLUG + '">data breach notification checklist</a> decides what may be shared externally; the after-action report decides what was learned internally.')

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
    import xml.dom.minidom
    xml.dom.minidom.parseString(sm.read_text(encoding="utf-8"))
    print("sitemap XML valid")

if __name__ == "__main__":
    main()
