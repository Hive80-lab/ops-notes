import re, os, sys
os.chdir('/private/tmp/ops-notes')
PAGE = 'physical-key-handover-register.html'
URL  = 'https://hive80-lab.github.io/ops-notes/physical-key-handover-register.html'
TODAY = '2026-09-13'
TITLE = 'Physical Key Handover Register: One Row Per Key, and the Rules That Keep the Back Door Accountable'

# 1) index.html - TOP card
card = ('<li><a href="' + PAGE + '">Physical Key Handover Register: One Row Per Key, '
        'and the Rules That Keep the Back Door Accountable</a>'
        '<div class="desc">The register that replaces key folklore with a table: one row per key '
        '(etched ID, never the door name), issue and return as two separate events with signatures '
        'and received-by initials; the five rules (whoever issues records, masters never leave the '
        'building, departures close rows before goodbyes close doors, a lost key is a lock-change '
        'event, copies are issued not improvised); fobs and alarm codes on the same law (a collected '
        'fob still opens the door until the system deactivates it); the traps (the drawer of unknown '
        'keys, the master on the daily ring, the row edited instead of appended); and the quarterly '
        'five-minute cabinet count. Worked example: two sites, one lost cleaner key &mdash; $180 and '
        'one morning versus a full weekend rekey and no answers.</div></li>')
idx = open('index.html').read()
if PAGE not in idx:
    m = re.search(r'(<h1>Ops notes</h1>\s*)(<li><a href="[^"]+\.html">)', idx)
    assert m, 'index anchor missing (first card li after h1)'
    idx = idx[:m.start(2)] + card + idx[m.start(2):]
    open('index.html', 'w').write(idx)

# 2) sitemap.xml - newest-first insert
sm = open('sitemap.xml').read()
if URL not in sm:
    url = ('<url><loc>' + URL + '</loc><lastmod>' + TODAY + '</lastmod>'
           '<changefreq>weekly</changefreq><priority>0.8</priority></url>')
    m = re.search(r'(<urlset[^>]*>)', sm)
    assert m, 'urlset missing'
    sm = sm[:m.end()] + url + sm[m.end():]
    open('sitemap.xml', 'w').write(sm)

# 3) README.md - new entry on line 1
readme = open('README.md').read()
if URL not in readme:
    entry = ('- **NEW: [Physical Key Handover Register (One Row Per Key, and the Rules That Keep '
             'the Back Door Accountable)](' + URL + ')** &mdash; the register that replaces key '
             'folklore with a table (one row per key, etched IDs, issue and return as two separate '
             'signed events), the five rules (whoever issues records, masters never leave the '
             'building, departures close rows before goodbyes close doors, a lost key is a '
             'lock-change event, copies are issued not improvised), fobs and alarm codes on the '
             'same law, the traps (the drawer of unknown keys, the master on the daily ring, the '
             'row edited instead of appended), and the quarterly five-minute cabinet count. '
             'Worked example: two sites, one lost cleaner key &mdash; $180 and one morning versus '
             'a weekend rekey with no answers.\\n')
    open('README.md', 'w').write(entry + readme)

# 4a) backlink: key-inventory-register (the what-exists sibling -> who-holds-it)
t = open('key-inventory-register.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: the inventory says what keys and locks exist; the '
           '<a href="' + URL + '">physical key handover register</a> says who holds each one '
           'right now &mdash; issue and return as two signed events, with the quarterly '
           'cabinet count that keeps the drawer of unknown keys from ever forming.</em></p>\n')
    if '</main>' in t:
        t = t.replace('</main>', rel + '</main>', 1)
    else:
        m = re.search(r'(<footer>)', t); assert m, 'key-inventory footer missing'
        t = t[:m.start()] + rel + t[m.start():]
    open('key-inventory-register.html', 'w').write(t)

# 4b) backlink: employee-offboarding-checklist
t = open('employee-offboarding-checklist.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: the physical side of the same exit &mdash; the '
           '<a href="' + URL + '">key handover register</a> makes key return a signed row that '
           'closes before the last pay is confirmed, so no departing colleague is a permanent '
           'uncontrolled copy of the building.</em></p>\n')
    if '</main>' in t:
        t = t.replace('</main>', rel + '</main>', 1)
    else:
        m = re.search(r'(<footer>)', t); assert m, 'offboarding footer missing'
        t = t[:m.start()] + rel + t[m.start():]
    open('employee-offboarding-checklist.html', 'w').write(t)

# 4c) backlink: badge-access-control-checklist
t = open('badge-access-control-checklist.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: fobs follow the <a href="' + URL + '">key handover register</a> law '
           'too &mdash; a collected fob still opens the door until the system deactivates it, so '
           'the row and the deactivation confirm together.</em></p>\n')
    if '</main>' in t:
        t = t.replace('</main>', rel + '</main>', 1)
    else:
        m = re.search(r'(<footer>)', t); assert m, 'badge footer missing'
        t = t[:m.start()] + rel + t[m.start():]
    open('badge-access-control-checklist.html', 'w').write(t)

# 5) linkcheck: every relative href in the new page must exist on disk
page = open(PAGE).read()
missing = [h for h in re.findall(r'href="([a-z0-9-]+\.html)"', page)
           if not os.path.exists(h)]
assert not missing, 'broken relative links: %r' % missing

# 6) summary
n = open('sitemap.xml').read().count('<url>')
cards = open('index.html').read().count('<li><a href="')
print('OK build_231: sitemap urls=%d, index cards~%d, page %d bytes, 0 coupon=%s'
      % (n, cards, os.path.getsize(PAGE),
         'HIVE20' not in open(PAGE).read()))
