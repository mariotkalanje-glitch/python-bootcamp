import pandas as pd
from datetime import datetime, timedelta

# ==============================================================================
# MOPO FORWARD DEMAND PLANNING, HUB REPLENISHMENT & CAPEX FORECASTING ENGINE
# Author: Mariot Margeson Kalanje | Head of Logistics & Inventory Capstone
# Inputs: tableau_mopo_onhand_cleaned.csv (Verified Odoo 19 ERP Baseline)
# ==============================================================================

# 1. LOAD VERIFIED ODOO ON-HAND BASELINE
onhand_df = pd.read_csv("tableau_mopo_onhand_cleaned.csv")

# Standard Hardware Costs, Failure Rates, Lead Times & Battery Shelf-Life Rules
sku_specs = {
    "[MOPO-BAT-50] MOPO50 Battery": {
        "Short_Name": "MOPO50 Battery",
        "Unit_FOB_USD": 55.00,
        "Landed_Multiplier": 1.14,
        "Failure_Rate": 0.08,
        "China_Lead_Days": 65,
        "Shelf_Life_Days": 180,
        "Kit_Qty": 12,
    },
    "[MOPO-BAT-MAX] MOPOMax Battery": {
        "Short_Name": "MOPOMax Battery",
        "Unit_FOB_USD": 200.00,
        "Landed_Multiplier": 1.14,
        "Failure_Rate": 0.06,
        "China_Lead_Days": 65,
        "Shelf_Life_Days": 180,
        "Kit_Qty": 6,
    },
    "[MOPO-CHG-01] MOPO Swap Charger": {
        "Short_Name": "MOPO Swap Charger",
        "Unit_FOB_USD": 28.00,
        "Landed_Multiplier": 1.12,
        "Failure_Rate": 0.05,
        "China_Lead_Days": 60,
        "Shelf_Life_Days": 730,
        "Kit_Qty": 4,
    },
    "[MOPO-HUB-KIT] MOPO Solar Hub Kit": {
        "Short_Name": "MOPO Solar Hub Kit",
        "Unit_FOB_USD": 980.00,
        "Landed_Multiplier": 1.16,
        "Failure_Rate": 0.03,
        "China_Lead_Days": 70,
        "Shelf_Life_Days": 730,
        "Kit_Qty": 1,
    },
}

# Summarize current Odoo stock by Country, Product & Tier
stock_pivot = (
    onhand_df.groupby(["Country", "Product", "Location_Tier"])["Quantity"]
    .sum()
    .unstack(fill_value=0)
    .reset_index()
)
for col in ["Central Warehouse", "Field Swap Hub", "Refurbishment & Faulty"]:
    if col not in stock_pivot.columns:
        stock_pivot[col] = 0

# ==============================================================================
# PILLAR 1: SCHEDULED HUB REPLENISHMENT, LAST-MILE & RMA REDEPLOYMENT
# ==============================================================================
hub_schedule_config = [
    {"Country": "Nigeria", "Hub": "Swap Hub - Abeokuta", "Dispatch_Day": "Monday", "Last_Mile_Mode": "Dedicated 3T Box Truck", "Weekly_Swap_Demand_M50": 6, "Weekly_Swap_Demand_MAX": 3, "Target_Buffer_Weeks": 2},
    {"Country": "Nigeria", "Hub": "Swap Hub - Ibadan", "Dispatch_Day": "Wednesday", "Last_Mile_Mode": "Dedicated 3T Box Truck", "Weekly_Swap_Demand_M50": 5, "Weekly_Swap_Demand_MAX": 2, "Target_Buffer_Weeks": 2},
    {"Country": "DRC", "Hub": "Swap Hub - Kinshasa", "Dispatch_Day": "Tuesday", "Last_Mile_Mode": "Contracted Van / Ferry", "Weekly_Swap_Demand_M50": 7, "Weekly_Swap_Demand_MAX": 4, "Target_Buffer_Weeks": 2},
    {"Country": "Liberia", "Hub": "Swap Hub - Monrovia", "Dispatch_Day": "Thursday", "Last_Mile_Mode": "MOPO Pickup Fleet", "Weekly_Swap_Demand_M50": 5, "Weekly_Swap_Demand_MAX": 2, "Target_Buffer_Weeks": 2},
    {"Country": "Sierra Leone", "Hub": "Swap Hub - Freetown", "Dispatch_Day": "Friday", "Last_Mile_Mode": "MOPO Pickup Fleet", "Weekly_Swap_Demand_M50": 4, "Weekly_Swap_Demand_MAX": 2, "Target_Buffer_Weeks": 2},
]

