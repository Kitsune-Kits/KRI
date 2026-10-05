# Proposal — GitLab Workspaces Infrastructure

Status: **Draft — awaiting Architect decision**
Author: ⚡ Piko (firmware & tooling)
Date: 2026-10-05
Related: `.devfile.yaml` on kitsuneOS, Project-Kogane, Project-Saffron-Blossom, Project-Lazy-Comet, kitsunebios; `.gitlab/wiki/EDITOR-SETUP.md` on all repos

---

## Why

The GitLab Web IDE covers quick edits and MR reviews, but cannot compile or run toolchains.
Workspaces give every repo a full remote Linux dev environment, from any browser —
Rust builds for kitsuneOS, Lua prop linting, kitsunebios running natively.
All five code repos already ship devfiles; the only missing piece is **infrastructure**.

GitLab does not host workspaces for you: they run on **our own Kubernetes cluster**,
connected to the `kitsune-kits` group via a GitLab agent.

## What we need

1. A Kubernetes cluster (single node is fine for our scale).
2. The **GitLab agent for Kubernetes** connected to the `kitsune-kits` group.
3. Agent config with remote development enabled:

```yaml
# .gitlab/agents/workspaces/config.yaml (in a repo connected to the agent)
remote_development:
  enabled: true
  dns_zone: "workspaces.kitsune-kits.dev"   # or any zone we own / a nip.io-style zone
```

4. A DNS record for the workspace zone pointing at the cluster ingress.

## Options

### Option A — Cheap single-node K3s on a VPS (recommended)
- One VM (2 vCPU / 4–8 GB RAM), K3s single-node.
- Cost ballpark: **~$6–15/month** (Hetzner CX22-class or equivalent DigitalOcean/Linode tier).
- Pros: cheapest, fully ours, five concurrent-ish workspaces feasible with devfile resource limits set modestly (1–2 vCPU / 2 GB per workspace).
- Cons: we own the ops — updates, backups, ingress TLS.

### Option B — Repurpose existing on-site hardware
- Any spare Mac/PC/Linux box running K3s with a tunnel or port-forward for ingress.
- Cost: **$0/month**, but home networking (CGNAT, dynamic IP) usually needs Cloudflare Tunnel or similar. The forge bench already exists — a NUC-class box would work.
- Cons: reliability tied to home internet; more fiddly DNS.

### Option C — Defer; Web IDE only
- Cost: $0. Devfiles stay dormant in the repos until needed.
- Cons: no remote builds; on-device VSCodium remains mandatory for any real firmware work.

## Recommendation

**Option A** — small monthly cost, zero home-networking pain, and it makes the
Web IDE → workspace → MR pipeline real from anywhere. Fall break is the right
moment: one afternoon of setup.

## Setup checklist (once a cluster exists)

1. Provision the VM; install K3s.
2. Install the GitLab agent (Helm chart or one-liner) and register it against `kitsune-kits`.
3. Add `.gitlab/agents/workspaces/config.yaml` (above) to the kri repo.
4. Point the DNS zone at the cluster ingress; TLS via cert-manager + Let's Encrypt.
5. In GitLab: group → **Build → Workspaces** → create a workspace from any repo (devfiles are already in place).
6. Set resource limits per workspace via devfile `cpuLimit`/`memoryLimit` once real usage is known.

## Security notes

- Workspaces inherit group RBAC — only kitsune-kits members can create them.
- Container images: the GitLab workspace image is used today; a custom KRI image (rust + lua toolchains preinstalled) would speed cold starts and can be built in CI later.
- No secrets in devfiles (checked: none committed).

## Decision needed from the Architect

- [ ] Pick option A / B / C.
- [ ] Approve the monthly budget if A.
- [ ] Choose the DNS zone.
