# Project Overview

## Title
**Food Ordering Behaviour and Consumer Trends: A Structured Analysis of Choices and Habits**

**Author:** Huzaifa Sheikh  
**GitHub Repository:** [SkillWallet](https://github.com/Huzaifa2526/SkillWallet)  
**Tableau Public Visualization:** [Live Interactive Dashboard](https://public.tableau.com/views/FoodOrderingBehaviourandConsumerTrend_Huzaifa/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)

---

## 1. Executive Summary

The on-demand food delivery market operates in an intensely competitive, dynamic environment characterized by fast-shifting consumer tastes, price sensitivity, and operational complexity. Food delivery platforms and restaurant aggregators require deep clarity into consumer ordering behavior, spending distributions, meal-timing dynamics, and fulfillment time consistency to optimize operational logistics, reduce churn, and drive profitability.

This project delivers an end-to-end Business Intelligence (BI) analytics solution built with **Tableau**, transforming 50,000 empirical food delivery transactions into interactive dashboards, strategic key performance indicators (KPIs), and executive stories.

---

## 2. Problem Statement

Modern food ordering platforms face multifaceted challenges:
1. **Unpredictable Demand Surges:** Difficulty in predicting peak order surges across specific meal types (lunch vs. dinner) and company categories.
2. **Geographic Variance:** Significant variations in consumer cuisine preferences across Tier-1 metropolitan hubs (e.g., Bangalore, Delhi, Mumbai, Hyderabad, Pune, Chennai).
3. **Operational Bottlenecks:** Delivery duration delays that risk degrading customer satisfaction ratings.
4. **Targeting Inefficiencies:** Lack of granular demographic segmentation (such as Age Groups and Restaurant Segments) leading to misallocated promotional discounts.

Without a centralized analytical framework, stakeholders are forced to rely on fragmented reporting, resulting in suboptimal delivery fleet utilization, ineffective restaurant partnerships, and lost customer lifetime value.

---

## 3. Project Objectives

- **Consolidate and Clean:** Ingest 50,000 transaction records, verifying data completeness, categorical consistency, and data types without synthetic bias.
- **Analyze Demand Distribution:** Dissect demand across 6 metropolitan cities, 6 major cuisines, 4 meal types, and 3 restaurant segments.
- **Identify Operational Patterns:** Measure order fulfillment times and correlate delivery durations with customer ratings.
- **Build Decision-Ready Visualizations:** Develop 13 focused worksheets, an executive dashboard (`Dashboard 1`), and a structured story (`Story 1`) enabling immediate root-cause inspection.
- **Deploy and Present:** Integrate the Tableau dashboard into a responsive web interface hosted via GitHub Pages, supplemented by demonstration resources.

---

## 4. Target Stakeholder Personas & Value Delivered

| Persona | Key Questions Addressed | Direct Value |
| :--- | :--- | :--- |
| **Business Analyst (Rahul Sharma)** | What cuisines drive the highest basket size? Where should marketing ad-spend be concentrated? | Identifies revenue contribution by meal type and demographic segments to steer customer acquisition strategies. |
| **Operations Manager (Priya Mehta)** | What is the average delivery duration? Which cities face high delivery latency during peak dinner hours? | Evaluates delivery time distributions to allocate delivery driver capacity and minimize transit bottlenecks. |
| **Customer Experience / End Consumer (Neha Reddy)** | How do meal types impact customer satisfaction ratings? Are discount campaigns improving loyalty? | Highlights customer satisfaction scores and repeat-order drivers to optimize service quality and user retention. |

---

## 5. Technology Stack

- **Analytics & BI:** Tableau Desktop 2026.2+ / Tableau Public Cloud
- **Data Engine:** Tableau Hyper In-Memory Data Extract Engine
- **Data Storage & Pipeline:** CSV / Google Drive Ingestion
- **Web Interface:** HTML5, Modern CSS3 (CSS Grid & Flexbox), Vanilla JavaScript (ES6+)
- **Verification & Testing:** Python 3.14 (Validation Suite `validate_workbook.py`, ElementTree XML Parser, SHA-256 Hashing)
- **Version Control & Hosting:** Git, GitHub, GitHub Pages
