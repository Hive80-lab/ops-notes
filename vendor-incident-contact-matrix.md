# Vendor Incident Contact Matrix
**Purpose:** Centralized vendor contact matrix for incident response. Know who to call, how to reach them, and what to expect.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Vendor Matrix Overview

| Vendor | Tier | Product/Service | On-Call | Email | Phone | PagerDuty | SLA Response | SLA Compensation |
|--------|------|----------------|---------|-------|-------|-----------|--------------|------------------|
| Stripe | Tier 1 | Payment Gateway | Support | support@stripe.com | +1 (855) 641-2193 | Stripe-P1 | 15 min | Credit per SLA violation |
| SendGrid | Tier 1 | Email Service | Support | support@sendgrid.com | +1 (855) 481-7446 | SendGrid-P1 | 15 min | Refund unused credits |
| CloudFlare | Tier 1 | CDN / DDoS Protection | 24/7 Support | 24x7@cloudflare.com | 1-844-933-1553 | CloudFlare-P1 | 15 min | Credit per SLA violation |
| AWS | Tier 2 | Cloud Infrastructure | Global Support | support@aws.amazon.com | 1-800-767-1727 | AWS-P1 | 30 min | Service credits |
| Vercel | Tier 2 | Frontend Hosting | 24/7 Support | support@vercel.com | 1-855-973-8355 | Vercel-P1 | 15 min | Credits |
| Gumroad | Tier 2 | Payment / Orders | Support | support@gumroad.com | [internal] | Gumroad-P1 | 15 min | Service credits |
| Datadog | Tier 1 | Monitoring | Support | support@datadoghq.com | 1-855-252-2362 | Datadog-P1 | 15 min | Credits |
| New Relic | Tier 1 | Monitoring | Support | support@newrelic.com | 1-855-207-6061 | NewRelic-P1 | 15 min | Credits |
| Sentry | Tier 1 | Error Tracking | Support | support@sentry.io | 1-415-795-3566 | Sentry-P1 | 15 min | Credits |
| Intercom | Tier 1 | Customer Support | Support | support@intercom.com | 1-888-330-9241 | Intercom-P1 | 15 min | Credits |
| Zendesk | Tier 2 | Customer Support | 24/7 Support | support@zendesk.com | 1-888-888-8247 | Zendesk-P1 | 30 min | Credits |
| Cloudinary | Tier 2 | Media Hosting | Support | support@cloudinary.com | 1-310-909-3173 | Cloudinary-P1 | 15 min | Credits |

---

## Vendor Categories

### Tier 1: Critical Infrastructure Vendors
**Products/Services:** Payments, CDNs, DDoS protection, monitoring, error tracking

| Vendor | On-Call | PagerDuty | SLA | Escalation Path |
|--------|---------|-----------|-----|-----------------|
| Stripe | Support | Stripe-P1 | 15 min | PagerDuty → VP Engineering |
| SendGrid | Support | SendGrid-P1 | 15 min | PagerDuty → VP Engineering |
| CloudFlare | 24/7 Support | CloudFlare-P1 | 15 min | PagerDuty → VP Engineering |
| Datadog | Support | Datadog-P1 | 15 min | PagerDuty → VP Engineering |
| New Relic | Support | NewRelic-P1 | 15 min | PagerDuty → VP Engineering |
| Sentry | Support | Sentry-P1 | 15 min | PagerDuty → VP Engineering |
| Intercom | Support | Intercom-P1 | 15 min | PagerDuty → VP Engineering |

**Vendor Escalation Rules:**
- **PagerDuty escalates automatically:** If no response after 15 min, escalate to VP Engineering
- **Customer comms:** If vendor SLA violated, notify customers immediately
- **Credit tracking:** Log all SLA violations, calculate credits

### Tier 2: Secondary Infrastructure Vendors
**Products/Services:** Cloud infrastructure, frontend hosting, media hosting, customer support

