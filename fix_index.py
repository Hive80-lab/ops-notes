import re

# Read the file
with open('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes/index.html', 'r') as f:
    content = f.read()

# Remove duplicate entries
pattern = r'(<li><a href="daily-audit-checklist.html">.*?</div></li>\s*){2,}'
content = re.sub(pattern, r'\1', content, flags=re.DOTALL)

# Write back
with open('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes/index.html', 'w') as f:
    f.write(content)

print("Fixed index.html - removed duplicates")