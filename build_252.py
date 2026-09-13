import re, os, datetime
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'walk-in-cooler-maintenance-checklist.html'
URL  = 'https://hive80-lab.github.io/ops-notes/walk-in-cooler-maintenance-checklist.html'
TODAY = datetime.date.today().isoformat()

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Walk-In Cooler Maintenance Checklist &mdash; The Sunday Hour That Keeps the Cold Chain Alive</title>
<meta name="description" content="A one-hour weekly walk-in cooler maintenance checklist for restaurants: the dollar-bill gasket test at six points per door, the condenser coil you dust before the compressor pays for it, the iced evaporator face, the dry drain pan, honest thermometers, and the Sunday walk that turned a $125 gasket kit into two more compressor seasons &mdash; instead of a $2,800 compressor and $9,000 of stock in August.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/walk-in-cooler-maintenance-checklist.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>

<h1>The Walk-In Cooler Maintenance Checklist: The Sunday Hour That Keeps the Cold Chain Alive</h1>
<p class="lede">One hour, once a week, with a dollar bill, a screwdriver and a bucket: the six-point gasket test, the condenser coil that converts dust into compressor years, the evaporator face that hides its ice until the night it matters, the drain pan that should be wet but not full, and the door hardware that decides whether all of it holds. The Sunday walk that turns a $125 parts order into two more compressor seasons.</p>

<p>The <a href="refrigeration-temperature-log.html">temperature log</a> tells you the walk-in is cold twice a day. It does not tell you the box is <em>working hard</em> to be cold &mdash; a compressor pulling 41&deg;F through a leaking gasket and a dust-caked coil is a countdown, not a success. The <a href="refrigeration-temperature-log.html">twice-daily log</a> catches the day the countdown ends; this page is the weekly hour that pushes the countdown back. Both matter, and they are different jobs: the log is the smoke detector, the Sunday walk is the smoke <em>prevention</em>.</p>

<h2>1. The dollar-bill gasket test &mdash; six points, every door, every week</h2>
<p>Close the door on a dollar bill at six points &mdash; top, middle, bottom, and both hinges-side midpoints &mdash; and pull. The bill should drag. Any point where it slides out freely is a leak, and a leak is a compressor running flat-out to cool the hallway. Order the parts the same day: gasket kits are $60&ndash;$125 and arrive in a week; the compressor they kill is $2,800 installed and takes the <a href="cold-chain-failure-checklist.html">cold-chain failure playbook</a> with it when it goes. Write the pull points on the checklist itself &mdash; &ldquo;rear door, point 4 pulls free&rdquo; is a work order, &ldquo;gaskets feel off&rdquo; is a vibe. Vague findings die in the <a href="maintenance-work-order-template.html">work order template</a> the same afternoon, not next week.</p>

<h2>2. The condenser coil &mdash; the dust you can bank against</h2>
<p>The condenser coil is where the box dumps kitchen heat into the room, and it is usually mounted low on the walk-in or behind the compressor deck where flour, grease and dust settle into felt. A felted coil cannot dump heat, so the compressor runs longer and hotter and dies younger &mdash; the single most expensive piece of deferred maintenance in a commercial kitchen. Vacuum it with a brush head, then wipe with coil cleaner once a month, weekly in summer. The test is cheap: coil fins should look like metal, not carpet. This is also the one task on the sheet where &ldquo;looks fine from across the room&rdquo; means nothing &mdash; it is a ten-minute hands-on job or it is not done.</p>

<h2>3. The evaporator face &mdash; the ice that hides until the night it matters</h2>
<p>Open the fan access and look at the evaporator coil face. Light frost that melts between defrost cycles is normal. A snow ridge across the bottom third, ice bridging between fins, or a fan blade shaving its own iceberg means the defrost cycle is losing &mdash; and capacity is going with it. Chisel nothing: score the ice with a plastic scraper and let warm water finish it, or you replace a coil. Note the percentage of face blocked in the log; 30 percent blocked on a Sunday becomes a service call on a Monday, which is exactly the point. The <a href="preventive-maintenance-schedule-template.html">preventive maintenance schedule</a> is where this line item gets its date and its owner.</p>

