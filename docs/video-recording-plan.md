# Project Video Recording and Demonstration Plan

This document provides a production guide for recording or reviewing the video demonstration for the **Food Ordering Behaviour and Consumer Trends** project.

---

## 1. Verified Live Video Demonstration Resources

The project features verified video demonstration assets hosted on Google Drive and embedded directly into the project demo website:

| Video Resource | File Asset Path | Player Integration | Focus |
| :--- | :--- | :--- | :--- |
| **Part 1: Dataset Ingestion & Setup** | `assets/videos/ingestion_demo_web.mp4` | Native HTML5 `<video>` / Direct MP4 | Ingestion of 50,000 records, data type auditing, null checks, and Hyper engine configuration. |
| **Part 2: Publishing & Walkthrough** | `assets/videos/walkthrough_demo_web.mp4` | Native HTML5 `<video>` / Direct MP4 | Tableau Public publication, interactive dashboard cross-filtering, and story exploration. |

---

## 2. Production Specifications for Walkthrough Recording

If re-recording or presenting live to an evaluation panel, use these exact parameters:

- **Presenter:** **Huzaifa Sheikh**
- **Narration Language:** English
- **Accent & Tone:** Natural Indian English (clear, calm, professional engineering/analytics student presentation style).
- **Target Duration:** 5 to 7 minutes.
- **Resolution:** 1080p Full HD ($1920 \times 1080$), 30 or 60 fps.
- **Recording Area:** Browser window showing the clean portfolio website (`demo/index.html`) and live embedded Tableau Public dashboard.
- **Audio Standards:** Clean voice microphone, zero distracting background music, no synthetic sound effects, consistent volume level.

---

## 3. Step-by-Step Recording Timeline

| Timestamp | Screen Navigation | Narration Focus |
| :---: | :--- | :--- |
| **00:00–00:30** | Homepage Hero & Navigation | Introduce self (Huzaifa Sheikh), project title, and role of visual analytics in food delivery. |
| **00:30–01:10** | Scroll to Problem & Objectives | Explain raw data limitations and outline the 6 core business objectives. |
| **01:10–01:50** | Scroll to Project Snapshot & Data | Detail the 50,000 empirical rows, 19 fields, null-check audit, and Hyper extract. |
| **01:50–02:30** | Scroll to Methodology Flow | Walk through the non-destructive pipeline from CSV to calculated fields and storyboards. |
| **02:30–04:20** | Live Tableau Dashboard Embed | Interactively demonstrate `Dashboard 1`: KPI cards, city vs. cuisine revenue heatmap, age group bar charts, meal type distributions, and delivery time histograms. |
| **04:20–05:10** | Scroll to Verified Key Insights | Highlight Bangalore volume dominance, regional Indian cuisine billing, and dinner revenue anchors. |
| **05:10–05:40** | Scroll to Technical Architecture | Explain data flow from local Tableau to Tableau Public cloud and GitHub Pages static hosting. |
| **05:40–06:20** | Scroll to Stakeholder Value Cards | Map findings to Rahul Sharma (Business Analyst), Priya Mehta (Operations Manager), and Neha Reddy (Customer). |
| **06:20–06:50** | Scroll to Footer / Repository | Highlight automated Python test suite (`validate_workbook.py`), MIT License, and invite mentor review. |

---

## 4. Narration Script Reference

The full verbatim narration script is documented in [`docs/video-walkthrough-script.md`](video-walkthrough-script.md).
