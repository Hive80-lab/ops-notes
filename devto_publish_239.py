#!/usr/bin/env python3
"""dev.to #239 publisher - purchase order process via API rail (browser UA required)."""
import json, urllib.request
KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
CANON = "https://hive80-lab.github.io/ops-notes/purchase-order-process-small-teams.html"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
API = "https://dev.to/api/articles"

BODY = """**The five-minute step that stops the surprise invoice.** Every small business has received the invoice nobody remembers ordering. Not fraud, usually — a tech ordered a compressor from the ute on Tuesday, the office met it three weeks later as a $9,400 line in the month-end stack. Approval and commitment travel by conversation; payment arrives on paper. The purchase order is the bridge between the two.

Here is the whole system, sized for a five-person shop — one page, seven lines, one threshold.

## The seven lines every PO carries

1. **PO number** — sequential, one series, never reused. The number is the spine.
2. **Supplier** — the legal name, not the rep's first name.
3. **What and how much** — description, quantity, unit price. Specific enough that a stranger could deliver it.
4. **Agreed price and terms** — the number you were quoted. If the quoted price isn't on the PO, the PO didn't happen.
5. **Job or cost code** — where the spend will live in the books. This line is what halves your month-end close.
6. **Approver** — a name, written down. Not a vibe.
7. **Date and delivery instructions** — so "it never arrived" has a place to be answered.

Sent to the supplier *before* the order is placed, it converts your side's conversation into the supplier's expectation — the only document that outranks the invoice at its own game.

## The threshold that keeps it out of the way

- **Under $500:** card it, claim it through the expense policy. No PO. The process exists for the large and the repeated, not the $40 box of fittings.
- **Over $500, one-off:** PO before order. Five minutes.
- **Recurring, any size:** one standing PO per supplier per quarter — the monthly service, the consumables, the hire fleet. One number, twelve deliveries.
- **Genuine urgency:** buy now, text the approver, raise the PO the same day. Fast is fine; silent is not.

## The three-way match — where ghost invoices die

Invoice arrives → one question: does it match? Compare **PO** (what was approved), **delivery docket** (what arrived), **invoice** (what's claimed). All three agree → pay on terms, book to the job code. They don't → one line of query naming the mismatch — never "pay and hope", never a silent deduction.

The match takes two minutes per invoice and reliably kills the three classics: the duplicate (same invoice, two numbers), the drift (delivered price creeps above PO price), and the phantom (delivered to an address you don't own).

## The weekly ten minutes

Same sitting as the 13-week cash forecast: read out every supplier invoice with no PO beside it. Each gets an answer — matched, backdated, or queried. Unapproved commitments are the reason your forecast's outflow row is fiction. Ten minutes a week and the surprise invoice goes extinct.

## The five traps

- **The verbal PO culture.** "Dave from site rang it through" is a story, not an approval.
- **The retroactive rubber stamp.** Raising a PO to *cover* an invoice that already arrived rewrites history and hides the gap the number exists to expose.
- **Number chaos.** Two ranges, reused numbers, "quote #4-1b". One series, one owner, no reuse.
- **The threshold nobody respects.** A $500 limit with $499 orders twice a week is an invitation, not a control.
- **Procurement theatre.** Twelve approval steps for a box of gloves. The whole process is one page. If it takes longer than the order, it dies by Christmas.

## Worked example — the HVAC contractor's $9,400 compressor

A fourteen-person HVAC service company, $4.2M revenue, profitable every year — and a pattern the owner called "the invoice ambush": spend committed by techs in the field, invoices landing at month-end for jobs already priced and forgotten. One quarter carried $2,300 of unreconcilable supplier spend, and a $9,400 compressor ordered by phone in a heatwave blew a hole in week 3 of the cash plan nobody knew existed until the statement came.

The fix took one Sunday: the seven-line PO on a single printed page, the $500 threshold, standing POs for the four recurring suppliers, the ten-minute unapproved-invoice list bolted onto Monday's cash-forecast hour. One quarter later: **unreconcilable spend $0**, the close two hours faster (every invoice arriving pre-coded to a job), and the forecast's outflow row believed for the first time. His verdict: *"I thought POs were for companies with procurement departments. It turns out they're for companies with utes."*

## Free tools for this

The full page — seven-line PO spec, threshold rules, the match procedure, and the traps — is free on the site:

👉 **[The Purchase Order Process for Small Teams — full playbook](https://hive80-lab.github.io/ops-notes/purchase-order-process-small-teams.html)**

If you want the paid versions of this thinking:

- **[The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes)** — free incident quick-start checklist
- **[Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit)** — incident response for small teams — $14
- **[Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2)** — advanced incident response & communications — $27
- **[Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle)** — all 5 kits in one download — $49

*Related: the [supplier payment terms checklist](https://hive80-lab.github.io/ops-notes/supplier-payment-terms-checklist.html) governs the timing side; the [13-week cash flow forecast](https://hive80-lab.github.io/ops-notes/13-week-cash-flow-forecast.html) is what approved commitments feed; the [expense reimbursement policy](https://hive80-lab.github.io/ops-notes/expense-reimbursement-policy.html) is the card-side sibling.*
"""

payload = {"article": {
    "title": "The Purchase Order Process for Small Teams: The Five-Minute Step That Stops the Surprise Invoice",
    "published": True,
    "tags": ["smallbusiness", "management", "finance", "operations"],
    "description": ("The seven-line PO, the threshold that keeps it out of the way, and the three-way "
                    "match that kills duplicate and phantom invoices — sized for a five-person shop."),
    "canonical_url": CANON,
    "body_markdown": BODY,
}}
json.dump(payload, open("devto_payload_239.json", "w"), indent=1)

def main():
    key = open(KEY_PATH).read().strip()
    data = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=data, method="POST", headers={
        "api-key": key, "Content-Type": "application/json",
        "User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            out = json.loads(r.read().decode())
            print("POSTED", out.get("id"), out.get("url"))
    except Exception as e:
        print("ERR", e)
        b = getattr(e, "read", lambda: b"")()
        if b: print(b.decode()[:400])
if __name__ == "__main__":
    main()
