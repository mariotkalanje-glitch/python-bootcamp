# MOPO Multi-Country Supply Chain & Serialized Inventory Control Capstone

**Builder:** Mariot Margeson Kalanje  
**Technology Stack:** Odoo 19 Enterprise Simulation • Python (Pandas) • Tableau Public • GitHub  
**Live Tableau Public Dashboard:** https://public.tableau.com/app/profile/mariot.kalanje/viz/MOPOMulti-CountrySupplyChainInventoryAudit  
**GitHub Repository:** https://github.com/mariotkalanje-glitch/python-bootcamp  

---

## Executive Summary & Verified Reconciliation Metrics

Across three structured build sessions, we designed, populated, audited, and published a full-lifecycle multi-country supply chain and serialized inventory control case study modeling operations across **Nigeria, Liberia, Sierra Leone, and DRC**.

| KPI / Audit Metric | Verified Result | Operational & Financial Breakdown |
| :--- | :--- | :--- |
| **Total Verified On-Hand Units** | **130 Units** | 100% reconciled across 4 countries and 3 location tiers |
| **Total Verified On-Hand CapEx** | **$21,645.00 USD** | Nigeria ($6,852), DRC ($5,727), Liberia ($5,196), Sierra Leone ($3,870) |
| **Central Warehouse Buffer Stock** | **$13,282.00 USD (83 Units)** | DRC ($4,071), Nigeria ($3,595), Liberia ($3,595), Sierra Leone ($2,497) |
| **Field Swap Hub Active Stock** | **$7,660.00 USD (39 Units)** | Nigeria ($2,947), Liberia ($1,518), Sierra Leone ($1,373), DRC ($1,346) |
| **Reverse Logistics (RMA) Pool** | **$703.00 USD (8 Units)** | Nigeria ($310 / 3 units), DRC ($310 / 3 units), Liberia ($83 / 2 units) |
| **Hub Replenishment Volume** | **$8,673.00 USD** | Central warehouse to regional swap hub transfers |
| **Outbound Field Deployment** | **$1,717.00 USD (20 Units)** | Direct swap-hub deployments to regional agent/micro-grid partners |
| **Cycle Count Shrinkage Caught** | **-$55.00 USD (1 Unit)** | Serial `NG-M50-006` (`MOPO50 Battery`) at `NG-WH/Stock/Swap Hub - Abeokuta` |

---

## Phase 1: Odoo 19 Multi-Warehouse & Serialized Architecture (Day 1)

### 1. Core ERP Configuration (`Metas Traders` Database)
* Enabled **Lots & Serial Numbers**, **Storage Locations**, **Multi-Step Routes**, and **Landed Costs** in **USD**.
* Established nominative case-study modeling (strictly synthetic numbers, clear simulation labeling, non-commercial portfolio use).

### 2. Regional Warehouses & 13 Internal Storage Locations
* **Nigeria (`NG-WH` — MOPO Nigeria Central):**
  * `NG-WH/Stock` (Central Warehouse)
  * `NG-WH/Stock/Swap Hub - Abeokuta`
  * `NG-WH/Stock/Swap Hub - Ibadan`
  * `NG-WH/Stock/Refurbishment & Faulty`
* **Liberia (`LR-WH` — MOPO Liberia Central):**
  * `LR-WH/Stock` (Central Warehouse)
  * `LR-WH/Stock/Swap Hub - Monrovia`
  * `LR-WH/Stock/Refurbishment & Faulty`
* **Sierra Leone (`SL-WH` — MOPO Sierra Leone Central):**
  * `SL-WH/Stock` (Central Warehouse)
  * `SL-WH/Stock/Swap Hub - Freetown`
  * `SL-WH/Stock/Refurbishment & Faulty`
* **DRC (`DRC-WH` — MOPO DRC Central):**
  * `DRC-WH/Stock` (Central Warehouse)
  * `DRC-WH/Stock/Swap Hub - Kinshasa`
  * `DRC-WH/Stock/Refurbishment & Faulty`

### 3. Serialized Product Master (`By Unique Serial Number`)

