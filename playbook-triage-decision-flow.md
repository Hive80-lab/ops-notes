# Playbook Triage Decision Flow
**Purpose:** Quick decision flow to select the right playbook for any incident. Match category × severity × impact → playbook.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Triage Decision Flow

### Step 1: 60-Second Severity Call
**Is money or data stuck?**

- **Yes (P1):** Move to **Availability/Security** playbooks
- **No:** Proceed to Step 2

### Step 2: Business Impact Call
**Is this a business/brand/compliance risk?**

- **Yes (P2):** Move to **High Impact** playbooks
- **No:** Proceed to Step 3

### Step 3: Technical Category Call
**What type of issue is this?**

- **Availability:** Service down or degraded
- **Security:** Unauthorized access, breach, malware
- **Performance:** Slow response, latency issues
- **Functional:** Feature broken, incorrect behavior
- **Data:** Data loss, corruption, partial inaccessibility
- **Third-Party:** Vendor/SRE/API dependency outage

### Step 4: Playbook Selection
**Select playbook based on Category × Severity:**

| Category | P1 Impact | P2 Impact | P3 Impact | P4 Impact |
|----------|-----------|-----------|-----------|-----------|
| **Availability** | Tier 1 Availability Playbook | Tier 2 Availability Playbook | Tier 3 Availability Playbook | Tier 4 Availability Playbook |
| **Security** | Tier 1 Security Playbook | Tier 2 Security Playbook | Tier 3 Security Playbook | Tier 4 Security Playbook |
| **Performance** | Tier 1 Performance Playbook | Tier 2 Performance Playbook | Tier 3 Performance Playbook | Tier 4 Performance Playbook |
| **Functional** | Tier 1 Functional Playbook | Tier 2 Functional Playbook | Tier 3 Functional Playbook | Tier 4 Functional Playbook |
| **Data** | Tier 1 Data Playbook | Tier 2 Data Playbook | Tier 3 Data Playbook | Tier 4 Data Playbook |
| **Third-Party** | Tier 1 Third-Party Playbook | Tier 2 Third-Party Playbook | Tier 3 Third-Party Playbook | Tier 4 Third-Party Playbook |

---

## Key Incident Playbooks

### Availability Playbooks

| Playbook | Purpose | First Response |
|----------|---------|----------------|
| `first-30-minutes-incident-response` | Initial response for any incident | Verify, assess, communicate |
| `availability-recovery-from-backup` | Service down, restore from backup | Check backup, restore, verify |
| `load-balancer-failover` | LB not routing traffic | Check LB config, restart, verify |
| `database-connection-pool-exhaustion` | DB connection pool full | Restart pool, increase limit, fix leak |

### Security Playbooks

| Playbook | Purpose | First Response |
|----------|---------|----------------|
| `data-breach-first-24-hours` | Data breach detected | Isolate, preserve, escalate, notify |
| `credential-compromise-response` | Credential leak/compromise | Revoke credentials, rotate passwords, notify |
| `phishing-response-checklist-small-teams` | Phishing attack | Report, investigate, train |

### Performance Playbooks

| Playbook | Purpose | First Response |
|----------|---------|----------------|
| `performance-degradation-first-15-min` | Slow response, latency | Check metrics, review changes, optimize |
| `cache-invalidation-strategy` | Stale data response | Clear cache, verify invalidation, monitor |
| `database-optimization` | DB query slowness | Check queries, add indexes, optimize |

### Functional Playbooks

| Playbook | Purpose | First Response |
|----------|---------|----------------|
| `feature-broken-detected` | Feature not working | Check code, revert, fix, test |
| `integration-failure` | External API failure | Check API status, fallback, retry |
| `race-condition-detected` | Unexpected behavior | Review concurrency, add lock, fix race |

### Data Playbooks

