📒 Notebooks Documentation

Financial Inclusion Analysis – Ethiopia

This folder contains all Jupyter notebooks used for data preparation, exploratory analysis, and forecasting in the Financial Inclusion project.
Each notebook corresponds to a specific task and builds logically on the previous one.

📘 task1_data_preparation.ipynb

Task 1: Data Collection & Cleaning

Purpose

Prepare raw financial inclusion datasets for analysis and modeling.

Key Steps

Load raw datasets (account ownership, digital payments)

Standardize column names and formats

Convert fiscal year labels (e.g., FY2022/23 → 2022)

Handle missing values and type conversions

Merge datasets into a unified structure

Output

Cleaned dataset saved to:

data/processed/ethiopia_fi_unified_data.csv

Why It Matters

Ensures consistency and reproducibility for all downstream analysis and forecasting.

📊 task2_eda_events.ipynb

Task 2: Exploratory Data Analysis & Event Impact

Purpose

Explore historical trends and understand how major events influenced financial inclusion.

Key Steps

Time-series visualization of key indicators

Event annotation (policy reforms, mobile money expansion, telecom competition)

Growth rate analysis

Indicator correlation analysis

Insights Generated

Digital payment usage is growing faster than account ownership

Policy and telecom-related events coincide with acceleration periods

Outputs

Analytical plots

Summary statistics

Event–indicator relationships

🔮 task3_forecasting.ipynb

Task 3: Baseline Forecasting

Purpose

Forecast financial inclusion indicators using historical trends.

Key Steps

Define forecasting targets:

Account ownership (%)

Digital payment usage (%)

Apply trend-based regression models

Generate baseline forecasts for 2025–2027

Evaluate model assumptions and limitations

Outputs

Forecast tables

Baseline projection plots

Saved forecast results for dashboard use

📈 task4_forecasting_scenarios.ipynb (if applicable)

Task 4: Scenario & Uncertainty Analysis

Purpose

Extend baseline forecasts with scenario-based adjustments and uncertainty ranges.

Key Steps

Define scenarios:

Optimistic

Base

Pessimistic

Incorporate event-driven impact multipliers

Generate scenario ranges and confidence intervals

Compare trajectories across scenarios

Outputs

Scenario forecast tables

Visualization of uncertainty bands

Written interpretation of risks and assumptions

Run notebooks in order:

task1 → task2 → task3 → task4

⚠️ Notes & Assumptions

Data availability is limited (sparse Findex points)

Forecasts are trend-based, not causal

Scenario analysis reflects assumptions, not predictions

Results are intended for strategic insight, not exact estimation

✅ Best Practice

✔ Run notebooks sequentially
✔ Do not skip Task 1 (required for all others)
✔ Outputs from forecasting notebooks feed directly into the dashboard

📌 Summary

The notebooks in this folder provide the analytical backbone of the project, moving from raw data to insights and forecasts in a clear, reproducible workflow.