# Playbook Selection Rules
**Purpose:** Define clear rules for selecting the correct playbook. Avoid decision paralysis and ensure consistent response.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Fundamental Rules

### Rule 1: Start with First 30 Minutes
**Every incident must start with `first-30-minutes-incident-response` playbook.**

- **Purpose:** Establish baseline, verify severity, communicate to stakeholders
- **Duration:** First 30 minutes only
- **After 30 min:** Switch to resolution playbooks
- **Exception:** If severity escalates, use Tier 2+ playbooks immediately

### Rule 2: Severity Defines Tier, Not Playbook
**P1 = Tier 1, P2 = Tier 2, P3 = Tier 3, P4 = Tier 4**

- **Tier 1 Playbooks:** Investigation and communication only
- **Tier 2 Playbooks:** Resolution and customer comms
- **Tier 3 Playbooks:** Major incidents, executive involvement, customer communication
- **Tier 4 Playbooks:** Post-resolution, RCA, lessons learned

### Rule 3: Category Trumps Secondary Factors
**Primary category overrides secondary factors.**

- Example: A payment gateway outage (Availability) is an Availability playbook, not a Data playbook
- Example: A database corruption (Data) is a Data playbook, not a Functional playbook

### Rule 4: Multiple Playbooks May Apply
**Complex incidents may require multiple playbooks.**

- Example: Payment gateway down → Availability playbook + Data playbook + Third-Party playbook
- Example: Phishing attack → Security playbook + Training playbook + Comms playbook

### Rule 5: Always Document Reasoning
**Each playbook selection must be documented with reasoning.**

- Document: Severity, Category, Why This Playbook
- Link: Incident timeline entry
- Review: Post-mortem to ensure playbook effectiveness

---

## Category-Based Selection Rules

### Availability Incidents
**Primary Rule:** Always use Availability playbook first.

| Severity | Playbook | Focus |
|----------|----------|-------|
| P1 | Tier 1 Availability Playbook | Investigation and communication |
| P2 | Tier 2 Availability Playbook | Resolution and customer comms |
| P3 | Tier 3 Availability Playbook | Executive involvement, major comms |
| P4 | Tier 4 Availability Playbook | RCA, lessons learned |

**Sub-playbooks (when needed):**
- `availability-recovery-from-backup`
- `load-balancer-failover`
- `database-connection-pool-exhaustion`
- `api-service-down`

### Security Incidents
**Primary Rule:** Always use Security playbook first.

| Severity | Playbook | Focus |
|----------|----------|-------|
| P1 | Tier 1 Security Playbook | Containment, preserve evidence, escalate |
| P2 | Tier 2 Security Playbook | Investigation, customer notification |
| P3 | Tier 3 Security Playbook | Legal, compliance, press comms |
| P4 | Tier 4 Security Playbook | RCA, training, prevention |

**Sub-playbooks (when needed):**
- `data-breach-first-24-hours`
- `credential-compromise-response`
- `phishing-response-checklist-small-teams`
- `malware-isolation-and-removal`

### Performance Incidents
**Primary Rule:** Always use Performance playbook first.

| Severity | Playbook | Focus |
|----------|----------|-------|
| P1 | Tier 1 Performance Playbook | Investigation, root cause |
| P2 | Tier 2 Performance Playbook | Resolution, customer comms |
| P3 | Tier 3 Performance Playbook | Engineering changes, optimization |
| P4 | Tier 4 Performance Playbook | RCA, monitoring improvements |

**Sub-playbooks (when needed):**
- `performance-degradation-first-15-min`
- `cache-invalidation-strategy`
- `database-optimization`
- `network-latency-reduction`

### Functional Incidents
**Primary Rule:** Always use Functional playbook first.

| Severity | Playbook | Focus |
|----------|----------|-------|
| P1 | Tier 1 Functional Playbook | Root cause, fix development |
| P2 | Tier 2 Functional Playbook | Rollback, customer comms |
| P3 | Tier 3 Functional Playbook | Engineering changes, stakeholder comms |
| P4 | Tier 4 Functional Playbook | RCA, feature improvements |

**Sub-playbooks (when needed):**
- `feature-broken-detected`
- `integration-failure`
- `race-condition-detected`
- `configuration-error-correction`

### Data Incidents
**Primary Rule:** Always use Data playbook first.

| Severity | Playbook | Focus |
|----------|----------|-------|
| P1 | Tier 1 Data Playbook | Containment, preserve evidence |
| P2 | Tier 2 Data Playbook | Restore from backup, notify customers |
| P3 | Tier 3 Data Playbook | Complex restoration, compliance comms |
| P4 | Tier 4 Data Playbook | RCA, backup improvements |

