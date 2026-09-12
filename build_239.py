import re, os
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
PAGE = 'purchase-order-process-small-teams.html'
URL  = 'https://hive80-lab.github.io/ops-notes/purchase-order-process-small-teams.html'
TODAY = '2026-09-13'

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Purchase Order Process for Small Teams &mdash; The Five-Minute Step That Stops the Surprise Invoice</title>
<meta name="description" content="A purchase order process small teams will actually run: the seven-line PO, the approval threshold that keeps it out of the way, the three-way match that kills duplicate and ghost invoices, and the five traps &mdash; plus the HVAC contractor whose $9,400 nobody-ordered compressor became the last surprise.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/purchase-order-process-small-teams.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>

<h1>The Purchase Order Process for Small Teams: The Five-Minute Step That Stops the Surprise Invoice</h1>
<p class="lede">The seven lines every PO carries, the threshold that keeps the process out of the way, the three-way match that kills duplicate and ghost invoices, and the five traps that turn "PO culture" into paperwork theatre.</p>

<p>Every small business has received the invoice nobody remembers ordering. Not fraud, usually &mdash; a tech ordered a compressor from the ute on Tuesday, the office met it three weeks later as a $9,400 line in the inbox, and by then the cash the <a href="13-week-cash-flow-forecast.html">13-week forecast</a> had planned for the week is spoken for. The problem is not the supplier and not the spender; it is that approval and commitment travel by conversation, while payment arrives on paper. A purchase order is the bridge: a one-page promise, numbered, that says who approved what, for how much, against which job &mdash; written <em>before</em> the money is committed, in five minutes. It is the third leg of the spend triad: the <a href="supplier-payment-terms-checklist.html">supplier payment terms</a> govern how you pay, the <a href="expense-reimbursement-policy.html">expense policy</a> governs what employees spend from their own pockets, and the PO governs what the company commits to before the invoice exists.</p>

<h2>1. What a PO actually is &mdash; a promise with a number on it</h2>
<p>A PO is not bureaucracy; it is a receipt for a decision. It captures, in seven lines, the conversation that used to evaporate:</p>
<ol>
<li><strong>PO number</strong> &mdash; sequential, one series, no reuse. This is the spine the whole system hangs on.</li>
<li><strong>Supplier</strong> &mdash; the legal name on the account, not the salesperson's first name.</li>
<li><strong>What and how much</strong> &mdash; description, quantity, unit price. Specific enough that a stranger could deliver it.</li>
<li><strong>Agreed price and terms</strong> &mdash; the number you were quoted, and the payment terms it sits on. If the quoted price isn't on the PO, the PO didn't happen.</li>
<li><strong>Job or cost code</strong> &mdash; where this spend will live in the books. This one line is what makes the <a href="monthly-close-checklist.html">month-end close</a> fast.</li>
<li><strong>Approver</strong> &mdash; a name, not a vibe. One name, written down.</li>
<li><strong>Date and delivery instructions</strong> &mdash; so "it never arrived" has a place to be answered.</li>
</ol>
<p>Sent to the supplier before the order is placed, the PO does something subtle: it converts your word into the supplier's expectation, which is the only document that beats the invoice at its own game.</p>

<h2>2. The threshold &mdash; where the process starts and where it stays out of the way</h2>
<ul>
<li><strong>Under the threshold (say $500):</strong> spend freely on the company card, claim through the <a href="expense-reimbursement-policy.html">expense policy</a>. No PO. The process exists to catch the large and the repeated, not to slow down a $40 box of fittings.</li>
<li><strong>Over the threshold, one-off:</strong> PO before order. Five minutes, seven lines, sent to the supplier.</li>
<li><strong>Recurring, any size:</strong> one standing PO per supplier, renewed quarterly &mdash; the monthly service, the consumables account, the hire fleet. One number, twelve deliveries, matched once a month.</li>
<li><strong>The exception path:</strong> genuine urgency &mdash; a breakdown at a client site &mdash; buys now with a text to the approver and a PO the same day. The exception is fast; it is never silent.</li>
</ul>

