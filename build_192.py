#!/usr/bin/env python3
"""ops-notes page #192 — feature flag cleanup checklist. Canonical repo: mirror."""
import re, sys
from pathlib import Path
from datetime import date
import xml.dom.minidom as minidom

R = Path("/Users/haroonqamer/Swarm/hive/state/seo/ops-notes")
SLUG = "feature-flag-cleanup-checklist"
URL = "https://hive80-lab.github.io/ops-notes/feature-flag-cleanup-checklist.html"
TODAY = date.today().isoformat()

PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Feature Flag Cleanup Checklist (Every Flag Has an Owner and a Kill Date) &mdash; HIVE80lab</title>
<meta name="description" content="A feature flag cleanup checklist that stops flag debt before it ships outages: the three flag classes (release, kill-switch, experiment), the three-field rule (named owner, kill date, removal task filed at 100%), the removal ritual with the off-path drill, the monthly 15-minute sweep with an OWN-or-KILL verdict, and what flags must never gate. Worked example: a 40-person SaaS that found 38 ownerless flags, cut 120 to 63, and turned a 9-day latency incident into a 9-minute mitigation.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/feature-flag-cleanup-checklist.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Feature flag cleanup checklist</h1>
<p><em>Every flag has an owner and a kill date &mdash; or it becomes the outage you shipped in advance.</em></p>
<p>A feature flag starts as safety and decays into debt. Each one is a second code path that only compiles in your head: a branch nobody reads, a config value nobody dares touch, an &ldquo;off&rdquo; state nobody has tested since the quarter it shipped. The flag you forget is not neutral &mdash; it is unvisited risk with a name like <code>checkout_v2_final_REAL</code>, and it will be involved in an incident you could have deleted instead. This page is the cleanup discipline: an inventory, three fields per flag, a removal ritual, and a monthly sweep that fits in fifteen minutes.</p>

<h2>1. Inventory first &mdash; and three classes, not one pile</h2>
<p>You cannot clean up what you have not listed. One sweep produces the inventory: grep the codebase for flag reads, scan config and feature-flag dashboards, and union the results into a single list. Then split it into three classes, because they have different lifetimes:</p>
<ul>
<li><strong>Release flags</strong> &mdash; gate a rollout. They exist to die: at 100% plus a soak period, the flag is removed. Their whole job is to die on schedule.</li>
<li><strong>Ops kill-switches</strong> &mdash; permanent by design, but <em>owned</em>: a named person, a documented off-path, and a drill proving the off-path works. These are the flags you will reach for at 2 a.m.; the <a href="https://hive80-lab.github.io/ops-notes/runaway-automation-runbook.html">runaway automation runbook</a> assumes they flip.</li>
<li><strong>Experiment flags</strong> &mdash; die at the decision date, not when someone remembers. Every experiment flag gets an end date the day it is created, and the decision is logged.</li>
</ul>
<p>A flag missing from the inventory is the dangerous one &mdash; not because it is worse, but because nobody counts it, and uncounted risk is the kind that compounds.</p>

<h2>2. The three-field rule: owner, kill date, removal task</h2>
<p>Every flag in the inventory carries three fields, and a flag missing any one of them is a defect:</p>
<ul>
<li><strong>Owner &mdash; one named person, never a team.</strong> Small-team correction: the engineer who added the flag owns it by default. Teams diffuse; a name on a list does not.</li>
<li><strong>Kill date &mdash; the day this flag is removed or re-reviewed.</strong> Release flags: 100% rollout plus 14 days. Experiments: the decision date. Kill-switches: quarterly review. &ldquo;Temporary&rdquo; with no date is a permanent flag lying about itself.</li>
<li><strong>Removal task &mdash; filed the day the flag hits 100%</strong>, with a ticket ID, into the normal backlog. If removal lives only in someone&rsquo;s memory, it competes with features and loses every sprint.</li>
</ul>
<p>Code review enforces this cheaply: a PR that adds a flag without an owner and a kill date gets one comment &mdash; &ldquo;add the three fields&rdquo; &mdash; and does not merge until they exist. Thirty seconds at merge time deletes an hour of archaeology later.</p>

