#!/usr/bin/env python3
"""
ops-notes build #259: restaurant-staff-scheduling-template.html
Revenue Shift 2 cadence: page → commit → sitemap → index card → README → dev.to → IndexNow
"""

import os, subprocess, json, time, random, hashlib, re
from datetime import datetime, date

# Change to the correct directory
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')

# Config
PAGE = 'restaurant-staff-scheduling-template.html'
URL = 'https://hive80-lab.github.io/ops-notes/restaurant-staff-scheduling-template.html'
TODAY = date.today().isoformat()
TITLE = 'Restaurant Staff Scheduling Template'
TOPIC = 'restaurant ops'

# CTA kits and URLs
CTA_KITS = ['Ops Starter Kit', 'Ops Starter Kit Vol. 2', 'Agent Ops 24/7', 'Automation Starter Pack']
CTA_URL = 'https://hive80lab.gumroad.com/l/ops-starter-kit'
CTA_MAGNET_URL = 'https://hive80lab.gumroad.com/l/first-30'
CTA_MAGNET_TITLE = 'First 30 Minutes'

def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()

def rand_suffix():
    return hashlib.md5(f"{time.time()}{random.random()}".encode()).hexdigest()[:6]

# Build the HTML page
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{TITLE} &mdash; Balance Labor Costs, Coverage, and Employee Preferences</title>
<meta name="description" content="A simple staff scheduling template for restaurants: match forecasted covers to staff requirements, factor in labor cost targets, track availability, and build a weekly schedule that keeps service high and costs predictable. Stop scheduling by gut and start scheduling by numbers.">
<link rel="canonical" href="{URL}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>{TITLE}: Balance Labor Costs, Coverage, and Employee Preferences</h1>
<p class="lede">One spreadsheet, three inputs, one output: forecasted covers, labor cost target, and staff availability. The schedule that follows is not a compromise; it is the math that tells you exactly how many bodies you need on the floor to hit your labor percentage while keeping service standards. Scheduling by gut creates overtime and service gaps. Scheduling by numbers creates predictability.</p>

<p>The <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> tells you whether you hit your labor cost target last week. This template helps you hit it next week. It is the planning tool that connects your cost goals to your staffing decisions. When the dashboard shows labor at 38%, you do not guess—you go to this template and adjust the forecast or the target before you publish the schedule.</p>

<h2>1. The three inputs that drive the schedule</h2>
<p><strong>1. Forecasted Covers</strong> — by day and by service period (lunch/dinner). Use historical data from your POS: last year's same week, recent trends, and reservations. A 40-seat restaurant that averages 1.2 turns at dinner needs 48 covers forecast to plan staffing.</p>
<p><strong>2. Labor Cost Target</strong> — your target percentage of sales. Most restaurants aim for 25-35%. Convert this to a dollar target using your average check: if your target is 30% and average check is $30, your labor budget is $9 per cover.</p>
<p><strong>3. Staff Availability</strong> — days off, requested time off, and availability windows. Collect this weekly before you build the schedule. Availability without consequence is just a wishlist; availability paired with labor targets is a planning constraint.</p>

<h2>2. How to build the schedule in 30 minutes</h2>
<p><strong>Step 1:</strong> Calculate labor hours needed per period. Use a simple ratio: 1 server per 15-20 covers, 1 busser per 30 covers, 1 cook per 25 covers, 1 dishwasher per 40 covers. Adjust for your concept and service level.</p>
<p><strong>Step 2:</strong> Convert labor hours to labor cost. Multiply hours by hourly rates and add benefits/taxes (typically 1.3 times base pay). Compare to your labor budget from the target percentage.</p>
<p><strong>Step 3:</strong> Match staff availability to labor needs. Start with required positions (line cook, lead server), then fill support roles. Honor availability where possible, but prioritize labor cost targets.</p>
<p><strong>Step 4:</strong> Review the schedule for gaps and overlaps. Look for double coverage during slow periods and understaffing during peaks. Adjust start times to match demand curves, not convenience.</p>

<h2>3. The weekly schedule template</h2>
<p>Build a simple grid with days as columns and roles as rows. For each cell, include: staff name, shift start/end, and scheduled hours. Add a summary row for total hours and total labor cost per day. Add a variance column to show actual vs. forecasted labor cost after each day.</p>

