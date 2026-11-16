import pandas as pd
import sqlite3
from datetime import datetime

# ── CONFIG ──────────────────────────────────────────
CSV_PATH = "C:/Users/ahmfa/Desktop/etl_layoff_project/Data/layoffs.csv"
DB_PATH  = "C:/Users/ahmfa/Desktop/etl_layoff_project/layoffs.db"
OUT_PATH = "C:/Users/ahmfa/Desktop/etl_layoff_project/outputs/validation_report.txt"

# ── LOAD CSV INTO SQLITE ─────────────────────────────
df = pd.read_csv(CSV_PATH)
conn = sqlite3.connect(DB_PATH)
df.to_sql("layoffs", conn, if_exists="replace", index=False)

report = []
report.append("=" * 45)
report.append("  ETL VALIDATION REPORT — LAYOFFS DATA")
report.append(f"  Run time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
report.append("=" * 45)

# ── SQL QUERY 1: Row count ───────────────────────────
row_count = pd.read_sql("SELECT COUNT(*) as total_rows FROM layoffs", conn)
report.append(f"\n✅ Total rows loaded: {row_count['total_rows'][0]}")

# ── SQL QUERY 2: Null check ──────────────────────────
report.append("\n--- NULL CHECK ---")
null_check = pd.read_sql("""
    SELECT 
        SUM(CASE WHEN total_laid_off IS NULL THEN 1 ELSE 0 END) as null_laid_off,
        SUM(CASE WHEN company IS NULL THEN 1 ELSE 0 END) as null_company,
        SUM(CASE WHEN industry IS NULL THEN 1 ELSE 0 END) as null_industry,
        SUM(CASE WHEN country IS NULL THEN 1 ELSE 0 END) as null_country
    FROM layoffs
""", conn)
report.append(str(null_check))

# ── SQL QUERY 3: Duplicate check ────────────────────
report.append("\n--- DUPLICATE CHECK ---")
dupes = pd.read_sql("""
    SELECT company, COUNT(*) as count 
    FROM layoffs 
    GROUP BY company 
    HAVING COUNT(*) > 1
    ORDER BY count DESC
    LIMIT 5
""", conn)
report.append(f"Companies with multiple entries (top 5):")
report.append(str(dupes))

# ── SQL QUERY 4: Top companies by layoffs ───────────
report.append("\n--- TOP 5 COMPANIES BY LAYOFFS ---")
top_companies = pd.read_sql("""
    SELECT company, SUM(total_laid_off) as total_laid_off
    FROM layoffs
    WHERE total_laid_off IS NOT NULL
    GROUP BY company
    ORDER BY total_laid_off DESC
    LIMIT 5
""", conn)
report.append(str(top_companies))

# ── SQL QUERY 5: Top industries ─────────────────────
report.append("\n--- TOP 5 INDUSTRIES HIT ---")
top_industries = pd.read_sql("""
    SELECT industry, SUM(total_laid_off) as total_laid_off
    FROM layoffs
    WHERE total_laid_off IS NOT NULL
    GROUP BY industry
    ORDER BY total_laid_off DESC
    LIMIT 5
""", conn)
report.append(str(top_industries))

report.append("\n" + "=" * 45)
report.append("  VALIDATION COMPLETE")
report.append("=" * 45)

# ── PRINT TO SCREEN ──────────────────────────────────
for line in report:
    print(line)

# ── SAVE TO FILE ─────────────────────────────────────
with open(OUT_PATH, "w") as f:
    f.write("\n".join(report))

print(f"\n📄 Report saved to: {OUT_PATH}")

conn.close()