import re, os, datetime
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'food-cost-percentage-tracker.html'
URL  = 'https://hive80-lab.github.io/ops-notes/food-cost-percentage-tracker.html'
TODAY = datetime.date.today().isoformat()

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Food Cost Percentage Tracker &mdash; The Friday Count That Tells You Where the Money Actually Goes</title>
<meta name="description" content="A one-page weekly food cost tracker for restaurants and cafes: the only formula on the page (COGS over sales), a ten-minute Friday count by storage area, the theoretical-vs-actual gap that puts a dollar figure on waste, over-portioning and unlogged spoilage, an investigation order that starts with the scale and ends with the door, and the 40-seat restaurant that found $1,850 a month inside a 4.5-point gap.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/food-cost-percentage-tracker.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>The Food Cost Percentage Tracker: The Friday Count That Tells You Where the Money Actually Goes</h1>
<p class="lede">One page, ten minutes, every Friday: beginning inventory, purchases, ending inventory, food sales &mdash; one ratio that tells you whether a busy week made money or just moved it around. Food cost percentage is not paperwork; it is a leak detector. The count does not tell you what to cut. It tells you <em>where to stand</em> when you go looking.</p>

<p>Most independent restaurants run blind on food cost. The POS says sales were great, the bank account says the money never arrived, and the gap between those two facts is eating the business one over-portioned plate at a time. The <a href="food-cost-percentage-tracker.html">tracker on this page</a> closes that gap: a weekly ratio, a theoretical number from the recipes, and an investigation order for the weeks when the two disagree. It is the money-side twin of the <a href="refrigeration-temperature-log.html">refrigeration temperature log</a> &mdash; the log keeps the stock alive, this one keeps the stock profitable.</p>

<h2>1. The only math on the page</h2>
<p><strong>Food Cost % = COGS &divide; Food Sales &times; 100.</strong> That is the entire formula, and every argument about it is really an argument about the two inputs:</p>
<ul>
<li><strong>COGS</strong> = beginning inventory + purchases &minus; ending inventory, all valued at <em>current invoice prices</em> (last cost, not what you paid in March &mdash; you will replace stock at today&rsquo;s price, so today&rsquo;s price is the honest one).</li>
<li><strong>Food sales</strong> = POS food revenue for <em>exactly the same window</em> as the inventory window. A count from Friday to Friday with sales from Sunday to Saturday is not a ratio, it is a coincidence wearing a ratio&rsquo;s clothes.</li>
</ul>
<p>Targets by service style: 25&ndash;30% for fast casual and QSR, 28&ndash;32% for full service, higher if the menu is steak-heavy and lower if it is pasta-heavy &mdash; the number is a directional instrument, not a tax form. What matters is not hitting someone else&rsquo;s number; it is knowing <em>yours</em>, weekly, and noticing the week it moves. A point of food cost on $41,000 of monthly food sales is $410 a month. Four points is the profit.</p>

<h2>2. The sheet &mdash; ten minutes, every Friday</h2>
<p>One count sheet, one row per storage area (walk-in, reach-ins, dry store, freezer), four columns:</p>
<ul>
<li><strong>Beginning value</strong> &mdash; last week&rsquo;s ending value, carried forward. Never recounted; the carry-forward is what makes the weeks comparable.</li>
<li><strong>Purchases</strong> &mdash; the week&rsquo;s food invoices, totaled. This is why the <a href="delivery-receiving-checklist.html">delivery receiving check</a> matters before the math ever starts: a short weight accepted at the door is a leak the count will eventually find, but only after it has been leaking for a week.</li>
<li><strong>Ending value</strong> &mdash; the Friday count. Same areas, same order, same person when possible: a count is a skill, and the person who knows where the backup oil lives counts faster and truer.</li>
<li><strong>Food sales</strong> &mdash; one number off the POS report for the matching seven days.</li>
</ul>
<p>(Beginning + purchases &minus; ending) &divide; sales = this week&rsquo;s percentage. Write it on the sheet next to last week&rsquo;s. The trend line is worth more than any single week &mdash; one bad week is a delivery shortage or a catering write-off; three weeks drifting up is a leak, and the tracker&rsquo;s job is to catch it in week two, not month four.</p>

