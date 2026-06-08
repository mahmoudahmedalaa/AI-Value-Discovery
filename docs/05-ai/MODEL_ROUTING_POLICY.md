# Model Routing Policy

All model calls go through AI provider gateway.

Provider modes: mock, local, openai, azure_openai, bedrock, vertex, client_managed.

## Pre-MVP

Default provider: mock. Optional: local.

## Sensitivity routing

Public/internal demo may use mock/configured provider. Confidential uses client-approved provider. Regulated uses client-hosted/data-residency-approved provider. Restricted uses local/client-hosted model only.

## Cost controls

Cache, batch, limit document size, dry-run mode, token usage logging where supported.
