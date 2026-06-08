# AI Value Discovery — Codex Build Pack

Prepared for: Mahmoud Alaaeldin / Mal7  
Repository: `https://github.com/mahmoudahmedalaa/AI-Value-Discovery`  
Date: 2026-06-08

This pack is designed to be unzipped into the repository root and used as the source of truth for Codex or any engineering agent building the AI Value Discovery Platform.

## Product thesis

AI Value Discovery is not a generic AI strategy chatbot. It is an enterprise AI investment decision platform.

It helps leadership teams turn scattered AI demand into a ranked, governed, financially defensible portfolio of AI opportunities by answering:

- Which opportunities deserve funding now?
- Which opportunities need data, workflow, risk, or ownership fixes first?
- Which opportunities should be deferred?
- Which should be stopped?
- What evidence, KPIs, data assets, controls, and owners support each decision?

## Build mode

Start with a **local, no-paid-services internal demo** that runs on Mahmoud's machine, but keep the architecture production-shaped:

- Browser-based web app
- Local Docker services
- Local Postgres
- Local Qdrant
- Local MinIO/S3-compatible object storage
- Mock / deterministic AI provider first
- Optional local Ollama provider if available
- Model-provider abstraction for later OpenAI / Azure OpenAI / Bedrock / Vertex / local models
- Client-hosted deployment architecture from day one

## How to use this pack

1. Unzip into the repository root.
2. Give Codex the prompt in `CODEX_KICKOFF_PROMPT.md`.
3. Instruct Codex to read `docs/00-master/MASTER_BUILD_BRIEF.md` first.
4. Codex must create/update the GitHub Project board using `docs/09-delivery/GITHUB_PROJECT_GOVERNANCE.md` and `project_board_seed/epics_and_stories.yaml`.
5. Codex must keep code, docs, commits, PRs, and board status aligned.

## Non-negotiables

- No generic AI slop UI.
- No neon gradients, fake glow, gimmicky chips, or toy chatbot UX.
- No unsupported AI claims.
- Every AI output must distinguish evidence, assumption, inference, confidence, and missing information.
- Human review is required before decision-pack generation.
- Data residency and client-hosted deployment must be treated as core product requirements, not later afterthoughts.
