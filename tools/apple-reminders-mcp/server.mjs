//
// server.mjs / apple-reminders-mcp / KRI
// MCP server: Streamable HTTP + Keychain bearer auth + DEFAULT_ACCOUNT policy.
// Copyright (c) 2026 Kitsune Kits. All rights reserved.
//

import { config } from "dotenv";
config({ path: new URL(".env", import.meta.url).pathname });
import express from "express";
import { randomUUID } from "node:crypto";
import { execFileSync } from "node:child_process";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";
import * as jxa from "./jxa.mjs";

// MARK: - Configuration

/**
 * Loads the bearer token. Priority: MCP_TOKEN env var (dev override only),
 * then the macOS Keychain entry com.kitsunekits.reminders-mcp (production).
 * The token never lives in a plaintext file on disk.
 */
function loadToken() {
  if (process.env.MCP_TOKEN) return process.env.MCP_TOKEN;
  try {
    return execFileSync("/usr/bin/security",
      ["find-generic-password", "-w", "-s", "com.kitsunekits.reminders-mcp"],
      { encoding: "utf8" }).trim();
  } catch (e) {
    console.error("No MCP_TOKEN env var and no Keychain entry for com.kitsunekits.reminders-mcp. Run setup.sh.");
    process.exit(1);
  }
}

const PORT = process.env.PORT || 3000;
const TOKEN = loadToken();

/**
 * DEFAULT_ACCOUNT: when set in .env, every tool call is force-scoped to this
 * account (e.g. an Apple Business managed account) and calls naming a different
 * account are rejected. Server policy, not model manners.
 */
const DEFAULT_ACCOUNT = process.env.DEFAULT_ACCOUNT || null;

function resolveAccount(accountName) {
  if (DEFAULT_ACCOUNT) {
    if (accountName && accountName !== DEFAULT_ACCOUNT) {
      throw new Error("This server only operates on account '" + DEFAULT_ACCOUNT + "' (server policy).");
    }
    return DEFAULT_ACCOUNT;
  }
  return accountName || null;
}

// MARK: - Tools

const server = new McpServer({ name: "apple-reminders", version: "0.1.0" });
const asText = (data) => ({ content: [{ type: "text", text: JSON.stringify(data) }] });

server.tool(
  "list_accounts",
  "List all Reminders accounts (iCloud, On My Mac, managed/exchange accounts).",
  {},
  async () => asText(await jxa.listAccounts())
);

server.tool(
  "list_lists",
  "List Reminders lists, optionally scoped to one account.",
  { accountName: z.string().optional().describe("Account name from list_accounts. Omit for all accounts.") },
  async ({ accountName }) => asText(await jxa.listLists({ accountName: resolveAccount(accountName) }))
);

server.tool(
  "list_reminders",
  "List reminders. Optionally filter by account, list name, and completion state.",
  {
    accountName: z.string().optional().describe("Account name from list_accounts. Omit for all accounts."),
    listName: z.string().optional().describe("Exact list name, e.g. 'Groceries'. Omit for all lists."),
    completed: z.boolean().optional().nullable().describe("null=all, false=open items (default), true=done."),
    limit: z.number().int().min(1).max(500).optional().describe("Max reminders per list. Default 100."),
  },
  async ({ accountName, listName, completed, limit }) => asText(await jxa.listReminders({
    accountName: resolveAccount(accountName),
    listName: listName || null,
    completed: (completed === undefined || completed === null) ? null : completed,
    limit: limit ?? 100,
  }))
);

server.tool(
  "create_reminder",
  "Create a new reminder.",
  {
    title: z.string().describe("Reminder title."),
    notes: z.string().optional().describe("Body/notes."),
    dueDate: z.string().optional().describe("ISO 8601 date-time, e.g. 2026-09-27T09:00:00."),
    accountName: z.string().optional().describe("Target account, e.g. a managed/work account."),
    listName: z.string().optional().describe("Target list. Omit for the default list."),
  },
  async (args) => {
    try {
      return asText(await jxa.createReminder({ ...args, accountName: resolveAccount(args.accountName) }));
    } catch (e) {
      return { isError: true, content: [{ type: "text", text: "Failed: " + e.message }] };
    }
  }
);

server.tool(
  "complete_reminder",
  "Mark a reminder as completed, by its id.",
  {
    id: z.string().describe("Reminder id from list_reminders."),
    accountName: z.string().optional().describe("Scope the id lookup to one account (faster)."),
  },
  async ({ id, accountName }) => asText(await jxa.completeReminder({ id, accountName: resolveAccount(accountName) }))
);

server.tool(
  "delete_reminder",
  "Delete a reminder by its id.",
  {
    id: z.string().describe("Reminder id from list_reminders."),
    accountName: z.string().optional().describe("Scope the id lookup to one account (faster)."),
  },
  async ({ id, accountName }) => asText(await jxa.deleteReminder({ id, accountName: resolveAccount(accountName) }))
);

// MARK: - HTTP transport (bearer auth, stateless)

const app = express();
app.use(express.json({ limit: "2mb" }));

// Log every request (any method, any path) — connector wizard probes must be visible.
app.use((req, res, next) => {
  console.log(new Date().toISOString(), req.ip, req.method, req.path,
    req.headers.authorization ? "has-auth-header" : "no-auth");
  next();
});

app.post("/mcp", async (req, res) => {
  // The MCP initialize handshake carries no data and no tool access, so it is
  // exempt from bearer auth — connector validators (e.g. Mistral's wizard) ping
  // the URL before the token is entered. Everything else still requires the
  // Keychain token.
  const method = req.body && req.body.method;
  const isInitialize = method === "initialize";
  const auth = req.headers.authorization || "";
  const authorized = auth === "Bearer " + TOKEN;
  console.log(new Date().toISOString(), req.ip, req.body && req.body.method, authorized ? "auth:ok" : (isInitialize ? "auth:skip(initialize)" : "auth:FAIL"));
  if (!isInitialize && !authorized) {
    res.set("WWW-Authenticate", 'Bearer realm="kitsunekits-reminders"');
    return res.status(401).json({ error: "unauthorized" });
  }
  try {
    const transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      enableJsonResponse: false,
    });
    res.on("close", () => transport.close());
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  } catch (e) {
    if (!res.headersSent) res.status(500).json({ error: e.message });
  }
});

app.get("/mcp", (req, res) => res.status(405).json({ error: "POST only (stateless mode)" }));
app.delete("/mcp", (req, res) => res.status(405).json({ error: "stateless: no sessions to delete" }));

app.listen(PORT, "127.0.0.1", () => {
  console.log("apple-reminders-mcp listening on http://127.0.0.1:" + PORT + "/mcp");
});
