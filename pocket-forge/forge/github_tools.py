"""
github_tools.py / pocket-forge / The forge's GitHub hands /
Copyright (c) 2026 Kitsune Kits. All rights reserved.

Typed GitHub REST tools for the Pocket Forge ensemble. Read tools carry a
read-only hint and the permission policy lets them run; write tools are
gated — the turn blocks until the Architect answers. Every tool speaks to
api.github.com with the token from GITHUB_TOKEN (or GH_TOKEN), and defaults
its owner to the Kitsune-Kits organization.
"""

import base64
import os
from typing import Any
from urllib.parse import quote

import httpx
from mistralai import agents

# ────────────────────────────────────────────────────────────────────────
# MARK: - Constants
# ────────────────────────────────────────────────────────────────────────

_API_ROOT = "https://api.github.com"
_API_VERSION = "2022-11-28"
_MAX_FILE_BYTES = 1_000_000

#: The org tools default to when a call omits `owner`.
DEFAULT_OWNER = os.environ.get("KRI_GITHUB_OWNER", "Kitsune-Kits")

#: Tool IDs the permission policy allows without approval (read-only).
READ_TOOL_IDS = [
    "client.gh_read_file",
    "client.gh_list_dir",
    "client.gh_get_branch_head",
    "client.gh_list_pull_requests",
    "client.gh_get_pull_request",
    "client.gh_list_issues",
    "client.gh_get_issue",
    "client.gh_list_workflow_runs",
    "client.gh_get_workflow_run",
    "client.gh_list_run_jobs",
]

#: Tool IDs that always wait for the Architect's word (writes).
WRITE_TOOL_IDS = [
    "client.gh_create_branch",
    "client.gh_write_file",
    "client.gh_create_pull_request",
    "client.gh_merge_pull_request",
    "client.gh_create_issue",
    "client.gh_add_comment",
    "client.gh_close_issue",
    "client.gh_rerun_workflow",
]


# ────────────────────────────────────────────────────────────────────────
# MARK: - Transport
# ────────────────────────────────────────────────────────────────────────

