#!/usr/bin/env python3
# ops-notes #248 integrations: sitemap, index top card (+dedupe defect), README (+\n defect fix), 5 reciprocal backlinks
import re, sys

D = '/Users/haroonqamer/Swarm/hive/state/seo/ops-notes/'
URL = 'https://hive80-lab.github.io/ops-notes/critical-spare-parts-list.html'
DATE = '2026-09-13'
ok = []

# 1) sitemap: prepend new url (newest-first)
s = open(D+'sitemap.xml').read()
if 'critical-spare-parts-list.html' not in s:
    entry = f'<url><loc>{URL}</loc><lastmod>{DATE}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
    i = s.index('<url>')
    s = s[:i] + entry + s[i:]
    open(D+'sitemap.xml','w').write(s)
n = len(re.findall(r'<url>', open(D+'sitemap.xml').read()))
ok.append(f'sitemap urls={n}')

# 2) index.html: dedupe duplicated supplier card, then insert new top card
h = open(D+'index.html').read()
sup = h.count('<li><a href="supplier-concentration-risk.html">')
if sup >= 2:
    first = h.index('<li><a href="supplier-concentration-risk.html">')
    # find the end of the first card (</li> after it) then check if an identical card follows
    end1 = h.index('</li>', first) + 5
    if h[end1:end1+50].startswith('<li><a href="supplier-concentration-risk.html">'):
        end2 = h.index('</li>', end1) + 5
        if h[first:end1] == h[end1:end2]:
            h = h[:end1] + h[end2:]
            ok.append('index dedupe supplier card')
new_card = ('<li><a href="critical-spare-parts-list.html">The Critical Spare Parts List: The Shelf That Turns a Breakdown Into an Annoyance</a>'
'<div class="desc">Five columns built from the maintenance log in an afternoon &mdash; part (named as the floor names it, with the manufacturer part number), what it gates behind the machine, source and real lead time, shelf quantity with a two-bin reorder point, last used &mdash; the 48-hour rule that decides what belongs on the shelf, and the annual kill list that frees the dead stock. Worked example: the twelve-person CNC shop whose $340 servo drive answered an eleven-day OEM lead time mid-way through a $180k aerospace lot &mdash; dark machine to spindle turning in forty minutes, fiche and parameter backup in the same drawer.</div></li>')
if 'critical-spare-parts-list.html' not in h:
    i = h.index('<h1>Ops notes</h1>')
    j = h.index('<li>', i)
    h = h[:j] + new_card + h[j:]
    open(D+'index.html','w').write(h)
    ok.append('index top card added')
sup2 = open(D+'index.html').read().count('<li><a href="supplier-concentration-risk.html">')
ok.append(f'supplier cards now={sup2}')

# 3) README: fix literal \n defect, prepend new NEW line
r = open(D+'README.md').read()
if '\\n- **NEW:' in r:
    r = r.replace('\\n- **NEW:', '\n- **NEW:', 1)
    ok.append('README literal-nl fixed')
new_line = ('- **NEW: [The Critical Spare Parts List: The Shelf That Turns a Breakdown Into an Annoyance]('+URL+')** &mdash; '
 'five columns from the maintenance log (part + manufacturer part number, what it gates, source and real lead time, two-bin reorder point, last used); '
 'the 48-hour rule for what belongs on the shelf, and the annual kill list that frees dead stock. Worked example: the twelve-person CNC shop whose $340 servo drive '
 'answered an eleven-day OEM lead mid-way through a $180k lot &mdash; dark machine to spindle turning in forty minutes.\n')
if 'critical-spare-parts-list' not in r:
    open(D+'README.md','w').write(new_line + r)
    ok.append('README NEW prepended')

# 4) reciprocal backlinks x5
def append_related(path, sentence):
    t = open(D+path).read()
    if 'critical-spare-parts-list.html' in t:
        return path + ': already'
    m = re.search(r'<p><em>Related:[^<]*(?:<(?!/em>)[^>]*>[^<]*)*?', t)
    # simpler: find first line containing '<p><em>Related'
    lines = t.split('\n')
    for k, ln in enumerate(lines):
        if '<p><em>Related' in ln:
            if '</em></p>' in ln:
                lines[k] = ln.replace('</em></p>', sentence + '</em></p>', 1)
                open(D+path,'w').write('\n'.join(lines))
                return path + ': linked'
            else:
                return path + ': NO </em></p> on related line'
    return path + ': no related line'

res = []
res.append(append_related('preventive-maintenance-schedule-template.html',
 ' the <a href="critical-spare-parts-list.html">critical spare parts list</a> is what the parts line points at &mdash; the shelf that turns the breakdown you scheduled around into a forty-minute Tuesday.'))
res.append(append_related('supplier-concentration-risk.html',
 ' the <a href="critical-spare-parts-list.html">critical spare parts list</a> is the buy-side hedge for the parts you chose to keep close instead of dual-sourcing.'))
res.append(append_related('asset-inventory-checklist.html',
 ' The <a href="critical-spare-parts-list.html">critical spare parts list</a> is the same ranking pointed at the shelf behind each asset &mdash; what it gates, how long the lead really is, and when to reorder.'))
res.append(append_related('vendor-outage-runbook.html',
 ' the <a href="critical-spare-parts-list.html">critical spare parts list</a> is what the shelf holds before the outage &mdash; the parts whose real lead time is longer than your downtime tolerance.'))
res.append(append_related('hot-spare-loaner-laptop-checklist.html', ''))
if res[-1].endswith('linked') or res[-1].endswith('already'):
    pass
ok += res

# hot-spare page uses <ul> list format -> add <li>
t = open(D+'hot-spare-loaner-laptop-checklist.html').read()
if 'critical-spare-parts-list.html' not in t:
    anchor = '<li><a href="it-asset-inventory-template.html">IT Asset Inventory Template</a> &mdash; the spare row with a readiness date.</li>'
    if anchor in t:
        t = t.replace(anchor, anchor + '\n<li><a href="critical-spare-parts-list.html">Critical Spare Parts List</a> &mdash; the same shelf logic for the machines that pay the rent.</li>', 1)
        open(D+'hot-spare-loaner-laptop-checklist.html','w').write(t)
        ok.append('hot-spare: linked')

print('\n'.join(ok))
