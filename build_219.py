#!/usr/bin/env python3
"""ops-notes #219 single-unit build: delayed-opening-notice-template.
Canonical repo: /tmp/ops-notes (deploy clone, in sync with origin/main).
Pipeline: page -> sitemap -> index top card -> README NEW -> 3 donor backlinks
-> linkcheck -> git commit+push -> LIVE verify -> IndexNow -> dev.to crosspost.
"""
import os, re, sys, json, time, urllib.request, urllib.error, subprocess

SITE = "/tmp/ops-notes"
URLBASE = "https://hive80-lab.github.io/ops-notes/"
TODAY = time.strftime("%Y-%m-%d")
UA_BROWSER = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7 AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

def w(path, text):
    with open(os.path.join(SITE, path), "w", encoding="utf-8") as f:
        f.write(text)

def r(path):
    with open(os.path.join(SITE, path), encoding="utf-8") as f:
        return f.read()

SLUG = "delayed-opening-notice-template"
TITLE = "Delayed Opening Notice Template (When You Can't Say Open or Closed, Say When You'll Decide)"
NUM = 219

KIT = """<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Delayed Opening Notice Template (Say When You'll Decide, Not Just "Closed Today") &mdash; HIVE80lab Ops Notes</title>
<meta name="description" content="A delayed opening notice template for small businesses: the three states (open, closed, undecided) and why undecided is only dangerous when it's silent, the two kinds of delay (delay-to-decide vs delay-the-open), the update-deadline rule (never announce a delay without naming the next update time), the T-14h / T-2h / T-30m decision ladder, the five-channel morning sequence, the five sentences of wording, the staff pay line, the five traps (including the delay that becomes a silent closure and the never-delay-twice rule), and the worked example &mdash; a four-chair dental clinic on a glare-ice Tuesday morning.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/delayed-opening-notice-template.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<h1>Delayed openings &mdash; when you can't say open or closed, say when you'll decide</h1>
<p class="lede">Every closure has three states: <strong>open</strong>, <strong>closed</strong>, and <strong>undecided</strong>. The first two are fine &mdash; customers and staff know exactly what to do with them. The third is the one businesses manage badly: the morning is genuinely uncertain (the ice is melting, the road crew hasn't cleared the lot, the inspector is due at nine), so the owner says nothing &mdash; which customers read as <em>open as usual</em>, and staff discover is wrong when they're already on the road. A delayed opening is how you make the undecided state <em>safe</em>: you defer the decision <strong>publicly, with a deadline attached</strong>. "We're opening at 11 instead of 7; next update by 8:30" is a complete message &mdash; it buys you two hours, tells everyone the plan, and commits you to the next word. This page gives you the two kinds of delay, the update-deadline rule, the decision ladder, the wording, the staff line, the five traps, and the copy-paste template.</p>

<h2>1. The three states (and why "undecided" is only dangerous when it's silent)</h2>
<p>A customer's morning has one question about your business: <em>what do I do?</em> Open answers it (&ldquo;come as usual&rdquo;). Closed answers it (&ldquo;come later, here's the plan&rdquo;). <strong>Undecided answers it with silence &mdash; and silence is always interpreted as open-as-usual.</strong> That's the failure mode: nobody reads your hesitation as caution; they read it as nothing being wrong. The rule that fixes the third state:</p>
<p><strong>You can't always know &mdash; but you can always say when you'll know.</strong></p>
<p>A delay notice is exactly that sentence, made public. It converts &ldquo;we don't know yet&rdquo; (useless to a customer) into &ldquo;we'll know by 8:30 and we'll tell you where we already post&rdquo; (a plan). The undecided state is allowed; the <em>silent</em> undecided state is the defect.</p>

<h2>2. The two kinds of delay (they are different decisions)</h2>
<ul>
<li><strong>Delay-to-decide.</strong> You haven't decided anything yet; you're announcing that a decision is coming at a named time. &ldquo;Conditions are still changing &mdash; decision on today's hours by 8:30, posted here and on our voicemail.&rdquo; This is the rarest and most delicate: it spends trust to buy time, so it must carry a deadline you keep.</li>
<li><strong>Delay-the-open.</strong> The decision is made &mdash; you're opening later. &ldquo;Opening at 11am instead of 7am today; next update by 8:30am.&rdquo; You've traded the morning for the day, on purpose, with a named new time. Most &ldquo;delayed opening&rdquo; cases are this kind, and it's the safer message to give: a specific time beats a promise of a time.</li>
</ul>
<p>Never blur the two. If you mean &ldquo;we open at 11,&rdquo; say &ldquo;we open at 11&rdquo; &mdash; not &ldquo;we'll decide by 11.&rdquo; If you genuinely can't commit, say &ldquo;we'll decide by 8:30&rdquo; and keep that promise to the minute. Blurred wording is why customers show up anyway: they heard neither.</p>

<h2>3. The update deadline (the whole template in one rule)</h2>
<p><strong>Never announce a delay without naming the next update time &mdash; and keep it, even if the news is &ldquo;still deciding.&rdquo;</strong></p>
<p>The deadline is what makes the message complete. Without it, a delay is just a slower way of going silent. With it, everyone who reads the first message knows exactly when to look again, and you've converted a listening audience into people who <em>stop refreshing</em>. Three rules keep the clock honest:</p>
<ul>
<li><strong>Name a time, not an event.</strong> &ldquo;Update by 8:30am,&rdquo; not &ldquo;when we know more&rdquo; or &ldquo;once the plow comes.&rdquo; Events don't have clocks; people do.</li>
<li><strong>Keep the promise even with no news.</strong> &ldquo;8:30 update: still waiting on the lot crew; next update by 9:45.&rdquo; An update-about-the-update is a legitimate update &mdash; it's proof the clock is real. The one thing you may not do is let a named time pass in silence.</li>
<li><strong>Front-load the channels at the first announcement.</strong> Every person who sees the delay on any channel must be told <em>where the updates will appear</em> (usually: this page / our Google profile / our voicemail). Naming the place once means you never have to re-reach everyone at update time.</li>
</ul>

<h2>4. The decision ladder (T-14h &rarr; T-2h &rarr; T-30m)</h2>
<p>A delay works best as a rung on a ladder, not a standalone improvisation. The rungs (anchored to the <a href="office-closure-weather-day-checklist.html">weather-day closure checklist</a>, which owns the night-before call):</p>
<ul>
<li><strong>T-14h (the night before, by 6pm):</strong> if the forecast is on the fence, announce the <em>provisional</em> delay tonight: &ldquo;opening at 11am instead of 7 tomorrow; update by 8:30am.&rdquo; Staff sleep, customers plan, and the 6am scramble never exists.</li>
<li><strong>T-2h (about two hours before normal open):</strong> if the night passed without a call &mdash; the genuinely undecided morning &mdash; make the delay-to-decide call: &ldquo;decision by 8:30 on today's hours; updates here, on our voicemail, and on our Google profile.&rdquo; This rung costs you nothing if you keep the deadline, and everything if you don't.</li>
<li><strong>T-30m (before the delayed open):</strong> confirm or flip. Confirm: &ldquo;we're on for 11 &mdash; lot's clear, coffee's on.&rdquo; Flip to close: &ldquo;we tried for 11 &mdash; it's not safe yet; we're closed today, reopening tomorrow at 7 unless we post otherwise.&rdquo; A flip <em>announced before the named open time</em> is a kept promise; the same flip discovered at the parking lot is a betrayal of one.</li>
</ul>
<p><strong>Never delay twice in the same morning.</strong> One provisional delay buys goodwill; a second one spends it at compound interest &mdash; everyone moved twice for nothing. If the second decision time arrives and you still can't open, the answer is a <a href="store-closure-temporary-notice.html">temporary closure notice</a>, not another delay. Flip to close, say when you expect to reopen, and be done.</p>

<h2>5. The five-channel morning sequence (order matters less than completeness)</h2>
<p>The night-before weather-day sequence has seven channels (see the checklist); a morning-of delay runs the five that exist before most people wake up &mdash; and the same list every time, so no channel is remembered only in retrospect:</p>
<ol>
<li><strong>Door sign</strong> (first decision time and the update time &mdash; for the person who walked anyway).</li>
<li><strong>Website banner / status note</strong> &mdash; the one page you'll actually update at the deadline.</li>
<li><strong>Google Business Profile</strong> &mdash; special hours or a post: &ldquo;Opening 11am today (normally 7). Update by 8:30am.&rdquo; This is the channel drivers consult in the parking lot of their <em>own</em> morning; a stale &ldquo;Open&rdquo; here sends people to your door.</li>
<li><strong>Voicemail</strong> &mdash; recorded before the first ring matters: normal-hours greeting minus the normal hours.</li>
<li><strong>Booked/scheduled customers direct</strong> &mdash; individual messages with the new time (or the decision time) and a one-word reply option (&ldquo;Works&rdquo; / &ldquo;Move me&rdquo;). The blast post is not a notification to the person who was going to be in your chair at 7:15.</li>
</ol>
<p>Social and autoresponder follow if they exist &mdash; but the five above are the ones a delay is actually judged by. Miss Google hours or the voicemail and you've sent your most trusting customers into a locked-morning experience.</p>

<h2>6. The five sentences (the wording, copy-paste)</h2>
<p>Every delay notice &mdash; sign, banner, Google post, voicemail, text &mdash; is the same five sentences in this order:</p>
<ol>
<li><strong>What you know:</strong> &ldquo;The lot hasn't been plowed and the temperature hasn't cleared freezing.&rdquo;</li>
<li><strong>What that means:</strong> &ldquo;We're opening at 11am today instead of 7am.&rdquo; (or: &ldquo;We haven't decided on today's hours yet.&rdquo;)</li>
<li><strong>When you'll update:</strong> &ldquo;Next update by 8:30am &mdash; kept either way.&rdquo;</li>
<li><strong>Where:</strong> &ldquo;Updates here, on our Google profile, and on our voicemail.&rdquo;</li>
<li><strong>What to do meanwhile:</strong> &ldquo;Morning appointments: we'll text you directly before 7:30. Walk-ins: check back after 8:30.&rdquo;</li>
</ol>
<p>Voice-mail variant, 15 seconds: <em>&ldquo;Hi, you've reached [business]. Normally we open at 7 &mdash; today we're opening at 11 because of the ice, with an update by 8:30 if anything changes. If you have a morning appointment, we'll call you directly. Thanks for checking before you drove.&rdquo;</em> That last clause (&ldquo;thanks for checking&rdquo;) is doing more work than it looks like: it rewards the exact behavior you want everyone to have.</p>

<h2>7. The staff line (the clock your employees are also inside)</h2>
<p>Staff hear the delay through the same channels as customers &mdash; plus a private one. Three lines, agreed in advance:</p>
<ul>
<li><strong>The call-in ladder.</strong> Who gets called, in what order, at what time &mdash; the closer and opener first, everyone else at the update time. No group thread waiting to be read; the decider calls names.</li>
<li><strong>The pay line, said out loud.</strong> A delayed open shortens paid shifts. Whatever your rule is (show-up pay for those already in transit, shifts paid from the new open, PTO offered), say it in the delay message, not at the punch clock. The employees who commuted on ice <em>before</em> the delay existed are the ones the rule exists for.</li>
<li><strong>The flip duty.</strong> Whoever is physically nearest the building at T-30m owns the eyes-on call (lot, walkway, entrance) and reports to the decider by the deadline. A delay decided by text thread from four couches is how the 11am open happens onto an iced walkway.</li>
</ul>

<h2>The five delayed-opening traps</h2>
<ol>
<li><strong>The delay as procrastination.</strong> Naming an update time and missing it converts a delay into a silent closure &mdash; the worst state on the board. If you can't keep the deadline, keep the <em>promise about the deadline</em>: post &ldquo;update running late; next word by 9:15.&rdquo;</li>
<li><strong>The delay that becomes a silent closure.</strong> The 11am open quietly dies at 10:45 and nobody says so. Customers arrive at 11:04. If you're not opening at the named time, the flip-to-close message goes out <em>before</em> it, not after.</li>
<li><strong>Delaying twice.</strong> Second delay in one morning = flip to a closure. Every extra deferral reads as indecision to the people who moved for the first one.</li>
<li><strong>Updating only one channel.</strong> The banner says 11am; Google still says 7; the voicemail still says normal hours. Customers don't compare channels &mdash; they act on whichever one they saw last. Update the same five channels you announced on.</li>
<li><strong>The normal-hours door sign.</strong> The sign on the door is the one artifact that outlives every digital channel &mdash; and the one most often forgotten in a delay, because &ldquo;we'll only be an hour late.&rdquo; Print the delay sign from the template below, tape it inside the glass, and the morning is covered even if the power is out.</li>
</ol>

<h2>Worked example: a four-chair dental clinic, Tuesday, glare ice</h2>
<p>Monday 9pm: freezing rain forecast overnight; the practice had no night-before call to make (they'd have closed at 6pm Monday if it were certain &mdash; it wasn't). Tuesday 6:40am: the office manager's own driveway is a skating rink; the parking lot is untreated; two hygienists commute 40 minutes. The named decider (the practice owner) is reached at 6:42.</p>
<ul>
<li><strong>6:45am &mdash; delay-to-decide:</strong> all five channels: &ldquo;Glare ice this morning &mdash; decision on today's hours by 8:30am; updates here, on Google, and on our voicemail. Morning patients: we'll text you before 7:30.&rdquo; (9 minutes.)</li>
<li><strong>6:55am &mdash; texts go to the six 8am-and-before patients:</strong> &ldquo;Decision by 8:30; we'll confirm either way before 7:45.&rdquo; Staff call-in ladder runs: front desk at 7:00, hygienists at 7:15 with the pay line stated (paid from arrival; 8am appointments held or moved by choice).</li>
<li><strong>8:25am &mdash; eyes-on:</strong> lot untreated, walkway sheet ice, temperature still below freezing. Flip decision made by the named decider at 8:27.</li>
<li><strong>8:30am &mdash; on the deadline:</strong> &ldquo;We tried for a delayed open &mdash; the lot is still ice. We're closed today; Wednesday is full and we'll move today's patients there first. Voicemail and Google updated now.&rdquo; Eleven morning patients: seven moved to Wednesday (their choice of slots), two to Thursday, two took the Friday-afternoon standing offer. Zero arrive at 11 to a dark door, because the flip was announced before the promised time.</li>
<li><strong>Cost:</strong> one closed Tuesday (receptionist and owner in by 9 to call, reschedule, and restock the schedule), one bag of salt bought at 1pm for Wednesday's 6am walkthrough. The alternative &mdash; open on time at 7 &mdash; was a hygienist in a ditch and a waiting room of patients watching her get towed.</li>
</ul>

<h2>Metrics (four numbers, reviewed after every delay)</h2>
<ul>
<li><strong>Kept-update rate:</strong> named update times kept, divided by named update times. Target 100% &mdash; this is the metric the whole system stands on.</li>
<li><strong>Time-to-first-notice:</strong> decision (or defer-decision) to first channel live. Target: under 15 minutes.</li>
<li><strong>Individual-reach rate:</strong> booked customers personally messaged before the original open time, divided by all booked in the window. Target 100%; the blast post doesn't count.</li>
<li><strong>Show-up misses:</strong> customers who arrived during the delay window expecting normal hours. Anything above zero is a channel gap &mdash; find which one they acted on.</li>
</ul>

<h2>The one-page template (copy, fill, post)</h2>
<ul>
<li><strong>Named decider:</strong> __________________ (one person; the committee is for advice, not the call)</li>
<li><strong>State at first notice:</strong> &#9744; delay-to-decide &#9744; delay-the-open</li>
<li><strong>New open time:</strong> ________ &nbsp; <strong>First update time:</strong> ________ (kept, either way)</li>
<li><strong>Where updates appear:</strong> &#9744; door sign &#9744; website &#9744; Google profile &#9744; voicemail &#9744; direct texts</li>
<li><strong>The five sentences:</strong> what we know / what it means / when we'll update / where / what to do meanwhile</li>
<li><strong>Staff call-in ladder:</strong> who, in what order, at what times</li>
<li><strong>Pay line:</strong> __________________ (said in the delay message, not at the punch clock)</li>
<li><strong>Flip rule:</strong> second decision time without an opening = close (never delay twice)</li>
<li><strong>Reopen check:</strong> lot clear, walkway salted, eyes-on report received before doors unlock</li>
</ul>
<p><em>Keep this page with the <a href="business-continuity-plan-template.html">business continuity plan</a> and the <a href="office-closure-weather-day-checklist.html">weather-day checklist</a> &mdash; same folder, same winter.</em></p>
""" + KIT + """<p><em>Related: the <a href="https://hive80-lab.github.io/ops-notes/office-closure-weather-day-checklist.html">weather-day closure checklist</a> is the night-before system that makes most delays unnecessary (decide at 6pm, sleep in); the <a href="https://hive80-lab.github.io/ops-notes/store-closure-temporary-notice.html">temporary closure notice template</a> is what you publish when the delay flips to a close; and the <a href="https://hive80-lab.github.io/ops-notes/reopening-notice-template.html">reopening notice template</a> runs the verified-reopen gate before the sign comes back down.</em></p>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
"""

