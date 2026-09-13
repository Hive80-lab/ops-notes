import re, os, datetime
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'restaurant-inventory-par-levels.html'
URL  = 'https://hive80-lab.github.io/ops-notes/restaurant-inventory-par-levels.html'
TODAY = datetime.date.today().isoformat()

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Par Level &amp; Ordering Guide &mdash; The Sheet That Turns Friday's Count Into Monday's Order</title>
<meta name="description" content="A one-page par level and ordering guide for restaurants and cafes: the only formula on the page (par = daily usage times delivery days plus one safety day, minus what is on the shelf), a Friday count that rides along with the food cost count, case-size rounding that respects the vendor's boxes, safety stock sized to delivery-day reality, and the 40-seat restaurant that freed $2,300 of dead freezer stock and stopped the Tuesday 4pm scramble.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/restaurant-inventory-par-levels.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>The Par Level &amp; Ordering Guide: The Sheet That Turns Friday's Count Into Monday's Order</h1>
<p class="lede">One page, one formula, one Friday walk: what you use in a day, how many days until the truck comes, one day of safety stock, minus what is actually on the shelf &mdash; that is the order. Par levels are not purchasing sophistication; they are the difference between ordering from a number and ordering from a feeling. The feeling buys $900 of skirt steak "just in case" and runs out of romaine on a Saturday.</p>

<p>The <a href="food-cost-percentage-tracker.html">food cost percentage tracker</a> counts what you have and prices what you lost. This page is the sheet that acts on it: for every item you carry, a number that says <em>order to here</em>. The two sheets share one Friday walk &mdash; the same storage areas, the same scale, twenty minutes total &mdash; because a count that only produces a percentage is a report, and a count that also produces a purchase list is an operating system. It is the demand-side twin of the <a href="delivery-receiving-checklist.html">delivery receiving checklist</a>: the receiving check keeps the vendor honest at the door, the par sheet keeps your own judgment honest at the order screen.</p>

<h2>1. The only math on the page</h2>
<p><strong>Par = (weekly usage &divide; 7) &times; (days between deliveries + 1 safety day) &minus; on-hand.</strong> Round to case size. That is the entire formula, and every argument about it is an argument about four honest inputs:</p>
<ul>
<li><strong>Weekly usage</strong> &mdash; from the purchase invoices and the Friday count, not from memory. The invoices already total it for the <a href="food-cost-percentage-tracker.html">food cost sheet</a>; reuse the same number.</li>
<li><strong>Delivery cycle</strong> &mdash; the real days between drops, not the contract days. The vendor who says "Tuesday and Friday" and delivers "Tuesday and most Fridays" has a three-day cycle some weeks.</li>
<li><strong>One safety day</strong> &mdash; sized to delivery-day reality: a missed truck on a holiday weekend is not a math error, it is a calendar fact. Items you can buy retail locally can run a thinner safety line than items only your vendor carries.</li>
<li><strong>On-hand</strong> &mdash; the Friday count, valued later for the food cost sheet but counted first for this one. Same shelf walk, two columns.</li>
</ul>
<p>Case-size rounding is not waste, it is the vendor's language: a par of 27 lb when the ground beef ships in 20 lb cases means you order 40 and bank the surplus in next week's count. What you never round is the <em>decision</em> &mdash; 27 lb of need met with a 20 lb case is a smaller produce par or a mid-week top-up, written on the sheet, not a shrug.</p>

<h2>2. The sheet &mdash; one row per item, one walk per week</h2>
<p>One sheet, one row per stock item, seven columns:</p>
<ul>
<li><strong>Item &amp; unit</strong> &mdash; the vendor's unit (case, bag, each), not the kitchen's unit. The order goes to the vendor; the math has to speak their language.</li>
<li><strong>Weekly usage</strong> &mdash; rolling three-week average from invoices, because one catering week will lie to you for a month.</li>
<li><strong>Lead/cycle days</strong> &mdash; actual, per vendor, written where the driver's phone number lives.</li>
<li><strong>Par</strong> &mdash; the formula's answer, in case-size language.</li>
<li><strong>On-hand</strong> &mdash; Friday's count for this row.</li>
<li><strong>Order</strong> &mdash; par minus on-hand, rounded to case size, zero if negative. A row that reads zero two weeks running is telling you the par is too fat &mdash; cut it before the money does.</li>
<li><strong>Par check</strong> &mdash; a one-word note the week the row surprises you: "salad special," "heat wave," "menu test." Three surprises in a quarter is a par change, not a coincidence.</li>
</ul>
<p>Sequence matters: count first, order second, price third. The <a href="walk-in-cooler-maintenance-checklist.html">Sunday cooler walk</a> keeps the box honest, the <a href="refrigeration-temperature-log.html">temperature log</a> keeps the stock alive &mdash; the par sheet assumes both, and puts its own order only against stock that will still be stock on Monday.</p>

