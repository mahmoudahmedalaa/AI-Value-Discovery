# ADR 0001: Pre-MVP Next.js Architecture

Date: 2026-06-09

Status: Accepted

## Context

The first build target is a local internal partner demo that runs without paid services while preserving production-shaped boundaries for later client-hosted deployments.

The architecture docs prefer Next.js, TypeScript, Tailwind/shadcn-style UI, PostgreSQL, Qdrant, MinIO, and a mock AI provider first. They allow a single Next.js app for pre-MVP speed if boundaries remain clean.

## Decision

Use a single Next.js App Router application under `apps/web` for the pre-MVP demo.

Keep domain seams explicit through `src/lib` data/provider modules and later extract shared packages only when the implementation needs them. Use Next.js API routes/server actions later for mock AI and local data workflows rather than calling model providers from UI code.

Use Docker Compose for local Postgres, Qdrant, and MinIO, but allow the first UI slice to run from deterministic seed data before persistent services are required.

## Alternatives Considered

- Separate FastAPI backend from day one: stronger backend separation, slower first demo setup.
- Full monorepo packages from day one: cleaner future boundaries, unnecessary overhead before product flows are visible.
- Pure static prototype: faster visually, but not production-shaped enough for provider, audit, scoring, and data-residency boundaries.

## Consequences

- Faster local demo development.
- The web app can run with no paid services and no cloud credentials.
- Backend boundaries must be reviewed as features move from seed data to persistence.
- A later ADR should revisit whether to extract API/worker packages once document ingestion, RAG, and export jobs become real.

## Follow-ups

- Add ADR for mock AI/provider abstraction.
- Add persistent database schema and migration tooling when Phase 2 begins.
- Add API route isolation tests before real client data or multi-workspace persistence.
