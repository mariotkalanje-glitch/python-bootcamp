# MOPO Global Warehouse & Serialized Inventory Standard Operating Procedure (SOP)

**Document Owner:** Head of Logistics & Inventory  
**Applicable Facilities:** All Regional Central Warehouses (`NG-WH`, `DRC-WH`, `LR-WH`, `SL-WH`), Field Swap Hubs, and Refurbishment Bays  
**System of Record:** Odoo 19 ERP (Inventory & Purchase Modules)

---

## 1. Standardized Facility Layout & Zoning
Every regional facility must be physically demarcated with floor tape and overhead signage into **five mandatory zones** matching Odoo's location hierarchy:
* **Zone A — Inbound Quarantine & QA Bay (`Receiving`):** Staging area for arriving China containers and local vendor deliveries prior to serial verification and QC sign-off.
* **Zone B — High-Security Serialized Vault (`Stock`):** Restricted-access racking for `MOPO50`, `MOPOMax`, `Swap Chargers`, and `Solar Hub Kits`, organized by SKU family and FEFO/FIFO sequence.
* **Zone C — Hub Replenishment Staging (`Outbound Dispatch`):** Pre-kitted pallets staged by Swap Hub route and scheduled dispatch day (Monday–Friday).
* **Zone D — Refurbishment & Faulty Quarantine (`Refurbishment & Faulty`):** Physically isolated, fire-rated containment zone for RMA returns awaiting cell testing, BMS repair, or safe disposal.
* **Zone E — Consumables & Packaging (`MRO / Spares`):** Binned storage for cables, fuses, connectors, and barcode labels governed by Min/Max reorder points.

## 2. Barcode & QR Labelling Standard
* **Asset-Level Serial Labels:** Every battery, charger, and hub kit must carry a tamper-evident, weather-resistant QR/Code-128 barcode label matching its unique Odoo serial format (`[COUNTRY]-[SKU]-[SEQ]`, e.g., `NG-M50-001`, `DRC-HUB-003`).
* **Bin & Location Barcodes:** Every warehouse aisle, rack, and Swap Hub shelf must display a scannable Odoo location barcode to eliminate manual location entry errors during transfers.

## 3. Inbound Receiving & Quality Assurance Protocol
1. **48-Hour Dock-to-Stock SLA:** All arriving containers must be unstuffed, physically counted, voltage-checked, and validated in Odoo within **48 hours** of port arrival.
2. **Three-Way Match:** Warehouse leads must reconcile the **Commercial Invoice / Packing List**, **Physical Serial Scan**, and **Odoo Purchase Order** before clicking **Validate**.
3. **Damaged-in-Transit Quarantine:** Any unit failing initial open-circuit voltage or casing inspection is immediately transferred to `Refurbishment & Faulty` and logged on a Supplier Claim Report.

## 4. Storage, Battery Health & Shelf-Life Controls
* **180-Day Lithium Shelf-Life Rule:** Unissued `MOPO50` and `MOPOMax` batteries in Central Warehouses must not sit static beyond **180 days**.
* **90-Day Maintenance Top-Up:** Warehouse technicians must execute a scheduled state-of-charge (SoC) inspection and balance-charge every **90 days** for static stock, logging the check in Odoo lot notes.
* **Environmental & Fire Safety:** Batteries stored on non-conductive pallets/racking with dry-powder/Class-D fire suppression, ventilated aisles, and strict separation of healthy vs. damaged lithium cells.

## 5. Cycle Counting & Shrinkage Governance
* **Weekly Swap Hub Cycle Counts:** Hub supervisors perform a 100% blind serial scan every **Friday close**, reconciled against Odoo `Stock by Location`.
* **Monthly Regional Wall-to-Wall Audit:** Central Warehouse teams conduct a full physical count on the **last working day of each month** to support Finance month-end close.
* **Zero-Tolerance Variance Escalation:** Any discrepancy (`> 0` units) requires an documented root-cause investigation within **24 hours** and Finance sign-off before posting an Odoo `Inventory Adjustment`.

## 6. End-to-End Serialisation & RMA Redeployment Rules
* **Mandatory Unique Serial Tracking:** No serialized hardware SKU may move between locations without scanning its exact `Lot/Serial Number` in Odoo.
* **RMA Triage Priority:** Refurbished units passing QA load-testing are re-classified back into `Central Warehouse` stock and prioritized for **next-day Swap Hub replenishment** before drawing down newly imported OEM inventory.

## 7. Odoo Record-Keeping & Month-End Finance Reconciliation
* **Same-Day Transaction Posting:** All hub replenishments, last-mile agent deployments, and RMA returns must be validated in Odoo on the **same calendar day** of physical movement—no paper backlogs.
* **Month-End Close Package (Business Day +2):** Logistics delivers an automated Python/Odoo reconciliation pack (`Available Stock`, `In-Transit`, `RMA Pool`, and `Cycle Count Shrinkage`) to Finance for balance-sheet valuation and landed-cost accrual.
