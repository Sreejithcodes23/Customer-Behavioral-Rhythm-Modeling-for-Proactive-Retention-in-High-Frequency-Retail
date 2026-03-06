# Methodology

## Overview
This project models customer purchase rhythm in high-frequency retail environments to detect behavioral deviation and predict expected purchase timing. The system computes daily behavioral scores for each customer and identifies early retention risk.

The framework combines historical purchase patterns with predictive modeling to estimate the expected purchase interval and measure deviations from this expected behavior.

---

## Behavioral Rhythm Modeling

Customers typically follow a purchase rhythm based on their historical buying patterns. Instead of predicting a specific future purchase date, this framework estimates the **expected interval between purchases** and measures how far the current behavior deviates from that expected rhythm.

The system produces two primary behavioral metrics:

- **Predicted Next Purchase Timing (NPT)**
- **Behavioral Deviation Score (BDS)**

These metrics are computed daily using a behavioral scoring pipeline.

---

## Predicted Next Purchase Timing (NPT)

NPT represents the expected time gap between consecutive purchases for a customer.

A machine learning model is trained using historical purchase behavior to estimate the expected purchase interval based on behavioral features such as:

- historical purchase frequency
- average purchase interval
- recent purchase activity

The trained model predicts the expected gap between purchases for each customer.

The predicted value is stored as:
predicted_npt

Interpretation example:

If `predicted_npt = 9` and the last purchase was today, the customer is expected to make their next purchase approximately 9 days later.

---

## Behavioral Deviation Score (BDS)

The Behavioral Deviation Score measures how much the customer's current purchase gap deviates from their expected purchase rhythm.

The deviation is computed as:
bds = days_since_last_purchase / predicted_npt

Interpretation:

| BDS | Meaning |
|----|----|
| < 1 | Customer is purchasing earlier than expected |
| ≈ 1 | Customer is following expected rhythm |
| > 1 | Customer is delaying purchases |
| >> 1 | Strong behavioral deviation |

---

## Risk Segmentation

Customers are segmented into behavioral states based on BDS values.

| BDS Range | Risk Bucket |
|----|----|
| BDS < 0.8 | early |
| 0.8 ≤ BDS ≤ 1.2 | on_time |
| 1.2 < BDS ≤ 1.8 | mild_delay |
| BDS > 1.8 | high_delay |

This segmentation helps identify customers whose purchase behavior is diverging from their expected rhythm.

---

## Priority Score

To prioritize retention interventions, a **priority score** is computed using both deviation magnitude and expected purchase cadence.
priority_score = bds × (1 / predicted_npt)

This ensures that:

- customers with high deviation
- customers expected to purchase soon

receive higher intervention priority.

---

## Overdue Customer Detection

A customer is considered overdue when their observed purchase gap exceeds the predicted purchase interval.
days_since_last_purchase > predicted_npt

These customers have exceeded their expected purchase timing and may require retention intervention.

---

## Daily Behavioral Scoring Pipeline

The system runs a daily ETL pipeline that:

1. Extracts latest order data
2. Generates behavioral features
3. Predicts next purchase timing using the trained model
4. Computes BDS and priority score
5. Assigns risk buckets
6. Saves the daily snapshot to the database

Each run produces a **customer behavioral snapshot** stored in:
customer_behavior_score

Each record represents one customer at a specific snapshot date.

---

## Monitoring and Visualization

A Power BI dashboard is used to monitor behavioral health of the customer base using:

- active customers
- high-risk customers
- overdue customers
- average BDS
- predicted purchase timing trends
- risk segmentation
- priority distribution

This allows early detection of behavioral drift and proactive retention action.

---
