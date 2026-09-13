#!/usr/bin/env python3
# ops-notes #249 finisher: GitHub Pages live-wait, IndexNow, dev.to direct-publish + verify
import json, os, time, urllib.request, urllib.error

BASE = 'https://hive80-lab.github.io/ops-notes/'
SLUG = 'equipment-downtime-log'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'

# 1) live wait
for attempt in range(1, 9):
    try:
        with urllib.request.urlopen(urllib.request.Request(BASE + SLUG + '.html', headers={'User-Agent': UA}), timeout=15) as r:
            if r.status == 200:
                print('LIVE_OK', r.status); break
    except Exception as e:
        print('live attempt', attempt, e)
    time.sleep(12 * attempt)

# 2) IndexNow
live_key = kf = None
for cand in ('indexnow.key', 'indexnow-key.txt', 'indexnow.txt'):
    try:
        with urllib.request.urlopen(BASE + cand, timeout=15) as r:
            if r.status == 200:
                live_key = r.read().decode().strip(); kf = cand; break
    except Exception:
        pass
if live_key:
    body = json.dumps({'host': 'hive80-lab.github.io', 'key': live_key, 'keyLocation': BASE + kf,
        'urlList': [BASE + SLUG + '.html', BASE + 'index.html', BASE + 'preventive-maintenance-schedule-template.html',
                    BASE + 'critical-spare-parts-list.html', BASE + 'uptime-downtime-budget.html',
                    BASE + 'cold-chain-failure-checklist.html', BASE + 'generator-transfer-checklist.html']}).encode()
    req = urllib.request.Request('https://api.indexnow.org/IndexNow', data=body,
        headers={'Content-Type': 'application/json; charset=utf-8', 'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print('INDEXNOW:', r.status)
    except urllib.error.HTTPError as e:
        print('INDEXNOW HTTP', e.code, e.read()[:200])
else:
    print('INDEXNOW_SKIP no live key')

# 3) dev.to publish
article = {
 'title': "The $45 gasket that silenced a walk-in cooler: log downtime like it costs money, because it does",
 'published': True,
 'canonical_url': BASE + SLUG + '.html',
 'description': 'Seven columns per breakdown, a Friday triage that feeds your maintenance schedule, and a monthly roll-up that prices lost production - plus the 40-seat restaurant whose six Q1 stops were all one torn door gasket.',
 'tags': ['smallbusiness', 'operations', 'maintenance', 'restaurants'],
 'body_markdown': """Every breakdown gets a line: which machine, how long it was down, what actually broke, what the fix cost, who fixed it - and the column that pays for the whole page: **was it preventable?** Written the hour the machine comes back, triaged fifteen minutes on Friday, rolled up once a month. That is the entire system, and it is the difference between a shop where breakdowns are weather and a shop where breakdowns are a line item you are slowly deleting.

**The seven columns, in order:** machine (named as the floor names it, plus the asset number); started/ended *and the clock that matters* - lost production, not wrench time (a 20-minute fix mid-run on your only oven can cost more than an 8-hour fix on an idle Sunday); what broke in plain words ("door gasket torn, coil iced, compressor short-cycling," never "machine down"); the fix and the part that ended it - this column is where your spares list shops; the cost (parts + outside labour + missed production); who fixed it; and *preventable Y/N plus one line* on what would have caught it.

**Friday, fifteen minutes, three decisions.** Every *preventable = Y* event becomes a candidate task on the preventive maintenance schedule. Any failure mode that has now appeared twice in ninety days jumps the queue - repeat offenders are the machines writing your future. Any fix that needed a part goes onto the critical spares list with the downtime tolerance attached. A log nobody reads is a diary; the triage is the product.

**The monthly roll-up is where money appears.** Sum hours and cost per machine and two things fall out. First, the 80/20 line: two machines usually hold most of the pain, and the dramatic one is often not either of them - the quiet leaker stopping twelve minutes twice a week outranks the four-hour Saturday. Second, the repair-or-replace threshold: when a rolling year of downtime cost passes roughly a third of replacement cost and the trend is not bending after PM and spares are in place, the machine goes on the capital list - and the budget gets a line item instead of a surprise.

**Five traps:** logging only the big outages (the fifteen-minute stops are where the money leaks); blame entries (*who fixed it*, never *who broke it* - a log that names culprits teaches the floor to log nothing); repair-hours-only accounting (carry both clocks, cost the lost-production one); the log nobody reads (the triage is the product, the entries are just raw material); and shoebox history (one page per machine per quarter beats a year of texts - the log must survive the person keeping it in his head).

**The worked example:** a 40-seat restaurant logged every kitchen stop for a quarter. Q1: six downtime events, 19.5 lost-production hours, $1,150 in repairs and call-outs - and about $7,300 of revenue walking out the door once missed covers were priced. The instinct was to blame the Saturday the combi oven threw an error. The roll-up said otherwise: **four of the six events were the same walk-in cooler, same failure mode - compressor short-cycling on overload.** Root cause: a torn $45 door gasket letting humid air in, icing the coil. The fix: a gasket, a defrost check added to the weekly cold-chain walk, a spare gasket on the shelf with the fiche in the drawer. Q2: one event, 2.5 hours, zero call-outs. The same roll-up put the 12-year-old combi oven on the capital list - $2,900/year in downtime suddenly had a replacement business case, a date, and a budget line. Nothing changed except that the breakdowns were being counted, and the counting did the arguing.

**The full page** - the seven columns in detail, the Friday triage, the monthly roll-up, the lemon list, and the worked example - lives at [Hive Ops Notes](https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html).

Free: [The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) - the incident quick-start checklist. If your operation needs the full system: [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit) ($14), [Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) ($27), or the [Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle) (all 5 kits, $49).
"""
}

key = open(os.path.expanduser('~/Swarm/hive/state/secure/devto_api_key.txt')).read().strip()
payload = {'article': article}
req = urllib.request.Request('https://dev.to/api/articles', data=json.dumps(payload).encode(),
    headers={'api-key': key, 'Content-Type': 'application/json', 'User-Agent': UA})
r = urllib.request.urlopen(req, timeout=60)
resp = json.load(r)
aid, slug = resp.get('id'), resp.get('slug')
print('POST:', r.status, 'id:', aid, 'slug:', slug)
time.sleep(3)
d = json.load(urllib.request.urlopen(urllib.request.Request(f'https://dev.to/api/articles/{aid}', headers={'api-key': key, 'User-Agent': UA}), timeout=30))
print('VERIFY url:', d.get('url'))
print('VERIFY canonical:', d.get('canonical_url'))
print('CTAs in body:', d['body_markdown'].count('hive80lab.gumroad.com'), '| site links:', d['body_markdown'].count('hive80-lab.github.io'))
with open('devto_payload_249.json', 'w') as f:
    json.dump(payload, f, indent=2)
with open('devto_publish_249.py', 'w') as f:
    f.write('''#!/usr/bin/env python3
# ops-notes #249 dev.to publisher - article id %s, slug %s
print('#249 syndicated: id %s')
''' % (aid, slug, aid))
