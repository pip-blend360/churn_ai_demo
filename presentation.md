# Coding with AI Agents for Data Scientists
### From Prompting → Collaborating

---

## Opening

AI can already write code.

But the real opportunity isn’t getting code from AI.

It’s learning how to *work with* AI to solve problems faster, explore ideas sooner, and remove friction from your workflow.

Today is about that shift:

**from asking AI for code**
→ **to collaborating with AI as a partner**

By the end, you’ll know how to make AI dramatically more useful for real data science work.


---

## Demo Introduction — Example we are using

**Problem:**
Predict whether a customer will churn based on product usage data.

**Dataset:**
A CSV file of user activity metrics, including:

* usage behavior
* support tickets
* subscription plan
* tenure

But — just like real-world data — it’s messy:

* missing values are encoded inconsistently
* some columns have wrong data types
* a few columns leak the answer if used incorrectly

**Goal:**
Build a baseline churn model that:

* cleans the data properly
* avoids leakage
* trains a model
* outputs ROC-AUC

We’ll do this twice:

1. without giving the AI context
2. after giving it a small project instruction file

Same prompt. Same model. Different results.

---

**What this demo is really about**

This isn’t a modeling tutorial. It’s a workflow tutorial.

You’ll see how small amounts of structured context can dramatically improve how an AI coding agent performs.

The takeaway:

> The quality of AI output depends more on context than prompting.

---

# Part 1 — Why Context Matters 

## Prompt vs Context

### Prompt = What you want done

Prompts describe the task.

Examples:

* Train a churn model
* Plot feature importance
* Clean this dataset

Prompts should change every time you ask for something new.

---

### Context = What must always be true

Context defines the environment the task happens in.

Examples:

* Target column is `churned`
* Metric is ROC-AUC
* Never use `cancellation_date`
* Missing values encoded as `-1`
* Use sklearn only

Context should *not* change between prompts.

---

### Why They Should Be Separate

If you mix context into prompts:

* prompts get long
* rules get forgotten
* mistakes increase
* performance drops

If you separate them:

* prompts stay short
* rules stay consistent
* results improve
* workflows scale

---

### One-Line Rule

> Prompts tell the AI what to do.
> Context tells the AI how the world works.

---

## Context Is Expensive

Everything you give an AI is converted into **tokens**. Tokens = memory space and money.
More context is not always better.

---

## The Tradeoff

You want the agent to have:

* enough context to be correct
* not so much that it gets overloaded

This is exactly the same problem humans have when learning a new project.

Too little info → mistakes
Too much info → confusion

---

## Layered Context

Instead of dumping everything into one prompt, we structure context into layers.

Each layer answers a different question:

| Layer         | Question it answers       |
| ------------- | ------------------------- |
| Always loaded | What must always be true? |
| On-demand     | What might be needed?     |
| Discoverable  | What exists if I look?    |

---

## Layer 1 — Always-Loaded Context 

This is a file that tells the agent the basics about the project

* what this project is
* what data looks like
* what tools to use
* what not to do

Example:

```
Target column: churned
Metric: ROC-AUC
Never use columns:
- last_login_date
- cancellation_date
- account_status_encoded
Use sklearn 
```

Small + precise beats long + detailed.

---

## Layer 2 — On-Demand Context

Information the agent loads only when needed:

* helper scripts
* reusable instructions
* domain rules

Examples in data science:

* feature engineering standards
* modeling checklist
* plotting guidelines

Key principle:

> Don’t load everything. Load only what’s needed.

---

## Layer 3 — Discoverable Context

Files the agent can read if relevant:

* README
* dataset
* schemas
* notebooks
* configs

Only read if needed.

---

## Mental Model

Think like onboarding a new teammate.

You wouldn’t dump every document on them immediately.

You’d give:

1. Orientation
2. Instructions when needed
3. Docs they can reference

That’s exactly how agents work.

---

## AGENTS.MD

The standard has become to put always loaded content into **AGENTS.MD**. Most models will automatically read this file. 

Claude does not. It automatically reads **CLAUDE.MD**. I recommend that you keep all of your always loaded content in AGENTS.MD and refer to it in CLAUDE.MD
