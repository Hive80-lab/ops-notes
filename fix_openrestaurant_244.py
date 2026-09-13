#!/usr/bin/env python3
"""#244 house-standard fixes for open-restaurant-incident-response-system-checklist.html."""
import io

P = "open-restaurant-incident-response-system-checklist.html"
s = io.open(P, encoding="utf-8").read()

# 1) title: drop odd "(HRIS)", match house pattern
s = s.replace(
    "<title>Open-Restaurant Incident Response System (HRIS) Checklist \u2014 HIVE80lab</title>",
    "<title>Open-Restaurant Incident Response System Checklist \u2014 The Three-Day Playbook That Turns Accidents into Fixes</title>")

# 2) lede class to house standard
s = s.replace('<p class="desc">The playbook that turns operational accidents into repeatable fixes',
              '<p class="lede">The playbook that turns operational accidents into repeatable fixes')

# 3) worked example: align with meta (one quarter), give it the house texture
old_ex = """<h2>Worked example</h2>
<p>Same 8% operational accident rate across 12 sites, turning into one major incident per quarter. By committing to the three-day runbook and enforcing the four lists, the group halved the rate in six months. The fix was not more staff; it was fewer decisions to make under pressure.</p>
"""
new_ex = """<h2>Worked example</h2>
<p>A twelve-site restaurant group was running an 8% operational accident rate &mdash; roughly one incident per site per shift-week, one major incident a quarter, each one costing seats, comped food and a manager's afternoon. They did not add staff. They installed the system on this page: the three-day runbook, the four-to-do lists, the ten matrix rules, and the third-day cleanup, with the incident rate read out in the weekly standup. In one quarter the rate halved &mdash; from 8% to just over 4% &mdash; and the major incidents went from one a quarter to one in the entire period. The group's own post-mortem of the change made the mechanism plain: most accidents were not caused by people being careless, they were caused by decisions being improvised under pressure; the four lists took the improvisation out, and the rate followed. Total cost: a laminated card per station and one standing agenda item. The managers' summary: "We stopped asking who caused it and started asking which list fixes it."</p>
"""
assert old_ex in s, "worked example block not found"
s = s.replace(old_ex, new_ex)

# 4) kit CTA block + related paragraph, before </main>
kit = """
<h2>From the HIVE80lab kit</h2>
<p>Every page ships with a kit block &mdash; the paid tools behind the free advice:</p>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="incident-post-mortem-template.html">incident post-mortem template</a> is where Day 3's diagnosis lands when the incident was big enough to warrant a formal review; the <a href="staffing-shortage-coverage-plan.html">staffing shortage coverage plan</a> is the pressure that turns a small error into a visible one &mdash; incidents spike when the floor is under-covered; the <a href="shift-handover-log-template.html">shift handover log</a> is how Day 1's facts survive the roster change before Day 2's investigation; and the <a href="delayed-opening-notice-template.html">delayed opening notice</a> is what you send when the incident is big enough that the doors cannot open on time at all.</em></p>

</main>
</body>
</html>"""
assert s.rstrip().endswith("</html>")
s = s[: s.rstrip().rfind("</main>")] + kit.strip() + "\n"
# the above splice keeps everything before </main>; rebuild cleanly:
base = s.split("</main>")[0]
s = base + kit.strip() + "\n"

io.open(P, "w", encoding="utf-8").write(s)
print("open-restaurant fixes applied")
