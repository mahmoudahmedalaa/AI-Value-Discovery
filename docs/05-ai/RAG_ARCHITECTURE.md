# RAG Architecture

## Components

Document loader, extractor, chunker, embedding service, Qdrant, metadata filters, retriever, reranker later, evidence citation builder.

## Chunking

800–1200 tokens with 150–200 overlap. Preserve title, section, page where available.

## Metadata

tenant_id, workspace_id, document_id, chunk_id, document_name, classification, page/section, source_type, created_at.

## Tenant isolation

Always filter by workspace_id. Prefer separate collections for enterprise deployments where appropriate.

## Deletion

Delete file, text, chunks, embeddings, and affected evidence references.