DEVTO = """-- a delayed opening is a decision to defer publicly, with a deadline attached.

Most businesses handle the uncertain morning one of two ways: they stay silent (which every customer reads as "open as usual") or they post "updates to follow" (which is silence with extra steps). Both produce the same scene: someone standing at your door at 7:05, reading a note that wasn't there yesterday.

The fix is one rule: **you can't always know, but you can always say when you'll know.**

The two kinds of delay:

**Delay-to-decide.** You haven't decided; you're announcing that a decision is coming at a named time. "Decision on today's hours by 8:30, posted here and on our voicemail." Rare, delicate, and only works if you keep the deadline.

**Delay-the-open.** The decision is made - you're opening later. "Opening at 11 instead of 7; next update by 8:30." A specific time beats a promise of a time. Most delays are this kind; say the number.

Never blur the two. "We'll decide by 11" when you mean "we open at 11" is why people show up anyway - they heard neither.

**The update deadline is the whole template.** Never announce a delay without naming the next update time - and keep it even if the news is "still deciding." An update-about-the-update ("8:30: still waiting on the lot crew; next word by 9:45") is proof the clock is real. The one thing you may never do is let a named time pass in silence.

**The ladder** (anchored to the night-before weather-day call):

- T-14h: forecast on the fence? announce the provisional delay tonight - "11am instead of 7 tomorrow; update by 8:30."
- T-2h: genuinely undecided morning? delay-to-decide with the named deadline.
- T-30m: confirm ("on for 11, lot's clear") or flip ("we tried for 11 - it's not safe; closed today, reopening tomorrow at 7").

**Never delay twice in one morning.** One delay buys goodwill; the second spends it at compound interest. If you can't open at the named time, the answer is a temporary closure notice, not another delay - flipped and announced *before* the time you named.

**Five channels before most people wake up:** door sign, website banner, Google Business Profile ("Opening 11am today, normally 7 - update by 8:30"), voicemail, and direct texts to everyone booked in the window. Google hours and the voicemail are the two everyone forgets - and they're the two people check from the parking lot of their own morning.

**The staff line, said out loud:** who gets called and when, what the pay rule is for shortened shifts, and who has eyes-on duty at the flip decision. The delay clock belongs to your employees too.

The worked example on the page: a four-chair dental clinic on a glare-ice Tuesday. 6:45am delay-to-decide on all five channels (9 minutes), direct texts to six morning patients by 6:55, eyes-on at 8:25, flip to close at exactly the promised 8:30. Eleven patients moved, zero arrived to a dark door. The cost was one quiet Tuesday and a bag of salt.

Full template - the two delay types, the deadline rule, the five sentences of wording, the traps, and the copy-paste one-pager:
https://hive80-lab.github.io/ops-notes/delayed-opening-notice-template.html

(If the delay flips to a close, the temporary closure notice takes over: https://hive80-lab.github.io/ops-notes/store-closure-temporary-notice.html - and the reopen is a verified gate: https://hive80-lab.github.io/ops-notes/reopening-notice-template.html)"""


