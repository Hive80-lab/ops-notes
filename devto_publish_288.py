#!/usr/bin/env python3
"""Dev.to publish script for page #288"""

import json, requests, sys, time
from pathlib import Path

# Load API key
api_key = Path("../../../state/secure/devto_api_key.txt").read_text().strip()
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Load payload
payload_path = Path(".devto_payload_288-cloud-cost-optimization-playbook.json")
payload = json.loads(payload_path.read_text())

# Add required fields
payload["article"]["published"] = True

# Publish
response = requests.post(
    "https://dev.to/api/articles",
    headers=headers,
    json=payload
)

if response.status_code == 201:
    article = response.json()
    print(f"✅ Published: {article['url']}")
    print(f"ID: {article['id']}")
    # Save published info
    Path("devto_288_published.txt").write_text(f"{article['id']}\n{article['url']}\n")
else:
    print(f"❌ Failed: {response.status_code}")
    print(response.text)
    sys.exit(1)