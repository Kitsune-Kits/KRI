# Editor Setup — Web IDE & VSCodium Parity

This repo is configured so the **GitLab Web IDE** and on-device **VSCodium** behave the same way.

## What's in the repo

- `.editorconfig` — line endings (LF), final newlines, whitespace hygiene, per-language indentation. Honored by the Web IDE and VSCodium (with the EditorConfig extension).
- `.vscode/settings.json` — workspace settings: rulers at 100, auto-save on focus change, whitespace rendering, per-language tabs (markdown).
- `.vscode/extensions.json` — recommended extensions, offered automatically when you open the repo in VS Code / the Web IDE.

Docs-only hub — no devfile; the Web IDE alone covers this repo.

## Enabling the Web IDE marketplace (per-user, one time)

1. GitLab → your avatar → **Preferences** → enable the **extension marketplace**.
2. Open this project → **Edit** → **Open in Web IDE**.
3. Install the recommended extensions from the Extensions tab (EditorConfig is the important one).
4. Command Palette: `Shift+Cmd+P` — themes, keymaps, settings sync work like desktop VS Code.

## GitLab Workspaces

For builds that the browser can't run, GitLab Workspaces give a full remote dev environment.
This repo ships a devfile (`.devfile.yaml`). See **Editor-Setup → Workspaces** notes in the kri hub for infrastructure requirements — workspace creation needs a Kubernetes cluster with a GitLab agent connected to the group.

## Limitations (honesty over hype)

- The Web IDE **cannot compile or run toolchains** — quick edits and MR reviews only.
- Real builds, flashing, and debugging stay on-device. The workspace closes the gap *if* the cluster infra is set up.