def _token() -> str:
    """The forge's key, from the environment — never hardcoded."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
    if not token:
        raise agents.ToolError(
            "No GITHUB_TOKEN in the environment. The Architect must set it "
            "before the forge can work on GitHub."
        )
    return token


async def _github(
    method: str,
    path: str,
    json_body: dict[str, Any] | None = None,
    params: dict[str, Any] | None = None,
) -> Any:
    """One GitHub REST call; expected failures become ToolError for the model."""
    headers = {
        "Authorization": f"Bearer {_token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": _API_VERSION,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.request(
            method, f"{_API_ROOT}{path}", headers=headers, json=json_body, params=params
        )
    if response.status_code == 404:
        raise agents.ToolError(
            f"GitHub says 404 for {path}: not found, or the token cannot see it."
        )
    if response.status_code in (401, 403):
        raise agents.ToolError(
            f"GitHub refused ({response.status_code}) for {path}: check the "
            f"token and its scopes. {response.text[:200]}"
        )
    if response.status_code >= 400:
        raise agents.ToolError(
            f"GitHub error {response.status_code} for {path}: {response.text[:300]}"
        )
    if response.status_code == 204:
        return None
    return response.json()


def _owner(owner: str | None) -> str:
    """Resolve the owner, defaulting to the KRI org."""
    return owner or DEFAULT_OWNER


def _ref_path(branch: str) -> str:
    """A branch name as a git ref path segment (slashes percent-encoded)."""
    return quote(branch, safe="")


# ────────────────────────────────────────────────────────────────────────
# MARK: - Read tools (allowed without approval)
# ────────────────────────────────────────────────────────────────────────

@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_read_file(
    repo: str,
    path: str,
    owner: str | None = None,
    ref: str = "main",
) -> dict[str, Any]:
    """Read one file from a repository. Returns its text, byte size, and blob
    sha — pass that sha as expected_sha when updating the file."""
    result = await _github(
        "GET",
        f"/repos/{_owner(owner)}/{repo}/contents/{path.lstrip('/')}",
        params={"ref": ref},
    )
    if isinstance(result, list):
        raise agents.ToolError(f"{path} is a directory — use gh_list_dir.")
    if result.get("encoding") != "base64" or int(result.get("size", 0)) > _MAX_FILE_BYTES:
        raise agents.ToolError(
            "The file is too large or not base64 text — read it a narrower scope."
        )
    return {
        "path": result["path"],
        "sha": result["sha"],
        "size": result["size"],
        "text": base64.b64decode(result["content"]).decode("utf-8", errors="replace"),
    }


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_list_dir(
    repo: str,
    path: str = "",
    owner: str | None = None,
    ref: str = "main",
) -> list[dict[str, str]]:
    """List one directory of a repository: name, type (file/dir), path."""
    result = await _github(
        "GET",
        f"/repos/{_owner(owner)}/{repo}/contents/{path.strip('/')}",
        params={"ref": ref},
    )
    if not isinstance(result, list):
        raise agents.ToolError(f"{path or '/'} is a file — use gh_read_file.")
    return [
        {"name": item["name"], "type": item["type"], "path": item["path"]}
        for item in result
    ]


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_get_branch_head(
    repo: str,
    branch: str = "main",
    owner: str | None = None,
) -> dict[str, str]:
    """The commit sha a branch currently points at (live source, never assumed)."""
    result = await _github(
        "GET", f"/repos/{_owner(owner)}/{repo}/git/ref/heads/{_ref_path(branch)}"
    )
    return {"branch": branch, "sha": result["object"]["sha"]}


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_list_pull_requests(
    repo: str,
    owner: str | None = None,
    state: str = "open",
    limit: int = 10,
) -> list[dict[str, Any]]:
    """List pull requests of a repository (state: open, closed, or all)."""
    result = await _github(
        "GET",
        f"/repos/{_owner(owner)}/{repo}/pulls",
        params={"state": state, "per_page": max(1, min(limit, 100))},
    )
    return [
        {
            "number": pr["number"],
            "title": pr["title"],
            "state": pr["state"],
            "draft": pr.get("draft", False),
            "merged": pr.get("merged", False),
            "head": pr["head"]["ref"],
            "base": pr["base"]["ref"],
            "author": pr["user"]["login"],
            "url": pr["html_url"],
        }
        for pr in result
    ]


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_get_pull_request(
    repo: str,
    number: int,
    owner: str | None = None,
) -> dict[str, Any]:
    """One pull request in detail, including mergeable state and diff size."""
    pr = await _github("GET", f"/repos/{_owner(owner)}/{repo}/pulls/{number}")
    return {
        "number": pr["number"],
        "title": pr["title"],
        "state": pr["state"],
        "draft": pr.get("draft", False),
        "merged": pr.get("merged", False),
        "mergeable_state": pr.get("mergeable_state"),
        "head": pr["head"]["ref"],
        "head_sha": pr["head"]["sha"],
        "base": pr["base"]["ref"],
        "changed_files": pr.get("changed_files"),
        "additions": pr.get("additions"),
        "deletions": pr.get("deletions"),
        "author": pr["user"]["login"],
        "body": (pr.get("body") or "")[:4000],
        "url": pr["html_url"],
    }


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_list_issues(
    repo: str,
    owner: str | None = None,
    state: str = "open",
    limit: int = 10,
) -> list[dict[str, Any]]:
    """List issues of a repository (pull requests excluded; state: open, closed, or all)."""
    result = await _github(
        "GET",
        f"/repos/{_owner(owner)}/{repo}/issues",
        params={"state": state, "per_page": max(1, min(limit, 100))},
    )
    return [
        {
            "number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "labels": [label["name"] for label in issue.get("labels", [])],
            "url": issue["html_url"],
        }
        for issue in result
        if "pull_request" not in issue
    ]


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_get_issue(
    repo: str,
    number: int,
    owner: str | None = None,
) -> dict[str, Any]:
    """One issue in detail, with its body and comment count."""
    issue = await _github("GET", f"/repos/{_owner(owner)}/{repo}/issues/{number}")
    return {
        "number": issue["number"],
        "title": issue["title"],
        "state": issue["state"],
        "labels": [label["name"] for label in issue.get("labels", [])],
        "comments": issue.get("comments"),
        "body": (issue.get("body") or "")[:4000],
        "url": issue["html_url"],
    }


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_list_workflow_runs(
    repo: str,
    owner: str | None = None,
    limit: int = 10,
) -> list[dict[str, Any]]:
    """List recent GitHub Actions runs of a repository."""
    result = await _github(
        "GET",
        f"/repos/{_owner(owner)}/{repo}/actions/runs",
        params={"per_page": max(1, min(limit, 100))},
    )
    return [
        {
            "id": run["id"],
            "name": run["name"],
            "event": run.get("event"),
            "status": run.get("status"),
            "conclusion": run.get("conclusion"),
            "branch": run.get("head_branch"),
            "sha": run.get("head_sha"),
            "created_at": run.get("created_at"),
            "url": run["html_url"],
        }
        for run in result.get("workflow_runs", [])
    ]


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_get_workflow_run(
    repo: str,
    run_id: int,
    owner: str | None = None,
) -> dict[str, Any]:
    """One workflow run in detail."""
    run = await _github(
        "GET", f"/repos/{_owner(owner)}/{repo}/actions/runs/{run_id}"
    )
    return {
        "id": run["id"],
        "name": run["name"],
        "event": run.get("event"),
        "status": run.get("status"),
        "conclusion": run.get("conclusion"),
        "branch": run.get("head_branch"),
        "sha": run.get("head_sha"),
        "created_at": run.get("created_at"),
        "updated_at": run.get("updated_at"),
        "url": run["html_url"],
    }


@agents.tool(annotations=agents.ToolAnnotations(read_only_hint=True))
async def gh_list_run_jobs(
    repo: str,
    run_id: int,
    owner: str | None = None,
) -> list[dict[str, Any]]:
    """The jobs of one workflow run, with per-step status — how a pipeline
    failure is actually diagnosed."""
    result = await _github(
        "GET", f"/repos/{_owner(owner)}/{repo}/actions/runs/{run_id}/jobs"
    )
    return [
        {
            "id": job["id"],
            "name": job["name"],
            "status": job.get("status"),
            "conclusion": job.get("conclusion"),
            "steps": [
                {"name": step["name"], "status": step["status"], "conclusion": step.get("conclusion")}
                for step in job.get("steps", [])
            ],
        }
        for job in result.get("jobs", [])
    ]


# ────────────────────────────────────────────────────────────────────────
# MARK: - Write tools (gated — the Architect's word)
# ────────────────────────────────────────────────────────────────────────

@agents.tool
async def gh_create_branch(
    repo: str,
    branch: str,
    owner: str | None = None,
    from_branch: str = "main",
) -> dict[str, str]:
    """Create a branch (gated: the Architect's word). Name it with your
    persona prefix, e.g. `piko/fix-ci-cache` — never push straight to main."""
    head = await _github(
        "GET", f"/repos/{_owner(owner)}/{repo}/git/ref/heads/{_ref_path(from_branch)}"
    )
    result = await _github(
        "POST",
        f"/repos/{_owner(owner)}/{repo}/git/refs",
        json_body={"ref": f"refs/heads/{branch}", "sha": head["object"]["sha"]},
    )
    return {"branch": branch, "from": from_branch, "sha": result["object"]["sha"]}


@agents.tool
async def gh_write_file(
    repo: str,
    path: str,
    branch: str,
    message: str,
    content: str,
    owner: str | None = None,
    expected_sha: str | None = None,
) -> dict[str, Any]:
    """Create or update one file on a branch (gated: the Architect's word).
    `message` is the full commit message — it must carry the persona
    attribution block and `KRI-Persona:` trailer per the ratified standard.
    Pass the file's current sha as `expected_sha` when updating (from
    gh_read_file); omit it when creating a new file."""
    payload: dict[str, Any] = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch": branch,
    }
    if expected_sha:
        payload["sha"] = expected_sha
    result = await _github(
        "PUT", f"/repos/{_owner(owner)}/{repo}/contents/{path.lstrip('/')}", json_body=payload
    )
    return {
        "path": path,
        "branch": branch,
        "commit_sha": result["commit"]["sha"],
    }


@agents.tool
async def gh_create_pull_request(
    repo: str,
    title: str,
    head: str,
    base: str = "main",
    owner: str | None = None,
    body: str = "",
) -> dict[str, Any]:
    """Open a pull request (gated: the Architect's word). Title follows the
    persona convention `<emoji> <Name>: <Title>`; the body carries the
    `KRI-Persona:` line."""
    pr = await _github(
        "POST",
        f"/repos/{_owner(owner)}/{repo}/pulls",
        json_body={"title": title, "head": head, "base": base, "body": body},
    )
    return {"number": pr["number"], "url": pr["html_url"], "head": head, "base": base}


@agents.tool
async def gh_merge_pull_request(
    repo: str,
    number: int,
    owner: str | None = None,
    merge_method: str = "squash",
) -> dict[str, Any]:
    """Merge a pull request (gated: the Architect's explicit word — the
    forge never merges on routine work). Squash is the org precedent."""
    result = await _github(
        "PUT",
        f"/repos/{_owner(owner)}/{repo}/pulls/{number}/merge",
        json_body={"merge_method": merge_method},
    )
    return {
        "merged": result.get("merged", False),
        "sha": result.get("sha"),
        "message": result.get("message", ""),
    }


@agents.tool
async def gh_create_issue(
    repo: str,
    title: str,
    owner: str | None = None,
    body: str = "",
    labels: list[str] | None = None,
) -> dict[str, Any]:
    """Open an issue (gated: the Architect's word)."""
    payload: dict[str, Any] = {"title": title, "body": body}
    if labels:
        payload["labels"] = labels
    issue = await _github(
        "POST", f"/repos/{_owner(owner)}/{repo}/issues", json_body=payload
    )
    return {"number": issue["number"], "url": issue["html_url"]}


@agents.tool
async def gh_add_comment(
    repo: str,
    number: int,
    body: str,
    owner: str | None = None,
) -> dict[str, Any]:
    """Comment on an issue or pull request (gated: the Architect's word)."""
    comment = await _github(
        "POST",
        f"/repos/{_owner(owner)}/{repo}/issues/{number}/comments",
        json_body={"body": body},
    )
    return {"id": comment["id"], "url": comment["html_url"]}


@agents.tool
async def gh_close_issue(
    repo: str,
    number: int,
    owner: str | None = None,
) -> dict[str, Any]:
    """Close an issue as completed (gated: the Architect's word)."""
    issue = await _github(
        "PATCH",
        f"/repos/{_owner(owner)}/{repo}/issues/{number}",
        json_body={"state": "closed", "state_reason": "completed"},
    )
    return {"number": issue["number"], "state": issue["state"]}


@agents.tool
async def gh_rerun_workflow(
    repo: str,
    run_id: int,
    owner: str | None = None,
) -> dict[str, bool]:
    """Re-run a failed GitHub Actions run (gated: the Architect's word)."""
    await _github(
        "POST", f"/repos/{_owner(owner)}/{repo}/actions/runs/{run_id}/rerun"
    )
    return {"rerun": True}


# ────────────────────────────────────────────────────────────────────────
# MARK: - Tool registries (for the Agent and its policy)
# ────────────────────────────────────────────────────────────────────────

READ_TOOLS = [
    gh_read_file,
    gh_list_dir,
    gh_get_branch_head,
    gh_list_pull_requests,
    gh_get_pull_request,
    gh_list_issues,
    gh_get_issue,
    gh_list_workflow_runs,
    gh_get_workflow_run,
    gh_list_run_jobs,
]

WRITE_TOOLS = [
    gh_create_branch,
    gh_write_file,
    gh_create_pull_request,
    gh_merge_pull_request,
    gh_create_issue,
    gh_add_comment,
    gh_close_issue,
    gh_rerun_workflow,
]
