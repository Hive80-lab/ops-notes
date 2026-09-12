# Customer Vendor Incident Communications
**Purpose:** Communicate vendor incidents to customers transparently and professionally. Manage expectations, provide solutions, reduce churn.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Communication Guidelines

### Core Principles
1. **Transparency:** Always inform customers of vendor incidents
2. **Timeliness:** Notify customers when SLA is violated
3. **Accuracy:** Provide correct information, admit gaps
4. **Empathy:** Acknowledge customer impact, apologize
5. **Solution:** Provide workaround, timeline, compensation

### When to Notify Customers
- **Tier 1 vendor (15 min SLA):** Notify if vendor response > 15 min
- **Tier 2 vendor (30 min SLA):** Notify if vendor response > 30 min
- **Critical vendor (payments, CDNs):** Notify immediately
- **Customer impact:** If customer experiences downtime, notify them

---

## Communication Templates

### Email Template

**Subject:** Vendor incident affecting [service] — [status]

**Body:**

**Dear [Customer Name],**

**We wanted to inform you that a vendor incident is affecting [service].** This incident began at [timestamp], and our team is actively working with [vendor name] to resolve it.

**Impact:**
- [What is affected?]
- [How does it impact customer experience?]
- [Estimated downtime: [time]]

**What we are doing:**
- Monitoring vendor status page: [link]
- Escalating to vendor executives if needed
- Preparing workaround [if available]
- Tracking SLA violations

**What you can do:**
- [Workaround if available: e.g., use alternative service]
- [Expectation management: e.g., no new orders during outage]
- [Contact support: [link]]

**Timeline:**
- Expected resolution: [time or "ongoing"]
- Update cadence: Every 30 minutes
- We will notify you immediately when resolution is confirmed

**Compensation:**
- [If SLA violated]: We will provide [credit/refund/extension] for affected period.

**If you have questions, please reach out to our support team:** [link]

**Sincerely,**
[Your Name]
[Your Role]

---

### In-App Notification Template

**Message:**

**⚠️ Vendor Incident — [service]**

We are experiencing an issue with [service] due to a vendor outage at [vendor name]. 

**Impact:**
- [What is affected?]
- [Estimated downtime: [time]]

**Current Status:**
- [Resolving / Investigating / Waiting for vendor]

**Updated:** [timestamp]

