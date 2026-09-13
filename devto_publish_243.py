import json, urllib.request

KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
CANON = "https://hive80-lab.github.io/ops-notes/weekly-ops-review.html"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
API = "https://dev.to/api/articles"

BODY = """**Operations fail in increments, not explosions.** The pick accuracy that slides from 99.4% to 98.1% over three weeks is invisible on any single day. The refund rate that creeps from 1.2% to 2.8% is a rounding error on Monday and a churn cause by the quarter. No dashboard alerts catch a slide this gentle, because alerts watch thresholds and slides live *between* thresholds. The weekly ops review exists to catch the slide: one meeting, thirty minutes, the same six items in the same order, every week.

Full playbook on the site: [Weekly Ops Review \u2014 the thirty minutes that keep a small operation honest](https://hive80-lab.github.io/ops-notes/weekly-ops-review.html). Here is the whole ritual.

## This is not a status meeting

Status meetings report what already happened to people who could have read it. The weekly ops review is a *control* meeting: it compares this week against the plan and against last week, forces each divergence to get an owner and a next action, and produces exactly two kinds of output \u2014 **a decision, or a date**. Anything else (observations, vibes, "interesting") does not count, because output that changes nothing is just a meeting with better punctuation. It pairs with the financial cadences \u2014 the [monthly budget vs actuals review](https://hive80-lab.github.io/ops-notes/budget-vs-actuals-monthly-review.html) and the weekly [13-week cash flow forecast](https://hive80-lab.github.io/ops-notes/13-week-cash-flow-forecast.html) read the money; this one reads the machine that earns it.

## The agenda \u2014 six items, thirty minutes, never reordered

1. **The number that matters this quarter** (5 min). One metric, chosen once per quarter, printed on the agenda itself. This week's value, last week's value, the trend arrow, one sentence of cause. If nobody can say why it moved, that *is* the finding.
2. **Incidents and near-misses** (5 min). One line each: what happened, what it cost, is it closed. Near-misses count double \u2014 they are free tuition. Anything structural goes to the [incident post-mortem template](https://hive80-lab.github.io/ops-notes/incident-post-mortem-template.html), not this meeting.
3. **The promises ledger** (5 min). Open commitments from last week, read aloud: done, moving, or slipped. A slipped promise is a data point about the promise (too big), the owner (wrong one), or the week (false capacity). Re-date it or shrink it; never silently carry it.
4. **Process changes shipped this week** (5 min). Announced so the whole room knows the current truth \u2014 unannounced process change is how teams run three different businesses. Each change gets a two-week check-in date.
5. **The coming week's known pressure** (5 min). The volume spike, the key person out, the supplier's long weekend \u2014 named before they land, mitigation pre-decided while it is still cheap.
6. **One improvement, chosen** (5 min). Not the best improvement \u2014 the one that will really get done. One per week is fifty a year, which compounds; ten "someday" per week is zero a year.

Thirty minutes, hard stop. If an item needs more, it leaves with an owner and a time.

## Three honesty rules

- **The written answer beats the spoken one.** The review's cause lines get written down before anyone moves on; definitions live on the agenda, and changing one is announced like a process change \u2014 because it is one.
- **Bad weeks are reviewed the same as good ones.** The meeting that gets skipped in a firefight is the meeting that was supposed to catch the fire early. "Is this a blip or the new normal" beats three weeks of finding out by invoice.
- **One improvement per week, shipped.** A review that ends with nine good ideas and zero owners was a brainstorm wearing a meeting's clothes. Throughput beats enthusiasm every quarter.

## The five traps

- **The status meeting in disguise.** Everyone reports, nobody compares. If no output was ever refused for lacking a decision or a date, the meeting was theatre \u2014 the chair's job is to make one such refusal per week, early.
- **The agenda that flexes to the loudest topic.** One big customer issue eats all thirty minutes and the slide continues in peace. Hot topics get triaged out with an owner and a time, exactly like everything else.
- **The drifting definition.** "On-time" quietly becomes "on-time-ish." Six months of chart, no trend, no catches.
- **The skipped week.** "Nothing happened this week" is the exact week the slide is happening. Crisis week? Run it async: fifteen lines, same six items.
- **The improvement list that never ships.** Twelve items noted, zero shipped, forever. Fifty small true improvements a year outrun one grand reorganization that never happened.

## Worked example \u2014 the warehouse that caught its own slide

A nine-person e-commerce operation ran a Friday 09:30 review with this agenda. The quarter's number was pick accuracy: 99.4%, then 98.9%, then 98.1% \u2014 the trend arrow turned orange and demanded its sentence of cause. Two questions found it: a new starter on the pick line unsupervised during a holiday week, plus a re-sequenced pick-face. Output: a decision (shadow-pairing for new starters, pick-face changes frozen without a second pair of eyes, logged in the [decision log](https://hive80-lab.github.io/ops-notes/decision-log-template.html)), a date (re-check Friday, target back over 99%), and the week's one improvement (a five-minute end-of-shift count on the two worst SKUs). Three weeks later: accuracy held 99.5%, wrong-item refunds down from 2.8% to 0.9%, zero added headcount. The counterfactual \u2014 no review \u2014 is the week-five version: same decision, made under fire, wearing an apology.

*Related: the [weekly review checklist](https://hive80-lab.github.io/ops-notes/weekly-review-checklist.html) is the personal-side weekly pass; the [one-on-one meeting template](https://hive80-lab.github.io/ops-notes/one-on-one-meeting-template.html) is the people-side twin of this operation-side review.*
"""

payload = {
    "article": {
        "title": "Weekly Ops Review: The Thirty Minutes That Keep a Small Operation Honest",
        "published": True,
        "tags": ["smallbusiness", "management", "operations", "productivity"],
        "description": ("A fixed six-item agenda, thirty minutes, same slot every week. Three inputs "
                        "(the numbers, the incidents, the promises), two outputs (a decision or a date), "
                        "three honesty rules, and five traps \u2014 plus the nine-person warehouse whose "
                        "Friday review caught a pick-accuracy slide three weeks before it caught them."),
        "canonical_url": CANON,
        "body_markdown": BODY,
    }
}
json.dump(payload, open("devto_payload_243.json", "w"), indent=1)

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
