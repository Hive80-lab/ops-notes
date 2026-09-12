# Simulation Preparation Checklist
**Purpose:** Prepare for mock incident response drills. Ensure readiness, clear goals, and documented expectations.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Simulation Objectives

### Primary Objectives
- [ ] **Test playbooks:** Verify correct playbook selected
- [ ] **Test escalation:** Verify Tier 1→Tier 2→Tier 3 escalation flow
- [ ] **Test communication:** Verify timely Slack updates
- [ ] **Test roles:** Verify on-call duties

### Secondary Objectives
- [ ] **Identify gaps:** What needs improvement?
- [ ] **Test documentation:** Verify incident timeline completeness
- [ ] **Test tools:** Verify monitoring, logging, alerting work
- [ ] **Measure SLAs:** Verify response times met

### Success Criteria
- [ ] **Playbook selected correctly:** Documentation confirms correct playbook
- [ ] **Escalation triggered on time:** Tier 2 escalation after 15 min, Tier 3 after 30 min
- [ ] **Communications up-to-date:** Every 15 min (Tier 1), every 30 min (Tier 2)
- [ ] **No major errors:** No missing context, no wrong playbook selection
- [ ] **Post-mortem documented:** Lessons learned captured

---

## Pre-Drill Configuration

### Environment Setup
- [ ] **Simulation environment prepared:** No impact to production
- [ ] **Alerting disabled:** Simulation alerts don't trigger real pager
- [ ] **Logs isolated:** Simulation logs not mixed with real logs
- [ ] **Data isolated:** Simulation data not mixed with production data
- [ ] **Channels configured:** Create `#simulation-[incident-id]` channel

### Incident Setup
- [ ] **Simulation scenario defined:** Clear trigger, expected impact
- [ ] **Expected behavior documented:** What should happen after drill?
- [ ] **Response time targets set:** Tier 1 in 15 min, Tier 2 in 30 min, Tier 3 in 1 hour
- [ ] **Success criteria listed:** As listed in objectives above
- [ ] **Post-mortem playbook prepped:** `incident-post-mortem-template.html` ready

### Team Setup
- [ ] **On-call assigned:** Primary on-call, backup on-call, escalation contacts
- [ ] **Roles defined:**
  - [ ] Tier 1: SRE on-call
  - [ ] Tier 2: Senior engineering lead
  - [ ] Tier 3: Engineering director (if needed)
- [ ] **Standby roles:**
  - [ ] Simulation observer: Documents observations
  - [ ] Simulation notetaker: Tracks timing, decisions
  - [ ] Reporter: Prepares post-mortem

### Tools Setup
- [ ] **Incident timeline template preloaded:** `incident-timeline-template.html` with sections
- [ ] **Slack channel created:** `#incident-simulation-[id]`
- [ ] **Alerting disabled:** No real pager or email
- [ ] **Monitoring tools accessible:** Check metrics, logs, health endpoints
- [ ] **Documentation tools ready:** Git repo, Google Docs, Confluence

---

## Documentation Setup

### Incident Definition
- [ ] **Incident title:** Clear, concise name for simulation
- [ ] **Incident description:** 2-3 sentence summary of scenario
- [ ] **Incident trigger:** What caused the simulation?
- [ ] **Expected impact:** What should the team see?
- [ ] **Success criteria:** As defined in objectives above

### Timeline Structure
- [ ] **Tier 1 section created:** First 15 min
- [ ] **Tier 2 section created:** Next 30 min
- [ ] **Tier 3 section created:** Next 1 hour
- [ ] **Resolution section created:** Final outcome
- [ ] **Post-mortem section created:** Lessons learned

### Channels Setup
- [ ] **Active channel:** `#incident-simulation-[id]`
- [ ] **Archive channel:** `#archive-incident-simulation-[id]` (after drill)
- [ ] **Observation log:** Separate channel for simulation observer notes
- [ ] **Timing log:** Separate document for timing, decisions, errors

