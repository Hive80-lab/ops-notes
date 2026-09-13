import re, os
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'supplier-concentration-risk.html'
URL  = 'https://hive80-lab.github.io/ops-notes/supplier-concentration-risk.html'
TODAY = '2026-09-13'

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Supplier Concentration Map &mdash; What Breaks When Your Biggest Vendor Dies</title>
<meta name="description" content="A one-page supplier concentration map for small teams: what each supplier gates, the percent of revenue flowing through it, the time-to-first-damage clock, the 20 percent dual-sourcing gate, and the 30/60/90 exit ramp &mdash; plus the joinery shop whose 78 percent single-source sheet-goods dependency nearly took down two contracted fit-outs.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/supplier-concentration-risk.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>

<h1>The Supplier Concentration Map: What Breaks When Your Biggest Vendor Dies</h1>
<p class="lede">One page, six columns, built from the purchase ledger in an afternoon: what each supplier gates, what share of revenue flows through it, how fast damage arrives when it stops, and the exit ramp you would actually use. The 20 percent gate that turns &ldquo;we should diversify someday&rdquo; into a dated line item, and the nine-person joinery whose 78 percent single-source dependency nearly took two contracted fit-outs down with it.</p>

<p>The <a href="single-point-of-failure-audit-checklist.html">single-point-of-failure audit</a> catches the internal dependencies &mdash; the one server, the one person, the one machine. This page covers the dependencies that audit finds least often because they live on an invoice: the external supplier whose outage is your outage. Concentration risk does not feel like risk while the supplier performs &mdash; every year of smooth delivery is evidence for the argument to do nothing. The map exists so the argument happens with numbers on the table: <strong>78 percent of materials through one distributor, eleven days of packaging stock, four weeks to first damage</strong> reads very differently from &ldquo;we get on well with our suppliers.&rdquo;</p>

<h2>1. The map &mdash; six columns, one table, no more than a page</h2>
<p>Build it from the purchase ledger, not from memory, and rank it by the percentage column:</p>
<ol>
<li><strong>Supplier</strong> &mdash; the legal entity on the invoice, not the sales rep&rsquo;s first name. Distributors and the factories behind them are different rows when they are different risks.</li>
<li><strong>What it gates</strong> &mdash; the thing that stops if this supplier stops: <em>all customer shipping cartons</em>, <em>the only powder-coat line within 300 km</em>, <em>payroll processing</em>. Write the operational thing, not the product category.</li>
<li><strong>Share of spend or revenue through it</strong> &mdash; last twelve months, one number. This is the column that ranks the map.</li>
<li><strong>Time-to-first-damage</strong> &mdash; the honest clock from &ldquo;supplier stops delivering&rdquo; to &ldquo;a customer notices&rdquo;: hours for consumables and packaging, days for standard components, weeks for tooling and exclusive lines. This column decides the order you work in &mdash; not spend, not sentiment.</li>
<li><strong>Second source status</strong> &mdash; one of: <em>qualified</em> (samples passed, price agreed), <em>on paper</em> (name and price known), <em>none</em>. A name in someone&rsquo;s head is &ldquo;none&rdquo; with better handwriting.</li>
<li><strong>Exit ramp</strong> &mdash; the specific first move: <em>merchant 40 minutes south, 3-day lead, +4 percent</em>. If the ramp is &ldquo;find someone,&rdquo; the column is not done.</li>
</ol>

<h2>2. The 20 percent gate &mdash; what the share column obligates you to do</h2>
<ul>
<li><strong>Above 20 percent:</strong> a qualified second source becomes a dated line item this quarter &mdash; owner, deadline, budget for samples. Not an intention; a task with a name on it, tracked in the <a href="weekly-ops-review.html">weekly ops review</a> until it closes.</li>
<li><strong>10 to 20 percent:</strong> a second source on paper &mdash; contact, current price, lead time &mdash; verified twice a year. The check is a phone call, not a feeling.</li>
<li><strong>Under 10 percent:</strong> know the fallback name and the order floor. That is proportionate; over-engineering the tail is its own trap.</li>
</ul>
<p>The gate is deliberately blunt. The failure mode it prevents is not the dramatic bankruptcy &mdash; it is the quiet one: your supplier gets acquired, the new parent consolidates the catalogue, and your line item dies in a pricing email you skimmed on a Friday.</p>

<h2>3. Time-to-first-damage &mdash; the clock that decides the order of work</h2>
<p>Spend follows the damage clock, not the dollar column. Four days of packaging stock means a packaging supplier outage reaches customers in four days &mdash; faster than most incidents get a <a href="incident-response-plan-template-small-teams.html">response plan</a> moving. The practical consequence: the highest-concentration supplier with the shortest clock gets its second source first, even when a bigger-dollar supplier has a longer runway. Worked example below turns on exactly this ordering.</p>

