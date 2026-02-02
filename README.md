Ethiopia Financial Inclusion Analytics Dashboard

Tasks 1–5 | Data Engineering, Analysis, Forecasting & Visualization

📌 Project Overview

This project analyzes financial inclusion trends in Ethiopia, focusing on account ownership and digital payment adoption.
Using historical data, event annotations, and forecasting models, the project delivers an interactive dashboard that enables stakeholders to:

Explore historical trends

Understand policy and market event impacts

Compare scenarios and forecasts

Track progress toward a 60% financial inclusion target

The project is structured and implemented across five progressive tasks, from data preparation to dashboard deployment.

✅ Task 1: Data Collection & Preparation
Objective

Collect, clean, and unify financial inclusion datasets into a single, analysis-ready format.

Key Activities

Imported raw datasets on:

Account ownership

Digital payments / mobile money usage

Standardized column names and formats

Converted fiscal year formats (e.g., FY2022/23 → 2022)

Created numeric indicator values

Saved unified dataset to:

data/processed/ethiopia_fi_unified_data.csv

Output

✔ Clean, structured dataset suitable for analysis and forecasting

📊 Task 2: Exploratory Data Analysis (EDA) & Event Impact
Objective

Explore trends and understand how major policy, telecom, and financial events influenced financial inclusion.

Key Activities

Time-series analysis of:

Account ownership

Digital payment usage

Event annotation (e.g., mobile money expansion, telecom competition)

Correlation analysis between indicators

Visual identification of growth accelerations

Key Insight

Digital payment adoption has grown faster than account ownership, indicating that usage growth outpaces access expansion.

🔮 Task 3: Forecasting & Scenario Analysis
Objective

Forecast financial inclusion trends under multiple future scenarios.

Models Used

Trend-based forecasting (baseline)

Scenario adjustments:

Optimistic

Base

Pessimistic

Forecast Horizon

2025–2027

Outputs

Account ownership forecasts

Digital payment usage forecasts

Scenario-specific projections saved as CSV:

data/processed/forecast_account_ownership.csv
data/processed/forecast_digital_payments.csv

Key Insight

Under optimistic conditions, Ethiopia approaches the 60% financial inclusion target by 2027.

📈 Task 4: Indicator Engineering & Metrics
Objective

Create derived indicators and metrics to support decision-making.

Key Indicators

Growth rates

P2P / ATM crossover indicators

Channel usage comparisons

Latest observed values vs projections

Outcome

✔ Metrics structured for direct dashboard integration
✔ Data validated and consistent across tasks

🖥 Task 5: Interactive Dashboard Development
Objective

Build an interactive dashboard for stakeholders using Streamlit.

📌 Overview

Key metric summary cards

Latest account ownership and digital payment usage

High-level insights

📈 Trends

Interactive time-series plots

Indicator selection

Historical comparisons

🔮 Forecasts

Scenario selection

Forecast visualizations (2025–2027)

Account ownership & digital payments

🎯 Inclusion Projections

Progress toward 60% inclusion target

Scenario comparison

Policy-relevant interpretations

Key Features

✅ At least 4 interactive visualizations

✅ Clear labels and explanations

✅ Scenario selectors

✅ Clean, reproducible code



🎯 Key Stakeholder Questions Answered

✔ How fast is financial inclusion growing?
✔ Which channels drive usage vs access?
✔ What is the impact of policy and telecom events?
✔ Will Ethiopia reach 60% inclusion by 2027?
✔ What scenarios enable or delay progress?


📌 Conclusion

This project delivers a data-driven, policy-relevant, and interactive analytics solution for tracking and forecasting financial inclusion in Ethiopia.
It is designed to support evidence-based decision-making by regulators, financial institutions, and development partners.