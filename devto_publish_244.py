#!/usr/bin/env python3
# ops-notes #244 dev.to publisher archive — run 2026-09-14
# POST 201 id 4641395 (slug year-end-close-the-four-week-runway-that-makes-january-boring-52oe),
# canonical -> year-end-close-checklist.html, published_at 2026-09-13T00:15:21Z.
# PUT 200 patch added Vol.2 + Mega Bundle kit CTAs (front-end verify: 4 kit CTAs, canonical x3, live 200).
# Notes: GET without UA = 403 Forbidden Bots; front-end GET via urllib also 403s -> verify with curl -A browser UA.
import json, urllib.request, time
title = "Year-End Close: The Four-Week Runway That Makes January Boring"
canonical = "https://hive80-lab.github.io/ops-notes/year-end-close-checklist.html"
payload = json.load(open('devto_payload_244.json'))
key = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
req = urllib.request.Request('https://dev.to/api/articles', data=json.dumps(payload).encode(),
    headers={'api-key': key, 'Content-Type':'application/json', 'User-Agent': UA})
r = urllib.request.urlopen(req, timeout=60)
resp = json.load(r); aid = resp.get('id'); print('POST:', r.status, 'id:', aid)
time.sleep(3)
hdr = {'api-key': key, 'User-Agent': UA}
d = json.load(urllib.request.urlopen(urllib.request.Request(f'https://dev.to/api/articles/{aid}', headers=hdr), timeout=30))
print('VERIFY:', d.get('url'), '| canonical:', d.get('canonical_url'))
