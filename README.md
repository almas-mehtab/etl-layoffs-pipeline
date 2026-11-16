# etl-layoffs-pipeline
# ETL Validation Pipeline — Tech Layoffs Data

An automated Python ETL validation pipeline built on real-world tech layoffs data (2020–2024).

## What This Project Does

This pipeline ingests raw layoffs data, runs a series of data quality checks, and outputs a structured validation report — simulating the kind of ETL validation work done in enterprise data environments.

**Validation checks include:**
- Row count verification
- Null value detection across all columns
- Duplicate record detection
- Schema and data type validation
- Key business insights (top companies and industries by layoffs)

## Tools & Technologies

- Python 3
- Pandas
- VS Code
- Git & GitHub

## Dataset

- Source: [Layoffs 2022 Dataset — Kaggle](https://www.kaggle.com/datasets/swaptr/layoffs-2022)
- 4,644 records across 3,003 companies and 67 countries

## Key Findings

- 1,614 rows had missing layoff numbers — a real data quality issue in the source
- Top companies by total layoffs: Amazon, Intel, Meta, Microsoft, Dell
- Most impacted industries: Retail, Hardware, Consumer, Transportation

## How to Run

1. Clone the repository
2. Install dependencies: `pip install pandas`
3. Run the pipeline: `python etl_validator.py`

## Author

Almas M Mehtab — Data & ML Professional | Toronto, Canada  
[LinkedIn](https://www.linkedin.com/in/almas-m-mehtab-003460199/)
