# MOPO Global Warehouse & Serialized Inventory Draft Standard Operating Procedure (SOP)

| Document Owner: Head of Logistics & Inventory | System of Record: Odoo 19 (Inventory, Purchase & Landed Costs) | Applicable Facilities: Regional Central Warehouses (NG-WH, DRC-WH, LR-WH, SL-WH), Field Swap Hubs & Refurbishment | Cross-Functional: Logistics & Inventory • Finance • Technical Operations • Commercial |
| :--- | :--- | :--- | :--- |

## 1. Standardized Facility Layout & Zoning
Every regional facility must be physically demarcated with floor tape and overhead signage into five mandatory zones matching Odoo's location hierarchy:
* **Zone A - Inbound Quarantine & QA Bay (Receiving):** Staging area for arriving China containers and local vendor deliveries prior to serial verification and QC sign-off.
* **Zone B - High-Security Serialized Vault (Stock):** Restricted-access racking for the high-value units like MOPO50, MOPOMax, Swap Chargers, and Solar Hub Kits, organized by SKU family and FEFO/ FIFO sequence.
* **Zone C - Hub Replenishment Staging (Outbound Dispatch):** Pre-kitted pallets staged by Swap Hub route and scheduled dispatch day (Monday–Friday).
* **Zone D - Refurbishment & Faulty Quarantine (Refurbishment & Faulty):** Physically isolated, fire-rated containment zone for RMA returns awaiting cell testing, BMS repair, or safe disposal.
* **Zone E - Consumables & Packaging (MRO / Spares):** Binned storage for low-value units like cables, fuses, connectors, and barcode labels governed by Min/ Max reorder points.

## 2. Barcode & QR Labelling Standard
* **Asset-Level Serial Labels:** Every battery, charger, and hub kit must carry a tamper-evident, weather-resistant QR/Code-128 barcode label matching its unique Odoo serial format ([COUNTRY]-[SKU]-[SEQ], e.g., NG-M50-001, DRC-HUB-003).
* **Bin & Location Barcodes:** Every warehouse aisle, rack, and Swap Hub shelf must display a scannable Odoo location barcode to eliminate manual location entry errors during transfers.

## 3. Inbound Receiving & Quality Assurance Protocol
1. **48-Hour Dock-to-Stock SLA:** All arriving containers must be unstuffed, physically counted, voltage-checked, and validated in Odoo within 48 hours of port arrival.
2. **Three-Way Match:** Warehouse leads must reconcile the Commercial Invoice / Packing List, Physical Serial Scan, and Odoo Purchase Order before clicking Validate.
3. **Damaged-in-Transit Quarantine:** Any unit failing initial open-circuit voltage or casing inspection is immediately transferred to Refurbishment & Faulty and logged on a Supplier Claim Report.

## 4. Storage, Battery Health & Shelf-Life Controls
* **180-Day Lithium Shelf-Life Rule:** Unused MOPO50 and MOPOMax batteries in Central Warehouses must not sit static beyond 180 days.
* **90-Day Maintenance Top-Up:** Warehouse technicians must execute a scheduled state-of-charge (SoC) inspection and balance-charge every 90 days for static stock, logging the check in Odoo lot notes.
* **Environmental & Fire Safety:** Batteries stored on non-conductive pallets/ racking with dry-powder/ Class-D fire suppression, ventilated aisles, and strict separation of healthy vs. damaged lithium cells.

## 5. Cycle Counting, Year-End Audit Cut-Off & Shrinkage Governance
* **Weekly Swap Hub Cycle Counts:** Hub supervisors perform a 100% serial scan every Friday close, reconciled against Odoo Stock by Location.
* **Monthly Regional Wall-to-Wall Audit:** Central Warehouse teams conduct a full physical count on the last working day of each month to support Finance month-end close.
* **Formal Year-End Audit Cut-Off Protocol:** Co-designed with Finance and external auditors:
  * **Transaction Freeze Window:** All physical dispatches and Odoo transfers pause during the scheduled year-end stocktake window.
  * **In-Transit & Agent Consignment Reconciliation:** All goods in transit between ports, central warehouses, and field agents are verified via signed waybills and serial logs before count closure.
  * **Blind Second-Count Recount Rule:** Any initial count variance triggers an immediate blind second recount by an independent supervisor before logging an adjustment.
  * **Zero-Tolerance Variance Escalation:** Any discrepancy (> 0 units) requires a documented root-cause investigation within 24 hours and Finance sign-off before posting an Odoo Inventory Adjustment.

## 6. End-to-End Serialisation, Milk-Run Backhaul & RMA Redeployment
* **Mandatory Unique Serial Tracking:** No serialized hardware SKU may move between locations without scanning its exact Lot/Serial Number in Odoo.
* **Milk-Run Backhaul Rule:** Every outbound last-mile replenishment vehicle delivering healthy batteries to a Swap Hub must backhaul all tagged RMA faulty units and empty crates on the return trip (zero empty-mile waste).
* **Value-Based RMA Triage Priority:** Refurbished units passing QA load-testing are re-classified back into Central Warehouse stock and routed first to highest-swap-velocity / lowest-buffer hubs before drawing down newly imported inventory.

