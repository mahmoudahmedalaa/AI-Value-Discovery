# Local Project Board

GitHub Project creation is currently blocked by missing project scope, so this file mirrors the seeded backlog until the board can be created.

## GitHub Project Blocker

- Required board: `AI Value Discovery Product Build`
- Current blocker: `error: your authentication token is missing required scopes [read:project]
To request it, run:  gh auth refresh -s read:project`
- Unblock command: `gh auth refresh -s project`

After refreshing auth, rerun:

```bash
python3 scripts/sync-github-governance.py
```

## Columns

Backlog, Ready, In Progress, In Review, Blocked, Done.

## Planned GitHub Project Fields

Phase, Epic, Priority, Area, Status, Target Release, Risk, Owner, Estimate, Demo Critical.

## Backlog

### #1 [E0] Epic: Product governance and tracking foundation
- Backlog: #2 [E0-S01] Create GitHub Project board and custom fields
- Backlog: #3 [E0-S02] Create repository issue templates
- Backlog: #4 [E0-S03] Create implementation status process
- Backlog: #5 [E0-S04] Establish branch, commit, and PR standards

### #6 [E1] Epic: Local demo environment
- Backlog: #7 [E1-S01] Set up local app scaffold
- Backlog: #8 [E1-S02] Set up local data services
- Backlog: #9 [E1-S03] Create demo seed data
- Backlog: #10 [E1-S04] Create mock AI provider

### #11 [E2] Epic: Enterprise design system and application shell
- Backlog: #12 [E2-S01] Implement app shell and navigation
- Backlog: #13 [E2-S02] Implement design tokens and core components
- Backlog: #14 [E2-S03] Create executive cockpit page

### #15 [E3] Epic: Opportunity management
- Backlog: #16 [E3-S01] Build opportunity backlog table
- Backlog: #17 [E3-S02] Build manual opportunity creation/editing
- Backlog: #18 [E3-S03] Build opportunity detail page
- Backlog: #19 [E3-S04] Implement evidence/assumption labels

### #20 [E4] Epic: Scoring and decision engine
- Backlog: #21 [E4-S01] Implement scoring model
- Backlog: #22 [E4-S02] Implement decision logic
- Backlog: #23 [E4-S03] Build score explanation UI

### #24 [E5] Epic: Portfolio cockpit
- Backlog: #25 [E5-S01] Build decision lanes
- Backlog: #26 [E5-S02] Build value-readiness matrix
- Backlog: #27 [E5-S03] Build risk/readiness blocker panels

### #28 [E6] Epic: Document intelligence and AI extraction
- Backlog: #29 [E6-S01] Build document library
- Backlog: #30 [E6-S02] Build document upload pipeline
- Backlog: #31 [E6-S03] Integrate Qdrant indexing
- Backlog: #32 [E6-S04] Implement structured AI extraction

### #33 [E7] Epic: Decision packs and exports
- Backlog: #34 [E7-S01] Build decision-pack preview
- Backlog: #35 [E7-S02] Implement Excel export
- Backlog: #36 [E7-S03] Implement PDF export
- Backlog: #37 [E7-S04] Implement PPTX export

### #38 [E8] Epic: Security, data residency, and audit
- Backlog: #39 [E8-S01] Build security posture page
- Backlog: #40 [E8-S02] Implement audit log
- Backlog: #41 [E8-S03] Implement RBAC foundation
- Backlog: #42 [E8-S04] Implement tenant isolation tests

### #43 [E9] Epic: Testing and quality
- Backlog: #44 [E9-S01] Add scoring unit tests
- Backlog: #45 [E9-S02] Add demo E2E test
- Backlog: #46 [E9-S03] Add lint/typecheck scripts
