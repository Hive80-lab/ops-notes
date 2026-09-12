# Incident Root Cause Categorization Checklist
**Purpose:** Systematically categorize root causes to prevent recurrence. Move from ad-hoc fixes to structured improvements.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Root Cause Categories

| Category | Definition | Common Examples |
|----------|------------|-----------------|
| **Infrastructure** | Hardware/OS/network failure | Server crash, disk full, network partition |
| **Human Error** | Process, process, process | Wrong config, delete data, mis-delete |
| **Development** | Code defect, missing tests | Bug, unhandled exception, race condition |
| **Operational** | Change management failure | Deploy went bad, rollback failed |
| **Third-Party** | External dependency failure | Vendor outage, API limit reached |
| **External** | Outage not caused by you | Internet outage, cloud provider outage |
| **Process** | Gap in procedure, not technology | Missing SOP, unclear escalation |
| **Change Request** | Unplanned change caused issue | Feature introduced bug |
| **Data Integrity** | Corrupted data, stale state | Missing migration, orphaned records |
| **Misconfiguration** | Wrong settings applied | Wrong region, incorrect environment |

---

## Root Cause Analysis Flow

### 1. Immediate Investigation
- [ ] **Review alert context:** What triggered the alert? Metric thresholds?
- [ ] **Examine logs:** System logs, application logs, error traces
- [ ] **Check recent changes:** Deployments (commit hash), config changes, environment variables
- [ ] **Interview witnesses:** Who saw what? When?

### 2. Hypothesis Generation
- [ ] **Hypothesis 1:** Infrastructure failure
- [ ] **Hypothesis 2:** Human error
- [ ] **Hypothesis 3:** Development defect
- [ ] **Hypothesis 4:** Operational failure
- [ ] **Hypothesis 5:** Third-party dependency
- [ ] **Hypothesis 6:** External factor

### 3. Evidence Collection
- [ ] **Collect logs:** Full logs around incident timeframe
- [ ] **Capture metrics:** CPU, memory, disk, network, error rates
- [ ] **Review changes:** Git commits, config diffs, deployment manifests
- [ ] **Preserve evidence:** Screenshot, database snapshot, network capture
- [ ] **Interview team members:** First responders, developers, operations

### 4. Verification
- [ ] **Test hypothesis 1:** Simulate or repeat failure
- [ ] **Test hypothesis 2:** Verify configuration/state
- [ ] **Test hypothesis 3:** Review code, reproduce bug
- [ ] **Test hypothesis 4:** Confirm change was applied
- [ ] **Test hypothesis 5:** Check external status pages
- [ ] **Test hypothesis 6:** Verify internet/cloud status

### 5. Final Categorization
- [ ] **Confirm root cause:** Which category matches best?
- [ ] **Confirm contributing factors:** Anything else?
- [ ] **Confirm evidence:** Logs? Metrics? Screenshots?
- [ ] **Confirm confidence level:** High / Medium / Low

---

## RCA Documentation Fields

- [ ] **Root Cause Category:** _______________
- [ ] **Root Cause Description:** _______________
- [ ] **Contributing Factors:** _______________
- [ ] **Evidence Collected:**
  - [ ] Logs collected
  - [ ] Metrics captured
  - [ ] Screenshots taken
  - [ ] Snapshots preserved
- [ ] **First Responder Names:** _______________
- [ ] **Investigation Duration:** ____ hours
- [ ] **Confidence Level:** High / Medium / Low

---

## Prevention Checklist (by Category)

### Infrastructure → Prevention
- [ ] **Monitor hardware health:** CPU, memory, disk, network
- [ ] **Automated failover:** Multi-AZ? Load balancer health checks?
- [ ] **Capacity planning:** Auto-scaling enabled? Scaling rules defined?

### Human Error → Prevention
- [ ] **Review approval gates:** Config changes need review?
- [ ] **Sanity checks:** Can't delete critical data without confirmation?
- [ ] **Training:** Regular on-call training, incident drills

### Development → Prevention
- [ ] **Test coverage:** Unit tests, integration tests, E2E tests
- [ ] **Code review:** All PRs reviewed?
- [ ] **Pre-deployment checks:** Staging environment validated?

### Operational → Prevention
- [ ] **Automated rollback:** Immediate rollback on failure?
- [ ] **Deployment safety:** Canary deployments? Feature flags?
- [ ] **Monitoring:** Alerting before production impact?

### Third-Party → Prevention
- [ ] **Vendor SLAs:** Documented response times and penalties?
- [ ] **Alternative providers:** What happens if this vendor fails?
- [ ] **Health checks:** Dependency uptime monitoring?

### External → Prevention
- [ ] **External dependency alerts:** Notify when outage detected?
- [ ] **Mitigation plans:** Workarounds if dependency fails?
- [ ] **Diversify dependencies:** Multi-cloud, multi-provider?

### Process → Prevention
- [ ] **SOPs documented:** All procedures written down?
- [ ] **Rollout procedures:** Training documented? Checked?
- [ ] **Post-mortem process:** Root cause captured and shared?

### Change Request → Prevention
- [ ] **Feature flags:** Rollback without code change?
- [ ] **Gradual rollout:** 10% → 50% → 100% with monitoring?
- [ ] **Observability:** Can we see impact before 100% rollout?

### Data Integrity → Prevention
- [ ] **Data migration tests:** Verified before production?
- [ ] **Incremental backups:** RPO target met?
- [ ] **Data validation:** Schema validation, data integrity checks?

### Misconfiguration → Prevention
- [ ] **Environment consistency:** Config sync across environments?
- [ ] **Secret management:** Environment variables encrypted?
- [ ] **Validation:** Can't deploy invalid config?

---

**Usage:** Complete after post-mortem. Use to prevent recurrence of similar incidents. Validate against existing post-mortem template: `incident-post-mortem-template.html`.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`