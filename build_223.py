"""Build script for #223 missed-call-text-back-setup.html - integrations (idempotent).
Pattern per build_222.py: index TOP card, sitemap newest-first, README line 1,
3 reciprocal backlinks (google-business-profile-optimization-checklist #222,
lead-response-time-checklist, staffing-shortage-coverage-plan).
"""
import os
import re
import xml.etree.ElementTree as ET

PAGE = 'missed-call-text-back-setup.html'
URL = 'https://hive80-lab.github.io/ops-notes/' + PAGE
TODAY = '2026-09-23'

# 1) index.html - TOP card (skip if already present)
idx = open('index.html').read()
if PAGE not in idx:
    card = ('<li><a href="' + PAGE + '">Missed Call Text Back Setup: Every Ring You Don\'t Answer Is a Job '
            'Handing Itself to the Next Listing</a> &mdash; why most calls to small businesses ring out and '
            'most callers never call back, the 60-second reply window, the one-time setup in five steps (the '
            'SMS rail you already pay for, the ring-all rule, the templates, the stop rule, the named owner), '
            'the four messages that cover every missed call (closed, busy, after hours, the default), '
            'compliance and manners (stop words, one text not a sequence, name in every message), what to do '
            'with the thread once it starts, the four traps (the stale auto-reply, the number nobody '
            'monitors, the text that answers nothing, the rail that messages people you called), the '
            'four-minute weekly audit, and the worked example &mdash; a two-chair barbershop whose '
            'invisible lunchtime leak was a dozen missed calls a week.</li>')
    anchor = '<ul><li><a href="google-business-profile-optimization-checklist.html">'
    assert anchor in idx, 'index anchor missing'
    idx = idx.replace(anchor, '<ul>' + card + '<li><a href="google-business-profile-optimization-checklist.html">', 1)
    open('index.html', 'w').write(idx)

# 2) sitemap.xml - newest-first insert (skip if already present)
sm = open('sitemap.xml').read()
if URL not in sm:
    url = ('<url><loc>' + URL + '</loc><lastmod>' + TODAY + '</lastmod>'
           '<changefreq>weekly</changefreq><priority>0.8</priority></url>')
    m = re.search(r'(<urlset[^>]*>)', sm)
    sm = sm[:m.end()] + url + sm[m.end():]
    open('sitemap.xml', 'w').write(sm)

# 3) README.md - new entry on line 1 (skip if already present)
readme = open('README.md').read()
if URL not in readme:
    entry = ('- **NEW: [Missed Call Text Back Setup (Every Ring You Don\'t Answer Is a Job Handing Itself to '
             'the Next Listing)](' + URL + ')** &mdash; why most calls to small businesses ring out and most '
             'callers never call back, the 60-second reply window, the one-time setup in five steps (the SMS '
             'rail you already pay for, the ring-all rule, the four templates, the stop rule, the named '
             'owner), the four messages that cover every case (closed, busy, after hours, the default), '
             'compliance and manners (stop words, one text not a sequence, business name in every message), '
             'the thread once it starts (same-day human reply, log the call-back, ring for the urgent ones), '
             'the four traps (the stale auto-reply, the number nobody monitors, the text that answers '
             'nothing, the rail that messages people you called), the four-minute weekly audit, and the '
             'worked example &mdash; a two-chair barbershop whose invisible lunchtime leak was a dozen '
             'missed calls a week.\\n')
    open('README.md', 'w').write(entry + readme)

# 4a) backlink in google-business-profile-optimization-checklist
t = open('google-business-profile-optimization-checklist.html').read()
if PAGE not in t:
    old = ('staffing shortage coverage plan</a> cover the days the doors open differently than the card '
           'says.</em></p>')
    assert old in t, 'GBP related anchor missing'
    new = ('staffing shortage coverage plan</a> cover the days the doors open differently than the card says; '
           'and the <a href="' + URL + '">missed call text back setup</a> catches the rings that beat you '
           'to the phone &mdash; the sixty-second text that saves the customer before they dial the next '
           'card down the list.</em></p>')
    t = t.replace(old, new, 1)
    open('google-business-profile-optimization-checklist.html', 'w').write(t)

# 4b) backlink in lead-response-time-checklist (insert Related paragraph if missing)
t = open('lead-response-time-checklist.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: for the channel that arrives by voice, the <a href="' + URL +
           '">missed call text back setup</a> covers the rings that beat you &mdash; the instant text that '
           'holds the customer while you finish with the one in front of you.</em></p>\n')
    assert '</main>' in t, 'lead-response main close missing'
    t = t.replace('</main>', rel + '</main>', 1)
    open('lead-response-time-checklist.html', 'w').write(t)

# 4c) backlink in staffing-shortage-coverage-plan
t = open('staffing-shortage-coverage-plan.html').read()
if PAGE not in t:
    m = re.search(r'(<p><em>Related:.*)</em></p>\s*</main>', t)
    assert m, 'staffing related paragraph missing'
    t = t[:m.end(1)] + ('; and on the thin days the phone is the first thing that stops getting answered '
                        '&mdash; the <a href="' + URL + '">missed call text back setup</a> is the automatic '
                        'second answerer every roster needs') + t[m.end(1):]
    open('staffing-shortage-coverage-plan.html', 'w').write(t)

# 5) linkcheck - all relative links in the new page resolve
html = open(PAGE).read()
missing = []
for href in re.findall(r'href="([^"#]+\.html)"', html):
    if href.startswith('http'):
        continue
    if not os.path.exists(href):
        missing.append(href)
assert not missing, 'broken relative links: %s' % missing

# 6) sitemap still XML-valid + count
root = ET.fromstring(open('sitemap.xml').read())
print('OK: index card in, sitemap %d urls valid, README updated, 3 backlinks, 0 broken links' % len(root))
