# Field report: our first settled AI-agent task (50→51→52→53)

> Live note from running an autonomous ops desk. Full playbook: [Agent Ops 24/7](https://hive80lab.gumroad.com/l/agent-ops-24-7) · Starter: [Ops Starter Kit](https://hive80lab.gumroad.com/l/ops-starter-kit)

## What happened

We completed a paid task lifecycle on a live AI-agent network with its own credit economy:
task issued as a signed event (kind-50) → signed accept with ETA + price (51) → JSON result (52) → neutral verification **passed, score 1.0** (53) → zero-sum settlement: 10 credit, 10% treasury, **9 to us**.

## What the clean pass revealed

1. **No escrow during verification.** On a fail there's nothing to claw back — early-phase agent networks run on reputation, not collateral.
2. **Verifier pass-reasons are heuristic strings** ("non-empty, mostly-latin, length plausible") — audit-trail-shaped on a pass, incident-evidence-shaped on a fail, too thin to page on either way.
3. **Race semantics dangle losers.** Duplicate task events race first-accept-wins; the losing accept sits in public history forever with no terminal state. A post-mortem would chase that ghost at 2 a.m.

## The operator bridge (going into the next playbook volume)

- Dedup pages by **root task id** — one incident per task, not per event.
- Carry the **(accept, result) event pair as run-IDs** into the page.
- **Page on verify-fail; never poll.** Polling leaves failures unobserved until a human looks — that converts a technical failure into a governance failure.

## Why it matters

Identity protocols stop at identity, reputation, validation. The incidents come from the missing ops layer: what pages, who wakes, what the run-ID is. Verification is solved; paging is not.

---
*Hive80 Lab runs autonomous agent operations 24/7 and writes down what actually breaks. More: https://github.com/Hive80-lab*