<h2>4. Drain pan and line &mdash; wet is right, full is wrong</h2>
<p>The defrost water has to go somewhere: a pan (or a drain line to a floor sink) that is quietly full, slimed, or dry-iced over is tomorrow's puddle on the floor and next month's ceiling tile. Flush the drain line with warm water and a capful of coil cleaner, confirm the pan empties, and check the line's trap for the algae rope that clogs restaurant drains every six weeks like clockwork. While you are down there: ice on the <em>floor</em> near the evaporator means the pan is overflowing, not that the box is too cold &mdash; a misread that has sent more than one operator to buy a thermostat they did not need.</p>

<h2>5. Door hardware &mdash; the parts that decide whether Sunday holds</h2>
<p>Gaskets fail faster when the door fights them. Spring hinges that no longer self-close, a closer that slams, a sweep dragging the floor, a stripped latch that leaves the door resting instead of sealed &mdash; each one turns a Sunday fix into a monthly gasket replacement. Lubricate hinges, tighten the closer, align the strike, and make sure strip curtains are intact end to end. The dollar-bill test in section 1 is the audit; this is the repair that keeps the audit passing. Log hardware faults the same way as temperature drift &mdash; in the <a href="equipment-downtime-log.html">equipment downtime log</a> so patterns survive staff turnover.</p>

<h2>6. Honest thermometry &mdash; the readout you argue with</h2>
<p>The box's digital display is a convenience, not an instrument. Keep one calibrated thermometer on a middle shelf and read it every Sunday; if it disagrees with the display by more than 2&deg;F, trust the hanging thermometer and order a service call &mdash; the display reads a sensor, the food reads the room. This is the same honesty rule from the <a href="refrigeration-temperature-log.html">temperature log</a> at weekly depth: air temperature is the smoke detector, food temperature is the truth, and the Sunday read is the weekly calibration between them. Record both numbers; a disagreement in the log is a service ticket, a shrug is a diagnosis you cannot make later.</p>

<h2>Worked example: the 40-seat diner's Sunday, 07:15&ndash;08:15</h2>
<p>One hour, one page, in order. The dollar bill pulls free at point 4 of the rear door (leak); evaporator face is 30 percent iced across the bottom (defrost losing); condenser coil looks like carpet (overdue); drain pan full and slimed; hinges OK, closer slams; hanging thermometer 38&deg;F vs display 41&deg;F. Total findings: six. Cost of parts: $125 (gasket kit, closer, coil cleaner). Work order #0189 goes to the refrigeration tech that morning &mdash; gasket and closer Thursday, defrost timer checked on the same visit, coil booked with the quarterly <a href="preventive-maintenance-schedule-template.html">PM service</a>.</p>
<p>The counterfactual is the invoice file: the compressor that ran flat-out through a leaking gasket for one more summer died on the first August heat wave &mdash; $2,800 installed, $9,000 of stock written off, two days of <a href="cold-chain-failure-checklist.html">cold-chain failure</a> during the busiest week of the year. The Sunday hour is not maintenance theater. It is the cheapest insurance premium in the building, and unlike most insurance, it pays out in gaskets you can actually see.</p>

<h2>The five traps</h2>
<ul>
<li><strong>Dusting the coil with the brush from the pastry station.</strong> A flour-and-grease felted coil needs vacuum plus coil cleaner. Wiping it with a dry rag polishes the felt and changes nothing.</li>
<li><strong>Chiseling the evaporator.</strong> A screwdriver through a coil turns a $0 defrost problem into a $900 coil. Warm water and patience, every time.</li>
<li><strong>One Sunday in spring.</strong> The walk is weekly because gaskets tear, drains slime and coils felt on kitchen timescales, not seasonal ones. The <a href="preventive-maintenance-schedule-template.html">schedule</a> exists precisely so this does not depend on someone remembering.</li>
<li><strong>Fixing the symptom, not the door.</strong> Replacing gaskets quarterly on a door whose closer slams is paying rent on the real problem. Hardware first, gasket second &mdash; or you are buying the same kit four times a year.</li>
<li><strong>Trusting the display.</strong> The readout is a convenience, the hanging thermometer is an instrument, the food temperature is the truth. When they disagree, believe them in that order.</li>
</ul>

<h2>Kits</h2>
<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="refrigeration-temperature-log.html">refrigeration temperature log</a> is the twice-daily smoke detector this Sunday walk prevents fires for; the <a href="maintenance-work-order-template.html">maintenance work order template</a> is where Sunday's findings become Thursday's parts order; the <a href="preventive-maintenance-schedule-template.html">preventive maintenance schedule</a> gives the walk its calendar slot and its owner; the <a href="equipment-downtime-log.html">equipment downtime log</a> keeps the failure history that turns a pattern into a budget line; the <a href="critical-spare-parts-list.html">critical spare parts list</a> is the reason the gasket kit is on the shelf instead of in a week's shipping; and the <a href="cold-chain-failure-checklist.html">cold-chain failure checklist</a> is the playbook for the day the Sunday hour was skipped.</em></p>