## 7. Odoo Record-Keeping & Month-End Finance Reconciliation
* **Same-Day Transaction Posting:** All hub replenishments, last-mile agent deployments, and RMA returns must be validated in Odoo on the same calendar day of physical movement, with no paper backlogs.
* **Landed-Cost Capitalization:** Freight, port clearing, and customs duty invoices are attached directly onto Odoo Receipts (Landed Costs) so balance-sheet inventory reflects true landed asset value.
* **30-Day RMA Impairment Provisioning:** Any faulty unit remaining in Refurbishment & Faulty beyond 30 days (or failing QA cell testing) is flagged on the month-end Finance report for impairment/ scrap provisioning.
* **Month-End Close Package (Business Day +2):** Logistics delivers an automated Python/ Odoo reconciliation pack (Available Stock, In-Transit, RMA Pool and Cycle Count Shrinkage) to Finance by Business Day 2 of each month.

## 8. Segregation of Duties (SoD) & Tiered Approval Matrix
To prevent internal collusion, unauthorized write-offs or silent record manipulation in Odoo:
* **Strict Role Separation:** Warehouse storekeepers and hub supervisors who physically receive, move, or dispatch stock do not have system permissions to validate Inventory Adjustments or Scrap orders in Odoo. Only Inventory Control and Finance hold adjustment validation rights.
* **Structured CAPA (Corrective & Preventive Action) Loop:** Every stock variance is classified into one of three mandatory root-cause categories; (1) Process / Odoo Posting Error, (2) Transit / Handling Damage or (3) Theft / Tampering with a documented Corrective & Preventive Action (CAPA) implemented before closing the ticket.

| Variance / Write-Off Tier (USD) | Root-Cause Requirement | Mandatory Approvers |
| :--- | :--- | :--- |
| Tier 1: $0 (Posting / Scan Error) | Same-day serial audit & Odoo log review | Country Inventory Lead |
| Tier 2: $1 - $250 USD | 24-hour CAPA report + CCTV/seal check | Country Inventory Lead + Regional Finance Controller |
| Tier 3: > $250 USD or Suspected Tampering / Theft | Full investigation + police/insurance report | Head of Logistics & Inventory + CFO |

## 9. Physical Security, Secure Transit & Insurance Governance
* **Biometric / Badge Vault Access:** Serialized vaults (Zone B) require individual badge/ biometric entry logs and dual-custody key/ code control outside operating hours.
* **24/7 HD CCTV Coverage:** Continuous camera monitoring covering all loading bays, serialized vaults, and RMA cages, with 90 - 180 days of cloud/ NVR backup retention audited monthly.
* **Secure Inland Transport:** All container hauls and inter-hub transfers use vetted 3PL carriers equipped with live GPS tracking, tamper-evident numbered container/truck seals (recorded on dispatch waybills and verified at arrival), and vetted security escorts on high-risk corridors.
* **Marine & Goods-in-Transit (GIT) Insurance:** All international sea/air/road shipments must maintain active Marine/GIT insurance coverage. Any transit seal break or damage must be photographed and filed with insurers within 24 hours.

## 10. Import Customs Clearance, Install-Site Surplus & Capacity Gatekeeping
* **Pre-Arrival Customs & 3PL SLAs:** Clearing agents must submit regulatory pre-clearance filings (e.g., Form M / SONCAP in Nigeria, BESC / FERI in DRC, and renewable-energy duty exemptions) 7–10 days prior to vessel ETA to prevent port demurrage. 3PL haulers are governed by quarterly KPI scorecards (on-time delivery, zero damage, and seal integrity).
* **Destination Capacity Gatekeeping & JIT Arrival Window:** Before releasing shipments, Logistics verifies physical warehouse floor space, racking capacity, and charging power readiness. Regional FCL containers are consolidated to arrive 14 - 21 days prior to Need-By Date - protecting customs clearance buffers without eroding the 180-day battery shelf life.
* **Install-Site Surplus Return Loop (48-Hour Rule):** Unused installation materials (cables, brackets, uncommissioned chargers) must be returned from new hub install sites to the regional Central Warehouse and scanned back into Odoo within 48 hours of site commissioning.
* **Scalable Team Expansion & 20-Point Monthly Compliance Audit:** New country launches deploy a standardized 4-role pod (Country Inventory Lead ---> Warehouse Storekeeper ---> QA/Refurb Technician ---> Hub Dispatch Coordinator), certified via hands-on Odoo scanning tests, fire-safety drills, deputy cross-training, and audited monthly using 20-point Warehouse Compliance Scorecard.

## 11. S&OP Alignment, Team Operating Cadence & Odoo Change-Control Governance
* **Weekly / Bi-Weekly S&OP Alignment Cadence:** Head of Logistics chairs a structured S&OP review with Commercial, Supply Chain Procurement, and Finance to lock rolling 12-week hub rollout forecasts, optimize multi-country FCL container consolidation/ MOQs, and approve any air-vs-sea expedite trade-offs.
* **Multi-Country Warehouse Leadership Rhythm:** Structured cadence keeping every hub aligned:
  * **Daily (15 Mins):** Country Warehouse Supervisors lead shift stand-ups reviewing inbound dock-to-stock SLAs, scheduled hub dispatches, and RMA repair queues.
  * **Weekly (30 Mins):** Head of Logistics chairs a cross-country operational review tracking 5 Core KPIs (Demand Forecast Accuracy, Hub Stockout Rate, Cycle Count Accuracy, RMA Repair Turnaround Speed, and Port/ Lead-Time Delays).
* **Odoo Business Ownership & Change-Control Governance:** As business owner of Odoo inventory workflows, no ad-hoc changes may be made to product categories, valuation methods (AVCO vs. FIFO), scrap reasons, or warehouse location hierarchies without joint sign-off from Logistics, Technical, and Finance,.
