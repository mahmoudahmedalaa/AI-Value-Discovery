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
PROJECT_DESCRIPTION = "Delivery board for the AI Value Discovery enterprise platform build."
PROJECT_README = """# AI Value Discovery Product Build

This Project tracks the product build from governance through internal demo, MVP, AI/RAG, portfolio decision packs, enterprise hardening, and pilot readiness.

Board lanes: Backlog, Ready, In Progress, In Review, Blocked, Done.

Source of truth:
- Repository: https://github.com/mahmoudahmedalaa/AI-Value-Discovery
- Roadmap: docs/09-delivery/ROADMAP.md
- Governance: docs/09-delivery/GITHUB_PROJECT_GOVERNANCE.md
- Live status: docs/09-delivery/IMPLEMENTATION_STATUS.md
"""

PHASE_LABEL_TO_MILESTONE = {
    "phase:0-governance": "Phase 0 — Product Governance & Repo Foundation",
    "phase:1-demo": "Phase 1 — Internal Demo / Pre-MVP",
    "phase:2-mvp": "Phase 2 — MVP Product Spine",
    "phase:3-ai-rag": "Phase 3 — AI/RAG & Document Intelligence",
    "phase:4-portfolio": "Phase 4 — Portfolio Cockpit & Decision Packs",
    "phase:5-enterprise": "Phase 5 — Enterprise Security & Deployment",
    "phase:6-release": "Phase 6 — Pilot-Ready Release",
}

PHASE_OPTIONS = list(PHASE_LABEL_TO_MILESTONE.values())
STATUS_OPTIONS = [
    ("Backlog", "GRAY", "Seeded but not ready for active work."),
    ("Ready", "BLUE", "Ready to start."),
    ("In Progress", "YELLOW", "Actively being worked."),
    ("In Review", "PURPLE", "Awaiting review or verification."),
    ("Blocked", "RED", "Blocked by an external dependency."),
    ("Done", "GREEN", "Completed and verified."),
]
PROJECT_FIELD_DEFINITIONS = {
    "Phase": ("SINGLE_SELECT", PHASE_OPTIONS),
    "Epic": ("TEXT", None),
    "Priority": ("SINGLE_SELECT", ["P0", "P1", "P2"]),
    "Area": ("TEXT", None),
    "Target Release": ("SINGLE_SELECT", ["Internal Demo", "MVP", "AI/RAG", "Portfolio", "Enterprise", "Pilot-Ready"]),
    "Risk": ("SINGLE_SELECT", ["Normal", "Watch", "High", "Blocked"]),
    "Owner": ("TEXT", None),
    "Estimate": ("NUMBER", None),
    "Demo Critical": ("SINGLE_SELECT", ["Yes", "No"]),
}


def run(args: list[str], *, check: bool = True, input_text: str | None = None, timeout: int = 45) -> subprocess.CompletedProcess[str]:
    attempts = 3 if check else 1
    result: subprocess.CompletedProcess[str] | None = None
    for attempt in range(attempts):
        try:
            result = subprocess.run(
                args,
                cwd=ROOT,
                text=True,
                input=input_text,
                capture_output=True,
                check=False,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exc:
            result = subprocess.CompletedProcess(args, 124, output=exc.stdout or "", stderr=exc.stderr or "Command timed out")
        if result.returncode == 0 or not check:
            return result
        if attempt < attempts - 1:
            time.sleep(1.5 * (attempt + 1))
    assert result is not None
    raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)


def gh_json(args: list[str]) -> object:
    result = run(args)
    return json.loads(result.stdout or "null")


def graphql(query: str, variables: dict[str, object]) -> object:
    payload = {"query": query, "variables": variables}
    with tempfile.NamedTemporaryFile("w", delete=False) as handle:
        json.dump(payload, handle)
        input_path = handle.name
    result = run(["gh", "api", "graphql", "--input", input_path])
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


def find_project() -> dict[str, object] | None:
    result = run(["gh", "project", "list", "--owner", OWNER, "--format", "json", "--limit", "50"], check=False)
    if result.returncode != 0:
        return None

    projects = json.loads(result.stdout or "{}").get("projects", [])
    for project in projects:
        if project.get("title") == PROJECT_TITLE:
            return project
    return None


