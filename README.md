# LLM Crystallography Evaluations

Evaluating large language model reasoning on crystallography problems using structured prompts, rubric-based scoring, and data-driven analysis.

---

## Overview

This project evaluates how well an LLM (Claude) performs on **domain-specific crystallography reasoning tasks**, focusing on:

- peak broadening interpretation  
- intensity anomalies  
- Rietveld refinement behaviour  
- peak position errors  
- doping and shared-site modelling  

Rather than relying on generic benchmarks, this project uses **expert-designed prompts and rubrics** to assess **physical reasoning quality**, not just correctness.

---

## Methodology

### 1. Prompt Design

Prompts were designed to test different reasoning modes:

- **Open-ended explanation**
- **Prioritisation / diagnosis**
- **Strategy critique**

Each prompt targets a specific crystallographic concept.

---

### 2. Data Collection

Responses were collected manually using Claude’s web interface.

- Each prompt was run in a **fresh conversation**
- This avoids context carryover and reflects **real user interaction**

---

### 3. Evaluation Framework

Responses were scored using **domain-specific rubrics** (see `docs/rubrics.md`).

Each response is evaluated across:

- problem framing  
- physical reasoning  
- prioritisation  
- refinement strategy  
- uncertainty handling  
- relevance and parsimony  

Scoring system:

- Core: **0–9**
- Bonus: **+0–2**
- Total: **/11**

---

### 4. Analysis

Results were analysed using Python:

- performance by prompt type  
- performance by crystallography domain  
- response length (verbosity)  
- correlation between verbosity and score  

See:
- `notebooks/analysis.ipynb`
- `data/` for processed outputs  

---

## Key Findings

- **Structured prompts outperform open-ended prompts**  
  → LLM reasoning improves when constrained  

- **Performance varies by domain**  
  → Peak position problems were significantly harder  

- **Verbosity does not strongly correlate with quality**  
  → Longer responses ≠ better reasoning  

- **Strong performance in diagnostic reasoning**  
  → Weakness in precise physical interpretation  

---

## Repository Structure

```
llm-crystallography-evals/
├── data/
│   ├── prompts.csv
│   ├── results_manual.csv
│   ├── scores.csv
│   ├── prompt_type_summary.csv
│   ├── module_summary.csv
│   └── correlation_matrix.csv
├── docs/
│   └── rubrics.md
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── create_prompts.py
│   ├── prepare_manual_results.py
│   ├── run_anthropic_api.py
│   ├── create_scores_template.py
│   └── analyse_scores.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Reproducibility

An API script (`run_anthropic_api.py`) is included for automated response generation.

Note:
- Results in this project were collected via the **web interface**
- API outputs may differ due to system prompts and generation settings

---

## Tech Stack

- Python
- Pandas
- Jupyter Notebook
- Anthropic API (optional)

---

## Why This Project

Most LLM evaluations focus on general benchmarks.

This project instead evaluates:

> **Can an LLM reason like a scientist in a specialised domain?**

It combines:
- domain expertise (crystallography)
- structured evaluation design
- reproducible data analysis

---

## Author

Andrea Paris 
Chemistry PhD | Data Engineering & AI Evaluation
