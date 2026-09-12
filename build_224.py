"""Build script for #224 voicemail-greeting-script.html - integrations (idempotent).
Pattern per build_223.py: index TOP card, sitemap newest-first, README line 1,
3 reciprocal backlinks (missed-call-text-back-setup #223, google-business-profile-
optimization-checklist #222, lead-response-time-checklist).
"""
import os
import re
import datetime
import xml.etree.ElementTree as ET

PAGE = 'voicemail-greeting-script.html'
URL = 'https://hive80-lab.github.io/ops-notes/' + PAGE
TODAY = str(datetime.date.today())

# 1) index.html - TOP card (skip if already present)
idx = open('index.html').read()
if PAGE not in idx:
    card = ('<li><a href="' + PAGE + '">Voicemail Greeting Script: The Ten-Minute Recording That Stops '
            'the Beep Losing the Customer</a> &mdash; why six in ten calls that don&rsquo;t connect die at '
            'the beep, the five-line script that keeps the caller on the line (name, back time, what to '
            'leave, the faster path, the urgent path), the four variations every business needs (workday, '
            'closed, busy, holiday), the recording craft that makes a cheap microphone sound trustworthy, '
            'the test call, the four traps (the full mailbox, the comedy greeting, the rebrand that never '
            'got re-recorded, the mailbox nobody checks), the four-minute monthly audit, and the worked '
            'example &mdash; the barbershop whose carrier-default greeting was handing every hung-up call '
            'to the shop next door.</li>')
    anchor = '<ul><li><a href="missed-call-text-back-setup.html">'
    assert anchor in idx, 'index anchor missing'
    idx = idx.replace(anchor, '<ul>' + card + '<li><a href="missed-call-text-back-setup.html">', 1)
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
    entry = ('- **NEW: [Voicemail Greeting Script (The Ten-Minute Recording That Stops the Beep Losing the '
             'Customer)](' + URL + ')** &mdash; why callers hang up on the beep and dial the next listing, '
             'the five-line script that keeps them (who you reached, when someone will listen, what to '
             'leave, the faster path, the urgent path), the four variations every business needs (workday, '
             'closed, busy, holiday/notice), the recording craft (one take standing up, smile on line one, '
             'numbers slowly, name-pronunciation check, re-record when anything changes), the test call, '
             'the four traps (full mailbox, comedy greeting, stale rebrand recording, the mailbox nobody '
             'checks), the four-minute monthly audit, and the worked example &mdash; the two-chair '
             'barbershop whose carrier-default greeting handed every hung-up call to the shop next door.\n')
    open('README.md', 'w').write(entry + readme)

# 4a) backlink in missed-call-text-back-setup (Related paragraph)
t = open('missed-call-text-back-setup.html').read()
if PAGE not in t:
    m = re.search(r'(<p><em>Related:.*)</em></p>', t)
    assert m, 'missed-call related paragraph missing'
    t = t[:m.end(1)] + ('; and when the ring connects but lands on the beep, the '
                        '<a href="' + URL + '">voicemail greeting script</a> is the ten-minute recording '
                        'that keeps the caller on the line instead of the next listing') + t[m.end(1):]
    open('missed-call-text-back-setup.html', 'w').write(t)

# 4b) backlink in google-business-profile-optimization-checklist (Related paragraph)
t = open('google-business-profile-optimization-checklist.html').read()
if PAGE not in t:
    m = re.search(r'(<p><em>Related:.*)</em></p>', t)
    assert m, 'gbp related paragraph missing'
    t = t[:m.end(1)] + ('; and once the profile wins the call, the '
                        '<a href="' + URL + '">voicemail greeting script</a> is what keeps the caller '
                        'through the beep') + t[m.end(1):]
    open('google-business-profile-optimization-checklist.html', 'w').write(t)

# 4c) backlink in lead-response-time-checklist (Related paragraph)
t = open('lead-response-time-checklist.html').read()
if PAGE not in t:
    m = re.search(r'(<p><em>Related:.*)</em></p>', t)
    assert m, 'lead-response related paragraph missing'
    t = t[:m.end(1)] + ('; and the <a href="' + URL + '">voicemail greeting script</a> is the beep-side '
                        'half of the same speed rule &mdash; the mailbox collects, the greeting keeps '
                        'them until it does') + t[m.end(1):]
    open('lead-response-time-checklist.html', 'w').write(t)

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