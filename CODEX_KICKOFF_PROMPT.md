# Codex Kickoff Prompt — AI Value Discovery Platform

You are the engineering lead and product execution agent for the repository:

`https://github.com/mahmoudahmedalaa/AI-Value-Discovery`

You are not here to brainstorm. The strategic thinking has already been captured in the documentation pack. Your job is to convert the documents into a functioning product, track the work properly in GitHub, and maintain implementation discipline.

## Mandatory first actions

Before writing application code:

1. Read `README.md`.
2. Read `docs/00-master/MASTER_BUILD_BRIEF.md`.
3. Read `docs/00-master/DOCUMENT_INDEX.md`.
4. Read `docs/09-delivery/GITHUB_PROJECT_GOVERNANCE.md`.
5. Read `docs/09-delivery/ROADMAP.md`.
6. Read `project_board_seed/epics_and_stories.yaml`.
7. Inspect the current repository structure.
8. Create or update a GitHub Project board for the repo called: `AI Value Discovery Product Build`.
9. Populate the board with epics, stories, and tasks based on `project_board_seed/epics_and_stories.yaml`.
10. Create milestones for the roadmap phases:
    - Phase 0 — Product Governance & Repo Foundation
    - Phase 1 — Internal Demo / Pre-MVP
    - Phase 2 — MVP Product Spine
    - Phase 3 — AI/RAG & Document Intelligence
    - Phase 4 — Portfolio Cockpit & Decision Packs
    - Phase 5 — Enterprise Security & Deployment
    - Phase 6 — Pilot-Ready Release
11. Create labels using the taxonomy in `docs/09-delivery/GITHUB_PROJECT_GOVERNANCE.md`.
12. Update `docs/09-delivery/IMPLEMENTATION_STATUS.md` with the exact project status and the next task.
13. Commit and push the governance setup before starting feature work.

If GitHub Project board creation is blocked by missing auth scopes, do not silently skip it. Create a local fallback board in `docs/09-delivery/LOCAL_PROJECT_BOARD.md`, create GitHub issues where possible, and write the exact blocker and command needed, for example `gh auth refresh -s project`.

## Product goal

Build a browser-based enterprise web platform called **AI Value Discovery**.

The platform helps GCC enterprise clients, especially regulated institutions, turn messy AI demand into a ranked, governed, financially defensible AI investment portfolio.

This is not a general chatbot. This is an AI investment decision cockpit.

The product must support:

- Workspace setup
- Data-residency/deployment-mode selection
- Opportunity intake
- Manual opportunity creation
- Document upload
- Document intelligence
- AI opportunity extraction
- KPI, value, data, and control mapping
- Value/readiness/risk scoring
- Portfolio prioritization
- Decision recommendations
- Human review
- Decision-pack exports
- Audit trail
- Local internal demo mode with no paid services
- Production-shaped architecture for later client-hosted deployments

## Critical build philosophy

Build a **demo-first but production-shaped** product.

For the internal demo phase, the product must run locally without paid subscriptions:

- Use Docker Compose.
- Use local Postgres.
- Use local Qdrant.
- Use local MinIO or filesystem-backed object storage.
- Use a mock/deterministic AI provider by default.
- Optionally support Ollama if available.
- Do not require AWS, OpenAI, Azure, Auth0, or paid services to run the first demo.
- Do not hardcode any future vendor dependency.

However, the codebase must be structured so later production deployment can support:

- Mal7-hosted demo cloud
- Mal7 managed single-tenant deployment
- Client cloud/VPC deployment
- Restricted/air-gapped deployment
- External LLMs or local LLMs depending on data policy

## Design direction

The UI must look like an enterprise investment cockpit, not an AI toy.

Strictly avoid:

- Neon gradients
- Fake glowing cards
- Excessive pills/chips
- Random emojis
- Generic SaaS hero design
- Chatbot-first interface
- Vague AI language
- “Unlock/supercharge/magic” copy
- Overcrowded dashboards without hierarchy

Use:

- Calm, premium, serious visual language
- High-quality typography
- Strong grid and spacing
- Data-dense but readable tables
- Executive dashboards
- Clear status and decision states
- Tooltips for methodology-heavy fields
- Evidence citations next to AI-derived claims
- Conservative charts
- Clear empty states and loading states
- Useful explanations where users may not know methodology terms

