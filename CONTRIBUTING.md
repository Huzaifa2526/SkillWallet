# Contributing Guidelines

Thank you for your interest in contributing to the **Food Ordering Behaviour and Consumer Trends** analytics project.

## How to Review or Reproduce the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Huzaifa2526/SkillWallet.git
   cd SkillWallet
   ```

2. **Explore the Tableau Workbook:**
   - Locate the packaged workbook: `Huzaifa_Tableau_Project/Huzaifa_Sheikh_Food_Ordering_Behaviour_and_Consumer_Trend.twbx`.
   - Open using **Tableau Desktop 2026.2+** or **Tableau Public** (free application).
   - Alternatively, view the live interactive dashboards directly on [Tableau Public](https://public.tableau.com/views/FoodOrderingBehaviourandConsumerTrend_Huzaifa/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link).

3. **Validate Workbook Integrity:**
   - Execute the validation script to verify package structure and data integrity:
     ```bash
     python validate_workbook.py
     ```

4. **Run the Demo Website Locally:**
   - Open `demo/index.html` in any modern web browser or run a local lightweight server:
     ```bash
     python -m http.server 8000
     ```
   - Navigate to `http://localhost:8000/demo/`.

## Proposing Improvements

- **Bug Reports & Inquiries:** Open an issue on GitHub detailing the observed problem or inquiry.
- **Pull Requests:**
  1. Fork the repository and create a feature branch (`git checkout -b feature/improvement`).
  2. Ensure no analytical formulas or raw dataset rows are altered unintentionally.
  3. Validate all changes against `validate_workbook.py`.
  4. Submit a clear Pull Request describing your methodology and rationale.

## Code of Conduct

Maintain academic integrity, respectful discourse, and constructive feedback across all interactions.
