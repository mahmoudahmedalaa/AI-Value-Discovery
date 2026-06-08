# Changelog

## 2026-06-09

Started Phase 1 implementation:

- Added Next.js, TypeScript, Tailwind, and ESLint web app scaffold under `apps/web`.
- Added local app shell, workspace selector, executive cockpit, seeded GCC bank demo data, opportunity detail view, and route placeholders for intake, documents, portfolio, decision packs, audit, methodology, and security posture.
- Added local `docker-compose.yml` for PostgreSQL, Qdrant, and MinIO, plus `.env.example`.
- Added ADR `docs/07-engineering/adr-0001-pre-mvp-nextjs-architecture.md`.
- Added executive cockpit concept asset under `docs/03-ux/concepts/`.
- Verified lint, typecheck, production build, and Playwright visual checks at desktop and mobile widths.

## 2026-06-08

Created Codex build pack with product, methodology, UX, architecture, AI, security, engineering, testing, delivery, commercial docs, board seed, templates, and kickoff prompt.

Added Phase 0 governance setup:

- Synchronized GitHub labels, milestones, epic issues, and story issues from `project_board_seed`.
- Added issue templates and pull request template.
- Documented GitHub Project access blocker and local fallback board.
- Closed completed Phase 0 governance stories and left the Project-board story blocked pending GitHub Project scope.
- Replaced the build-pack README with a product-facing repository README.
- Created and populated the GitHub Project board with all seeded issues, custom fields, and Kanban statuses.
- Closed Phase 0 governance issues after board completion.
- Added detailed implementation task seed with 103 planned tasks across the roadmap.
- Synchronized the 103 implementation tasks into GitHub as Project items and sub-issues under parent stories.
