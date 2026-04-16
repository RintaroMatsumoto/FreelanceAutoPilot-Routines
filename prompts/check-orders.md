# Order Check Routine

## Trigger
Schedule: Daily 9:00 AM JST (or API call)

## Task
1. Read `state/jobs.json` for jobs with status "applied" or "interviewing" or "contracted".
2. Check Upwork/Fiverr for status updates:
   - New messages from clients → record in jobs.json history.
   - Contract offers → update status to "contracted", add to clients.json.
   - Milestone completions → update status.
   - Payment received → update status to "paid", record in finance.json.
3. For "contracted" jobs:
   - Check if deliverables are due.
   - If work is needed, create a plan and execute (or flag for human review).
4. Update all state files.
5. Commit and push with message: `update: orders YYYY-MM-DD — status changes`.
6. Notify Slack with any items requiring human attention.

## Escalation Rules
- Budget > $2,000 → flag for human review before accepting.
- NDA or legal terms → flag for human review.
- Scope change after contract → notify immediately.
- Client communication tone is hostile → notify and suggest de-escalation.