hub_stock = onhand_df[onhand_df["Location_Tier"] == "Field Swap Hub"].copy()
hub_stock["Hub_Name"] = hub_stock["Location"].apply(lambda x: x.split("/")[-1])

rma_pool = (
    onhand_df[onhand_df["Location_Tier"] == "Refurbishment & Faulty"]
    .groupby(["Country", "Product"])["Quantity"]
    .sum()
    .reset_index()
)
rma_pool["QA_Recovered_Units"] = (rma_pool["Quantity"] * 0.75).round().astype(int)

hub_rows = []
for cfg in hub_schedule_config:
    for prod, demand_key in [
        ("[MOPO-BAT-50] MOPO50 Battery", "Weekly_Swap_Demand_M50"),
        ("[MOPO-BAT-MAX] MOPOMax Battery", "Weekly_Swap_Demand_MAX"),
    ]:
        curr_qty = hub_stock[
            (hub_stock["Hub_Name"] == cfg["Hub"]) & (hub_stock["Product"] == prod)
        ]["Quantity"].sum()
        weekly_dem = cfg[demand_key]
        target_stock = weekly_dem * cfg["Target_Buffer_Weeks"]
        gross_replenish = max(0, int(target_stock - curr_qty + weekly_dem))

        rec_match = rma_pool[(rma_pool["Country"] == cfg["Country"]) & (rma_pool["Product"] == prod)]
        rma_redeploy = min(gross_replenish, int(rec_match["QA_Recovered_Units"].sum())) if not rec_match.empty else 0
        central_wh_draw = gross_replenish - rma_redeploy

        hub_rows.append({
            "Country": cfg["Country"],
            "Swap_Hub": cfg["Hub"],
            "Product": sku_specs[prod]["Short_Name"],
            "Scheduled_Dispatch_Day": cfg["Dispatch_Day"],
            "Last_Mile_Transport": cfg["Last_Mile_Mode"],
            "Current_Hub_Stock": int(curr_qty),
            "Weekly_Demand": weekly_dem,
            "Target_2Wk_Buffer": target_stock,
            "RMA_Refurb_Redeployed": rma_redeploy,
            "Central_WH_Replenishment": central_wh_draw,
            "Total_Scheduled_Delivery": gross_replenish,
            "Stockout_Risk_Status": "HIGH - Immediate Dispatch" if curr_qty <= weekly_dem else "CONTROLLED",
        })

hub_replenishment_df = pd.DataFrame(hub_rows)

# ==============================================================================
# PILLAR 2: 12-WEEK FORWARD ROLLOUT DEMAND PLAN & JIT CHINA PROCUREMENT
# ==============================================================================
base_date = datetime(2026, 11, 16)

rollout_milestones = [
    {"Week_Num": 2, "Country": "Nigeria", "New_Hubs_Planned": 1, "Install_Site": "Ogun Industrial Corridor"},
    {"Week_Num": 4, "Country": "DRC", "New_Hubs_Planned": 1, "Install_Site": "Kinshasa East Commercial Zone"},
    {"Week_Num": 6, "Country": "Nigeria", "New_Hubs_Planned": 1, "Install_Site": "Ibadan Ring-Road Hub"},
    {"Week_Num": 8, "Country": "Liberia", "New_Hubs_Planned": 1, "Install_Site": "Paynesville Market Hub"},
    {"Week_Num": 10, "Country": "Sierra Leone", "New_Hubs_Planned": 1, "Install_Site": "Waterloo Transit Hub"},
    {"Week_Num": 12, "Country": "DRC", "New_Hubs_Planned": 1, "Install_Site": "Matadi Port Logistics Hub"},
]

