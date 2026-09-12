#!/usr/bin/env python3
"""Build ops-notes unit #208: configuration-drift-audit-checklist.html
Rail: page -> sitemap TOP -> index card -> README NEW -> reciprocal backlinks x3 -> linkcheck.
"""
import re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SLUG = "configuration-drift-audit-checklist.html"
BASE = "https://hive80-lab.github.io/ops-notes/"
TODAY = datetime.date.today().isoformat()

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Configuration Drift Audit for Small Teams (The Server That Stopped Matching Its Documentation) &mdash; HIVE80lab Ops Notes</title>
<meta name="description" content="A configuration drift audit checklist for small teams: a read-only pass that diffs production against the repo, classifies every difference as fix-forward, revert, or documented exception, finds the pipeline gap that let the hand-change through, and keeps any box rebuildable in under an hour.">
<link rel="canonical" href="https://hive80-lab.github.io/ops-notes/configuration-drift-audit-checklist.html">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><a href="index.html">HIVE80lab &mdash; Ops notes</a></header>
<main>

<h1>Configuration Drift Audit for Small Teams</h1>
<p class="lede">Every small team has a machine that stopped matching its documentation months ago. A hand-edit during an outage, a cron job added at 2am, a package upgraded &ldquo;just this once.&rdquo; None of it went through the repo, so none of it survives a rebuild &mdash; and nobody discovers that until the day the rebuild is the emergency. Drift is not a scandal; it is <strong>uncommitted work running your business</strong>. The audit is a read-only pass, once a quarter, that diffs production against the baseline and turns every difference into a decision: fix forward, revert, or declare. Run it on a quiet Tuesday, not mid-incident.</p>

<h2>The audit (read-only until step 5)</h2>
<ol>
<li><strong>Pick the three boxes that hurt most.</strong> You are not auditing the fleet; you are auditing the snowflakes &mdash; the machines nobody has rebuilt since onboarding, the one with the &ldquo;temporary&rdquo; edit, the box only one person can deploy to. If you don&rsquo;t know which three those are, that fact <em>is</em> the audit&rsquo;s first finding.</li>
<li><strong>Export the live config, read-only.</strong> Installed packages, running services, crontabs, firewall rules, env files (keys redacted &mdash; diff the <em>names</em>, never the values), mount points, kernel/sysctl settings. One command per box if you can; the point is a snapshot you can diff, not a change session. Nothing gets modified during the audit &mdash; that discipline is the whole game.</li>
<li><strong>Diff against the baseline.</strong> Baseline means: the repo, the infrastructure code, or the last audited tag. If none exists, the baseline is today&rsquo;s export and step one next quarter is comparing against it &mdash; a baseline you create now beats a perfect one you never create.</li>
<li><strong>Sort the diffs by blast radius.</strong> What breaks customers first if this box dies? A changed backup schedule is bigger than a changed MOTD. Sort before you triage, because step 5 is a budget and you will not clear the whole list in one sitting.</li>
<li><strong>Classify every diff, three buckets only.</strong> <em>Fix forward</em> &mdash; production is right, the repo is stale: the diff becomes a PR (this is most diffs, and it is the happy path, because the change already shipped and someone depended on it). <em>Revert</em> &mdash; production is wrong: put prod back and note why. <em>Declare</em> &mdash; production must differ (a CAN bus of licensing quirks, a vendor-required sysctl, a bigger swap on the reporting box): write it down as a documented exception with an owner and a review date. Anything not in one of the three buckets is a diff you are hiding from yourself.</li>
<li><strong>Fix-forward first, as PRs.</strong> Every fix-forward diff is a pull request against the baseline, reviewed like any other change. Production is the source of truth <em>until the PR merges</em>; then the repo is. If the PR would be rejected as-is, that is not a merge blocker &mdash; it is a finding: the hand-change encoded a decision nobody documented.</li>
<li><strong>Revert every &ldquo;temporary&rdquo; edit older than a sprint.</strong> If it was temporary in spirit but load-bearing in fact, that is exactly what the declare bucket is for. What you must not do is leave it silently &mdash; the silent temporary is the diff that takes the rebuild down with it.</li>
<li><strong>Find the pipeline gap, not the person.</strong> For each diff, answer one question: <em>which process should have carried this change and didn&rsquo;t?</em> A 2am hand-edit means the break-glass path worked but the backport never happened (the <a href="hotfix-process-checklist.html">hotfix process</a> owns that receipt); a hand-edited crontab means there was no repo for cron at all. The fix is a missing script, a missing repo, or a missing step &mdash; never a conversation about who to be mad at.</li>
<li><strong>Close the gap while the audit is warm.</strong> Anything done by hand twice becomes a script; anything scripted goes in the repo; anything in the repo gets deployed by the pipeline. Small closes: one crontab dir added to git, one env template added, one break-glass backport check added to the checklist you already run.</li>
<li><strong>Re-baseline and book the next one.</strong> Tag the audited state, log the audit&rsquo;s findings in the <a href="decision-log-template.html">decision log</a>, and put the next audit in the calendar &mdash; quarterly for the snowflakes, and a cheap monthly hash check (cron a config checksum and diff it) so drift between audits trips an alarm instead of a surprise. A drift audit that happens &ldquo;when we have time&rdquo; is a rebuild that happens when you don&rsquo;t.</li>
</ol>

