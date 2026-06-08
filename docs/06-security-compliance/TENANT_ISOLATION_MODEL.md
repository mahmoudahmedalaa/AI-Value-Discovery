# Tenant Isolation Model

Database rows include tenant/workspace IDs. API queries are scoped. Vector retrieval filters by tenant/workspace. Object storage uses tenant/workspace prefixes or buckets. Audit events include tenant/workspace. Tests verify cross-tenant access is blocked.

Enterprise options: separate DB, schema, Qdrant collection, object bucket, customer-managed keys.
