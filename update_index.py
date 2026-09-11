import re

# Read the file
with open('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes/index.html', 'r') as f:
    content = f.read()

# Find the decision-log entry and insert the new page after it
new_entry = '''<li><a href="daily-audit-checklist.html">Daily Ops Audit Checklist for Small Teams: The 15-Minute Reboot into Governance</a><div class="desc">A daily 15-minute ops audit checklist that turns annual fire drills into a weekly habit: who has admin access, what's actually being patched, which endpoints are still answering to old workstations, and when the last time anyone logged into that server was. One-page log template, quarterly deep dive, and high-intent CTA for Ops Auditing Reloaded — Pro.</div></li>'''

# Find the pattern and insert after decision-log
pattern = r'(<li><a href="decision-log-template.html">.*?</div></li>)'
replacement = r'\1\n' + new_entry

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('/Users/haroonqamer/Swarm/hive/state/seo/ops-notes/index.html', 'w') as f:
    f.write(content)

print("Updated index.html")