# Detailed Visualization Catalog

The **Food Ordering Behaviour and Consumer Trends** workbook comprises 13 dedicated analytical worksheets that feed into the master executive dashboard and interactive story.

---

## 1. Executive KPI Cards

### Worksheet: `KPI - Total orders`
- **Chart Type:** KPI Text Card
- **Measure:** `COUNT(order_id)`
- **Value:** `50,000`
- **Business Question:** What is the cumulative transaction scale analyzed?
- **Interpretation:** Establishes the full volume sample baseline of 50,000 orders across all observed territories.

### Worksheet: `KPI - Total revenue`
- **Chart Type:** KPI Text Card
- **Measure:** `SUM(order_value)` (formatted in Indian Rupees ₹)
- **Business Question:** What is the total gross order value generated?
- **Interpretation:** Measures overall gross platform billing across all completed consumer food orders.

### Worksheet: `KPI - average rating`
- **Chart Type:** KPI Text Card
- **Measure:** `AVG(rating_given)`
- **Business Question:** What is the overall customer sentiment and quality score?
- **Interpretation:** Provides the high-level quality benchmark across meal orders, evaluating operational consistency.

### Worksheet: `KPI - order average value`
- **Chart Type:** KPI Text Card
- **Measure:** `AVG(order_value)` (formatted in Indian Rupees ₹)
- **Business Question:** What is the average basket size per transaction?
- **Interpretation:** Serves as a vital metric for unit economics and consumer willingness to spend.

---

## 2. Core Dimensional Visualizations

### 2. Flavours Across Cities (Heat Map / Matrix)
- **Worksheet:** `Flavours Across Cities` / `CIty vs Cuisine`
- **Rows:** `[city]` | **Columns:** `[cuisine]`
- **Color/Mark:** `SUM(order_value)`
- **Business Question:** Which cuisines generate the highest revenue within each metropolitan market?
- **Interpretation:** Reveals geographic taste profiles, showing heavy concentration in North Indian and South Indian cuisines across Bangalore, Delhi, and Mumbai.

### 3. Order Distribution by Age Group and Restaurant Segment
- **Worksheet:** `Order Distribution by Age Group and Restaurant Segment`
- **Rows:** `COUNT(order_id)` | **Columns:** `[Age (bin)]`
- **Color Mark:** `[restaurant_type]`
- **Business Question:** How do dining formats (Fine Dining, Fast Casual, Street Food) vary across age cohorts?
- **Interpretation:** Illustrates that mature adults and working professionals lean towards Fast Casual and Fine Dining, whereas younger cohorts drive volume in Fast Casual and Street Food.

### 4. Orders Across Company Type and Meal Type
- **Worksheet:** `Analysis of Orders Across Company Type and Meal Type`
- **Rows:** `[meal_type]` | **Columns:** `[company]`
- **Mark:** `COUNT(order_id)`
- **Business Question:** When do corporate vs. individual orders peak throughout the day?
- **Interpretation:** Shows concentrated spikes of corporate and group orders during lunch and dinner hours, highlighting high-value catering potential.

### 5. Customer Rating Analysis by Meal Type
- **Worksheet:** `Customer Rating Analysis by Meal Type`
- **Rows:** `AVG(rating_given)` | **Columns:** `[meal_type]`
- **Business Question:** Do specific meal windows suffer from degraded customer satisfaction?
- **Interpretation:** Evaluates rating distribution across Breakfast, Lunch, Dinner, and Snacks to pinpoint service consistency across different meal prep cycles.

### 6. Revenue Contribution by Meal Type
- **Worksheet:** `Revenue Contribution by Meal Type`
- **Rows:** `SUM(order_value)` | **Columns:** `[meal_type]`
- **Business Question:** Which meal times drive the majority of platform revenue?
- **Interpretation:** Confirms Dinner and Lunch as the primary gross merchandise value (GMV) drivers.

### 7. Customer Preferences Across Cuisines
- **Worksheet:** `Distribution of Customer Preferences Across Cuisines`
- **Rows:** `COUNT(order_id)` | **Columns:** `[cuisine]`
- **Business Question:** What is the overall popularity distribution among available cuisines?
- **Interpretation:** Demonstrates dominant customer affinity for traditional Indian culinary choices, with Chinese and Italian forming popular secondary segments.

### 8. Cities by Order Volume
- **Worksheet:** `Cities by Order Volume`
- **Rows:** `COUNT(order_id)` | **Columns:** `[city]`
- **Business Question:** Which metropolitan areas exhibit the highest customer demand?
- **Interpretation:** Highlights Bangalore and Delhi as the primary demand centers, guiding regional delivery fleet expansions.

### 9. Distribution of Delivery Time Across Orders
- **Worksheet:** `Distribution of Delivery Time`
- **Rows:** `COUNT(order_id)` | **Columns:** `[Time Taken To Order (bin)]`
- **Business Question:** How consistent and predictable are delivery turnaround times?
- **Interpretation:** Visualizes the standard normal distribution of order fulfillment, helping identify delivery SLA breach thresholds.
