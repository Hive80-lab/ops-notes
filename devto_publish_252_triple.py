#!/usr/bin/env python3
"""ops-notes triple unit dev.to syndication (#252 walk-in cooler, #253 pest control, #254 shift handover).
Pattern per devto_publish_251.py. Idempotent-ish: 422 (slug taken) is non-fatal."""
import json, urllib.request

KEY = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
BASE = 'https://hive80-lab.github.io/ops-notes'

KITS = """
---

**Kits** — the paid tools behind the free advice:

- [The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) — free incident quick-start checklist
- [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit) — incident response for small teams — $14
- [Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) — advanced incident response & communications — $27
- [Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle) — all 5 kits in one download — $49

Code **HIVE-LAUNCH30** takes 30% off any kit at checkout.
"""

WALKIN_URL = f'{BASE}/walk-in-cooler-maintenance-checklist.html'
PEST_URL = f'{BASE}/pest-control-service-log.html'
HANDOVER_URL = f'{BASE}/shift-handover-log.html'

WALKIN = f"""One hour, once a week, with a dollar bill, a screwdriver and a bucket: the six-point gasket test, the condenser coil that converts dust into compressor years, the evaporator face that hides its ice until the night it matters, the drain pan that should be wet but not full, and the door hardware that decides whether all of it holds.

The [twice-daily temperature log]({BASE}/refrigeration-temperature-log.html) tells you the walk-in is cold. It does not tell you the box is *working hard* to be cold — a compressor pulling 41°F through a leaking gasket and a dust-caked coil is a countdown, not a success. The log catches the day the countdown ends; the weekly walk pushes the countdown back. The log is the smoke detector. The Sunday walk is smoke *prevention*.

## The dollar-bill gasket test — six points, every door

Close the door on a dollar bill at six points — top, middle, bottom, both hinge-side midpoints — and pull. The bill should drag. Any point where it slides out freely is a leak, and a leak is a compressor running flat-out to cool the hallway. Gasket kits are $60–$125 and arrive in a week; the compressor they kill is $2,800 installed, and it takes the [cold-chain failure playbook]({BASE}/cold-chain-failure-checklist.html) with it when it goes.

"Rear door, point 4 pulls free" is a work order. "Gaskets feel off" is a vibe. Vague findings die in the [work order template]({BASE}/maintenance-work-order-template.html) the same afternoon, not next week.

## The condenser coil — the dust you can bank against

The coil is where the box dumps kitchen heat into the room, and it lives low where flour, grease and dust settle into felt. A felted coil cannot dump heat, so the compressor runs longer, hotter and dies younger — the single most expensive piece of deferred maintenance in a commercial kitchen. Vacuum with a brush head, wipe with coil cleaner monthly (weekly in summer). The test is cheap: fins should look like metal, not carpet.

## The evaporator face — the ice that hides until the night it matters

Ice on the evaporator means the box cools worse while the thermostat swears everything is fine. It builds for weeks, then the unit trips out on a Saturday. Look at the face weekly; heavy ice is a defrost problem — a work order, not a scrape.

## The drain pan and the door hardware

The pan should be wet, not full — full means the drain line is blocked and you are growing a biology experiment above your stock. Door hinges, closer tension, strike alignment: a door that doesn't seal undoes every dollar the gaskets and the coil save.

## Worked example — the 40-seat restaurant's Sunday

Week 31: rear door point 4 pulls free. Gasket kit ordered Monday, $125. Fit check on the next Sunday walk: full grip at all six points. The counterfactual — same leak found at the next temperature log's *three-alarm* read instead — is the $2,800 compressor and $9,000 of stock in August. The walk is one hour a week. The failure it prevents is a quarter's margin.
"""

PEST = f"""A pest control service log is not about pests; it is about proof. "We've never had pests" is a claim nobody can check, and a health inspector is trained not to take claims. "We monitor — here are twelve months of weekly checks, contractor reports, and receipts for every fix" is a record the inspector can read in thirty seconds, and it is the difference between the pest conversation ending and the pest conversation *starting*.

The log has two parts, and both matter: the weekly self-checks your own crew does (Part A) and the block you fill at every contractor visit (Part B).

## Part A — the weekly self-check (five minutes, before the contractor ever comes)

One row per week, on one sheet taped inside a cabinet near the back door:

- **Sightings and signs.** What was actually seen, where, and when. "Nothing observed" written honestly every week is worth more than a page of perfect weeks that suddenly stops.
- **Trap and station status.** The numbered stations on the floor plan: intact, baited, sprung, missing. A missing station is a work order.
- **Harborage.** The cardboard stack behind the prep line, the mop head stored wet, the gap under the back door sweep. Pests are a habitat problem before they are a bug problem.
- **What was done right then.** Harborage removed, trap reset, bin re-lidded — the same-hour fix is the heart of the log.
- **Initials.** A real person. Accountability is what makes it a log instead of a poster.

## Part B — the contractor visit block (filled at hand-off, never from memory)

Date, tech name and **license number** — the license line is what the inspector looks for first. Stations serviced plus the **bait map updated** — numbered stations on a current floor plan, not the map from 2023. Product used plus the **EPA registration number** — every chemical gets its number, or the visit is a liability instead of a defense. Findings, corrective actions, and the next scheduled visit.

## Why it reads as a defense

When the inspector asks about pests, the binder opens to: twelve months of weekly rows, signed; contractor reports with license and EPA numbers; the receipts for the door sweep and the bin lids; and the correction trail for the two incidents the year before — both closed. That binder reads as *management*. A folder of contractor invoices with nothing around them reads as *spending*.

## Worked example

Two mouse droppings behind the dish pit, week 33. Row written same hour: location, count, harborage found (a cardboard tower), action (tower removed, two traps set, gaps sealed under the dish line), initials. Contractor's quarterly visit lands week 35 — the tech confirms the seal, resets the map, EPA number on file. The inspector in week 41 reads the trail in thirty seconds. The counterfactual: the same two droppings found *by the inspector*, with no row, no map and no receipts, is the conversation where kitchens get closed.

Full sheet, plus the [equipment downtime log]({BASE}/equipment-downtime-log.html) and the [maintenance work order]({BASE}/maintenance-work-order-template.html) that pest findings feed into, on the page itself.
"""

