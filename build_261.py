#!/usr/bin/env python3
"""
ops-notes build #261: restaurant-daily-sales-report-template.html
Revenue Shift 2 cadence: page → commit → sitemap → index card → README → dev.to → IndexNow
"""

import os, subprocess, json, time, random, hashlib, re
from datetime import datetime, date

# Change to the correct directory
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')

# Config
PAGE = 'restaurant-daily-sales-report-template.html'
URL = 'https://hive80-lab.github.io/ops-notes/restaurant-daily-sales-report-template.html'
TODAY = date.today().isoformat()
TITLE = 'Restaurant Daily Sales Report Template'
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
<title>{TITLE} &mdash; Track Revenue, Covers, and Key Metrics Every Day</title>
<meta name="description" content="A daily sales report template for restaurants: capture total revenue, covers by period, average check, labor cost, food cost, and weather notes. Create a consistent daily snapshot that reveals trends and informs tomorrow's decisions.">
<link rel="canonical" href="{URL}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>{TITLE}: Track Revenue, Covers, and Key Metrics Every Day</h1>
<p class="lede">One page, five minutes, complete picture: total revenue, covers by service period, average check, labor cost percentage, food cost percentage, and context notes like weather and events. A daily sales report is not about yesterday; it is about tomorrow. The patterns that emerge over weeks tell you whether your staffing, pricing, and menu decisions are working.</p>

<p>The <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> shows your trends over time. This daily report captures the raw data that feeds those trends. It is the foundation layer: without consistent daily data, your weekly analysis is guesswork. With it, you can spot a Tuesday slump before it becomes a month-long problem.</p>

<h2>1. The six essential daily metrics</h2>
<p><strong>1. Total Revenue</strong> — broken out by service period (lunch, dinner, late night) and channel (dine-in, takeout, delivery). Include tax and exclude tax consistently—pick one method and stick with it.</p>
<p><strong>2. Covers</strong> — customer count by period. Separate dine-in, takeout, and delivery if your system tracks them. Covers without revenue context are just foot traffic; revenue without covers is just sales volume.</p>
<p><strong>3. Average Check</strong> — total revenue divided by covers. Track this by period to see if your dinner service drives higher checks than lunch. A declining average check signals portion or pricing issues.</p>
<p><strong>4. Labor Cost %</strong> — (total labor cost ÷ total revenue) × 100. Include all labor: wages, taxes, benefits, and contractor fees. Calculate this daily, not weekly, to catch overtime immediately.</p>
<p><strong>5. Food Cost %</strong> — (daily COGS ÷ total revenue) × 100. Use the same daily count from your <a href="food-cost-percentage-tracker.html">food cost tracker</a>. A sudden spike from 28% to 35% is a signal, not a mystery.</p>
<p><strong>6. Context Notes</strong> — weather, local events, specials, staff issues. A rainy Tuesday explains a slow night. A festival nearby explains a spike. Without context, numbers are meaningless.</p>

<h2>2. How to complete the report in 5 minutes</h2>
<p><strong>Step 1:</strong> Pull revenue and covers from your POS system at close. Most systems can export a daily summary by period. If not, create a simple report template and run it daily.</p>
<p><strong>Step 2:</strong> Calculate average check for each period. Revenue ÷ covers = average check. Write this down—it is the quickest health indicator.</p>
<p><strong>Step 3:</strong> Get labor cost from your scheduling system or payroll. If you track hours, multiply by hourly rates and add 30% for taxes/benefits.</p>
<p><strong>Step 4:</strong> Get food cost from your daily count sheet. Use the same method every day to ensure consistency.</p>
<p><strong>Step 5:</strong> Add context notes. Weather, events, staff call-outs, equipment issues. Be specific: "Heavy rain all day" not "Bad weather."</p>

