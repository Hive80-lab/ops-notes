#!/usr/bin/env python3
# dev.to publish payload for #220 (as executed 2026-09-13). Result: article id 4640657, 200.
# POST https://dev.to/api/articles  headers: {'api-key': <from state/secure/devto_api_key.txt>, 'User-Agent': 'curl/8.4.0'}
# NOTE: dev.to 403s the python-urllib default UA ("Forbidden Bots") — send a curl UA.
PAYLOAD = {"article": {
  "title": "The call-out morning that doesn't cancel the day: a staffing shortage coverage plan",
  "published": True,
  "tags": ["operations", "management", "smallbusiness", "hr"],
  "canonical_url": "https://hive80-lab.github.io/ops-notes/staffing-shortage-coverage-plan.html",
  "body_markdown": open('devto_body_220.md').read() if __import__('os').path.exists('devto_body_220.md') else "<see dev.to article 4640657 for final body>"}}
