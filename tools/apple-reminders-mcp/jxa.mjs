//
// jxa.mjs / apple-reminders-mcp / KRI
// JXA bridge to macOS Apple Reminders. Self-contained serialized functions; no shell quoting.
// Copyright (c) 2026 Kitsune Kits. All rights reserved.
//

import { execFile } from "node:child_process";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);

// MARK: - JXA execution

/**
 * Executes a JXA function against the Reminders app and parses its JSON output.
 * The function's source is serialized with Function.prototype.toString and its
 * arguments are spliced in as a JSON literal, so no shell quoting is involved.
 * macOS will prompt for Automation + Reminders access on first run — approve it.
 */
function callJxa(fn, args) {
  const src = "(" + fn.toString() + ")(" + JSON.stringify(args || {}) + ")";
  return execFileAsync("/usr/bin/osascript", ["-l", "JavaScript", "-e", src], {
    maxBuffer: 16 * 1024 * 1024,
  }).then(function (r) { return JSON.parse(r.stdout); });
}

// MARK: - JXA bodies (must each be fully self-contained)

function listAccountsJXA() {
  const Rem = Application("Reminders");
  return JSON.stringify(Rem.accounts().map(function (a) {
    return { id: a.id(), name: a.name() };
  }));
}

function listListsJXA(args) {
  const Rem = Application("Reminders");
  const out = [];
  const accounts = args.accountName
    ? Rem.accounts().filter(function (a) { return a.name() === args.accountName; })
    : Rem.accounts();
  accounts.forEach(function (a) {
    a.lists().forEach(function (l) {
      out.push({ id: l.id(), name: l.name(), account: a.name(), count: l.reminders().length });
    });
  });
  return JSON.stringify(out);
}

function listRemindersJXA(args) {
  const Rem = Application("Reminders");
  const out = [];
  const accounts = args.accountName
    ? Rem.accounts().filter(function (a) { return a.name() === args.accountName; })
    : Rem.accounts();
  accounts.forEach(function (a) {
    const lists = args.listName
      ? a.lists().filter(function (l) { return l.name() === args.listName; })
      : a.lists();
    lists.forEach(function (l) {
      let rems = l.reminders();
      if (args.completed !== null && args.completed !== undefined) {
        rems = rems.filter(function (r) { return r.completed() === args.completed; });
      }
      rems.slice(0, args.limit).forEach(function (r) {
        const d = r.dueDate();
        out.push({
          id: r.id(),
          name: r.name(),
          notes: r.body() || "",
          completed: r.completed(),
          dueDate: d ? new Date(d).toISOString() : null,
          account: a.name(),
          list: l.name(),
        });
      });
    });
  });
  return JSON.stringify(out);
}

function createReminderJXA(args) {
  const Rem = Application("Reminders");
  let target;
  if (args.accountName && args.listName) {
    const acc = Rem.accounts().filter(function (a) { return a.name() === args.accountName; })[0];
    if (!acc) throw new Error("account not found: " + args.accountName);
    target = acc.lists().filter(function (l) { return l.name() === args.listName; })[0];
    if (!target) throw new Error("list not found in account " + args.accountName + ": " + args.listName);
  } else if (args.listName) {
    target = Rem.lists.byName(args.listName);
  } else if (args.accountName) {
    const acc = Rem.accounts().filter(function (a) { return a.name() === args.accountName; })[0];
    if (!acc) throw new Error("account not found: " + args.accountName);
    const lists = acc.lists();
    target = lists.length ? lists[0] : Rem.defaultList();
  } else {
    target = Rem.defaultList();
  }
  const r = Rem.Reminder({ name: args.title });
  if (args.notes) r.body = args.notes;
  if (args.dueDate) r.dueDate = new Date(args.dueDate);
  target.reminders.push(r);
  const d = r.dueDate();
  return JSON.stringify({
    id: r.id(),
    name: r.name(),
    account: args.accountName || null,
    list: target.name(),
    dueDate: d ? new Date(d).toISOString() : null,
  });
}

function completeReminderJXA(args) {
  const Rem = Application("Reminders");
  const accounts = args.accountName
    ? Rem.accounts().filter(function (a) { return a.name() === args.accountName; })
    : Rem.accounts();
  for (let i = 0; i < accounts.length; i++) {
    const lists = accounts[i].lists();
    for (let j = 0; j < lists.length; j++) {
      const rems = lists[j].reminders();
      for (let k = 0; k < rems.length; k++) {
        if (rems[k].id() === args.id) {
          rems[k].completed = true;
          return JSON.stringify({ ok: true });
        }
      }
    }
  }
  return JSON.stringify({ ok: false, error: "not found" });
}

function deleteReminderJXA(args) {
  const Rem = Application("Reminders");
  const accounts = args.accountName
    ? Rem.accounts().filter(function (a) { return a.name() === args.accountName; })
    : Rem.accounts();
  for (let i = 0; i < accounts.length; i++) {
    const lists = accounts[i].lists();
    for (let j = 0; j < lists.length; j++) {
      const rems = lists[j].reminders();
      for (let k = 0; k < rems.length; k++) {
        if (rems[k].id() === args.id) {
          const owner = lists[j].name();
          Rem.delete(rems[k]);
          return JSON.stringify({ ok: true, deletedFrom: owner });
        }
      }
    }
  }
  return JSON.stringify({ ok: false, error: "not found" });
}

// MARK: - Public bridge API

export function listAccounts() { return callJxa(listAccountsJXA, {}); }
export function listLists(args) { return callJxa(listListsJXA, args || {}); }
export function listReminders(args) { return callJxa(listRemindersJXA, args || {}); }
export function createReminder(args) { return callJxa(createReminderJXA, args || {}); }
export function completeReminder(args) { return callJxa(completeReminderJXA, args || {}); }
export function deleteReminder(args) { return callJxa(deleteReminderJXA, args || {}); }
