# Project Demonstration and Walkthrough Guide

This guide describes the demonstration flow and outlines the recommended structure for presenting the project to academic or industry mentors.

---

## 1. Verified Video Demonstration Resources

The project incorporates native video demonstration recordings hosted directly within the repository and website without requiring external Google Drive access:

1. **Dataset Loading & Extraction Demonstration:**  
   - Local Asset Path: [`assets/videos/ingestion_demo_web.mp4`](file:///a:/Skill%20wallet%201/assets/videos/ingestion_demo_web.mp4)  
   - Web Player: Native HTML5 `<video>` embedded directly on the GitHub Pages demo website.
   - *Topic Covered:* Ingesting the 50,000-record dataset into Tableau Desktop, configuring the Hyper data engine, validating field data types, and setting up dimension binning.

2. **Publishing & Interactive Walkthrough Demonstration:**  
   - Local Asset Path: [`assets/videos/walkthrough_demo_web.mp4`](file:///a:/Skill%20wallet%201/assets/videos/walkthrough_demo_web.mp4)  
   - Web Player: Native HTML5 `<video>` embedded directly on the GitHub Pages demo website.
   - *Topic Covered:* Interactive exploration of `Dashboard 1`, cross-filtering across cities and cuisines, stepping through the 7 story points in `Story 1`, and validating author metadata on Tableau Public.

---

## 2. Recommended 5–7 Minute Mentor Presentation Agenda

When presenting the project to an evaluation committee, follow this structured 12-step script:

| Phase | Time | Agenda Item | Key Talking Points |
| :---: | :---: | :--- | :--- |
| **I** | 0:00–0:45 | 1. Introduction & Context | Introduce self (Huzaifa Sheikh), project title, and importance of data analytics in on-demand food delivery platforms. |
| **II** | 0:45–1:30 | 2. Problem Statement & Scope | Highlight the challenges of unpredictable meal surges, geographic taste variance, and delivery SLA maintenance. |
| **III** | 1:30–2:15 | 3. Dataset & Data Prep | Detail the 50,000 empirical rows, 19 fields, null-check validation, and creation of `[Age (bin)]` and `[Time Taken To Order (bin)]`. |
| **IV** | 2:15–3:30 | 4. Tableau Dashboard Demo | Live interaction on `Dashboard 1`: walk through the 4 executive KPIs, city vs. cuisine revenue heatmap, and age group distributions. |
| **V** | 3:30–4:30 | 5. Story Point Walkthrough | Step through the 7-point narrative in `Story 1`, illustrating how individual sheets answer discrete operational questions. |
| **VI** | 4:30–5:30 | 6. Stakeholder Scenarios | Map findings back to Rahul (Business Analyst), Priya (Operations Manager), and Neha (Customer Experience). |
| **VII**| 5:30–6:30 | 7. Web Integration & GitHub | Display the GitHub Pages live demo site, automated validation scripts (`validate_workbook.py`), and documentation repository. |
| **VIII**| 6:30–7:00 | 8. Conclusion & Q&A | Summarize key takeaways, operational recommendations, and invite mentor feedback. |
