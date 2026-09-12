#!/usr/bin/env python3
"""Build ops-notes page #164: client-onboarding-checklist.html + rail updates."""
import re, sys
from pathlib import Path

R = Path("/tmp/ops-notes")
BASE = "https://hive80-lab.github.io/ops-notes"
SLUG = "client-onboarding-checklist"
URL = f"{BASE}/{SLUG}.html"
TODAY = "2026-09-22"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Client Onboarding Checklist for Small Teams (The First 14 Days That Decide the Renewal) &mdash; HIVE80lab</title>
<meta name="description" content="A client onboarding checklist for agencies and consultancies: the 48-hour welcome window, the kickoff call that puts scope and success on the record, the one-page expectations contract, the first win shipped on the client's own data inside ten business days, the 30-day value checkpoint that seeds the renewal, and the five weekly numbers. Worked example: scope-confusion tickets down 70%, ten of eleven renewals signed, one expansion the client proposed.">
<link rel="canonical" href="{URL}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>
<h1>Client onboarding checklist: the first 14 days that decide the renewal</h1>
<p>A client decides whether an engagement is going well in the first two weeks &mdash; before the real work has had time to prove anything. What they judge is not the deliverable (it isn't finished yet); it's the experience: did anyone own us, did anything happen fast, do we know what's next, does this team keep promises. Onboarding is therefore the first renewal conversation, held months before the <a href="retainer-renewal-checklist.html">renewal runway opens</a>. This checklist is the service-business version &mdash; agencies, consultancies, freelancers with named clients; for product teams onboarding SaaS users, the <a href="customer-onboarding-first-30-days-checklist.html">first-30-days customer onboarding checklist</a> covers that side. The mirror image &mdash; ending a client relationship well &mdash; lives in the <a href="client-offboarding-checklist.html">client offboarding checklist</a>, and the two are one system: clients onboarded cleanly are easy to offboard cleanly.</p>

<h2>1. One internal owner, one client-facing owner, written down</h2>
<p>Every bad onboarding starts the same way: the client emails three people and gets three tones. The first line of the checklist is ownership &mdash; not the org chart, the two names.</p>
<ul>
<li><strong>The internal owner is one person, always.</strong> Not "the team," not "whoever's free." One named person is accountable for this client's first 14 days: the welcome email, the kickoff call, the first win. If that person is on leave the week the client signs, the onboarding is rescheduled, not delegated-by-default to nobody.</li>
<li><strong>The client-facing owner is named in writing, to the client.</strong> "From today, [name] is your main point of contact &mdash; anything at all, that's the address." The client should never have to wonder who to write to; a client who wonders writes to the founder, and the founder becomes the bottleneck they were paying you to remove.</li>
<li><strong>The handover from sales to delivery is a message, not a mood.</strong> Whoever closed the sale writes one paragraph to the delivery owner: what the client bought, the three things they said they cared about, any promises made in the sale. Half of scope friction is a promise made in the sale that delivery never heard about; the paragraph costs two minutes and prevents the first conflict before it exists.</li>
<li><strong>Nothing starts until the money clears or the contract is signed &mdash; pick one, in advance.</strong> The most common onboarding failure in small shops is starting work "pending paperwork" and then chasing paperwork for three weeks alongside delivery. The <a href="upfront-deposit-policy.html">upfront deposit policy</a> exists precisely so this line is already answered: deposits clear before kickoff, so kickoff is delivery, not invoicing.</li>
</ul>

<h2>2. The 48-hour welcome window</h2>
<p>Between signature and first call there is a gap, and clients fill gaps with anxiety. The welcome window is everything that happens in the first 48 hours after the contract lands &mdash; before any work is due, before the kickoff, while the client's decision still feels like a good idea.</p>
<ul>
<li><strong>The day-0 email answers four questions:</strong> what happens next (the kickoff, with a date), who your contact is (the named owner), what we need from you before then (one item, never a questionnaire), and one question worth replying to. The question is reply-bait &mdash; "which part of this matters most to your team this quarter?" &mdash; because a reply converts the client from audience to participant, and the answer seeds the kickoff.</li>
<li><strong>One item, not a questionnaire.</strong> The 40-question onboarding form is where enthusiasm goes to die: a client who opens a spreadsheet of homework on day 0 has bought a job, not a service. One artifact per 48 hours. The deep discovery belongs to the <a href="discovery-call-checklist.html">discovery call</a>, which already happened; onboarding reuses its answers, it doesn't re-ask them.</li>
<li><strong>Calendar holds go out with the welcome email.</strong> The kickoff is booked, and the standing check-in slot is proposed in the same message &mdash; with the cadence the engagement implies (weekly for projects, fortnightly for retainers). Asking for calendar time in week 1 is easy; in week 5 it's friction. The standing slot also feeds the <a href="no-show-reminder-sequence.html">no-show reminder ladder</a> from day one, so the first missed call is an event, not a surprise.</li>
<li><strong>The welcome one-pager, not a portal.</strong> One page: who we are on this account, what the first two weeks look like, how to reach us, how and when invoices arrive. Portals are software projects; a one-pager is a PDF the client actually reads on their phone between meetings.</li>
</ul>

<h2>3. The kickoff call: thirty minutes, on the record</h2>
<p>The kickoff is not a meet-and-greet; it is where scope, success, and rhythm get said out loud with every stakeholder in the room. Thirty minutes, agenda sent the day before, notes sent within two hours after.</p>
<ul>
<li><strong>Success is defined as three numbers, in the client's words.</strong> "What does this look like when it's working?" The answer becomes the engagement's north star &mdash; and the raw material for the <a href="retainer-renewal-checklist.html">value memo at renewal</a>. A client who hears their own numbers repeated back in week 1 hears them quoted back in month 11 with a sense of recognition; a client who never defined success grades you on vibes.</li>
<li><strong>Scope is restated in your words, not quoted from the SOW.</strong> "So we're building the migration and the two landing pages; the email platform migration itself is your team's, and we advise on it." SOWs are skimmed; a spoken paragraph with a pause for correction is where scope mismatches surface &mdash; now, when they're a sentence, not in month 3, when they're a conflict.</li>
<li><strong>The who-does-what grid gets filled on the call.</strong> Four columns: item, us, you, decision needed by. Clients who know their homework deliver it; clients who don't, don't, and then the delay is "communication problems."</li>
<li><strong>The rhythm is agreed, not proposed:</strong> check-in day and time, what lands in it (progress, blockers, decisions needed), and the response-time expectation between meetings. The expectations conversation belongs in the kickoff &mdash; it's the cheapest moment it will ever have.</li>
</ul>

<h2>4. The expectations contract: one page, week one</h2>
<p>Between the signed SOW and the client's actual experience sits a layer of unstated rules: how fast you reply, how revisions work, what counts as an emergency. Making them stated is the single highest-leverage hour of onboarding.</p>
<ul>
<li><strong>Response times and channels are named.</strong> "We reply to email within one business day; Slack within four working hours; anything truly urgent, the phone number below." Without a named channel for urgent, every email is potentially urgent, and the client learns to escalate everything.</li>
<li><strong>Revisions have a number and a clock.</strong> Two rounds included, five business days per round of client review, and what happens after (the <a href="change-order-request-template.html">change-order path</a>). This is the paragraph that makes the project profitable; unwritten, it is also the paragraph that makes the engagement unpaid overtime.</li>
<li><strong>The invoice schedule is stated in week 1, by a human, in the same breath as the work.</strong> "Invoices go out on the 1st, net 14, chased by reminder on day 7" &mdash; said before the first invoice, the <a href="failed-payment-dunning-sequence.html">dunning ladder</a> reads as the system you promised, not a hostile surprise.</li>
<li><strong>One page, confirmed in writing, referenced forever.</strong> "As agreed in the onboarding notes of the 14th" becomes the gentlest and strongest sentence in client management. You are no longer enforcing your preference; you're both following the thing you co-signed.</li>
</ul>

<h2>5. The first win on their data, inside ten business days</h2>
<p>The first two weeks need one visible, specific deliverable &mdash; small, real, and on the client's own data. Not the strategy deck, not the audit, not "settling in." A thing they can show their boss.</p>
<ul>
<li><strong>Ship something small before you build the big thing.</strong> A cleaned-up page, a fixed workflow, a report in their template, a working draft of the thing they're most nervous about. A small win on day 8 buys the patience a big deliverable needs on day 40; silence for four weeks buys the meeting where they ask whether this was a good idea.</li>
<li><strong>The first win is chosen for visibility, not effort.</strong> Ask in the kickoff: "what's the one thing your boss will ask about first?" Ship a version of that. An internal migration that saves hours but is invisible loses week 2; a one-page before/after that the boss can see wins the quarter.</li>
<li><strong>Deliver it in their format, in their channel.</strong> The win arrives where the client's team already reads &mdash; their deck template, their meeting, their subject-line conventions. Borrowed formats read as vendor work; native formats read as team output.</li>
<li><strong>Say out loud that it's the first of the plan.</strong> "First of the three numbers we set &mdash; here's what's next." One early win that is explicitly framed as step one of the agreed plan converts a happy moment into momentum; the same win unframed is just a nice email.</li>
</ul>

<h2>6. The 30-day checkpoint: the value memo, seeded early</h2>
<p>Day 30 is a short, scheduled, written checkpoint &mdash; not a meeting if it can be a memo. It is also where the renewal is quietly won: the <a href="retainer-renewal-checklist.html">renewal value memo</a> that lands at day -45 is only strong if its first draft was written at day 30.</p>
<ul>
<li><strong>Three numbers, one prevented list, one next paragraph.</strong> The same shape as the renewal memo, miniature: the two or three outcomes so far (even early ones), the things that were caught before they cost money ("the DNS conflict that would have taken the site down Tuesday"), and one honest paragraph of what the next month is for.</li>
<li><strong>The checkpoint is where scope drift gets named, gently, with a receipt.</strong> "Two items this month sat outside the original scope &mdash; we did them this once; here's the path for the next ones." Naming drift at day 30 with one freebie behind it is generous; discovering drift at day 90 is an argument.</li>
<li><strong>A one-question pulse, in the same email:</strong> "one thing we should start, one we should stop?" The answer arrives while the engagement is still malleable &mdash; and the client who was asked at day 30 rarely needs a survey at month 6.</li>
<li><strong>The checkpoint closes with dates, not thanks.</strong> Next deliverable, next check-in, next invoice. Endings with dates read as management; endings with gratitude alone read as endings.</li>
</ul>

<h2>7. The onboarding file and the five weekly numbers</h2>
<p>Onboarding is managed like a pipeline, not a vibe: one row per new client, reviewed in the same weekly block as sales and the <a href="quote-follow-up-sequence.html">quote follow-up ladder</a>.</p>
<ul>
<li><strong>The row has six columns:</strong> client, signed date, day-0 email sent (yes/no), kickoff held (yes/no), first win shipped (date), day-30 checkpoint (date). A client sitting with three empty columns at week 3 is not "going fine"; it is the renewal risk you can still fix.</li>
<li><strong>Number one &mdash; day-0 email within 48 hours.</strong> Target: 100%. It is entirely in your control, and it is the cheapest leading indicator you will ever have.</li>
<li><strong>Number two &mdash; time-to-first-win in business days.</strong> Target: under 10. When this drifts, the pipeline of small wins is broken &mdash; usually because the team is batching everything for the big deliverable.</li>
<li><strong>Number three &mdash; kickoff-with-grid rate.</strong> Kickoffs that happened <em>with</em> the who-does-what grid filled and scope restated, as a share of new clients. 100% is the standard; anything below is onboarding being skipped under delivery pressure, which is exactly when it matters most.</li>
<li><strong>Number four &mdash; scope-confusion tickets in the first 30 days.</strong> Questions about what's included, who does what, how revisions work. This number is the expectations contract working or failing; watch it per client, not just in total.</li>
<li><strong>Number five &mdash; day-30 checkpoint completion.</strong> Checkpoints done as written memos, on time. This is the leading indicator of renewal readiness, months before the renewal conversation exists.</li>
</ul>

<h2>8. Worked example: the eleven-client agency</h2>
<p>An eleven-client design-and-build agency, onboarding handled the old way: a kickoff call "when we get to it" (average: day 12), homework sent as a 40-row spreadsheet, first deliverable whenever it was ready (average: week 5), invoices on the usual cycle, no checkpoint until a client complained. The visible costs: 40% of first-quarter support emails were scope confusion ("was this included?"), two of the year's renewals opened with "honestly, the start felt chaotic," and the owner spent the first month of every engagement re-explaining the process by hand.</p>
<p>One quarter after the checklist went live:</p>
<ul>
<li><strong>Day-0 emails went to 100% within 48 hours.</strong> The welcome email was templated with three fill-ins; the reply-bait question produced a reply from 10 of 11 new clients, and every kickoff started with the client's own answer to it.</li>
<li><strong>Time-to-first-win fell from ~25 business days to 8.</strong> The rule "one visible thing inside ten days" forced the schedule change; the visibility question in the kickoff ("what will your boss ask about first?") picked better first wins than instinct had.</li>
<li><strong>Scope-confusion tickets dropped about 70%.</strong> The restated-scope paragraph and the one-page expectations contract removed the two questions that generated most of the volume; the remainder became change orders with a receipt trail instead of arguments.</li>
<li><strong>Ten of eleven renewals signed &mdash; and one client proposed the expansion themselves,</strong> at the day-30 checkpoint, because the next paragraph of the memo described exactly the thing they'd been hoping someone would offer.</li>
<li><strong>Owner admin in month one fell by half.</strong> The named-owner rule and the grid absorbed the "quick questions" that used to arrive at the founder; the first month now runs on the schedule the client watched being set in week 1.</li>
</ul>

<h2>Where this fits</h2>
<p>Onboarding is the front door of the system this note sits inside: the sale is qualified in the <a href="discovery-call-checklist.html">discovery call checklist</a> and closed by the <a href="quote-follow-up-sequence.html">quote follow-up sequence</a>; the money side is protected by the <a href="upfront-deposit-policy.html">upfront deposit policy</a> and, if a payment slips, the <a href="failed-payment-dunning-sequence.html">failed-payment dunning sequence</a>; the mid-life of the account is managed by the <a href="retainer-renewal-checklist.html">retainer renewal checklist</a>; and the end &mdash; every engagement has one &mdash; is the <a href="client-offboarding-checklist.html">client offboarding checklist</a>, whose referral ask and keep-warm file turn exits into the next onboarding.</p>

<h2>This checklist is part of the kit line</h2>
<p>This checklist is part of the <strong>Hive80 Lab ops kit line</strong> &mdash; field-tested, instantly downloadable:</p>
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
""".replace("{URL}", URL)

(R / f"{SLUG}.html").write_text(PAGE)
print(f"page written: {len(PAGE)} bytes")

# ---------------------------------------------------------------- reciprocals
RECIP = {
 "client-offboarding-checklist.html":
   ('<h2>Where this fits',
    '<p>Onboarding is the other end of the same system: the <a href="client-onboarding-checklist.html">client onboarding checklist</a> makes the start so clean that this exit is routine when it comes &mdash; clients onboarded with named owners, defined success, and a first win rarely exit as arguments.</p>\n'),
 "retainer-renewal-checklist.html":
   ('<h2>1.',
    '<p>The renewal starts earlier than the runway: clients whose first 30 days ran on the <a href="client-onboarding-checklist.html">client onboarding checklist</a> arrive at this decision with defined success metrics and a value story already half-written.</p>\n'),
 "quote-follow-up-sequence.html":
   ('</main>',
    '<p>The handoff matters as much as the close: once the quote is signed, the <a href="client-onboarding-checklist.html">client onboarding checklist</a> takes over &mdash; the first 14 days decide whether this client renews or becomes a win-back row.</p>\n'),
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
CARD = ('<li><a href="client-onboarding-checklist.html">Client Onboarding Checklist for Small Teams '
 '(The First 14 Days That Decide the Renewal)</a><div class="desc">Onboarding is the first renewal '
 'conversation: the 48-hour welcome window with a reply-bait question instead of a 40-question form, '
 'the 30-minute kickoff call that puts scope, three success numbers, and rhythm on the record, the '
 'one-page expectations contract (named channels, numbered revisions, the invoice schedule said out '
 'loud), the first win shipped on the client\'s own data inside ten business days, the day-30 value '
 'checkpoint that seeds the renewal memo, and five weekly numbers (day-0 rate, time-to-first-win, '
 'kickoff-with-grid rate, scope-confusion tickets, checkpoint completion). Worked example: '
 'scope-confusion tickets down 70%, ten of eleven renewals signed, one expansion the client proposed '
 'at the checkpoint.</div></li>')
ip = R / "index.html"
i = ip.read_text()
if SLUG not in i:
    i = i.replace('<ul>\n<li><a href="client-offboarding-checklist.html"',
                  '<ul>\n' + CARD + '\n<li><a href="client-offboarding-checklist.html"', 1)
    ip.write_text(i)
i2 = ip.read_text()
pos = i2.find(SLUG); first_card = i2.find('<li><a href="')
print(f"index: TOP card order ok={0 < pos - first_card < 500}")

# ---------------------------------------------------------------- README
rp = R / "README.md"
r = rp.read_text()
line = ('- **NEW: [Client Onboarding Checklist for Small Teams (The First 14 Days That Decide the Renewal)]'
 '(https://hive80-lab.github.io/ops-notes/client-onboarding-checklist.html)** \u2014 the 48-hour welcome window '
 'with one reply-bait question (never a 40-question form), the 30-minute kickoff that defines three success '
 'numbers and restates scope in your own words, the one-page expectations contract (channels, revision rounds, '
 'invoice rhythm), the first visible win on the client\'s data inside ten business days, the day-30 value '
 'checkpoint that seeds the renewal memo, and five weekly numbers; worked example: scope tickets \u221270%, '
 '10 of 11 renewals signed, one client-proposed expansion.\n')
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