<h2>3. The rhythm &mdash; and the audit that pays for the whole page</h2>
<p>The weekly loop: Friday count &rarr; order sheet &rarr; Monday deliveries checked at the door &rarr; invoices into the <a href="food-cost-percentage-tracker.html">purchases column</a> &rarr; repeat. Once a quarter, run the par audit that makes the page famous: list every item with its inventory value and how many weeks of usage the shelf holds. Anything holding more than three weeks of usage is dead money wearing a uniform. Freezer proteins are the usual suspects &mdash; bought for a special that ended, too heavy to carry again, too visible to throw away.</p>
<p>The audit's output is not a spreadsheet; it is a decision per row: run it as a special, cut the par, or let it ride because the vendor's minimum forces it. Par is a living number &mdash; seasonal menus move it, a new fryer moves it, the street festival outside moves it. The sheet's <em>par check</em> column is how the number learns without a consultant.</p>

<h2>Worked example &mdash; the 40-seat restaurant</h2>
<p>Week 32, same restaurant as the <a href="food-cost-percentage-tracker.html">food cost tracker</a> (the one with the 34.1% week and the $45 gasket). The first par audit finds <strong>$2,300 of dead stock</strong>: lamb shoulder for a winter special nobody ordered since July, a case of hearts of palm from one forgotten catering bid, and six bags of the premium bun the menu switched away from. The quarter's par cuts and case-size fixes:</p>
<ul>
<li><strong>Ground beef:</strong> usage 190 lb/week, Tuesday-Friday deliveries, par 81 lb &rarr; ordered 4&times;20 lb cases with a standing mid-week top-up. The burger-patty drift from the tracker's example gets a second fix here: the <a href="delivery-receiving-checklist.html">door check</a> weighs one random patty per delivery.</li>
<li><strong>Romaine:</strong> the Saturday 86 list (sold out by 7pm twice in a month) traced to a three-day cycle written as two. Safety day added, par 24 &rarr; 30 cases-of-6. The 86 disappears; the <a href="weekly-ops-review.html">weekly ops review</a> records the fix.</li>
<li><strong>Produce par cut 15%</strong> behind the repaired walk-in gasket &mdash; the spoilage fix from the tracker's example, now permanent in the math instead of remembered in a story.</li>
</ul>
<p>Net effect: roughly $2,300 freed on day one, about $180 a week of carrying cost and 86s gone, and an order screen that takes eleven minutes because every row already knows its answer. The par sheet did not buy smarter; it stopped buying stupider &mdash; which is where most food businesses keep their margins.</p>

<h2>5 traps (the ones that make the sheet lie)</h2>
<ul>
<li><strong>Set once, never revisited.</strong> A par from opening month is a fossil. The par check column exists so the number learns from the weeks it was wrong.</li>
<li><strong>Ordering by feel.</strong> "We were busy Saturday" is a story; 190 lb is a number. Feel orders double when the rep visits, halves when cash is tight, and is never right in between.</li>
<li><strong>Ignoring case sizes.</strong> A par in kitchen units ordering in vendor units rounds every week into drift. Write the par in the unit you order in.</li>
<li><strong>Safety stock sized by fear.</strong> One day is a cushion; five days is a second walk-in you pay rent on. Safety is for the missed truck, not for the missed sale you are nostalgic about.</li>
<li><strong>Letting the vendor set the par.</strong> The supplier's delivery minimum is their number, not yours. Their case pack, their lead times &mdash; those are inputs. The par is yours.</li>
</ul>

<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>
<p>Code <strong>HIVE-LAUNCH30</strong> takes 30% off any kit at checkout.</p>