<h2>3. The three-way match &mdash; where ghost invoices go to die</h2>
<p>When a supplier invoice arrives, it gets one question: <em>does it match?</em> Three documents, compared line by line:</p>
<ol>
<li><strong>The PO</strong> &mdash; what was approved: item, quantity, price, terms.</li>
<li><strong>The delivery or completion evidence</strong> &mdash; what actually arrived: signed docket, job sheet, tracking confirmed.</li>
<li><strong>The invoice</strong> &mdash; what is being claimed.</li>
</ol>
<p>All three agree &rarr; pay on terms, book to the job code, done. They don't &rarr; one line of query to the supplier naming the mismatch: "PO 2147 says 4 units at $380; invoice claims 6 at $410." Never "pay and hope"; never a silent deduction. The match takes two minutes per invoice and is the only reliable killer of the three classics: the duplicate (same invoice, two numbers), the drift (delivered price creeps above PO price), and the phantom (delivered to an address you don't trade at).</p>

<h2>3a. The weekly ten minutes &mdash; feeding the forecast</h2>
<p>Once a week &mdash; the same sitting as the <a href="13-week-cash-flow-forecast.html">13-week cash flow hour</a> &mdash; read out the unapproved-invoice list: every supplier invoice with no PO number beside it. Each gets its answer: matched to a standing PO, backdated to an approval, or queried. The list exists not to punish anyone; it exists because unapproved commitments are the reason the forecast's outflow row is a guess. Ten minutes, one owner, and the surprise invoice goes extinct.</p>

<h2>4. The five traps</h2>
<ul>
<li><strong>The verbal PO culture.</strong> "Dave from site rang it through" is not an approval; it is a story. The PO is where the story becomes a record &mdash; if the process can be bypassed with a phone call, you don't have a process, you have a memo nobody signed.</li>
<li><strong>The PO-after-invoice rubber stamp.</strong> Raising PO 2147 to "cover" an invoice that already arrived is paperwork theatre. It rewrites history and hides the very gap the number exists to expose. Late POs are honest; retroactive ones are lies with formatting.</li>
<li><strong>Number chaos.</strong> Two people issuing POs from two ranges, reused numbers, "quote #4-1b". One sequential series, one owner of the series, no reuse &mdash; ever.</li>
<li><strong>The threshold nobody respects.</strong> A $500 limit that a $499 order sails under twice a week isn't a control, it's an invitation. Watch the pattern of just-under orders the way you'd watch a till.</li>
<li><strong>Procurement theatre for a five-person shop.</strong> The opposite failure: twelve approval steps for a box of gloves. The whole process is one page, seven lines, one threshold. If it takes longer than the order itself, it will be abandoned by Christmas.</li>
</ul>

<h2>5. Worked example &mdash; the HVAC contractor's $9,400 nobody ordered</h2>
<p>A fourteen-person HVAC service company, $4.2M revenue, profitable every year &mdash; and a pattern the owner described as "the invoice ambush": spend committed by techs from the field, invoices landing at month-end for jobs the office had already priced and forgotten. The worst quarter carried $2,300 of genuinely unreconcilable supplier spend, and a $9,400 compressor ordered by phone during a heatwave week blew a hole in week 3 of the cash plan nobody knew was there until the statement arrived. The fix took one Sunday: the seven-line PO on a single printed page, a $500 threshold, standing POs for the four recurring suppliers, and the ten-minute unapproved-invoice list bolted onto the Monday cash hour. One quarter later: unreconcilable spend $0, the close two hours faster (every invoice arriving pre-coded to a job), and the forecast's outflow row finally describing reality, because every commitment entered the books the week it was made. The owner's verdict: <em>"I thought POs were for companies with procurement departments. It turns out they're for companies with utes."</em></p>

