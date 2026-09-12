# Simulation Execute and Observe Checklist
**Purpose:** Execute mock incident response drills and document observations. Measure team performance against success criteria.

**Status:** READY | **Product links:** /l/ops-starter-kit-vol-2 | **Links:** incident-response-pillars-overview.md

---

## Simulation Execution Phase

### Start of Simulation
- [ ] **Simulation announced:** `#incident-simulation-[id]` channel created
- [ ] **Simulation observer notified:** Observes and documents
- [ ] **Simulation notetaker ready:** Tracks timing and decisions
- [ ] **Incident timeline template preloaded:** All sections created
- [ ] **Real alerts disabled:** No real pager or email

### Phase 1: Tier 1 Response (0-15 minutes)
- [ ] **Alert triggered:** Simulation alert fires (mock)
- [ ] **First responder acknowledges:** Within 2 minutes
- [ ] **Severity call completed:** Within 5 minutes
- [ ] **Playbook selected correctly:** Documented in timeline
- [ ] **First update posted:** Within 10 minutes
- [ ] **Escalation to Tier 2:** If unresolved after 15 min

**Observation Log:**
- First response time: ____ minutes
- Severity call completed: Yes / No
- Playbook selected: [playbook-name]
- Errors encountered: [list]
- Team performance: Excellent / Good / Needs Improvement

### Phase 2: Tier 2 Response (15-30 minutes)
- [ ] **Tier 2 activated:** If unresolved after 15 min
- [ ] **Root cause identified:** Within 20 minutes
- [ ] **Resolution in progress:** Within 25 minutes
- [ ] **Customer comms prepared:** Within 30 minutes
- [ ] **Escalation to Tier 3:** If unresolved after 30 min

**Observation Log:**
- Tier 2 activated: Yes / No
- Root cause identified: Yes / No
- Resolution progress: 0% / 25% / 50% / 75% / 100%
- Customer comms prepared: Yes / No
- Errors encountered: [list]
- Team performance: Excellent / Good / Needs Improvement

### Phase 3: Tier 3 Response (30-60 minutes)
- [ ] **Tier 3 activated:** If unresolved after 30 min
- [ ] **Final plan defined:** Within 40 minutes
- [ ] **Executive notified:** Within 45 minutes
- [ ] **Customer comms executed:** Within 55 minutes
- [ ] **Resolution confirmed:** Within 60 minutes

**Observation Log:**
- Tier 3 activated: Yes / No
- Final plan defined: Yes / No
- Executive notified: Yes / No
- Customer comms executed: Yes / No
- Errors encountered: [list]
- Team performance: Excellent / Good / Needs Improvement

### Phase 4: Resolution and Post-Drill (1-2 hours)
- [ ] **Incident resolved:** Status = resolved
- [ ] **Post-mortem started:** Within 2 hours
- [ ] **Lessons learned documented:** [list]
- [ ] **Prevention plan created:** [list]
- [ ] **Team debrief scheduled:** [time]

**Observation Log:**
- Resolution time: ____ hours
- Post-mortem started: Yes / No
- Lessons learned: [list]
- Prevention plan: [list]
- Errors encountered: [list]
- Team performance: Excellent / Good / Needs Improvement

---

## Performance Metrics

### Response Time Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| First response (Tier 1) | ≤ 5 min | ____ min | ⬜ / ✅ |
| Severity call (Tier 1) | ≤ 10 min | ____ min | ⬜ / ✅ |
| Playbook selection (Tier 1) | ≤ 5 min | ____ min | ⬜ / ✅ |
| First update (Tier 1) | ≤ 15 min | ____ min | ⬜ / ✅ |
| Tier 2 escalation (if unresolved) | ≤ 15 min | ____ min | ⬜ / ✅ |
| Root cause (Tier 2) | ≤ 30 min | ____ min | ⬜ / ✅ |
| Resolution (Tier 2) | ≤ 60 min | ____ min | ⬜ / ✅ |
| Tier 3 escalation (if unresolved) | ≤ 30 min | ____ min | ⬜ / ✅ |
| Customer comms (Tier 3) | ≤ 60 min | ____ min | ⬜ / ✅ |
| Resolution (Tier 3) | ≤ 120 min | ____ min | ⬜ / ✅ |