rollout_rows = []
for m in rollout_milestones:
    need_by_date = base_date + timedelta(weeks=m["Week_Num"])
    for prod, spec in sku_specs.items():
        base_kit_units = m["New_Hubs_Planned"] * spec["Kit_Qty"]
        spares_units = max(1, round(base_kit_units * spec["Failure_Rate"]))
        total_req_units = base_kit_units + spares_units

        wh_match = stock_pivot[(stock_pivot["Country"] == m["Country"]) & (stock_pivot["Product"] == prod)]
        wh_avail = int(wh_match["Central Warehouse"].sum()) if not wh_match.empty else 0

        net_china_order = max(0, total_req_units - wh_avail)
        order_by_date = need_by_date - timedelta(days=spec["China_Lead_Days"])
        fob_cost = net_china_order * spec["Unit_FOB_USD"]
        landed_cost = round(fob_cost * spec["Landed_Multiplier"], 2)

        rollout_rows.append({
            "Rollout_Week": f"W{m['Week_Num']:02d}",
            "Week_Number": m["Week_Num"],
            "Country": m["Country"],
            "Install_Site": m["Install_Site"],
            "Product": spec["Short_Name"],
            "Kit_BOM_Units": base_kit_units,
            "Failure_Rate_Spares": spares_units,
            "Total_Required_Units": total_req_units,
            "Central_WH_OnHand": wh_avail,
            "Net_China_PO_Qty": net_china_order,
            "Need_By_Date": need_by_date.strftime("%Y-%m-%d"),
            "China_Order_By_Date": order_by_date.strftime("%Y-%m-%d"),
            "Shelf_Life_Limit_Days": spec["Shelf_Life_Days"],
            "FOB_Procurement_USD": round(fob_cost, 2),
            "Landed_Cost_Forecast_USD": landed_cost,
            "JIT_Action_Flag": "URGENT - Expedite Air/Sea" if order_by_date <= base_date else "ON SCHEDULE - Sea Freight",
        })

rollout_plan_df = pd.DataFrame(rollout_rows)

# ==============================================================================
# PILLAR 3: FINANCE MONTH-END RECONCILIATION & SUPPLY CHAIN COST FORECAST
# ==============================================================================
finance_summary = (
    onhand_df.groupby(["Country", "Location_Tier"])
    .agg(OnHand_Units=("Quantity", "sum"), Current_FOB_Valuation_USD=("Total_Value_USD", "sum"))
    .reset_index()
)

country_capex = (
    rollout_plan_df.groupby("Country")
    .agg(
        Planned_PO_Units=("Net_China_PO_Qty", "sum"),
        Forecast_FOB_Spend_USD=("FOB_Procurement_USD", "sum"),
        Forecast_Landed_Spend_USD=("Landed_Cost_Forecast_USD", "sum"),
    )
    .reset_index()
)

# ==============================================================================
# 4. EXECUTIVE CONSOLE OUTPUT & TABLEAU CSV EXPORTS
# ==============================================================================
print("=== PILLAR 1: WEEKLY HUB REPLENISHMENT & RMA REDEPLOYMENT SCHEDULE ===")
print(hub_replenishment_df[["Country", "Swap_Hub", "Product", "Scheduled_Dispatch_Day", "Current_Hub_Stock", "RMA_Refurb_Redeployed", "Central_WH_Replenishment", "Stockout_Risk_Status"]].to_string(index=False))

print("\n=== PILLAR 2: 12-WEEK ROLLOUT KIT DEMAND & JIT PROCUREMENT SUMMARY BY COUNTRY ===")
print(country_capex.to_string(index=False))
print(f"Total 12-Week Forecasted Landed CapEx: ${country_capex['Forecast_Landed_Spend_USD'].sum():,.2f} USD")

print("\n=== PILLAR 3: FINANCE MONTH-END STOCK VALUATION & RECONCILIATION ===")
print(finance_summary.to_string(index=False))
print(f"Total Verified Balance-Sheet Inventory Value (FOB): ${finance_summary['Current_FOB_Valuation_USD'].sum():,.2f} USD")

hub_replenishment_df.to_csv("tableau_mopo_hub_replenishment.csv", index=False)
rollout_plan_df.to_csv("tableau_mopo_weekly_rollout_plan.csv", index=False)
finance_summary.to_csv("tableau_mopo_finance_reconciliation.csv", index=False)