| Product Name | Internal Reference | Sales Price (USD) | Unit CapEx Cost (USD) | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **MOPO50 Battery** | `MOPO-BAT-50` | $85.00 | $55.00 | By Unique Serial Number |
| **MOPOMax Battery** | `MOPO-BAT-MAX` | $320.00 | $200.00 | By Unique Serial Number |
| **MOPO Swap Charger** | `MOPO-CHG-01` | $45.00 | $28.00 | By Unique Serial Number |
| **MOPO Solar Hub Kit** | `MOPO-HUB-KIT` | $1,450.00 | $980.00 | By Unique Serial Number |

---

## Phase 2: Global Procurement, Receipts & Inter-Hub Transfers (Day 2)

### 1. Global & Regional Suppliers
* `MOPO China Sourcing Hub` (China — consolidated pre-shipment QC & container hub)
* `Shenzhen PowerCell Energy Ltd` (China — battery & charger OEM)
* `Ningbo SolarGrid Manufacturing Co` (China — solar hub & inverter OEM)

### 2. Inbound Container Receipts (148 Serialized Units Received)
* **Nigeria (`P00002` / `NG-WH/IN/00002`):** `NG-M50-001..020` (20), `NG-MAX-001..010` (10), `NG-CHG-001..010` (10), `NG-HUB-001..004` (4) = 44 units.
* **Liberia (`P00003`):** `LR-M50-001..015` (15), `LR-MAX-001..008` (8), `LR-CHG-001..008` (8), `LR-HUB-001..003` (3) = 34 units.
* **Sierra Leone (`P00004`):** `SL-M50-001..015` (15), `SL-MAX-001..006` (6), `SL-CHG-001..006` (6), `SL-HUB-001..002` (2) = 29 units.
* **DRC (`P00005`):** `DRC-M50-001..020` (20), `DRC-MAX-001..010` (10), `DRC-CHG-001..008` (8), `DRC-HUB-001..003` (3) = 41 units.

### 3. Internal Transfers (8 Validated Transfers — Forward Replenishment & Reverse RMA)
1. `NG-WH/Stock` ➔ `Swap Hub - Abeokuta`: 6 MOPO50, 3 MOPOMax, 3 Chargers, 1 Solar Hub Kit
2. `NG-WH/Stock` ➔ `Swap Hub - Ibadan`: 5 MOPO50, 2 MOPOMax, 2 Chargers, 1 Solar Hub Kit
3. `Swap Hub - Abeokuta` ➔ `NG-WH/Stock/Refurbishment & Faulty` (RMA): 2 MOPO50, 1 MOPOMax
4. `LR-WH/Stock` ➔ `Swap Hub - Monrovia`: 6 MOPO50, 3 MOPOMax, 3 Chargers, 1 Solar Hub Kit
5. `Swap Hub - Monrovia` ➔ `LR-WH/Stock/Refurbishment & Faulty` (RMA): 1 MOPO50, 1 Charger
6. `SL-WH/Stock` ➔ `Swap Hub - Freetown`: 5 MOPO50, 2 MOPOMax, 2 Chargers, 1 Solar Hub Kit
7. `DRC-WH/Stock` ➔ `Swap Hub - Kinshasa`: 7 MOPO50, 4 MOPOMax, 3 Chargers, 1 Solar Hub Kit
8. `Swap Hub - Kinshasa` ➔ `DRC-WH/Stock/Refurbishment & Faulty` (RMA): 2 MOPO50, 1 MOPOMax

---

## Phase 3: Field Deployments, Cycle Count & CSV Exports (Day 3)

### 1. Outbound Field Partner Deliveries (20 Serialized Units Deployed)
* `NG-WH/Stock/Swap Hub - Abeokuta` ➔ `Ogun State Swap Agent Network`: 3 MOPO50, 1 MOPOMax, 1 Charger
* `LR-WH/Stock/Swap Hub - Monrovia` ➔ `Monrovia Micro-Grid Cooperative`: 3 MOPO50, 1 MOPOMax, 1 Charger
* `SL-WH/Stock/Swap Hub - Freetown` ➔ `Freetown Solar Kiosk Partners`: 2 MOPO50, 1 MOPOMax, 1 Charger
* `DRC-WH/Stock/Swap Hub - Kinshasa` ➔ `Kinshasa Peri-Urban Energy Agents`: 3 MOPO50, 2 MOPOMax, 1 Charger

