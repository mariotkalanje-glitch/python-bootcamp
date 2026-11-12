# 1. Import the pandas tool and give it a short nickname 'pd'
import pandas as pd
# 2. Create a dictionary where each key is a column name, and each list holds the rows
sales_data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [1200, 25, 75, 300],
    "Units_Sold": [5, 40, 15, 10]
}
# 3. Convert that dictionary into a Pandas DataFrame table
df = pd.DataFrame(sales_data)

# 4. Display the table
print(df)

# View only the first 2 rows
print(df.head(2))

# View column names, data types, and missing value counts
print(df.info())

# View automatic math statistics (averages, minimums, maximums)
print(df.describe())

# Create a brand-new column by multiplying two existing columns
df["Total_Revenue"] = df["Price"] * df["Units_Sold"]
print(df)

