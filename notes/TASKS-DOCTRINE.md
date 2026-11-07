# KRI Task Doctrine — the 2026-10-31 reset

Companion to `VAULT.md`. Where the Vault laws govern where notes live, these
laws govern where tasks live. Ratified by the Architect, 2026-10-31.

## The three laws of tasks

1. **Tasks live in the repos.** Every repo carries a `TASKS.md` at its root,
   versioned like code, committed like code, reviewed like code. A task that
   exists nowhere in a repo does not exist.
2. **Apple Reminders is a surface, not a home.** It displays; it does not
   originate. Completions and dates may flow back to the checkbox line.
   Nothing authored inside Reminders (or by Siri) enters a repo — stray
   captures are filed by hand or deleted, never synced.
3. **One hand on the task Ledger.** AI writes to tasks only through GitLab
   commits — attributed, versioned. No in-vault scribes.

## TASKS.md format

```markdown
# TASKS — <repo name>

## Now
- [ ] Short task — concrete detail (due 2026-11-05) `#project/kri`

## Next
- [ ] ...

## Someday
- [ ] ...
```

- Plain markdown checkboxes. Sections map 1:1 to the Reminders lists.
- One task per line; a line is a task, prose is prose. Subtasks are
  indented checkboxes.
- Tags map to lists and filters (confirm Task Hub's recognized syntax on
  first calibration, then freeze it here — same MR).
- `PROJECT-STATUS.md` remains the state of record; `TASKS.md` is the queue.

## Reminders lists

Fresh KRI lists (business **Kitsune Kits** account only):
`Now` · `Next` · `Someday` · `Conventions` (con prep — AWA lives here).
Personal account and personal lists are never written.

## Freshness ritual (after each forge session)

Re-scan the vault in Task Hub, confirm the account indicator reads
*Kitsune Kits*, and commit any checked-off tasks from the session.

## Task Hub scoping

- Desktop-only plugin: Mac only. The iPad keeps Working Copy — task edits
  there are plain markdown edits, committed like any note.
- Account selector: **Kitsune Kits only.** If it ever shows personal account
  data, stop and re-scope.
- Point its filters at the four lists and the vault's `TASKS.md` files.
- Edit discipline: checkbox lines and dates only. A tool that rewrites
  prose gets confiscated at the door.
- First calibration: note which date/tag syntax it recognizes, freeze the
  template format in the same MR that lands the doctrine.