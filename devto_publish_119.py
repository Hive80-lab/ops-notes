import urllib.request, json, time, sys

key = open('/home/haroon/Swarm/hive/state/secure/devto_api_key.txt').read().strip()

body_md = open('/tmp/ops-notes/devto_119_card.md').read() if False else None
