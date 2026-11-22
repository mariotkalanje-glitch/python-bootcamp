# Multi-Country Supply Chain, Serialized Inventory Control & Forward Demand Planning (Case Study)

**Author:** Mariot Margeson Kalanje  
**Core Systems:** Odoo 19 ERP (Multi-Warehouse & Serialisation) • Automated Python Reconciliation • Tableau Executive BI  
**Interactive Dashboard #1 (Asset Control & Serial Audit):** [MOPO Multi-Country Supply Chain & Inventory Audit](https://public.tableau.com/app/profile/mariot.kalanje/viz/MOPOMulti-CountrySupplyChainInventoryAudit/AssetExposure)  
**Interactive Dashboard #2 (Forward Demand & CapEx Control Tower):** [MOPO Forward Demand Planning & Replenishment Control Tower](https://public.tableau.com/app/profile/mariot.kalanje/viz/MOPOForwardDemandPlanningReplenishmentControlTower/2_MOPOForwardDemandPlanningReplenishmentCapExStory)

**Standard Operating Procedure:** [MOPO Global Warehouse & Serialized Inventory Draft SOP](./MOPO_GLOBAL_WAREHOUSE_DRAFT_SOP.md) 

> *Note: This case study models a simulated multi-country battery-swapping and solar micro-grid logistics network across Nigeria, DRC, Liberia, and Sierra Leone to demonstrate end-to-end ERP control, forward demand planning, and cross-functional governance.*

---

## Executive Overview

Scaling high-velocity battery-swapping operations across multiple African markets requires tight alignment between **physical warehouse discipline**, **unique serial traceability in Odoo**, **forward-looking rollout demand planning**, and **month-end financial accuracy**.

This end-to-end operating model connects four core pillars:

1. **Serialized ERP Control & Inventory Audit:**
   * Models 4 regional central warehouses (`NG-WH`, `DRC-WH`, `LR-WH`, `SL-WH`), 13 internal storage locations (Field Swap Hubs + Refurbishment & Faulty bays), and 4 unique-serial-tracked hardware SKUs (`MOPO50`, `MOPOMax`, `Swap Charger`, `Solar Hub Kit`).
   * Reconciles raw Odoo 19 movements and location balances down to **130 verified on-hand units ($21,645.00 FOB)** and isolates cycle-count shrinkage down to the exact serial number (`NG-M50-006`, `-$55.00`).
2. **Scheduled Hub Replenishment & Milk-Run Reverse Logistics:**
   * Establishes fixed weekly last-mile dispatch schedules (`Monday–Friday`) and 2-week target hub buffers across all 5 active Swap Hubs.
   * Enforces **milk-run backhauls** (returning faulty RMA units on outbound delivery trucks) and prioritizes redeploying QA-certified refurbished batteries (`75%` recovery yield) to high-velocity hubs before drawing new central stock.
3. **12-Week Forward Rollout Demand Plan & JIT China Procurement:**
   * Translates 6 planned regional hub installations (`W02`–`W12`) into weekly Bill-of-Materials (BOM) kit demand plus failure-rate spares (`8%` batteries, `5%` chargers).
   * Nets out existing Central Warehouse stock, checks destination storage capacity, and applies 60–70 day China sea-freight lead times and 180-day lithium shelf-life limits to set exact **Order-By Dates**, **Need-By Dates**, and **12-Week Landed CapEx Forecasts ($4,553.96 USD)**.
4. **Global Warehouse & Serialisation Draft SOP (`MOPO_GLOBAL_WAREHOUSE_DRAFT_SOP.md`):**
   * Standardizes 5-zone facility layout, tamper-evident QR/barcode labelling, 48-hour dock-to-stock QA receiving, 90-day lithium balance-charging, pre-arrival port customs clearance, physical/transit security, and Segregation of Duties across all 4 countries.

---

## Reconciled Executive Summary

| Functional Area | Key Metric | Verified Result | Operational & Financial Impact |
| :--- | :--- | :--- | :--- |
| **Inventory Control** | **Verified On-Hand Stock** | **130 Units ($21,645.00 FOB)** | 100% reconciled across 4 countries and 3 location tiers |
| **Reverse Logistics** | **RMA Refurbishment Pool** | **8 Units ($703.00 FOB)** | Faulty units isolated; 75% QA yield routed back to high-demand hubs |
| **Loss Prevention** | **Cycle Count Shrinkage** | **1 Unit (-$55.00 FOB)** | Serial `NG-M50-006` (`Swap Hub - Abeokuta`) isolated and investigated |
| **Forward Demand** | **12-Week Net China POs** | **27 Units ($3,978.00 FOB)** | Netted against existing warehouse stock across 6 new hub rollouts |
| **Cost Forecasting** | **12-Week Landed CapEx** | **$4,553.96 USD** | Includes ocean freight, marine insurance, and customs duty multipliers (+12%–16%) |

---

## Cross-Functional Governance & Leadership Highlights

* **For Operations (`Stock Control, Teams & In-Country Logistics`):**
  * **Segregation of Duties & Security:** Separates physical stock handlers from Odoo adjustment approvers (`Tiered USD Approval Matrix`), backed by biometric/badge vault access, 24/7 CCTV, GPS-tracked inland haulage, and tamper-evident container seals.
  * **Port-to-Site Execution:** Submits pre-arrival customs filings (`Form M/SONCAP`, `BESC/FERI`) 7–10 days before vessel ETA to prevent demurrage, enforces a 14–21 day JIT port arrival window, and requires install crews to return unused site hardware within 48 hours.
  * **Multi-Country Team Cadence:** Runs daily 15-minute hub stand-ups, weekly 5-KPI operational reviews, monthly 20-point warehouse compliance audits, and a scalable 4-role expansion pod for new country launches.
* **For Technical & Systems (`Odoo Business Ownership`):**
  * Enforces mandatory unique serial scanning on every stock move across a 5-zone Odoo location hierarchy (`Input ➔ Stock ➔ Output`, `Refurbishment & Faulty`, and `MRO Spares`), governed by joint Logistics–Engineering–Finance change control before modifying valuation or location rules.
* **For Finance (`Valuation, Audits & Forecasting`):**
  * Delivers a reconciled close package by **Business Day +2**, capitalizes freight/duties via Odoo `Landed Costs`, flags >30-day RMA units for impairment provisioning, and enforces year-end stocktake freeze and blind second-count recount protocols.
