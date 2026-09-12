# On-Call Rotation Cadence
**Purpose:** Define on-call rotation schedules, escalation contacts, and standby processes. Move from "call the person who works last" to structured rotation.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Rotation Structure

| Tier | Role | On-Call | Escalation | Backup | Standby Period |
|------|------|---------|------------|--------|----------------|
| **Tier 1** | SRE / Infrastructure | `@sre-lead-01` | PagerDuty P1 | `@sre-lead-02` | 4 weeks |
| **Tier 2** | Senior Engineering | `@senior-lead-01` | PagerDuty P2 | `@senior-lead-02` | 4 weeks |
| **Tier 3** | Engineering Director | `@cto-lead` | PagerDuty P3 | `@vp-engineering` | 1 month |
| **Tier 4** | Operations Manager | `@ops-manager` | PagerDuty P4 | `@team-lead` | 2 weeks |

---

## Rotation Schedule

### SRE / Infrastructure Rotation (4 weeks)
| Week | On-Call | Backup | Handoff Day | Handoff Time |
|------|---------|--------|-------------|--------------|
| 1 | `@sre-lead-01` | `@sre-lead-02` | Saturday | 17:00 |
| 2 | `@sre-lead-02` | `@sre-lead-01` | Saturday | 17:00 |
| 3 | `@sre-lead-01` | `@sre-lead-02` | Saturday | 17:00 |
| 4 | `@sre-lead-02` | `@sre-lead-01` | Saturday | 17:00 |

### Senior Engineering Rotation (4 weeks)
| Week | On-Call | Backup | Handoff Day | Handoff Time |
|------|---------|--------|-------------|--------------|
| 1 | `@senior-lead-01` | `@senior-lead-02` | Saturday | 17:00 |
| 2 | `@senior-lead-02` | `@senior-lead-01` | Saturday | 17:00 |
| 3 | `@senior-lead-01` | `@senior-lead-02` | Saturday | 17:00 |
| 4 | `@senior-lead-02` | `@senior-lead-01` | Saturday | 17:00 |

### C-Level Rotation (1 month)
| Month | On-Call | Backup | Handoff Day |
|-------|---------|--------|-------------|
| September | `@cto-lead` | `@vp-engineering` | Last Saturday |
| October | `@vp-engineering` | `@cto-lead` | Last Saturday |

---

## On-Call Responsibilities

### Tier 1: SRE / Infrastructure On-Call
- **Primary duty:** Respond to Tier 1 alerts within 15 min
- **Investigate SLO breaches:** Check logs, metrics, infrastructure status
- **Communicate to Tier 2:** Escalate if unresolved in 15 min
- **Update incident timeline:** Every 15 min
- **Post-updates to Slack:** `#incident-sre`

### Tier 2: Senior Engineering On-Call
- **Primary duty:** Resolve Tier 2 incidents within 30 min
- **Assess business impact:** What does this mean for customers?
- **Allocate resources:** Assign devs, QA, design
- **Communicate to Tier 3:** Escalate if unresolved in 30 min
- **Update incident timeline:** Every 30 min

### Tier 3: C-Level On-Call
- **Primary duty:** Make major decisions for Tier 3 incidents
- **Authorize resources:** People, budget, customer comms
- **Finalize incident plan:** What will we do? How do we communicate?
- **Communicate to Tier 4:** Hand off after 1 hour or resolution
- **Document incident:** Review RCA, ensure lessons learned

### Tier 4: Operations Manager On-Call
- **Primary duty:** Monitor Tier 4 incidents after 1 hour
- **Complete RCA:** Root cause analysis, prevention
- **Close incident:** Finalize post-mortem, lessons learned
- **Track recurrence:** Similar incidents in last 30 days?
- **Share with team:** Weekly ops sync

---

## Standby Process

### Backup On-Call
- **No duty:** Only activated if primary fails to respond
- **Monitoring:** No alerts, just standby
- **Notifications:** Only escalated to primary
- **Documentation:** Log standby time for compensation

