# Multi-Country Supply Chain & Serialized Inventory Control (Simulated Case Study)

**Author:** Mariot Margeson Kalanje  
**Stack:** Odoo 19 ERP (Enterprise Simulation) • Python (Pandas) • Tableau Public  
**Live Interactive Dashboard:** [MOPO Multi-Country Supply Chain & Inventory Audit on Tableau Public](https://tableau.com)  

> *Disclaimer: This repository models a synthetic multi-country battery-swapping and solar micro-grid logistics network (DRC, Liberia, Nigeria, and Sierra Leone) built strictly for executive case-study demonstration. All unit costs, quantities, and locations are simulated.*

---

## Executive Overview

High-velocity distributed energy operations require end-to-end serial traceability from China OEM procurement through regional central warehouses, local field swap hubs, customer deployments, and reverse-logistics refurbishment bays.

This capstone demonstrates an automated **ERP ➔ Python Audit ➔ Executive BI** pipeline:
1. **Odoo 19 Multi-Warehouse & Serialized ERP Architecture:** Configured 4 regional central warehouses (`NG-WH`, `LR-WH`, `SL-WH`, `DRC-WH`), 13 internal storage locations (Swap Hubs + Refurbishment & Faulty bays), 3 global OEM/sourcing vendors, and 4 unique-serial-tracked hardware SKUs (`MOPO50 Battery`, `MOPOMax Battery`, `MOPO Swap Charger`, `MOPO Solar Hub Kit`).
2. **Automated Python Reconciliation (`mopo_hub_inventory_audit.py`):** Ingests raw Odoo stock move history and location-level quants, filters out cancelled records, classifies multi-tier supply chain flows, reconciles CapEx valuation across countries, and isolates cycle-count shrinkage down to the exact serial number.
3. **Executive BI Visualization (Tableau Public):** Delivers cross-filterable regional CapEx exposure, product mix distribution, supply chain flow throughput, and serial-level RMA/shrinkage audit tables.

---

## Reconciled Audit Summary

| Metric | Verified Result | Operational Insight |
| :--- | :--- | :--- |
| **Total Verified On-Hand Units** | **130 Units** | 100% reconciled across 4 countries and 3 location tiers |
| **Total Verified On-Hand CapEx** | **$21,645.00 USD** | Nigeria leads active deployment ($6,852 total; $2,947 in Swap Hubs) |
| **Hub Replenishment Volume** | **$8,673.00 USD** | Automated central-to-hub transfers maintaining swap station buffers |
| **Reverse Logistics (RMA) Pool** | **$703.00 USD (8 Units)** | Faulty units isolated in Refurbishment bays for cell recovery |
| **Cycle Count Shrinkage Flagged** | **-$55.00 USD (1 Unit)** | Serial `NG-M50-006` (`Swap Hub - Abeokuta`) caught and written off |

---

## Repository Structure

* `mopo_hub_inventory_audit.py` — End-to-end Pandas data cleaning, classification, and financial reconciliation script.
* `mopo_stock_moves.csv` — Raw serialized stock movement export from Odoo 19 (`Moves History`).
* `mopo_stock_onhand.csv` — Raw location-level serialized quant export from Odoo 19 (`Stock by Location`).
* `tableau_mopo_moves_cleaned.csv` — Enriched movement dataset powering Tableau flow & audit charts.
* `tableau_mopo_onhand_cleaned.csv` — Enriched on-hand valuation dataset powering Tableau regional & product charts.

---

## Additional Bootcamp Foundations

This repository also includes foundational data engineering exercises (`day2_csv.py`, `day2_pandas.py`, `day3_cleaning.py`, `loops.py`, `practice1.py`, and `practice2.py`) covering CSV parsing, Pandas transformations, and data standardization.
