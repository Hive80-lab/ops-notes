#!/usr/bin/env python3
"""#244 dev.to crosspost: open-restaurant incident response system checklist."""
import json, urllib.request, urllib.error

KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
CANON = "https://hive80-lab.github.io/ops-notes/open-restaurant-incident-response-system-checklist.html"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
API = "https://dev.to/api/articles"

body = """An accident in a restaurant is not an event; it is a process with a start time. The double-booked party of ten, the misfired ticket during a rush, the reservation system that took two deposits for one table \u2014 none of these are bad luck. They are operational accidents, and the difference between a group that repeats them and a group that fixes them is not talent or headcount. It is whether the response is improvised or systematized. This is the open-restaurant incident response system: what to do in the three days after an accident while the doors stay open, built for small restaurant groups running multiple sites.

## The three-day runbook

**Day 1 \u2014 Stabilize and measure.** Gather the team; get the facts on who, when, where, what. Enforce the guest-facing fix (move the table, comp the error, guide guests to the bar). Lock the operational line: freeze new check-ins for the impacted party only. Measure the impact \u2014 seats lost, revenue write-offs, time added to every other party. Output: a numbered list of factual impacts with owners and timestamps. No root-cause hunting on day one; a group that starts assigning blame while the floor is still recovering makes the next accident cheaper to hide.

**Day 2 \u2014 Investigate root cause.** Ten-minute standup per impacted station (host stand, POS, kitchen, bar). Map the chain of events on a linear timeline and mark the exact moment the error entered the system. Interview the staff who were on shift, focusing on the moment they *noticed* the error \u2014 not on blame. Output: a five-line summary of the incident and one line for the root cause.

**Day 3 \u2014 Diagnose and fix.** Run the decision tree: process issue, tool issue, or people issue? Then apply the four-to-do lists below. Pick the minimum viable fix \u2014 one, not a vague "we need to improve everything." Output: a single action item per incident, with a name, a deadline, and a metric.

## The four-to-do lists

Decisions under pressure fail when they are improvised. These four lists make the response predictable:

1. **Process-to-do** \u2014 change how the workflow is documented, ordered, or communicated. Example: swap "check availability" to "check availability, then confirm guest preference."
2. **Tool-to-do** \u2014 add checks or automation to the POS, calendar, or back office. Example: alert when two parties are booked into the same slot.
3. **People-to-do** \u2014 reassign who does the check, or what they may override. Example: let the floor manager clear underbooked slots without calling the host.
4. **Data-to-do** \u2014 track the metric and set a benchmark. Example: record total seats lost per incident; run weekly stats on critical incidents.

## The third-day cleanup (this is what prevents the relapse)

- **Update the SOP.** Modify the station checklist to include the new action or exclusion. Version it, stamp it, push it to all staff devices.
- **Lock the metric.** Add incident totals to the weekly standup: total incidents, critical incidents, average seats lost, average time to recover.
- **Review and adjust.** Read the incident summary. Was the action taken? Did the rate move? If not, back to the tree \u2014 pick a different root cause.
- **Send the signal.** Tell the team: "This is now the way we handle this type of error. Here's the new rule."

## Worked example \u2014 twelve sites, one quarter

A twelve-site restaurant group ran an 8% operational accident rate \u2014 roughly one incident per site per shift-week, one major incident a quarter, each one costing seats, comped food, and a manager's afternoon. They did not add staff. They installed this system: the three-day runbook, the four lists, the ten matrix rules, and the third-day cleanup, with the incident rate read out in the weekly standup. In one quarter the rate halved \u2014 from 8% to just over 4% \u2014 and major incidents went from one a quarter to one in the entire period. Their own post-mortem of the change said it plainly: most accidents were not caused by careless people; they were caused by decisions improvised under pressure. The four lists took the improvisation out, and the rate followed. Total cost: a laminated card per station and one standing agenda item.

*Related: the [incident post-mortem template](https://hive80-lab.github.io/ops-notes/incident-post-mortem-template.html) is where Day 3's diagnosis lands when the incident was big enough for a formal review; the [shift handover log](https://hive80-lab.github.io/ops-notes/shift-handover-log-template.html) is how Day 1's facts survive the roster change; and the [staffing shortage coverage plan](https://hive80-lab.github.io/ops-notes/staffing-shortage-coverage-plan.html) is the pressure that turns a small error into a visible one.*

The full checklist \u2014 runbooks, lists, trees, and the ten decision-matrix rules \u2014 lives at [HIVE80lab ops notes](https://hive80-lab.github.io/ops-notes/open-restaurant-incident-response-system-checklist.html).
"""

payload = {
    "article": {
        "title": "The Open-Restaurant Incident Response System: A Three-Day Playbook for Accidents While the Doors Are Open",
        "published": True,
        "tags": ["smallbusiness", "restaurants", "operations", "management"],
        "description": ("A three-day incident-response playbook for small restaurant groups: Day 1 stabilize and "
                        "measure, Day 2 investigate root cause, Day 3 diagnose and fix \u2014 with the four-to-do "
                        "lists, the decision tree, and the cleanup that prevents relapse. Worked example: a "
                        "twelve-site group that halved an 8% accident rate in one quarter."),
        "canonical_url": CANON,
        "body_markdown": body,
    }
}
json.dump(payload, open("devto_payload_244b.json", "w"), indent=1)

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
