import re, sys
from pathlib import Path

R = Path("/tmp/ops-notes")
SLUG = "expansion-revenue-playbook"
URL = "https://hive80-lab.github.io/ops-notes/" + SLUG + ".html"
TODAY = "2026-09-22"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Expansion revenue playbook: growth that starts with accounts you already have | HIVE80 Lab Ops Notes</title>
<meta name="description" content="An expansion revenue playbook for small teams: five listening posts you already have, a trigger-to-offer ladder with price framing, four rules for raising the conversation, the guardrails that keep it from dying, a worked quarter with numbers, and the five metrics that tell you it is working.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/expansion-revenue-playbook.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Expansion revenue playbook: growth that starts with accounts you already have</h1>
<p><em>Filed under client lifecycle &middot; pairs with the <a href="client-onboarding-checklist.html">onboarding checklist</a> and the <a href="retainer-renewal-checklist.html">renewal checklist</a></em></p>
<p>Every small studio's growth plan has the same flaw: it is a list of new logos. New logos are the most expensive revenue there is &mdash; cold outreach, discovery calls, proposals, and a win rate that hovers near one in four. Meanwhile the six accounts already paying you sit there with problems you have never asked about. Expansion revenue is the only growth line where you already know the client, they already know your work, and nobody has to be persuaded that you exist. This playbook makes it systematic instead of accidental.</p>

<h2>1. Why expansion is the only growth line you control this quarter</h2>
<p>Pipeline math, not philosophy:</p>
<table>
<tr><th></th><th>New logo</th><th>Expansion</th></tr>
<tr><td>Contact quality</td><td>Cold; you compete with their incumbent</td><td>You are the incumbent</td></tr>
<tr><td>Cost to first conversation</td><td>Dozens of touches, weeks of chasing</td><td>One email referencing their own data</td></tr>
<tr><td>Trust at the table</td><td>None &mdash; you are a claim on a webpage</td><td>Earned; the last invoice is your reference</td></tr>
<tr><td>Typical close rate</td><td>20&ndash;30%</td><td>50&ndash;70% when the offer answers a real signal</td></tr>
<tr><td>Time to revenue</td><td>6&ndash;12 weeks</td><td>Same month</td></tr>
</table>
<p>The catch: expansion revenue cannot be blasted. It is earned signal by signal, account by account, and it dies from one clumsy pitch. That is why it is a playbook and not a sales target shouted at the team.</p>

<h2>2. The signal inventory: five listening posts you already have</h2>
<p>You do not need new tooling. You need a monthly hour where someone reads what already exists:</p>
<ul>
<li><strong>Usage and scope signals in the work itself.</strong> Their ticket volume, the pages they asked you to touch, the templates they reuse. A client who asked for landing pages twice this quarter is a client with a landing-page habit you can formalize.</li>
<li><strong>Support inbox themes.</strong> Three "quick questions" about the same topic is a training day wearing a trench coat. Log recurring topics; the theme that repeats is the offer.</li>
<li><strong>Invoice drift.</strong> Their bill to you is flat but their business is visibly growing &mdash; new locations, new hires on their team, more traffic. Flat scope against a growing business means unmet demand, and unmet demand is someone else's prospecting call unless you make it yours.</li>
<li><strong>Stakeholder changes.</strong> A new manager or director inherits you and does not know you. That is not just a risk &mdash; it is the best-paid conversation of the quarter: a paid re-onboarding workshop (see the <a href="client-onboarding-checklist.html">onboarding checklist</a>) re-establishes scope, success numbers, and rhythm with a fresh budget-holder.</li>
<li><strong>Silence with growth.</strong> A quiet account whose business is booming is DIY-ing something you could be doing. Quiet is a signal, not a comfort.</li>
</ul>

