import pandas as pd
# 1. Create a sample table and save it as a CSV file on your computer
sales_data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [1200, 25, 75, 300],
    "Units_Sold": [5, 40, 15, 10]
}
df = pd.DataFrame(sales_data)
df.to_csv("sales_report.csv", index=False)

# 2. Read that CSV file back into a brand-new DataFrame
loaded_df = pd.read_csv("sales_report.csv")
print("Loaded from CSV:")
print(loaded_df)
pd.read_csv("sales_report.csv")
