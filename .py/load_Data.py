import pandas as pd
import sqlite3

# Load CSV files
total_sales_df = pd.read_csv("totalsales.csv")
ad_metrics_df = pd.read_csv("ad_metrics.csv")
eligibility_df = pd.read_csv("eligibility.csv")

# Connect to SQLite
conn = sqlite3.connect("ecommerce.db")

# Store DataFrames as tables
total_sales_df.to_sql("total_sales", conn, if_exists="replace", index=False)
ad_metrics_df.to_sql("ad_metrics", conn, if_exists="replace", index=False)
eligibility_df.to_sql("eligibility", conn, if_exists="replace", index=False)

conn.close()
print("Data loaded into ecommerce.db successfully!")
