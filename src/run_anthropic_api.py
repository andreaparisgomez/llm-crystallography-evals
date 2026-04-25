import pandas as pd
import os
import time
from anthropic import Anthropic
from dotenv import load_dotenv

# =========================
# Setup
# =========================
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("❌ API key not found. Check your .env file.")

client = Anthropic(api_key=api_key)

# The configuration below aims to approximate realistic user-facing Claude behaviour.
# It will not exactly reproduce Claude web UI responses, because the web UI may use
# different hidden system prompts, routing, and generation settings.

MODEL = "claude-3-5-sonnet-latest"
MAX_TOKENS = 2000
TEMPERATURE = 0.7

# =========================
# Load prompts
# =========================
df = pd.read_csv("data/prompts.csv")

# =========================
# Storage for results
# =========================
results = []

# =========================
# Loop through prompts
# =========================
for i, row in df.iterrows():
    prompt_id = row["prompt_id"]
    prompt_text = row["prompt_text"]

    print(f"➡️ Running {prompt_id}...")

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            messages=[
                {"role": "user", "content": prompt_text}
            ]
        )

        answer = response.content[0].text

    except Exception as e:
        print(f"❌ Failed: {prompt_id} — {e}")
        answer = f"ERROR: {e}"

    results.append({
        "model": "claude",
        "module": row["module"],
        "prompt_type": row["prompt_type"],
        "prompt_id": prompt_id,
        "response_text": answer
    })

    # Avoid rate limits
    time.sleep(1)

# =========================
# Save results
# =========================
results_df = pd.DataFrame(results)
results_df.to_csv("data/responses_anthropic.csv", index=False)

print("✅ Responses saved to data/responses_anthropic.csv")
