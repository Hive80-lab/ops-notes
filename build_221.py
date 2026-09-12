#!/usr/bin/env python3
"""#221 negative-review-response-playbook.html - integrations.
Ran in /private/tmp/ops-notes after writing the page.
Pattern per build_220.py: index TOP card, sitemap newest-first, README line 1,
3 reciprocal backlinks (win-back, referral-request, no-show)."""
import re

PAGE = 'negative-review-response-playbook.html'
URL = 'https://hive80-lab.github.io/ops-notes/' + PAGE
TODAY = '2026-09-13'

# 1) index.html - new TOP card at start of the first ul
idx = open('index.html').read()
card = ('<li><a href="' + PAGE + '">Negative Review Response Playbook for Small Businesses: '
        'The 24-Hour Reply That Keeps the Next Customer</a> &mdash; the reply written for the '
        'next fifty readers, the 24-hour rule and who holds the pen, the fact-check before a '
        'single word is typed, the five-part reply anatomy (thank, acknowledge specific, own the '
        'fixable part, the offline move, the new-state line), what never goes in a public reply, '
        'the make-good ladder (fix, credit, refund) with the call-before-credit rule, flag-don&rsquo;t-fight '
        'for fake reviews, the theme log where the third mention becomes a policy fix, the '
        'delight-moment ask that buries a bad review with fresh ones, and the caf&eacute;&rsquo;s '
        'cold-flat-white worked example: zero discount, one process fix, one repeat customer.</li>')
anchor = '<ul><li><a href="staffing-shortage-coverage-plan.html">'
assert anchor in idx, 'index anchor missing'
idx = idx.replace(anchor, '<ul>' + card + '<li><a href="staffing-shortage-coverage-plan.html">', 1)
open('index.html', 'w').write(idx)

# 2) sitemap.xml - newest-first insert after <urlset...>
sm = open('sitemap.xml').read()
url = ('<url><loc>' + URL + '</loc><lastmod>' + TODAY + '</lastmod>'
       '<changefreq>weekly</changefreq><priority>0.8</priority></url>')
m = re.search(r'(<urlset[^>]*>)', sm)
sm = sm[:m.end()] + url + sm[m.end():]
open('sitemap.xml', 'w').write(sm)

# 3) README.md - new entry on line 1
readme = open('README.md').read()
entry = ('- **NEW: [Negative Review Response Playbook for Small Businesses (The 24-Hour Reply That Keeps the Next Customer)]('
         + URL + ')** &mdash; the reply written for the next fifty readers rather than the reviewer, the 24-hour rule and '
         'who holds the pen (the owner, never the named employee), the fact-check before a single word is typed '
         '(find the visit, hear the story, decide which of the three it is), the five-part reply anatomy (thank and '
         'acknowledge the specific, own the fixable part, the offline move with a named person, the new-state line, stop), '
         'what never goes in a public reply (the word fake, the receipt-by-receipt defense, the 11pm owner rant), the '
         'make-good ladder (fix, credit, refund) with the call-before-credit rule, flag-don&rsquo;t-fight for fake reviews, '
         'the theme log where the third mention becomes a Monday-huddle policy fix, the delight-moment ask with the '
         'two-tap QR that buries a bad review with fresh ones, and the worked example &mdash; a caf&eacute;&rsquo;s '
         'cold-flat-white two-star answered in four hours, fixed by the Monday huddle, and out-ranked by the '
         'reviewer&rsquo;s own four-star update two weeks later.\n')
open('README.md', 'w').write(entry + readme)

# 4) reciprocal backlinks
# 4a) win-back: append a sentence to its final closing paragraph
t = open('win-back-sequence-churned-customers.html').read()
ps = re.findall(r'<p>.*?</p>\s*</main>', t, re.S)
assert ps, 'win-back final <p> not found'
last = ps[-1]
sent = (' When the churn started with a public two-star, the <a href="https://hive80-lab.github.io/ops-notes/negative-review-response-playbook.html">'
        'negative review response playbook</a> runs the first 24 hours &mdash; and the phone call is the win-back.</p>')
t = t.replace(last[:last.rfind('</p>')], last[:last.rfind('</p>')] , 1)
# append inside the final paragraph before </main>
cut = t.rfind('</p>\n</main>')
assert cut != -1, 'win-back closing p not found'
t = t[:cut] + sent.rstrip('</p>'.replace('</p>','')) + t[cut:]
open('win-back-sequence-churned-customers.html', 'w').write(t)

# 4b) referral-request: insert a paragraph before </main>
t = open('referral-request-sequence.html').read()
add = ('\n<p>One referral source is hiding in the complaints folder: a two-star handled well. The '
       '<a href="https://hive80-lab.github.io/ops-notes/negative-review-response-playbook.html">negative review response playbook</a> '
       'turns the 24-hour reply and the owner&rsquo;s phone call into the kind of story customers repeat &mdash; '
       'and customers who felt heard refer.</p>\n</main>')
assert '</main>' in t, 'referral </main> missing'
t = t.replace('</main>', add, 1)
open('referral-request-sequence.html', 'w').write(t)

# 4c) no-show: insert a paragraph before </main>
t = open('no-show-reminder-sequence.html').read()
add = ('\n<p>Reminders also prevent the worst kind of review: the "waited twenty minutes for a table that never '
       'showed" two-star. The <a href="https://hive80-lab.github.io/ops-notes/negative-review-response-playbook.html">'
       'negative review response playbook</a> covers the reply when one still lands.</p>\n</main>')
assert '</main>' in t, 'no-show </main> missing'
t = t.replace('</main>', add, 1)
open('no-show-reminder-sequence.html', 'w').write(t)

print('integrations done')