<h2>3. The removal ritual (and the off-path drill)</h2>
<p>Removal is the step everyone skips, which is how codebases end up carrying 120 flags. The ritual:</p>
<ul>
<li><strong>Trigger:</strong> flag at 100% for 14 days with zero flips and zero incidents &rarr; removal PR goes into the <em>current</em> sprint, not the next one. Removal is not a backlog item; it is the last 10% of shipping the feature.</li>
<li><strong>Delete everything:</strong> the flag read, both code paths&rsquo; dead one, the config entry, the dashboard series, and the tests covering the removed path. Grep for stray reads afterwards &mdash; half-deleted flags are their own incident class.</li>
<li><strong>The off-path drill:</strong> before a flag earns kill-switch status, flip it off in staging and watch what actually happens. A flag whose off-path has never been exercised is not a safety mechanism; it is a rumor. This is the test the forgotten flag fails &mdash; and the reason <a href="https://hive80-lab.github.io/ops-notes/deployment-rollback-checklist.html">rollback drills</a> exist in every serious shop.</li>
<li><strong>Never during a freeze:</strong> flag removal is a code change like any other. It waits out the <a href="https://hive80-lab.github.io/ops-notes/change-freeze-window-policy.html">freeze window</a>, and if the removal rollback would be slow, it belongs in a <a href="https://hive80-lab.github.io/ops-notes/maintenance-window-policy.html">maintenance window</a> instead of a Tuesday afternoon.</li>
</ul>

<h2>4. The monthly 15-minute sweep: OWN or KILL, no third state</h2>
<p>Once a month, fifteen minutes, hard stop. Print the flags older than 90 days whose owner, date, or ticket field has gone stale, and give each one a verdict:</p>
<ul>
<li><strong>OWN</strong> &mdash; still earns its existence: refresh the owner, the kill date, and the removal ticket. A kill-switch that survived review re-earns its place for another quarter.</li>
<li><strong>KILL</strong> &mdash; everything else: file the removal PR before the sweep ends. Not &ldquo;next sprint&rdquo; &mdash; the sweep exists because next-spring never comes.</li>
<li><strong>One escalation rule:</strong> any incident where a forgotten or unowned flag was a cause &mdash; that flag dies <em>this week</em>, and the post-mortem names the flag, its age, and its ownerless duration. Nothing motivates the three-field rule like a flag that caused an outage with no name attached.</li>
</ul>
<p>The sweep is deliberately cheap. Fifteen minutes monthly beats a quarterly &ldquo;flag debt week&rdquo; that gets cancelled twice and then never scheduled again.</p>

<h2>5. What flags must never gate</h2>
<p>Some things are not flag material, no matter how convenient it looks:</p>
<ul>
<li><strong>Pricing and billing logic.</strong> If the flag flips, your invoices change. That is a change-management decision with a paper trail, not a toggle.</li>
<li><strong>Data migrations and one-way doors.</strong> A migration gated by a flag looks reversible and is not. Migrations get the <a href="https://hive80-lab.github.io/ops-notes/database-outage-runbook.html">restore-path treatment</a>, not a boolean.</li>
<li><strong>Anything an auditor must be able to explain.</strong> Flags hide state from audits: &ldquo;which customers saw the old logic?&rdquo; is a question a flag answers badly and a log answers well.</li>
<li><strong>Default-on flags with an untested off-path.</strong> That is not risk mitigation; it is a permanent code path wearing a safety costume.</li>
</ul>

<h2>6. Worked example</h2>
<p>A 40-person SaaS, checkout team. The flag inventory said 120 flags; 38 had no owner, 61 had no kill date, and the median age was 14 months. The motivating incident: a release flag that had gone default-on a year earlier, whose off-path broke silently in a library upgrade &mdash; when a slow memory leak made someone try the switch, it did nothing, and checkout ran with doubled latency for <strong>nine days</strong> before anyone found the flag. One cleanup sprint: 46 flags killed (24 of them dead code paths verified by grep), 11 converted to owned kill-switches with off-path drills, 63 flags total, median age 30 days. Six weeks later a bad deploy hit the same checkout path; the kill-switch flipped in <strong>4 minutes</strong>, and the incident report was one page, not one post-mortem.</p>

