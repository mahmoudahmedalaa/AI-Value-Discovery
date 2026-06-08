# Audit Log Spec

Fields: id, tenant_id, workspace_id, user_id, action, entity_type, entity_id, metadata, ip_address if available, user_agent if available, created_at.

Required actions: login, workspace create/update policy, document upload/delete/classify, AI extraction start/complete/fail, opportunity create/update/delete, assessment create, score override, decision change, export generate/download, user invite, permission change.
