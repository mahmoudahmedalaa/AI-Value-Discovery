# AI Value Discovery

AI Value Discovery is an enterprise AI investment decision platform for GCC organizations.

It helps leadership, transformation, data, risk, and finance teams turn scattered AI ideas, pilots, documents, workflows, and pain points into a ranked, governed, financially defensible AI opportunity portfolio.

The product is being built for Mal7's consulting and client delivery motion. It is not a chatbot, deck generator, prompt library, vendor marketplace, or generic project management tool.

## Product Purpose

Most enterprises do not need more AI ideas. They need a disciplined way to decide:

- Which opportunities deserve funding now.
- Which opportunities need data, workflow, risk, or ownership fixes first.
- Which opportunities should be deferred.
- Which opportunities should be stopped.
- What evidence, KPIs, data assets, controls, assumptions, and owners support each decision.

AI Value Discovery is designed to become the system of record for AI demand, value hypotheses, decision history, blockers, funding readiness, and portfolio status.

## First Demo Target

The first build target is a local, no-paid-services internal partner demo. It should run on a developer machine and let Mal7 walk partners through:

1. Select a sample GCC bank workspace.
2. Review an executive cockpit.
3. Inspect seeded documents and opportunities.
4. Run deterministic mock AI extraction.
5. Review draft opportunities.
6. Open an opportunity detail page.
7. Inspect business problem, workflow, KPI, value lever, data assets, systems, controls, evidence, assumptions, and missing information.
8. Review value, readiness, risk, and fundability scoring.
9. Open the portfolio cockpit.
10. See Fund Now, Fix First, Defer, Stop, and Explore Further recommendations.
11. Generate a sample executive decision-pack preview.
12. Show audit log, security posture, and data-residency posture.

## Build Principles

- Browser-based enterprise web platform.
- Local-first internal demo with no paid services.
- Mock deterministic AI provider first.
- Production-shaped architecture from the start.
- Client-hosted and data-residency-aware deployment model.
- Evidence, assumptions, confidence, and missing information must be explicit.
- Human review is required before final decision-pack generation.
- Every score and recommendation must be explainable and auditable.

## Preferred Technical Direction

The architecture documents are the source of truth. Current preferred stack:

- Next.js
- TypeScript
- Tailwind
- shadcn/ui or equivalent component system
- PostgreSQL
- Qdrant
- MinIO or local S3-compatible object storage
- Provider abstraction for mock AI first, then OpenAI, Azure OpenAI, Bedrock, Vertex, or local models later
- Docker Compose
- Unit, integration, and Playwright E2E tests

Material technical decisions should be recorded as ADRs.

## Repository Map

- `docs/00-master/` - product north star and document index
- `docs/01-product/` - product strategy, PRD, scope, personas, user stories
- `docs/02-methodology/` - scoring, value levers, KPI, data readiness, risk/control methodology
- `docs/03-ux/` - information architecture, journeys, wireframes, design system, UX copy
- `docs/04-architecture/` - system architecture, data model, APIs, deployment, stack decisions
- `docs/05-ai/` - AI system design, RAG architecture, prompts, schemas, routing, guardrails
- `docs/06-security-compliance/` - security, data residency, tenant isolation, audit, privacy
- `docs/07-engineering/` - repo structure, standards, local setup, definition of done, ADRs
- `docs/08-testing/` - test strategy, test cases, fixtures, UAT, performance requirements
- `docs/09-delivery/` - roadmap, governance, implementation status, backlog, demo script
- `docs/10-commercial/` - business model, financial model, dashboard metrics
- `project_board_seed/` - seeded milestones, labels, epics, stories, and tasks

## Delivery Governance

The live delivery tracker is the GitHub Project:

[AI Value Discovery Product Build](https://github.com/users/mahmoudahmedalaa/projects/3)

The tracker is seeded from:

- `project_board_seed/milestones.yaml`
- `project_board_seed/labels.yaml`
- `project_board_seed/epics_and_stories.yaml`
- `project_board_seed/implementation_tasks.yaml`

To re-sync GitHub governance objects:

```bash
python3 scripts/sync-github-governance.py
python3 scripts/sync-implementation-tasks.py
```

Current implementation status is maintained in:

`docs/09-delivery/IMPLEMENTATION_STATUS.md`

## Local Demo

The first browser demo app lives in `apps/web`.

```bash
npm install
npm run dev
```

Open the local URL printed by Next.js. If port `3000` is occupied, Next.js will use the next available port, such as `http://localhost:3001`.

Validation commands:

```bash
npm run lint
npm run typecheck
npm run build
```

## Current Status

Phase 0 governance is complete. The repository has product documentation, delivery governance, GitHub milestones, labels, issues, issue templates, PR template, and a populated GitHub Project board.

Phase 1 implementation has started with the local Next.js demo scaffold, app shell, seeded GCC bank workspace data, executive cockpit, opportunity detail view, route placeholders, local service compose file, and architecture ADR.
