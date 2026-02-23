# Project: Churn prediction from product usage logs

## Goal
Train a baseline churn classifier from `data/usage_churn.csv` and write a small report.
For project goals see README.MD.

## Data
- Target label: `churned` (0/1)
- Identifier: `user_id` (never a feature)
- **Leakage columns (DO NOT USE as features):**
  - `account_status`
  - `cancel_reason_code`
  - 'account_status'

## Messy data rules
- Numeric columns may contain strings.
- Missing values are encoded as `-1` for some numeric columns.
- Categorical columns may contain `"unknown"`.

## Data Cleaning
- when you get to data cleaning use the SKILL 'SKILLS/data_preprocessing/data_preprocessing.md'

## Modeling constraints
- Use Python + pandas + scikit-learn only.
- Use a `Pipeline` with preprocessing:
  - numeric: impute missing values, scale
  - categorical: impute missing values, one-hot encode
- Use a simple model:
  - LogisticRegression (preferred) or RandomForestClassifier

## Evaluation
- Split: random train/valid split (80/20), stratified by `churned`
- Primary metric: ROC-AUC
- Also report: accuracy and F1

## Repo conventions
- Source code lives in `src/`
- Write artifacts to:
  - `reports/metrics.json` and `reports/metrics.md`
  - `models/churn_model.joblib`