---

## Communication Plan

### Slack Setup
- [ ] **Channel created:** `#incident-simulation-[id]`
- [ ] **Members added:** On-call, backup, observers, note-taker
- [ ] **Bot integration disabled:** No alerts fire
- [ ] **Custom emoji added:** 🎭 simulation started, ✅ simulation complete

### Alerting Disabled
- [ ] **PagerDuty paused:** No real pager notifications
- [ ] **Email alerts disabled:** No real email notifications
- [ ] **Slack alerts disabled:** No automated Slack alerts
- [ ] **Webhook disabled:** No external integrations fire

### Reporter Setup
- [ ] **Observer assigned:** One person to document observations
- [ ] **Timing tracked:** Document first response time, escalation time, resolution time
- [ ] **Decision log created:** What decisions were made? Why?
- [ ] **Error log created:** What errors occurred? How were they handled?

---

## Simulation Prerequisites Checklist

### Before Starting Simulation
- [ ] **All team members aligned:** Schedule confirmed, objectives understood
- [ ] **Simulation environment ready:** No impact to production
- [ ] **Documentation prepped:** Timeline template, channels, logs
- [ ] **Tools accessible:** Monitoring, logging, communication
- [ ] **Post-mortem plan ready:** `simulation-after-action-report.md`

### During Simulation
- [ ] **Simulation started:** Announce in `#ops-notes` or team channel
- [ ] **Simulation observer present:** Observes, documents
- [ ] **Simulation notetaker present:** Tracks timing, decisions
- [ ] **Real alerts disabled:** No unintended notifications

### After Simulation
- [ ] **Simulation paused:** Document current state
- [ ] **Timeline updated:** Final status
- [ ] **Post-mortem drafted:** Start immediately while fresh
- [ ] **Team debrief scheduled:** Share findings, set improvements

---

## Simulation Scenarios

### Scenario 1: Payment Gateway Down
- **Trigger:** Payment API returns 502 for all requests
- **Impact:** Revenue loss, customer checkout blocked
- **Tier 1:** Verify, assess, escalate (15 min)
- **Tier 2:** Check backup, customer comms (30 min)
- **Resolution:** Restore from backup, restart gateway

### Scenario 2: Data Breach (Simulated)
- **Trigger:** Security team detects unusual log activity
- **Impact:** Customer data exposure (fake data)
- **Tier 1:** Contain, preserve evidence, escalate (15 min)
- **Tier 2:** Investigate, notify customers (30 min)
- **Resolution:** Data restored from backup, legal involved

### Scenario 3: Slow Checkout Flow
- **Trigger:** p95 checkout response > 10 seconds
- **Impact:** Revenue loss, customer abandonment
- **Tier 1:** Check metrics, investigate (15 min)
- **Tier 2:** Optimize, customer comms (30 min)
- **Resolution:** Cache optimized, checkout back to 2 seconds

### Scenario 4: Phishing Attack
- **Trigger:** User reports suspicious email
- **Impact:** Potential credential compromise (fake)
- **Tier 1:** Investigate, escalate to security (15 min)
- **Tier 2:** Train affected user (30 min)
- **Resolution:** Password rotated, training plan created

---

## Documentation Fields

- [ ] **Simulation ID:** `simulation-[YYYY-MM-DD]-[id]`
- [ ] **Simulation title:** [scenario name]
- [ ] **Simulation date:** YYYY-MM-DD
- [ ] **Simulation start time:** HH:MM
- [ ] **Simulation end time:** HH:MM
- [ ] **Simulation duration:** ____ hours
- [ ] **Simulation observer:** @username
- [ ] **Simulation notetaker:** @username
- [ ] **Simulation team:** [list of team members]

---

**Usage:** Use before every mock incident response drill. Verify environment, tools, and team readiness. Document simulation details for post-mortem.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`