**Sub-playbooks (when needed):**
- `data-loss-restore-from-backup`
- `data-corruption-detected`
- `data-migration-failed`
- `database-recovery-procedures`

### Third-Party Incidents
**Primary Rule:** Always use Third-Party playbook first.

| Severity | Playbook | Focus |
|----------|----------|-------|
| P1 | Tier 1 Third-Party Playbook | Vendor escalation, workaround |
| P2 | Tier 2 Third-Party Playbook | Customer comms, SLA tracking |
| P3 | Tier 3 Third-Party Playbook | Vendor penalties, legal escalation |
| P4 | Tier 4 Third-Party Playbook | RCA, alternative providers |

**Sub-playbooks (when needed):**
- `vendor-incident-coordination`
- `third-party-api-failure`
- `customer-vendor-incident-comms`
- `vendor-performance-review`

---

## Tier-Specific Selection Rules

### Tier 1 (15 min)
**Tier 1 playbooks focus on investigation and communication.**

**Rules:**
1. **Never escalate without reason:** Document why escalation is needed
2. **Communicate early:** Update Slack, incident timeline
3. **Link to timeline:** Track every step
4. **Acknowledge immediately:** Use emoji reactions, confirm receipt

**Tier 1 Playbooks:**
- `first-30-minutes-incident-response`
- Tier 1 Availability / Security / Performance / Functional / Data / Third-Party playbooks

### Tier 2 (30 min)
**Tier 2 playbooks focus on resolution and customer comms.**

**Rules:**
1. **Allocate resources:** Devs? QA? Design? Customer success?
2. **Update timeline:** Document every decision
3. **Customer comms:** If business impact > 30 min, notify customers
4. **Escalate if needed:** If unresolved in 30 min, escalate to Tier 3

**Tier 2 Playbooks:**
- Tier 2 Availability / Security / Performance / Functional / Data / Third-Party playbooks
- `incident-response-plan-template-small-teams`

### Tier 3 (1 hour)
**Tier 3 playbooks focus on major incidents, executive involvement, stakeholder comms.**

**Rules:**
1. **Finalize plan:** What will we do? What resources? What timeline?
2. **Customer comms:** Notify customers of impact, solution, compensation
3. **Executive involvement:** CTO / Director notified
4. **Post-mortem started:** Document incident, root cause, prevention

**Tier 3 Playbooks:**
- Tier 3 Availability / Security / Performance / Functional / Data / Third-Party playbooks
- `incident-post-mortem-template`
- `incident-communication-templates`

### Tier 4 (4 hours)
**Tier 4 playbooks focus on RCA, lessons learned, prevention.**

**Rules:**
1. **Complete RCA:** Document root cause, contributing factors
2. **Prevention plan:** What changes will prevent recurrence?
3. **Track recurrence:** Similar incidents in last 30 days?
4. **Team learning:** Share findings in weekly ops sync

**Tier 4 Playbooks:**
- Tier 4 Availability / Security / Performance / Functional / Data / Third-Party playbooks
- `simulation-after-action-report`
- `incident-taxonomy-root-cause-categorization`

---

## Special Cases

### Mixed Impact Incidents
**Example:** Payment gateway down (Availability + Business + Data)

**Rule:** Use Availability playbook for Tier 1, Data playbook for Tier 2, Third-Party playbook for customer comms.

**Selection:**
- Tier 1: `first-30-minutes-incident-response` (Availability focus)
- Tier 2: `data-loss-restore-from-backup` (Data recovery)
- Tier 3: `third-party-api-failure` (Vendor escalation)

### Recurring Incidents
**Rule:** Use `simulation-after-action-report` playbook to prevent recurrence.

**Steps:**
1. Review post-mortem from previous incident
2. Identify root cause (use `incident-taxonomy-root-cause-categorization`)
3. Create prevention plan
4. Schedule mock drill (use `incident-response-drill-schedule-template`)
5. Track recurrence

### Unexpected Third-Party Impact
**Rule:** Use `customer-vendor-incident-comms` playbook immediately.

**Steps:**
1. Notify customer (provide transparency)
2. Escalate to vendor (use `vendor-incident-coordination`)
3. Track SLA (record vendor response time)
4. Compensate if SLA violated

---

## Documentation Fields

- [ ] **Primary Playbook:** [playbook-name]
- [ ] **Secondary Playbooks:** [playbook-name, playbook-name]
- [ ] **Playbook Selection Rule:** [rule number]
- [ ] **Reasoning:** [why this playbook]
- [ ] **Tier:** Tier 1 / Tier 2 / Tier 3 / Tier 4
- [ ] **Escalation Needed:** Yes / No

---

**Usage:** Use for every incident selection. Follow rules for consistency. Document decisions in incident timeline.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`