<h2>4. The 30/60/90 exit ramp &mdash; hedging without breaking up</h2>
<ol>
<li><strong>Days 0&ndash;30:</strong> get samples and a written price from the second source. The objective is evidence, not a relationship: can they make the thing, at the spec, on the clock?</li>
<li><strong>Days 31&ndash;60:</strong> move 10 percent of volume. A small real order teaches you more than three samples &mdash; how they package, how they invoice, how they behave when something goes wrong. Run it in parallel; the <a href="vendor-outage-runbook.html">outage runbook</a> should name this source as the live fallback.</li>
<li><strong>Days 61&ndash;90:</strong> make the split the default and write it into the next <a href="vendor-contract-checklist.html">contract renewal</a>. Tell the primary supplier &mdash; plainly: volume will follow reliability and price, and the split is the hedge that keeps both relationships honest.</li>
</ol>
<p>This is not a divorce. It is the purchasing version of the <a href="backup-restore-drill-checklist.html">restore drill</a>: the hedge is worth exactly as much as its last real test, and an untested second source is a hope with a logo.</p>

<h2>The five traps</h2>
<ul>
<li><strong>Building the map from the AP ledger alone.</strong> Spend data misses the exclusive distributor, the sole-licensed software reseller, and the tooling shop nobody else can run. Ask the floor: &ldquo;if this stopped arriving Monday, what stops?&rdquo; The answer list is part of the map even when the invoices are small.</li>
<li><strong>&ldquo;They&rsquo;d never fail us.&rdquo;</strong> Friendship is not capacity, and capacity is not priority. When allocation gets tight, suppliers feed the accounts with contracts and volume &mdash; which is precisely what the 20 percent gate keeps you from being at the mercy of.</li>
<li><strong>Dual-sourcing the cheap stuff.</strong> It is easy and feels like progress. The map ranks by share and damage clock precisely so effort lands on the one exclusive line that gates revenue, not on the third supplier of copy paper.</li>
<li><strong>Paper diversity.</strong> Two suppliers, one upstream factory. If you have not asked where the second source actually manufactures, you have bought the feeling of a hedge without the hedge. One question: <em>where is this made?</em></li>
<li><strong>The map that is never re-run.</strong> Concentration creeps. The savings consolidation program, the reps&rsquo; loyalty pricing, the &ldquo;just this once&rdquo; single-source order that became the default &mdash; rebuild the map every quarter, next to the <a href="vendor-renewal-calendar-template.html">renewal calendar</a>, and the drift never gets a decade to compound.</li>
</ul>

<h2>Worked example &mdash; the joinery with 78 percent of its materials behind one door</h2>
<p>A nine-person commercial joinery shop bought effectively all of its sheet goods &mdash; MDF, ply, veneered board &mdash; through one regional distributor. Not by accident: consolidated volume had earned the best pricing in the region, and four quiet years had made the concentration invisible. Then the distributor&rsquo;s parent company tightened credit terms after a review, the account was frozen for nine business days over a disputed invoice, and lead times on standard board went from four days to twenty-one. Two contracted fit-outs &mdash; $46,000 of signed work &mdash; were scheduled into exactly that window. The joinery found out on a Tuesday, from a delivery driver, not from the supplier.</p>
<p>They spent one afternoon building the map. It ranked four suppliers by share and damage clock: sheet goods at 78 percent share with an eleven-day damage clock (board stores run out first, CNC stops day twelve), hardware at 14 percent with a three-week clock, finish at 6 percent, consumables under 2 percent. The obligation was unambiguous. A timber merchant forty minutes south quoted within two days &mdash; 3-day lead, +4 percent on board, samples cut and passed the same week. The 30/60/90 ramp ran through the next quarter: 10 percent of volume in month one to test the real-world behaviour, 30 percent by the end of month two, and the split written into the annual pricing conversation with both suppliers. Total premium paid for the hedge across the year: about $1,900 &mdash; roughly one fit-out delay fee, never mind two.</p>
<p>The test came eight months later, when the original distributor&rsquo;s own supply chain broke for three weeks &mdash; the same outage that put two of their other customers out of business. The joinery shipped both remaining fit-outs on time, on a 70/30 split nobody had to improvise. The map takes one afternoon a quarter. The alternative path &mdash; the one they were on &mdash; ends with the delivery driver delivering the bad news about your biggest quarter.</p>

<h2>Kits</h2>
<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="single-point-of-failure-audit-checklist.html">single-point-of-failure audit</a> covers the internal dependencies this page&rsquo;s map is the outside half of; the <a href="vendor-outage-runbook.html">vendor outage runbook</a> is the 48-hour playbook for the day a mapped supplier actually stops; the <a href="supplier-payment-terms-checklist.html">payment terms checklist</a> keeps a credit freeze like the joinery&rsquo;s from arriving as a surprise; the <a href="vendor-escalation-ladder.html">vendor escalation ladder</a> is how you escalate before switching; and the <a href="vendor-renewal-calendar-template.html">renewal calendar</a> is where the 30/60/90 split gets written into the next contract.</em></p>

