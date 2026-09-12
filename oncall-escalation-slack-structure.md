# On-Call Escalation Slack Structure
**Purpose:** Define Slack channels, roles, and messaging conventions for on-call escalation. Move from chaotic chat to structured incident communication.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Incident Channels

| Channel Name | Purpose | Members | Auto-Invite | Urgency |
|--------------|---------|---------|-------------|---------|
| `#incident-sre` | Tier 1 SLO breach | SREs, Infra Team | Yes (PagerDuty) | P1 |
| `#incident-lead` | Tier 2 business impact | Senior Leads, Product | No (human) | P2 |
| `#incident-critical` | Tier 3 major incidents | C-level, Legal, Comms | No (human) | P3 |
| `#oncall-updates` | Non-critical updates | All Ops, Weekly | No | P4 |

### Channel Rules
- **Use reactions:** `👍` to acknowledge, `👀` to read, `🐛` to investigate
- **One message per update:** Keep updates concise
- **Link incident timeline:** Use `incident-timeline-template.html` for tracking
- **Escalate to higher tier:** Move to more urgent channel if needed

---

## Alert Message Format

### P1 / Tier 1 Alert
```
🚨 P1 - SLO BREACH DETECTED
Service: [service-name]
SLA: [SLA name] ([SLA %]) ([downtime allowed])
Metric: [metric-name] ([value])
Window: [last X minutes]
Impact: [business impact]
Responder: @sre-oncall
Status: [investigating / observed / detected]
```

### P2 / Tier 2 Update
```
🏥 INCIDENT UPDATE (Tier 2 - [time elapsed])
Status: [resolved / under control / escalating]
Root cause: [one sentence summary]
Progress: [what was tried]
Next action: [what will happen next]
Est. resolution: [time or "ongoing"]
```

### P3 / Tier 3 Update
```
🚨 MAJOR INCIDENT - ACTION REQUIRED
Service: [service-name]
Impact: [revenue / customers / compliance]
Responder: [all-critical-team]
Plan: [high-level plan]
Customer comms: [plan]
Next update: [time]
```

### P4 / Tier 4 Update
```
📝 Incident Update (Tier 4 - [time elapsed])
Status: [resolved / paused]
Root cause: [summary]
Resolution: [what was fixed]
Lessons learned: [summary]
```

---

## Escalation Workflow

### Step 1: Initial Alert (Tier 1)
1. **Automated alert fires** → posted to `#incident-sre`
2. **@sre-oncall notified** → must respond within 15 min
3. **Message format:** Use `🚨 P1 - SLO BREACH DETECTED` format
4. **First responder links incident timeline**

### Step 2: Tier 2 Escalation
1. **If unresolved after 15 min** → escalate to `#incident-lead`
2. **Senior lead notified** → must respond within 30 min
3. **Message format:** Use `🏥 INCIDENT UPDATE (Tier 2 - X min)` format
4. **SRE leads:** Keep `#incident-sre` updated on progress

### Step 3: Tier 3 Escalation
1. **If unresolved after 30 min** → escalate to `#incident-critical`
2. **CTO / Director notified** → stand-up call triggered
3. **Message format:** Use `🚨 MAJOR INCIDENT - ACTION REQUIRED` format
4. **Plan finalized:** Customer comms, resources allocated

### Step 4: Tier 4 Follow-up
1. **After 1 hour** or resolution → move to `#oncall-updates`
2. **Post-mortem drafted** → linked in incident timeline
3. **Lessons learned shared** → team weekly sync

---

## On-Call Message Templates

### Acknowledgement Template
```
👀 Received - investigating now
```

### Update Template (Progress)
```
Update: Testing hypothesis X
Timeline: Est. 15 min to verify
```

### Escalation Template
```
Escalating to Tier 2 - no resolution after 15 min
Please join: #incident-lead
```

### Resolution Template
```
✅ Resolved - check incident timeline for details
RCA: [link to post-mortem]
Lessons learned: [one sentence]
```

---

## Escalation Timer Setup

### Slack App Integration
- [ ] **Install PagerDuty / Opsgenie integration**
- [ ] **Set up escalation schedule:**
  - Tier 1: 15 min timeout
  - Tier 2: 30 min timeout
  - Tier 3: 1 hour timeout
- [ ] **Configure notification rules:**
  - Tier 1 → `#incident-sre` only
  - Tier 2 → `#incident-lead` only
  - Tier 3 → `#incident-critical` only

### Manual Escalation
- If automated escalation fails, **manually @mention** the next level
- Example: `@senior-lead Tier 2 escalation required: incident #123 unresolved`

---

## Channel Naming Conventions

### Active Incidents
- `#incident-123-sre` (Tier 1)
- `#incident-124-lead` (Tier 2)
- `#incident-125-critical` (Tier 3)

### Historical Incidents
- `#archive-incident-123-2026-09-12`

### Archive Rule
- Move completed incidents to archive after 30 days
- Keep link to post-mortem in archive

---

## Documentation Fields

- [ ] **Channel Used:** `#incident-[tier]-[id]`
- [ ] **Messages Posted:** [count]
- [ ] **Update Frequency:** Tier 1/X min, Tier 2/Y min, Tier 3/Z min
- [ ] **Escalations Triggered:** [count]
- [ ] **Resolution Time:** [hours]

---

## Best Practices

### For First Responders
- **Acknowledge within 2 min:** Use `👀` reaction
- **Update every 15 min:** Tier 1, every 30 min: Tier 2
- **Link incident timeline:** Track progress in one place
- **Escalate early:** Better to escalate than be silent

### For Senior Leads
- **Assume Tier 1 failed:** Review logs immediately
- **Clarify scope:** What are you owning?
- **Assign resources:** Devs? QA? Design?
- **Set expectations:** Timeline, communication cadence

### For C-Level
- **Focus on decisions:** Not debugging
- **Authorize resources:** People, budget, customers
- **Approve customer comms:** Email, in-app, press
- **Protect brand:** Don't expose internal details publicly

### For Everyone
- **One message per update:** Keep it concise
- **Use emoji conventions:** 🚨 P1, 🏥 P2, 🚨 P3, 📝 P4
- **Link to documentation:** RCA, playbooks, timeline
- **Learn from each incident:** Document lessons

---

**Usage:** Use for every incident. Follow the channel structure for Tier 1-4 escalation. Works with `incident-timeline-template.html` for structured tracking.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`