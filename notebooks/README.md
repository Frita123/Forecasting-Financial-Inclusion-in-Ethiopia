📊 Forecasting Financial Inclusion in Ethiopia

Task 1 & Task 2 Documentation

📌 Project Overview

This project analyzes the evolution and drivers of financial inclusion in Ethiopia, with a focus on Access, Usage, and enabling infrastructure. The work is structured in sequential tasks to support exploratory analysis, causal reasoning, and future impact modeling.

Task 1 focuses on data integration, cleaning, and enrichment.

Task 2 performs exploratory data analysis (EDA) and insight generation.

✅ Task 1: Data Integration & Enrichment
🎯 Objective

To create a unified, analysis-ready dataset by integrating multiple financial inclusion data sources and enriching them with structural metadata.

🔧 Key Steps

Loaded and standardized raw datasets from surveys, operator reports, and policy sources

Harmonized indicator names, units, and time formats

Classified records into:

Observations

Events

Impact links

Enriched data with:

Financial inclusion pillars (Access, Usage, Infrastructure)

Confidence levels

Impact direction and lag assumptions

📦 Output

### Enrichment Rationale
- Telebirr and M-Pesa user counts were added to capture usage dynamics
  not present in survey-only data.
- Impact links encode hypothesized causal relationships for modeling,
  not confirmed causality.
- Events provide temporal anchors for interpreting trend shifts.

Enriched dataset:

data/processed/ethiopia_fi_unified_data_enriched.csv

✔ Key Outcome

A clean, structured dataset enabling:

Time-series analysis

Cross-pillar comparison

Future causal and forecasting models

📈 Task 2: Exploratory Data Analysis & Insights
🎯 Objective

To analyze patterns, trends, and constraints in financial inclusion across time and population segments in Ethiopia.

🔍 Analyses Performed

Dataset composition and temporal coverage

Data quality and confidence assessment

Access analysis (Account ownership trends & growth rates)

Gender gap analysis

Usage analysis (Telebirr, M-Pesa adoption)

Registered vs active account usage

Infrastructure enablers (smartphones, 4G coverage)

Event overlay analysis (policy & market milestones)

Correlation analysis between indicators

🧠 Key Insights

Mobile money strongly increases usage, but not formal account ownership

Account ownership growth slowed despite rapid digital wallet adoption

Persistent gender gap in financial access

Infrastructure lags constrain active and deep usage

Access appears more policy-constrained than demand-constrained

📌 Key Output

Insight-driven visualizations and tables supporting hypotheses for impact modeling