<p>Key columns to include:</p>
<ul>
<li><strong>Position</strong> — Server, Busser, Line Cook, Dishwasher, Host</li>
<li><strong>Staff</strong> — assigned employee name</li>
<li><strong>Shift</strong> — start and end times</li>
<li><strong>Hours</strong> — scheduled hours for that shift</li>
<li><strong>Cost</strong> — hourly rate times hours (including burden)</li>
<li><strong>Cover Ratio</strong> — covers per staff hour (target: 15-20 for servers)</li>
</ul>

<h2>4. How to use the schedule daily</h2>
<p><strong>Pre-shift meeting:</strong> Review the day's forecasted covers against scheduled staff. If you are overstaffed, consider sending someone home early. If understaffed, call in backups or adjust stations.</p>
<p><strong>Mid-shift check:</strong> Compare actual covers to forecast. If you are running 20% above forecast, consider pulling a backup from a non-essential task. If running 20% below, start sending people early to protect labor cost.</p>
<p><strong>Post-shift review:</strong> Record actual covers and actual labor hours. Update the variance column. Use this data to improve next week's forecast.</p>

<h2>5. What the numbers tell you</h2>
<p><strong>Consistently over labor target?</strong> Either your forecast is too low, your labor ratio is too generous, or your service standards require higher staffing. Consider raising prices or improving efficiency.</p>
<p><strong>Service complaints on busy nights?</strong> You may be understaffed for your peak demand. Consider adding a floater or adjusting start times to better cover the rush.</p>
<p><strong>High overtime costs?</strong> Review shift lengths and break policies. Sometimes two 6-hour shifts are cheaper than one 8-hour shift with overtime.</p>
<p><strong>Staff requesting more hours?</strong> Use the schedule to show where you can add hours without breaking labor targets. Sometimes the solution is cross-training, not more bodies.</p>

<h2>6. From schedule to consistency</h2>
<p>A good schedule is not about fairness; it is about predictability. When staff know the schedule is built on numbers, not favoritism, they trust the process. When managers know the schedule is tied to costs, they protect the bottom line. This template turns scheduling from a constant negotiation into a data-driven process.</p>

<p>Pair this schedule with your <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> to verify whether your labor targets are working. Pair it with the <a href="daily-operations-checklist-template.html">daily ops checklist</a> to ensure the scheduled staff actually perform the required tasks.</p>

<p><strong>Get the full kit:</strong> <a href="{CTA_URL}">{CTA_KITS[0]}</a> — templates, runbooks, and checklists for service businesses.</p>
<p><strong>Free lead magnet:</strong> <a href="{CTA_MAGNET_URL}">{CTA_MAGNET_TITLE}</a> — the exact onboarding checklist we use to win clients in the first half-hour.</p>
<p><strong>More tools:</strong> {", ".join([f'<a href="https://hive80lab.gumroad.com/l/{kit.lower().replace(" ", "-").replace("24/7", "24-7")}">{kit}</a>' for kit in CTA_KITS[1:]])}.</p>