<h2>Five traps</h2>
<ul>
<li><strong>Documenting the snowflake instead of converging it.</strong> The audit that ends with &ldquo;we wrote down how the box actually is&rdquo; has declared permanent drift. Documentation is the <em>declare</em> bucket for things that must differ &mdash; not a retirement home for hand-edits that should have become PRs. If the diff could ride the normal pipeline, fix it forward.</li>
<li><strong>The audit that changes production.</strong> &ldquo;While we&rsquo;re in here&hellip;&rdquo; is how a read-only audit becomes an outage. Audit read-only; every change goes through the normal path afterward. The discipline is what makes the next audit trustworthy &mdash; and what keeps the diff honest.</li>
<li><strong>Drift-blind CI.</strong> The pipeline is green because it runs on a clean machine the pipeline built. The box serving traffic is not that machine. CI proves the code builds; only the diff proves the fleet matches. That is why the audit reads production directly instead of trusting green.</li>
<li><strong>The eternal temporary.</strong> A hand-edit from 2023 with a comment &ldquo;remove after migration&rdquo; &mdash; the migration shipped, the edit stayed, nobody remembers which of them is load-bearing. Temporary without an expiry date is permanent without an owner. Sprint-old temporaries get reverted (or declared) in step 7; that is the whole point of the cutoff.</li>
<li><strong>The blame hunt.</strong> If the audit&rsquo;s output is a name, the next hand-edit happens invisibly at 2am and the drift you find next quarter is the drift someone was scared to log. Drift archaeology finds missing pipelines, not guilty people &mdash; the <a href="blameless-post-incident-review-template.html">blameless post-incident review</a> rule applies here too.</li>
</ul>

<h2>Worked example</h2>
<p>A nine-person analytics company, twelve staff-facing servers, no infra code. The old way: the reporting box&rsquo;s disk died on a Thursday; rebuild from &ldquo;the docs&rdquo; took three days, and six weeks later finance asked why invoices had stopped reconciling &mdash; a 4am cron the dead box ran had never been documented, and 410 invoices had silently double-billed. Cost: three days of rebuild, a credits batch, and an auditor&rsquo;s raised eyebrow.</p>
<p>The rerun: quarterly read-only audit. The export diffed against a baseline tag they created that same morning found seven diffs across the three worst boxes: five fix-forwarded as PRs (including the missing reconcile cron, now in a git-tracked crontab dir deployed by the pipeline), one reverted (a debug logging flag someone left at verbose in prod, quietly eating 14% of disk), one declared (the reporting box&rsquo;s vendor-required sysctl, documented with owner and review date). The monthly hash alarm caught its first drift eleven weeks later &mdash; a package installed during a support call &mdash; and the whole loop was one PR, not one surprise. Rebuild-from-repo time for all three boxes: under an hour, measured, because they made it a drill.</p>

<h2>Metrics (for the drift loop itself)</h2>
<ul>
<li>% of production boxes with a written baseline and a diff date. If it is under 100%, the rebuild plan is a story, not a plan.</li>
<li>Median age of undocumented diffs found per audit. A shrinking median means the monthly alarm is working; a growing one means changes are still bypassing the repo.</li>
<li>Rebuild-from-repo time, measured as a drill. The number that matters: any box rebuildable in under an hour, from nothing but the repo.</li>
<li>Audits actually held per quarter. Two booked and one held beats three booked and zero held &mdash; but hold the ones you book.</li>
</ul>

<h2>From the HIVE80lab kit</h2>
<ul>
<li><a href="https://hive80lab.gumroad.com/l/first-30-minutes">The First 30 Minutes</a> &mdash; free incident quick-start checklist</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit">Ops Starter Kit</a> &mdash; incident response for small teams &mdash; $14</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-starter-kit-vol-2">Ops Starter Kit Vol. 2</a> &mdash; advanced incident response &amp; communications &mdash; $27</li>
<li><a href="https://hive80lab.gumroad.com/l/ops-mega-bundle">Ops Mega Bundle</a> &mdash; all 5 kits in one download &mdash; $49</li>
</ul>

