#!/usr/bin/env python3
"""
ops-notes build #260: restaurant-menu-engineering-worksheet.html
Revenue Shift 2 cadence: page → commit → sitemap → index card → README → dev.to → IndexNow
"""

import os, subprocess, json, time, random, hashlib, re
from datetime import datetime, date

# Change to the correct directory
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')

# Config
PAGE = 'restaurant-menu-engineering-worksheet.html'
URL = 'https://hive80-lab.github.io/ops-notes/restaurant-menu-engineering-worksheet.html'
TODAY = date.today().isoformat()
TITLE = 'Restaurant Menu Engineering Worksheet'
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
<title>{TITLE} &mdash; Classify Menu Items by Popularity and Profitability</title>
<meta name="description" content="A menu engineering worksheet for restaurants: plot each menu item by popularity (units sold) and profitability (contribution margin), classify into Stars, Plowhorses, Puzzles, and Dogs, and decide whether to promote, reprice, or remove. Stop guessing what sells and start data-driven menu decisions.">
<link rel="canonical" href="{URL}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>{TITLE}: Classify Menu Items by Popularity and Profitability</h1>
<p class="lede">One matrix, four quadrants, clear actions: plot each menu item by units sold (popularity) and contribution margin (profitability), then classify as Stars, Plowhorses, Puzzles, or Dogs. Stars keep, Plowhorses optimize, Puzzles promote, Dogs reconsider. Menu engineering is not about cutting items; it is about moving items through the matrix to maximize profit per square foot.</p>

<p>The <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> tells you your overall food cost percentage. This worksheet tells you which items are driving that number and which are dragging it down. It is the diagnostic tool that turns your menu from a list of recipes into a portfolio of profit centers.</p>

<h2>1. The four quadrants of menu engineering</h2>
<p><strong>Stars (High popularity, High profitability)</strong> — your winners. These items sell well and make good money. Your job is to protect them: ensure consistent quality, train staff to upsell from them, and feature them prominently on the menu.</p>
<p><strong>Plowhorses (High popularity, Low profitability)</strong> — your volume drivers. These items sell well but have thin margins. Your job is to optimize them: raise prices slightly, reduce portion costs, or bundle with higher-margin items. Do not remove them—they bring customers in.</p>
<p><strong>Puzzles (Low popularity, High profitability)</strong> — your hidden gems. These items make good money but few people order them. Your job is to promote them: reposition on the menu, add photos, train servers to recommend them, or feature them as specials.</p>
<p><strong>Dogs (Low popularity, Low profitability)</strong> — your draggers. These items do not sell well and do not make money. Your job is to reconsider them: redesign the recipe, reprice significantly, or remove them from the menu. Every Dog costs you kitchen time and menu space.</p>

<h2>2. How to build the worksheet in 45 minutes</h2>
<p><strong>Step 1:</strong> Pull sales data from your POS for the last 4-8 weeks. Export units sold and revenue per menu item. If you do not have item-level data, start tracking it today—this worksheet requires it.</p>
<p><strong>Step 2:</strong> Calculate contribution margin per item. Subtract plate cost (ingredients + portion of labor) from menu price. Plate cost should include everything that goes on the plate, not just raw ingredients.</p>
<p><strong>Step 3:</strong> Calculate averages. Find the average units sold across all items and the average contribution margin across all items. These become your axis lines on the matrix.</p>
<p><strong>Step 4:</strong> Plot each item. Place units sold on the x-axis and contribution margin on the y-axis. Draw the average lines to create four quadrants. Classify each item based on where it falls.</p>

<h2>3. The menu engineering template</h2>
<p>Create a spreadsheet with the following columns:</p>
<ul>
<li><strong>Menu Item</strong> — name as it appears on the menu</li>
<li><strong>Menu Price</strong> — selling price to customers</li>
<li><strong>Plate Cost</strong> — ingredient cost + labor cost per portion</li>
<li><strong>Contribution Margin</strong> — Menu Price minus Plate Cost</li>
<li><strong>Units Sold</strong> — total units sold in the analysis period</li>
<li><strong>Total Revenue</strong> — Menu Price times Units Sold</li>
<li><strong>Total Profit</strong> — Contribution Margin times Units Sold</li>
<li><strong>Classification</strong> — Star/Plowhorse/Puzzle/Dog (auto-calculated)</li>
<li><strong>Action</strong> — recommended next step (Keep/Optimize/Promote/Reconsider)</li>
</ul>

