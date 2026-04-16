# Upwork Hunt Routine

## Trigger
Schedule: Every 6 hours (or API call)

## Task
1. Read `state/config.json` for search keywords and limits.
2. Read `state/jobs.json` to know which jobs have already been seen/applied.
3. Open Upwork and search for jobs matching the keywords.
4. For each new job found:
   - Evaluate fit (skills match, budget, client rating, competition level).
   - Score 0-100 on: skill_match, budget_attractiveness, client_trust, win_probability.
   - If score >= 60, add to jobs.json with status "discovered".
   - If score >= 75 and daily apply limit not reached, draft a proposal.
5. For proposals:
   - Structure: HOOK (understand their problem) → PROOF (2-3 relevant achievements) → APPROACH (how you'd solve it) → DIFFERENTIATOR (why you) → CTA (next step).
   - 200-300 words. No template phrases. No AI mention.
   - If dry_run is true: save proposal to jobs.json but do NOT submit.
   - If dry_run is false: submit proposal on Upwork, record Connects consumed.
6. Update `state/jobs.json` with all changes.
7. Commit and push with message: `feat: hunt YYYY-MM-DD — X new jobs, Y proposals`.
8. Notify Slack with summary.

## Freelancer Profile (for proposal context)
- Name: Rintaro Matsumoto
- Experience: 23 years mission-critical engineering, C#/DirectX, 3D combat simulation
- Current stack: Python, Claude API, MCP, Playwright, FastAPI, PostgreSQL
- Education: UTokyo GCI (Machine Learning)
- Location: Japan (UTC+9)
- Tone: Confident, direct, natural. NOT sycophantic.

## Forbidden in Proposals
"I am interested in", "I am writing to", "I hope this message finds you",
"I am excited to", "I am passionate about", "look no further",
"I am the perfect candidate", "as an AI", "as a language model"