<h2>3. The expansion ladder: match the offer to the trigger</h2>
<table>
<tr><th>Trigger (signal)</th><th>Expansion move</th><th>How the price is framed</th><th>Timing</th></tr>
<tr><td>Recurring support theme</td><td>Paid training day or a written playbook for their team</td><td>Fixed-fee day, itemized &mdash; never "we'll figure it out"</td><td>Within 2 weeks of the third occurrence</td></tr>
<tr><td>Scope creep tolerated twice</td><td>Convert the drift into a formal add-on via the <a href="change-order-request-template.html">change-order path</a></td><td>Retro-priced as what it already cost you, forward-priced as a retainer line</td><td>At the next check-in, not mid-sprint</td></tr>
<tr><td>Stakeholder change</td><td>Paid re-onboarding workshop</td><td>Half-day rate; framed as "bringing your new lead up to speed"</td><td>Within 2 weeks of the announcement</td></tr>
<tr><td>Visible business growth</td><td>Tier up the retainer (more scope, more cadence)</td><td>Two named tiers with the delta spelled out &mdash; they choose</td><td>Aligned to the <a href="retainer-renewal-checklist.html">renewal runway</a>, 60&ndash;90 days out</td></tr>
<tr><td>Adjacent problem you already solve</td><td>Cross-sell a second engagement line</td><td>Pilot: one fixed-scope project, priced to stand alone</td><td>After a win you can point to on their account</td></tr>
</table>
<p>The rule underneath the table: the offer must be triggered by <em>their</em> data, never by <em>your</em> quota. "We noticed your team filed nine requests about email deliverability" sells. "Do you want to buy more from us?" never does.</p>

<h2>4. The conversation: four rules for raising it</h2>
<ul>
<li><strong>Attach to value, not to the invoice.</strong> The sentence order is: observation from their data &rarr; the outcome it points at &rarr; the offer. "Your team's filed nine email deliverability requests this quarter &mdash; that's a pattern, not luck. We run a one-day deliverability clinic that typically cuts those tickets by half; it's a fixed $1,500. Want the agenda?" Value first makes the price a detail instead of a verdict.</li>
<li><strong>One expansion per conversation.</strong> Naming three offers makes you a vendor reading a menu; naming one makes you a specialist who noticed something. Keep the other two in your back pocket &mdash; they are the follow-up if the first lands.</li>
<li><strong>Make it decidable, not ignorable.</strong> Every offer ships with a scope line, a price, a start date, and what it does <em>not</em> include. Vague offers get "sounds good, let's circle back" &mdash; the polite graveyard.</li>
<li><strong>Price it at list.</strong> Expansion is the one sale where the client already believes your work is worth paying for. Discounting here trains them that every conversation ends in a haircut &mdash; and it cheapens every future renewal (see the <a href="price-increase-notice-template.html">price increase notice</a>).</li>
</ul>

<h2>5. The guardrails: four ways expansion dies</h2>
<ul>
<li><strong>Never expand mid-incident.</strong> During their outage or your <a href="client-offboarding-checklist.html">worst week</a>, the relationship is defensive; the pitch lands as opportunism. Expansion conversations belong in calm weeks and check-ins.</li>
<li><strong>Never bundle silently.</strong> An add-on slipped into the next invoice reads as a billing error and poisons trust &mdash; and can turn into a <a href="chargeback-dispute-response.html">dispute</a>. Every expansion is a separate, named line the client approved in writing.</li>
<li><strong>Never let an expansion become a favor.</strong> "We'll just absorb it for now" is how unpaid overtime is born. If it is real work, it is a real line item &mdash; that is what the change-order template exists for.</li>
<li><strong>Never run more than one conversation per account per quarter.</strong> Expansion is farming. A client who hears a pitch every fortnight stops opening your emails, and then you have burned the listening posts too.</li>
</ul>

