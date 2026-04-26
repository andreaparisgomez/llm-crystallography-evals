# LLM Crystallography Evaluations

Can a language model reason like a crystallographer?

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

This project is designed as a **hard-to-game evaluation framework**, probing where an LLM can reason correctly and where it fails in domain-specific scientific tasks.

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

### 5. Data & Outputs

The repository includes:

- raw prompts and model responses  
- manually curated scoring data  
- aggregated performance summaries  

All processed data is available in the `data/` folder.

---

## Key Findings

- **Structured prompts outperform open-ended prompts**  
  → LLM reasoning improves when constrained  

- **Performance varies by domain**  
  → Peak position problems were significantly harder  

- **Verbosity does not strongly correlate with quality**  
  → Longer responses ≠ better reasoning  

- **Strong performance in diagnostic reasoning**  
  → Weakness in precise physical and geometric interpretation
  
---

## Interpretation

These results suggest that LLM performance in technical domains is highly sensitive to **problem framing**.

- Structured prompts (e.g. prioritisation, critique) guide the model toward **explicit reasoning pathways**, improving performance
- Open-ended prompts lead to **diffuse, less focused explanations**, even when the underlying knowledge is present
- Performance variability across domains (e.g. weaker results on peak positions) highlights limitations in **precise physical reasoning**, particularly where geometric or instrumental effects dominate
- The weak correlation between response length and score indicates that **verbosity is not a reliable proxy for reasoning quality**

Overall, the results suggest that LLMs are more effective as **guided reasoning systems** than as fully autonomous experts in specialised scientific domains.

---

## Future Work

This project focuses on a single model (Claude) and a limited set of crystallography tasks. Several extensions would improve robustness and generality:

- **Multi-model comparison**  
  Evaluate performance across different LLMs (e.g. GPT, Gemini) to compare reasoning patterns

- **Scaling the dataset**  
  Increase the number and diversity of prompts to reduce variance and improve statistical confidence

- **Automated evaluation**  
  Develop a semi-automated scoring pipeline to reduce manual bias while preserving rubric quality

- **Prompt sensitivity analysis**  
  Systematically vary prompt phrasing to measure robustness of model reasoning

- **Deeper error analysis**  
  Categorise failure modes (e.g. conceptual misunderstanding vs reasoning gaps vs overgeneralisation)

- **Extension to other scientific domains**  
  Apply the same evaluation framework to chemistry, physics, or materials science tasks

These directions would move the project toward a more general framework for evaluating LLM reasoning in technical domains.

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

## Author

Andrea Paris

Chemistry PhD | Data Engineering & AI Evaluation
