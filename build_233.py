import re, os
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'overdue-invoice-letters.html'
URL  = 'https://hive80-lab.github.io/ops-notes/overdue-invoice-letters.html'
TODAY = '2026-09-13'

# 1) index.html - TOP card
card = ('<li><a href="' + PAGE + '">Overdue Invoice Letters: Chasing Late Payers '
        'Without Losing the Customer</a>'
        '<div class="desc">The four-letter ladder that turns unpaid invoices into paid ones: '
        'day-1 friendly reminder (assumption-first, rails re-attached), day-14 direct follow-up '
        '("still showing unpaid" plus the question), day-30 phone call that converts a balance '
        'into a promise with a date, day-45 final notice with the stop-work rule stated once. '
        'One thread per invoice, one named pen, never an apology for the invoice; disputes are '
        'resolved line by line while silence goes up the ladder unchanged; and the four terms '
        '(deposit on first jobs, short terms for strangers, the late-fee clause printed on the '
        'invoice, same-day invoicing) that stop the next late payer before the invoice goes out. '
        'Worked example: the plumber whose $11,400 of ninety-day receivables became six paid '
        'invoices, one split, one collections handoff &mdash; and a Tuesday balance under a '
        'thousand dollars.</div></li>')
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
    entry = ('- **NEW: [Overdue Invoice Letters (Chasing Late Payers Without Losing the '
             'Customer)](' + URL + ')** &mdash; why late payers are a business you run for free, '
             'the four-letter ladder (day-1 reminder, day-14 follow-up, day-30 call, day-45 final '
             'notice), who holds the pen, the rules that make chasing work (one thread per '
             'invoice, rails re-attached every time, chase the process not the person, never '
             'apologise for the invoice, stop work stated once), the telephone step that converts '
             'a balance into a dated promise, disputes versus silence, and the four terms that '
             'stop the next late payer. Worked example: the plumber\'s $11,400 answer.\\\\n')
    open('README.md', 'w').write(entry + readme)

# 4a) backlink: failed-payment-dunning-sequence (the card-bounce sibling)
t = open('failed-payment-dunning-sequence.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: a card that bounces and an invoice that waits are the same money in '
           'two wrappers &mdash; the <a href="' + URL + '">overdue invoice letters</a> run the '
           'same four-step ladder against invoices, where a phone call on day thirty converts '
           'the balance into a promise with a date.</em></p>\n')
    if '</main>' in t:
        t = t.replace('</main>', rel + '</main>', 1)
    else:
        m = re.search(r'(<footer>)', t); assert m, 'dunning footer missing'
        t = t[:m.start()] + rel + t[m.start():]
    open('failed-payment-dunning-sequence.html', 'w').write(t)

# 4b) backlink: monthly-close-checklist
t = open('monthly-close-checklist.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: the close is where the <a href="' + URL + '">overdue invoice '
           'letters</a> get their marching orders &mdash; the aging report read out loud, invoice '
           'by invoice, decides which reminder, call, or final notice goes out before the books '
           'shut.</em></p>\n')
    if '</main>' in t:
        t = t.replace('</main>', rel + '</main>', 1)
    else:
        m = re.search(r'(<footer>)', t); assert m, 'monthly-close footer missing'
        t = t[:m.start()] + rel + t[m.start():]
    open('monthly-close-checklist.html', 'w').write(t)

# 4c) backlink: cash-runway-checklist
t = open('cash-runway-checklist.html').read()
if PAGE not in t:
    rel = ('<p><em>Related: receivables are runway living in somebody else\'s bank account &mdash; '
           'the <a href="' + URL + '">overdue invoice letters</a> are the scheduled, polite '
           'machinery that flies it home before the tank reads empty.</em></p>\n')
    if '</main>' in t:
        t = t.replace('</main>', rel + '</main>', 1)
    else:
        m = re.search(r'(<footer>)', t); assert m, 'runway footer missing'
        t = t[:m.start()] + rel + t[m.start():]
    open('cash-runway-checklist.html', 'w').write(t)

# 5) linkcheck: every relative href in the new page must exist on disk
page = open(PAGE).read()
missing = [h for h in re.findall(r'href="([a-z0-9-]+\.html)"', page)
           if not os.path.exists(h)]
assert not missing, 'broken relative links: %r' % missing

# 6) summary
n = open('sitemap.xml').read().count('<url>')
cards = open('index.html').read().count('<li><a href="')
print('OK build_233: sitemap urls=%d, index cards~%d, page %d bytes, 0 coupon=%s'
      % (n, cards, os.path.getsize(PAGE),
         'HIVE20' not in open(PAGE).read()))
