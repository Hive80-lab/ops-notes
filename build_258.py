#!/usr/bin/env python3
"""
ops-notes build #258: restaurant-customer-feedback-loop-template.html
Revenue Shift 2 cadence: page → commit → sitemap → index card → README → dev.to → IndexNow
"""

import os, subprocess, json, time, random, hashlib, re
from datetime import datetime, date

# Change to the correct directory
os.chdir('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes')

# Config
PAGE = 'restaurant-customer-feedback-loop-template.html'
URL = 'https://hive80-lab.github.io/ops-notes/restaurant-customer-feedback-loop-template.html'
TODAY = date.today().isoformat()
TITLE = 'Restaurant Customer Feedback Loop Template'
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
<title>{TITLE} &mdash; Turn Guest Comments into Weekly Action Plans</title>
<meta name="description" content="A simple feedback loop template for restaurants: collect guest comments daily, tag them by category (food/service/atmosphere), review weekly with the team, and pick one actionable improvement. Stop letting feedback vanish and start turning complaints into consistency.">
<link rel="canonical" href="{URL}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>{TITLE}: Turn Guest Comments into Weekly Action Plans</h1>
<p class="lede">One sheet, four columns, one weekly meeting: what guests said, what it means, who owns it, and what will change. Feedback that is collected but never reviewed is just data. Feedback that is reviewed but never assigned is just discussion. Feedback that is assigned but never acted on is just disappointment. This template turns the stream of guest comments into a weekly action plan that moves the needle.</p>

<p>The <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> tells you whether satisfaction is rising or falling. This template tells you why. It is the qualitative twin to the quantitative dashboard: the dashboard shows the score, the feedback loop shows the stories behind the score. Together, they answer the two questions every manager asks: <strong>Are we winning? And why?</strong></p>

<h2>1. The four columns that close the loop</h2>
<p><strong>1. Guest Comment</strong> — the exact words, date, and source (Google review, in-person comment, feedback card). Keep it raw. Do not summarize or paraphrase; the team needs to hear the voice.</p>
<p><strong>2. Category</strong> — tag each comment as Food, Service, Atmosphere, or Other. Use consistent tags so you can spot patterns. A spike in 'Food' comments points to kitchen issues; a spike in 'Service' points to front-of-house training.</p>
<p><strong>3. Owner</strong> — assign a person or role: Head Chef for food, Floor Manager for service, GM for atmosphere. Ownership turns complaints into projects. Without an owner, feedback is just noise.</p>
<p><strong>4. Action</strong> — the specific, measurable change that will address the comment. Not 'improve service' but 'train hosts on greeting script within 7 days'. Not 'fix food' but 'standardize portion sizes by Friday'.</p>

<h2>2. How to run the weekly feedback review</h2>
<p><strong>Step 1:</strong> Collect feedback daily. Print a simple comment card for tables, set up a QR code to a Google form, and monitor Google reviews. Assign one staff member to log every comment into the template.</p>
<p><strong>Step 2:</strong> Tag and assign immediately. Do not wait for the weekly meeting. The faster you tag, the clearer the patterns become. The faster you assign, the faster the owner can start thinking.</p>
<p><strong>Step 3:</strong> Hold a 30-minute weekly review with the owners. Go through each comment, confirm the category and owner, and agree on one action per category maximum. More than one action per week is too much change.</p>
<p><strong>Step 4:</strong> Track actions in a separate log. Note the due date and completion date. Review the action log monthly to see if you are closing the loop or just collecting comments.</p>

<h2>3. What the patterns tell you</h2>
<p><strong>Food comments clustering around weekends?</strong> Review weekend prep and staffing. Consider batch prep or simplified weekend menus to maintain quality under pressure.</p>
<p><strong>Service comments mentioning 'slow'?</strong> Check table turnover data from your <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a>. Low turnover with slow service suggests understaffing or inefficient workflows.</p>
<p><strong>Atmosphere comments about 'noise'?</strong> Look at table spacing and music volume. Sometimes the fix is as simple as turning down music or adding soft surfaces.</p>
<p><strong>Repeat comments on the same issue?</strong> That is a systemic problem, not a one-off mistake. Elevate to the owner for a process or training fix, not just a staff coaching moment.</p>

<h2>4. From feedback to consistency</h2>
<p>Consistency is not about perfection; it is about response. A restaurant that fixes problems quickly earns more loyalty than a restaurant that never has problems. This template makes response systematic: you will not fix every comment, but you will address every pattern.</p>

<p>Pair this loop with your <a href="restaurant-kpi-dashboard-template.html">KPI dashboard</a> to see whether your actions are moving the satisfaction score. Pair it with the <a href="daily-operations-checklist-template.html">daily ops checklist</a> to ensure the changes stick.</p>

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

A simple feedback loop template for restaurants: collect guest comments daily, tag them by category (food/service/atmosphere), review weekly with the team, and pick one actionable improvement. Stop letting feedback vanish and start turning complaints into consistency.

**How it works:**
- Log the exact guest comment and source
- Tag by category (Food/Service/Atmosphere)
- Assign an owner (Head Chef/Floor Manager/GM)
- Commit to one specific action per week

**Why it matters:** Feedback that is collected but never reviewed is just data. This template turns the stream of guest comments into a weekly action plan that moves the needle.

**Get the full ops kit:** [{CTA_KITS[0]}]({CTA_URL}) — templates, runbooks, and checklists for service businesses.

**Free lead magnet:** [{CTA_MAGNET_TITLE}]({CTA_MAGNET_URL}) — the exact onboarding checklist we use to win clients in the first half-hour.

**More tools:**
{chr(10).join([f"- [{kit}](https://hive80lab.gumroad.com/l/{kit.lower().replace(' ', '-').replace('24/7', '24-7')})" for kit in CTA_KITS[1:]])}

#restaurant #feedback #service #operations
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
        "tags": ["restaurant", "feedback", "service", "operations"],
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

print(f"Build #258 complete: {PAGE} live, dev.to article {article_id}")