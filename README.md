# Customer Behavioral Rhythm Modeling for Proactive Retention in High-Frequency Retail

## Overview
This project models customer purchase rhythm in high-frequency retail by predicting expected purchase cadence and measuring behavioral deviation over time.  
It introduces a daily customer behavioral scoring framework using **Predicted Next Purchase Timing (NPT)** and **Behavioral Deviation Score (BDS)** to identify early retention risk and purchase timing breaches.

The project includes a behavioral scoring pipeline and an executive Power BI dashboard for monitoring customer rhythm stability and intervention priority.

---

## Business Problem
Traditional retention approaches rely on static RFM metrics and coarse churn labels. These methods fail to capture dynamic purchase rhythm and early behavioral drift.

This project addresses:
- When a customer is expected to purchase next  
- Whether the customer is deviating from their normal rhythm  
- Which customers have exceeded predicted purchase timing  
- Which customers require proactive retention action  

---

## Methodology

Customers are scored daily using historical order behavior to compute rhythm-based features:

**Mean Purchase Gap (`mean_gap`)**  
Average days between purchases for each customer.

**Days Since Last Purchase (`days_since_last_purchase`)**  
Elapsed time since the most recent order at each snapshot date.

**Predicted Next Purchase Timing (`predicted_npt`)**  
Expected total interval between consecutive purchases for a customer.

**Behavioral Deviation Score (`bds`)**  
Deviation of current purchase gap from expected rhythm.

**Risk Bucket (`risk_bucket`)**  
Behavioral state based on deviation level:
- early
- on_time
- mild_delay
- high_delay

**Priority Score (`priority_score`)**  
Urgency metric combining deviation and purchase timing:
priority_score = bds × (1 / predicted_npt)

**Overdue Customers**  
Customers whose observed gap exceeds predicted timing:
days_since_last_purchase > predicted_npt

---

## Data Pipeline
A daily ETL pipeline computes behavioral scores for each customer and stores them in a snapshot table:

Each record represents one customer at one snapshot date.

Features include:

- userid  
- snapshot_date  
- days_since_last_purchase  
- mean_gap  
- bds  
- predicted_npt  
- priority_score  
- risk_bucket  
- total_orders  
- orders_last_30  
- total_spend  
- avg_order_value  
- spend_last_30  

---

## Dashboard

An executive Power BI dashboard provides behavioral retention monitoring:

**Key KPIs**
- Active Customers
- High Risk Customers
- Overdue Customers (%)
- Average BDS
- Average Predicted NPT

**Behavioral Monitoring**
- Risk distribution
- Priority segmentation
- Behavioral deviation trend
- Purchase cadence trend

The dashboard enables identification of rhythm instability and intervention priority.

![Executive Overview](dashboard/dashboard_screenshots/executive_overview.png)

---

## Key Insights Enabled
The framework detects:

- Growth in behavioral deviation
- Purchase cadence extension
- Customers exceeding predicted timing
- High-risk behavioral segments
- Retention intervention load

---

## Repository Structure
customer-behavioral-rhythm-retention/
│
├── data/
│   └── sample_customer_behavior_score.csv
│
├── src/
│   ├── features.py
│   ├── bds.py
│   ├── npt.py
│   ├── priority.py
│   ├── snapshot.py
│   ├── save.py
│   └── scheduler.py
│
├── models/
│   └── npt_model.pkl
│
├── config/
│   └── db.py
│
├── dashboard/
│   ├── Executive_Overview.pbix
│   └── dashboard_screenshots/
│       └── executive_overview.png
│
├── docs/
│   ├── methodology.md
│   └── feature_definitions.md
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

---

## Technologies
- Python
- SQL / PostgreSQL
- Power BI
- Pandas

---

## Use Cases
This framework supports:

- Proactive retention campaigns  
- Purchase timing prediction  
- Behavioral drift monitoring  
- CRM prioritization  
- Customer lifecycle analytics  

---

## Author
**Sreejith Nair**  
Data Analytics / Data Science  

---

## Notes
This project demonstrates behavioral modeling and retention analytics using purchase rhythm rather than static recency-frequency metrics.
