#!/usr/bin/env python3
"""Synchronize implementation task issues and Project items."""

from __future__ import annotations

import json
import subprocess
import tempfile
import time
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REPO = "mahmoudahmedalaa/AI-Value-Discovery"
OWNER = "mahmoudahmedalaa"
PROJECT_NUMBER = "3"
PROJECT_TITLE = "AI Value Discovery Product Build"
PROJECT_ID = "PVT_kwHOAQ7yDs4BaF3o"


PHASE_LABEL_TO_MILESTONE = {
    "phase:0-governance": "Phase 0 — Product Governance & Repo Foundation",
    "phase:1-demo": "Phase 1 — Internal Demo / Pre-MVP",
    "phase:2-mvp": "Phase 2 — MVP Product Spine",
    "phase:3-ai-rag": "Phase 3 — AI/RAG & Document Intelligence",
    "phase:4-portfolio": "Phase 4 — Portfolio Cockpit & Decision Packs",
    "phase:5-enterprise": "Phase 5 — Enterprise Security & Deployment",
    "phase:6-release": "Phase 6 — Pilot-Ready Release",
}

TARGET_BY_PHASE = {
    "Phase 1 — Internal Demo / Pre-MVP": "Internal Demo",
    "Phase 2 — MVP Product Spine": "MVP",
    "Phase 3 — AI/RAG & Document Intelligence": "AI/RAG",
    "Phase 4 — Portfolio Cockpit & Decision Packs": "Portfolio",
    "Phase 5 — Enterprise Security & Deployment": "Enterprise",
    "Phase 6 — Pilot-Ready Release": "Pilot-Ready",
}


def run(args: list[str], *, check: bool = True, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    result: subprocess.CompletedProcess[str] | None = None
    for attempt in range(3 if check else 1):
        try:
            result = subprocess.run(
                args,
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exc:
            result = subprocess.CompletedProcess(args, 124, output=exc.stdout or "", stderr=exc.stderr or "Command timed out")
        if result.returncode == 0 or not check:
            return result
        time.sleep(1.5 * (attempt + 1))
    assert result is not None
    raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)


def gh_json(args: list[str]) -> object:
    return json.loads(run(args).stdout or "null")


def graphql(query: str, variables: dict[str, object], *, check: bool = True) -> object:
    payload = {"query": query, "variables": variables}
    with tempfile.NamedTemporaryFile("w", delete=False) as handle:
        json.dump(payload, handle)
        path = handle.name
    result = run(["gh", "api", "graphql", "--input", path], check=check)
    if result.returncode != 0:
        return {"error": (result.stderr or result.stdout).strip()}
    return json.loads(result.stdout or "{}")


def load_tasks() -> list[dict[str, object]]:
    return yaml.safe_load((ROOT / "project_board_seed/implementation_tasks.yaml").read_text())


def milestone_for(labels: list[str], phase: str) -> str:
    for label in labels:
        if label in PHASE_LABEL_TO_MILESTONE:
            return PHASE_LABEL_TO_MILESTONE[label]
    return phase


def issue_body(task: dict[str, object], parent_issue: dict[str, object]) -> str:
    criteria = "\n".join(f"- [ ] {criterion}" for criterion in task.get("acceptance_criteria", []))
    labels = "\n".join(f"- `{label}`" for label in task.get("labels", []))
    return f"""Seed ID: `{task['id']}`
Parent story: #{parent_issue['number']} `{task['parent']}` {parent_issue['title']}

## Summary

Implementation task for `{task['parent']}`.

## Labels
{labels}

## Acceptance Criteria
{criteria}

## Governance
- [ ] Added to GitHub Project board
- [ ] Linked as a sub-issue under the parent story where GitHub supports it
- [ ] Relevant checks/docs/status updates completed before closing
"""


def issues_by_title() -> dict[str, dict[str, object]]:
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
            "number,title,url,id,state,labels,milestone",
        ]
    )
    return {issue["title"]: issue for issue in issues}


def parent_stories() -> dict[str, dict[str, object]]:
    mapping: dict[str, dict[str, object]] = {}
    for issue in issues_by_title().values():
        title = str(issue["title"])
        if title.startswith("[") and "]" in title:
            seed_id = title.split("]", 1)[0].lstrip("[")
            mapping[seed_id] = issue
    return mapping


def create_or_update_task(task: dict[str, object], existing: dict[str, dict[str, object]], parents: dict[str, dict[str, object]]) -> dict[str, object]:
    parent = parents[str(task["parent"])]
    title = f"[{task['id']}] {task['title']}"
    labels = list(task["labels"])
    milestone = milestone_for(labels, str(task["phase"]))
    body = issue_body(task, parent)

    if title in existing:
        issue = existing[title]
        with tempfile.NamedTemporaryFile("w", delete=False) as handle:
            handle.write(body)
            path = handle.name
        run(
            [
                "gh",
                "issue",
                "edit",
                str(issue["number"]),
                "--repo",
                REPO,
                "--body-file",
                path,
                "--add-label",
                ",".join(labels),
                "--milestone",
                milestone,
            ]
        )
        return issue

    result = run(
        [
            "gh",
            "issue",
            "create",
            "--repo",
            REPO,
            "--title",
            title,
            "--body",
            body,
            "--label",
            ",".join(labels),
            "--milestone",
            milestone,
        ]
    )
    url = result.stdout.strip().splitlines()[-1]
    issue = {
        "number": int(url.rstrip("/").split("/")[-1]),
        "title": title,
        "url": url,
        "id": "",
    }
    existing[title] = issue
    return issue