</main>
<footer><a href="https://hive80lab.github.io/ops-notes/">HIVE80lab ops notes</a> — practical operations templates & checklists</footer>
</body>
</html>'''

# Write the file
with open(PAGE, 'w') as f:
    f.write(html)

# Git commit
run(f"git add {PAGE}")
run(f"git commit -m 'Add ops-notes page: {TITLE} ({PAGE})'")

# Update sitemap
sitemap_path = "sitemap.xml"
if os.path.exists(sitemap_path):
    with open(sitemap_path) as f:
        sitemap = f.read()
    new_entry = f'  <url><loc>{URL}</loc><lastmod>{TODAY}</lastmod></url>'
    if PAGE not in sitemap:
        sitemap = re.sub(r'</urlset>', f'{new_entry}\n</urlset>', sitemap)
        with open(sitemap_path, 'w') as f:
            f.write(sitemap)
        run(f"git add {sitemap_path}")
        run("git commit -m 'Update sitemap for new page'")

# Update index (TOP card)
index_path = "index.html"
if os.path.exists(index_path):
    with open(index_path) as f:
        index = f.read()
    card = f'<li><a href="{PAGE}">{TITLE}</a> <span>({TOPIC})</span></li>'
    if PAGE not in index:
        index = re.sub(r'<!-- NEW -->', f'{card}\n<!-- NEW -->', index)
        with open(index_path, 'w') as f:
            f.write(index)
        run(f"git add {index_path}")
        run("git commit -m 'Add TOP card to index'")

# Update README
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path) as f:
        readme = f.read()
    line = f"- [{PAGE}]({PAGE}) — {TITLE}"
    if PAGE not in readme:
        readme = re.sub(r'^# ops-notes', f'# ops-notes\n{line}', readme, flags=re.MULTILINE)
        with open(readme_path, 'w') as f:
            f.write(readme)
        run(f"git add {readme_path}")
        run("git commit -m 'Add to README'")

# Push
run("git push origin main")

# dev.to API
devto_token = os.getenv("DEVTO_TOKEN")
if not devto_token:
    raise RuntimeError("DEVTO_TOKEN env var required")

devto_body = f"""# {TITLE}

A simple staff scheduling template for restaurants: match forecasted covers to staff requirements, factor in labor cost targets, track availability, and build a weekly schedule that keeps service high and costs predictable. Stop scheduling by gut and start scheduling by numbers.

**How it works:**
- Forecast covers by day and service period
- Set labor cost target (25-35% of sales)
- Map staff availability to labor needs
- Build schedule with position-based ratios

**Key ratios:**
- 1 server per 15-20 covers
- 1 busser per 30 covers
- 1 cook per 25 covers
- 1 dishwasher per 40 covers

**Why it matters:** The KPI dashboard tells you whether you hit your labor cost target last week. This template helps you hit it next week.

**Get the full ops kit:** [{CTA_KITS[0]}]({CTA_URL}) — templates, runbooks, and checklists for service businesses.

**Free lead magnet:** [{CTA_MAGNET_TITLE}]({CTA_MAGNET_URL}) — the exact onboarding checklist we use to win clients in the first half-hour.

**More tools:**
{chr(10).join([f"- [{kit}](https://hive80lab.gumroad.com/l/{kit.lower().replace(' ', '-').replace('24/7', '24-7')})" for kit in CTA_KITS[1:]])}

#restaurant #scheduling #labor #operations
"""

# Ensure unique slug
slug = re.sub(r'[^a-z0-9]+', '-', TITLE.lower()).strip('-')
if os.path.exists(f".devto_payload_{PAGE.split('.')[0]}.json"):
    with open(f".devto_payload_{PAGE.split('.')[0]}.json") as f:
        try:
            prev = json.load(f)
            if prev.get("article") and prev["article"].get("slug"):
                slug = prev["article"]["slug"]
        except:
            pass
else:
    slug = f"{slug}-{rand_suffix()}"

payload = {
    "article": {
        "title": TITLE,
        "published": True,
        "body_markdown": devto_body,
        "tags": ["restaurant", "scheduling", "labor", "operations"],
        "series": "ops-notes",
        "slug": slug,
        "canonical_url": URL
    }
}

with open(f".devto_payload_{PAGE.split('.')[0]}.json", "w") as f:
    json.dump(payload, f, indent=2)

# Post to dev.to
import urllib.request
import urllib.error
req = urllib.request.Request(
    "https://dev.to/api/articles",
    data=json.dumps(payload).encode(),
    headers={
        "Content-Type": "application/json",
        "api-key": devto_token,
        "User-Agent": "hive-ops-notes/1.0"
    }
)
try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        article_id = result["id"]
        print(f"dev.to article published: https://dev.to/api/articles/{article_id}")
except urllib.error.HTTPError as e:
    raise RuntimeError(f"dev.to API failed: {e.code} {e.reason}")

# IndexNow
key_path = "indexnow.key"
if os.path.exists(key_path):
    with open(key_path) as f:
        key = f.read().strip()
    indexnow_payload = {
        "host": "hive80-lab.github.io",
        "key": key,
        "urlList": [URL]
    }
    req = urllib.request.Request(
        "https://api.indexnow.org/v2/submit",
        data=json.dumps(indexnow_payload).encode(),
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            print("IndexNow submitted")
    except urllib.error.HTTPError as e:
        print(f"IndexNow failed: {e.code} {e.reason}")

print(f"Build #259 complete: {PAGE} live, dev.to article {article_id}")