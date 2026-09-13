import json, os, urllib.request, urllib.error
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')
KEY = open(os.path.expanduser('~/Swarm/hive/state/secure/devto_api_key.txt')).read().strip()
BASE = 'https://hive80-lab.github.io/ops-notes'
URL = f'{BASE}/restaurant-inventory-par-levels.html'

KITS = """
---

Every page ships with a kit block - the paid tools behind the free advice:

- [The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) - free incident quick-start checklist
- [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit) - incident response for small teams - $14
- [Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) - advanced incident response & communications - $27
- [Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle) - all 5 kits in one download - $49

Code **HIVE-LAUNCH30** takes 30% off any kit at checkout.
"""

BODY = f"""One page, one formula, one Friday walk: what you use in a day, how many days until the truck comes, one day of safety stock, minus what is actually on the shelf - that is the order. Par levels are not purchasing sophistication; they are the sheet that turns the [food cost count]({BASE}/food-cost-percentage-tracker.html) into an action. The tracker finds the leak. The par sheet stops reordering the water that leaks out of it.

## The only math on the page

**Par = (weekly usage ÷ 7) × (delivery cycle days + 1 safety day) − on-hand.** Round to case size. That is the entire formula, and every argument about it is an argument about four honest inputs:

- **Weekly usage** - from the purchase invoices, not from memory. One catering week will lie to you for a month; use a rolling three.
- **Delivery cycle** - the real days between drops, not the contract days. The vendor who says "Tuesday and Friday" and delivers "Tuesday and most Fridays" has a three-day cycle some weeks.
- **One safety day** - sized to delivery-day reality. A missed truck on a holiday weekend is a calendar fact, not a math error. Safety is for the missed truck, not for the sale you are nostalgic about.
- **On-hand** - the Friday count. Same shelf walk that feeds the food cost sheet: count first, order second, price third, twenty minutes total.

## The sheet - one row per item, one walk per week

Seven columns per row: **item in vendor units** (cases, bags, each - the math has to speak the vendor's language), **weekly usage**, **real cycle days**, **par**, **on-hand**, **order** (par minus on-hand, rounded to case size, zero if negative), and a **par check** note for the weeks the row surprises you - "salad special," "heat wave," "menu test." Three surprises in a quarter is a par change, not a coincidence.

A row that reads zero two weeks running is telling you the par is too fat. Cut it before the money does.

## The quarterly dead-stock audit

Once a quarter, list every item with its shelf value and how many weeks of usage the shelf holds. Anything over three weeks is dead money wearing a uniform: the lamb shoulder from the winter special, the hearts of palm from the catering bid that never came back, the premium bun the menu abandoned. The audit's output is a decision per row - special it, cut the par, or accept the vendor minimum. Not a spreadsheet; decisions.

## Worked example - the 40-seat restaurant

Same restaurant as the food cost tracker's 34.1% week. The first par audit finds **$2,300 of dead stock**. Then the fixes:

- **Ground beef:** usage 190 lb/week, par 81 lb, ordered as 4×20 lb cases with a standing mid-week top-up. The burger-patty drift from the tracker's example gets a second fix: one random patty weighed per delivery at the door.
- **Romaine:** sold out by 7pm twice in a month - a three-day cycle written as two. Safety day added, par 24 → 30. The Saturday 86 disappears.
- **Produce par cut 15%** behind the repaired walk-in gasket - the spoilage fix from the tracker's example, now permanent in the math instead of remembered in a story.

Net effect: roughly $2,300 freed on day one and about $180 a week back, without buying anything smarter. The par sheet did not buy cleverly; it stopped buying stupidly - which is where most food businesses keep their margins.

## 5 traps (the ones that make the sheet lie)

1. **Set once, never revisited.** A par from opening month is a fossil. The par check column exists so the number learns from the weeks it was wrong.
2. **Ordering by feel.** "We were busy Saturday" is a story; 190 lb is a number. Feel orders double when the rep visits and halves when cash is tight.
3. **Ignoring case sizes.** A par in kitchen units ordering in vendor units rounds every week into drift. Write the par in the unit you order in.
4. **Safety stock sized by fear.** One day is a cushion; five days is a second walk-in you pay rent on.
5. **Letting the vendor set the par.** Their case pack and lead times are inputs. The minimum delivery is their number. The par is yours.

*Related: the [delivery receiving checklist]({BASE}/delivery-receiving-checklist.html) is where the order becomes fact; the [walk-in cooler maintenance checklist]({BASE}/walk-in-cooler-maintenance-checklist.html) keeps the box working; the [refrigeration temperature log]({BASE}/refrigeration-temperature-log.html) protects the money the order just spent; the [weekly ops review]({BASE}/weekly-ops-review.html) is where par misses get decided; and the [purchase order process]({BASE}/purchase-order-process-small-teams.html) covers everything with a PO number.*
"""

payload = {
    "article": {
        "title": "The Par Level & Ordering Guide - The Sheet That Turns Friday's Count Into Monday's Order",
        "published": True,
        "body_markdown": BODY + KITS,
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
    with urllib.request.urlopen(req, timeout=60) as r:
        art = json.loads(r.read().decode())
    print(f"OK par-levels -> id={art.get('id')} url={art.get('url')}")
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()[:300]}")
