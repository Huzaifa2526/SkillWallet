# Executive Dashboard and Story Architecture

## 1. Overview of `Dashboard 1`

`Dashboard 1` is an integrated executive dashboard designed to give stakeholders a high-level and granular view of platform operations on a single unified canvas.

### The "2-Minute Mentor Evaluation" Walkthrough
When an evaluator or executive opens `Dashboard 1`, they can extract five critical insights within two minutes:
1. **Top-Line Health (0–30s):** The four prominent KPI cards immediately communicate overall volume (50,000 orders), platform revenue, average basket size, and overall satisfaction rating.
2. **Geographic Hotspots (30–60s):** The city and cuisine charts pinpoint Bangalore and Delhi as the primary demand and revenue drivers.
3. **Product & Meal Trends (60–90s):** The meal-type and revenue breakdown shows Dinner and Lunch as core revenue anchors.
4. **Demographic & Context Clues (90–110s):** The Age Group vs. Restaurant Segment distribution illustrates that adult consumers dominate order volume.
5. **Operational Health (110–120s):** The delivery duration histogram confirms operational stability and standard fulfillment time consistency.

---

## 2. Dashboard Layout Structure

```
┌────────────────────────────────────────────────────────────────────────┐
│                          EXECUTIVE KPI STRIP                           │
│  [ Total Orders ]   [ Total Revenue ]   [ Avg Basket ]   [ Avg Rating ]│
├───────────────────────────────────┬────────────────────────────────────┤
│   Flavours Across Cities          │  Order Distribution by Age Group   │
│   (City vs Cuisine Revenue)       │  & Restaurant Segment              │
├───────────────────────────────────┼────────────────────────────────────┤
│   Customer Preferences by Cuisine │  Top Cities by Order Volume        │
├───────────────────┬───────────────┴────┬───────────────────────────────┤
│  Revenue by Meal  │  Delivery Time     │  Orders by Company & Meal     │
│  Contribution     │  Distribution      │  Type Analysis                │
└───────────────────┴────────────────────┴───────────────────────────────┘
```

- **Sizing Mode:** Fixed / Responsive automatic grid with auto-generated responsive mobile phone layout (`devicelayout` enabled for vertical mobile scrolling).
- **Interactive Filtering:** Cross-filtering enabled across dimensions (clicking on a city filters all associated charts for targeted regional drill-downs).

---

## 3. Story Architecture (`Story 1`)

`Story 1` organizes the findings into an interactive 7-point narrative walkthrough:

| Point # | Story Point Caption | Captured Worksheet | Narrative Goal |
| :---: | :--- | :--- | :--- |
| **1** | `City vs Cuisine` | `CIty vs Cuisine` | Frame regional culinary preferences across major metros. |
| **2** | `Orders by Age Group` | `Order Distribution by Age Group and Restaurant Segment` | Demonstrate how demographic cohorts drive restaurant segment choice. |
| **3** | `Cuisine Preference Distribution` | `Distribution of Customer Preferences Across Cuisines` | Benchmark relative popularity across culinary categories. |
| **4** | `Company Type - Meal Type Orders`| `Analysis of Orders Across Company Type and Meal Type` | Highlight corporate ordering surges during lunch and dinner. |
| **5** | `Meal Type VS Customer Rating` | `Customer Rating Analysis by Meal Type` | Evaluate customer satisfaction consistency across dining windows. |
| **6** | `Top 5 Cities by Order Volume` | `Cities by Order Volume` | Identify lead metropolitan markets for fleet scaling. |
| **7** | `Delivery Time Distribution` | `Distribution of Delivery Time` | Review operational delivery SLA adherence and consistency. |
