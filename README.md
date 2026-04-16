# FreelanceAutoPilot-Routines

Claude Routines driven freelance automation. No Python code — just prompts and state files.

## Structure

```
prompts/          — Routine prompt definitions
  hunt-upwork.md  — Job discovery + proposal generation
  check-orders.md — Order status monitoring
  daily-report.md — Daily summary to Slack
state/            — JSON state files (the "database")
  config.json     — Platform settings, limits, toggles
  jobs.json       — Job pipeline (discovered → paid)
  clients.json    — Client profiles
  finance.json    — Revenue tracking
CLAUDE.md         — Instructions for Claude (read by every Routine)
```

## How It Works

Each Routine:
1. Clones this repo
2. Reads CLAUDE.md + state/*.json
3. Acts autonomously (search, evaluate, propose, deliver)
4. Updates state/*.json
5. Commits + pushes
6. Notifies via Slack

No server. No cron. No laptop required.
