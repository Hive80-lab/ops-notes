import json, urllib.request
KEY = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
payload = json.load(open('/private/tmp/ops-notes/devto_payload_231.json'))
req = urllib.request.Request('https://dev.to/api/articles',
    data=json.dumps(payload).encode(),
    headers={'api-key': KEY, 'Content-Type': 'application/json', 'User-Agent': UA}, method='POST')
try:
    r = json.load(urllib.request.urlopen(req, timeout=30))
    print('DEVTO-OK id=%s url=%s canonical=%s' % (r.get('id'), r.get('url'), bool(r.get('canonical_url'))))
except urllib.error.HTTPError as e:
    print('DEVTO-ERR', e.code, e.read().decode()[:300])
