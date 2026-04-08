# 🧠 Customer Behavioral Rhythm Modeling for Proactive Retention

---

## 🚀 Overview

This project builds a **production-grade customer retention intelligence system** that models purchase behavior as a dynamic rhythm rather than static metrics.

It predicts **when a customer is expected to purchase next** and detects **behavioral deviations in real time**, enabling proactive retention strategies.

### 🔥 Key Capabilities

- 📊 Daily behavioral scoring pipeline  
- ⚡ Real-time prediction API (FastAPI)  
- 🖥️ Interactive app (Streamlit)  
- 📊 Executive dashboard (Power BI)  
- 🔁 MLflow-based model lifecycle management  
- 🐳 Dockerized microservices deployment  

---

## 💼 Business Problem

Traditional retention systems rely on:

- Static RFM metrics  
- Binary churn labels  

These approaches fail to capture **dynamic behavioral shifts**.

### This project answers:

- When will a customer purchase next?  
- Is the customer deviating from their normal behavior?  
- Which customers are overdue?  
- Who should be prioritized for retention?  

---

## 🧠 Core Concept: Behavioral Rhythm

Instead of treating customers as static entities, this system models:

Customer = Behavioral Pattern over Time

---

## ⚙️ Methodology

Customers are evaluated daily using historical transaction patterns.

### 🔑 Key Features

**Mean Purchase Gap (`mean_gap`)**  
Average interval between purchases (baseline behavior)

**Days Since Last Purchase (`days_since_last_purchase`)**  
Current behavioral state

**Predicted Next Purchase Timing (`predicted_npt`)**  
ML-based expected purchase interval

**Behavioral Deviation Score (`bds`)**

bds = days_since_last_purchase / mean_gap

**Priority Score**

priority_score = bds × (1 / predicted_npt)

---

## 🤖 Machine Learning (Advanced)

### 🔥 Segmented Modeling Approach

Instead of a single global model, the system uses **two specialized models**:

| Segment | Model |
|--------|------|
| Recent customers (`≤ 10 days`) | `npt_model_le_10` |
| Delayed customers (`> 10 days`) | `npt_model_gt_10` |

### 🎯 Why This Matters

Customer behavior differs significantly between:

- Active users → predictable patterns  
- Inactive users → irregular patterns  

👉 Segmentation improves accuracy and stability

---

## 🔄 Model Inference Logic

if days_since_last_purchase ≤ 10:
    use Model A
else:
    use Model B

---

## 🔬 A/B Testing (Business Validation)

The system includes an A/B testing framework to evaluate model impact.

### 🎯 Experiment Design

| Group | Strategy |
|------|--------|
| A (Control) | Random / baseline targeting |
| B (Treatment) | Model-based targeting (BDS + Priority) |

### 📊 Metrics

- Conversion rate  
- Retention uplift  
- Statistical significance (p-value)

👉 Validates whether **ML-driven targeting improves retention**

---

## ⚡ System Architecture

Batch Pipeline (ETL)
        ↓
   ML Models (Segmented)
        ↓
 ┌──────────────┬──────────────┐
 │              │              │
Batch        FastAPI        Streamlit
Pipeline        API            App
        ↓
   PostgreSQL DB
        ↓
   Power BI Dashboard

---

## 🔄 Data Pipeline

A daily ETL pipeline generates behavioral snapshots.

### Pipeline Steps

1. Data extraction from database  
2. Feature engineering  
3. Segmented model prediction  
4. Behavioral scoring (BDS, priority)  
5. Storage in database  

Each record = **customer × date snapshot**

---

## ⚡ Real-Time API (FastAPI)

Provides real-time insights:

- Predict next purchase timing  
- Compute behavioral deviation  
- Generate retention insights  

### Endpoint

POST /customer-insight

---

## 🖥️ Streamlit Application

- Real-time predictions  
- Customer insight visualization  
- API-based interaction  

---

## 📊 Power BI Dashboard

### KPIs

- Active Customers  
- High-Risk Customers  
- Overdue Customers (%)  
- Average BDS  
- Average Predicted NPT  

### Insights

- Behavioral drift trends  
- Risk segmentation  
- Priority distribution  
- Purchase cadence patterns  

---

## 🐳 Docker Deployment

The system is containerized into:

- FastAPI service  
- Streamlit app  

docker compose up --build

---

## 🗂️ Repository Structure

customer-behavioral-rhythm-retention/
│
├── app/
├── src/
├── models/
├── config/
├── dashboard/
├── docs/
│
├── log_model_mlflow.py
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn, XGBoost  
- FastAPI  
- Streamlit  
- PostgreSQL  
- Power BI  
- MLflow  
- Docker  

---

## 🎯 Use Cases

- Proactive retention campaigns  
- Behavioral drift detection  
- Purchase timing prediction  
- CRM prioritization  
- Customer lifecycle analytics  

---

## 💼 Key Highlights

- 🔥 End-to-end production ML system  
- 🔥 Segmented modeling (advanced ML design)  
- 🔥 Batch + real-time architecture  
- 🔥 A/B testing for business validation  
- 🔥 Fully containerized deployment  

---

## 👤 Author

**Sreejith Nair**  
Data Analytics | Data Science  

---

## 📝 Final Note

This project demonstrates a shift from:

Static analytics → Dynamic behavioral intelligence

enabling **data-driven, proactive customer retention strategies**.
