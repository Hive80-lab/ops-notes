# Incident Technical Category Matrix
**Purpose:** Map incidents to technical categories to route to the right expert. This complements business impact (P1-P4).

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Incident Category Overview

| Category | Definition | Typical Playbooks | Owner Role |
|----------|------------|-------------------|------------|
| **Availability** | Service/endpoint unavailable or degraded | Recovery from backup, DB restore, load balancer failover | Infrastructure SRE |
| **Security** | Unauthorized access, data breach, malware | Incident response, forensic analysis, containment | Security Lead |
| **Performance** | Response time degradation, latency, throughput issues | Capacity testing, cache invalidation, optimization | Performance Engineer |
| **Functional** | Feature broken, incorrect behavior | Root cause analysis, fix development, rollback | Engineering Lead |
| **Data** | Data loss, corruption, partial inaccessibility | Backup verification, restore, data recovery | Database Admin |
| **Third-Party** | Vendor/SRE/API dependency outage | Vendor escalation, failover to alternative, SLA tracking | Vendor Manager |

---

## Category-Based First Response Actions

### Availability Incidents
- [ ] **Check endpoint status:** HTTP 500? Service down?
- [ ] **Verify health endpoint:** `/healthz`, `/status`
- [ ] **Review metrics:** CPU, memory, disk, network I/O
- [ ] **Check infrastructure logs:** Recent deployments, config changes
- [ ] **Verify dependencies:** Downstream services, third-party APIs
- [ ] **Trigger: Availability Recovery Playbook**

### Security Incidents
- [ ] **Isolate affected systems:** Cut network access, freeze accounts
- [ ] **Preserve evidence:** Logs, network captures, filesystem snapshots
- [ ] **Escalate to Security Lead:** Phishing, breach, malware
- [ ] **Notify compliance officer:** GDPR, SOC2, PII at risk
- [ ] **Trigger: Security Incident Response Playbook**

### Performance Incidents
- [ ] **Identify metrics:**
  - [ ] Response time (p95, p99)
  - [ ] Throughput (requests/sec)
  - [ ] Error rate (% 500)
- [ ] **Compare against SLO thresholds:** Alert thresholds
- [ ] **Check for recent changes:** Deployments, config updates, scaling events
- [ ] **Review scaling behavior:** Auto-scaling inactive? Scale-out complete?
- [ ] **Trigger: Performance Optimization Playbook**

### Functional Incidents
- [ ] **Confirm expected behavior:** User ticket, automated test failure
- [ ] **Check code review status:** Recently merged? Unreviewed?
- [ ] **Verify data state:** Incorrect input? Outdated cache?
- [ ] **Assess rollback risk:** High? Medium? Low?
- [ ] **Trigger: Fix Development or Rollback**

### Data Incidents
- [ ] **Verify last successful backup:** RPO timeline
- [ ] **Check backup integrity:** Restore test? Verification logs?
- [ ] **Assess data loss extent:** Rows affected? Tables affected? Time range?
- [ ] **Contact database admin:** Restore from point-in-time recovery?
- [ ] **Trigger: Data Recovery Playbook**

### Third-Party Incidents
- [ ] **Verify vendor status:** Public outage? Paged vendor?
- [ ] **Check SLA response time:** Vendor committed? Verified?
- [ ] **Identify workaround:** Can you switch providers? Can you fail over?
- [ ] **Update customer communications:** Is customer aware?
- [ ] **Track SLA penalties:** Credit calculations, legal escalation

---

## Combined Category × Impact Matrix

| Category | P1 Business Impact | P2 Business Impact | P3 Business Impact | P4 Business Impact |
|----------|-------------------|-------------------|-------------------|-------------------|
| **Availability** | Payment gateway down → Exec notified | Core API degraded → Users notified | Non-critical API degraded | Minor UI delay |
| **Security** | Data breach → Legal, Compliance | Credential theft → Customer comms | Unauthorized access (self) | Attempted access logged |
| **Performance** | No revenue impact | Slow checkout flow | Slow article load | Slow login |
| **Functional** | Checkout broken | Feature unavailable | Search broken | Form validation error |
| **Data** | Customer data lost | User profile corrupted | Config backup lost | Log file truncated |
| **Third-Party** | Payments via Stripe blocked | Email via SendGrid degraded | Support via Zendesk degraded | Analytics via GA paused |

---

## Documentation Fields

- [ ] **Category:** Availability / Security / Performance / Functional / Data / Third-Party
- [ ] **First Expert:** Infrastructure / Security / Performance / Engineering / DBA / Vendor Mgr
- [ ] **Category Confirmation:** User ticket / Test failure / Automation alert
- [ ] **Workaround Available:** Yes / No / Pending
- [ ] **SLA / SLO Threshold:** ___ min / ___ ms

---

**Usage:** Use after impact classification. Route incident to the correct expert and tooling stack. Works best with `incident-response-plan-template-small-teams.html`.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`