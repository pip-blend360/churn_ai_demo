# Churn Prediction (AI Pair-Programming Demo)

This repo is intentionally **small and data-science friendly**. It's built for a live demo showing how a coding agent (Claude CLI) becomes dramatically more useful when you provide **lightweight project context** in `CLAUDE.md`.

## What you'll do in the demo
1. Run a baseline churn model on a messy CSV (`data/usage_churn.csv`)
2. Generate a short metrics report in `reports/`
3. (Optional) Run quick EDA plots

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

python src/train.py
python src/eda.py
```

Outputs:
- `reports/metrics.json`
- `reports/metrics.md`
- `models/churn_model.joblib`

## Notes
- The dataset includes **intentional messiness** (missing-value codes, wrong dtypes) to make the demo realistic.
- The dataset also includes **leakage columns** (`account_status`, `cancel_reason_code`). Your model must **not** use them.