### 2. Physical Cycle Count Audit
* **Confirmed Match (`0.0` Variance):** `DRC-MAX-004` verified `1.00` at `DRC-WH/Stock/Swap Hub - Kinshasa`.
* **Shrinkage Variance (`-1.0` Unit / `-$55.00`):** `NG-M50-006` counted `0.00` at `NG-WH/Stock/Swap Hub - Abeokuta` and written off to `Inventory adjustment`.

### 3. Raw Odoo CSV Exports (`C:\Users\Administrator\Desktop\python-bootcamp`)
* `mopo_stock_moves.csv` — Exported from **Reporting ➔ Moves History** (`Date`, `Reference`, `Product`, `Lot/Serial Number`, `From`, `To`, `Quantity`, `Unit`, `Status`).
* `mopo_stock_onhand.csv` — Exported from **Reporting ➔ Stock by Location** (`Location`, `Product`, `Lot/Serial Number`, `Quantity`, `Reserved Quantity`).

---

## Phase 4: Python & Pandas Reconciliation Script (`mopo_hub_inventory_audit.py`)

```python
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
```

---

## Phase 5: Tableau Public Dashboard & GitHub Portfolio Deployment

### 1. Tableau Public 4-Panel Executive Dashboard
* **Sheet 1 (`Regional CapEx Valuation`):** Stacked bar chart (`Country` vs. `SUM(Total_Value_USD)`, colored by `Location_Tier`).
* **Sheet 2 (`Product Mix & Unit Deployment`):** Horizontal stacked bar chart (`SUM(Quantity)` vs. `Product`, colored by `Country`).
* **Sheet 3 (`End-to-End Supply Chain Flow`):** Horizontal flow bar chart (`SUM(Move_Value_USD)` vs. `Flow_Category`).
* **Sheet 4 (`RMA & Cycle Count Serial Audit Table`):** Serial-level exception audit table filtered to `3. Reverse Logistics (RMA)` and `5. Cycle Count Audit` (`Quantity >= 1`).

### 2. GitHub Commits (`mariotkalanje-glitch/python-bootcamp`)
* `af555a4`: Added `mopo_hub_inventory_audit.py`, `mopo_stock_moves.csv`, `mopo_stock_onhand.csv`, `tableau_mopo_moves_cleaned.csv`, and `tableau_mopo_onhand_cleaned.csv`.
* `56cfab7`: Updated `README.md` with executive overview, reconciled audit table, and live Tableau Public dashboard link.

---

## Key Operational Concepts & Panel Talking Points

* **What is RMA (Return Merchandise Authorization)?**
  * Formal reverse-logistics workflow used to isolate faulty or underperforming field units (`Swap Hub` ➔ `Refurbishment & Faulty` bay) so broken batteries are never counted as rent-ready buffer stock and Finance can track repair CapEx exposure (`$703.00` across `8 units`).
* **Operations Panelists (`Phil Howden` & `Benjamin Clay`):**
  * Focus on 3-tier location separation (`Central Warehouse` buffer vs. `Field Swap Hub` active stock vs. `Refurbishment & Faulty` quarantine) to eliminate stockouts while preventing faulty battery deployment.
* **Technical Panelists (`Luke Burras` & `Bawo Megbele`):**
  * Focus on unique serial-level traceability (`NG-M50-001` to `DRC-HUB-003`) and automated Pandas reconciliation scripts replacing manual spreadsheet audits.
* **Finance Panelist (`David Barclay`):**
  * Focus on 100% dollar-for-dollar CapEx reconciliation (`$21,645.00` across `130 units`), working-capital visibility across borders, and transparent cycle-count shrinkage governance (`NG-M50-006` at `-$55.00`).

---

## Next Session Plan: Rapid-Fire Mock Q&A
* **Trigger:** Say **"Start mock Q&A"** whenever ready.
* **Format:** Targeted, high-stakes interview questions tailored individually to **Phil Howden, Benjamin Clay, Luke Burras, Bawo Megbele, and David Barclay** ahead of **November 26**.
