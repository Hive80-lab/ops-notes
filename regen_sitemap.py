#!/usr/bin/env python3
"""Regenerate sitemap.xml from all published HTML pages (extensionless URLs)."""
import os, datetime

SITE = "https://hive80-lab.github.io/ops-notes"
EXCLUDE = {"index.html", "sitemap.xml", "404.html"}

pages = sorted(
    f for f in os.listdir(".")
    if f.endswith(".html") and f not in EXCLUDE and not f.startswith("_")
)

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in pages:
    slug = p[:-5]
    lines += ["  <url>",
              f"    <loc>{SITE}/{slug}</loc>",
              f"    <lastmod>{now}</lastmod>",
              "  </url>"]
lines.append("</urlset>")
with open("sitemap.xml", "w") as f:
    f.write("\n".join(lines) + "\n")
print(f"sitemap.xml regenerated: {len(pages)} urls")
