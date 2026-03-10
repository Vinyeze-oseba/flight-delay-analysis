# ✈️ US Flight Delay Analysis 2023

A complete data analyst portfolio project analysing 551 US domestic 
flights across 8 major airlines and 15 airports throughout 2023.

## 📊 Key Findings

- **Worst Airline:** Spirit Airlines — 49.2% delay rate
- **Best Airline:** Delta Air Lines — only 9.2% delay rate
- **Worst Month:** June — 18.0 mins average delay
- **Best Month:** September — only 2.0 mins average delay
- **Most Delayed Route:** LAS → LAX — 20.7 mins average delay
- **Top Cancellation Cause:** Carrier fault (47.6% of cancellations)
- **On Time Rate:** 59.5% of all flights arrived on time

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| PostgreSQL | Database, data cleaning, SQL analysis |
| Python | pandas, matplotlib, seaborn charts |
| Claude AI | Interactive HTML dashboard |
| VS Code | Python development environment |
| GitHub | Version control and portfolio hosting |

## 📁 Project Files

| File | Description |
|------|-------------|
| flights_raw.csv | Original dirty dataset (552 rows) |
| flights_clean.csv | Cleaned dataset after SQL processing |
| flight_cleaning.sql | All SQL cleaning and analysis queries |
| flight_charts.py | Python code for generating charts |
| flight_dashboard.html | Interactive dashboard (open in browser) |
| Flight_Analysis_Report.docx | Full professional analysis report |

## 📈 Charts

- Airline Delay Rate comparison
- Monthly delay trends across 2023
- On time performance breakdown
- Top 8 most delayed routes

## 🔍 Data Quality Issues Found & Fixed

- 1 completely empty row → deleted
- 12 negative distance values → fixed with ABS()
- 4 impossible delay values (999+) → set to NULL
- Inconsistent airline name casing → fixed with INITCAP()
- 14 missing on_time values → flagged as Unknown

## 👤 Author

**Oghenevinteze Oseba**  
Aspiring Data Analyst | SQL | Python | Power BI  
github.com/Vinyeze-oseba
