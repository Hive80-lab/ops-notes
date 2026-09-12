#!/usr/bin/env python3
"""dev.to #232 publisher - stocktake checklist via API rail (browser UA required)."""
import json, urllib.request
KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
ART_PATH = "devto_payload_232.json"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
API = "https://dev.to/api/articles"
def main():
    key = open(KEY_PATH).read().strip()
    payload = json.load(open(ART_PATH))
    data = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=data, method="POST", headers={
        "api-key": key, "Content-Type": "application/json",
        "User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            out = json.loads(r.read().decode())
            print("POSTED", out.get("id"), out.get("url"))
    except Exception as e:
        print("ERR", e)
        b = getattr(e, "read", lambda: b"")()
        if b: print(b.decode()[:400])
if __name__ == "__main__":
    main()