Read `docs/03-ux/DESIGN_SYSTEM.md`, `docs/03-ux/UX_COPY_GUIDE.md`, and `docs/03-ux/WIREFRAME_SPEC.md` before building screens.

## Technical direction

Use the architecture in `docs/04-architecture/SYSTEM_ARCHITECTURE.md`.

Preferred stack unless the existing repo strongly requires otherwise:

- Frontend: Next.js, TypeScript, Tailwind, shadcn/ui
- Backend: FastAPI or Next.js API routes for pre-MVP; if choosing one, justify in an ADR
- Database: PostgreSQL
- Vector DB: Qdrant
- Object storage: MinIO locally, S3-compatible abstraction
- AI orchestration: provider abstraction first; LangGraph/custom workflows later
- Auth: local demo auth first; SSO-ready abstraction later
- Exports: server-side export service for Excel/PDF/PPTX
- Testing: unit, integration, and Playwright E2E
- Tooling: Docker Compose, linting, type checking, formatting, seed data

Use ADRs for important technical decisions.

## First demo target

The first internal demo must allow Mahmoud to walk partners through this story end to end:

1. Open local web app.
2. Select a sample GCC bank workspace.
3. See a serious executive cockpit.
4. Upload or select preloaded sample documents.
5. Run mock AI extraction.
6. Review extracted AI opportunities.
7. Open one opportunity and inspect:
   - business problem
   - workflow
   - KPI
   - value lever
   - data assets
   - systems
   - controls
   - evidence
   - assumptions
   - missing information
8. See value/readiness/risk/fundability scores.
9. Open portfolio cockpit.
10. See Fund Now / Fix First / Defer / Stop recommendations.
11. Generate a sample executive decision pack.
12. Show audit trail and data-residency posture.

This demo must feel like a real product even if the AI provider is mocked.

## Git and project governance

Every meaningful work unit must be tracked.

When Mahmoud says “make sure git is updated,” it means:

1. Code is formatted.
2. Tests/checks are run.
3. Relevant docs are updated.
4. GitHub issues/project board statuses are updated.
5. A clear commit is created.
6. Work is pushed to the remote branch.
7. `docs/09-delivery/IMPLEMENTATION_STATUS.md` is updated.
8. If there is a PR, the PR description links issues and summarizes evidence of completion.

Use branches:

- `main` for stable
- `develop` for integrated active work if useful
- `feature/<short-name>`
- `fix/<short-name>`
- `docs/<short-name>`
- `chore/<short-name>`

Use conventional commits:

- `feat:`
- `fix:`
- `docs:`
- `test:`
- `refactor:`
- `chore:`
- `ci:`

Do not make huge unreviewable commits. If a task is large, break it into sub-issues and commits.

## Implementation sequence

Follow this sequence unless there is a strong reason to change it. If you change it, update the roadmap and write an ADR.

1. Repo foundation and governance
2. Local demo environment
3. Design system and application shell
4. Workspace, tenant, and user stubs
5. Opportunity data model
6. Manual opportunity management
7. Scoring engine
8. Portfolio cockpit
9. Mock document intelligence pipeline
10. Mock AI opportunity extraction
11. Evidence and assumptions model
12. Decision-pack export
13. Audit log
14. Demo seed data
15. Demo script
16. Security and data-residency posture screen
17. Tests and hardening

## Required documentation updates during build

When implementing a feature, keep these files current:

- `docs/09-delivery/IMPLEMENTATION_STATUS.md`
- `docs/09-delivery/CHANGELOG.md`
- relevant PRD/user story docs
- relevant architecture docs if design changes
- relevant ADR if a material decision is made
- relevant test docs if coverage changes

## Quality bar

A task is not done unless:

- It works locally.
- It is visually consistent.
- It handles loading, empty, and error states.
- It validates inputs.
- It respects tenant/workspace boundaries.
- It does not leak sample data across workspaces.
- It has basic tests or a documented reason for temporary omission.
- It updates the project board.
- It updates implementation status.
- It is committed and pushed.

## Your first response to Mahmoud after reading this pack

Report:

1. What documents you read.
2. Current repo state.
3. Whether GitHub auth/project creation is available.
4. The board/milestone/label plan.
5. The first implementation slice you will execute.
6. Any blockers that require Mahmoud action.

Do not ask strategic questions already answered in the docs. Make reasonable engineering decisions and document them.
