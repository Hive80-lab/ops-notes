# Incident Response Playbook Matrix
**Purpose:** Quick-reference matrix matching incidents to playbooks. Use this during triage to select the right playbook immediately.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Incident Matrix

| Incident Type | Trigger | Severity | Category | Playbook | Tier | First Response |
|---------------|---------|----------|----------|----------|------|----------------|
| **Service Down** | HTTP 500 / 503 / timeout | P1 | Availability | `first-30-minutes-incident-response` | Tier 1 | Verify, assess |
| **Database Down** | Connection refused | P1 | Availability | `first-30-minutes-incident-response` | Tier 1 | Check DB status |
| **Load Balancer Down** | No routing | P1 | Availability | `load-balancer-failover` | Tier 1 | Check LB config |
| **Connection Pool Full** | Error 503 | P1 | Availability | `database-connection-pool-exhaustion` | Tier 1 | Restart pool |
| **Data Breach** | Unusual log activity | P1 | Security | `data-breach-first-24-hours` | Tier 1 | Contain, preserve |
| **Credential Leak** | Suspicious auth logs | P1 | Security | `credential-compromise-response` | Tier 1 | Revoke, rotate |
| **Phishing Attack** | User reports | P2 | Security | `phishing-response-checklist-small-teams` | Tier 1 | Investigate, report |
| **Slow Response** | p95/p99 > threshold | P2 | Performance | `performance-degradation-first-15-min` | Tier 1 | Check metrics |
| **Slow Checkout** | Revenue impact | P2 | Performance | `performance-optimization` | Tier 1 | Review code |
| **Feature Broken** | User ticket | P2 | Functional | `feature-broken-detected` | Tier 1 | Check code |
| **Wrong Address** | Customer error | P4 | Functional | `integration-failure` | Tier 1 | Fix integration |
| **Data Loss** | No rows in table | P1 | Data | `data-loss-restore-from-backup` | Tier 1 | Restore from backup |
| **Data Corruption** | Data integrity issues | P2 | Data | `data-corruption-detected` | Tier 1 | Stop writes |
| **Migration Failed** | Migration incomplete | P2 | Data | `data-migration-failed` | Tier 1 | Rollback, retry |
| **Vendor Down** | Vendor status page | P1 | Third-Party | `vendor-incident-coordination` | Tier 1 | Escalate vendor |
| **API Down** | HTTP 502 / 504 | P1 | Third-Party | `third-party-api-failure` | Tier 1 | Check API status |
| **Customer Payment Down** | Payment failed | P1 | Third-Party | `third-party-api-failure` | Tier 1 | Notify customer |

---

## Quick Triage Matrix

### Severity → Tier Mapping

| Severity | SLA | Update Frequency |
|----------|-----|------------------|
| **P1** | 15 min | Every 15 min |
| **P2** | 30 min | Every 30 min |
| **P3** | 1 hour | Every 1 hour |
| **P4** | 4 hours | Next business day |

### Category → Playbook Family

| Category | Core Playbook | Tier-Specific Playbooks |
|----------|---------------|--------------------------|
| **Availability** | `first-30-minutes-incident-response` | Tier 1 → Tier 2 → Tier 3 → Tier 4 |
| **Security** | `first-30-minutes-incident-response` | Tier 1 → Tier 2 → Tier 3 → Tier 4 |
| **Performance** | `first-30-minutes-incident-response` | Tier 1 → Tier 2 → Tier 3 → Tier 4 |
| **Functional** | `first-30-minutes-incident-response` | Tier 1 → Tier 2 → Tier 3 → Tier 4 |
| **Data** | `first-30-minutes-incident-response` | Tier 1 → Tier 2 → Tier 3 → Tier 4 |
| **Third-Party** | `first-30-minutes-incident-response` | Tier 1 → Tier 2 → Tier 3 → Tier 4 |

---

## Tier-Specific Playbooks

### Tier 1 (Investigation + Communication)
| Incident | Playbook | Focus |
|----------|----------|-------|
| Service Down | `first-30-minutes-incident-response` | Verify, assess, communicate |
| Data Breach | `data-breach-first-24-hours` | Contain, preserve, escalate |
| Slow Response | `performance-degradation-first-15-min` | Check metrics, investigate |
| Feature Broken | `feature-broken-detected` | Check code, investigate |
| Data Loss | `data-loss-restore-from-backup` | Check backup, restore |
| Vendor Down | `vendor-incident-coordination` | Escalate vendor, find workaround |

