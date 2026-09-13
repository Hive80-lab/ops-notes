import re, os
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'monthly-ops-report-template.html'
URL  = 'https://hive80-lab.github.io/ops-notes/monthly-ops-report-template.html'
TODAY = '2026-09-13'

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Monthly Ops Report &mdash; The One Page That Makes Last Month Legible</title>
<meta name="description" content="A monthly operations report small teams actually write and actually read: one page, six fixed sections, numbers pulled from the month-end close, the three honesty rules, and the five traps &mdash; plus the print shop whose trend number caught an on-time-delivery slide three months before the customer did.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/monthly-ops-report-template.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>

<h1>The Monthly Ops Report: The One Page That Makes Last Month Legible</h1>
<p class="lede">One page, six fixed sections, written the morning after the month-end close and shipped the same day. The three honesty rules that keep it a report instead of a press release, the five traps that turn it into wallpaper, and the twelve-person print shop whose trend number caught an on-time-delivery slide three months before the customer did.</p>

<p>Ask most small-business teams how last month went and you get a mood: &ldquo;pretty good I think?&rdquo; Ask for a number and you get a different number from whoever you ask &mdash; because nobody wrote it down, and memory quietly rounds bad months up. The monthly ops report is the antidote, and it is deliberately small: <strong>one page</strong>, the same six sections every month, filled in the morning after the <a href="monthly-close-checklist.html">month-end close</a> so every number comes from the books rather than from recollection. It is the monthly answer to what the <a href="weekly-ops-review.html">weekly ops review</a> answers every Friday &mdash; the review is where the month is steered; the report is where the month is <em>recorded</em>, so that next month&rsquo;s decisions are made on this month&rsquo;s truth instead of on whoever argued longest.</p>

<p>The one page matters more than it sounds. A report nobody reads is a report nobody wrote next month. The discipline is not &ldquo;more reporting&rdquo; &mdash; it is a fixed page, a fixed author, and a fixed morning, sixty days in a row.</p>

<h2>1. The one-page rule &mdash; six fixed sections, in this order</h2>
<ol>
<li><strong>The trend number.</strong> One metric that defines this operation &mdash; on-time delivery, pick accuracy, first-response time, gross margin, billable utilization &mdash; defined once, in writing, and never quietly redefined. Written as <em>number, prior month, one-line cause</em> if it moved more than the threshold. This is the line the whole report exists for.</li>
<li><strong>Money.</strong> Revenue, gross margin percent, cash at month end &mdash; four lines at most, all pulled from the close, never from memory. This section has one job: make the <a href="budget-vs-actuals-monthly-review.html">budget vs actuals hour</a> findable when someone asks &ldquo;where did that number come from?&rdquo;</li>
<li><strong>Incidents and near-misses.</strong> The count, the worst one in two lines, and what changed because of it. Sourced from the <a href="incident-post-mortem-template.html">post-mortems</a> &mdash; if nothing changed, that is the line: &ldquo;no change made&rdquo; is an honest sentence that starts useful arguments.</li>
<li><strong>People.</strong> Headcount, open roles with days-open, and one staffing risk with a name on it. The risk line is what makes the <a href="staffing-shortage-coverage-plan.html">coverage plan</a> get written before the crunch instead of during it.</li>
<li><strong>Process changes shipped.</strong> Dated one-liners, &ldquo;shipped&rdquo; meaning live in the operation, not planned or proposed. This section is the receipt for the improvement list the weekly review keeps producing.</li>
<li><strong>Next month&rsquo;s known pressure.</strong> Two or three items, each with an owner and a date &mdash; the renewal, the launch, the audit, the season. This is where next month&rsquo;s report goes to find out whether the pressure was handled.</li>
</ol>
<p>That is the page. If a seventh section is fighting to get in, the question is not &ldquo;where does it fit?&rdquo; but &ldquo;which of the six does it replace?&rdquo; &mdash; because the answer &ldquo;none, add it anyway&rdquo; is how one page becomes six pages, and six pages is how reports die.</p>