| Vendor | On-Call | PagerDuty | SLA | Escalation Path |
|--------|---------|-----------|-----|-----------------|
| AWS | Global Support | AWS-P1 | 30 min | PagerDuty → SRE Lead |
| Vercel | 24/7 Support | Vercel-P1 | 15 min | PagerDuty → SRE Lead |
| Gumroad | Support | Gumroad-P1 | 15 min | PagerDuty → SRE Lead |
| Zendesk | 24/7 Support | Zendesk-P1 | 30 min | PagerDuty → SRE Lead |
| Cloudinary | Support | Cloudinary-P1 | 15 min | PagerDuty → SRE Lead |

**Vendor Escalation Rules:**
- **PagerDuty escalates after 15 min:** Escalate to SRE Lead
- **Customer comms:** If vendor SLA violated after 30 min, notify customers
- **Credit tracking:** Log SLA violations, calculate credits

---

## Vendor Contact Info

### Stripe
- **Email:** support@stripe.com
- **Phone:** +1 (855) 641-2193
- **Web:** https://support.stripe.com/contact
- **SLA:** 15 min response, 99.9% uptime
- **Compensation:** Credit per SLA violation (auto-credited)

### SendGrid
- **Email:** support@sendgrid.com
- **Phone:** +1 (855) 481-7446
- **Web:** https://help.sendgrid.com/hc/en-us/requests/new
- **SLA:** 15 min response, 99.9% uptime
- **Compensation:** Refund unused credits

### CloudFlare
- **Email:** 24x7@cloudflare.com
- **Phone:** 1-844-933-1553
- **Web:** https://www.cloudflarestatus.com/incidents
- **SLA:** 15 min response, 99.99% uptime
- **Compensation:** Credit per SLA violation (auto-credited)

### AWS
- **Email:** support@aws.amazon.com
- **Phone:** 1-800-767-1727
- **Web:** https://status.aws.amazon.com/
- **SLA:** 30 min response, 99.99% uptime
- **Compensation:** Service credits (auto-credited)

### Vercel
- **Email:** support@vercel.com
- **Phone:** 1-855-973-8355
- **Web:** https://vercel.statuspage.io/
- **SLA:** 15 min response, 99.9% uptime
- **Compensation:** Credits (auto-credited)

### Gumroad
- **Email:** support@gumroad.com
- **Phone:** [internal, see SRE Lead]
- **Web:** https://help.gumroad.com/hc/en-us/requests/new
- **SLA:** 15 min response, 99.9% uptime
- **Compensation:** Service credits (via API)

### Datadog
- **Email:** support@datadoghq.com
- **Phone:** 1-855-252-2362
- **Web:** https://www.datadoghq.com/support/
- **SLA:** 15 min response, 99.99% uptime
- **Compensation:** Credits (auto-credited)

### New Relic
- **Email:** support@newrelic.com
- **Phone:** 1-855-207-6061
- **Web:** https://support.newrelic.com/hc/en-us/requests/new
- **SLA:** 15 min response, 99.99% uptime
- **Compensation:** Credits (auto-credited)

### Sentry
- **Email:** support@sentry.io
- **Phone:** 1-415-795-3566
- **Web:** https://sentry.io/support/
- **SLA:** 15 min response, 99.99% uptime
- **Compensation:** Credits (auto-credited)

### Intercom
- **Email:** support@intercom.com
- **Phone:** 1-888-330-9241
- **Web:** https://developers.intercom.com/
- **SLA:** 15 min response, 99.9% uptime
- **Compensation:** Credits (auto-credited)

### Zendesk
- **Email:** support@zendesk.com
- **Phone:** 1-888-888-8247
- **Web:** https://support.zendesk.com/hc/en-us/requests/new
- **SLA:** 30 min response, 99.9% uptime
- **Compensation:** Credits (auto-credited)

### Cloudinary
- **Email:** support@cloudinary.com
- **Phone:** 1-310-909-3173
- **Web:** https://cloudinary.com/feature/help
- **SLA:** 15 min response, 99.9% uptime
- **Compensation:** Credits (auto-credited)

---

## Escalation Protocols

### Step 1: Initial Contact
1. **Contact method:** PagerDuty → Email → Phone
2. **Message format:** Incident ID, severity, impact, what you need
3. **Response time:** Vendor SLA target (15 min for Tier 1, 30 min for Tier 2)
4. **Observation log:** Document time, contact method, response

