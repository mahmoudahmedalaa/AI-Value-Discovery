#!/usr/bin/env bash
set -euo pipefail
REPO="mahmoudahmedalaa/AI-Value-Discovery"
OWNER="mahmoudahmedalaa"
PROJECT_TITLE="AI Value Discovery Product Build"

echo "Checking GitHub auth..."
gh auth status || true

echo "If project commands fail, run: gh auth refresh -s project"

echo "Create labels from project_board_seed/labels.yaml, milestones from project_board_seed/milestones.yaml, and issues from epics_and_stories.yaml."
echo "Codex should complete this script after confirming available gh/yq tooling."
# Example:
# gh project create --owner "$OWNER" --title "$PROJECT_TITLE" --format json
# gh issue create --repo "$REPO" --title "Epic: ..." --body "..." --label "type:epic"
