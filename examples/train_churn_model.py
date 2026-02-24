"""
Churn Prediction Model Training Script
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
import joblib

# Load data
print("Loading data...")
df = pd.read_csv("data/usage_churn.csv")

print(f"Dataset shape: {df.shape}")
print(f"\nTarget distribution:\n{df['churned'].value_counts(normalize=True)}")

# Data preprocessing
print("\nPreprocessing data...")

# Handle missing values in avg_sessions_week (-1.0 indicates missing)
df["avg_sessions_week"] = df["avg_sessions_week"].replace(-1.0, np.nan)
df["avg_sessions_week"] = df["avg_sessions_week"].fillna(df["avg_sessions_week"].median())

# Features to use
feature_cols = [
    "tenure_days",
    "avg_sessions_week",
    "tickets_last_30d",
    "days_since_last_session",
    "plan_type",
    "country",
    "account_status",
]

# Encode categorical features
label_encoders = {}
categorical_cols = ["plan_type", "country", "account_status"]

for col in categorical_cols:
    le = LabelEncoder()
    df[col + "_encoded"] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# Prepare feature matrix
numeric_features = ["tenure_days", "avg_sessions_week", "tickets_last_30d", "days_since_last_session"]
encoded_features = [col + "_encoded" for col in categorical_cols]
all_features = numeric_features + encoded_features

X = df[all_features]
y = df["churned"]

print(f"\nFeatures used: {all_features}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# Train model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

# Evaluate
print("\nEvaluating model...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"\n{'='*50}")
print("MODEL PERFORMANCE")
print(f"{'='*50}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")

print(f"\n{'='*50}")
print("CLASSIFICATION REPORT")
print(f"{'='*50}")
print(classification_report(y_test, y_pred, target_names=["Not Churned", "Churned"]))

print(f"\n{'='*50}")
print("CONFUSION MATRIX")
print(f"{'='*50}")
cm = confusion_matrix(y_test, y_pred)
print(f"                Predicted")
print(f"              No     Yes")
print(f"Actual No   {cm[0][0]:4d}   {cm[0][1]:4d}")
print(f"Actual Yes  {cm[1][0]:4d}   {cm[1][1]:4d}")

# Feature importance
print(f"\n{'='*50}")
print("FEATURE IMPORTANCE")
print(f"{'='*50}")
importance_df = pd.DataFrame({
    "feature": all_features,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

for _, row in importance_df.iterrows():
    print(f"{row['feature']:30s}: {row['importance']:.4f}")

# Save model and encoders
print("\nSaving model...")
joblib.dump(model, "churn_model.joblib")
joblib.dump(label_encoders, "label_encoders.joblib")
print("Model saved to 'churn_model.joblib'")
print("Label encoders saved to 'label_encoders.joblib'")
