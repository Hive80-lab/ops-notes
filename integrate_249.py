#!/usr/bin/env python3
# ops-notes #249 integrations: sitemap, index top card, README NEW, 5 reciprocal backlinks, linkcheck
import re, os, glob

D = '/Users/haroonqamer/Swarm/hive/state/seo/ops-notes/'
URL = 'https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html'
DATE = '2026-09-24'
NEW = 'equipment-downtime-log.html'
ok = []

# 1) sitemap: prepend new url (newest-first), anchor at first <url>
s = open(D+'sitemap.xml').read()
if NEW not in s:
    entry = f'<url><loc>{URL}</loc><lastmod>{DATE}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
    i = s.index('<url>')
    s = s[:i] + entry + s[i:]
    open(D+'sitemap.xml','w').write(s)
n = len(re.findall(r'<url>', open(D+'sitemap.xml').read()))
ok.append(f'sitemap urls={n}')

# 2) index.html: insert new top card after <h1>Ops notes</h1>
h = open(D+'index.html').read()
if NEW not in h:
    new_card = ('<li><a href="equipment-downtime-log.html">The Equipment Downtime Log: The Ledger That Turns Breakdowns Into a Maintenance Budget</a>'
'<div class="desc">Seven columns per breakdown, written the hour the machine comes back &mdash; machine, both downtime clocks (lost production and wrench time), the failure mode in plain words, the fix and its part, the cost, who fixed it, and the preventable line that pays for the page. The Friday triage turns preventable events into maintenance tasks and repeat offenders into queue-jumpers; the monthly roll-up finds the 80/20 machines and the repair-or-replace threshold; the annual lemon walk reads the trend. Worked example: the 40-seat restaurant whose six Q1 stops ($7,300 in lost revenue) were mostly one walk-in cooler killed by a torn $45 door gasket &mdash; Q2: one event, 2.5 hours, and a combi oven moved onto the capital list with a date instead of a panic quote.</div></li>')
    i = h.index('<h1>Ops notes</h1>')
    j = h.index('<li>', i)
    h = h[:j] + new_card + h[j:]
    open(D+'index.html','w').write(h)
    ok.append('index top card added')
else:
    ok.append('index: already')

# 3) README: prepend NEW line
r = open(D+'README.md').read()
if NEW not in r:
    new_line = ('- **NEW: [The Equipment Downtime Log: The Ledger That Turns Breakdowns Into a Maintenance Budget]('+URL+')** &mdash; '
'seven columns per breakdown recorded the hour it ends (machine, both downtime clocks, failure mode, fix, cost, who fixed it, preventable Y/N + one line); '
'the Friday triage that feeds the maintenance schedule, the monthly roll-up that prices lost production and finds the 80/20 machines, '
'the repair-or-replace third-of-replacement threshold, and the annual lemon list. Worked example: the 40-seat restaurant whose $45 walk-in door gasket '
'killed four repeat compressor failures &mdash; Q1 six events/$7,300 lost revenue to Q2 one event/2.5 hours, plus a combi oven onto the capital list.\n')
    open(D+'README.md','w').write(new_line + r)
    ok.append('README NEW prepended')
else:
    ok.append('README: already')

# 4) reciprocal backlinks x5 via Related-line injection
def append_related(path, sentence):
    t = open(D+path).read()
    if NEW in t:
        return path + ': already'
    lines = t.split('\n')
    for k, ln in enumerate(lines):
        if '<p><em>Related' in ln:
            if '</em></p>' in ln:
                lines[k] = ln.replace('</em></p>', sentence + '</em></p>', 1)
                open(D+path,'w').write('\n'.join(lines))
                return path + ': linked'
            else:
                return path + ': NO </em></p> on related line'
    return path + ': no related line'

ok.append(append_related('preventive-maintenance-schedule-template.html',
 ' the <a href="equipment-downtime-log.html">equipment downtime log</a> is where the schedule&rsquo;s frequencies come from &mdash; its Friday triage turns every preventable event into next month&rsquo;s scheduled hour.'))
ok.append(append_related('critical-spare-parts-list.html',
 ' the <a href="equipment-downtime-log.html">equipment downtime log</a> is the evidence the list is built on &mdash; every part that ended a stop is a candidate for the shelf.'))
ok.append(append_related('uptime-downtime-budget.html',
 ' the <a href="equipment-downtime-log.html">equipment downtime log</a> is where the budget lands &mdash; the per-machine ledger that shows where the allowed downtime actually went.'))
ok.append(append_related('cold-chain-failure-checklist.html',
 ' the <a href="equipment-downtime-log.html">equipment downtime log</a> is where the event goes after the doors shut &mdash; duration, cost, and the one line about what would have caught it.'))
ok.append(append_related('generator-transfer-checklist.html',
 ' the <a href="equipment-downtime-log.html">equipment downtime log</a> takes the transfer as its next line &mdash; started, ended, what broke, what it cost, preventable next time.'))

# 5) linkcheck: every local href/src target must exist
broken = []
total = 0
for f in glob.glob(D+'*.html'):
    t = open(f).read()
    for href in re.findall(r'(?:href|src)="([^"]+)"', t):
        if href.startswith(('http', 'mailto:', '#', 'data:')):
            continue
        total += 1
        target = href.split('#')[0]
        if target and not os.path.exists(D+target):
            broken.append(os.path.basename(f) + ' -> ' + href)
ok.append(f'linkcheck local hrefs={total} broken={len(broken)}')
for b in broken[:10]:
    ok.append('  BROKEN: ' + b)

print('\n'.join(ok))
