# Data Model

Core entities: Tenant, Workspace, User, Role, Document, DocumentChunk, EmbeddingReference, Opportunity, Workflow, KPI, ValueLever, DataAsset, System, Control, Evidence, Assumption, Assessment, Score, Decision, Export, AuditEvent.

Every workspace-scoped entity must include workspace_id. Every tenant-scoped entity must include tenant_id. Vector entries and object storage paths must also include tenant/workspace metadata.