<h2>3. The gap &mdash; theoretical vs. actual</h2>
<p>The actual percentage from the count answers <em>what food really cost</em>. The theoretical percentage answers <em>what the food should have cost</em>: every recipe&rsquo;s plate cost &times; units sold, summed for the week. Most POS systems or recipe tools can hold the plate costs; if yours cannot, one spreadsheet with the top-twenty sellers covers 80% of the dollars.</p>
<p>The difference between the two &mdash; the gap &mdash; is the entire point of the exercise, because the gap has an address:</p>
<ul>
<li><strong>1&ndash;2 points: normal.</strong> Spoilage, line-cook sampling, rounding, the fries that never made it to the pass. Nobody runs a zero; a zero is usually a counting error, not a miracle.</li>
<li><strong>2&ndash;3 points sustained: a leak forming.</strong> Usually over-portioning that has drifted, or waste that no one is writing down. Worth an investigation week.</li>
<li><strong>3+ points: an emergency by restaurant standards.</strong> At $41k monthly food sales, a 4.5-point gap is $1,845 a month &mdash; call it $22,000 a year bleeding through doors nobody is watching.</li>
</ul>
<p>Notice what the gap does that a single percentage never can: it converts a feeling (&ldquo;food costs seem high&rdquo;) into a dollar figure with a timeframe. That figure is what makes the fix fund itself &mdash; a $30 scale that closes a $620/month portion leak has a payback measured in days, and the tracker is the document that proves it.</p>

<h2>4. The investigation order &mdash; where to stand when the gap is wide</h2>
<ol>
<li><strong>The scale, first, always.</strong> Weigh the top five sellers during a normal service, against spec. Portion drift is the most common cause of a widening gap and the cheapest to fix &mdash; and it is almost never dramatic. An eighth of an ounce over, on the number-one seller, done a thousand times a month, is a line item.</li>
<li><strong>The waste sheet, second.</strong> One page taped above the bin for a week: item, amount, why (overprepped, dropped, returned, expired). Most kitchens discover their real waste rate the first week they measure it &mdash; and overproduction is a forecast problem, not a character problem.</li>
<li><strong>Receiving, third.</strong> Pull the week&rsquo;s invoices against what the <a href="delivery-receiving-checklist.html">receiving check</a> actually caught. Short weights, substitution at the same price, and the invoice paid for what the order said rather than what arrived all land silently in the count.</li>
<li><strong>Comps and voids, fourth.</strong> Unmanaged void codes and comps are food leaving without revenue arriving. If the POS lets anyone void anything, the count inherits every mistake and every favor.</li>
<li><strong>Theft, last &mdash; and expect to be wrong.</strong> Real theft exists, but it is the least common explanation on this list. Standing at the scale with the tracker in hand finds more money in an afternoon than a week of suspecting the staff, and it is the version of the conversation that keeps the team.</li>
</ol>

