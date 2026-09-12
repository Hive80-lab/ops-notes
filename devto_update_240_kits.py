import json, urllib.request

KEY_PATH = "/Users/haroonqamer/Swarm/hive/state/secure/devto_api_key.txt"
ART_ID = 4641244
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

p = json.load(open("devto_payload_240.json"))
body = p["article"]["body_markdown"]

MARK = "\n---\n\n*The [annual ops budget template]"
KIT = """## Kits

Every page ships with a kit block \u2014 the paid tools behind the free advice:

- [The First 30 Minutes](https://hive80lab.gumroad.com/l/first-30-minutes) \u2014 free incident quick-start checklist
- [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit) \u2014 incident response for small teams \u2014 $14
- [Ops Starter Kit Vol. 2](https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2) \u2014 advanced incident response & communications \u2014 $27
- [Ops Mega Bundle](https://hive80lab.gumroad.com/l/ops-mega-bundle) \u2014 all 5 kits in one download \u2014 $49

"""
assert MARK in body and "Kits" not in body, "unexpected body state"
body = body.replace(MARK, "\n" + KIT + MARK, 1)

payload = {"article": {"body_markdown": body}}
req = urllib.request.Request(
    "https://dev.to/api/articles/%d" % ART_ID,
    data=json.dumps(payload).encode(), method="PUT",
    headers={"api-key": open(KEY_PATH).read().strip(),
             "Content-Type": "application/json",
             "User-Agent": UA, "Accept": "application/json"})
with urllib.request.urlopen(req, timeout=60) as r:
    res = json.load(r)
    print("HTTP", r.status, "id", res.get("id"), "edited", res.get("edited_at") is not None)
json.dump({"article": p["article"] | {"body_markdown": body}},
          open("devto_payload_240.json", "w"), indent=1)
