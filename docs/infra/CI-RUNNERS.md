# CI Forge — Group Runner Runbook

> **Maintained by:** ⚡ Piko (CI infrastructure) · **Status:** proposed —
> pending bring-up on the Architect's Mac · Companion:
> [SETUP-UI-CHECKLIST.md](../SETUP-UI-CHECKLIST.md) (runner creation is a
> manual UI step, listed there).

## Why — the diagnosis (2026-10-26)

Every CI job in every repo since ~Oct 18 has failed with a **zero-byte
job log** — including green-status pipelines whose only failures were
allow_failure jobs. That signature is not broken CI. GitLab.com Free
gives the whole `kitsune-kits` namespace **400 compute minutes per
month** on instance runners; when the quota runs out, instance runners
silently stop picking up new jobs, which "can look like a runner
availability problem rather than a compute quota problem" (GitLab docs).
The quota resets on the first day of each month (next: Nov 1).

Self-hosted group runners are **unlimited and do not count against the
quota at all**. One group runner registered for `kitsune-kits` covers
all seven repos.

**Rule of thumb going in:** jobs failing with a full log are real
failures (read the log); jobs failing with zero-byte logs across all
repos at once are infrastructure starvation, not code. The last
known-good CI signal is the Oct 13–14 pipelines.

## The fix — a self-hosted group runner on the Mac (Docker executor)

A group runner, Docker executor, **run-untagged**. Docker executor
means every job runs in the image its `.gitlab-ci.yml` already names
(`alpine:latest`, etc.) and the Mac stays clean; run-untagged means
**zero per-repo CI config changes** — all seven repos adopt it the
moment it goes green.

### 1. Prepare the Mac

- Install and start **Docker Desktop** (or colima). Jobs cannot run
  without it.
- Install the **official** gitlab-runner binary. GitLab does not
  maintain the Homebrew formula — use the official binary on Apple
  Silicon:

```bash
sudo mkdir -p /usr/local/bin
sudo curl --output /usr/local/bin/gitlab-runner \
  "https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/latest/binaries/gitlab-runner-darwin-arm64"
sudo chmod +x /usr/local/bin/gitlab-runner
gitlab-runner --version
```

### 2. Create the runner in the GitLab UI (Owner, once)

`kitsune-kits` group → **Settings → CI/CD → Runners** → **New group
runner**:

- Description: `KRI Forge (Mac, docker)`
- Tags: none needed — tick **Run untagged jobs** (this is what avoids
  all per-repo config changes)
- Click **Create**, copy the `glrt-` authentication token (shown once)

### 3. Register

```bash
gitlab-runner register \
  --url https://gitlab.com \
  --token glrt-XXXXXXXXXXXX \
  --executor docker \
  --docker-image alpine:latest \
  --description "KRI Forge (Mac, docker)"
```

Config lands in `/etc/gitlab-runner/config.toml` (user install:
`~/.gitlab-runner/config.toml`).

### 4. Run it as a service

```bash
gitlab-runner install   # installs a launchd user service
gitlab-runner start
```

Docker Desktop must be running before jobs start. Set it to launch at
login.

### 5. Mac housekeeping

- **Sleep kills the forge.** During build sessions either run
  `caffeinate -is` in a terminal, or set
  `sudo pmset -a sleep 0` and revert after.
- Concurrency defaults to 1 simultaneous job — fine for our workloads;
  raise `concurrent` in `config.toml` if queues annoy you.
- The runner only works while the Mac is awake; queued jobs simply wait.

### 6. Verify (smoke test)

1. Group → Settings → CI/CD → Runners — the KRI Forge dot is green.
2. Retry a zero-byte-failed job (e.g. the `agents-guard` job on the
   kri docs MRs, or Kogane MR !54's `prop-validate`). It should now
   produce a real log and pass.
3. **"Pipelines must succeed"** in MR settings is then safe to enforce
   namespace-wide — the mid-Oct blackout was never a code problem.

### 7. Quota doctrine (recommendation)

- Once the Forge is green, **disable instance runners for the group**
  (Settings → CI/CD → Runners → "Enable instance runners for this
  group" off). Jobs then never touch the 400-minute pool, and the
  quota survives as a pure fallback if the Mac is down.
- Keep the existing compute-minute defense: pipelines only for merge
  requests, `main`, and tags (already in every repo's workflow rules).

## Failure signature cheat-sheet (for future sessions)

| Signature | Meaning |
|---|---|
| Jobs failed, zero-byte logs, across all repos at once | Instance-runner quota exhausted (or every runner offline) — infrastructure, not code |
| Job failed with a full log | Real CI failure — read the log, fix the repo |
| Pipeline green with red allowed jobs | Fine — signals, not gates (org convention) |
| Jobs stuck `pending` forever | No runner available: Mac asleep, Docker down, or instance runners disabled with the Forge offline |

## Known real failures (fixed, tracked separately)

Saffron Blossom carried three genuine non-blocking failures under the
blackout (Oct 13 logs): luacheck line-length warnings in the prop
macros, a markdownlint config mismatch against legacy docs, and a
busybox `date` incompatibility in the countdown-badge job. Fixed in
`piko/ci-green-pipeline-fixes` (Project-Saffron-Blossom).
