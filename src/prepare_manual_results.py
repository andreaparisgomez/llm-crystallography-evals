import pandas as pd
from pathlib import Path

# =========================
# Load file
# =========================
data_path = Path("data/results_manual.csv")

if not data_path.exists():
    raise FileNotFoundError(f"❌ File not found: {data_path}")

df = pd.read_csv(data_path)

# =========================
# Clean columns
# =========================
df.columns = df.columns.str.strip()

# =========================
# Validation
# =========================
required_cols = [
    "model",
    "module",
    "prompt_type",
    "prompt_id",
    "response_text"
]

missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    raise ValueError(f"❌ Missing columns: {missing_cols}")

# Check empty dataset
if df.empty:
    raise ValueError("❌ Dataset is empty")

# Check missing responses
if df["response_text"].isna().any():
    raise ValueError("❌ Some response_text values are missing")

# =========================
# Success message
# =========================
print("✅ Manual results validated")
print(f"Rows: {len(df)}")
print(df.head())
