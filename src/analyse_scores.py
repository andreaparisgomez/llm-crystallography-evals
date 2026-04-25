import pandas as pd
from pathlib import Path

# =========================
# Paths
# =========================

DATA_DIR = Path("data")

RESULTS_PATH = DATA_DIR / "results.csv"
SCORES_PATH = DATA_DIR / "scores.csv"
OUTPUT_PATH = DATA_DIR / "analysis_summary.csv"


# =========================
# Load data
# =========================

results = pd.read_csv(RESULTS_PATH)
scores = pd.read_csv(SCORES_PATH)

results.columns = results.columns.str.strip()
scores.columns = scores.columns.str.strip()


# =========================
# Add response length
# =========================

results["response_length"] = results["response_text"].apply(
    lambda x: len(str(x).split())
)


# =========================
# Merge responses + scores
# =========================

merged = results.merge(
    scores,
    on=["model", "module", "prompt_type", "prompt_id"],
    how="inner"
)


# =========================
# Core analysis
# =========================

print("\n==============================")
print("OVERALL SCORE SUMMARY")
print("==============================")
print(merged["total_score"].describe())


print("\n==============================")
print("MEAN SCORE BY PROMPT TYPE")
print("==============================")
print(
    merged.groupby("prompt_type")["total_score"]
    .mean()
    .sort_values(ascending=False)
)


print("\n==============================")
print("MEAN SCORE BY MODULE")
print("==============================")
print(
    merged.groupby("module")["total_score"]
    .mean()
    .sort_values(ascending=False)
)


print("\n==============================")
print("AVERAGE RESPONSE LENGTH BY PROMPT TYPE")
print("==============================")
print(
    merged.groupby("prompt_type")["response_length"]
    .mean()
    .sort_values(ascending=False)
)


print("\n==============================")
print("AVERAGE RESPONSE LENGTH BY MODULE")
print("==============================")
print(
    merged.groupby("module")["response_length"]
    .mean()
    .sort_values(ascending=False)
)


print("\n==============================")
print("RESPONSE LENGTH / SCORE CORRELATION")
print("==============================")
print(merged[["response_length", "total_score"]].corr())


print("\n==============================")
print("CITATION FLAG COUNTS")
print("==============================")
if "citation_flag" in merged.columns:
    print(merged["citation_flag"].value_counts())
else:
    print("citation_flag column not found.")


print("\n==============================")
print("LOWEST SCORING RESPONSES")
print("==============================")
print(
    merged[["prompt_id", "module", "prompt_type", "total_score", "notes"]]
    .sort_values("total_score")
    .head(5)
)


print("\n==============================")
print("HIGHEST SCORING RESPONSES")
print("==============================")
print(
    merged[["prompt_id", "module", "prompt_type", "total_score", "notes"]]
    .sort_values("total_score", ascending=False)
    .head(5)
)


# =========================
# Save summary tables
# =========================

summary_rows = []

# Prompt type summary
prompt_type_summary = (
    merged.groupby("prompt_type")
    .agg(
        mean_score=("total_score", "mean"),
        mean_response_length=("response_length", "mean"),
        count=("prompt_id", "count")
    )
    .reset_index()
)
prompt_type_summary["summary_type"] = "prompt_type"
prompt_type_summary = prompt_type_summary.rename(columns={"prompt_type": "category"})
summary_rows.append(prompt_type_summary)


# Module summary
module_summary = (
    merged.groupby("module")
    .agg(
        mean_score=("total_score", "mean"),
        mean_response_length=("response_length", "mean"),
        count=("prompt_id", "count")
    )
    .reset_index()
)
module_summary["summary_type"] = "module"
module_summary = module_summary.rename(columns={"module": "category"})
summary_rows.append(module_summary)


analysis_summary = pd.concat(summary_rows, ignore_index=True)

analysis_summary = analysis_summary[
    ["summary_type", "category", "mean_score", "mean_response_length", "count"]
]

analysis_summary.to_csv(OUTPUT_PATH, index=False)

print(f"\n✅ Analysis summary saved to: {OUTPUT_PATH}")
