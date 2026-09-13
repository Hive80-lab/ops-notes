#!/usr/bin/env python3
import json, urllib.request, sys

KEY = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
URL = 'https://hive80-lab.github.io/ops-notes/refrigeration-temperature-log.html'

body = """Fridges don't fail all at once. They fail slowly — a torn gasket, a blocked condenser, a tired compressor — and every one of them sends a warning reading days before the food is at risk. The [equipment downtime log](https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html) tells you what a breakdown cost after it happens; the [refrigeration temperature log](https://hive80-lab.github.io/ops-notes/refrigeration-temperature-log.html) is how you almost never write one.

Full template on the site: [The Refrigeration Temperature Log](https://hive80-lab.github.io/ops-notes/refrigeration-temperature-log.html)

## Why twice a day — the drift arithmetic

A walk-in with a failing gasket does not jump from 38°F to 55°F overnight; it creeps — 38 on Monday, 40 by Wednesday, 43 by Friday morning, and by Friday dinner the milk is past saving. One check a day can still miss a full day of drift, and the unit that warms overnight is the classic failure: checked at 07:00 and 16:00, an overnight compressor failure surfaces at the morning read, not at the smell.

Two reads a day cap the exposure window at roughly twelve hours — and the morning read plus a pre-service read catches the one mode that matters most: *a unit that was fine at close and dead by open*, exactly when the stock is fullest and the day is busiest.

## One row per unit, per check — eight columns

1. **Date and time** — the *actual* time of the reading. 07:05 logged as 07:00 is the first small lie, and small lies are where logs die.
2. **Unit and ID** — named as the maintenance records name it ("Walk-in #2", not "the big fridge"), so the log line, the [downtime log](https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html) line and the [work order](https://hive80-lab.github.io/ops-notes/maintenance-work-order-template.html) all tell one story.
3. **Air temperature** — the unit's display or a probe mid-shelf, door closed two minutes first.
4. **Food temperature** — probe into product, or a thermal bottle standing in the worst spot. This is the number the health code cares about.
5. **Initials** — a real person, every read. Accountability is the difference between a log and a decoration.
6. **OK / flag** — one checkbox. A flag is not a failure; it is a recheck.
7. **Action line** — only when flagged: what was done, what was found.
8. **(and the clipboard lives by the walk-in door)** — the sheet on the floor is the one that gets filled; the spreadsheet in the office is not.

## Air versus food — the two readings that disagree usefully

Air temperature swings on purpose: every door opening, every defrost cycle, every hot sheet pan parked in front of the evaporator moves the air read 5–10 degrees for twenty minutes. Air is the early signal, **noisy by design**.

Food temperature is the **truth** — product warms and cools slowly, averaging the swings. Probe the warmest realistic load: the door shelf, the top rail, the milk at the front — not the back corner where the air never touches.

The pair is what makes the log diagnostic:

- **Air high, food fine** → usually behavior (door discipline, a blocked fan, lunch rush). Recheck.
- **Air high, food climbing** → a machine losing: gasket, coil, refrigerant, compressor. Start the clock.

Logging only the air gives you a week of false alarms; logging only the food gives you a week of silence before a real failure. Both numbers, same row.

## The limits and the danger-zone clock

- **Cold holding: 41°F (5°C) or below** for TCS foods — dairy, meat, cut produce, cooked rice, dressings.
- Walk-in target: **38°F or below**, so the unit has headroom before it breaks the limit.
- Freezer: **0°F (−18°C)** or below — freezer burn is a cost problem, not a safety one.
- A flagged read starts the **4-hour danger-zone clock**, and the clock starts *on paper* — the action line records the time of the first out-of-range read, because "it was probably only warm for a bit" is exactly what the inspector is trained to test.

## The flag rule — fifteen minutes

Any out-of-range read gets one recheck 15 minutes later with the same probe. Still out of range, or climbing? That is a work order, not a wait: run the [cold-chain failure checklist](https://hive80-lab.github.io/ops-notes/cold-chain-failure-checklist.html), open a [work order](https://hive80-lab.github.io/ops-notes/maintenance-work-order-template.html), and start moving product to the healthy unit if the food is at risk.

## The Sunday walk — thirty minutes that save the week

Once a week, with the log in hand: the dollar-bill test on every door gasket (it should grip), a look at the condenser coil for dust, a confirming thermometer against the unit's display, and the honest answer to "has this unit flagged twice this week?" — because two flags is a pattern, and a pattern is a [work order](https://hive80-lab.github.io/ops-notes/maintenance-work-order-template.html) before it is a loss.

## Inspector day — the 30-second answer

"Show me your temperature logs." The binder opens to six months of unbroken rows, flags with their action lines, and rechecks that came back in range. Honest flags beat magic zeros every time — a page of perfect 38s with no action lines reads as fiction, and inspectors know it.

## The five traps

- **Air-only logging.** A week of false alarms, then log-blindness right before the real failure.
- **Backfilling.** Two reads at 16:00 is not a log; it is a memory test you will fail on the day it matters.
- **The magic pen.** Every read in exactly the same handwriting at exactly the same temperature. Nobody believes it — least of all the inspector.
- **One log for five units.** Rows blur, units get skipped. One row per unit, per check.
- **The sheet in the office.** The log lives on the floor by the walk-in door, or it doesn't live.

## Worked example — the 40-seat restaurant's Tuesday

07:05: walk-in #2 reads **air 43°F, food 41°F**. The food is at the limit but the air says the unit is struggling — flag, action line, recheck 15 minutes. 07:20: air 43°F, food 41.5°F — climbing. The [downtime log](https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html) pattern from last quarter said this exact signature was a torn door gasket. Work order **#0143** opens at 07:30, the $45 gasket goes on the parts order before service, and the alternative — the same failure missed until Friday dinner — is the **$7,300 quarter** already sitting in the log's history.

---

**Kits** — the paid tools behind the free advice:

- [The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) — free incident quick-start checklist
- [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit) — incident response for small teams — $14
- [Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) — advanced incident response & communications — $27
- [Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle) — all 5 kits in one download — $49
"""

payload = {
    "article": {
        "title": "The Refrigeration Temperature Log — The Twice-a-Day Sheet That Keeps the Stock Alive and the Inspector Happy",
        "published": True,
        "body_markdown": body,
        "canonical_url": URL,
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
    r = urllib.request.urlopen(req, timeout=60)
    d = json.load(r)
    print("201 id=%d url=%s" % (d["id"], d["url"]))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read()[:300].decode(errors="replace"))
    sys.exit(1)
