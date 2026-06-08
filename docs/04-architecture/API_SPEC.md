# API Spec

## Workspaces

GET /api/workspaces, POST /api/workspaces, GET/PATCH /api/workspaces/:id.

## Opportunities

GET/POST /api/workspaces/:workspaceId/opportunities, GET/PATCH/DELETE /api/opportunities/:id.

## Assessments

POST /api/opportunities/:id/assessments, GET /api/opportunities/:id/assessments/latest, POST /api/scores/:id/override.

## Portfolio

GET /api/workspaces/:workspaceId/portfolio.

## Documents

POST /api/workspaces/:workspaceId/documents, GET /api/workspaces/:workspaceId/documents, GET/DELETE /api/documents/:id.

## AI

POST /api/documents/:id/extract-opportunities, GET /api/jobs/:id, POST /api/draft-opportunities/:id/approve.

## Exports

POST /api/workspaces/:workspaceId/exports/decision-pack, GET /api/exports/:id.

## Audit

GET /api/workspaces/:workspaceId/audit.
