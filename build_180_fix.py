#!/usr/bin/env python3
"""ops-notes #180 recip fix — inject raci backlinks with verified anchors + rerun linkcheck."""
import re, sys
from pathlib import Path
R = Path("/private/tmp/ops-notes")

RECIP = {
 "role-permission-matrix-template.html": (
   'the <a href="employee-offboarding-checklist.html">employee offboarding checklist</a>.',
   'the <a href="employee-offboarding-checklist.html">employee offboarding checklist</a>. The <a href="raci-matrix-template.html">RACI matrix template</a> handles the other half of the same question &mdash; not what a role may touch, but who decides, one name per letter.'),
 "decision-log-template.html": (
   '<li><strong>A postmortem that starts from facts.</strong>',
   '<li><strong>One accountable name per decision.</strong> The log records what was decided; the <a href="raci-matrix-template.html">RACI matrix template</a> fixes who could decide it &mdash; one A per row, named before the decision needs logging.</li>\n<li><strong>A postmortem that starts from facts.</strong>'),
 "incident-severity-matrix-template.html": (
   'If you would rather have the whole incident loop',
   'The declaration itself is a decision row: the <a href="raci-matrix-template.html">RACI matrix template</a> gives it one A (who declares) and one R (who leads) before 2 a.m. ever asks. If you would rather have the whole incident loop'),
}
for fname, (anchor, block) in RECIP.items():
    p = R / fname
    t = p.read_text()
    if SLUG if (SLUG:="raci-matrix-template") in t else False:
        print(f"recip {fname}: already linked, skip"); continue
    if anchor not in t:
        print(f"recip {fname}: anchor NOT FOUND"); sys.exit(1)
    p.write_text(t.replace(anchor, block, 1))
    print(f"recip {fname}: injected")

# now fix the linkcheck regex in build_180 and rerun full linkcheck
broken = 0; checked = 0
for f in sorted(R.glob("*.html")):
    t = f.read_text()
    for href in re.findall(r'href="([^"#]+\.html)"', t):
        checked += 1
        if href.startswith("http"):
            continue
        if not (R / href).exists():
            broken += 1; print(f"  BROKEN in {f.name}: {href}")
print(f"linkcheck: {checked} internal links, {broken} broken")
sys.exit(1 if broken else 0)