import urllib.request, json, sys
try:
    key = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
    md = open('/Users/haroonqamer/Swarm/hive/state/revenue/devto_125_ops_audit.md').read()
    canonical = 'https://hive80-lab.github.io/ops-notes/'
    title = md.split('---\n')[1].split('title: ')[1].split('\n')[0].strip()
    tags = [t.strip() for t in md.split('tags: ')[1].split('\n')[0].split(',')]
    body = md.split('---\n',2)[2]
    payload = {'article': {'title': title, 'published': True, 'body_markdown': body,
               'tags': tags, 'canonical_url': canonical, 'description': 'A daily 15-minute ops audit checklist that turns annual fire drills into a weekly habit: who has admin access, what''s actually being patched, which endpoints are still answering to old workstations, and when the last time anyone logged into that server was. One-page log template, quarterly deep dive, and flash offer.'}}
    req = urllib.request.Request('https://dev.to/api/articles',
        data=json.dumps(payload).encode(),
        headers={'api-key': key, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'}, method='POST')
    r = urllib.request.urlopen(req, timeout=30)
    print('Status:', r.status)
    print('Response:', r.read().decode())
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code, e.reason)
    print('Response:', e.read().decode())
except Exception as e:
    print('Error:', str(e))