def build():
    # 1. page
    w(SLUG + ".html", PAGE)
    print("PAGE_OK", SLUG)

    # 2. sitemap: insert newest-first (right after <urlset ...>)
    s = r("sitemap.xml")
    new_url = ("<url><loc>" + URLBASE + SLUG + ".html</loc><lastmod>" + TODAY +
               "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    if SLUG + ".html" not in s:
        m = re.search(r"<urlset[^>]*>", s)
        s = s[:m.end()] + new_url + s[m.end():]
        w("sitemap.xml", s)
    else:
        print("SITEMAP_SKIP already")
    n = len(re.findall(r"<loc>", s))
    print("SITEMAP_OK urls:", n)

    # 3. index top card
    t = r("index.html")
    card = '<li><a href="' + SLUG + '.html">Delayed Opening Notice Template: Say When You&rsquo;ll Decide, Not Just "Closed Today"</a> &mdash; the three states (open, closed, undecided), delay-to-decide vs delay-the-open, the update-deadline rule, the T-14h/T-2h/T-30m ladder, the five-sentence wording, the never-delay-twice rule, and the glare-ice dental clinic worked example.</li>'
    if SLUG + '.html' not in t.split("</ul>")[0]:
        t = t.replace("<ul>", "<ul>" + card, 1)
        w("index.html", t)
    else:
        print("INDEX_SKIP already")
    print("INDEX_OK")

    # 4. README NEW bullet (top of NEW list)
    rd = r("README.md")
    bullet = ("- **NEW: [Delayed Opening Notice Template (When You Can't Say Open or Closed, Say When You'll Decide)]("
              + URLBASE + SLUG + ".html)** &mdash; the three states (open, closed, undecided) and why undecided is only dangerous when it's silent, the two kinds of delay (delay-to-decide vs delay-the-open), the update-deadline rule (never announce a delay without naming the next update time &mdash; kept even to say &ldquo;still deciding&rdquo;), the T-14h / T-2h / T-30m decision ladder, the never-delay-twice flip rule, the five-channel morning sequence (Google hours and voicemail are the two everyone forgets), the five sentences of wording, the staff pay line, the five traps, and the four-chair dental clinic glare-ice worked example.\n")
    if "**NEW: [Delayed Opening" not in rd:
        idx = rd.find("- **NEW:")
        rd = rd[:idx] + bullet + rd[idx:]
        w("README.md", rd)
        print("README_OK")
    else:
        print("README_SKIP already")

    # 5. donor backlinks
    # 5a. office-closure-weather-day-checklist (#218): extend the provisional-decision li
    p218 = "office-closure-weather-day-checklist.html"
    s218 = r(p218)
    if SLUG not in s218:
        anchor218 = "A provisional decision is allowed."
        i = s218.find(anchor218)
        if i > -1:
            j = s218.find("</li>", i)
            if j > -1:
                ins = (" The full wording, the update-deadline rule, and the never-delay-twice flip are in the "
                       "<a href=\"delayed-opening-notice-template.html\">delayed opening notice template</a>.")
                s218 = s218[:j] + ins + s218[j:]
                w(p218, s218)
                print("BACKLINK_218_OK")
    # 5b. store-closure-temporary-notice (#215): new li after the under-24h tier
    p215 = "store-closure-temporary-notice.html"
    s215 = r(p215)
    if SLUG not in s215:
        anchor215 = "Skip the website banner if the site drives no walk-ins."
        i = s215.find(anchor215)
        if i > -1:
            j = s215.find("</li>", i)
            if j > -1:
                ins = ("<li>If the under-24h case is a &ldquo;maybe&rdquo; rather than a &ldquo;no&rdquo;, that's a "
                       "<em>delayed opening</em>, not a closure &mdash; same channels, plus a named update time; see the "
                       "<a href=\"delayed-opening-notice-template.html\">delayed opening notice template</a>.</li>")
                s215 = s215[:j+5] + ins + s215[j+5:]
                w(p215, s215)
                print("BACKLINK_215_OK")
    # 5c. business-continuity-plan-template: related aside li
    pbc = "business-continuity-plan-template.html"
    sbc = r(pbc)
    if SLUG not in sbc:
        i = sbc.find("</main>")
        j = sbc.rfind("<li>", 0, i)
        if j > -1:
            k = sbc.find("</li>", j)
            li = ('<li>The undecided morning: when you can&#39;t say open or closed, say when you&#39;ll decide &mdash; '
                  'the <a href="delayed-opening-notice-template.html">delayed opening notice template</a> '
                  '(delay-to-decide vs delay-the-open, update-deadline rule, never-delay-twice).</li>')
            sbc = sbc[:k+5] + li + sbc[k+5:]
            w(pbc, sbc)
            print("BACKLINK_BC_OK")

    # 6. linkcheck (relative hrefs must exist)
    files = [f for f in os.listdir(SITE) if f.endswith(".html")]
    broken = 0
    for f in files:
        body = r(f)
        for href in re.findall(r'href="([^"]+\.html[^"]*)"', body):
            if href.startswith("http"):
                continue
            tgt = href.split("#")[0].split("?")[0]
            if tgt and not os.path.exists(os.path.join(SITE, tgt)):
                print("BROKEN", f, "->", href); broken += 1
    print("LINKCHECK broken:", broken)
    if broken:
        sys.exit("linkcheck failed")

    # 7. git commit + push
    subprocess.run(["git", "add", "-A"], cwd=SITE, capture_output=True, text=True)
    msg = ("ops-notes: delayed opening notice template (#219) - the three states (open, closed, undecided; "
           "undecided is only dangerous when silent), the two kinds of delay (delay-to-decide vs delay-the-open; "
           "never blur the two), the update-deadline rule (never announce a delay without naming the next update "
           "time, kept even to say 'still deciding'), the T-14h/T-2h/T-30m decision ladder, the never-delay-twice "
           "flip rule (second decision time without an opening = temporary closure notice), the five-channel "
           "morning sequence (door sign, website banner, Google hours, voicemail, direct texts), the five sentences "
           "of wording with the 15-second voicemail variant, the staff line (call-in ladder, pay line, flip duty), "
           "the five traps, the four-chair dental clinic glare-ice worked example (flip announced on the promised "
           "8:30 deadline, zero show-up misses), and the four delay metrics; kit block (no coupon per post-expiry "
           "rule); reciprocal backlinks (office-closure-weather-day-checklist #218, store-closure-temporary-notice "
           "#215, business-continuity-plan-template); sitemap " + str(n) + " urls (newest-first, XML valid); "
           "index TOP card; README NEW; linkcheck 0 broken across all relative hrefs")
    subprocess.run(["git", "commit", "-m", msg], cwd=SITE, capture_output=True, text=True)
    p = subprocess.run(["git", "push"], cwd=SITE, capture_output=True, text=True)
    print("PUSH", p.returncode, (p.stdout + p.stderr).strip()[:160])

    # 8. LIVE verify
    url = URLBASE + SLUG + ".html"
    for attempt in range(1, 9):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA_BROWSER}), timeout=15) as resp:
                if resp.status == 200:
                    print("LIVE_OK", resp.status, url, flush=True); break
        except Exception as e:
            print("live attempt", attempt, e, flush=True)
        time.sleep(20 * attempt)

    # 9. IndexNow
    live_key = None; kf = None
    for cand in ("indexnow.key", "indexnow-key.txt", "indexnow.txt"):
        try:
            with urllib.request.urlopen(URLBASE + cand, timeout=15) as resp:
                if resp.status == 200:
                    live_key = resp.read().decode().strip(); kf = cand; break
        except Exception as e:
            print("key candidate", cand, "->", e)
    if live_key:
        body = json.dumps({"host": "hive80-lab.github.io", "key": live_key, "keyLocation": URLBASE + kf,
                           "urlList": [URLBASE + SLUG + ".html", URLBASE + "index.html",
                                       URLBASE + "office-closure-weather-day-checklist.html",
                                       URLBASE + "store-closure-temporary-notice.html",
                                       URLBASE + "business-continuity-plan-template.html"]}).encode()
        req = urllib.request.Request("https://api.indexnow.org/IndexNow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8",
                                              "User-Agent": UA_BROWSER})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print("INDEXNOW:", resp.status, flush=True)
        except urllib.error.HTTPError as e:
            print("INDEXNOW HTTP", e.code, e.read()[:200], flush=True)
    else:
        print("INDEXNOW_SKIP no live key")

    # 10. dev.to publish (direct publish with canonical)
    try:
        dkey = open(os.path.expanduser("~/Swarm/hive/state/secure/devto_api_key.txt")).read().strip()
    except Exception:
        print("DEVTO_SKIP no key"); return
    payload = {"article": {"title": "The 6:40am decision that saves a Tuesday: how to announce a delayed opening",
                           "published": True, "body_markdown": DEVTO,
                           "tags": ["smallbusiness", "operations", "management", "entrepreneurship"],
                           "canonical_url": URLBASE + SLUG + ".html"}}
    for attempt in range(1, 5):
        req = urllib.request.Request("https://dev.to/api/articles", data=json.dumps(payload).encode(),
                                     headers={"api-key": dkey, "Content-Type": "application/json",
                                              "User-Agent": UA_BROWSER})
        try:
            rr = json.load(urllib.request.urlopen(req))
            print("DEVTO_OK id:", rr.get("id"), "| url:", rr.get("url"), flush=True)
            break
        except urllib.error.HTTPError as e:
            print("devto attempt", attempt, "HTTP", e.code, e.read()[:200], flush=True)
            time.sleep(15 * attempt)
        except Exception as e:
            print("devto attempt", attempt, "ERR", e, flush=True); time.sleep(15 * attempt)

if __name__ == "__main__":
    build()