<h2>4. How to act on the classifications</h2>
<p><strong>For Stars:</strong> Feature them in the top-right of menu sections, add "Chef's Favorite" callouts, and ensure they are never 86'd. Train servers to suggest them when customers ask for recommendations.</p>
<p><strong>For Plowhorses:</strong> Increase price by 5-10%, reduce portion size slightly, or pair with a high-margin side. Consider creating a premium version at a higher price point.</p>
<p><strong>For Puzzles:</strong> Move to a more visible menu location, add a photo or description highlight, feature as a weekly special, or bundle with a popular item as a combo.</p>
<p><strong>For Dogs:</strong> If the item has sentimental value, redesign it to reduce costs or increase price. Otherwise, remove it and replace with a test item that could become a Star or Puzzle.</p>

<h2>5. What the matrix reveals</h2>
<p><strong>Too many Dogs?</strong> Your menu may be too large or unfocused. Consider cutting to 70-80% of current items and focusing on quality over quantity.</p>
<p><strong>All Plowhorses?</strong> Your pricing may be too low across the board. Consider an overall price increase or premium versions of popular items.</p>
<p><strong>No Puzzles?</strong> You may be missing opportunities for higher-margin items. Consider adding seasonal specials or experimental dishes to test new concepts.</p>
<p><strong>Stars concentrated in one category?</strong> You may have an unbalanced menu. Consider developing Stars in other categories to create a more diverse profit base.</p>

<h2>6. From analysis to action</h2>
<p>Menu engineering is not a one-time project; it is a quarterly discipline. Markets change, costs fluctuate, and tastes evolve. Update this worksheet every 3 months and track how items move between quadrants. An item that is a Puzzle today might become a Star tomorrow with the right promotion.</p>

<p>Pair this worksheet with your <a href="food-cost-percentage-tracker.html">food cost tracker</a> to see whether menu changes are moving your overall food cost percentage. Pair it with the <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> to verify whether changes are improving profitability.</p>

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

A menu engineering worksheet for restaurants: plot each menu item by popularity (units sold) and profitability (contribution margin), classify into Stars, Plowhorses, Puzzles, and Dogs, and decide whether to promote, reprice, or remove. Stop guessing what sells and start data-driven menu decisions.

**The four quadrants:**
- **Stars:** High popularity, high profitability — protect and feature
- **Plowhorses:** High popularity, low profitability — optimize or bundle
- **Puzzles:** Low popularity, high profitability — promote and reposition
- **Dogs:** Low popularity, low profitability — reconsider or remove

**How to build it:**
- Pull sales data (units sold, revenue) from POS
- Calculate contribution margin (price minus plate cost)
- Plot on matrix with averages as axis lines
- Classify and act accordingly

**Why it matters:** The KPI dashboard shows overall food cost. This worksheet shows which items drive that number and which drag it down.

**Get the full ops kit:** [{CTA_KITS[0]}]({CTA_URL}) — templates, runbooks, and checklists for service businesses.

**Free lead magnet:** [{CTA_MAGNET_TITLE}]({CTA_MAGNET_URL}) — the exact onboarding checklist we use to win clients in the first half-hour.

**More tools:**
{chr(10).join([f"- [{kit}](https://hive80lab.gumroad.com/l/{kit.lower().replace(' ', '-').replace('24/7', '24-7')})" for kit in CTA_KITS[1:]])}

#restaurant #menu #engineering #profitability
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
        "tags": ["restaurant", "menu", "engineering", "profitability"],
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

print(f"Build #260 complete: {PAGE} live, dev.to article {article_id}")