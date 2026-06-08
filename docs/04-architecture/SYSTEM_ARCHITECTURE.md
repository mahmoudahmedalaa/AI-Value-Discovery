# System Architecture

## Components

Web app, API/backend, PostgreSQL, Qdrant, object storage, AI provider gateway, worker/job service, export service, audit/logging, deployment/config layer.

## Preferred stack

Frontend: Next.js, TypeScript, Tailwind, shadcn/ui. Backend: Next.js API routes for speed or FastAPI for AI-heavy architecture. DB: PostgreSQL. Vector: Qdrant. Storage: MinIO locally, S3-compatible abstraction. AI: provider abstraction with mock first.

## Data flow

Upload document -> save metadata -> store file -> extract text -> chunk -> embed -> save vectors -> extract opportunities -> save drafts -> human review -> scoring -> portfolio -> exports.

## Pre-MVP simplification

Seed docs/opportunities, mock AI, simulate retrieval, but keep interfaces production-shaped.

## Hard rule

No direct UI calls to LLM providers. All AI calls go through backend provider gateway.
