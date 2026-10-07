# Data Preparation and Quality Audit

## 1. Source Dataset Overview

- **Dataset File:** `food_ordering_behaviour_dataset.csv`
- **Total Rows:** `50,000` records
- **Total Columns:** `19` attributes
- **Extract Format:** High-performance Tableau Hyper Extract (`.hyper`)
- **Extract Checksum (SHA-256):**  
  `a89ae164911088ef60ccc075e8680aeb459f2ff91f68ecc326466a9f107ac7ef`

---

## 2. Complete Field Dictionary

The 19 attributes present in the verified dataset are documented below:

| # | Field Name | Data Type | Tableau Role | Description | Sample Cardinality |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `order_id` | Integer | Dimension | Unique transaction identifier | 50,000 unique values |
| 2 | `user_id` | Integer | Dimension | Unique customer profile ID | 8,933 distinct users |
| 3 | `age` | Integer | Measure | Customer age in years | 27 distinct age points |
| 4 | `city` | String | Dimension | Delivery metro location | 6 cities (Bangalore, Delhi, Mumbai, Hyderabad, Pune, Chennai) |
| 5 | `order_time` | String | Dimension | Time of day placement slot | 4 time slots |
| 6 | `day_type` | String | Dimension | Calendar day category | 2 categories (Weekday, Weekend) |
| 7 | `cuisine` | String | Dimension | Cuisine style of the order | 6 types (North Indian, South Indian, Chinese, Italian, Mexican, Fast Food) |
| 8 | `meal_type` | String | Dimension | Meal classification | 4 categories (Breakfast, Lunch, Dinner, Snack) |
| 9 | `restaurant_type` | String | Dimension | Restaurant segment category | 3 segments (Fine Dining, Fast Casual, Street Food) |
| 10 | `order_value` | Integer | Measure | Total bill amount in INR (₹) | 2,572 distinct monetary points |
| 11 | `discount_applied`| String | Dimension | Promotional discount status | 2 values (Yes, No) |
| 12 | `delivery_fee` | Integer | Measure | Delivery charge in INR (₹) | 80 distinct monetary points |
| 13 | `time_taken_to_order`| Integer | Measure | Order-to-delivery time in minutes | 14 distinct durations |
| 14 | `rating_given` | Integer | Measure | Customer rating score (1 to 5) | 5 discrete values |
| 15 | `is_repeat_order` | String | Dimension | Repeat customer indicator | 2 values (Yes, No) |
| 16 | `mood` | String | Dimension | Reported customer sentiment | 4 distinct moods |
| 17 | `hunger_level` | String | Dimension | Perceived hunger level | 3 levels (Low, Medium, High) |
| 18 | `company` | String | Dimension | Customer ordering context | 4 categories (Corporate, Individual, Family, Friends) |
| 19 | `rainy_weather` | String | Dimension | Weather condition indicator | 2 values (Yes, No) |

---

## 3. Data Integrity & Validation Verification

Completeness and structural fidelity were verified through automated checks:

- **Row Count Verification:** Exact count of `order_id` verified at `50,000` (`COUNT(order_id) = 50,000`).
- **Null Value Assessment:** Core analytical dimensions (`city`, `cuisine`, `meal_type`, `company`, `restaurant_type`) contained zero null or unmapped tokens.
- **Data Type Alignment:** Measures (`order_value`, `delivery_fee`, `rating_given`, `age`, `time_taken_to_order`) mapped to continuous integers; categorical labels mapped to strings.
- **Extract Integrity:** Byte-level integrity confirmed against the master original extract.

---

## 4. Calculated Fields & Binning

To facilitate structured demographic and operational segmentations, the following bins and calculations were applied:

### Age Group Binning (`[Age (bin)]`)
- **Formula:** Binning on continuous dimension `[age]`.
- **Purpose:** Converts granular age values into discrete age groups:
  - $\le 20$ years: Student / Child cohort
  - $21 - 30$ years: Young Adults / Gen Z
  - $31 - 40$ years: Working Professionals / Millennials
  - $> 40$ years: Mature Adults
- **Business Rationale:** Enables cross-tabulation of culinary preference by life stage without cluttering visual axes with 27 individual age ticks.

### Delivery Time Binning (`[Time Taken To Order (bin)]`)
- **Formula:** Binning on continuous dimension `[time_taken_to_order]`.
- **Purpose:** Segregates delivery durations into uniform intervals to evaluate fleet performance consistency across rush-hour meal windows.
