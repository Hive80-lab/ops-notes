# Vendor Escalation Protocols
**Purpose:** Define escalation steps for vendor incidents. Move from initial contact to resolution, tracking, and compensation.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Escalation Protocol Overview

| Tier | Definition | Response SLA | Escalation Path | Customer Notification |
|------|------------|--------------|-----------------|-----------------------|
| **Tier 1** | Vendor response within SLA | SLA target (15 min) | PagerDuty → VP Engineering | When SLA violated |
| **Tier 2** | Vendor response after SLA | SLA + 15 min | PagerDuty → SRE Lead | When SLA violated |
| **Tier 3** | Vendor fails to respond | After 1 hour | VIP Escalation → Legal | Immediately |

---

## Tier 1: Vendor Response (Within SLA)

### When to Use Tier 1
- Vendor responds within SLA target (15 min)
- Vendor acknowledges incident
- Vendor working on resolution

### Response Steps
1. **Contact vendor:**
   - [ ] **PagerDuty:** Use vendor PagerDuty escalation path
   - [ ] **Email:** support@vendor.com (include incident details)
   - [ ] **Phone:** Vendor phone number

2. **Provide incident context:**
   - [ ] **Incident ID:** [ID]
   - [ ] **Impact:** [what is failing?]
   - [ ] **Severity:** P1-P4
   - [ ] **Time observed:** [timestamp]
   - [ ] **What you need:** [resolution or workaround]

3. **Track vendor response:**
   - [ ] **Time contacted:** ____:____
   - [ ] **Vendor response time:** ____:____ (total minutes: ____)
   - [ ] **Vendor acknowledgment:** Yes / No
   - [ ] **Vendor estimated resolution:** ____ minutes

4. **Document in timeline:**
   - [ ] **Timeline entry:** Vendor contacted, acknowledged
   - [ ] **Vendor response:** [summary of response]
   - [ ] **Next steps:** [what vendor will do]

### Tier 1 Communication
- **Slack update:** "Vendor contacted, awaiting response (SLA: 15 min)"
- **Timeline update:** Document vendor response
- **Customer comms:** Not required unless SLA violated

### Tier 1 Success Criteria
- [ ] **Vendor responds within SLA:** 15 min (Tier 1 vendor) or 30 min (Tier 2 vendor)
- [ ] **Vendor acknowledges incident:** Yes
- [ ] **Vendor provides estimated resolution:** Yes
- [ ] **Vendor updates timeline:** Yes

---

## Tier 2: Extended Vendor Response (After SLA)

### When to Use Tier 2
- Vendor response after SLA target
- Vendor working on resolution, but slower than SLA
- SLA violation detected

### Response Steps
1. **Escalate to higher tier:**
   - [ ] **PagerDuty escalation:** PagerDuty automatically escalates after SLA
   - [ ] **Email escalation:** Send escalation email to vendor VP
   - [ ] **Phone escalation:** Call vendor VP directly

2. **Check vendor status page:**
   - [ ] **Check vendor status page:** Is vendor having outage?
   - [ ] **Document status page:** [link, timestamp]
   - [ ] **Update customer:** If customer affected, notify them

3. **Prepare workaround:**
   - [ ] **Identify workaround:** Can you switch providers?
   - [ ] **Prepare fallback:** Database, CDN, payment gateway
   - [ ] **Test workaround:** Verify workaround works

4. **Track SLA violation:**
   - [ ] **Time SLA violated:** ____:____ (total minutes: ____)
   - [ ] **SLA violation duration:** ____ minutes
   - [ ] **Calculate credit:** [amount]
   - [ ] **Document SLA violation:** [reason, impact]

5. **Document in timeline:**
   - [ ] **Timeline entry:** Vendor SLA violated
   - [ ] **Escalation:** Vendor VP notified
   - [ ] **Workaround:** [summary of workaround]

### Tier 2 Communication
- **Slack update:** "Vendor SLA violated, escalated to VP (SLA + 15 min)"
- **Timeline update:** Document SLA violation, workaround
- **Customer comms:** Notify customers if SLA violated

### Tier 2 Success Criteria
- [ ] **Vendor responds after SLA:** Yes
- [ ] **Escalation triggered:** Yes
- [ ] **Vendor provides workaround:** Yes
- [ ] **SLA violation documented:** Yes

---

## Tier 3: Critical Vendor Failure (1+ hours)

### When to Use Tier 3
- Vendor fails to respond after 1 hour
- Critical vendor outage (payments, CDNs, monitoring)
- Customer churn risk
- Revenue loss > $X per minute

### Response Steps
1. **VIP escalation:**
   - [ ] **PagerDuty VIP escalation:** Notify vendor executive
   - [ ] **Email escalation:** vendor-executive@vendor.com
   - [ ] **Phone escalation:** Call vendor CEO/CFO

2. **Prepare customer comms:**
   - [ ] **Notify customers:** Email, in-app notification, support ticket
   - [ ] **Explain impact:** What is failing? What will it cost?
   - [ ] **Provide workaround:** How can customers work around?
   - [ ] **Offer compensation:** Credits, refunds, extensions

3. **Customer comms plan:**
   - [ ] **Notify customers:** All affected customers
   - [ ] **Communication cadence:** Update every 30 min
   - [ ] **Comms channel:** Email, in-app, support ticket
   - [ ] **Comms template:** Use `customer-vendor-incident-comms.md`

4. **Document in timeline:**
   - [ ] **Timeline entry:** VIP escalation triggered
   - [ ] **Customer comms:** Notify customers
   - [ ] **Workaround:** [summary of workaround]