<h2>5. Worked example &mdash; the 40-seat restaurant&rsquo;s Friday count</h2>
<p>The same 40-seat restaurant that pulled the <a href="refrigeration-temperature-log.html">43&deg;F Tuesday read</a> runs its first tracked month. The Friday count lands at <strong>34.1% actual</strong> against <strong>29.6% theoretical</strong> &mdash; a 4.5-point gap, $1,845 on the month&rsquo;s $41,000 of food sales. The investigation order runs in one week:</p>
<ul>
<li><strong>Scale:</strong> the burger patty weighs 6.4 oz against a 6.0 spec &mdash; the cook who trained everyone portions by eye, generously. 1,900 burgers a month &times; 0.4 oz &asymp; 47.5 lb &asymp; <strong>$620/month</strong>. Fix: one scale at the grill station, one line on the prep list.</li>
<li><strong>Waste sheet:</strong> $710 of spoilage in a week, most of it produce spoiling behind the leaking walk-in door gasket &mdash; the same door the <a href="walk-in-cooler-maintenance-checklist.html">Sunday cooler walk</a> had flagged. Fix: the $45 gasket (work order #0143, already on the shelf from the spare parts list) and a smaller produce par. <strong>&asymp;$700/month recovered.</strong></li>
<li><strong>Comps:</strong> the POS void report shows 62 unapproved voids in the week. Fix: manager code on voids, reviewed in the <a href="weekly-ops-review.html">weekly ops review</a>. <strong>&asymp;$400/month.</strong></li>
</ul>
<p>Six weeks later the tracker reads 30.9% &mdash; not the theoretical 29.6%, and that is fine; the remaining 1.3 points are the honest cost of running a real kitchen. The tracker&rsquo;s job was never zero. Its job was to make the leak visible while it was still a $30 scale problem instead of a $22,000 year.</p>

<h2>5 traps (the ones that make the number lie)</h2>
<ul>
<li><strong>Counting monthly.</strong> A month is four weeks of drift averaged into one number &mdash; by the time the month-end count screams, the leak has a lease. Weekly, ten minutes.</li>
<li><strong>Pricing inventory at old cost.</strong> Valuing stock at what you paid in March while prices moved in August understates COGS and flatters the percentage until the cash is gone. Last invoice price, always.</li>
<li><strong>Mismatched windows.</strong> Inventory Friday-to-Friday with sales Sunday-to-Sunday invents a phantom week. The ratio is only true if both inputs cover the same seven days.</li>
<li><strong>The dead theoretical number.</strong> Plate costs from a menu that changed last spring make every actual look guilty. When the menu changes, twenty minutes of recipe costing &mdash; or the gap means nothing all year.</li>
<li><strong>Worshipping the percentage.</strong> 30% of a $12 salad is $3.60; 28% of a $30 steak is $8.40. Percentages steer; <em>margin dollars</em> pay rent. Track the ratio, decide on the dollars.</li>
</ul>

<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>
<p>Code <strong>HIVE-LAUNCH30</strong> takes 30% off any kit at checkout.</p>

<p><em>Related: the <a href="gross-margin-pricing-review.html">gross margin pricing review</a> is what a stable food cost licenses &mdash; once the ratio is honest, the pricing review decides which plates earn their shelf space; the <a href="price-increase-announcement-template.html">price increase announcement</a> is what you send when the count says inputs moved and the menu has to follow; the <a href="delivery-receiving-checklist.html">delivery receiving checklist</a> is where purchases get verified before they ever reach the count; the <a href="refrigeration-temperature-log.html">refrigeration temperature log</a> is the spoilage half of the same leak &mdash; warm stock is inventory cost you already paid for; the <a href="weekly-ops-review.html">weekly ops review</a> is where the Friday number gets read with the other vital signs instead of dying in a drawer; and the <a href="monthly-close-checklist.html">monthly close checklist</a> is the month-end tie-out that keeps the weekly counts honest against the books.</em></p>
</main>
</body>
</html>
'''
open(PAGE, 'w').write(html)

# 2) index TOP card
idx = open('index.html').read()
assert PAGE not in idx
card = ('<li><a href="' + PAGE + '">The Food Cost Percentage Tracker: The Friday Count That Tells You Where the Money Actually Goes</a>'
        '<div class="desc">One page, ten minutes, every Friday: the only formula on the page (COGS over sales, same seven-day window, current invoice prices), '
        'the count by storage area, the theoretical-vs-actual gap that puts a dollar figure on waste, over-portioning and unlogged spoilage, '
        'and an investigation order that starts with the scale and ends with the door. Worked example: the 40-seat restaurant whose 4.5-point gap '
        '&mdash; $1,845 a month &mdash; broke down into a $620 burger-patty drift, $700 of spoilage behind a leaking gasket and 62 unapproved voids; '
        'six weeks later the tracker reads 30.9% and the fix paid for itself in days.</div></li>')
marker = '<h1>Ops notes</h1>'
assert marker in idx
idx = idx.replace(marker, marker + card, 1)
open('index.html', 'w').write(idx)

# 3) README NEW line (top)
readme = open('README.md').read()
if PAGE not in readme:
    entry = ('- **NEW: [The Food Cost Percentage Tracker: The Friday Count That Tells You Where the Money Actually Goes](' + URL + ')** '
             '&mdash; one page, ten minutes, every Friday: COGS over food sales across the same seven-day window at current invoice prices, '
             'the theoretical-vs-actual gap that turns a feeling into a dollar figure with an address, an investigation order that starts with '
             'the scale (portion drift first, waste sheet, receiving, voids, theft last) and the margin-dollars rule. Worked example: the 40-seat '
             'restaurant&rsquo;s 4.5-point gap &mdash; $620 of burger-patty drift, $700 of spoilage behind a flagged gasket, 62 unapproved voids '
             '&mdash; closed to 1.3 points in six weeks.\\n')
    open('README.md', 'w').write(entry + readme)

# 4) reciprocal backlinks
def backlink(fname, rel):
    t = open(fname).read()
    if PAGE not in t:
        assert '</main>' in t, fname + ' no </main>'
        t = t.replace('</main>', rel + '</main>', 1)
        open(fname, 'w').write(t)

backlink('gross-margin-pricing-review.html',
    '<p><em>Related: the <a href="' + URL + '">food cost percentage tracker</a> is the weekly count that keeps the '
    'gross-margin review honest &mdash; the review decides which plates earn their shelf space, the tracker makes sure the '
    'decisions are running on real numbers.</em></p>\n')
backlink('price-increase-announcement-template.html',
    '<p><em>Related: the <a href="' + URL + '">Friday food cost count</a> is the early warning that inputs moved '
    '&mdash; three weeks of drift is the evidence base for the <a href="price-increase-announcement-template.html">price '
    'increase letter</a>, sent before the margin is gone instead of after.</em></p>\n')
backlink('delivery-receiving-checklist.html',
    '<p><em>Related: purchases verified at the door by the <a href="delivery-receiving-checklist.html">delivery receiving '
    'checklist</a> are what make the <a href="' + URL + '">food cost tracker</a> true &mdash; a short weight accepted '
    'on Tuesday is a mystery in the Friday count.</em></p>\n')
backlink('refrigeration-temperature-log.html',
    '<p><em>Related: the <a href="' + URL + '">food cost tracker</a> prices the spoilage; the <a href='
    '"refrigeration-temperature-log.html">refrigeration temperature log</a> prevents it &mdash; the count finds the '
    '$700 of dead produce, the twice-daily log is why it never dies.</em></p>\n')
backlink('weekly-ops-review.html',
    '<p><em>Related: the <a href="' + URL + '">Friday food cost percentage</a> is one number on the weekly ops '
    'review sheet &mdash; trend line, owner, decision, same as the rest of the vital signs.</em></p>\n')
backlink('monthly-close-checklist.html',
    '<p><em>Related: the <a href="' + URL + '">weekly food cost counts</a> feed the month-end tie-out in the '
    '<a href="monthly-close-checklist.html">monthly close checklist</a> &mdash; four Fridays that agree with the '
    'books is what makes January boring.</em></p>\n')

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

# 6) sitemap insert + XML validity
sm = open('sitemap.xml').read()
if PAGE not in sm:
    entry = ('<url><loc>https://hive80-lab.github.io/ops-notes/' + PAGE + '</loc>'
             '<lastmod>' + TODAY + '</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    sm = sm.replace('</urlset>', entry + '</urlset>', 1)
    open('sitemap.xml', 'w').write(sm)

import xml.etree.ElementTree as ET
ET.parse('sitemap.xml')
n = open('sitemap.xml').read().count('<url>')
cards = open('index.html').read().count('<li><a href="')
print('OK build_255:', PAGE, '| sitemap urls:', n, '| index cards:', cards, '| total hrefs checked:', total_hrefs)
