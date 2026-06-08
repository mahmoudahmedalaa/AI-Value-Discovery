#!/usr/bin/env python3
"""Synchronize Phase 0 GitHub governance objects from project_board_seed."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REPO = "mahmoudahmedalaa/AI-Value-Discovery"
OWNER = "mahmoudahmedalaa"
PROJECT_TITLE = "AI Value Discovery Product Build"
PROJECT_UNBLOCK = "gh auth refresh -s project"

PHASE_LABEL_TO_MILESTONE = {
    "phase:0-governance": "Phase 0 — Product Governance & Repo Foundation",
    "phase:1-demo": "Phase 1 — Internal Demo / Pre-MVP",
    "phase:2-mvp": "Phase 2 — MVP Product Spine",
    "phase:3-ai-rag": "Phase 3 — AI/RAG & Document Intelligence",
    "phase:4-portfolio": "Phase 4 — Portfolio Cockpit & Decision Packs",
    "phase:5-enterprise": "Phase 5 — Enterprise Security & Deployment",
    "phase:6-release": "Phase 6 — Pilot-Ready Release",
}


def run(args: list[str], *, check: bool = True, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    attempts = 3 if check else 1
    result: subprocess.CompletedProcess[str] | None = None
    for attempt in range(attempts):
        result = subprocess.run(
            args,
            cwd=ROOT,
            text=True,
            input=input_text,
            capture_output=True,
            check=False,
        )
        if result.returncode == 0 or not check:
            return result
        if attempt < attempts - 1:
            time.sleep(1.5 * (attempt + 1))
    assert result is not None
    raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)


def gh_json(args: list[str]) -> object:
    result = run(args)
    return json.loads(result.stdout or "null")


def load_yaml(name: str) -> object:
    with (ROOT / "project_board_seed" / name).open() as handle:
        return yaml.safe_load(handle)


def sync_labels(labels: list[dict[str, str]]) -> list[str]:
    touched: list[str] = []
    for label in labels:
        run(
            [
                "gh",
                "label",
                "create",
                label["name"],
                "--repo",
                REPO,
                "--color",
                str(label["color"]).strip("'"),
                "--description",
                label.get("description", ""),
                "--force",
            ]
        )
        touched.append(label["name"])
    return touched


def sync_milestones(milestones: list[dict[str, str]]) -> list[str]:
    existing = gh_json(["gh", "api", "--method", "GET", f"repos/{REPO}/milestones", "-f", "state=all"])
    existing_titles = {item["title"] for item in existing}
    touched: list[str] = []
    for milestone in milestones:
        if milestone["title"] in existing_titles:
            touched.append(milestone["title"])
            continue
        run(
            [
                "gh",
                "api",
                f"repos/{REPO}/milestones",
                "-f",
                f"title={milestone['title']}",
                "-f",
                f"description={milestone.get('description', '')}",
            ]
        )
        touched.append(milestone["title"])
    return touched


def milestone_for_labels(labels: list[str], fallback: str | None = None) -> str:
    for label in labels:
        if label in PHASE_LABEL_TO_MILESTONE:
            return PHASE_LABEL_TO_MILESTONE[label]
    return fallback or PHASE_LABEL_TO_MILESTONE["phase:0-governance"]


def current_issues() -> dict[str, dict[str, object]]:
    issues = gh_json(
        [
            "gh",
            "issue",
            "list",
            "--repo",
            REPO,
            "--state",
            "all",
            "--limit",
            "500",
            "--json",
            "number,title,url",
        ]
    )
    return {issue["title"]: issue for issue in issues}


def issue_body(item_id: str, title: str, summary: str, labels: list[str], acceptance: list[str] | None = None) -> str:
    lines = [
        f"Seed ID: `{item_id}`",
        "",
        "## Summary",
        summary,
        "",
        "## Labels",
    ]
    lines.extend(f"- `{label}`" for label in labels)
    if acceptance:
        lines.extend(["", "## Acceptance Criteria"])
        lines.extend(f"- [ ] {criterion}" for criterion in acceptance)
    lines.extend(
        [
            "",
            "## Governance",
            "- [ ] Added to GitHub Project board once project scope is available",
            "- [ ] Status reflected in `docs/09-delivery/IMPLEMENTATION_STATUS.md` when active",
        ]
    )
    return "\n".join(lines) + "\n"


def create_or_get_issue(
    *,
    title: str,
    body: str,
    labels: list[str],
    milestone: str,
    existing: dict[str, dict[str, object]],
) -> dict[str, object]:
    if title in existing:
        issue = existing[title]
        run(["gh", "issue", "edit", str(issue["number"]), "--repo", REPO, "--add-label", ",".join(labels), "--milestone", milestone])
        return issue

    args = [
        "gh",
        "issue",
        "create",
        "--repo",
        REPO,
        "--title",
        title,
        "--body",
        body,
        "--milestone",
        milestone,
    ]
    if labels:
        args.extend(["--label", ",".join(labels)])
    result = run(args)
    url = result.stdout.strip().splitlines()[-1]
    number = int(url.rstrip("/").split("/")[-1])
    issue = {"number": number, "title": title, "url": url}
    existing[title] = issue
    return issue


def sync_issues(seed: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    existing = current_issues()
    epics: list[dict[str, object]] = []
    stories: list[dict[str, object]] = []

    for epic in seed:
        epic_labels = list(epic["labels"])
        epic_title = f"[{epic['id']}] {epic['title']}"
        epic_issue = create_or_get_issue(
            title=epic_title,
            body=issue_body(str(epic["id"]), str(epic["title"]), str(epic["summary"]), epic_labels),
            labels=epic_labels,
            milestone=str(epic["phase"]),
            existing=existing,
        )
        epic_issue["seed_id"] = epic["id"]
        epic_issue["stories"] = []
        epics.append(epic_issue)

        for story in epic.get("stories", []):
            story_labels = list(story["labels"])
            story_title = f"[{story['id']}] {story['title']}"
            story_issue = create_or_get_issue(
                title=story_title,
                body=issue_body(
                    str(story["id"]),
                    str(story["title"]),
                    f"Story under {epic['id']}: {epic['title']}",
                    story_labels,
                    list(story.get("acceptance_criteria", [])),
                ),
                labels=story_labels,
                milestone=milestone_for_labels(story_labels, str(epic["phase"])),
                existing=existing,
            )
            story_issue["seed_id"] = story["id"]
            story_issue["epic_id"] = epic["id"]
            stories.append(story_issue)
            epic_issue["stories"].append(story_issue)

    for epic_issue in epics:
        story_lines = [f"- [ ] #{story['number']} `{story['seed_id']}` {story['title']}" for story in epic_issue["stories"]]
        body = "\n".join(
            [
                f"Seed ID: `{epic_issue['seed_id']}`",
                "",
                "## Tracked Stories",
                *story_lines,
                "",
                "## Governance",
                "- [ ] Add this epic and child stories to the GitHub Project board once project scope is available",
                "- [ ] Keep status synchronized with `docs/09-delivery/IMPLEMENTATION_STATUS.md`",
            ]
        )
        with tempfile.NamedTemporaryFile("w", delete=False) as handle:
            handle.write(body + "\n")
            body_path = handle.name
        run(["gh", "issue", "edit", str(epic_issue["number"]), "--repo", REPO, "--body-file", body_path])

    return epics, stories


def project_status() -> tuple[bool, str]:
    result = run(["gh", "project", "list", "--owner", OWNER, "--format", "json", "--limit", "50"], check=False)
    if result.returncode != 0:
        return False, (result.stderr or result.stdout).strip()

    projects = json.loads(result.stdout or "{}").get("projects", [])
    for project in projects:
        if project.get("title") == PROJECT_TITLE:
            return True, f"Project exists: {project.get('url', PROJECT_TITLE)}"

    result = run(["gh", "project", "create", "--owner", OWNER, "--title", PROJECT_TITLE, "--format", "json"], check=False)
    if result.returncode != 0:
        return False, (result.stderr or result.stdout).strip()
    created = json.loads(result.stdout or "{}")
    return True, f"Project created: {created.get('url', PROJECT_TITLE)}"


def write_status_docs(
    *,
    labels: list[str],
    milestones: list[str],
    epics: list[dict[str, object]],
    stories: list[dict[str, object]],
    project_ok: bool,
    project_message: str,
) -> None:
    today = date.today().isoformat()
    board_lines = [
        "# Local Project Board",
        "",
        "GitHub Project creation is currently blocked by missing project scope, so this file mirrors the seeded backlog until the board can be created.",
        "",
        "## GitHub Project Blocker",
        "",
        f"- Required board: `{PROJECT_TITLE}`",
        f"- Current blocker: `{project_message}`",
        f"- Unblock command: `{PROJECT_UNBLOCK}`",
        "",
        "After refreshing auth, rerun:",
        "",
        "```bash",
        "python3 scripts/sync-github-governance.py",
        "```",
        "",
        "## Columns",
        "",
        "Backlog, Ready, In Progress, In Review, Blocked, Done.",
        "",
        "## Backlog",
        "",
    ]
    for epic in epics:
        board_lines.append(f"### #{epic['number']} {epic['title']}")
        for story in epic["stories"]:
            board_lines.append(f"- Backlog: #{story['number']} {story['title']}")
        board_lines.append("")

    status_lines = [
        "# Implementation Status",
        "",
        f"Last updated: {today}",
        "",
        "## Current phase",
        "",
        "Phase 0 — Product Governance & Repo Foundation",
        "",
        "## Current status",
        "",
        f"- GitHub labels synchronized: {len(labels)}.",
        f"- GitHub milestones synchronized: {len(milestones)}.",
        f"- GitHub epic issues synchronized: {len(epics)}.",
        f"- GitHub story issues synchronized: {len(stories)}.",
        "- Issue templates and PR template added under `.github/`.",
        "",
        "## GitHub Project board",
        "",
    ]
    if project_ok:
        status_lines.append(f"- Board status: {project_message}")
    else:
        status_lines.extend(
            [
                "- Board status: Blocked by missing GitHub Project scope.",
                f"- Current error: `{project_message}`",
                f"- Required action: run `{PROJECT_UNBLOCK}` and then rerun `python3 scripts/sync-github-governance.py`.",
                "- Fallback: `docs/09-delivery/LOCAL_PROJECT_BOARD.md` mirrors the seeded backlog until Projects access is available.",
            ]
        )

    status_lines.extend(
        [
            "",
            "## Next action for Codex",
            "",
            "Commit and push the Phase 0 governance setup. After project scope is refreshed, create/update the GitHub Project board and add the existing issues to it. Then begin Phase 1 with the local demo foundation slice.",
            "",
            "## Blockers",
            "",
        ]
    )
    if project_ok:
        status_lines.append("None for governance setup.")
    else:
        status_lines.append(f"GitHub Project access requires `{PROJECT_UNBLOCK}`.")

    (ROOT / "docs/09-delivery/LOCAL_PROJECT_BOARD.md").write_text("\n".join(board_lines).rstrip() + "\n")
    (ROOT / "docs/09-delivery/IMPLEMENTATION_STATUS.md").write_text("\n".join(status_lines).rstrip() + "\n")


def main() -> int:
    labels = sync_labels(load_yaml("labels.yaml"))
    milestones = sync_milestones(load_yaml("milestones.yaml"))
    project_ok, project_message = project_status()
    epics, stories = sync_issues(load_yaml("epics_and_stories.yaml"))
    write_status_docs(
        labels=labels,
        milestones=milestones,
        epics=epics,
        stories=stories,
        project_ok=project_ok,
        project_message=project_message,
    )
    print(f"labels={len(labels)} milestones={len(milestones)} epics={len(epics)} stories={len(stories)} project_ok={project_ok}")
    if not project_ok:
        print(f"project_blocker={project_message}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
