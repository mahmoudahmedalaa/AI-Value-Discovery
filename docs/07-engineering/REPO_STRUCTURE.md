# Repo Structure

Recommended monorepo:

```text
/apps/web
/apps/api
/apps/worker
/packages/ui
/packages/types
/packages/db
/packages/ai
/packages/config
/packages/export
/infra
/docs
/project_board_seed
/scripts
```

For speed, a single Next.js app is acceptable for pre-MVP if boundaries are clean and the decision is captured in an ADR.
