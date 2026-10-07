# Methodology and Analytical Framework

This document outlines the structured methodology adopted for the **Food Ordering Behaviour and Consumer Trends** project.

---

## 1. End-to-End Analytical Lifecycle

The methodology follows the standard Data Analytics Lifecycle, structured into six systematic phases:

```
┌─────────────────────────┐
│ 1. Business Framing     │  Define stakeholder questions, KPIs & operational goals
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 2. Data Ingestion       │  Collect 50,000 records from food_ordering_behaviour_dataset.csv
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 3. Data Validation      │  Type auditing, null check, cardinality check, checksum verification
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 4. Exploratory Analysis │  Tableau Hyper extract profiling, dimension binning, field calculations
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 5. Visualization Design │  13 Worksheets, 1 Dashboard, 1 Storyboard with interactive filtering
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ 6. Deployment & Audit   │  Tableau Public publication, GitHub Pages web integration, validation
└─────────────────────────┘
```

---

## 2. Quantitative Metric Formulations

Key business metrics were formulated to represent operational and financial health:

1. **Total Order Volume:**
   $$\text{Total Orders} = \text{COUNT}(\text{order\_id}) = 50,000$$

2. **Total Gross Revenue:**
   $$\text{Total Revenue} = \sum (\text{order\_value})$$

3. **Average Order Value (AOV):**
   $$\text{AOV} = \frac{\sum (\text{order\_value})}{\text{COUNT}(\text{order\_id})}$$

4. **Customer Satisfaction Index:**
   $$\text{Average Rating} = \frac{\sum (\text{rating\_given})}{\text{COUNT}(\text{rating\_given})}$$

5. **Fulfillment Efficiency:**
   Aggregated distribution of `time_taken_to_order` partitioned into continuous bins to examine delivery cycle predictability.

---

## 3. Dimensional Analysis Dimensions

The analysis explores seven cross-cutting analytical dimensions:
- **Temporal:** `order_time` (Morning, Afternoon, Evening, Night), `day_type` (Weekend, Weekday).
- **Geographic:** `city` (Bangalore, Delhi, Mumbai, Hyderabad, Pune, Chennai).
- **Product / Culinary:** `cuisine` (North Indian, South Indian, Chinese, Italian, Mexican, Fast Food).
- **Meal Category:** `meal_type` (Breakfast, Lunch, Dinner, Snack).
- **Entity Context:** `company` (Corporate vs. Individual), `restaurant_type` (Fine Dining, Fast Casual, Street Food).
- **Behavioral & Psychological:** `mood`, `hunger_level`, `discount_applied`, `is_repeat_order`, `rainy_weather`.
- **Demographic:** `age` grouped into targeted analytical cohorts (`Age (bin)`).
