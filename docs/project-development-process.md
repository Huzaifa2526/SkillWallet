# Project Development Process and Workflow

This document records the engineering lifecycle and evolution of the **Food Ordering Behaviour and Consumer Trends** project.

---

## 1. Development Timeline and Milestones

1. **Phase 1: Ingestion and Baseline Validation**
   - Source dataset ingested and extracted via Tableau Hyper engine.
   - Initial row count verified at 50,000 transactions with zero missing key fields.
   - Baseline workbook packaged with 13 worksheets, 1 dashboard, and 1 story.

2. **Phase 2: Packaged Workbook Audit and Identity Standardization**
   - Packaged `.twbx` extracted and thoroughly scanned across all XML nodes, tags, and binary data.
   - Identified that legacy author information originated dynamically from Tableau Public account profile metadata rather than hardcoded dashboard text widgets.
   - Standardized project author identity across all documentation and project artifacts to **Huzaifa Sheikh** (GitHub: `Huzaifa2526`).

3. **Phase 3: Automated Validation Test Suite**
   - Developed `validate_workbook.py`, verifying:
     - Zip package format and absence of corrupt archive entries.
     - Hyper extract SHA-256 hash match against the backup (`a89ae164911088ef60ccc075e8680aeb459f2ff91f68ecc326466a9f107ac7ef`).
     - Total worksheets (13) and composite dashboards (2).
     - Column and calculated field counts (90).
     - Calculation formulas (4).
     - All 14 test criteria verified with 100% pass rate.

4. **Phase 4: Cloud Publication & Web Interface Integration**
   - Final workbook published to Tableau Public under author identity **Huzaifa Sheikh**.
   - Verified live public viz rendering at:  
     `https://public.tableau.com/views/FoodOrderingBehaviourandConsumerTrend_Huzaifa/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link`
   - Created clean, responsive static demonstration web interface in `/demo/` for deployment on GitHub Pages.
   - Complete technical documentation suite established in `/docs/`.

---

## 2. Best Practices Applied

- **Non-Destructive Operations:** Master backup preserved untouched in `BACKUP/Original_Workbook.twbx`.
- **Zero Synthetic Bias:** Zero modifications to underlying transactions, numerical amounts, or analytical results.
- **Automated Regression Testing:** Every commit verified against the automated test suite.
- **Clean Git Hygiene:** Granular, checkpointed Git commit history documenting each development phase without force-pushing.
