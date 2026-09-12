# On-Call Escalation Path Tiers
**Purpose:** Define structured escalation for different severity and business impact levels. Move from "call the owner" to defined tiers, SLAs, and channels.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Escalation Path Overview

| Tier | Definition | Response SLA | Communication Cadence |
|------|------------|--------------|----------------------|
| **Tier 1** | SLO breach within 15 minutes | Notify in **15 min** | Update every 15 min |
| **Tier 2** | Business impact > 1 hour | Notify in **30 min** | Update every 30 min |
| **Tier 3** | P1 breach > 1 hour | Notify in **1 hour** | Update every 1 hour |
| **Tier 4** | P3/P4 incidents | Notify in **4 hours** | Next business day |

---

## Tier 1: SLO Breach Response (15 min)

### Who Escalates
- **SRE / Infrastructure Lead** on-call
- **Automation** for automated detection
- **Notification channel:** PagerDuty / Opsgenie / Slack pager

### Response Actions
- [ ] **Verify SLO breach:** Check metrics, health endpoints, alert payload
- [ ] **Identify impact:** Which service? Which SLA? Which metric?
- [ ] **First investigation:** Check logs, metrics, recent changes
- [ ] **Communicate to team:** Status channel, alert channel
- [ ] **Trigger Tier 2 escalation:** If unresolved in 15 min

### Escalation Criteria
- **No response after 15 min**
- **Business impact increasing**
- **Root cause unclear**
- **Customer complaints**

### Example Alert Message
```
⚠️ P1 - SLO BREACH DETECTED
Service: api-gateway
SLA: 99.9% uptime (3 min downtime allowed)
Impact: 2.3% downtime in last hour
First responder: @sre-lead
Status: Investigating - checking logs
```

---

## Tier 2: Business Impact Response (30 min)

### Who Escalates
- **Senior Engineering Lead** on-call
- **Product Owner** if customer impact
- **Notification channel:** Slack #incident-lead channel

### Response Actions
- [ ] **Review Tier 1 findings:** What was tried? What still failing?
- [ ] **Assess business impact:** Revenue? Customers? Trust?
- [ ] **Allocate resources:** Devs? QA? Design? Customer success?
- [ ] **Update Tier 1:** Provide status, timeline, resources
- [ ] **Trigger Tier 3 escalation:** If unresolved in 30 min

### Escalation Criteria
- **No resolution after Tier 1**
- **Customer churn risk**
- **Data breach risk**
- **Compliance deadline risk**

### Example Status Update
```
🏥 INCIDENT UPDATE (30 min mark)
Status: Under control - fix in progress
Root cause: Memory leak in worker pool
Progress: Restarting pool, verifying metrics
Est. resolution: 15 min
Escalating: None (progress good)
```

---

## Tier 3: Major Incident Response (1 hour)

### Who Escalates
- **CTO / Engineering Director**
- **Customer Success Director** (if churn risk)
- **Legal / Compliance** (if breach risk)
- **Notification channel:** Stand-up call, critical Slack channel

### Response Actions
- [ ] **Finalize incident plan:** What will we do? What resources?
- [ ] **Customer comms plan:** What will we say to customers?
- [ ] **Internal sync:** Full team stand-up
- [ ] **Document incident:** Post-mortem, RCA, lessons learned
- [ ] **Trigger Tier 4 escalation:** If unresolved in 1 hour

### Escalation Criteria
- **No resolution after Tier 2**
- **Major customer churn risk**
- **Regulatory fine at risk**
- **Brand damage at risk**

### Example Stand-up Message
```
🚨 MAJOR INCIDENT - C-LEVEL INVOLVED
Service: Payment Gateway Integration
Impact: $50K revenue lost per hour, 2,000 customers affected
Plan: Rollback to last known good, notify customers, allocate chargebacks
Customer comms: Email + in-app notification
Next update: 30 min
```

---

## Tier 4: Low Priority Response (4 hours)

### Who Escalates
- **On-call manager**
- **Team lead** if recurring
- **Notification channel:** Next business day stand-up

### Response Actions
- [ ] **Root cause analysis:** Complete RCA
- [ ] **Fix deployment:** Patch, config change, rollback
- [ ] **Post-mortem:** Document lessons, prevention
- [ ] **Track recurrence:** Similar incidents in last 30 days?
- [ ] **Team learning:** Share findings in weekly ops sync

### Escalation Criteria
- **Minor operational inconvenience**
- **Low customer impact**
- **No revenue loss**
- **No brand/compliance risk**

### Example Status Update
```
📝 LOW PRIORITY - RESOLVED
Incident: Search index delayed
Root cause: Migration job stuck, timeout
Resolution: Task restarted, index back to 99% complete
Next steps: Monitor for recurring issues
```

---

## Escalation Decision Flow

### Step 1: Initial Response
- **Tier 1 (SLO breach):** Automated alert → SRE on-call → 15 min
- **Tier 2 (Business impact):** Human escalation → Senior lead → 30 min
- **Tier 3 (Major):** Full team escalation → C-level → 1 hour
- **Tier 4 (Low):** Team lead escalation → Post-mortem → 4 hours

### Step 2: Update Frequency
| Tier | First Update | Subsequent Updates |
|------|---------------|--------------------|
| Tier 1 | Within 15 min | Every 15 min |
| Tier 2 | Within 30 min | Every 30 min |
| Tier 3 | Within 1 hour | Every 1 hour |
| Tier 4 | Within 4 hours | End of shift |

### Step 3: Escalation Loop
- Tier 1 → Tier 2: No response in 15 min
- Tier 2 → Tier 3: No response in 30 min
- Tier 3 → Tier 4: No resolution in 1 hour

---

## Documentation Fields

- [ ] **Initial Tier:** Tier 1 / Tier 2 / Tier 3 / Tier 4
- [ ] **Escalation Path:** SRE → Senior Lead → CTO / Owner
- [ ] **Escalation Triggered:** Yes / No
- [ ] **Escalation Level:** Tier 1 → Tier 2 → Tier 3 → Tier 4
- [ ] **SLA Status:** Met / Missed (minutes)
- [ ] **Final Tier:** Tier 1 / Tier 2 / Tier 3 / Tier 4 (resolved)

---

## Escalation Contacts

| Tier | Role | On-Call | Emergency Contact |
|------|------|---------|-------------------|
| Tier 1 | SRE / Infrastructure | `@sre-lead` | PagerDuty: SRE-P1 |
| Tier 2 | Senior Engineering | `@senior-lead` | PagerDuty: SRE-P2 |
| Tier 3 | Engineering Director | `@cto` | PagerDuty: SRE-P3 |
| Tier 4 | Operations Manager | `@ops-manager` | PagerDuty: SRE-P4 |

---

**Usage:** Use after initial incident classification. Route incident to the correct escalation path and SLA. Works with `incident-timeline-template.html` for tracking.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`