# From Prompting to Pair Programming with AI (Data Science Edition)

> Live demo: VSCode + Claude CLI using a small churn-prediction repo.

---

## 1. Why we're here
Most of us use ChatGPT like:
- “What’s the Python code to do XYZ?”
- copy/paste
- debug manually

Goal today: use an AI coding agent like a **pair programmer**.

---

## 2. The problem (simple + realistic)
We have a messy CSV: `data/usage_churn.csv`

Task:
- build a baseline churn model
- produce a small metrics report

Constraints:
- sklearn only
- avoid leakage columns (`account_status`, `cancel_reason_code`)

---

## 3. The key idea: context beats prompting
Same prompt, different results.

### Without context
Agent makes assumptions (wrong columns, leakage, wrong metric, etc).

### With a tiny “constitution”
A short file (`CLAUDE.md`) that tells the agent:
- what the target is
- what to never use (leakage)
- what “good” looks like (metric, pipeline)

---

## 4. Demo plan

### Demo A — No context
1. Delete/rename `CLAUDE.md` temporarily
2. Ask Claude:
   - “Train a churn model and write a report”
3. Observe mistakes / extra back-and-forth

### Demo B — Add context
1. Restore `CLAUDE.md`
2. Ask the *same* prompt
3. Watch it produce the correct pipeline + reports

### Demo C — The one habit that matters
- Use `/clear` between unrelated tasks

---

## 5. Takeaways
- Don’t prompt harder — **provide better context**
- Keep the constitution small and stable
- Write down “gotchas” the agent gets wrong
- Clear context between tasks

---

## Appendix: Prompts to use live
- “Read the dataset and propose a baseline approach.”
- “Implement training in `src/train.py` and write metrics to `reports/metrics.md`.”
- “Do a quick EDA script and save plots to `reports/`.”
