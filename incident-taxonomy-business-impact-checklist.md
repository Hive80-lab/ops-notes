# Incident Business Impact Checklist
**Purpose:** Classify incident severity by business impact, not just technical severity. Use the 90-second impact call to assign the right response resource.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Quick Impact Call — 90 Seconds

### 1. Revenue Impact
- [ ] **Is revenue blocked or significantly reduced?**
  - Yes → **P1 (Critical)**: Revenue lost per minute calculated, executive notified within 15 minutes.
  - No → Continue.

- [ ] **Is billing/payment system down?**
  - Yes → **P1 (Critical)**: Payment gateway status checked, finance notified.
  - No → Continue.

### 2. Data Impact
- [ ] **Is customer data breached, exposed, or deleted?**
  - Yes → **P1 (Critical)**: Data breach response playbook triggered, legal/compliance notified.
  - No → Continue.

- [ ] **Is user data corrupted or partially inaccessible?**
  - Yes → **P2 (High)**: Restore from backup attempted, affected users notified.
  - No → Continue.

### 3. Customer Trust Impact
- [ ] **Is customer trust visibly damaged (customer-facing messaging required)?**
  - Yes → **P2 (High)**: Customer comms plan triggered.
  - No → Continue.

- [ ] **Are major customers threatening churn or legal action?**
  - Yes → **P2 (High)**: Account manager notified, retention resources allocated.

### 4. Compliance Impact
- [ ] **Is regulatory reporting deadline at risk?**
  - Yes → **P2 (High)**: Compliance officer notified, deadlines re-evaluated.
  - No → Continue.

- [ ] **Is audit access or logs at risk?**
  - Yes → **P2 (High)**: Audit trail preserved, forensic analysis considered.

### 5. Brand Impact
- [ ] **Is the incident publicly visible or likely to become public?**
  - Yes → **P2 (High)**: PR/social media protocols activated.
  - No → Continue.

- [ ] **Is internal culture affected (team morale, burnout)?**
  - Yes → **P3 (Medium)**: Team lead notified, burnout risk assessed.

---

## Impact Tier Mapping

| Tier | Business Impact | Example Scenarios | Response SLA |
|------|----------------|-------------------|--------------|
| **P1** | Revenue loss > $X/min or data breach | Payment gateway down, data breach, core service unavailable | **15 min** notification, **30 min** first update |
| **P2** | Significant customer trust/compliance impact | Data partial loss, compliance deadline risk, major customer churn threat | **30 min** notification, **1 hour** first update |
| **P3** | Moderate brand/operational impact | Feature unavailable to some customers, minor compliance gap | **1 hour** notification, **2 hours** first update |
| **P4** | Minor operational inconvenience | Non-critical service degradation, documentation issue | **4 hours** notification, **next business day** update |

---

## Documentation Fields

- [ ] **Impact Date/Time:** _______________
- [ ] **Estimated Revenue Loss:** $_______/min
- [ ] **Customers Affected:** _______________
- [ ] **Publicly Visible:** Yes / No
- [ ] **Regulatory Requirement Triggered:** Yes / No
- [ ] **Triage Category:** Revenue / Data / Trust / Compliance / Brand

---

**Usage:** Use after the 60-second severity call. Document impact to align resources and communication cadence. Use the `_template.html` for structured form logging.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`