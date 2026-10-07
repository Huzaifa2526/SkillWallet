# Web Integration Architecture and Strategy

This document outlines how the analytical Tableau artifacts are integrated into web platforms, distinguishing between the static production implementation and potential future full-stack extensions.

---

## 1. Implemented Production Architecture (Static Web Integration)

To ensure zero hosting costs, high availability, and seamless deployment on **GitHub Pages**, the project implements a clean client-side integration architecture:

```
┌─────────────────────────────────┐
│     User Browser / Client       │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│  GitHub Pages Static Web Demo   │  Hosted at:
│       (demo/index.html)         │  https://huzaifa2526.github.io/SkillWallet/
└───────┬─────────────────┬───────┘
        │                 │
        ▼                 ▼
┌──────────────────┐   ┌──────────────────────────────┐
│  Tableau Public  │   │  Demonstration Video Embeds  │
│ Cloud Embed API  │   │   (Google Drive Media Player)│
└──────────────────┘   └──────────────────────────────┘
```

### Integration Details
1. **Live Visualization Embedding:**
   - Embedded using Tableau Public's optimized JavaScript embed API and iframe container.
   - Live URL:
     `https://public.tableau.com/views/FoodOrderingBehaviourandConsumerTrend_Huzaifa/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link`
   - Parameters:
     - `showVizHome=no`
     - `embed=true`
     - Sizing mode dynamic container with 100% responsive width and 780px viewport height.

2. **Demonstration Video Players:**
   - Embedded via native HTML5 `<video controls playsinline preload="metadata">`:
     - Ingestion Demo: `assets/videos/ingestion_demo_web.mp4` (H.264, web-optimized faststart, 3.75 MB)
     - Publishing / Walkthrough Demo: `assets/videos/walkthrough_demo_web.mp4` (H.264, web-optimized faststart, 7.66 MB)
   - Equipped with direct download buttons for evaluators.

---

## 2. Distinction: Implemented vs. Planned / Extended Architectures

| Layer | Implemented in Current Repository | Extended / Planned Full-Stack Architecture |
| :--- | :--- | :--- |
| **Hosting Model** | **Static GitHub Pages** (HTML5/CSS3/Vanilla JS) | Dynamic Container / Cloud Platform (AWS, Heroku) |
| **Backend Framework** | **None (Pure Static Client)** | Python Flask / FastAPI REST API |
| **Data Querying** | Client-side Tableau Public Cloud API | Direct SQLAlchemy / Pandas database connectivity |
| **Authentication** | Publicly accessible portfolio showcase | JWT Role-Based Access Control (RBAC) |
| **Maintenance Cost** | **$0.00 / Zero server management overhead** | Requires continuous VM/server hosting & compute |

*Clarification for Evaluators:* No Python Flask or Node.js server is required or running in this repository; the implementation is intentionally designed as an accessible, performant static web demonstration leveraging Tableau Public Cloud APIs.