<h2>2. The writing ritual &mdash; one author, forty-five minutes, the morning after the close</h2>
<p>The report has one author (the ops lead, or the owner in a team of five) and one slot: the morning after the month-end close finishes, because the close is what makes the money lines true. The ritual is forty-five minutes: pull the three money lines from the close, the count and the worst incident from the post-mortems, and write the other sections from the weekly reviews of the past four Fridays &mdash; which is why the <a href="weekly-ops-review.html">weekly review&rsquo;s</a> promise ledger is worth keeping. Distribution is the same day: team channel or one-page email, everyone, not a meeting. A report that requires a meeting to be read has already failed; the meeting is where it gets <em>discussed</em>, once a month, for twenty minutes, if a line earns it.</p>

<h2>3. The three honesty rules</h2>
<ul>
<li><strong>Same definitions every month.</strong> The trend number is defined once &mdash; window, denominator, exclusions &mdash; and redefining it requires writing down why. A metric quietly redefined in month four is not a trend anymore; it is two unrelated numbers wearing the same name, and every month-over-month comparison is fiction from that day.</li>
<li><strong>Bad months ship the same page.</strong> A report that only goes out when it flatters is a press release. The bad months are the ones where the page earns its keep &mdash; they are also the ones where skipping it is most tempting, which is how you end up with a report habit that evaporates the first time it matters.</li>
<li><strong>Every line has a name and a date.</strong> Risks, pressures, actions &mdash; owned and dated or cut. &ldquo;Someone should look at supplier lead times&rdquo; is not a line in a report; it is a wish with formatting.</li>
</ul>

<h2>4. The five traps</h2>
<ul>
<li><strong>The novel.</strong> Six pages with appendixes. Nobody reads past page one, so nobody notices the trend number, which was the whole point. One page. The detail lives in the close file, the post-mortems, and the reviews &mdash; the report cites, it does not contain.</li>
<li><strong>The vanity report.</strong> Only good news, curated by the person who wants the month to have gone well. It reads fine for four months and then the business has no record of when the problem started &mdash; which is the only thing a report is actually for.</li>
<li><strong>The dashboard dump.</strong> A screenshot of the analytics dashboard pasted in and called a report. Dashboards answer &ldquo;what is happening right now?&rdquo;; the report answers &ldquo;what happened last month, what changed, and what is coming?&rdquo; A dump has no causes, no owners, no next month &mdash; and no reader.</li>
<li><strong>The drifting definition.</strong> Covered above and worth its own line, because it is the most common way a habit survives while becoming useless: the page keeps shipping, the numbers stop meaning anything.</li>
<li><strong>The late report.</strong> Ships on the 20th of the following month, after the decisions it was supposed to feed. A late report is a history book; the report is a steering input, and it only steers if it arrives before the decisions &mdash; which is why the slot is tied to the close, not to &ldquo;when we get around to it.&rdquo;</li>
</ul>

<h2>5. Worked example &mdash; the print shop that saw the slide coming</h2>
<p>A twelve-person custom print shop &mdash; trade work for design agencies plus walk-in business &mdash; ran its first monthly ops report in March. The trend number they picked was on-time delivery, defined as orders shipped on the promised date, measured across the month. March read 96.4%. April, 95.1% &mdash; a one-line cause was owed under their own threshold and the line said &ldquo;two rush orders rescheduled, no pattern identified.&rdquo; May read 91.8%, and the cause line &mdash; which they now had to write, in front of the team, every month &mdash; could no longer say &ldquo;no pattern.&rdquo; The slide had been invisible before because it lived in three separate weekly conversations, each small enough to absorb; the report stacked the three months on one line and the slide became a fact. The trace led to a paper supplier change made in February &mdash; cheaper per sheet, two days slower, and nobody had connected the supplier switch to the delivery dates because no one was reading the trend line monthly. The fix was small and unglamorous: dual-sourcing on the two stock grades that caused the slips, a one-week buffer, and a delivery-date commitment written into the new supplier&rsquo;s renewal. On-time delivery was back to 96.1% by September. The stakes behind the trend number were real: their largest trade account &mdash; roughly $40,000 a year &mdash; had started quietly moving rush work to a competitor, and the account manager said later that the September report, with the recovery on one line, was the only reason the account was not already gone. The counterfactual is the version they almost ran: six months of mood-based reporting, the slide discovered by the customer, and the first honest report written as a post-mortem of a lost account.</p>