### Tier 3 Communication
- **Slack update:** "CRITICAL: Vendor SLA violated > 1 hour, VIP escalation"
- **Timeline update:** Document VIP escalation, customer comms
- **Customer comms:** Notify all affected customers

### Tier 3 Success Criteria
- [ ] **Vendor responds after 1 hour:** Yes
- [ ] **VIP escalation triggered:** Yes
- [ ] **Customer comms executed:** Yes
- [ ] **Compensation provided:** Yes

---

## Vendor Escalation Decision Flow

```
START
  │
  ├─ Vendor outage detected
  │    ├─ Vendor status page: outage declared?
  │    │    ├─ YES → Verify outage, escalate
  │    │    └─ NO  → Contact vendor directly
  │    └─ Contact vendor (PagerDuty/email/phone)
  │
  ├─ Vendor response received?
  │    ├─ YES → Track response, update timeline
  │    └─ NO  → Check response time
  │           ├─ Within SLA → Tier 1 (continue tracking)
  │           ├─ After SLA → Tier 2 (escalate)
  │           └─ > 1 hour → Tier 3 (VIP escalation, customer comms)
  │
  └─ Incident resolved?
       ├─ YES → Document resolution, update timeline
       └─ NO  → Escalate again
```

---

## SLA Violation Tracking

### SLA Violation Types

| Violation Type | Definition | SLA Target | SLA Threshold | Compensation |
|----------------|------------|------------|---------------|--------------|
| **Response time** | Vendor response slower than SLA | 15 min (Tier 1) / 30 min (Tier 2) | SLA + 15 min | Credit |
| **Uptime** | Vendor uptime < SLA target | 99.9% (Tier 1) / 99.99% (Tier 2) | SLA - 1% | Credit |
| **Resolution** | Vendor fails to resolve | Within SLA | SLA + 30 min | Credit |

### SLA Violation Calculation

**Example 1: Response Time Violation**
- SLA target: 15 min
- Actual response: 30 min
- SLA violation: 30 - 15 = 15 min
- Compensation: Credit for 15 min (based on pricing)

**Example 2: Uptime Violation**
- SLA target: 99.9% uptime
- Actual uptime: 98%
- SLA violation: 99.9% - 98% = 1.9% downtime
- Compensation: Credit based on downtime

**Example 3: Resolution Failure**
- SLA target: Resolution within 15 min
- Actual resolution: 45 min
- SLA violation: 45 - 15 = 30 min
- Compensation: Credit for 30 min (based on pricing)

---

## Vendor Incident Documentation

### Incident ID Format
- `vendor-[YYYY-MM-DD]-[vendor]-[id]`

### Example Incident ID
- `vendor-2026-09-13-stripe-payment-api-down-001`

### Documentation Fields
- [ ] **Incident ID:** `vendor-[YYYY-MM-DD]-[vendor]-[id]`
- [ ] **Vendor:** [vendor name]
- [ ] **Incident start:** ____:____
- [ ] **Incident end:** ____:____
- [ ] **Total duration:** ____ hours
- [ ] **SLA target:** ____ min
- [ ] **SLA violation:** Yes / No
- [ ] **SLA violation duration:** ____ min
- [ ] **Compensation amount:** $____
- [ ] **Customer affected:** Yes / No
- [ ] **Workaround used:** Yes / No

---

## Vendor SLA Enforcement

### Automatic SLA Tracking
- [ ] **PagerDuty tracking:** Monitor vendor PagerDuty escalations
- [ ] **Email tracking:** Log vendor response times
- [ ] **Phone tracking:** Log phone call durations
- [ ] **Status page tracking:** Monitor vendor status page

### SLA Violation Log

| Incident ID | Vendor | SLA Target | Violation | Duration | Compensation | Date |
|-------------|--------|------------|-----------|----------|--------------|------|
| vendor-2026-09-13-stripe-001 | Stripe | 15 min | Yes | 30 min | $____ | 2026-09-13 |
| vendor-2026-09-13-sendgrid-001 | SendGrid | 15 min | No | 10 min | $0 | 2026-09-13 |
| vendor-2026-09-14-aws-001 | AWS | 30 min | Yes | 60 min | $____ | 2026-09-14 |

### SLA Compliance Score

| Vendor | Total Incidents | SLA Violations | Compliance Score | Trend |
|--------|-----------------|----------------|------------------|-------|
| Stripe | [count] | [count] | ____% | ↑ / ↓ / → |
| SendGrid | [count] | [count] | ____% | ↑ / ↓ / → |
| CloudFlare | [count] | [count] | ____% | ↑ / ↓ / → |
| AWS | [count] | [count] | ____% | ↑ / ↓ / → |
| Vercel | [count] | [count] | ____% | ↑ / ↓ / → |
| Gumroad | [count] | [count] | ____% | ↑ / ↓ / → |

---

## Prevention and Improvement

### Vendor Performance Review
- **Frequency:** Quarterly
- **Reviewers:** SRE Lead, VP Engineering
- **Review criteria:** SLA compliance, response times, customer impact

### Vendor Negotiation
- **Frequency:** Annually
- **Negotiators:** VP Engineering, CFO
- **Negotiation goals:** Improve SLA, reduce cost, increase uptime

### Vendor Switching
- **Trigger:** SLA violations > [threshold] or customer churn risk
- **Process:** Evaluate alternatives, plan migration, switch providers
- **Documentation:** Update `vendor-incident-contact-matrix.md`

---

**Usage:** Use for every vendor incident. Follow escalation protocol, track SLA violations, calculate credits. Works with `vendor-incident-contact-matrix.md` and `customer-vendor-incident-comms.md`.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`