[Link to status page: https://...]
[Link to support: https://...]

---

### Support Ticket Template

**To Customer Support:**

**Customer:** [Customer Name]
**Incident:** Vendor incident affecting [service]
**Customer Impact:** [describe customer's issue]

**Information to Customer:**
- [Incident start time]
- [Vendor name and SLA]
- [Current status]
- [Expected resolution time]
- [Workaround if available]
- [Compensation if SLA violated]

**Action Items:**
- [ ] Notify customer via email
- [ ] Update customer in-app notification
- [ ] Link incident timeline
- [ ] Track SLA violation
- [ ] Calculate compensation

**Support Ticket:** [customer-ticket-id]

---

## Communication Cadence

### Immediate Notification (Tier 1)
- **Time:** Within 15 minutes of SLA violation
- **Channel:** Email + in-app notification
- **Content:** Incident start, impact, vendor info, status

### Updates (Every 30 minutes)
- **Time:** Every 30 minutes until resolution
- **Channel:** Email + in-app notification
- **Content:** Status update, estimated resolution, new information

### Resolution Notification
- **Time:** As soon as vendor incident is resolved
- **Channel:** Email + in-app notification
- **Content:** Resolution confirmed, compensation applied, next steps

---

## Customer Impact Categories

### Minor Impact
- **Definition:** Non-essential service degraded
- **Customer action:** None required
- **Comms:** In-app notification only (no email)
- **Compensation:** None (unless SLA violated)

### Moderate Impact
- **Definition:** Essential service degraded, minor inconvenience
- **Customer action:** Can still use service but with limitations
- **Comms:** Email + in-app notification
- **Compensation:** Credit (if SLA violated)

### Major Impact
- **Definition:** Critical service unavailable for extended period
- **Customer action:** Cannot use service
- **Comms:** Email + in-app notification + priority support
- **Compensation:** Significant credit or refund

### Severe Impact
- **Definition:** Critical service unavailable, significant revenue loss
- **Customer action:** Cannot use service, may seek alternative provider
- **Comms:** Email + in-app notification + phone call
- **Compensation:** Full refund + credit

---

## SLA Violation and Compensation

### Compensation Types

| Compensation Type | When to Use | Amount | Process |
|-------------------|-------------|--------|---------|
| **Credit** | Minor/SLA violation | [amount based on pricing] | Auto-applied by vendor |
| **Refund** | Major/SLA violation | [full refund of affected period] | Manual refund by finance |
| **Extension** | Contract term length | [extend contract by [time]] | Manual by account manager |
| **Compensation** | Severe impact | [full credit + compensation] | Manual by finance + legal |

### Compensation Calculation

**Example 1: Credit**
- SLA target: 99.9% uptime
- Actual uptime: 98%
- Downtime: 1.9%
- Billing: $1,000/month
- Credit: $1,000 × 1.9% = $19.00

**Example 2: Refund**
- Customer impacted for 4 hours
- SLA target: 15 min response
- SLA violation: 4 hours = 240 minutes
- Credit: $240 / 60 min × $10/min = $40.00

**Example 3: Extension**
- Customer contract: 12 months
- SLA violation: 1 month
- Extension: Contract extended by 1 month

---

## Communication Workflow

### Step 1: Incident Detected
- [ ] **SLA violation detected:** Vendor response > SLA target
- [ ] **Check customer impact:** Which customers are affected?
- [ ] **Calculate compensation:** Based on SLA violation

### Step 2: Prepare Comms
- [ ] **Draft email template:** Use template above
- [ ] **Identify affected customers:** List of customers affected
- [ ] **Identify support staff:** Customer success, account managers
- [ ] **Prepare status page:** Update status page with incident info

### Step 3: Notify Customers
- [ ] **Send email:** To all affected customers
- [ ] **Send in-app notification:** To all affected customers
- [ ] **Notify account manager:** If customer is high value
- [ ] **Update support queue:** If support tickets are affected

### Step 4: Update Cadence
- [ ] **Update every 30 min:** Status, timeline, compensation
- [ ] **Communicate resolution:** When vendor incident resolved
- [ ] **Confirm compensation:** Apply credit/refund

### Step 5: Follow-Up
- [ ] **Send follow-up email:** Incident resolved, compensation applied
- [ ] **Track customer satisfaction:** Did customer experience improve?
- [ ] **Review customer churn risk:** Any customers at risk of churning?

---

## Documentation Fields

- [ ] **Incident ID:** `vendor-[YYYY-MM-DD]-[vendor]-[id]`
- [ ] **Customer affected:** [yes/no]
- [ ] **Customers notified:** [count]
- [ ] **Notification method:** Email / In-app / Both
- [ ] **SLA violated:** Yes / No
- [ ] **SLA violation duration:** ____ min
- [ ] **Compensation type:** Credit / Refund / Extension / Compensation
- [ ] **Compensation amount:** $____
- [ ] **Resolution time:** ____:____
- [ ] **Follow-up needed:** Yes / No

---

## Post-Incident Follow-Up

### Customer Churn Risk Assessment
- [ ] **Customer churn risk:** High / Medium / Low
- [ ] **Actions taken:**
  - [ ] Personal call to customer
  - [ ] Extra support attention
  - [ ] Enhanced monitoring
  - [ ] Contract review
- [ ] **Outcomes:**
  - [ ] Customer retained: Yes / No
  - [ ] Compensation: [amount]
  - [ ] Feedback: [customer feedback]

### Customer Satisfaction Survey
- [ ] **Survey sent:** Yes / No
- [ ] **Survey response rate:** ____%
- [ ] **Overall satisfaction:** [rating]
- [ ] **Improvements requested:** [list]
- [ ] **Lessons learned:** [summary]

### Process Improvement
- [ ] **Update vendor list:** Based on incident
- [ ] **Improve SLA terms:** Negotiate better SLA
- [ ] **Update comms template:** Based on feedback
- [ ] **Improve monitoring:** Add vendor monitoring

---

## Best Practices

### For Customer Comms
- **Be transparent:** Don't hide vendor incidents
- **Be honest:** Admit gaps, don't over-promise
- **Be empathetic:** Acknowledge customer impact, apologize
- **Be specific:** Provide timeline, compensation, next steps
- **Be timely:** Notify customers when SLA is violated

### For Account Managers
- **Personal contact:** Call high-value customers personally
- **Explain impact:** Clearly explain how vendor incident affects customer
- **Offer support:** Provide extra support during incident
- **Track churn risk:** Monitor customer satisfaction during and after incident
- **Follow up:** Check in after incident resolved

### For Support Team
- **Update tickets:** Add incident info to customer tickets
- **Set expectations:** Tell customers expected resolution time
- **Provide workaround:** If workaround exists, provide to customers
- **Track SLA violations:** Document SLA violations, calculate compensation
- **Escalate if needed:** Escalate to account manager if customer churn risk

---

**Usage:** Use for every vendor incident that affects customers. Communicate transparently, manage expectations, provide compensation. Works with `vendor-incident-contact-matrix.md` and `vendor-escalation-protocols.md`.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`