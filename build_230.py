"""Build script for #230 delivery-receiving-checklist.html - integrations (idempotent).
Pattern per build_224.py: index TOP card, sitemap newest-first, README line 1,
3 reciprocal backlinks (cold-chain-failure #228, monthly-close, vendor-escalation-ladder).
Anchor is derived dynamically (parallel sessions keep changing the TOP card).
"""
import os
import re
import datetime
import xml.etree.ElementTree as ET

PAGE = 'delivery-receiving-checklist.html'
URL = 'https://hive80-lab.github.io/ops-notes/' + PAGE
TODAY = str(datetime.date.today())

# 1) index.html - TOP card, dynamic anchor
card = ('<li><a href="delivery-receiving-checklist.html">Delivery Receiving Checklist: '
        'The Two Minutes at the Door That Decide Who Pays for What\'s Wrong</a>'
        '<div class="desc">The five-step receiving ritual before the pen touches the docket: '
        'count cartons against the order (not the invoice), cold check in product not air, '
        'open-and-verify the lines that walk, condition and date row, discrepancies written on '
        'the docket and countersigned; the rules that turn a discrepancy into a credit note '
        '(quarantine don\'t shelve, verbal credits don\'t exist, unordered goods are a question); '
        'the four traps (rubber-stamp signature, shelve first count later, the friendly '
        'supplier\'s word, the swallowed discrepancy); and the weekly five-minute audit. '
        'Worked example: two cafes, the same roaster, one forty-second docket note worth '
        'three weeks of arguments.</div></li>')
idx = open('index.html').read()
if PAGE not in idx:
    m = re.search(r'(<h1>Ops notes</h1>\s*)(<li><a href="[^"]+\.html">)', idx)
    assert m, 'index anchor missing (first card li after h1)'
    idx = idx[:m.end(2)] and idx[:m.start(2)] + card + idx[m.start(2):]
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
    entry = ('- **NEW: [Delivery Receiving Checklist (The Two Minutes at the Door That Decide '
             'Who Pays for What\'s Wrong)](' + URL + ')** &mdash; the five-step receiving ritual '
             'before signing (count cartons against the PO, cold check in product, open-and-verify '
             'the short-shippable lines, condition and dates, discrepancies on the docket with a '
             'driver countersign), the rules (whoever signs counts, quarantine don\'t shelve, '
             'verbal credits don\'t exist, unordered goods are a question, the docket feeds the '
             'close), the weekly five-minute audit, and the four traps. Worked example: two '
             'cafes, the same roaster, and a forty-second docket note that saved a three-week '
             'argument.\\n')
    open('README.md', 'w').write(entry + readme)

# 4a) backlink in cold-chain-failure-checklist (Related paragraph)
t = open('cold-chain-failure-checklist.html').read()
if PAGE not in t:
    m = re.search(r'(<p><em>Related:.*)</em></p>', t)
    assert m, 'cold-chain related paragraph missing'
    t = t[:m.end(1)] + ('; and the <a href="' + URL + '">delivery receiving checklist</a> is '
                        'where the temperature question gets asked &mdash; at the door, in '
                        'product, while the driver is still standing there') + t[m.end(1):]
    open('cold-chain-failure-checklist.html', 'w').write(t)

# 4b) backlink in monthly-close-checklist (Related paragraph insert)
t = open('monthly-close-checklist.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: the <a href="' + URL + '">delivery receiving checklist</a> is where '
           'invoice-vs-goods mismatches are born &mdash; a docket annotated at the door is the '
           'close\'s cheapest reconciling item.</em></p>\n')
    assert '</main>' in t, 'monthly-close main close missing'
    t = t.replace('</main>', rel + '</main>', 1)
    open('monthly-close-checklist.html', 'w').write(t)

# 4c) backlink in vendor-escalation-ladder (Related paragraph insert)
t = open('vendor-escalation-ladder.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: the <a href="' + URL + '">delivery receiving checklist</a> is the '
           'front door of the same discipline &mdash; most escalations never happen when the '
           'discrepancy was written on the docket before the driver left.</em></p>\n')
    assert '</main>' in t, 'vendor-escalation main close missing'
    t = t.replace('</main>', rel + '</main>', 1)
    open('vendor-escalation-ladder.html', 'w').write(t)

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
count = len(root.findall('{*}url'))
print('sitemap urls:', count)
print('linkcheck: OK - 0 broken relative links in', PAGE)
assert count >= 249, 'sitemap count unexpected'
print('ALL INTEGRATIONS OK (#230)')
