# Database Schema

## Principles

UUID primary keys, tenant/workspace IDs, enums for states, timestamps, soft delete where appropriate, append-only audit events.

## Enums

deployment_mode: demo, managed_single_tenant, client_hosted, restricted.

decision_state: fund_now, fix_first, defer, stop, explore_further, unreviewed.

document_classification: public, internal, confidential, regulated, restricted.

processing_status: pending, processing, completed, failed.

score_dimension: strategic_alignment, value_potential, evidence_strength, data_readiness, workflow_readiness, technical_feasibility, control_score, adoption_complexity, sponsor_strength, time_to_impact, reusability.

## Indexes

workspace_id, tenant_id, document_id, opportunity_id, decision_state, created_at on audit.
