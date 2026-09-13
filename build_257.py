#!/usr/bin/env python3
"""
ops-notes build #257: restaurant-kpi-dashboard-template.html
Revenue Shift 2 cadence: page → commit → sitemap → index card → README → dev.to → IndexNow
"""

import os, subprocess, json, time, random, hashlib, re
from datetime import datetime, date

# Change to the correct directory
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')

# Config
PAGE = 'restaurant-kpi-dashboard-template.html'
URL = 'https://hive80-lab.github.io/ops-notes/restaurant-kpi-dashboard-template.html'
TODAY = date.today().isoformat()
TITLE = 'Restaurant KPI Dashboard Template'
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
<title>{TITLE} &mdash; Track Daily Sales, Labor %, Food Cost %, and Turnover in One View</title>
<meta name="description" content="A ready-to-use KPI dashboard template for restaurant operations. Track daily revenue, labor cost percentage, food cost percentage, table turnover, and customer satisfaction—all in one clean view. Stop flying blind and start spotting cost spikes and service gaps before they hurt the bottom line.">
<link rel="canonical" href="{URL}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>{TITLE}: Track Daily Sales, Labor %, Food Cost %, and Turnover in One View</h1>
<p class="lede">One page, five numbers, one decision point: daily revenue, labor cost % of sales, food cost % of sales, table turnover rate, and customer satisfaction score. Without a clear dashboard, restaurants fly blind—missing cost spikes and service gaps until it's too late. This template turns raw daily counts into actionable insights that fit on a single screen.</p>

<p>The <a href="restaurant-inventory-par-levels.html">par level and ordering guide</a> tells you what to order. The <a href="food-cost-percentage-tracker.html">food cost percentage tracker</a> tells you what you spent. This dashboard tells you whether those decisions are working: it is the control panel that connects purchasing to performance, and staffing to sales. It answers the five questions every owner asks at the end of the night: <strong>Did we make money? Did we staff right? Did we waste food? Did we turn tables? Did we keep guests happy?</strong></p>

<h2>1. The five metrics that matter</h2>
<p><strong>1. Daily Revenue</strong> — total sales for the day, broken out by dine-in, takeout, and delivery if you track them. Revenue without context is just a number; revenue against labor and food cost is a story.</p>
<p><strong>2. Labor Cost %</strong> — (total labor cost ÷ daily revenue) × 100. Include wages, taxes, and benefits. The industry rule of thumb is 25-35%, but your number is your number. Track it daily, not weekly, to catch overtime before it becomes a habit.</p>
<p><strong>3. Food Cost %</strong> — (COGS ÷ daily revenue) × 100. Use the same daily count from your <a href="food-cost-percentage-tracker.html">food cost sheet</a>. A sudden jump from 28% to 34% is not a mystery; it is a signal to check waste, theft, or pricing.</p>
<p><strong>4. Table Turnover Rate</strong> — (covers ÷ seats) per service period. A 40-seat restaurant that serves 120 covers at dinner turned each table three times. Low turnover with high revenue means high checks; low turnover with low revenue means trouble.</p>
<p><strong>5. Customer Satisfaction Score</strong> — whatever you track: Google rating, feedback forms, or complaint count. A 4.8 rating with a 38% food cost is a pricing problem; a 4.2 rating with a 28% food cost is a service problem.</p>

<h2>2. How to build it in 20 minutes</h2>
<p><strong>Step 1:</strong> Create a daily log sheet or spreadsheet with five columns: Revenue, Labor Cost, Food Cost, Covers, and Satisfaction. Add calculated columns for Labor % and Food %.</p>
<p><strong>Step 2:</strong> Pull revenue from your POS system at close. Pull labor from your schedule/payroll. Pull food cost from your <a href="food-cost-percentage-tracker.html">daily count sheet</a>. Count covers from the floor. Record satisfaction from your chosen source.</p>
<p><strong>Step 3:</strong> Calculate the percentages and turnover. Plot the last seven days in a simple line chart or just look at the trend. Highlight any day where labor % exceeds 35% or food % exceeds 35%.</p>
<p><strong>Step 4:</strong> Make one decision before you go home: adjust tomorrow's staffing, tweak the menu, or talk to the team about service. The dashboard is not a report; it is a decision tool.</p>

<h2>3. What the numbers tell you</h2>
<p><strong>Labor % rising while revenue flat?</strong> Check the schedule for overtime or understaffing that forces extra shifts. Consider a pre-service briefing to improve table turns.</p>
<p><strong>Food % spiking on weekends?</strong> Review waste logs and prep quantities. High-volume days often create over-prep; tighten pars using the <a href="restaurant-inventory-par-levels.html">par level guide</a>.</p>
<p><strong>Turnover low but revenue high?</strong> You are pricing well but turning tables slowly. Train hosts on table reset timing and consider reservation buffers.</p>
<p><strong>Satisfaction down while costs up?</strong> Guests are feeling the service or quality dip. Cross-train staff and audit portion consistency. Cost control without quality control is false economy.</p>

<h2>4. Templates and tools</h2>
<p>This dashboard is one piece of a complete ops system. The <a href="restaurant-inventory-par-levels.html">par level sheet</a> prevents over-ordering. The <a href="food-cost-percentage-tracker.html">food cost tracker</a> measures waste. The <a href="daily-operations-checklist-template.html">daily ops checklist</a> keeps the floor consistent. Together, they turn reactive firefighting into proactive management.</p>

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

A ready-to-use KPI dashboard template for restaurant operations. Track daily sales, labor cost %, food cost %, table turnover, and customer satisfaction—all in one view.

**Key metrics:**
- Daily revenue & covers
- Labor cost % of sales
- Food cost % (COGS)
- Table turnover rate
- Customer satisfaction score

**Why this matters:** Without a clear dashboard, restaurants fly blind—missing cost spikes and service gaps until it's too late.

**Get the full ops kit:** [{CTA_KITS[0]}]({CTA_URL}) — templates, runbooks, and checklists for service businesses.

**Free lead magnet:** [{CTA_MAGNET_TITLE}]({CTA_MAGNET_URL}) — the exact onboarding checklist we use to win clients in the first half-hour.

**More tools:**
{chr(10).join([f"- [{kit}](https://hive80lab.gumroad.com/l/{kit.lower().replace(' ', '-').replace('24/7', '24-7')})" for kit in CTA_KITS[1:]])}

#restaurant #operations #kpi #dashboard
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
        "tags": ["restaurant", "operations", "kpi", "dashboard"],
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

print(f"Build #257 complete: {PAGE} live, dev.to article {article_id}")