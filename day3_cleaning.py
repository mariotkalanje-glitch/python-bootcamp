import pandas as pd

# 1. Create a messy dataset with missing values (None)
messy_data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": (1200, 25, None, 300, 50),
    "Units_Sold": (5, 40, 15, None, 20)
}

df = pd.DataFrame(messy_data)
print("--- Original Messy Table ---")
print(df)

# 2. Option A: Drop any row that has a missing value
clean_dropped = df.dropna()
print("\n--- Cleaned Table (Dropped Rows with Missing Values) ---")
print(clean_dropped)

# 3. Option B: Fill missing numbers with 0 instead of deleting the row
clean_filled = df.fillna(0)
print("\n--- Cleaned Table (Filled Missing Values with 0) ---")
print(clean_filled)

# 4. Filter rows where Price is greater than 100
expensive_items = clean_filled[clean_filled["Price"] > 100]
print("\n--- Filtered Table (Price > 100) ---")
print(expensive_items)

# 5. Filter rows where Category is "Accessories"
accessories_only = clean_filled[clean_filled["Category"] == "Accessories"]
print("\n--- Filtered Table (Category: Accessories) ---")    
print(accessories_only)

# 6. Group by Category and sum the Units_Sold for each group
category_summary = clean_filled.groupby("Category")["Units_Sold"].sum()
print("\n--- Total Units Sold by Category ---")
print(category_summary)

# 7. Export the cleaned table to a final CSV file
clean_filled.to_csv("cleaned_sales_data.csv", index=False)
print("\nSaved cleaned_sales_data.csv successfully!")

