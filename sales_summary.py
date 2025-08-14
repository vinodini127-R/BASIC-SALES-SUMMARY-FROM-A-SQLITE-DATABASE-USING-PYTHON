import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# 2. SQL query to calculate total quantity and revenue
query = """
SELECT
    "Product Name" AS product,
    SUM("Units Sold") AS total_qty,
    SUM("Units Sold" * "Unit Price") AS revenue
FROM sales
GROUP BY "Product Name"
ORDER BY revenue DESC
"""


# 3. Load results into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# 4. Print sales summary
print("SALES SUMMARY:\n")
print(df)

# 5. Plot Revenue by Product
plt.figure(figsize=(10, 6))
plt.bar(df['product'], df['revenue'], color='skyblue')
plt.title("REVENUE BY PRODUCT", fontsize=14)
plt.xlabel("PRODUCT", fontsize=12)
plt.ylabel("REVENUE", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save and show chart
plt.savefig("sales_chart.png")
plt.show()

# 6. Close connection
conn.close()


