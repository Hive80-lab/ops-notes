#!/usr/bin/env python3
"""#220 staffing-shortage-coverage-plan.html — integrations (as executed 2026-09-13).
Ran in /Users/haroonqamer/Swarm/hive/state/seo/ops-notes after writing the page.
Committed as 181aa41; fixed 2 pre-existing broken absolute links; sitemap 239 urls."""
import re

# 1) index.html — new TOP card at start of the first ul
idx = open('index.html').read()
card = '<li><a href="staffing-shortage-coverage-plan.html">Staffing Shortage Coverage Plan for Small Businesses: The Call-Out Morning That Doesn&rsquo;t Cancel the Day</a> &mdash; the coverage ladder written in peacetime (first call, second call, and the pre-agreed drop line), the three-list triage (must-run / can-slow / won&rsquo;t-today), the two-sentence call-out reply that replaces the guilt call, the one-job-outside-your-lane cross-training bench, the PTO rule that never leaves a lane empty, the customer line said before it&rsquo;s slow, the pay line that keeps sick people home, the five traps, and the four-chair salon&rsquo;s busiest-Saturday worked example (78% revenue against the zero of a closed morning).</li>'
anchor = '<ul><li><a href="delayed-opening-notice-template.html">'
idx = idx.replace(anchor, '<ul>' + card + '<li><a href="delayed-opening-notice-template.html">', 1)
open('index.html','w').write(idx)

# 2) sitemap.xml — newest-first insert after <urlset...>
sm = open('sitemap.xml').read()
url = '<url><loc>https://hive80-lab.github.io/ops-notes/staffing-shortage-coverage-plan.html</loc><lastmod>2026-09-13</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
m = re.search(r'(<urlset[^>]*>)', sm)
sm = sm[:m.end()] + url + sm[m.end():]
open('sitemap.xml','w').write(sm)

# 3) README.md — new entry on line 1
readme = open('README.md').read()
entry = '- **NEW: [Staffing Shortage Coverage Plan for Small Businesses (The Call-Out Morning That Doesn&rsquo;t Cancel the Day)](https://hive80-lab.github.io/ops-notes/staffing-shortage-coverage-plan.html)** &mdash; the coverage ladder written in peacetime (first call with name and arrangement, second call from the cross-trained bench, the pre-agreed drop line), the three-list triage cut before doors open (must-run protected, can-slow between customers, won&rsquo;t-today said out loud), the two-sentence call-out reply (thanks for telling me early / we&rsquo;ve got it) that replaces the guilt call, the one-job-outside-your-lane quarterly cross-training bench, the PTO rule that never leaves a lane&rsquo;s first and second call away the same week, the one-sentence customer line posted at door + website + Google before opening, the pay line that keeps sick people home (presenteeism costs the busiest week), the five traps (the group-chat scramble, the guilt call-back, open-but-slow, the hero manager, the plan in the owner&rsquo;s head), and the worked example &mdash; a four-chair salon&rsquo;s 6:40am fever text on its busiest Saturday: four of five chairs ran, bookings held 100%, 11 walk-ins converted to Sunday, 78% of full-staff revenue.\n'
open('README.md','w').write(entry + readme)

# 4) reciprocal backlink in the delayed-opening page's Related paragraph
t = open('delayed-opening-notice-template.html').read()
m = re.search(r'(<p><em>Related:.*?</em></p>)', t, re.S)
t = t.replace(m.group(1), m.group(1)[:-len('</em></p>')] + ' And when the shortage is people rather than weather, the <a href="https://hive80-lab.github.io/ops-notes/staffing-shortage-coverage-plan.html">staffing shortage coverage plan</a> runs the call-out morning with a pre-written ladder instead of a group-chat scramble.</em></p>', 1)
open('delayed-opening-notice-template.html','w').write(t)

# 4b) weather-day page
t = open('office-closure-weather-day-checklist.html').read()
m = re.search(r'(<p><em>Related:.*?</em></p>)', t, re.S)
t = t.replace(m.group(1), m.group(1)[:-len('</em></p>')] + ' The <a href="https://hive80-lab.github.io/ops-notes/staffing-shortage-coverage-plan.html">staffing shortage coverage plan</a> covers the third breakage mode: the 5:47am call-out text, handled by a written ladder instead of a scramble.</em></p>', 1)
open('office-closure-weather-day-checklist.html','w').write(t)

# 5) fix 2 pre-existing broken absolute links
def sub(f, old, new):
    t = open(f).read()
    open(f,'w').write(t.replace(old, new))
sub('maintenance-window-announcement-template.html',
    'https://hive80-lab.github.io/ops-notes/status-page-comms-templates.html',
    'https://hive80-lab.github.io/ops-notes/incident-communication-templates.html')
sub('ir-readiness-score.html',
    'https://hive80-lab.github.io/ops-notes/incident-severity-matrix.html',
    'https://hive80-lab.github.io/ops-notes/incident-severity-matrix-template.html')
