import pandas as pd

# ==============================================================================
# MOPO MULTI-COUNTRY LOGISTICS & INVENTORY AUDIT (SIMULATED CASE STUDY)
# Author: Mariot Margeson Kalanje | Head of Logistics & Inventory Capstone
# Data Source: Odoo 19 ERP Exports (mopo_stock_moves.csv & mopo_stock_onhand.csv)
# ==============================================================================

# 1. LOAD RAW ODOO EXPORTS
moves_df = pd.read_csv("mopo_stock_moves.csv")
onhand_df = pd.read_csv("mopo_stock_onhand.csv")

print("=== 1. RAW DATA INSPECTION ===")
print(f"Total Stock Move Rows Loaded: {len(moves_df)}")
print(f"Total Stock by Location Rows Loaded: {len(onhand_df)}\n")

# 2. DATA CLEANING & STANDARDIZATION
clean_moves = moves_df[moves_df["Status"] == "Done"].copy()
clean_moves["Quantity"] = pd.to_numeric(clean_moves["Quantity"], errors="coerce").fillna(0)

# Standard MOPO USD Unit CapEx Costs
unit_cost_map = {
    "[MOPO-BAT-50] MOPO50 Battery": 55.00,
    "[MOPO-BAT-MAX] MOPOMax Battery": 200.00,
    "[MOPO-CHG-01] MOPO Swap Charger": 28.00,
    "[MOPO-HUB-KIT] MOPO Solar Hub Kit": 980.00,
}

clean_moves["Unit_Cost_USD"] = clean_moves["Product"].map(unit_cost_map).fillna(0)
clean_moves["Move_Value_USD"] = clean_moves["Quantity"] * clean_moves["Unit_Cost_USD"]

# Helper function to extract Country & Location Tier from Odoo Location paths
def classify_location(loc_str):
    loc = str(loc_str)
    if loc.startswith("NG-WH"):
        country = "Nigeria"
    elif loc.startswith("LR-WH"):
        country = "Liberia"
    elif loc.startswith("SL-WH"):
        country = "Sierra Leone"
    elif loc.startswith("DRC-WH"):
        country = "DRC"
    else:
        country = "External / Virtual"

    if "Refurbishment" in loc:
        tier = "Refurbishment & Faulty"
    elif "Swap Hub" in loc:
        tier = "Field Swap Hub"
    elif loc.endswith("/Stock"):
        tier = "Central Warehouse"
    elif "Vendors" in loc:
        tier = "China / OEM Supplier"
    elif "Customers" in loc:
        tier = "Field Deployment / Customer"
    elif "Inventory adjustment" in loc:
        tier = "Cycle Count Adjustment"
    else:
        tier = "Other"
    return country, tier

clean_moves[["From_Country", "From_Tier"]] = clean_moves["From"].apply(
    lambda x: pd.Series(classify_location(x))
)
clean_moves[["To_Country", "To_Tier"]] = clean_moves["To"].apply(
    lambda x: pd.Series(classify_location(x))
)

def classify_move_type(row):
    if row["From_Tier"] == "China / OEM Supplier":
        return "1. Inbound Import Receipt"
    elif row["To_Tier"] == "Field Swap Hub":
        return "2. Hub Replenishment Transfer"
    elif row["To_Tier"] == "Refurbishment & Faulty":
        return "3. Reverse Logistics (RMA)"
    elif row["To_Tier"] == "Field Deployment / Customer":
        return "4. Outbound Field Deployment"
    elif row["To_Tier"] == "Cycle Count Adjustment":
        return "5. Cycle Count Audit"
    else:
        return "6. Other Internal Move"

clean_moves["Flow_Category"] = clean_moves.apply(classify_move_type, axis=1)

# 3. AUDIT CHECKS: SHRINKAGE & RMA REFURBISHMENT RATE
print("=== 2. CYCLE COUNT & SHRINKAGE AUDIT ===")
audit_moves = clean_moves[clean_moves["Flow_Category"] == "5. Cycle Count Audit"]
shrinkage = audit_moves[audit_moves["Quantity"] > 0]
print(shrinkage[["Date", "Reference", "Product", "Lot/Serial Number", "From", "Quantity", "Move_Value_USD"]].to_string(index=False))
print(f"Total Shrinkage Loss Identified: ${shrinkage['Move_Value_USD'].sum():,.2f}\n")

# 4. CLEAN & ENRICH CURRENT ON-HAND INVENTORY (FOR TABLEAU)
onhand_clean = onhand_df.copy()
qty_col = "Quantity" if "Quantity" in onhand_clean.columns else "On Hand Quantity"
onhand_clean[qty_col] = pd.to_numeric(onhand_clean[qty_col], errors="coerce").fillna(0)

# Keep only positive internal on-hand units
onhand_clean = onhand_clean[onhand_clean[qty_col] > 0].copy()

onhand_clean[["Country", "Location_Tier"]] = onhand_clean["Location"].apply(
    lambda x: pd.Series(classify_location(x))
)
onhand_clean = onhand_clean[onhand_clean["Country"] != "External / Virtual"].copy()
onhand_clean["Unit_Cost_USD"] = onhand_clean["Product"].map(unit_cost_map).fillna(0)
onhand_clean["Total_Value_USD"] = onhand_clean[qty_col] * onhand_clean["Unit_Cost_USD"]

print("=== 3. ON-HAND INVENTORY BY COUNTRY & LOCATION TIER ===")
summary_table = (
    onhand_clean.groupby(["Country", "Location_Tier"])[["Total_Value_USD", qty_col]]
    .sum()
    .reset_index()
)
print(summary_table.to_string(index=False))
print(f"\nGrand Total Verified Units: {int(onhand_clean[qty_col].sum())}")
print(f"Grand Total Verified On-Hand Value: ${onhand_clean['Total_Value_USD'].sum():,.2f}")

# 5. EXPORT TABLEAU-READY CLEANED DATASETS
clean_moves.to_csv("tableau_mopo_moves_cleaned.csv", index=False)
onhand_clean.to_csv("tableau_mopo_onhand_cleaned.csv", index=False)
print("\n[SUCCESS] Exported 'tableau_mopo_moves_cleaned.csv' and 'tableau_mopo_onhand_cleaned.csv'!")
