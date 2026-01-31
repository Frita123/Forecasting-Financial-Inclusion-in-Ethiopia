# Forecasting-Financial-Inclusion-in-Ethiopia
## Project Overview
This project analyzes financial inclusion trends in Ethiopia using enriched
survey, operator, and event-level data. It focuses on Access, Usage, and
enabling infrastructure to support downstream impact modeling.

## Repository Structure
- data/raw: Original datasets
- data/processed: Enriched and cleaned datasets
- notebooks:
  - task1_enrichment.ipynb
  - task2_eda.ipynb
- src:
  - data_loader.py: Centralized data loading with validation
  - preprocessing.py: Cleaning and feature preparation
  - eda_plots.py: Reusable visualization functions
  - utils.py: Common helpers

## Tasks Completed
- Task 1: Data enrichment (events, observations, impact links)
- Task 2: Exploratory data analysis with visual insights

## Key Insights
- Mobile money drives usage, not ownership
- Infrastructure constrains active adoption
- Gender gap persists despite digital expansion

## How to Run
1. Create a virtual environment
2. Install dependencies
3. Run notebooks or import functions from `src/`

## Next Steps
- Impact modeling
- Causal analysis using event timing