### Step 2: If No Response
1. **Escalate to primary on-call:** PagerDuty escalates automatically
2. **Alternative contact:** Try different channel (email vs phone)
3. **Check vendor status page:** Is the vendor having an outage?
4. **Prepare workaround:** Can you switch providers?

### Step 3: SLA Violation
1. **Calculate credit:** Vendor SLA violation → credit
2. **Document SLA violation:** Time, severity, credit amount
3. **Notify customer:** If customer affected, notify them
4. **Track credits:** Log in financial system

### Step 4: Vendor Performance Review
1. **Review SLA violations:** How often do they fail?
2. **Evaluate alternative providers:** Is there a better vendor?
3. **Negotiate terms:** Update SLA terms if needed
4. **Consider switching:** If SLA violations are frequent

---

## Vendor Management

### Vendor Performance Tracking

| Vendor | SLA Violations (Last 90 days) | Response Time Average | Customer Impact | Rating | Action Needed |
|--------|-------------------------------|----------------------|-----------------|--------|---------------|
| Stripe | [count] | ____ min | [yes/no] | Excellent / Good / Needs Improvement | [none / review / switch] |
| SendGrid | [count] | ____ min | [yes/no] | Excellent / Good / Needs Improvement | [none / review / switch] |
| CloudFlare | [count] | ____ min | [yes/no] | Excellent / Good / Needs Improvement | [none / review / switch] |
| AWS | [count] | ____ min | [yes/no] | Excellent / Good / Needs Improvement | [none / review / switch] |
| Vercel | [count] | ____ min | [yes/no] | Excellent / Good / Needs Improvement | [none / review / switch] |
| Gumroad | [count] | ____ min | [yes/no] | Excellent / Good / Needs Improvement | [none / review / switch] |

### Vendor Onboarding Process
1. **Evaluate vendor:** SLA, support quality, pricing
2. **Negotiate terms:** Ensure SLA terms are documented
3. **Onboard vendor:** Add to matrix, enable PagerDuty
4. **Monitor performance:** Track SLA violations, response times
5. **Review regularly:** Quarterly vendor performance review

### Vendor Offboarding Process
1. **Evaluate alternatives:** Is there a better vendor?
2. **Plan migration:** Transition away from vendor
3. **Notify customers:** If vendor is critical, notify customers
4. **Switch providers:** Migrate to alternative vendor
5. **Close vendor:** Remove from matrix, archive contacts

---

## Documentation Fields

- [ ] **Vendor:** [vendor name]
- [ ] **Contact Email:** support@vendor.com
- [ ] **Contact Phone:** [phone number]
- [ ] **PagerDuty Escalation:** [PagerDuty ID]
- [ ] **SLA Response:** [target response time]
- [ ] **SLA Compensation:** [type of compensation]
- [ ] **SLA Violations (90 days):** [count]
- [ ] **Customer Impact:** [yes/no]
- [ ] **Vendor Rating:** Excellent / Good / Needs Improvement
- [ ] **Action Needed:** [none / review / switch]

---

## Vendor SLA Summary

| Vendor | SLA Response | SLA Uptime | Compensation Type | Auto-Credit |
|--------|--------------|------------|-------------------|-------------|
| Stripe | 15 min | 99.9% | Credit | Yes |
| SendGrid | 15 min | 99.9% | Refund | Yes |
| CloudFlare | 15 min | 99.99% | Credit | Yes |
| AWS | 30 min | 99.99% | Credits | Yes |
| Vercel | 15 min | 99.9% | Credits | Yes |
| Gumroad | 15 min | 99.9% | Credits | Yes |
| Datadog | 15 min | 99.99% | Credits | Yes |
| New Relic | 15 min | 99.99% | Credits | Yes |
| Sentry | 15 min | 99.99% | Credits | Yes |
| Intercom | 15 min | 99.9% | Credits | Yes |
| Zendesk | 30 min | 99.9% | Credits | Yes |
| Cloudinary | 15 min | 99.9% | Credits | Yes |

---

**Usage:** Use during vendor incidents. Contact vendor using the matrix, track SLA violations, and calculate credits. Works with `vendor-escalation-protocols.md` and `customer-vendor-incident-comms.md`.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`