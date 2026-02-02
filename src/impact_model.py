import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------
# Configuration / Constants
# ---------------------------
IMPACT_SCALE = {
    "low": 0.5,
    "medium": 1.5,
    "high": 3.0
}

DATA_PATH = "../data/processed/ethiopia_fi_unified_data_enriched.csv"
SUMMARY_CSV = "../data/processed/event_indicator_summary.csv"
MATRIX_CSV = "../data/processed/event_indicator_matrix.csv"
HEATMAP_PNG = "../reports/figures/event_indicator_heatmap.png"
VALIDATION_CSV = "../data/processed/impact_model_validation.csv"

# ---------------------------
# Functions
# ---------------------------

def load_data(file_path=DATA_PATH):
    """Load the enriched dataset"""
    df = pd.read_csv(file_path)
    return df

def extract_impact_links(df):
    """Return only the impact_link records"""
    return df[df["record_type"] == "impact_link"].copy()

def map_impact_to_numeric(impact_links):
    """Map qualitative impact magnitudes to numeric values"""
    impact_links["impact_numeric"] = impact_links["impact_magnitude"].map(IMPACT_SCALE)
    return impact_links

def create_impact_summary(impact_links, save_csv=True):
    """Create summary table of event impacts"""
    summary = impact_links[[
        "record_id",          # Event ID
        "related_indicator",  # Affected Indicator
        "impact_direction",
        "impact_magnitude",
        "impact_numeric",
        "lag_months",
        "evidence_basis",
        "notes"
    ]]
    if save_csv:
        summary.to_csv(SUMMARY_CSV, index=False)
    return summary

def build_association_matrix(impact_links, save_csv=True):
    """Pivot the impact_links to create an Event–Indicator Association Matrix"""
    matrix = impact_links.pivot_table(
        index="record_id",
        columns="related_indicator",
        values="impact_numeric",
        aggfunc="sum"
    ).fillna(0)
    if save_csv:
        matrix.to_csv(MATRIX_CSV)
    return matrix

def plot_heatmap(matrix, save_png=HEATMAP_PNG):
    """Generate a heatmap for the Event–Indicator Association Matrix"""
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".1f",
        cmap="Blues",
        linewidths=0.5
    )
    plt.title("Event–Indicator Impact Association Matrix")
    plt.xlabel("Financial Inclusion Indicators")
    plt.ylabel("Events")
    plt.tight_layout()
    if save_png:
        os.makedirs(os.path.dirname(save_png), exist_ok=True)
        plt.savefig(save_png, dpi=300)
    plt.show()

def validate_telebirr(df, impact_links, save_csv=True):
    """Simple validation against Telebirr observed account growth"""
    # Observed growth
    observed_2021 = 4.7
    observed_2024 = 9.45
    observed_growth = (observed_2024 - observed_2021) / observed_2021 * 100  # %

    # Model growth from Telebirr events
    telebirr_links = impact_links[impact_links["notes"].str.contains("Telebirr", na=False)]
    model_growth = telebirr_links["impact_numeric"].sum()

    validation = pd.DataFrame({
        "indicator": ["Mobile Money Account Ownership"],
        "observed_growth_pct": [observed_growth],
        "model_estimated_growth": [model_growth],
        "difference": [observed_growth - model_growth]
    })
    
    if save_csv:
        os.makedirs(os.path.dirname(VALIDATION_CSV), exist_ok=True)
        validation.to_csv(VALIDATION_CSV, index=False)
    
    return validation

# ---------------------------
# Main workflow (if run as script)
# ---------------------------
if __name__ == "__main__":
    print("Loading data...")
    df = load_data()
    
    print("Extracting impact links...")
    impact_links = extract_impact_links(df)
    
    print("Mapping impact magnitudes to numeric...")
    impact_links = map_impact_to_numeric(impact_links)
    
    print("Creating impact summary...")
    summary = create_impact_summary(impact_links)
    
    print("Building association matrix...")
    matrix = build_association_matrix(impact_links)
    
    print("Plotting heatmap...")
    plot_heatmap(matrix)
    
    print("Validating Telebirr impact...")
    validation = validate_telebirr(df, impact_links)
    
    print("\nValidation Results:")
    print(validation)
    print("\nTask 3 complete!")
