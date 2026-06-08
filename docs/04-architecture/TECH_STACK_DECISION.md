# Tech Stack Decision

Preferred: Next.js + TypeScript + Tailwind/shadcn, PostgreSQL, Qdrant, MinIO, mock AI provider, Docker Compose, unit tests and Playwright.

Rationale: web app supports collaboration and client-hosted deployment; PostgreSQL is system of record; Qdrant is serious self-hostable vector DB; MinIO mimics S3 locally; mock AI prevents early vendor lock-in and paid dependencies.

Codex must create ADRs if deviating.