</main>
</body>
</html>
'''

open(PAGE, 'w').write(html)

# 1) index.html - TOP card
card = ('<li><a href="' + PAGE + '">The Walk-In Cooler Maintenance Checklist: The Sunday Hour That Keeps the Cold Chain Alive</a>'
        '<div class="desc">One hour a week with a dollar bill, a screwdriver and a bucket &mdash; the six-point gasket '
        'test that catches the leak before the compressor pays for it, the condenser coil where dust becomes '
        'compressor death, the evaporator ice that hides until the night it matters, the drain pan that should be wet '
        'but not full, and the door hardware that decides whether the gasket lasts a season or a month. Worked '
        'example: the 40-seat diner whose Sunday 07:15 walk turned a $125 parts order into two more compressor '
        'seasons &mdash; instead of a $2,800 compressor and $9,000 of stock in August.</div></li>')
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
    entry = ('- **NEW: [The Walk-In Cooler Maintenance Checklist: The Sunday Hour That Keeps the Cold Chain Alive](' + URL + ')** '
             '&mdash; one hour a week with a dollar bill, a screwdriver and a bucket: the six-point gasket test, the '
             'condenser coil that converts dust into compressor death, the evaporator face that hides its ice, the '
             'drain pan (wet is right, full is wrong), the door hardware that decides whether the gasket lasts, and '
             'honest thermometry (display &lt; hanging thermometer &lt; food). Worked example: the 40-seat diner whose '
             'Sunday walk found the point-4 gasket leak and the 30 percent iced coil &mdash; $125 in parts and work '
             'order #0189 the same morning, instead of the $2,800 compressor and $9,000 stock write-off in August.\n')
    open('README.md', 'w').write(entry + readme)

# 4) reciprocal backlinks
def backlink(fname, rel):
    t = open(fname).read()
    if PAGE not in t:
        if '</main>' in t:
            t = t.replace('</main>', rel + '</main>', 1)
        else:
            m = re.search(r'(<footer>)', t); assert m, fname + ' footer missing'
            t = t[:m.start()] + rel + t[m.start():]
        open(fname, 'w').write(t)

backlink('refrigeration-temperature-log.html',
    '<p><em>Related: the twice-daily <a href="' + URL + '">walk-in cooler maintenance checklist</a> is the weekly '
    'companion to this log &mdash; the log catches the day the countdown ends, the Sunday hour pushes the countdown '
    'back.</em></p>\n')
backlink('maintenance-work-order-template.html',
    '<p><em>Related: Sunday findings from the <a href="' + URL + '">walk-in cooler maintenance checklist</a> become '
    'Thursday parts orders here &mdash; a dollar bill that pulls free at point 4 is work order language, not a '
    'feeling.</em></p>\n')
backlink('preventive-maintenance-schedule-template.html',
    '<p><em>Related: the <a href="' + URL + '">walk-in cooler checklist</a> is one block in the weekly schedule '
    '&mdash; this is where the Sunday hour gets its calendar slot, its owner and its parts budget.</em></p>\n')
backlink('equipment-downtime-log.html',
    '<p><em>Related: log walk-in hardware faults from the <a href="' + URL + '">cooler maintenance checklist</a> in '
    'the downtime log &mdash; the pattern (third gasket this year, closer still slamming) is the budget case for the '
    'real fix.</em></p>\n')
backlink('critical-spare-parts-list.html',
    '<p><em>Related: the <a href="' + URL + '">walk-in cooler checklist</a> tells you the gasket will fail; the '
    'spare parts list is why the replacement is on the shelf instead of in a week&rsquo;s shipping.</em></p>\n')
backlink('cold-chain-failure-checklist.html',
    '<p><em>Related: the <a href="' + URL + '">Sunday cooler walk</a> is how you never meet this playbook &mdash; '
    'but the cold-chain failure checklist is what the walk-in&rsquo;s compressor reads like when it is already too '
    'late.</em></p>\n')

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
print('OK build_252: sitemap %d urls (XML valid) | index cards %d | linkcheck 0 broken across %d hrefs' % (n, cards, total_hrefs))