</main>
</body>
</html>
'''

open(PAGE, 'w').write(html)

# 1) index.html - TOP card
card = ('<li><a href="' + PAGE + '">The Supplier Concentration Map: What Breaks When Your Biggest Vendor Dies</a>'
        '<div class="desc">Six columns built from the purchase ledger in an afternoon &mdash; supplier (legal '
        'entity, not the rep), what it gates, share of revenue, time-to-first-damage, second-source status, exit '
        'ramp &mdash; the 20% gate that turns diversify-someday into a dated line item, the damage clock that '
        'decides order of work, the 30/60/90 ramp, and the five traps (AP-ledger blindness, paper diversity, the '
        'map never re-run). Worked example: the nine-person joinery with 78% of materials through one distributor, '
        '$46k of fit-outs scheduled into a nine-day credit freeze, and the $1,900 hedge that shipped both on '
        'time.</div></li>')
idx = open('index.html').read()
if URL not in idx:
    m = re.search(r'(<h1>Ops notes</h1>\s*)(<li><a href="[^"]+\.html">)', idx)
    assert m, 'index anchor missing'
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
    entry = ('- **NEW: [The Supplier Concentration Map: What Breaks When Your Biggest Vendor Dies](' + URL + ')** '
             '&mdash; one page, six columns built from the purchase ledger; the 20% gate (qualified second source '
             'this quarter), the time-to-first-damage clock that decides order of work, the 30/60/90 exit ramp, and '
             'the five traps (AP-ledger blindness, paper diversity, the map never re-run). Worked example: the nine-person '
             'joinery with 78% of materials through one distributor, $46k of fit-outs scheduled into the freeze window, '
             'and the $1,900 hedge that shipped both on time.\\n')
    open('README.md', 'w').write(entry + readme)

def backlink(fname, rel):
    t = open(fname).read()
    if PAGE not in t:
        if '</main>' in t:
            t = t.replace('</main>', rel + '</main>', 1)
        else:
            m = re.search(r'(<footer>)', t); assert m, fname + ' footer missing'
            t = t[:m.start()] + rel + t[m.start():]
        open(fname, 'w').write(t)

# 4) reciprocal backlinks
backlink('single-point-of-failure-audit-checklist.html',
    '<p><em>Related: the SPOF audit catches the internal single points &mdash; the <a href="' + URL + '">supplier '
    'concentration map</a> is its outside half: what breaks when the dependency is on someone else&rsquo;s truck, '
    'ranked by share of revenue and time-to-first-damage.</em></p>\\n')
backlink('vendor-outage-runbook.html',
    '<p><em>Related: the <a href="' + URL + '">supplier concentration map</a> tells you which outage hurts before '
    'it happens; this runbook is the 48-hour playbook for the day one of those mapped suppliers actually stops '
    'delivering.</em></p>\\n')
backlink('supplier-payment-terms-checklist.html',
    '<p><em>Related: the joinery in the <a href="' + URL + '">concentration map</a> learned about its supplier&rsquo;s '
    'credit freeze from a delivery driver &mdash; the terms checklist is how the commercial side of the same '
    'relationship gets watched before it bites.</em></p>\\n')
backlink('vendor-escalation-ladder.html',
    '<p><em>Related: the <a href="' + URL + '">concentration map</a> ranks the dependencies; the escalation ladder '
    'is how you work a failing supplier &mdash; and how you time the switch so the second source is qualified '
    'before you need it, not after.</em></p>\\n')
backlink('vendor-renewal-calendar-template.html',
    '<p><em>Related: the 30/60/90 split from the <a href="' + URL + '">supplier concentration map</a> only holds if '
    'it is written into the next renewal &mdash; this calendar is where the contract dates live so the hedge '
    'becomes the default instead of a memo.</em></p>\\n')

# 5) linkcheck - new page + full repo
page = open(PAGE).read()
hrefs = re.findall(r'href="([^"#]+?\.html)"', page)
missing = [h for h in hrefs if not h.startswith('http') and not os.path.exists(h)]
assert not missing, 'broken relative links on new page: %r' % missing
total_hrefs, total_missing = 0, []
for fn in [f for f in os.listdir('.') if f.endswith('.html')]:
    t = open(fn).read()
    hs = re.findall(r'href="([^"#]+?\.html)"', t)
    total_hrefs += len(hs)
    total_missing += [(fn, h) for h in hs if not h.startswith('http') and not os.path.exists(h)]
assert not total_missing, 'broken: %r' % total_missing[:10]

# 6) sitemap XML validity + summary
import xml.etree.ElementTree as ET
ET.parse('sitemap.xml')
n = open('sitemap.xml').read().count('<url>')
cards = open('index.html').read().count('<li><a href="')
print('OK build_247: sitemap %d urls (XML valid) | index cards %d | linkcheck 0 broken across %d hrefs' % (n, cards, total_hrefs))
