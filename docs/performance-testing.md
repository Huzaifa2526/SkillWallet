# Performance Testing and Technical Audit

This document details the performance testing, data integrity verification, and web asset audit conducted on the project artifacts.

---

## 1. Automated Tableau Workbook Validation Suite

The integrity of the Tableau packaged workbook (`Huzaifa_Sheikh_Food_Ordering_Behaviour_and_Consumer_Trend.twbx`) was evaluated using `validate_workbook.py`.

### Test Suite Execution Output
```
=== FINAL WORKBOOK VALIDATION ===
[PASS] Zip package integrity test: OK
[PASS] Hyper extract integrity: 100% bit-for-bit match (SHA256: a89ae164911088ef60ccc075e8680aeb459f2ff91f68ecc326466a9f107ac7ef)
[PASS] XML well-formedness: OK
[PASS] Worksheets: All 13 intact and identical in order
[PASS] Dashboards & Storyboards: All 2 intact: ['Dashboard 1', 'Story 1']
[PASS] Story points: All 7 intact
[PASS] Columns and calculations: All 90 intact and identical
[PASS] Calculation formulas: All 4 intact and identical

ALL 14 VALIDATION CRITERIA VERIFIED AND PASSED SUCCESSFULLY.
```

### Metrics Verified:
- **Zip Archive Compression:** Deflate compression verified with zero CRC errors (`testzip()` returned `None`).
- **Data Engine Hash:** The extracted Hyper database matches the validated source byte-for-byte.
- **XML Schema:** Evaluated using Python's `xml.etree.ElementTree` parser; zero malformed tags or encoding anomalies.

---

## 2. Web Interface & Embed Performance Audit

The `/demo/` static web client was evaluated for lightweight, responsive execution:

| Metric | Measured Value | Standard Target | Assessment |
| :--- | :--- | :--- | :--- |
| **HTML Payload Size (`demo/index.html`)** | $\approx 25$ KB | $< 100$ KB | Excellent |
| **CSS Stylesheet Size (`demo/style.css`)** | $\approx 15$ KB | $< 50$ KB | Lightweight & Minimized |
| **Client JS Size (`demo/script.js`)** | $\approx 8$ KB | $< 50$ KB | Zero external runtime dependencies |
| **External JS Libraries** | 0 (Pure Vanilla JS) | Minimal | No framework overhead |
| **Tableau Embed Load Strategy** | Deferred / On-Demand iframe | Asynchronous | Zero blocking of initial render |
| **Responsive Breakpoints** | 480px, 768px, 1024px, 1280px | Mobile-friendly | Fluid Grid & Flexbox |
| **Broken Link Check** | 0 broken internal/external links | 0 errors | Verified |

---

## 3. Accessibility & Usability Standards (a11y)

- **Semantic Tags:** Structured with proper `<header>`, `<nav>`, `<main>`, `<section>`, and `<footer>` semantics.
- **Color Contrast:** Deep navy/slate background (`#0b0f19`) paired with high-contrast text (`#ffffff` and `#cbd5e1`), satisfying WCAG AA standard ($\ge 4.5:1$).
- **Responsive Viewport:** Meta tag configured with `width=device-width, initial-scale=1.0`.
- **Keyboard Navigation:** Native link and button tab indexing preserved with visible `:focus-visible` styling.
