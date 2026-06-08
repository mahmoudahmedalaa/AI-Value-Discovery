# Requirements Traceability Matrix

| ID | Requirement | Story | Screen | API | Entity | Test |
|---|---|---|---|---|---|---|
| R-001 | Workspace creation | Workspace | Workspace setup | POST /workspaces | Workspace | TC-001 |
| R-002 | Data posture | Workspace policy | Security posture | PATCH /workspaces/:id/policy | WorkspacePolicy | TC-002 |
| R-003 | Opportunity CRUD | Opportunity | Backlog/detail | /opportunities | Opportunity | TC-003 |
| R-004 | Scoring | Scoring | Scoring panel | POST /assessments | Assessment/Score | TC-005 |
| R-005 | Document upload | Document intelligence | Intake | POST /documents | Document | TC-007 |
| R-006 | AI extraction | Document intelligence | Review queue | POST /ai/extract | DraftOpportunity | TC-008 |
| R-007 | Portfolio cockpit | Portfolio | Portfolio | GET /portfolio | Opportunity/Assessment | TC-009 |
| R-008 | Exports | Decision pack | Decision pack builder | POST /exports | Export | TC-010 |
| R-009 | Audit | Governance | Audit | GET /audit | AuditEvent | TC-011 |
