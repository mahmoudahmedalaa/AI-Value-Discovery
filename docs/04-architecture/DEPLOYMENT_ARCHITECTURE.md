# Deployment Architecture

## Modes

1. Local Demo: Docker Compose, local Postgres/Qdrant/MinIO, mock AI, seed data.
2. Mal7 Demo Cloud: synthetic/public data only.
3. Mal7 Managed Single Tenant: dedicated tenant in approved region.
4. Client Cloud/VPC: deployed inside client cloud with client-managed IAM/storage/network/model endpoints where required.
5. Restricted/Air-gapped: no external calls, local/client model only.

## Infrastructure path

Pre-MVP: Docker Compose. Enterprise: Kubernetes/Helm, Terraform, secrets management, backup/restore, observability.
