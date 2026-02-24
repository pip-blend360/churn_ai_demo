
# From Vibe Coding to Real AI‑Assisted Data Science

---

## Slide 1 — Title
**From Vibe Coding to Real AI‑Assisted Data Science**

---

## Slide 2 — The Hype
You've seen demos where someone types one sentence and AI builds a model.

Let's try it.

Prompt:
> Train a churn prediction model using this dataset.

---

## Slide 3 — Reality Check
Would you trust this model?

Problems:
- No validation
- Leakage risk
- Random preprocessing
- No reproducibility

**Vibe coding looks impressive — but it guesses.**

---

## Slide 4 — Why AI Fails
AI doesn't understand your project.  
It only sees the context you give it.

**Formula**

Quality = Relevant Context ÷ Total Context

---

## Slide 5 — Key Insight
AI success is NOT prompting skill.

**It’s context control.**

### Three Layers of Context

| Layer         | Question it answers       |
| ------------- | ------------------------- |
| Always loaded | What must always be true? |
| On-demand     | What might be needed?     |
| Discoverable  | What exists if I look?    |


---

## Slide 6 — How Models Read Code
Myth: AI reads your whole repo.  
Reality: It reads (most) files *on demand.*

Demo prompt:
> What files have you read so far?

Then:
> Read src/train.py and explain it.

**It’s not loaded. It’s looked up.**

---

## Slide 7 — Always Loaded Context -- Give the AI Rules

### Always Loaded Context - use AGENTS.md.
* Most other models automatically read AGENTS.md  -- AGENTS.md is becoming a standard.
* **Claude** automatically reads CLAUDE.md -- if you are using claude, point CLAUDE.md to AGENTS.md.

Create: AGENTS.md

Add:

- Split data before preprocessing  
- Prevent target leakage  
- Use sklearn pipelines  
- Metric = ROC‑AUC  

Commit to GitHub.

Run same prompt again.

**Same prompt. Better result.**

---

## Slide 8 — Principle
Short rules > long rules.

Why?

Your instructions compete with the model’s built‑in instructions.

**Minimal context = stronger control**

---

## Slide 9 — On Demand Context -- Scoped Rules by Folder
Different parts of a project need different rules.

Create:

src/features/AGENTS.md

Example rules:
- Impute missing values
- Scale numeric columns
- Encode categoricals

Claude automatically loads local rules when editing that folder.

Refer to on demand context from root AGENTS.md.

---

## Slide 10 — Mental Model
Root rules = global standards  
Folder rules = local expertise  

---

## Slide 11 — Examples Beat Instructions
Prompt:
> Build model following examples/model_template.py

Why it works:
Examples compress information better than documentation.

---

## Slide 12 — GitHub Is Shared Memory
When you commit context files:

You’re not just saving code.  
You’re saving intelligence for your team.

**Your repo becomes a shared brain for AI.**

---

## Slide 13 — Security Insight
Context files are not docs.

They are executable instructions for AI.

**Treat AGENTS.md like CI config.  
Review it in pull requests.**

---

## Slide 14 — Token Reality
Everything AI sees costs tokens:
- prompts
- history
- files
- rules
- examples

Too much context →
- slower
- worse reasoning
- higher cost

---

## Slide 15 — Live Lesson
Ask multiple unrelated questions in one session → worse output.

Start fresh session → better output.

**Rule: New task = new chat**

---

## Slide 16 — Optimization Checklist
- Start new chats often
- Keep AGENTS.md small
- Scope rules by folder
- Reference docs instead of pasting
- Use examples instead of explanations
- Don’t paste datasets

---

## Slide 17 — The Big Shift
Vibe coding = guessing  
Context engineering = reliable

---

## Slide 18 — Final Takeaway
The difference between AI demos and real productivity  
is NOT the model.

**It’s how you structure context.**

---

## Slide 19 — Repo Structure
project/
 ├── data/churn.csv
 ├── src/
 │    ├── train.py
 │    └── features/
 │         ├── build_features.py
 │         └── AGENTS.md
 ├── examples/model_template.py
 └── AGENTS.md

---

## Slide 20 — Closing Line
**AI isn’t magic.  
It’s a junior teammate who only knows what you show it.**