def project_status() -> tuple[bool, str]:
    result = run(["gh", "project", "list", "--owner", OWNER, "--format", "json", "--limit", "50"], check=False)
    if result.returncode != 0:
        return False, (result.stderr or result.stdout).strip()

    project = find_project()
    if project:
        return True, f"Project exists: {project.get('url', PROJECT_TITLE)}"

    result = run(["gh", "project", "create", "--owner", OWNER, "--title", PROJECT_TITLE, "--format", "json"], check=False)
    if result.returncode != 0:
        return False, (result.stderr or result.stdout).strip()
    created = json.loads(result.stdout or "{}")
    return True, f"Project created: {created.get('url', PROJECT_TITLE)}"


def project_fields(project_number: int) -> dict[str, dict[str, object]]:
    data = gh_json(["gh", "project", "field-list", str(project_number), "--owner", OWNER, "--format", "json", "--limit", "100"])
    return {field["name"]: field for field in data.get("fields", [])}


def update_status_options(status_field_id: str) -> None:
    query = """
    mutation($fieldId: ID!, $options: [ProjectV2SingleSelectFieldOptionInput!]) {
      updateProjectV2Field(input: {fieldId: $fieldId, singleSelectOptions: $options}) {
        projectV2Field {
          ... on ProjectV2SingleSelectField {
            id
            name
          }
        }
      }
    }
    """
    options = [
        {"name": name, "color": color, "description": description}
        for name, color, description in STATUS_OPTIONS
    ]
    graphql(query, {"fieldId": status_field_id, "options": options})


def ensure_project_fields(project_number: int) -> dict[str, dict[str, object]]:
    fields = project_fields(project_number)
    if "Status" in fields:
        update_status_options(str(fields["Status"]["id"]))

    for name, (data_type, options) in PROJECT_FIELD_DEFINITIONS.items():
        fields = project_fields(project_number)
        if name in fields:
            continue
        args = [
            "gh",
            "project",
            "field-create",
            str(project_number),
            "--owner",
            OWNER,
            "--name",
            name,
            "--data-type",
            data_type,
        ]
        if options:
            args.extend(["--single-select-options", ",".join(options)])
        run(args)

    return project_fields(project_number)


def project_items(project_number: int) -> dict[int, dict[str, object]]:
    data = gh_json(["gh", "project", "item-list", str(project_number), "--owner", OWNER, "--format", "json", "--limit", "500"])
    items: dict[int, dict[str, object]] = {}
    for item in data.get("items", []):
        content = item.get("content") or {}
        number = content.get("number")
        if isinstance(number, int):
            items[number] = item
    return items


def single_select_options_by_name(field: dict[str, object]) -> dict[str, str]:
    return {option["name"]: option["id"] for option in field.get("options", [])}


def set_project_value(
    *,
    project_id: str,
    item_id: str,
    field: dict[str, object],
    text: str | None = None,
    number: float | None = None,
    option: str | None = None,
) -> None:
    args = [
        "gh",
        "project",
        "item-edit",
        "--project-id",
        project_id,
        "--id",
        item_id,
        "--field-id",
        str(field["id"]),
    ]
    if option is not None:
        option_id = single_select_options_by_name(field).get(option)
        if not option_id:
            return
        args.extend(["--single-select-option-id", option_id])
    elif text is not None:
        args.extend(["--text", text])
    elif number is not None:
        args.extend(["--number", str(number)])
    else:
        return
    run(args)