### Quality Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Playbook selected correctly | 100% | ____% | ⬜ / ✅ |
| Timeline documentation complete | 100% | ____% | ⬜ / ✅ |
| Slack updates on time | 100% | ____% | ⬜ / ✅ |
| No major errors | 0 errors | ____ errors | ⬜ / ✅ |
| Success criteria met | 5/5 | ____/5 | ⬜ / ✅ |

### Team Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Team communication | Clear, concise | ____ | ⬜ / ✅ |
| Role clarity | Each role understood | ____ | ⬜ / ✅ |
| Escalation triggered on time | Yes | ____ | ⬜ / ✅ |
| Problem solving | Effective | ____ | ⬜ / ✅ |
| Team morale | Calm, focused | ____ | ⬜ / ✅ |

---

## Observation Log Fields

### Timing Documentation
- [ ] **Simulation start time:** ____:____
- [ ] **First response time:** ____:____ (total minutes: ____)
- [ ] **Severity call completed:** ____:____ (total minutes: ____)
- [ ] **Playbook selected:** ____:____ (total minutes: ____)
- [ ] **First update posted:** ____:____ (total minutes: ____)
- [ ] **Tier 2 escalation:** ____:____ (total minutes: ____)
- [ ] **Tier 3 escalation:** ____:____ (total minutes: ____)
- [ ] **Resolution confirmed:** ____:____ (total minutes: ____)
- [ ] **Post-mortem started:** ____:____ (total minutes: ____)

### Decision Documentation
- [ ] **Playbook decisions:** [list of playbooks selected]
- [ ] **Escalation decisions:** [list of escalations triggered]
- [ ] **Resource decisions:** [list of resources allocated]
- [ ] **Communication decisions:** [list of comms plans created]

### Error Documentation
- [ ] **Critical errors:** [list of major errors]
- [ ] **Minor errors:** [list of minor errors]
- [ ] **How errors were handled:** [how team responded]

### Performance Assessment
- [ ] **What went well:** [list of positives]
- [ ] **What needs improvement:** [list of gaps]
- [ ] **Team performance rating:** Excellent / Good / Needs Improvement
- [ ] **Overall simulation rating:** Excellent / Good / Needs Improvement

---

## Simulation Stop Criteria

### Automatic Stop (Any Tier)
- [ ] **All success criteria met:** 5/5 criteria complete
- [ ] **Resolution achieved:** Incident resolved
- [ ] **Time limit reached:** 2 hours max

### Manual Stop (Manual Intervention)
- [ ] **Critical error encountered:** Safety issue or data loss
- [ ] **Team stuck:** No progress for 30 minutes
- [ ] **Escalation loop:** Repeated escalation without resolution
- [ ] **External factor:** Production impact beyond simulation scope

---

## Post-Drill Documentation

### Immediate (Within 2 hours)
- [ ] **Observation log finalized:** All observations documented
- [ ] **Timing log finalized:** All times captured
- [ ] **Decision log finalized:** All decisions captured
- [ ] **Error log finalized:** All errors captured
- [ ] **Performance assessment drafted:** Initial rating

### Within 24 hours
- [ ] **Post-mortem written:** Full RCA, lessons learned, prevention plan
- [ ] **Team debrief held:** Share findings, improvements
- [ ] **Improvements scheduled:** Specific actions assigned

---

## Documentation Fields

- [ ] **Simulation ID:** `simulation-[YYYY-MM-DD]-[id]`
- [ ] **Simulation start time:** HH:MM
- [ ] **Simulation end time:** HH:MM
- [ ] **Simulation duration:** ____ hours
- [ ] **Simulation observer:** @username
- [ ] **Simulation notetaker:** @username
- [ ] **Overall performance rating:** Excellent / Good / Needs Improvement
- [ ] **Success criteria met:** ____/5
- [ ] **Major errors:** [count]
- [ ] **Prevention plan required:** Yes / No

---

**Usage:** Use during simulation execution to track performance, document decisions, and identify gaps. Use observation log to measure against success criteria.

**Product links:** `/l/ops-starter-kit-vol-2` | `/l/ops-starter-kit` | `/l/automation-starter-pack`