<h2>7. Metrics</h2>
<ul>
<li>Flags with a named owner: <strong>100%</strong> &mdash; an ownerless flag is an orphan waiting to page you.</li>
<li>Flags older than 180 days: <strong>zero</strong> &mdash; either it is a documented kill-switch, or it is debt.</li>
<li>Median removal lag after 100% rollout: <strong>&lt; 2 weeks</strong>.</li>
<li>Kill-switch drill: <strong>any flag flippable in &lt; 5 minutes</strong>, off-path verified, staging first.</li>
</ul>

<h2>Where this fits</h2>
<p>Flags sit at the intersection of three siblings: the <a href="https://hive80-lab.github.io/ops-notes/change-freeze-window-policy.html">change freeze window policy</a> decides when flag changes pause entirely; the <a href="https://hive80-lab.github.io/ops-notes/maintenance-window-announcement-template.html">maintenance window announcement</a> is where slow-rollback removals belong; the <a href="https://hive80-lab.github.io/ops-notes/runaway-automation-runbook.html">runaway automation runbook</a> is what your kill-switches exist for. For the rest of the estate &mdash; the flags, the crons, the access nobody remembers granting &mdash; book the <a href="small-team-ops-audit-and-runbook-services.html">small-team ops audit &amp; runbook service</a>.</p>

<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $29</li>
</ul>

<p><em>Related: the <a href="https://hive80-lab.github.io/ops-notes/change-freeze-window-policy.html">change freeze window policy</a> pauses flag changes along with everything else, the <a href="https://hive80-lab.github.io/ops-notes/maintenance-window-announcement-template.html">maintenance window announcement</a> schedules the downtime slow removals need, and the <a href="https://hive80-lab.github.io/ops-notes/runaway-automation-runbook.html">runaway automation runbook</a> is what your kill-switches are for.</em></p>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
'''

# reciprocal backlinks into 3 existing pages
RECIP = {
 "runaway-automation-runbook.html": (
   '<li><a href="cron-job-monitoring-checklist.html">Cron Job Monitoring Checklist (Heartbeats Catch Silent Failures)</a></li>',
   '<li><a href="cron-job-monitoring-checklist.html">Cron Job Monitoring Checklist (Heartbeats Catch Silent Failures)</a></li>\n<li><a href="feature-flag-cleanup-checklist.html">Feature flag cleanup checklist</a> &mdash; every flag has a named owner and a kill date; the off-path drill proves the kill switch flips.</li>\n'),
 "change-freeze-window-policy.html": (
   '</main>',
   '<p class="related">Flags are the freeze&rsquo;s quiet loophole and its quiet debt: a behind-a-flag change can ship during a freeze without users seeing it, and the <a href="feature-flag-cleanup-checklist.html">feature flag cleanup checklist</a> keeps the flag list from becoming its own reason for a freeze.</p>\n</main>'),
 "maintenance-window-announcement-template.html": (
   '</main>',
   '<p class="related">Flag removals are window work when the rollback is slow: the <a href="https://hive80-lab.github.io/ops-notes/feature-flag-cleanup-checklist.html">feature flag cleanup checklist</a> decides which flags survive, and the <a href="https://hive80-lab.github.io/ops-notes/maintenance-window-policy.html">maintenance window policy</a> decides when they are deleted.</p>\n</main>'),
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

CARD = ('<li><a href="feature-flag-cleanup-checklist.html">Feature Flag Cleanup Checklist</a>'
 '<div class="desc">Every flag has an owner and a kill date: the three flag classes (release, kill-switch, '
 'experiment), the three-field rule enforced at merge time, the removal ritual with the off-path drill, the '
 'monthly 15-minute OWN-or-KILL sweep, and what flags must never gate (pricing, migrations, audit paths). '
 'Worked example: 40-person SaaS, 38 ownerless flags, a forgotten flag that doubled checkout latency for 9 '
 'days &mdash; cleanup cut 120 flags to 63 and a repeat incident to a 4-minute mitigation.</div></li>')
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
line = ('- **NEW: [Feature Flag Cleanup Checklist]'
 '(https://hive80-lab.github.io/ops-notes/feature-flag-cleanup-checklist.html)** \u2014 every flag has an owner '
 'and a kill date: the three flag classes, the three-field rule enforced at merge time, the removal ritual with '
 'the off-path drill, the monthly 15-minute OWN-or-KILL sweep, and what flags must never gate. Worked example: '
 '38 ownerless flags, a 9-day doubled-latency incident \u2014 cleanup cut 120 flags to 63 and the repeat to 4 minutes.\n')
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