<h2>6. Worked example: a six-client studio, one quarter</h2>
<p>A six-retainer studio, A$18,400 MRR, no new-business person on payroll. The monthly signal hour found: one account filing repeated email-deliverability questions, one client that announced a new marketing lead, one whose scope had drifted two months running, and one whose silence coincided with a funding announcement.</p>
<ul>
<li>Deliverability clinic, fixed fee: <strong>+A$1,500</strong> (one-off) &mdash; closed on the third "quick question" about the same topic.</li>
<li>Re-onboarding workshop for the new lead: <strong>+A$1,800</strong> (one-off) &mdash; booked within ten days of the announcement.</li>
<li>Drift formalized into a retainer line: <strong>+A$900/month</strong> via change order.</li>
<li>Funded client: tier-up quoted at renewal runway, closed the following quarter &mdash; not forced early.</li>
</ul>
<p>Quarter total: <strong>A$6,300 expansion revenue, zero new logos, one discount given</strong> (workshop bundle price, decided in advance, not negotiated in panic). The tier-up conversation is already scheduled &mdash; because the renewal conversation and the expansion conversation are the same conversation held at the right time.</p>

<h2>7. Five numbers that tell you if this is working</h2>
<ul>
<li><strong>Signal-hour completion:</strong> did the monthly listening hour actually happen? (Target: 12 of 12 months. It is the whole engine.)</li>
<li><strong>Offers raised:</strong> expansion conversations started per quarter &mdash; target at least one per account, evidence-first.</li>
<li><strong>Signal-to-offer rate:</strong> of the signals logged, how many became a concrete offer? (Target &ge;50%; below that you are listening and then flinching.)</li>
<li><strong>Expansion revenue share:</strong> expansion &divide; total revenue this quarter. (Target 20&ndash;30% before any new-logo marketing spend.)</li>
<li><strong>Net revenue retention:</strong> (this quarter's revenue from last quarter's accounts) &divide; (last quarter's revenue). (Target &ge;100%; 110%+ means the base compounds on its own.)</li>
</ul>

<h2>Where this fits</h2>
<p>Expansion sits at the profitable end of the lifecycle this site documents: the <a href="client-onboarding-checklist.html">client onboarding checklist</a> creates the first win that makes expansion pitchable, the <a href="retainer-renewal-checklist.html">retainer renewal checklist</a> carries the value story to the tier-up conversation, the <a href="quote-follow-up-sequence.html">quote follow-up sequence</a> closes the expansion quote like any other quote, and &mdash; when an account is truly gone &mdash; the <a href="win-back-sequence-churned-customers.html">win-back sequence</a> is the expansion playbook's last stand.</p>

<h2>This playbook is part of the kit line</h2>
<p>This playbook is part of the <strong>Hive80 Lab ops kit line</strong> &mdash; field-tested, instantly downloadable:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start</li>
<li><a href="https://hive80lab.gumroad.com/l/rtodsv">Ops Field Cards</a> &mdash; 12 printable incident checklists &mdash; $4</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; full incident-response kit for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $29</li>
</ul>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
"""

(R / f"{SLUG}.html").write_text(PAGE)
print(f"page written: {SLUG}.html ({len(PAGE)} bytes)")

# ---------------------------------------------------------------- reciprocals
RECIP = {
 "client-onboarding-checklist.html":
   ('<h2>This checklist is part of the kit line',
    '<p>Onboarding is also the doorway to growth: a client whose first 30 days produced defined success numbers and a visible win is the easiest account to expand &mdash; the <a href="expansion-revenue-playbook.html">expansion revenue playbook</a> turns that first win into tier-ups, add-ons, and second engagement lines.</p>\n'),
 "retainer-renewal-checklist.html":
   ('<h2>This checklist is part of the kit line',
    '<p>Renewal and expansion are the same conversation at different altitudes: the <a href="expansion-revenue-playbook.html">expansion revenue playbook</a> matches offers to signals (scope drift, stakeholder changes, support themes) so the tier-up at renewal is a continuation, not a cold pitch.</p>\n'),
 "win-back-sequence-churned-customers.html":
   ('</main>',
    '<p>The best win-back is often a re-entry with better terms: the <a href="expansion-revenue-playbook.html">expansion revenue playbook</a> applies to lapsed accounts too &mdash; lead with what changed in <em>their</em> business since the exit, not with your price list.</p>\n'),
}

for fname, (anchor, block) in RECIP.items():
    p = R / fname
    t = p.read_text()
    if SLUG in t:
        print(f"recip {fname}: already linked, skip"); continue
    if anchor not in t:
        print(f"recip {fname}: anchor NOT FOUND: {anchor[:40]}"); continue
    t = t.replace(anchor, block + anchor, 1)
    p.write_text(t)
    print(f"recip {fname}: injected")

# ---------------------------------------------------------------- sitemap
import xml.dom.minidom as minidom
sp = R / "sitemap.xml"
s = sp.read_text()
entry = f'<url><loc>{URL}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
if URL not in s:
    s = s.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + entry, 1)
    sp.write_text(s)
minidom.parseString(sp.read_text())
n = sp.read_text().count("<loc>")
print(f"sitemap XML-valid, {n} urls, newest-first ok={sp.read_text().split('<url>')[1].count(SLUG)==1}")

# ---------------------------------------------------------------- index card
CARD = ('<li><a href="expansion-revenue-playbook.html">Expansion Revenue Playbook '
 '(Growth That Starts With Accounts You Already Have)</a><div class="desc">New logos are the '
 'most expensive revenue there is; the accounts already paying you are the cheapest. The five '
 'listening posts you already own (work-usage signals, support-inbox themes, invoice drift, '
 'stakeholder changes, silence with growth), a trigger-to-offer ladder with price framing and '
 'timing, four rules for raising the conversation (attach to value, one offer per conversation, '
 'make it decidable, price at list), the four guardrails (never mid-incident, never bundle '
 'silently, never a favor, one conversation per account per quarter), a worked quarter with '
 'A$6,300 expansion on zero new logos, and the five numbers that tell you it is working '
 '(signal-hour completion, offers raised, signal-to-offer rate, expansion share, net revenue '
 'retention).</div></li>')
ip = R / "index.html"
i = ip.read_text()
if SLUG not in i:
    i = i.replace('<ul>\n<li><a href="client-onboarding-checklist.html"',
                  '<ul>\n' + CARD + '\n<li><a href="client-onboarding-checklist.html"', 1)
    ip.write_text(i)
i2 = ip.read_text()
pos = i2.find(SLUG); first_card = i2.find('<li><a href="')
print(f"index: TOP card order ok={0 < pos - first_card < 500}")

# ---------------------------------------------------------------- README
rp = R / "README.md"
r = rp.read_text()
line = ('- **NEW: [Expansion Revenue Playbook (Growth That Starts With Accounts You Already Have)]'
 '(https://hive80-lab.github.io/ops-notes/expansion-revenue-playbook.html)** \u2014 new logos are the '
 'most expensive revenue; this playbook works the accounts you already have: five listening posts you '
 'already own, a trigger-to-offer ladder (support themes \u2192 training day, drift \u2192 change order, '
 'stakeholder change \u2192 paid re-onboarding, growth \u2192 tier-up, silence \u2192 audit), four rules '
 'for raising it (attach to value, one offer per conversation, decidable scope, list price), four '
 'guardrails, a worked quarter (A$6,300 expansion, zero new logos), and five metrics including net '
 'revenue retention.\n')
if SLUG not in r:
    anchor = r.index("- **NEW:")
    r = r[:anchor] + line + r[anchor:]
    rp.write_text(r)
first_new = [l for l in (R/"README.md").read_text().splitlines() if l.startswith("- **NEW")][0]
print("README top:", first_new[:70])

# ---------------------------------------------------------------- linkcheck
broken = 0; checked = 0
for f in sorted(R.glob("*.html")):
    t = f.read_text()
    for href in re.findall(r'href="([^"#]+\.html)"', t):
        checked += 1
        if not (R / href).exists():
            broken += 1; print(f"  BROKEN in {f.name}: {href}")
print(f"linkcheck: {checked} internal links, {broken} broken")
sys.exit(1 if broken else 0)