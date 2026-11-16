import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv("C:/Users/ahmfa/Desktop/etl_layoff_project/data/layoffs.csv")

print("=" * 40)
print("   ETL VALIDATION REPORT — LAYOFFS DATA")
print(f"   Run time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 40)

# 1. Row count
print(f"\n✅ Total rows loaded: {len(df)}")
print(f"✅ Total columns: {len(df.columns)}")
print(f"   Columns: {list(df.columns)}")

# 2. Null check
print("\n--- NULL CHECK ---")
null_counts = df.isnull().sum()
nulls_found = null_counts[null_counts > 0]
if len(nulls_found) > 0:
    print("⚠️  Null values found:")
    print(nulls_found)
else:
    print("✅ No nulls found")

# 3. Duplicate check
print("\n--- DUPLICATE CHECK ---")
dupes = df.duplicated().sum()
if dupes > 0:
    print(f"⚠️  {dupes} duplicate rows found")
else:
    print(f"✅ No duplicates found")

# 4. Schema check
print("\n--- SCHEMA CHECK ---")
print(df.dtypes)

# 5. Basic insights
print("\n--- KEY INSIGHTS ---")
print(f"Companies in dataset: {df['company'].nunique()}")
print(f"Countries covered: {df['country'].nunique()}")
print(f"\nTop 5 companies by layoffs:")
print(df.groupby('company')['total_laid_off'].sum().sort_values(ascending=False).head())
print(f"\nTop 5 industries hit:")
print(df.groupby('industry')['total_laid_off'].sum().sort_values(ascending=False).head())

print("\n" + "=" * 40)
print("   VALIDATION COMPLETE")
print("=" * 40)