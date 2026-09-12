#!/usr/bin/env python3
"""#222 google-business-profile-optimization-checklist.html - integrations.
Ran in /private/tmp/ops-notes after writing the page.
Pattern per build_221.py: index TOP card, sitemap newest-first, README line 1,
3 reciprocal backlinks (negative-review-response-playbook, reopening-notice-template,
store-closure-temporary-notice)."""
import re

PAGE = 'google-business-profile-optimization-checklist.html'
URL = 'https://hive80-lab.github.io/ops-notes/' + PAGE
TODAY = '2026-09-16'

# 1) index.html - TOP card (push previous top card down)
idx = open('index.html').read()
card = ('<li><a href="' + PAGE + '">Google Business Profile Optimization Checklist for Small Businesses: '
        'The Free Storefront Most Owners Leave Half-Open</a> &mdash; why the profile is the storefront where '
        'first-time customers actually arrive, the one-time setup most owners never finish (claim and verify, '
        'hunt duplicates, hide the address for true service-area businesses), the three fields that decide '
        'whether you exist (real-world name, the category of the money, the attributes people filter by), '
        'the hours discipline that stops the &ldquo;Google said you were open&rdquo; one-star factory, the photo '
        'freshness rule, owner-seeded questions and answers, the weekly post with a one-week shelf life, '
        'shelves with prices, the booking and messaging rails, the review loop, the four Insights numbers '
        'that tell you what to fix, the traps that get profiles suspended, the weekly ten-minute routine, '
        'and the worked example &mdash; a mobile dog groomer whose direction-request map showed her the two '
        'suburbs she&rsquo;d been treating as too far to bother.</li>')
anchor = '<ul><li><a href="negative-review-response-playbook.html">'
assert anchor in idx, 'index anchor missing'
idx = idx.replace(anchor, '<ul>' + card + '<li><a href="negative-review-response-playbook.html">', 1)
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
entry = ('- **NEW: [Google Business Profile Optimization Checklist for Small Businesses (The Free Storefront '
         'Most Owners Leave Half-Open)](' + URL + ')** &mdash; why the profile is the storefront where '
         'first-time customers actually arrive, the one-time setup most owners never finish (claim and verify, '
         'hunt duplicate listings, hide the address for true service-area businesses), the three fields that '
         'decide whether you exist (the real-world name, the category of the money, the attributes people '
         'filter by), the hours discipline that stops the &ldquo;Google said you were open&rdquo; one-star, '
         'the monthly photo freshness rule, owner-seeded questions and answers, the weekly post with a '
         'one-week shelf life, shelves with prices, the booking and messaging rails, the review loop, the '
         'four Insights numbers that tell you what to fix (calls, direction requests, website clicks, top '
         'search terms), the traps that get profiles suspended, the weekly ten-minute routine, and the '
         'worked example &mdash; a mobile dog groomer whose direction-request map showed her the two suburbs '
         'she&rsquo;d been treating as too far to bother.\\n')
open('README.md', 'w').write(entry + readme)

# 4) reciprocal backlinks
# 4a) negative-review-response-playbook: extend the final Related paragraph
t = open('negative-review-response-playbook.html').read()
assert PAGE not in t, 'already linked'
old = '"waited twenty minutes."</em></p>\n</main>'
assert old in t, 'nrp related para anchor missing'
new = ('"waited twenty minutes." The profile those reviews live on gets its own checklist: the '
       '<a href="' + URL + '">Google Business Profile optimization checklist</a> finishes the storefront '
       '&mdash; hours, photos, Q&amp;A, posts &mdash; so the stars land on a page worth landing on.</em></p>\n</main>')
t = t.replace(old, new, 1)
open('negative-review-response-playbook.html', 'w').write(t)

# 4b) reopening-notice-template: insert paragraph before </main>
t = open('reopening-notice-template.html').read()
assert '</main>' in t, 'reopen </main> missing'
add = ('\n<p>While the notice is out, update the storefront itself: the <a href="' + URL + '">'
       'Google Business Profile optimization checklist</a> covers the special-hours discipline &mdash; '
       'set them before the holiday, clear them the morning you reopen, and the &ldquo;Google said you '
       'were open&rdquo; one-star never happens.</p>\n</main>')
t = t.replace('</main>', add, 1)
open('reopening-notice-template.html', 'w').write(t)

# 4c) store-closure-temporary-notice: insert paragraph before </main>
t = open('store-closure-temporary-notice.html').read()
assert '</main>' in t, 'closure </main> missing'
add = ('\n<p>The same day the notice goes up, flip the profile: the <a href="' + URL + '">'
       'Google Business Profile optimization checklist</a> covers the temporarily-closed flag &mdash; '
       'set it for the flood, take it off the day the doors open, and never leave the fuse blown.</p>\n</main>')
t = t.replace('</main>', add, 1)
open('store-closure-temporary-notice.html', 'w').write(t)

print('integrations done')