<h2>3. The daily sales report template</h2>
<p>Create a simple form or spreadsheet with these sections:</p>
<ul>
<li><strong>Date & Day of Week</strong> — always include the day name for pattern recognition</li>
<li><strong>Revenue Breakdown</strong> — Lunch/Dinner/Late Night, Dine-in/Takeout/Delivery</li>
<li><strong>Covers Breakdown</strong> — same structure as revenue</li>
<li><strong>Average Check</strong> — calculated for each period</li>
<li><strong>Labor Cost</strong> — dollars and percentage of revenue</li>
<li><strong>Food Cost</strong> — dollars and percentage of revenue</li>
<li><strong>Context</strong> — weather, events, specials, notes</li>
<li><strong>Yesterday Comparison</strong> — quick variance vs. previous day</li>
</ul>

<h2>4. How to use the report for decisions</h2>
<p><strong>Daily review (5 minutes):</strong> Look at labor cost % and food cost % first. If either is outside your target range, make a note to investigate tomorrow.</p>
<p><strong>Weekly review (15 minutes):</strong> Compare the same day of the week across weeks. Is every Tuesday slow? Is every Friday labor high? Look for patterns, not outliers.</p>
<p><strong>Monthly review (30 minutes):</strong> Aggregate the data and compare to last month. Are your average checks trending up or down? Are labor costs improving with better scheduling?</p>

<h2>5. What the daily patterns reveal</h2>
<p><strong>Consistently high labor cost on weekends?</strong> Review your weekend schedule using the <a href="restaurant-staff-scheduling-template.html">staff scheduling template</a>. You may be overstaffed for actual demand.</p>
<p><strong>Food cost spikes on busy days?</strong> Check for waste during rushes. Busy days often create over-prep; tighten pars using the <a href="restaurant-inventory-par-levels.html">par level guide</a>.</p>
<p><strong>Low average check on lunch?</strong> Consider lunch specials or upselling prompts. Lunch customers are often price-sensitive but time-conscious.</p>
<p><strong>Weather impacts sales significantly?</strong> Plan for weather in your scheduling. If rain always kills sales, consider reducing staff forecast on rainy days.</p>

<h2>6. From data to decisions</h2>
<p>The power of a daily sales report is not in any single day's numbers—it is in the accumulation of days that creates trend lines. A bad day is just a bad day. Three bad Tuesdays in a row is a pattern that requires action.</p>

<p>Make this report part of your closing routine: the manager on duty completes it before leaving. The opening manager reads it before starting the next day. This creates continuity and ensures that insights are not lost between shifts.</p>

<p>Pair this daily report with your <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> to see how daily numbers roll into weekly trends. Pair it with the <a href="restaurant-customer-feedback-loop-template.html">feedback loop</a> to connect sales performance with customer satisfaction.</p>

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

A daily sales report template for restaurants: capture total revenue, covers by period, average check, labor cost, food cost, and weather notes. Create a consistent daily snapshot that reveals trends and informs tomorrow's decisions.

**Key metrics to track daily:**
- Total revenue by period (lunch/dinner) and channel (dine-in/takeout/delivery)
- Covers by period and channel
- Average check (revenue ÷ covers)
- Labor cost % of sales
- Food cost % of sales
- Context notes (weather, events, specials)

**How to use it:**
- Complete at close in 5 minutes using POS data
- Review labor and food cost % first for immediate flags
- Compare same day of week across weeks to spot patterns
- Use trends to adjust scheduling and menu pricing

**Why it matters:** The KPI dashboard shows trends over time. This daily report captures the raw data that feeds those trends—without it, your weekly analysis is guesswork.

**Get the full ops kit:** [{CTA_KITS[0]}]({CTA_URL}) — templates, runbooks, and checklists for service businesses.

**Free lead magnet:** [{CTA_MAGNET_TITLE}]({CTA_MAGNET_URL}) — the exact onboarding checklist we use to win clients in the first half-hour.

**More tools:**
{chr(10).join([f"- [{kit}](https://hive80lab.gumroad.com/l/{kit.lower().replace(' ', '-').replace('24/7', '24-7')})" for kit in CTA_KITS[1:]])}

#restaurant #sales #reporting #operations
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
        "tags": ["restaurant", "sales", "reporting", "operations"],
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

print(f"Build #261 complete: {PAGE} live, dev.to article {article_id}")