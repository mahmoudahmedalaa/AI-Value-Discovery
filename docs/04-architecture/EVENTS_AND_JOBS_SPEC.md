# Events and Jobs Spec

## Jobs

document.ingest: validate, store, extract text, chunk, embed, mark complete/failed.

ai.extract_opportunities: retrieve chunks, run prompt, validate schema, create draft opportunities, link evidence.

scoring.generate: load opportunity, calculate scores, save assessment.

export.decision_pack: validate review gate, load portfolio, generate file, store export, audit.

## Statuses

queued, running, completed, failed, cancelled.