def refresh_issue(issue_number: int) -> dict[str, object]:
    return gh_json(
        [
            "gh",
            "issue",
            "view",
            str(issue_number),
            "--repo",
            REPO,
            "--json",
            "number,title,url,id,state,labels,milestone",
        ]
    )


def project_fields() -> dict[str, dict[str, object]]:
    data = gh_json(["gh", "project", "field-list", PROJECT_NUMBER, "--owner", OWNER, "--format", "json", "--limit", "100"])
    fields = {field["name"]: field for field in data.get("fields", [])}
    if "Story" not in fields:
        run(["gh", "project", "field-create", PROJECT_NUMBER, "--owner", OWNER, "--name", "Story", "--data-type", "TEXT"])
        data = gh_json(["gh", "project", "field-list", PROJECT_NUMBER, "--owner", OWNER, "--format", "json", "--limit", "100"])
        fields = {field["name"]: field for field in data.get("fields", [])}
    return fields


def project_items() -> dict[int, dict[str, object]]:
    data = gh_json(["gh", "project", "item-list", PROJECT_NUMBER, "--owner", OWNER, "--format", "json", "--limit", "500"])
    items: dict[int, dict[str, object]] = {}
    for item in data.get("items", []):
        content = item.get("content") or {}
        number = content.get("number")
        if isinstance(number, int):
            items[number] = item
    return items


def option_id(field: dict[str, object], name: str) -> str | None:
    for option in field.get("options", []):
        if option["name"] == name:
            return option["id"]
    return None


def set_project_value(item_id: str, field: dict[str, object], *, option: str | None = None, text: str | None = None) -> None:
    args = ["gh", "project", "item-edit", "--project-id", PROJECT_ID, "--id", item_id, "--field-id", str(field["id"])]
    if option is not None:
        selected = option_id(field, option)
        if not selected:
            return
        args += ["--single-select-option-id", selected]
    elif text is not None:
        args += ["--text", text]
    else:
        return
    run(args)


def add_to_project(issue: dict[str, object], task: dict[str, object], fields: dict[str, dict[str, object]], items: dict[int, dict[str, object]]) -> None:
    item = items.get(int(issue["number"]))
    if not item:
        result = run(["gh", "project", "item-add", PROJECT_NUMBER, "--owner", OWNER, "--url", str(issue["url"]), "--format", "json"])
        item = json.loads(result.stdout or "{}")
        items[int(issue["number"])] = item

    labels = list(task["labels"])
    priority = next((label.split(":", 1)[1].upper() for label in labels if label.startswith("priority:")), "")
    area = ", ".join(label.split(":", 1)[1] for label in labels if label.startswith("area:"))
    phase = str(task["phase"])
    target = TARGET_BY_PHASE.get(phase, "Internal Demo")
    demo = "Yes" if "demo-critical" in labels else "No"
    epic = str(task["parent"]).split("-", 1)[0]

    values = {
        "Status": str(task.get("status", "Backlog")),
        "Phase": phase,
        "Priority": priority,
        "Target Release": target,
        "Risk": "Normal",
        "Demo Critical": demo,
    }
    for field_name, value in values.items():
        if field_name in fields and value:
            set_project_value(str(item["id"]), fields[field_name], option=value)
    for field_name, value in {"Epic": epic, "Story": str(task["parent"]), "Area": area, "Owner": "Codex / Mal7"}.items():
        if field_name in fields:
            set_project_value(str(item["id"]), fields[field_name], text=value)


def link_subissue(parent: dict[str, object], child: dict[str, object]) -> None:
    query = """
    mutation($issueId: ID!, $subIssueId: ID!) {
      addSubIssue(input: {issueId: $issueId, subIssueId: $subIssueId, replaceParent: true}) {
        issue { id }
        subIssue { id }
      }
    }
    """
    graphql(query, {"issueId": parent["id"], "subIssueId": child["id"]}, check=False)


def append_parent_task_index(parents: dict[str, dict[str, object]], tasks_by_parent: dict[str, list[dict[str, object]]]) -> None:
    for parent_id, tasks in tasks_by_parent.items():
        parent = parents[parent_id]
        lines = [
            f"## Implementation Tasks",
            "",
            *[f"- [ ] #{task['number']} `{task['id']}` {task['title']}" for task in tasks],
        ]
        comment = "\n".join(lines)
        run(["gh", "issue", "comment", str(parent["number"]), "--repo", REPO, "--body", comment], check=False)


def main() -> int:
    tasks = load_tasks()
    existing = issues_by_title()
    parents = parent_stories()
    fields = project_fields()
    items = project_items()
    tasks_by_parent: dict[str, list[dict[str, object]]] = {}
    created_or_updated: list[dict[str, object]] = []

    for task in tasks:
        parent = parents[str(task["parent"])]
        issue = create_or_update_task(task, existing, parents)
        issue = refresh_issue(int(issue["number"]))
        add_to_project(issue, task, fields, items)
        link_subissue(parent, issue)
        record = {"number": issue["number"], "id": task["id"], "title": task["title"]}
        tasks_by_parent.setdefault(str(task["parent"]), []).append(record)
        created_or_updated.append(record)
        print(f"synced #{issue['number']} {task['id']} {task['title']}")

    append_parent_task_index(parents, tasks_by_parent)
    print(f"tasks_synced={len(created_or_updated)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
