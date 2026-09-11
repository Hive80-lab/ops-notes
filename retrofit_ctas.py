import urllib.request, json, sys
key = open('/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt').read().strip()
offer_link = '[link to offer page]'  # Placeholder — owner will fill in

cta_footer = '''
---
### Get the Full Ops Auditing Package

Turn your ops auditing from an annual fire drill into a daily habit with the complete **Ops Auditing Reloaded — Pro** package:

- Runnable checklist script with automated admin login checks
- Pre-built audit dashboard with visibility into orphaned accounts, delayed patches, and orphaned endpoints
- Weekly email summary showing what changed since your last audit
- Quarterly audit report template mapped to bad-day runbooks

**[{{offer_link}}] — Ops Auditing Reloaded — Pro Edition**

Everything pre-built and ready to deploy in two days. Click to get your ops governance running today.
'''

articles = [4635121, 4634941, 4634901, 4634814]

for article_id in articles:
    # Fetch current article
    req = urllib.request.Request(
        f'https://dev.to/api/articles/{article_id}',
        headers={'api-key': key, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
    )
    r = urllib.request.urlopen(req, timeout=30)
    data = json.loads(r.read())

    # Append CTA footer
    current_body = data.get('body_markdown', '')
    updated_body = current_body.rstrip() + cta_footer

    # Update article
    update_payload = {
        'article': {
            'title': data.get('title', ''),
            'body_markdown': updated_body,
            'tags': data.get('tags', []),
            'published': True
        }
    }

    update_req = urllib.request.Request(
        f'https://dev.to/api/articles/{article_id}',
        data=json.dumps(update_payload).encode(),
        headers={'api-key': key, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'},
        method='PUT'
    )
    update_r = urllib.request.urlopen(update_req, timeout=30)
    update_data = json.loads(update_r.read())
    print(f'Updated article {article_id}: {update_data.get("url", "failed")}')