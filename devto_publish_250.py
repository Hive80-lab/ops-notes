#!/usr/bin/env python3
import json, urllib.request, sys

KEY = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
URL = 'https://hive80-lab.github.io/ops-notes/maintenance-work-order-template.html'

body = """The [equipment downtime log](https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html) counts what broke and what it cost. The [preventive maintenance schedule](https://hive80-lab.github.io/ops-notes/preventive-maintenance-schedule-template.html) books what should happen next. The work order is the piece between them that most small operations never write down: the actual job. Not a text message, not a shout across the floor, not "I'll get Dave to look at it" — a numbered, one-page ticket that says who owns it, what it will take, and whether it ended.

Full template on the site: [The Maintenance Work Order](https://hive80-lab.github.io/ops-notes/maintenance-work-order-template.html)

## The eight fields — written at hand-off, not from memory

1. **Number and date.** Every ticket gets a number, even the fifteen-minute ones — it's what the invoice, the part and the log line all reference.
2. **Asset and number.** "The walk-in" is not an asset; "Walk-in cooler #2, 2019 Beck" is.
3. **The complaint in the operator's own words.** "It's making a noise again" is data. Quote it; don't translate it into jargon until the diagnosis line is written.
4. **Priority.** P1, P2 or P3, set by downtime cost. Not by loudness, not by rank.
5. **Assigned tech and parts.** A named person — "whoever's free" is nobody — and parts reserved from the [critical spares shelf](https://hive80-lab.github.io/ops-notes/critical-spare-parts-list.html) against this ticket number.
6. **Work performed.** What was actually done, in words the next tech could repeat: replaced, torqued, tested, observed for one full cycle.
7. **Downtime hours and cost.** Both clocks — lost production and wrench time — matching the downtime log.
8. **Preventable, Y/N, plus one line.** The sentence that feeds the PM schedule. If it's blank, the ticket closed a job but taught nothing.

## Priority is arithmetic, not volume

- **P1 — down now, or about to be.** Production stopped, a safety issue, or the cold chain at risk. Everything drops, parts come off the shelf, the log line opens the same hour.
- **P2 — inside 48 hours.** Degraded, intermittent, or the failure mode that ended another machine last quarter.
- **P3 — the schedule's next slot.** Cosmetic or pure prevention. It goes on the schedule and stops occupying anyone's head.

The rule that makes the levels real: *the downtime log's cost column decides, not the loudest voice in the room.*

## Close-out: the machine running is not the job done

A work order is finished when four things are true — the [downtime log](https://hive80-lab.github.io/ops-notes/equipment-downtime-log.html) line is closed with hours and cost; the parts are off the shelf and reordered; the preventable line has become a task on the [PM schedule](https://hive80-lab.github.io/ops-notes/preventive-maintenance-schedule-template.html); the invoice is attached to the ticket number. No close-out, no ticket.

## The five traps

- **Verbal work orders.** "Just tell Dave" is how a repeat failure stays invisible. If it isn't on a page, it will happen again on a Saturday.
- **The ticket without a close-out.** Half of December's open tickets are finished jobs nobody closed.
- **Priority inflation.** When everything is P1, the genuinely-down machine waits behind a squeaky fan.
- **One giant ticket.** "Fix the kitchen" is not a work order; it's a wish.
- **The invisible backlog.** Tickets scattered across a whiteboard and three texts can't be triaged — one numbered list, or the [uptime budget](https://hive80-lab.github.io/ops-notes/uptime-downtime-budget.html) is spent by whoever shouts first.

## Worked example — the 40-seat restaurant's third "just tell Dave"

The walk-in cooler has stopped three times in six weeks; the Friday triage already flagged it. Monday 07:10 the prep cook logs "compressor short-cycling again, food temp creeping." Work order **#0142, priority P1** — cold chain at risk, not because the cook shouted. 07:20 assigned to Dave by name, spare gasket reserved from the shelf against #0142. 08:00 the door gasket is off, torn along the hinge edge — same failure mode as last time, now undeniable. 10:30 close-out: log line closed at **2.5 lost-production hours** (brunch moved to ice chests, 40 covers saved), **$45 part** plus 90 minutes of Dave, invoice stapled, and the line that pays for the whole page: *preventable Y — add weekly door-gasket and defrost check to the [cold-chain walk](https://hive80-lab.github.io/ops-notes/cold-chain-failure-checklist.html); reorder spare gasket (bin empty).*

Total paperwork: one page, eight minutes. The alternative is exactly how the first quarter became six events and **$7,300 of lost revenue** nobody could prove.

---

**Kits** — the paid tools behind the free advice:

- [The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) — free incident quick-start checklist
- [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit) — incident response for small teams — $14
- [Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) — advanced incident response & communications — $27
- [Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle) — all 5 kits in one download — $49
"""

payload = {
    "article": {
        "title": "The One-Page Work Order That Turns 'It's Making a Noise' Into 'Fixed, Costed, Prevented'",
        "published": True,
        "body_markdown": body,
        "canonical_url": URL,
        "tags": ["maintenance", "smallbusiness", "operations", "productivity"],
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
