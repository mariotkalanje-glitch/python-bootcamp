markdown
# 🐍 3-Day Python Data Analytics Bootcamp: Complete Master Summary

This master document recaps every core concept, command, and workflow built from scratch across Days 1, 2, and 3, along with Git/GitHub version control integration in Visual Studio Code.

---

## 🛠️ Developer Environment & GitHub Workflow
* **Code Editor:** Visual Studio Code configured with Python interpreter (`Python 3.15` / `base` environment).
* **Version Control (`Git` & `GitHub`):** Linked local `python-bootcamp` workspace directly to a public GitHub repository (`mariotkalanje-glitch/python-bootcamp`).
* **Daily Backup Cycle:** Stage Changes (`+`) ➔ Enter Commit Message ➔ **Commit** ➔ **Sync Changes** (`Push`).

---

## 📅 Day 1: Python Core Foundations
*Scripts: `practice1.py`, `practice2.py`*

### 1. Variables, Comments & Data Types
* **Variables (`=`):** Labeled storage boxes in computer memory (e.g., `user_name = "Mariot"`).
* **Comments (`#`):** Plain-English notes ignored by Python during execution.
* **Strings (`str`):** Text wrapped in quotation marks (`"Mwanza"`).
* **Integers (`int`):** Whole numbers without decimals used for counting and math (`1`, `25`).

### 2. Formatted Strings (`f-strings`)
* Prefixing a string with `f` and wrapping variable names in curly braces `{}` injects live values directly into sentences:
  ```python
  print(f"Welcome back {user_name}, today is day {bootcamp_day}!")
  ```

### 3. Lists & Zero-Indexing
* **Lists (`[]`):** Ordered collections of items separated by commas (`my_friends = ["Margeson", "Fred", "Kalanje"]`).
* **Zero-Indexing:** Python counts positions starting at **`0`** (`0` = 1st item, `1` = 2nd item, `2` = 3rd item). Requesting an index beyond the list length triggers an `IndexError: list index out of range`.

### 4. Control Flow (`for` Loops)
* Automates repetitive tasks across every item in a collection using a trailing colon `:` and strict **4-space indentation**:
  ```python
  for friend in my_friends:
      print(f"Hello {friend}! Welcome to Python Bootcamp.")
  ```

### 5. Dictionaries (Key-Value Pairs)
* **Dictionaries (`{}`):** Stores connected pairs of labeled data (`Key: Value`) separated by commas:
  ```python
  student = {"name": "Mariot", "city": "Mwanza", "day": 1}
  print(student["city"])  # Outputs: Mwanza
  ```

### 6. Decision Logic (`if / elif / else`)
* Evaluates conditions (`==` for equal to, `>` for greater than, `<` for less than) to steer the program down specific indented paths:
  ```python
  if student["day"] == 1:
      print("Welcome to Day 1: Foundations!")
  elif student["day"] == 2:
      print("Welcome to Day 2: Pandas DataFrames!")
  else:
      print("Welcome to Day 3: Data Cleansing!")
  ```

---

## 📅 Day 2: Introduction to Pandas DataFrames
*Scripts: `day2_pandas.py`, `day2_csv.py` | Output: `sales_report.csv`*

### 1. Package Management & Importing
* **Installation:** Installed Pandas via terminal using `pip install pandas`.
* **Importing:** Loaded Pandas under its standard industry nickname `pd` (`import pandas as pd`).

### 2. Building & Inspecting DataFrames
* **DataFrames (`pd.DataFrame()`):** Converts dictionaries of lists into 2-dimensional tables with rows and columns.
* **`.head(n)`:** Previews the first `n` rows of a dataset (defaults to 5).
* **`.info()`:** Displays row counts, column names, non-null counts, and data types (`object` for text, `int64` for integers).
* **`.describe()`:** Generates automatic summary statistics (`count`, `mean`, `std`, `min`, `max`) for numeric columns.

### 3. Vectorized Column Math
* Performs calculations across an entire column at once without loops:
  ```python
  df["Total_Revenue"] = df["Price"] * df["Units_Sold"]
  ```

### 4. CSV File Handling (Two-Way Spreadsheet Bridge)
* **Exporting (`.to_csv()`):** Saves a DataFrame onto disk as a spreadsheet (`df.to_csv("sales_report.csv", index=False)`). Using `index=False` prevents saving row numbers as an extra column.
* **Importing (`pd.read_csv()`):** Loads an external CSV spreadsheet into a Python variable (`loaded_df = pd.read_csv("sales_report.csv")`).

---

## 📅 Day 3: Dataset Cleansing & Restructuring
*Script: `day3_cleaning.py` | Output: `cleaned_sales_data.csv`*

### 1. Handling Missing Values (`None` / `NaN`)
* **`.dropna()`:** Removes any row containing a missing (`NaN`) value.
* **`.fillna(value)`:** Preserves all rows by replacing missing `NaN` cells with a safe default value (e.g., `clean_filled = df.fillna(0)`).

### 2. Conditional Row Filtering
* Extracts subsets of rows matching logical rules inside square brackets:
  ```python
  expensive_items = clean_filled[clean_filled["Price"] > 100]
  accessories_only = clean_filled[clean_filled["Category"] == "Accessories"]
  ```

### 3. Grouping & Aggregating (`.groupby()`)
* Groups rows by category and calculates summary totals (similar to an Excel Pivot Table):
  ```python
  category_summary = clean_filled.groupby("Category")["Units_Sold"].sum()
  ```
### 4. Final Dataset Export
* Saved the cleaned, zero-filled dataset to disk as `cleaned_sales_data.csv` ready for sharing or visualization.