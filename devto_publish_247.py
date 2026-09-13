#!/usr/bin/env python3
# ops-notes #247 dev.to publisher — run 2026-09-13
# POST direct-publish (payload includes kit CTAs + site link), then API verify canonical/url.
# Lesson carried: front-end GET 403s urllib UA -> verify front-end with curl -A browser UA (done separately).
import json, urllib.request, time
payload = json.load(open('devto_payload_247.json'))
key = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
req = urllib.request.Request('https://dev.to/api/articles', data=json.dumps(payload).encode(),
    headers={'api-key': key, 'Content-Type': 'application/json', 'User-Agent': UA})
r = urllib.request.urlopen(req, timeout=60)
resp = json.load(r); aid = resp.get('id'); slug = resp.get('slug')
print('POST:', r.status, 'id:', aid, 'slug:', slug)
time.sleep(3)
hdr = {'api-key': key, 'User-Agent': UA}
d = json.load(urllib.request.urlopen(urllib.request.Request(f'https://dev.to/api/articles/{aid}', headers=hdr), timeout=30))
print('VERIFY url:', d.get('url'))
print('VERIFY canonical:', d.get('canonical_url'))
print('CTAs in body:', d['body_markdown'].count('hive80lab.gumroad.com'), '| site links:', d['body_markdown'].count('hive80-lab.github.io'))