### Tier 2 (Resolution + Customer Comms)
| Incident | Playbook | Focus |
|----------|----------|-------|
| Service Down | Tier 2 Availability Playbook | Resolve, customer comms |
| Data Breach | Tier 2 Security Playbook | Investigate, notify customers |
| Slow Response | Tier 2 Performance Playbook | Optimize, customer comms |
| Feature Broken | Tier 2 Functional Playbook | Fix, customer comms |
| Data Loss | Tier 2 Data Playbook | Restore, customer comms |
| Vendor Down | Tier 2 Third-Party Playbook | Customer comms, SLA tracking |

### Tier 3 (Major Incident + Executive Involvement)
| Incident | Playbook | Focus |
|----------|----------|-------|
| Service Down | Tier 3 Availability Playbook | Executive, major comms |
| Data Breach | Tier 3 Security Playbook | Legal, compliance, press comms |
| Slow Response | Tier 3 Performance Playbook | Engineering changes, optimization |
| Feature Broken | Tier 3 Functional Playbook | Engineering changes, stakeholder comms |
| Data Loss | Tier 3 Data Playbook | Complex restoration, compliance comms |
| Vendor Down | Tier 3 Third-Party Playbook | Vendor penalties, legal escalation |

### Tier 4 (RCA + Prevention)
| Incident | Playbook | Focus |
|----------|----------|-------|
| Service Down | Tier 4 Availability Playbook | RCA, prevention |
| Data Breach | Tier 4 Security Playbook | Prevention, training |
| Slow Response | Tier 4 Performance Playbook | RCA, monitoring |
| Feature Broken | Tier 4 Functional Playbook | RCA, feature improvements |
| Data Loss | Tier 4 Data Playbook | RCA, backup improvements |
| Vendor Down | Tier 4 Third-Party Playbook | RCA, alternative providers |

---

## Common Playbook Combinations

### Payment Gateway Down
| Incident | Playbook | Tier |
|----------|----------|------|
| Initial | `first-30-minutes-incident-response` | Tier 1 |
| Recovery | `availability-recovery-from-backup` | Tier 2 |
| Customer Comms | `customer-vendor-incident-comms` | Tier 2 |
| Post-Mortem | `incident-post-mortem-template` | Tier 4 |

### Phishing Attack
| Incident | Playbook | Tier |
|----------|----------|------|
| Initial | `first-30-minutes-incident-response` | Tier 1 |
| Investigation | `phishing-response-checklist-small-teams` | Tier 1 |
| Training | `training-response-plan` | Tier 4 |
| Prevention | `simulation-after-action-report` | Tier 4 |

### Slow Checkout Flow
| Incident | Playbook | Tier |
|----------|----------|------|
| Initial | `first-30-minutes-incident-response` | Tier 1 |
| Performance | `performance-optimization` | Tier 2 |
| Customer Comms | `customer-comms-for-degradation` | Tier 2 |
| Post-Mortem | `incident-post-mortem-template` | Tier 4 |

### Feature Broken (Release 1.0.0)
| Incident | Playbook | Tier |
|----------|----------|------|
| Initial | `first-30-minutes-incident-response` | Tier 1 |
| Fix | `feature-broken-detected` | Tier 1 |
| Rollback | `rollback-procedure` | Tier 2 |
| Post-Mortem | `incident-post-mortem-template` | Tier 4 |

---

## How to Use This Matrix

### Step 1: Identify Incident
- **Trigger:** What caused the incident?
- **Severity:** P1-P4 (use `incident-severity-matrix-template.html`)
- **Category:** Availability/Security/Performance/Functional/Data/Third-Party

### Step 2: Find Playbook
- **Row match:** Find incident in Incident Matrix
- **Column match:** Check severity → tier → playbook
- **Cross-reference:** Validate with Playbook Selection Rules

### Step 3: Start Playbook
- **Tier 1:** Focus on investigation and communication
- **Tier 2+:** Focus on resolution and customer comms
- **Document:** Link playbook to incident timeline

### Step 4: Adjust if Needed
- **Escalation:** Move to higher tier if unresolved
- **Multiple Playbooks:** Add sub-playbooks if needed
- **Prevention:** Use post-mortem playbook for recurrence prevention

---

## Documentation Fields

- [ ] **Incident Trigger:** [trigger]
- [ ] **Severity:** P1 / P2 / P3 / P4
- [ ] **Category:** Availability / Security / Performance / Functional / Data / Third-Party
- [ ] **Playbook Selected:** [playbook-name]
- [ ] **Tier:** Tier 1 / Tier 2 / Tier 3 / Tier 4
- [ ] **Escalation Plan:** [how to escalate if needed]

---

**Usage:** Use during triage to quickly select the right playbook. Match incident type, severity, and category to the matrix row. Link to playbook in incident timeline.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`