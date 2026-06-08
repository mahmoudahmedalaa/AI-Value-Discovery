# GitHub Project Governance

Repository: `mahmoudahmedalaa/AI-Value-Discovery`

Required project board: `AI Value Discovery Product Build`.

## Purpose

The board is the live product management system and must track the full build from docs to internal demo, MVP, enterprise hardening, and pilot-ready release.

## Milestones

Phase 0 — Product Governance & Repo Foundation; Phase 1 — Internal Demo / Pre-MVP; Phase 2 — MVP Product Spine; Phase 3 — AI/RAG & Document Intelligence; Phase 4 — Portfolio Cockpit & Decision Packs; Phase 5 — Enterprise Security & Deployment; Phase 6 — Pilot-Ready Release.

## Issue hierarchy

Use epic issues for workstreams, story issues for capabilities, task issues for implementation, bugs for defects. Where GitHub sub-issues are available, link stories/tasks under epics.

## Custom fields

Phase, Epic, Priority, Area, Status, Target Release, Risk, Owner, Estimate, Demo Critical.

## Statuses

Backlog, Ready, In Progress, In Review, Blocked, Done.

## Update discipline

When Mahmoud says “make sure git is updated,” Codex must run checks/tests, update docs, update issues/project board, commit with conventional commit, push remote, update `IMPLEMENTATION_STATUS.md`.

## GitHub CLI hints

Use `gh auth status`, `gh auth refresh -s project`, `gh project create --owner mahmoudahmedalaa --title "AI Value Discovery Product Build"`, and `gh issue create --repo mahmoudahmedalaa/AI-Value-Discovery ...` where available.

If project scope is blocked, create issues/milestones/labels where possible and maintain `LOCAL_PROJECT_BOARD.md` until access is fixed.