| Playbook | Purpose | First Response |
|----------|---------|----------------|
| `data-loss-restore-from-backup` | Data deleted/corrupted | Check backup, restore, verify |
| `data-corruption-detected` | Data integrity issues | Stop write access, restore from backup, validate |
| `data-migration-failed` | Migration incomplete | Rollback migration, fix, retry |

### Third-Party Playbooks

| Playbook | Purpose | First Response |
|----------|---------|----------------|
| `vendor-incident-coordination` | Vendor outage | Check vendor status, escalate, workaround |
| `third-party-api-failure` | External API down | Check API status, fallback, notify vendor |
| `customer-vendor-incident-comms` | Customer impacted by vendor | Notify customer, provide updates, compensate |

---

## Quick Reference: Decision Tree

```
START
  │
  ├─ 60-second severity call: money/data stuck?
  │    ├─ YES → P1 → Availability/Security playbooks
  │    └─ NO  → business impact call
  │           ├─ YES → P2 → High Impact playbooks
  │           └─ NO  → technical category call
  │                  ├─ Availability → Tier 1 Availability Playbook
  │                  ├─ Security → Tier 1 Security Playbook
  │                  ├─ Performance → Tier 1 Performance Playbook
  │                  ├─ Functional → Tier 1 Functional Playbook
  │                  ├─ Data → Tier 1 Data Playbook
  │                  └─ Third-Party → Tier 1 Third-Party Playbook
  │
  └─ Document decision in incident timeline
```

---

## Triage Documentation Fields

- [ ] **Severity Call:** P1 / P2 / P3 / P4
- [ ] **Business Impact:** Revenue / Data / Trust / Compliance / Brand
- [ ] **Category:** Availability / Security / Performance / Functional / Data / Third-Party
- [ ] **Selected Playbook:** [playbook-name]
- [ ] **Playbook Reasoning:** [1 sentence summary]
- [ ] **First Response Actions:** [list of initial actions]

---

## Common Playbook Combinations

### Scenario 1: Payment Gateway Down (Availability + Business)
- **Severity:** P1 (money stuck)
- **Category:** Availability
- **Playbook:** `first-30-minutes-incident-response` + `availability-recovery-from-backup`
- **Escalation:** Tier 1 → Tier 2 → Tier 3

### Scenario 2: Phishing Attack (Security)
- **Severity:** P2 (compliance risk)
- **Category:** Security
- **Playbook:** `phishing-response-checklist-small-teams`
- **Escalation:** Tier 1 → Tier 2

### Scenario 3: Slow Checkout Flow (Performance + Business)
- **Severity:** P2 (revenue impact)
- **Category:** Performance
- **Playbook:** `performance-degradation-first-15-min` + `performance-optimization`
- **Escalation:** Tier 1 → Tier 2

### Scenario 4: Wrong Customer Address (Functional)
- **Severity:** P4 (minor inconvenience)
- **Category:** Functional
- **Playbook:** `feature-broken-detected` + `integration-failure`
- **Escalation:** Tier 1 → Tier 4

---

## Playbook Selection Rules

### Rule 1: Always Start with First 30 Minutes
Every incident should start with `first-30-minutes-incident-response` playbook to establish baseline: verify, assess, communicate.

### Rule 2: Severity Trumps Category
A P1 Security incident (data breach) always uses Security playbooks, even if it's also an Availability issue.

### Rule 3: Business Impact Defines Escalation
A P2 data corruption issue (no breach, but data lost) should be escalated to Tier 2, not Tier 1.

### Rule 4: Use Tier-Specific Playbooks
Tier 1 playbooks focus on quick investigation and communication. Tier 2+ playbooks focus on resolution and customer comms.

### Rule 5: Multiple Playbooks Allowed
Advanced incidents may require multiple playbooks. Example: Payment down (Availability) → Data loss (Data) → Customer comms (Third-Party).

---

**Usage:** Use immediately after incident classification. Select the right playbook based on severity × category. Link to playbook in incident timeline.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`