<p><em>Related: the <a href="https://hive80-lab.github.io/ops-notes/post-deploy-verification-checklist.html">post-deploy verification</a> is the ten minutes after a deploy where fresh drift is cheapest to catch; the <a href="https://hive80-lab.github.io/ops-notes/change-management-checklist.html">change management checklist</a> is what keeps changes riding the pipeline that the audit then diffs against; and the <a href="https://hive80-lab.github.io/ops-notes/break-glass-account-checklist.html">break-glass account checklist</a> is where emergency hand-changes come from &mdash; the audit is how their backports stop getting forgotten.</em></p>
</main>
<footer><a href="index.html">&larr; All ops notes</a></footer>
</body>
</html>
"""

def main():
    root = ROOT
    page = root / SLUG
    if page.exists():
        print("ABORT: page exists:", SLUG); sys.exit(1)
    page.write_text(PAGE, encoding="utf-8")
    print("page written:", SLUG, len(PAGE), "bytes")

    # --- sitemap: insert at TOP (newest-first) ---
    sm = root / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    entry = ("<url><loc>" + BASE + SLUG + "</loc><lastmod>" + TODAY +
             "</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    marker = 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    assert marker in s, "sitemap marker missing"
    s = s.replace(marker, marker + entry, 1)
    sm.write_text(s, encoding="utf-8")
    print("sitemap url inserted at TOP; total urls:", s.count("<url>"))

    # --- index: insert card before current TOP card ---
    ix = root / "index.html"
    t = ix.read_text(encoding="utf-8")
    card = ('<li><a href="' + SLUG + '">Configuration Drift Audit for Small Teams: The Server That Stopped Matching Its Documentation</a>'
            '<div class="desc">Drift is uncommitted work running your business &mdash; the 2am hand-edit, the &ldquo;temporary&rdquo; crontab, the package upgraded just this once, none of it surviving a rebuild. A read-only quarterly audit diffs the three worst boxes against a baseline and turns every difference into a decision: fix forward (the diff becomes a PR), revert, or declare with an owner and review date. Read-only until the PRs, diffs sorted by blast radius, temporaries older than a sprint reverted or declared, the pipeline gap fixed instead of the person blamed, a monthly config-hash alarm between audits. The five traps (documenting the snowflake instead of converging it, the audit that changes production, drift-blind CI, the eternal temporary, the blame hunt) and the nine-person analytics team whose 410 double-billed invoices became a one-PR loop and an under-an-hour rebuild drill.</div></li>')
    anchor = '<li><a href="post-deploy-verification-checklist.html">'
    assert anchor in t, "index anchor missing"
    t = t.replace(anchor, card + anchor, 1)
    ix.write_text(t, encoding="utf-8")
    print("index card inserted at TOP")

    # --- README: NEW line at top ---
    rd = root / "README.md"
    r = rd.read_text(encoding="utf-8")
    line = ('- **NEW: [Configuration Drift Audit for Small Teams (The Server That Stopped Matching Its Documentation)]('
            + BASE + SLUG + ')** &mdash; drift is uncommitted work running your business; a read-only quarterly audit diffs the three worst '
            'boxes against a baseline and turns every difference into a decision (fix-forward PR, revert, or documented exception), '
            'finds the pipeline gap instead of the person, and books a monthly config-hash alarm between audits; the five traps '
            '(documenting the snowflake, the audit that changes production, drift-blind CI, the eternal temporary, the blame hunt); '
            'worked example: 410 double-billed invoices from an undocumented 4am cron, rerun with seven diffs cleared as PRs and any box rebuildable in under an hour.\\n')
    rd.write_text(line + r, encoding="utf-8")
    print("README NEW line added at top")

    # --- reciprocal backlinks x3 ---
    def add_related(fname, sentence):
        p = root / fname
        t = p.read_text(encoding="utf-8")
        if SLUG in t:
            print("backlink already present:", fname); return
        anchor2 = '<p><em>Related:'
        if anchor2 in t:
            idx = t.rfind('</em></p>')
            t = t[:idx] + sentence + t[idx:]
        else:
            idx = t.rfind('</main>')
            t = t[:idx] + '<p><em>Related: ' + sentence.strip() + '</em></p>\n' + t[idx:]
        p.write_text(t, encoding="utf-8")
        print("backlink added:", fname)

    add_related("post-deploy-verification-checklist.html",
                'a week later, run the <a href="' + BASE + SLUG + '">configuration drift audit</a> &mdash; the hand-fixes and break-glass edits a hot week produces are exactly the diffs it clears into PRs.')
    add_related("hotfix-process-checklist.html",
                'the <a href="' + BASE + SLUG + '">configuration drift audit</a> is where forgotten hotfix backports surface &mdash; step 8 of the audit reads the break-glass receipts.')
    add_related("change-management-checklist.html",
                'the <a href="' + BASE + SLUG + '">configuration drift audit</a> is what the change pipeline is audited <em>against</em> &mdash; every diff it finds is a change that skipped this checklist.')

    # --- linkcheck: every relative href exists ---
    broken = []
    total = 0
    for f in root.glob("*.html"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'href="([^"#]+?\.html[^"]*)"', t):
            href = m.group(1)
            if href.startswith("http"):
                continue
            path = href.split("#")[0].split("?")[0]
            if not path:
                continue
            total += 1
            if not (root / path).exists():
                broken.append((f.name, path))
    print("linkcheck: relative html hrefs:", total, "broken:", len(broken))
    for b in broken[:10]:
        print("  BROKEN:", b)

    # --- sitemap XML well-formedness ---
    import xml.dom.minidom as md
    md.parseString(sm.read_text(encoding="utf-8"))
    print("sitemap XML valid")

if __name__ == "__main__":
    main()