def field_context_for_issue(issue: dict[str, object]) -> dict[str, str]:
    labels = [label["name"] for label in issue.get("labels", [])]
    title = str(issue["title"])
    seed_id = title.split("]", 1)[0].lstrip("[") if title.startswith("[") else ""
    epic_id = seed_id.split("-")[0] if seed_id else ""
    phase = milestone_for_labels(labels, issue.get("milestone", {}).get("title") if issue.get("milestone") else None)
    priority = next((label.split(":", 1)[1].upper() for label in labels if label.startswith("priority:")), "")
    areas = ", ".join(label.split(":", 1)[1] for label in labels if label.startswith("area:"))
    demo_critical = "Yes" if "demo-critical" in labels else "No"
    status = "Done" if issue.get("state") == "CLOSED" else "Backlog"
    risk = "Normal"
    if int(issue["number"]) == 2:
        status = "Blocked"
        risk = "Blocked"
    elif int(issue["number"]) in {6, 7, 8, 11, 12, 13, 14, 43, 46}:
        status = "Ready"

    target = {
        "Phase 1 — Internal Demo / Pre-MVP": "Internal Demo",
        "Phase 2 — MVP Product Spine": "MVP",
        "Phase 3 — AI/RAG & Document Intelligence": "AI/RAG",
        "Phase 4 — Portfolio Cockpit & Decision Packs": "Portfolio",
        "Phase 5 — Enterprise Security & Deployment": "Enterprise",
        "Phase 6 — Pilot-Ready Release": "Pilot-Ready",
    }.get(phase, "Internal Demo")

    return {
        "Phase": phase,
        "Epic": epic_id,
        "Priority": priority,
        "Area": areas,
        "Target Release": target,
        "Risk": risk,
        "Owner": "Codex / Mal7",
        "Demo Critical": demo_critical,
        "Status": status,
    }


def sync_project_board(epics: list[dict[str, object]], stories: list[dict[str, object]]) -> tuple[bool, str]:
    project = find_project()
    if not project:
        return False, "Project is not available."

    project_number = int(project["number"])
    project_id = str(project["id"])
    run(
        [
            "gh",
            "project",
            "edit",
            str(project_number),
            "--owner",
            OWNER,
            "--description",
            PROJECT_DESCRIPTION,
            "--readme",
            PROJECT_README,
            "--visibility",
            "PRIVATE",
        ]
    )
    run(["gh", "project", "link", str(project_number), "--owner", OWNER, "--repo", REPO], check=False)
    fields = ensure_project_fields(project_number)
    issue_numbers = [int(issue["number"]) for issue in [*epics, *stories]]
    existing_items = project_items(project_number)

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
            "number,title,url,state,labels,milestone",
        ]
    )
    issues_by_number = {int(issue["number"]): issue for issue in issues if int(issue["number"]) in issue_numbers}

    for number in issue_numbers:
        issue = issues_by_number[number]
        item = existing_items.get(number)
        if not item:
            result = run(["gh", "project", "item-add", str(project_number), "--owner", OWNER, "--url", str(issue["url"]), "--format", "json"])
            item = json.loads(result.stdout or "{}")
            existing_items[number] = item
        item_id = str(item["id"])
        context = field_context_for_issue(issue)
        for field_name in ["Status", "Phase", "Priority", "Target Release", "Risk", "Demo Critical"]:
            if field_name in fields and context.get(field_name):
                set_project_value(project_id=project_id, item_id=item_id, field=fields[field_name], option=context[field_name])
        for field_name in ["Epic", "Area", "Owner"]:
            if field_name in fields:
                set_project_value(project_id=project_id, item_id=item_id, field=fields[field_name], text=context.get(field_name, ""))

    return True, f"Project populated: {project.get('url', PROJECT_TITLE)} with {len(issue_numbers)} issue items"


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
    if project_ok:
        board_intro = [
            "GitHub Project is available and is the live delivery board. This file is kept as a lightweight local mirror/reference.",
            "",
            "## GitHub Project",
            "",
            f"- Board: `{PROJECT_TITLE}`",
            f"- Status: `{project_message}`",
        ]
    else:
        board_intro = [
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
        ]

    board_lines = [
        "# Local Project Board",
        "",
        *board_intro,
        "",
        "## Columns",
        "",
        "Backlog, Ready, In Progress, In Review, Blocked, Done.",
        "",
        "## GitHub Project Fields",
        "",
        "Phase, Epic, Priority, Area, Status, Target Release, Risk, Owner, Estimate, Demo Critical.",
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
    epics, stories = sync_issues(load_yaml("epics_and_stories.yaml"))
    project_ok, project_message = project_status()
    if project_ok:
        project_ok, project_message = sync_project_board(epics, stories)
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
