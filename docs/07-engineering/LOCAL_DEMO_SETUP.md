# Local Demo Setup

Goal: run a credible internal demo on Mahmoud's machine with no paid services.

Demo story: start app, login/select demo user, open GCC bank workspace, show cockpit, run mock extraction, review opportunities, open detail, show evidence/assumptions/missing info, score, portfolio, decision pack, security posture, audit.

Data: synthetic only.

## Current Local App

The browser demo lives in `apps/web` and uses deterministic seeded data. It does not require OpenAI, AWS, Azure, Auth0, or any paid service.

```bash
npm install
npm run dev
```

Open the URL printed by Next.js. On this machine, port `3000` may already be occupied, so the app can run at `http://localhost:3001`.

## Checks

```bash
npm run lint
npm run typecheck
npm run build
```

## Optional Local Services

The first UI slice runs without services. The repo includes `docker-compose.yml` for the intended local service spine:

- PostgreSQL for relational application data.
- Qdrant for vector search.
- MinIO for S3-compatible local object storage.

Start those services only when implementing the persistence/document-ingestion slices:

```bash
docker compose up -d
```
