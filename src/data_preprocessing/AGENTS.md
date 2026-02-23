Rules:
- Let me know when you are running this step
- Always inspect the dataset before acting.
- Always explain problems found in data.
- Always clean data safely (never drop columns or rows without justification).
- Never introduce data leakage.
- Always separate preprocessing from model training.
- Always output runnable Python code using pandas + scikit-learn.
- Prefer pipelines and ColumnTransformer.
- Always handle:
  missing values
  categorical encoding
  scaling numeric features
  train/test split (stratified if classification)
- If unsure about a column, ask.

Workflow you must follow:
1. Inspect dataset
2. Diagnose issues
3. Propose cleaning plan
4. Write code

Goal:
Produce clean features ready for churn classification.

Do not skip steps.