### Standby Period (4 weeks)
- **Primary active:** Always monitoring
- **Backup standby:** No alert monitoring
- **Emergency contact:** PagerDuty escalation path
- **Backup duty activated:** Only if primary fails to respond after 15 min

### Handoff Process
1. **Primary pulls incident timeline** for last incident
2. **Primary posts handoff message** in channel
3. **Backup confirms receipt** within 30 min
4. **Backup links incident timeline** in channel
5. **Primary archives incident** from active channel
6. **Documentation shared:** Handoff notes, incident timeline

---

## Escalation Contacts

### PagerDuty Integrations

**Tier 1 Escalation:**
- Primary: PagerDuty P1 → `@sre-lead-01`
- Backup: PagerDuty P2 → `@sre-lead-02`
- Auto-escalate: If no response after 15 min → `@senior-lead-01`

**Tier 2 Escalation:**
- Primary: PagerDuty P2 → `@senior-lead-01`
- Backup: PagerDuty P3 → `@senior-lead-02`
- Auto-escalate: If no response after 30 min → `@cto-lead`

**Tier 3 Escalation:**
- Primary: PagerDuty P3 → `@cto-lead`
- Backup: PagerDuty P4 → `@vp-engineering`
- Auto-escalate: If no response after 1 hour → PagerDuty VIP alert

---

## Incident Rotation Workflow

### Step 1: New Incident
1. **Alert fires** → primary on-call notified
2. **Primary acks** → backup notified of escalation path
3. **Primary investigates** → updates incident timeline
4. **Primary communicates** → posts updates to Slack

### Step 2: Incident Escalation
1. **No response after X min** → backup activated
2. **Backup takes over** → links incident timeline
3. **Backup communicates** → posts updates to Slack
4. **Primary archived** → documentation preserved

### Step 3: Incident Resolution
1. **Primary resolves** → marks incident resolved
2. **Timeline updated** → final status
3. **Post-mortem written** → linked in timeline
4. **Team notified** → lessons learned shared

---

## Documentation Fields

- [ ] **On-Call Tier:** Tier 1 / Tier 2 / Tier 3 / Tier 4
- [ ] **On-Call Person:** @username
- [ ] **Backup On-Call:** @username
- [ ] **Incident ID:** #123
- [ ] **Rotation Week:** 1-4
- [ ] **Standby Hours:** ____ hours
- [ ] **Incident Count:** [count]

---

## Rotations and On-Call Duty

| Month | Tier 1 On-Call | Tier 2 On-Call | Tier 3 On-Call | Tier 4 On-Call |
|-------|----------------|----------------|----------------|----------------|
| Sep 2026 | @sre-lead-01 | @senior-lead-01 | @cto-lead | @ops-manager |
| Oct 2026 | @sre-lead-02 | @senior-lead-02 | @vp-engineering | @team-lead |
| Nov 2026 | @sre-lead-01 | @senior-lead-01 | @cto-lead | @ops-manager |
| Dec 2026 | @sre-lead-02 | @senior-lead-02 | @vp-engineering | @team-lead |

---

## On-Call Duty Compensation

### Primary On-Call (Active Duty)
- **Pay rate:** 1.5x normal rate for Tier 1
- **Premium:** 2x normal rate for Tier 3 (major incident)
- **Documentation:** Incident time recorded in incident timeline

### Backup On-Call (Standby Duty)
- **Compensation:** 0.5x standby rate
- **Standby time:** Logged in incident timeline
- **Standby criteria:** No active incidents

### On-Call Rotation Schedule
- **Rotation length:** 4 weeks (monthly rotation)
- **Backup coverage:** Always
- **Standby period:** 4 weeks between on-call cycles

---

**Usage:** Use for on-call scheduling and escalation. Document primary, backup, and escalation paths. Works with `oncall-escalation-slack-structure.md` for communication.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`