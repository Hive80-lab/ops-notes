#!/usr/bin/env python3
"""dev.to #238 publisher - 13-week cash flow forecast via API rail (browser UA required)."""
import json, urllib.request
KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
CANON = "https://hive80-lab.github.io/ops-notes/13-week-cash-flow-forecast.html"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
API = "https://dev.to/api/articles"

BODY = """**The weekly hour that ends the overdraft surprise.** Most small businesses discover their cash position the way you discover a low tyre: at the worst possible moment, and only once it has already cost something. The P&L says the business is fine; the bank says Tuesday is a problem; and the gap between the two is timing — invoices that age while payroll and the BAS sit on fixed dates.

The fix is one spreadsheet tab, four rows, thirteen Mondays, and one hour a week. Here is the whole system.

## Why thirteen weeks — not a month, not a year

- **A month is too short.** It hides the week inside the month where payroll, rent and the tax instalment land together. Businesses don't run out of money "in March"; they run out on the Thursday of week 5.
- **A year is too vague.** An annual budget is a set of opinions. At thirteen weeks the inputs are named invoices and dated runs — commitments, not hopes.
- **Thirteen weeks is a full quarter.** It catches every recurring beast at least once: rent, payroll, BAS, super, supplier end-of-month terms, the seasonal dip you always forget.
- **It is the length of the future you can still change.** A hole thirteen weeks out has eleven solutions. A hole on Friday has two, and both are phone calls you didn't want to make.

## The four rows — the whole instrument

1. **Cash in.** Only money that clears. Collections by customer, moved to the week you *believe* based on real behaviour — not the due date printed on the invoice.
2. **Cash out.** The five fat lines each get their own row: payroll, rent, suppliers (by terms), tax and super (dated, immovable), and one thin long-tail line for everything else.
3. **Opening balance.** Last week's *actual* closing balance, from the bank's word — never from the forecast.
4. **Closing balance.** Opening + in − out. Colour-coded against a floor you agreed once — commonly four weeks of payroll — not re-litigated on a frightened Friday.

## The Monday, nine o'clock ritual

Pull last week's actuals (5 min) → roll the window one week forward (2 min) → update every invoice promise to the week it will *really* clear (10 min, the highest-value ten minutes of the hour) → scan the thirteen closing Mondays and decide on any amber or red week *today* → write one line about what moved and what you're watching.

Same hour, same chair, one owner. A forecast that updates "when there's time" is a spreadsheet of the dead; the ritual is the instrument.

## The three rules that keep it honest

- **Book the cheque, not the promise.** "He always pays around the 15th" goes in on the 15th only if it has cleared there three months running. Collection optimism is the #1 corruption of small-business forecasts.
- **The tax calendar is rows, not weather.** BAS, super and payroll tax are the most predictable numbers in the business — every quarter, same shape. If they surprise you, they were never rows.
- **The floor is agreed once, in writing.** Four weeks of cover, or whatever your nerves require — decided on a calm Monday, not negotiated on a frightened one.

## Worked example — the joinery contractor's week 5

A nine-person joinery contractor, $1.9M revenue, profitably busy for years — and every quarter there was still a fortnight where the owner checked the account before payroll ran. One wet Monday he built the sheet: two hours, four rows. **Week 5 closed red: a $68,400 hole** — three progress claims, payroll and the BAS instalment all landing on the same days.

Because it was week 5 and not Friday, there were eleven options: two claims invoiced same-day instead of "when the site wraps", the timber order moved onto 30-day terms agreed in one phone call, and a discretionary $9,800 hire moved three weeks right. **Week 5 closed at +$11,200.** Payroll never checked the weather again; the overdraft was cancelled at renewal because it hadn't been touched. His line: *"The hole was always there. The only thing that changed is that I met it eleven weeks early, with options, instead of on the day, with none."*

## Free tools for this

The full page — with the four-row template spec, the floor rule, and the five traps (profit-vs-cash, tax-as-weather, collection optimism, the sheet built once and never rolled, three owners and no owner) — is free on the site:

👉 **[The 13-Week Cash Flow Forecast — full playbook](https://hive80-lab.github.io/ops-notes/13-week-cash-flow-forecast.html)**

If you want the paid versions of this thinking:

- **[The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes)** — free incident quick-start checklist
- **[Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit)** — incident response for small teams — $14
- **[Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2)** — advanced incident response & communications — $27
- **[Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle)** — all 5 kits in one download — $49

*Related reading: the [debtor days monthly review](https://hive80-lab.github.io/ops-notes/debtor-days-monthly-review.html) is the truth about how fast receivables really turn into cash; the [cash runway checklist](https://hive80-lab.github.io/ops-notes/cash-runway-checklist.html) is the survival instrument this forecast keeps you from ever needing; the [supplier payment terms checklist](https://hive80-lab.github.io/ops-notes/supplier-payment-terms-checklist.html) is the lever on the outflow side.*
"""

payload = {"article": {
    "title": "The 13-Week Cash Flow Forecast for Small Businesses: The Weekly Hour That Ends the Overdraft Surprise",
    "published": True,
    "tags": ["smallbusiness", "cashflow", "finance", "management"],
    "description": ("Four rows, thirteen Mondays, one hour: the forecast that finds the cash hole "
                    "eleven weeks early — plus the five traps that turn a spreadsheet into a decoration."),
    "canonical_url": CANON,
    "body_markdown": BODY,
}}
json.dump(payload, open("devto_payload_238.json", "w"), indent=1)

def main():
    key = open(KEY_PATH).read().strip()
    data = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=data, method="POST", headers={
        "api-key": key, "Content-Type": "application/json",
        "User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            out = json.loads(r.read().decode())
            print("POSTED", out.get("id"), out.get("url"), "| published:", out.get("published"))
    except Exception as e:
        print("ERR", e)
        b = getattr(e, "read", lambda: b"")()
        if b: print(b.decode()[:400])
if __name__ == "__main__":
    main()
