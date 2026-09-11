import urllib.request, json
key = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
md = open('/Users/haroonqamer/Swarm/hive/state/revenue/devto_125_aar.md').read()
canonical = 'https://hive80-lab.github.io/ops-notes/after-action-report-template.html'
title = md.split('---\n')[1].split('title: ')[1].split('\n')[0].strip()
tags = [t.strip() for t in md.split('tags: ')[1].split('\n')[0].split(',')]
body = md.split('---\n',2)[2]
payload = {'article': {'title': title, 'published': True, 'body_markdown': body,
           'tags': tags, 'canonical_url': canonical, 'description': 'Five sections, thirty minutes, within 48 hours: the gap timeline, the keep list, a fix list capped at five rows with owners and dates, twice-why root cause without blame, and the linked proof that something changed.'}}
req = urllib.request.Request('https://dev.to/api/articles',
    data=json.dumps(payload).encode(),
    headers={'api-key': key, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}, method='POST')
r = urllib.request.urlopen(req, timeout=30)
d = json.loads(r.read())
print(r.status, d.get('id'), d.get('url'))