<h2>Kits</h2>
<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="supplier-payment-terms-checklist.html">supplier payment terms checklist</a> is the paying half of the same relationship &mdash; the PO locks the price, the terms govern the timing; the <a href="expense-reimbursement-policy.html">expense reimbursement policy</a> is the under-threshold sibling &mdash; card spend with its own three questions; the <a href="13-week-cash-flow-forecast.html">13-week cash flow forecast</a> is where approved commitments become known outflow rows instead of month-end surprises; the <a href="monthly-close-checklist.html">month-end close</a> is where the three-way match gets reconciled &mdash; PO-coded invoices close in half the time; and the <a href="upfront-deposit-checklist.html">upfront deposit checklist</a> is the same promise-number idea pointed the other way &mdash; money the customer commits before you start.</em></p>
</main>
</body>
</html>
'''
if not os.path.exists(PAGE):
    open(PAGE, 'w').write(html)

# 1) index.html - TOP card
card = ('<li><a href="' + PAGE + '">The Purchase Order Process for Small Teams: The Five-Minute '
        'Step That Stops the Surprise Invoice</a>'
        '<div class="desc">The seven-line PO (number, supplier, what and how much, agreed price and '
        'terms, job code, approver, date) sent before the money is committed; the $500 threshold that '
        'keeps the process out of the way of the $40 box of fittings; standing POs for recurring '
        'suppliers; the three-way match (PO, delivery, invoice) that kills duplicates, drift and '
        'phantoms; the weekly ten-minute unapproved-invoice list bolted onto the cash-forecast hour; '
        'and the five traps (verbal PO culture, the retroactive rubber stamp, number chaos, the '
        'threshold nobody respects, procurement theatre for a five-person shop). Worked example: the '
        'HVAC contractor whose $9,400 nobody-ordered compressor became the last surprise &mdash; '
        'unreconcilable spend $2,300/quarter to $0, and the close two hours faster.</div></li>')
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
    entry = ('- **NEW: [The Purchase Order Process for Small Teams (The Five-Minute Step That Stops '
             'the Surprise Invoice)](' + URL + ')** &mdash; the seven-line PO sent before the money is '
             'committed, the threshold that keeps it out of the way, standing POs for recurring suppliers, '
             'the three-way match that kills duplicate and phantom invoices, the weekly unapproved-invoice '
             'list, and the five traps. Worked example: the HVAC contractor\'s $9,400 compressor.\\n')
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
backlink('supplier-payment-terms-checklist.html',
    '<p><em>Related: terms govern when you pay; the <a href="' + URL + '">purchase order process</a> '
    'governs what you committed to before the invoice existed &mdash; the PO locks the price your terms '
    'then pay on.</em></p>\n')
backlink('expense-reimbursement-policy.html',
    '<p><em>Related: the <a href="' + URL + '">purchase order process</a> is the over-threshold sibling '
    'of the expense policy &mdash; card-first under the line, a numbered promise before the order above it.</em></p>\n')
backlink('13-week-cash-flow-forecast.html',
    '<p><em>Related: the <a href="' + URL + '">purchase order process</a> is why the forecast\'s outflow '
    'row can be believed &mdash; every commitment enters the books the week it is made, not the week the '
    'invoice ambushes you.</em></p>\n')
backlink('monthly-close-checklist.html',
    '<p><em>Related: invoices that arrive <a href="' + URL + '">PO-coded</a> close in half the time '
    '&mdash; the job code was decided in five minutes at order time, not reverse-engineered at month-end.</em></p>\n')

# 5) linkcheck
page = open(PAGE).read()
hrefs = re.findall(r'href="([^"#]+?\.html)"', page)
missing = [h for h in hrefs if not h.startswith('http') and not os.path.exists(h)]
assert not missing, 'broken relative links: %r' % missing

# 6) summary
n = open('sitemap.xml').read().count('<url>')
cards = open('index.html').read().count('<li><a href="')
print('OK build_239: sitemap urls=%d, index cards~%d, page %d bytes, 0 coupon=%s'
      % (n, cards, os.path.getsize(PAGE), 'HIVE20' not in page))
