import pandas as pd
import os

# Create data folder 
os.makedirs("data", exist_ok=True)

prompts = [

    # =========================
    # 1. PEAK BROADENING
    # =========================
    {
        "module": "peak_broadening",
        "prompt_type": "open_ended",
        "prompt_id": "PB_01",
        "prompt_text": """A Rietveld refinement of PXRD data shows:

- Peak broadening that increases with 2θ
- Good agreement in peak positions
- Instrumental broadening has been accounted for

What are the most likely causes of this behaviour?"""
    },
    {
        "module": "peak_broadening",
        "prompt_type": "prioritisation",
        "prompt_id": "PB_02",
        "prompt_text": """A PXRD refinement shows peak broadening increasing with 2θ. Multiple factors may contribute to peak broadening.

Which is the most likely dominant cause in this case, and why?"""
    },
    {
        "module": "peak_broadening",
        "prompt_type": "strategy_critique",
        "prompt_id": "PB_03",
        "prompt_text": """A PXRD refinement shows peak broadening increasing with 2θ. A researcher decides to begin by refining crystallite size and profile parameters to improve the fit.

Is this an appropriate approach? Why or why not?"""
    },

    # =========================
    # 2. INTENSITY ANOMALY
    # =========================
    {
        "module": "intensity_anomaly",
        "prompt_type": "open_ended",
        "prompt_id": "IA_01",
        "prompt_text": """A series of isostructural, same-phase materials shows broadly similar PXRD patterns.
One sample displays a single unusually sharp and significantly more intense reflection at ~30° 2θ, while the rest of the pattern remains consistent with the series.

What are the most likely causes of this anomaly?"""
    },
    {
        "module": "intensity_anomaly",
        "prompt_type": "prioritisation",
        "prompt_id": "IA_02",
        "prompt_text": """A series of isostructural, same-phase materials shows broadly similar PXRD patterns.
One sample displays a single unusually sharp and significantly more intense reflection at ~30° 2θ.

Possible explanations include preferred orientation, a minor impurity phase, or differences in local ordering.

Which is the most likely cause, and why?"""
    },
    {
        "module": "intensity_anomaly",
        "prompt_type": "strategy_critique",
        "prompt_id": "IA_03",
        "prompt_text": """A researcher concludes that the anomalous peak arises from a new crystalline phase and proceeds to model the system as multiphase.

Is this a reasonable interpretation? Why or why not?"""
    },

    # =========================
    # 3. NON-CONVERGENCE
    # =========================
    {
        "module": "non_convergence",
        "prompt_type": "open_ended",
        "prompt_id": "NC_01",
        "prompt_text": """A Rietveld refinement fails to converge despite a reasonable starting model and acceptable data quality.

What are the most likely causes of this behaviour?"""
    },
    {
        "module": "non_convergence",
        "prompt_type": "prioritisation",
        "prompt_id": "NC_02",
        "prompt_text": """A Rietveld refinement fails to converge. Possible causes include an incorrect structural model, parameter correlations, or over-parameterisation.

Which is the most likely cause, and why?"""
    },
    {
        "module": "non_convergence",
        "prompt_type": "strategy_critique",
        "prompt_id": "NC_03",
        "prompt_text": """A researcher decides to refine atomic positions and thermal parameters first to improve convergence.

Is this an appropriate strategy? Why or why not?"""
    },

    # =========================
    # 4. PEAK POSITIONS
    # =========================
    {
        "module": "peak_positions",
        "prompt_type": "open_ended",
        "prompt_id": "PP_01",
        "prompt_text": """A PXRD pattern shows that peak positions are generally close to the calculated pattern, but small systematic deviations remain, particularly at higher 2θ.

What could explain these discrepancies?"""
    },
    {
        "module": "peak_positions",
        "prompt_type": "prioritisation",
        "prompt_id": "PP_02",
        "prompt_text": """Possible explanations include lattice parameter errors, sample displacement (zero shift), or structural model limitations.

Which is the most likely cause, and why?"""
    },
    {
        "module": "peak_positions",
        "prompt_type": "strategy_critique",
        "prompt_id": "PP_03",
        "prompt_text": """A researcher attempts to resolve peak position discrepancies by refining atomic positions and occupancies.

Is this an appropriate strategy? Why or why not?"""
    },

    # =========================
    # 5. DOPING / SHARED SITE
    # =========================
    {
        "module": "doping",
        "prompt_type": "open_ended",
        "prompt_id": "DS_01",
        "prompt_text": """A Rietveld refinement of a doped material with partial occupancy shows good peak positions and shapes, but systematic intensity mismatches across the pattern.

What are the most likely causes?"""
    },
    {
        "module": "doping",
        "prompt_type": "prioritisation",
        "prompt_id": "DS_02",
        "prompt_text": """Possible explanations include incorrect occupancy values, local ordering, or preferred orientation.

Which is the most likely cause, and why?"""
    },
    {
        "module": "doping",
        "prompt_type": "strategy_critique",
        "prompt_id": "DS_03",
        "prompt_text": """A researcher decides to refine occupancy and thermal parameters simultaneously to fix intensity mismatches.

Is this an appropriate strategy? Why or why not?"""
    }

]

# Convert to DataFrame
df = pd.DataFrame(prompts)

# Save to CSV
df.to_csv("data/prompts.csv", index=False)

print("✅ prompts.csv created successfully")
print(df.head())
