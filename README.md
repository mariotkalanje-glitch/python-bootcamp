# Multi-Country Supply Chain, Serialized Inventory Control & Forward Demand Planning (Simulated Case Study)

**Author:** Mariot Margeson Kalanje  
**Stack:** Odoo 19 ERP (Enterprise Simulation) • Python (Pandas) • Tableau Public  
**Live Dashboard #1 (Inventory & Serial Audit):** [MOPO Multi-Country Supply Chain & Inventory Audit](https://tableau.com)  
**Live Dashboard #2 (Forward Demand & Replenishment):** [MOPO Forward Demand Planning & Replenishment Control Tower](https://tableau.com)  

> *Disclaimer: This repository models a synthetic multi-country battery-swapping and solar micro-grid logistics network (DRC, Liberia, Nigeria, and Sierra Leone) built strictly for executive case-study demonstration. All unit costs, quantities, and locations are simulated.*

---

## Executive Overview

High-velocity distributed energy operations require both **backward-looking serialized asset control** and **forward-looking rollout demand planning** from China OEM sourcing through regional central warehouses, local field swap hubs, customer deployments, and reverse-logistics refurbishment bays.

This capstone demonstrates an automated **ERP ➔ Python Data Engineering ➔ Executive BI** ecosystem across four operational pillars:

1. **Serialized ERP Control & Inventory Audit (`mopo_hub_inventory_audit.py`):**
   * Models 4 regional warehouses (`NG-WH`, `LR-WH`, `SL-WH`, `DRC-WH`), 13 internal storage locations (Swap Hubs + Refurbishment & Faulty bays), and 4 unique-serial-tracked hardware SKUs (`MOPO50 Battery`, `MOPOMax Battery`, `MOPO Swap Charger`, `MOPO Solar Hub Kit`).
   * Reconciles raw Odoo 19 stock movements and location quants down to **130 verified on-hand units ($21,645.00 FOB)** and isolates cycle-count shrinkage down to the exact serial number (`NG-M50-006`, `-$55.00`).
2. **Scheduled Hub Replenishment & RMA Redeployment (`mopo_demand_and_rollout_planner.py`):**
   * Establishes fixed weekly last-mile dispatch schedules (`Monday–Friday`) and 2-week target hub buffers across all 5 active Swap Hubs.
   * Prioritizes redeploying QA-recovered RMA batteries (`75%` refurbishment recovery yield) before drawing down new Central Warehouse buffer stock.
3. **12-Week Forward Rollout Demand Plan & JIT Procurement (`mopo_demand_and_rollout_planner.py`):**
   * Translates 6 planned regional hub installations (`W02`–`W12`) into weekly Bill-of-Materials (BOM) kit demand plus failure-rate spares (`8%` batteries, `5%` chargers).
   * Nets out existing Central Warehouse stock and applies 60–70 day China sea-freight lead times and 180-day lithium battery shelf-life limits to set exact **Order-By Dates**, **Need-By Dates**, and **12-Week Landed CapEx Forecasts ($4,553.96 USD)**.
4. **Global Warehouse & Serialisation SOP Governance (`MOPO_GLOBAL_WAREHOUSE_SOP.md`):**
   * Codifies one standardized operating rulebook across all 4 countries covering 5-zone facility layout, QR/barcode labelling, 48-hour dock-to-stock QA receiving, 90-day lithium balance-charging, weekly/monthly cycle counts, and Business Day +2 Finance close.

---

## Reconciled Executive Summary

| Domain | Metric | Verified Result | Operational & Financial Impact |
| :--- | :--- | :--- | :--- |
| **Inventory Audit** | **Verified On-Hand Stock** | **130 Units ($21,645.00 FOB)** | 100% reconciled across 4 countries and 3 location tiers |
| **Reverse Logistics** | **RMA Refurbishment Pool** | **8 Units ($703.00 FOB)** | Faulty units isolated; 75% QA yield routed back to high-demand hubs |
| **Loss Prevention** | **Cycle Count Shrinkage** | **1 Unit (-$55.00 FOB)** | Serial `NG-M50-006` (`Swap Hub - Abeokuta`) caught and written off |
| **Forward Demand** | **12-Week Net China POs** | **27 Units ($3,978.00 FOB)** | Netted against existing warehouse stock across 6 new hub rollouts |
| **Cost Forecasting** | **12-Week Landed CapEx** | **$4,553.96 USD** | Includes ocean freight, marine insurance, and customs multipliers (+12%–16%) |

---

## Repository Structure

* `mopo_hub_inventory_audit.py` — Automated Pandas ERP reconciliation, location-tier classification, and serial shrinkage audit script.
* `mopo_demand_and_rollout_planner.py` — Forward 12-week rollout MRP, weekly hub replenishment, RMA redeployment, and landed-cost CapEx forecasting script.
* `MOPO_GLOBAL_WAREHOUSE_SOP.md` — Standardized multi-country warehouse layout, barcode labelling, receiving QA, shelf-life, and Finance month-end SOP.
* `mopo_stock_moves.csv` & `mopo_stock_onhand.csv` — Raw serialized Odoo 19 ERP exports (`Moves History` and `Stock by Location`).
* `tableau_mopo_onhand_cleaned.csv` & `tableau_mopo_moves_cleaned.csv` — Enriched datasets powering Tableau Dashboard #1.
* `tableau_mopo_weekly_rollout_plan.csv`, `tableau_mopo_hub_replenishment.csv` & `tableau_mopo_finance_reconciliation.csv` — Enriched planning datasets powering Tableau Dashboard #2.
* `mopo_capstone_session_archive.md` — Complete technical build log and executive walkthrough reference.