HANDOVER = f"""A shift handover log is not paperwork; it is a firewall. Every shift ends with knowledge only the outgoing crew holds — the walk-in that read warm at lunch, the dishwasher making the new noise, the porter who didn't show, the supplier who called about Monday's delivery. When that knowledge leaves in people's heads instead of on a sheet, the next shift rediscovers it the hard way, hours later, at full price.

The [equipment downtime log]({BASE}/equipment-downtime-log.html) records what broke and what it cost. The handover log is what stops the breaking from happening in the first place.

## The crossover arithmetic

Problems follow the cheapest path: the cheapest person to tell is whoever just noticed it, and the cheapest time to act is while the person who understands it is still on the floor. A walk-in that flagged at lunch is a thirty-second recheck at handover; the same walk-in discovered by the dinner crew at 6 p.m. is a stock decision, a work order and a bad night. The log moves every open issue across the boundary while it is still cheap — and it does it in writing, because "I told the manager" is the most expensive sentence in operations.

## Seven lines per handover

One sheet at the crossover point, dated and initialed by **both** shifts:

1. **Date, shift, both initials** — the outgoing shift signs for what it leaves; the incoming signs for what it accepts. Both names in one row turns a note into a contract.
2. **Open work orders** — every ticket still open, with number and state, from the [work order queue]({BASE}/maintenance-work-order-template.html).
3. **Equipment watching** — anything behaving oddly but not yet broken: "walk-in #2 air 43°F at lunch, food OK, recheck pending" — the front line of the [temperature log]({BASE}/refrigeration-temperature-log.html) workflow.
4. **People** — absences, no-shows, and who covers the gap.
5. **Suppliers and deliveries** — the call about Monday's order, the short delivery accepted at the door, the invoice dispute. These decay badly overnight.
6. **Money** — till variance, refunds, flagged invoices. Unexplained variances age like milk.
7. **The one thing the next shift must know** — written even when it is "nothing — good shift." An empty must-know line means someone stopped thinking.

## The walk-the-floor rule

The handover is not a document exchange; it is a five-minute walk. Outgoing and arriving leads walk the floor together: the walk-in door, the dish machine, the delivery door, the office desk. Points get shown, not described. Two minutes of walking saves twenty minutes of "wait, which ice machine?" at the worst hour of the night.

## Worked example

Lunch shift: walk-in #2 read 43°F air at 12:40, recheck pending. Handover 14:55, line 3: *walk-in #2 flagged 43°F air / 41°F food, recheck pending, gasket suspected*. Dinner shift rechecks at 15:10, still climbing, opens work order #0143, orders the $45 gasket before service. Counterfactual without the sheet: the dinner crew meets a warm walk-in at 18:00 with a full prep table — and the $7,300 quarter of stock in the balance.
"""

ARTICLES = [
    (WALKIN_URL,
     "The Walk-In Cooler Maintenance Checklist — The Sunday Hour That Keeps the Cold Chain Alive",
     WALKIN + KITS),
    (PEST_URL,
     "The Pest Control Service Log — The Paper Trail That Proves the Kitchen Is Cleaner Than It Looks",
     PEST + KITS),
    (HANDOVER_URL,
     "The Shift Handover Log — The Ten-Minute Sheet That Stops the Next Shift Paying for This One's Surprises",
     HANDOVER + KITS),
]

for url, title, body in ARTICLES:
    payload = {
        "article": {
            "title": title,
            "published": True,
            "body_markdown": body,
            "canonical_url": url,
            "tags": ["restaurants", "smallbusiness", "operations", "productivity"],
        }
    }
    req = urllib.request.Request(
        "https://dev.to/api/articles",
        data=json.dumps(payload).encode(),
        headers={"api-key": KEY, "User-Agent": "hive80lab-publisher/1.0", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            art = json.loads(r.read().decode())
        print(f"OK {url.rsplit('/',1)[1]} -> id={art.get('id')} url={art.get('url')}")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} {url.rsplit('/',1)[1]}: {e.read().decode()[:200]}")