<h2>Kits</h2>
<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="weekly-ops-review.html">weekly ops review</a> is the four Fridays that feed this page&rsquo;s incidents, changes, and pressures; the <a href="monthly-close-checklist.html">monthly close checklist</a> is where the money lines come from &mdash; the report is written the morning after the close, never before it; the <a href="budget-vs-actuals-monthly-review.html">budget vs actuals review</a> is the variance hour that runs off the same close, same coffee; the <a href="year-end-close-checklist.html">year-end close</a> is twelve of these months plus adjustments &mdash; a year of honest monthly pages is what makes December&rsquo;s runway short; and the <a href="incident-post-mortem-template.html">post-mortem template</a> is where section 3&rsquo;s worst incident comes from, with the change it produced.</em></p>

</main>
</body>
</html>'''

with open(PAGE, 'w') as f:
    f.write(html)
print('wrote', PAGE, len(html), 'bytes')

# 1) index.html - TOP card
card = ('<li><a href="' + PAGE + '">The Monthly Ops Report: The One Page That Makes Last Month Legible</a>'
        '<div class="desc">One page, six fixed sections (the trend number, money from the close, incidents '
        'and near-misses, people, process changes shipped, next month&rsquo;s known pressure), a forty-five-minute '
        'ritual the morning after the month-end close, the three honesty rules (same definitions every month, bad '
        'months ship the same page, every line has a name and a date), and the five traps (the novel, the vanity '
        'report, the dashboard dump, the drifting definition, the late report). Worked example: a twelve-person '
        'print shop whose trend number stacked three months of small slips into one fact &mdash; an on-time-delivery '
        'slide traced to a February supplier change and fixed before the $40k account walked.</div></li>')
idx = open('index.html').read()
if PAGE not in idx:
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
    entry = ('- **NEW: [The Monthly Ops Report: The One Page That Makes Last Month Legible](' + URL + ')** '
             '&mdash; one page, six fixed sections, written the morning after the month-end close; the three '
             'honesty rules (same definitions every month, bad months ship the same page, every line owned and '
             'dated) and the five traps. Worked example: the print shop whose trend number caught an on-time-delivery '
             'slide three months before the customer did.\n')
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
backlink('weekly-ops-review.html',
    '<p><em>Related: the weekly review is the four Fridays that feed the <a href="' + URL + '">monthly ops '
    'report</a> &mdash; incidents, shipped changes, and next month&rsquo;s pressure all come from the week&rsquo;s '
    'notes; the monthly page is where they are recorded once, in one place, on the same definitions.</em></p>\n')
backlink('monthly-close-checklist.html',
    '<p><em>Related: the <a href="' + URL + '">monthly ops report</a> is written the morning after this close '
    '&mdash; the close produces the money lines, the report records them; never ship a report built on '
    'half-closed books.</em></p>\n')
backlink('budget-vs-actuals-monthly-review.html',
    '<p><em>Related: the <a href="' + URL + '">monthly ops report</a> and the budget vs actuals hour run off the '
    'same close &mdash; the report records what happened and what is coming, the variance hour reads the plan '
    'against it; findings from one belong in the other the same day.</em></p>\n')
backlink('year-end-close-checklist.html',
    '<p><em>Related: the year-end close is twelve monthly closes plus adjustments &mdash; and a year of honest '
    '<a href="' + URL + '">monthly ops reports</a> is what makes the December runway short instead of '
    'archaeological.</em></p>\n')
backlink('incident-post-mortem-template.html',
    '<p><em>Related: the <a href="' + URL + '">monthly ops report</a> incident section is fed by the '
    'post-mortems &mdash; count, worst one, and the change it produced; if nothing changed, the report says so, '
    'on purpose.</em></p>\n')

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
print('OK build_245: sitemap %d urls (XML valid) | index cards %d | linkcheck 0 broken across %d hrefs' % (n, cards, total_hrefs))