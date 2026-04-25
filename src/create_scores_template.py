import pandas as pd
import os

# =========================
# Paths
# =========================
responses_path = "data/responses_anthropic.csv"
scores_path = "data/scores_template.csv"

# =========================
# Load responses
# =========================
if not os.path.exists(responses_path):
    raise FileNotFoundError(f"Could not find {responses_path}. Run run_anthropic.py first.")

responses = pd.read_csv(responses_path)

# =========================
# Create scoring template
# =========================
scores = responses[[
    "model",
    "module",
    "prompt_type",
    "prompt_id"
]].copy()

scores["core_score"] = pd.NA
scores["bonus_score"] = pd.NA
scores["total_score"] = pd.NA
scores["citation_flag"] = 0
scores["notes"] = ""

# =========================
# Save
# =========================
scores.to_csv(scores_path, index=False)

print(f"✅ Scoring template created: {scores_path}")
print(scores.head())