<p><em>Related: the <a href="food-cost-percentage-tracker.html">food cost percentage tracker</a> is the Friday count this sheet rides along with &mdash; one walk produces both the ratio and the order; the <a href="delivery-receiving-checklist.html">delivery receiving checklist</a> is where the order gets verified at the door before the math ever sees it; the <a href="walk-in-cooler-maintenance-checklist.html">walk-in cooler maintenance checklist</a> keeps the box your stock lives in actually working; the <a href="refrigeration-temperature-log.html">refrigeration temperature log</a> is why the stock you ordered is still stock on Monday; the <a href="weekly-ops-review.html">weekly ops review</a> is where the 86s and the par checks get read as vital signs; and the <a href="purchase-order-process-small-teams.html">purchase order process</a> is the approval layer for the orders that leave the food world &mdash; equipment, services, everything with a PO number.</em></p>
</main>
</body>
</html>
'''
open(PAGE, 'w').write(html)

# 2) index TOP card
idx = open('index.html').read()
assert PAGE not in idx
card = ('<li><a href="' + PAGE + '">The Par Level &amp; Ordering Guide: The Sheet That Turns Friday&rsquo;s Count Into Monday&rsquo;s Order</a>'
        '<div class="desc">One formula (par = daily usage &times; delivery days + one safety day, minus on-hand, rounded to case size), '
        'one walk per week that shares its twenty minutes with the food cost count, a par check column that lets the number learn from '
        'its surprises, and the quarterly dead-stock audit that finds the lamb shoulder from the special that ended in July. Worked example: '
        'the 40-seat restaurant freed $2,300 on day one, killed the Saturday romaine 86 with an honest safety day, and cut the produce par 15% '
        'behind the repaired gasket &mdash; $180 a week back without buying anything.</div></li>')
marker = '<h1>Ops notes</h1>'
assert marker in idx
idx = idx.replace(marker, marker + card, 1)
open('index.html', 'w').write(idx)

# 3) README NEW line (top)
readme = open('README.md').read()
if PAGE not in readme:
    entry = ('- **NEW: [The Par Level & Ordering Guide: The Sheet That Turns Friday\'s Count Into Monday\'s Order](' + URL + ')** '
             '&mdash; the only formula on the page (par = daily usage &times; delivery cycle + one safety day &minus; on-hand, rounded to case size), '
             'one row per item with a par-check column that learns from its own surprises, the quarterly dead-stock audit, and safety stock sized '
             'to delivery-day reality instead of fear. Worked example: the 40-seat restaurant&rsquo;s first audit freed $2,300 of dead stock, fixed '
             'the Saturday romaine 86 and cut produce par 15% behind the repaired gasket.\\n')
    open('README.md', 'w').write(entry + readme)

# 4) reciprocal backlinks
def backlink(fname, rel):
    t = open(fname).read()
    if PAGE not in t:
        assert '</main>' in t, fname + ' no </main>'
        t = t.replace('</main>', rel + '</main>', 1)
        open(fname, 'w').write(t)

backlink('food-cost-percentage-tracker.html',
    '<p><em>Related: the <a href="' + URL + '">par level &amp; ordering guide</a> is what acts on the count &mdash; the tracker '
    'finds the leak, the par sheet reorders to here instead of to vibes, and the two share the same Friday shelf walk.</em></p>\n')
backlink('delivery-receiving-checklist.html',
    '<p><em>Related: the <a href="' + URL + '">par sheet</a> writes the order; the <a href="delivery-receiving-checklist.html">'
    'delivery receiving checklist</a> is where the order becomes fact &mdash; count, weigh, reject, invoice &mdash; before the '
    'stock ever reaches the shelf the Friday walk will count.</em></p>\n')
backlink('walk-in-cooler-maintenance-checklist.html',
    '<p><em>Related: the <a href="' + URL + '">par levels</a> assume the box works; the <a href='
    '"walk-in-cooler-maintenance-checklist.html">Sunday cooler walk</a> is what keeps that assumption true &mdash; a failing '
    'gasket turns a correct par into a spoilage order.</em></p>\n')
backlink('refrigeration-temperature-log.html',
    '<p><em>Related: the <a href="' + URL + '">ordering guide</a> decides what arrives; the <a href='
    '"refrigeration-temperature-log.html">refrigeration temperature log</a> decides what survives &mdash; twice-daily reads '
    'protect the money the par sheet just spent.</em></p>\n')
backlink('weekly-ops-review.html',
    '<p><em>Related: par misses and 86s belong in the <a href="weekly-ops-review.html">weekly ops review</a> next to the '
    '<a href="' + URL + '">par sheet&rsquo;s</a> order log &mdash; three surprises in a quarter is a par change, and the '
    'review is where the change gets decided.</em></p>\n')
backlink('purchase-order-process-small-teams.html',
    '<p><em>Related: food orders run on the <a href="' + URL + '">par sheet</a>; everything else with a PO number '
    'runs through the <a href="purchase-order-process-small-teams.html">purchase order process</a> &mdash; same principle, '
    'fewer zeros: order to a number, not to a mood.</em></p>\n')

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
cards = open('index.html').read().count('<li><a hre')
print(f"BUILT {PAGE}")
print(f"sitemap urls: {n}; index cards: {cards}; linkcheck: {total_hrefs} hrefs, 0 broken")
