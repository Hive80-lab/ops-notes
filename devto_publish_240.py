import json, urllib.request

KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
CANON = "https://hive80-lab.github.io/ops-notes/budget-vs-actuals-monthly-review.html"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
API = "https://dev.to/api/articles"

BODY = """**The plan and the bank statement have nothing to say to each other — until you give them one hour a month.** Most small businesses write a budget once, in a burst of January energy, and never open it again. The budget was never the point. The *comparison* is the point: three columns, one threshold, thirty minutes, once a month. That hour is where a creeping cost is caught in month two instead of month ten.

Full checklist on the site: [Budget vs Actuals — the monthly hour](https://hive80-lab.github.io/ops-notes/budget-vs-actuals-monthly-review.html). Here is the whole ritual.

## Three columns and one threshold

Every line gets **budget**, **actual**, **variance** — dollars *and* percent, sign included (under-budget is not automatically good; starved marketing will invoice you later). Then the rule that keeps the hour to an hour:

> Any line off by more than **10% or $500, whichever is smaller**, gets a written one-line cause and a one-line action. Everything else is allowed to be fine this month.

Why both measures: a $180 variance on a $2,000 line is noise; a $180 variance on a $200 line is a fire. Percent catches small-line explosions, dollars catch big-line drift.

## The five lines worth reading first

1. **Revenue** — off by 10%+? Either the plan was fiction or the market moved. Both are worth knowing in month two.
2. **Gross margin** — the most underrated line in small business. Materials creep, subcontractor creep, and every scope increase you absorbed for free hide here.
3. **Payroll** — usually the biggest line and the slowest to fix. It compounds monthly.
4. **Rent and fixed overhead** — boring on purpose. These lines exist to be flat; movement is always worth the question.
5. **One discretionary line on rotation** — travel, software, marketing. Rotate monthly; it's where budgets quietly leak.

Forty-line variance reviews die by March. Five lines read with intent survive.

## The ritual — thirty minutes, same sitting as the close

1. Pull actuals from the **finished** close, never the raw bank feed — comparing against half-closed books is how phantom variances are born.
2. Mark every line past the threshold. Two to five lines is healthy. More than eight means the coding is drifting — fix the instrument before trusting the reading.
3. One line per variance: cause, then action. *"Fuel +22% — two country jobs; recharge travel on those jobs."*
4. Roll the lesson forward: a **permanent** change (new wage rate, new supplier price) updates the remaining months of the budget. A **one-off** (repair, event) does not — over-reacting to one-offs is how a budget stops matching reality within a quarter.
5. Feed the 13-week cash forecast the same day: anything now known-committed becomes an outflow row.

## Three honesty rules

- **The budget is a decision record, not a wish.** If actuals beat plan six months running, the plan was wrong in an interesting way.
- **Never re-forecast the gap away.** Mid-year "re-baselines" that move the budget down to meet the actuals are how a dying margin hides. Once a year, in writing, reason named.
- **Classify once, consistently.** Half of all variances are not performance — they're inconsistent coding that vanishes the day the same invoice always lands in the same line.

## The five traps

- **The built-and-shelved budget.** A budget without a monthly hour is a New Year's gym membership.
- **Variance theatre.** Reading all forty lines aloud. Five lines read deeply beats forty read shallowly.
- **Fixing the number instead of the cause.** Reclassifying your way out of a payroll variance. The problem keeps drawing wages.
- **"It's just timing."** Sometimes true. Excused three months running, it's a trend wearing a disguise.
- **Nobody owns a line.** "The budget" belongs to everyone, so every variance belongs to no one. Each movable line gets one name beside it.

## Worked example — the cleaning company's two un-repriced contracts

An eleven-person commercial cleaning business, $1.6M revenue, forty sites. Payroll budgeted at 46% of revenue; month two actuals landed at 53% — a $5,800 variance. The old way absorbed it as "wages went up". The new way forced a cause: two fixed-price contracts that had quietly grown — one client added two floors and a weekend service and the price never moved; the other crept from three nights a week to five across a year of polite yeses. Together they were running **38% over contract hours**.

Re-quoted both at renewal: **+$3,100/month, roughly $37k a year** that had been leaking for an estimated fourteen months before the first review caught it. The owner's verdict: *"The budget didn't find the problem. The hour did. I'd just never given it the hour."*

---

*The [annual ops budget template](https://hive80-lab.github.io/ops-notes/annual-ops-budget-template.html) is where the budget column comes from; the [month-end close](https://hive80-lab.github.io/ops-notes/monthly-close-checklist.html) produces the actuals; the [13-week cash flow forecast](https://hive80-lab.github.io/ops-notes/13-week-cash-flow-forecast.html) is the cash-side twin; and the [debtor days review](https://hive80-lab.github.io/ops-notes/debtor-days-monthly-review.html) is the same ritual pointed at receivables.*
"""

payload = {"article": {
    "title": "Budget vs Actuals: The Monthly Hour That Tells You If You\u2019re Running the Business You Planned",
    "published": True,
    "tags": ["smallbusiness", "management", "finance", "accounting"],
    "description": ("Three columns, a variance threshold, the five lines worth reading first, and the thirty-minute "
                    "ritual that catches creeping costs in month two \u2014 plus the cleaning company whose payroll "
                    "creep was two un-repriced contracts."),
    "canonical_url": CANON,
    "body_markdown": BODY,
}}
json.dump(payload, open("devto_payload_240.json", "w"), indent=1)

def main():
    key = open(KEY_PATH).read().strip()
    data = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=data, method="POST", headers={
        "api-key": key, "Content-Type": "application/json",
        "User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.load(r)
            print("HTTP", r.status, "id", res.get("id"), "url", res.get("url"),
                  "published", res.get("published"))
    except urllib.error.HTTPError as e:
        print("HTTPError", e.code, e.read()[:300])

if __name__ == "__main__":
    main()
