import sqlite3
import pandas as pd

# Load CSV into Pandas DataFrame
csv_file = "Online Sales Data.csv"  # Make sure this file is in the same folder
df = pd.read_csv(csv_file)

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("sales_data.db")

# Save DataFrame to SQLite table named 'sales'
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ CSV imported into SQLite database 'sales_data.db' with table 'sales'.")

# Check first 5 rows
print(pd.read_sql_query("SELECT * FROM sales LIMIT 5;", conn))

# Close connection
conn.close()
