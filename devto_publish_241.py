import json, urllib.request

KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
CANON = "https://hive80-lab.github.io/ops-notes/bank-reconciliation-checklist.html"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
API = "https://dev.to/api/articles"

BODY = """**Your books say one cash number. The bank says another. One of them is wrong, and it is never the bank.** A bank reconciliation is the weekly thirty minutes that explains every dollar of that gap — and the gap is where duplicate payments, unrecorded fees, phantom receipts, and the first $9.90 of a fraud all live. Small teams skip it because it looks like accounting hygiene. It is cash control: the single number every other decision trusts — runway, reorder timing, whether you can hire.

Full checklist on the site: [Bank Reconciliation — the 30-minute ritual](https://hive80-lab.github.io/ops-notes/bank-reconciliation-checklist.html). Here is the whole ritual.

## The two cash numbers, and where the gap hides

The books say what you *did*. The statement says what *happened*. Every dollar of difference between them is one of five things: money that left and the books missed, money the books recorded but that never arrived, a payment that happened twice, a timing difference that will clear, or theft. The [13-week cash flow forecast](https://hive80-lab.github.io/ops-notes/13-week-cash-flow-forecast.html) runs on one iron rule — cash in only when it clears — and reconciliation is what makes that rule enforceable. An unreconciled balance overstates the week-6 row by exactly the size of the gap.

## The thirty-minute ritual — weekly beats monthly beats never

1. **Pull the statement and mark every line that cleared.** Auto-match proposes; you dispose. Do not let a clean import feel like a finished reconciliation.
2. **Collect the statement lines with no book entry.** Card fees, debit orders, reversals, chargebacks — the outflows your books are missing.
3. **Collect the book entries with no statement line.** Invoices recorded but never paid, bounced direct debits, deposits recorded on a promise. The inflows your books invented.
4. **Age the unmatched list.** Two statements old or older is not timing — it is a hole. Holes get an owner and a deadline.
5. **Fix the books, never the bank.** Then fix the process that let the error through. The error is the symptom; the process is the patient.
6. **Feed the forecast and sign it.** Findings become forecast rows the same day; the reconciliation gets initials and a date. An unsigned reconciliation is a rumour.

## The five finds

- **The duplicate payment** — the vendor paid twice, the card swap that re-ran a subscription.
- **The unrecorded outflow** — processor fees, debit orders, reversals: the recurring leak that never has an invoice.
- **The money that never landed** — the failed debit still sitting as revenue. Receivables and revenue are both overstated until caught.
- **The fraud seed** — the $9.90 charge nobody recognises. Card testers start small because nobody reconciles.
- **The honest timing** — cheques genuinely in flight: dated, named, expected. Shrink this pile so the other four have nowhere to hide.

## Three honesty rules

- **The bank is the truth; the books travel to meet it.** A "balancing adjustment" with no explanation is a symptom written in numbers — permitted exactly never.
- **Unreconciled is a date, not a state.** "Unmatched since Sep 3" ages and demands attention. Write dates, not labels.
- **The reconciliation feeds the forecast or it is theatre.** Findings that stay in the sheet change nothing.

## The five traps

- **The year-end big bang.** Once a year is archaeology, not control: twelve months of drift, zero early catches.
- **Matching books to books.** Reconciling the spreadsheet to the spreadsheet proves only that you copied consistently. The statement is the only independent witness.
- **The small unrecognised charge, ignored forever.** Too small to chase, exactly the right size to test whether anyone is watching. The next one is never $9.90.
- **Auto-match trust.** The matches are the easy 95%; the exception list is the entire point.
- **Reconciling only when the accountant asks.** The ritual belongs to the business, not the tax calendar. April finds nothing a weekly half hour would not have found in September.

## Worked example — the nine-person Shopify brand with the $8,450 gap

A nine-person e-commerce brand, $2.1M revenue, reconciling "whenever the accountant chased". Books said **$48,200 cash; the bank said $39,750** — an $8,450 gap growing since April. One reconciliation found it all: processor fees double-billed since April ($2,180), a failed direct debit still recorded as received ($1,900), a vendor invoice paid twice during a card swap ($2,600), a mystery subscription charging monthly ($340/month, $1,020 gone), and unrecorded debit orders ($770).

Fees recovered, duplicate refunded, failed debit re-collected, subscription killed. The bigger repair was the forecast: overstated by $8,450 the whole time. Once the cash number was true, the week-6 row moved from comfortable to red and a reorder got deferred a week *on purpose* instead of by surprise. Weekly thirty-minute reconciliation ever since. The owner's verdict: *"The number I was running the business on was six months old."*

---

*Related: the [month-end close](https://hive80-lab.github.io/ops-notes/monthly-close-checklist.html) starts from a reconciled balance; the [cash runway checklist](https://hive80-lab.github.io/ops-notes/cash-runway-checklist.html) divides by a cash number that is only as honest as this ritual; and the [budget vs actuals review](https://hive80-lab.github.io/ops-notes/budget-vs-actuals-monthly-review.html) compares against closed, reconciled books — never against a bank feed.*
"""

payload = {"article": {
    "title": "Bank Reconciliation: The 30-Minute Ritual That Keeps Your Cash Number Honest",
    "published": True,
    "tags": ["smallbusiness", "finance", "accounting", "management"],
    "description": ("Six steps, the five finds, and the three honesty rules behind the weekly thirty minutes "
                    "that explains every dollar between your books' cash and the bank's cash — plus the Shopify "
                    "brand whose cash number had been overstated by $8,450 since April."),
    "canonical_url": CANON,
    "body_markdown": BODY,
}}
json.dump(payload, open("devto_payload_241.json", "w"), indent=1)

def main():
    key = open(KEY_PATH).read().strip()
    data = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=data, method="POST", headers={
        "api-key": key, "Content-Type": "application/json",
        "User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.load(r)
            print("HTTP", r.status, "id", res.get("id"), "url", res.get("url"))
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode()[:500])

if __name__ == "__main__":
    main()
