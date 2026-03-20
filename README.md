# Customer Behavioral Rhythm Modeling for Proactive Retention in High-Frequency Retail

---

## 🚀 Overview

This project models **customer purchase rhythm** in high-frequency retail by predicting expected purchase cadence and detecting behavioral deviation over time.

It introduces a **production-grade retention intelligence system** powered by:

* 📊 **Batch behavioral scoring pipeline**
* ⚡ **Real-time prediction API (FastAPI)**
* 🖥️ **Interactive dashboard (Streamlit + Power BI)**
* 🔁 **MLflow-based model lifecycle management**
* 🐳 **Dockerized deployment**

The system enables **early detection of retention risk** and supports proactive customer engagement strategies.

---

## 💼 Business Problem

Traditional retention models rely on static RFM metrics and binary churn labels, which fail to capture **dynamic behavioral patterns**.

This project solves:

* When is a customer expected to purchase next?
* Is the customer deviating from their natural purchase rhythm?
* Which customers are overdue?
* Who requires immediate retention intervention?

---

## 🧠 Methodology

Customers are evaluated daily using behavioral features derived from historical transactions.

### Key Features

**Mean Purchase Gap (`mean_gap`)**
Average interval between purchases.

**Days Since Last Purchase (`days_since_last_purchase`)**
Time elapsed since last transaction.

**Predicted Next Purchase Timing (`predicted_npt`)**
ML model prediction of expected purchase interval.

**Behavioral Deviation Score (`bds`)**
Deviation between observed and expected purchase behavior.

**Risk Bucket (`risk_bucket`)**

* early
* on_time
* mild_delay
* high_delay

**Priority Score (`priority_score`)**

```
priority_score = bds × (1 / predicted_npt)
```

**Overdue Customers**

```
days_since_last_purchase > predicted_npt
```

---

## ⚙️ System Architecture

```
Batch Pipeline (ETL) ───────────────┐
                                   │
                                   ▼
                           MLflow Model Registry
                                   │
                 ┌─────────────────┴─────────────────┐
                 │                                   │
        Batch Predictions                     Real-Time API
        (Daily Pipeline)                     (FastAPI)
                 │                                   │
                 ▼                                   ▼
           PostgreSQL DB                    Streamlit App
                 │
                 ▼
          Power BI Dashboard
```

---

## 🔄 Data Pipeline

A daily pipeline processes customer transactions and generates behavioral snapshots.

### Pipeline Steps:

1. Data extraction from database
2. Feature engineering
3. Model prediction (MLflow production model)
4. Behavioral scoring (BDS, priority)
5. Storage in snapshot table

Each record represents a **customer-day snapshot**.

---

## 🤖 Machine Learning

### Model: Next Purchase Timing (NPT)

* Predicts expected purchase interval
* Used as baseline for behavioral deviation

### MLflow Integration

* Model versioning and tracking
* Alias-based deployment (`production`)
* Decoupled model serving

```python
model = mlflow.pyfunc.load_model("models:/NPT_Model@production")
```

### Key Benefits:

* No hardcoded `.pkl` files
* Seamless model updates
* Easy rollback to previous versions
* Reproducibility

---

## ⚡ Real-Time API (FastAPI)

Provides real-time customer predictions:

* Predict NPT
* Calculate Behavioral Deviation Score
* Generate customer insights

### Example Endpoint:

```
POST /customer-insight
```

---

## 🖥️ Streamlit Application

Interactive UI for:

* Input-based prediction
* Customer insight visualization
* Real-time model inference

---

## 📊 Dashboard (Power BI)

### Key KPIs:

* Active Customers
* High Risk Customers
* Overdue Customers (%)
* Average BDS
* Average Predicted NPT

### Insights:

* Behavioral drift trends
* Risk segmentation
* Priority distribution
* Purchase cadence patterns

---

## 🐳 Docker Deployment

The system is fully containerized:

* FastAPI service
* Streamlit application

Run locally:

```bash
docker compose up --build
```

---

## 🗂️ Repository Structure

```
customer-behavioral-rhythm-retention/
│
├── app/                     # FastAPI application
├── src/                     # Pipeline modules
├── models/                  # Trained models
├── config/                  # Database configuration
├── dashboard/               # Power BI files
├── docs/                    # Documentation
│
├── log_model_mlflow.py      # Model logging script
│
├── main.py                  # Pipeline entry point
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies

* Python
* Pandas / NumPy
* Scikit-learn
* FastAPI
* Streamlit
* PostgreSQL
* Power BI
* MLflow
* Docker

---

## 🎯 Use Cases

* Proactive customer retention
* Behavioral drift detection
* Purchase timing prediction
* CRM prioritization
* Customer lifecycle analytics

---

## 💼 Key Highlights

* End-to-end production-grade ML system
* Batch + real-time inference architecture
* MLflow-based model lifecycle management
* Fully containerized deployment
* Business-focused analytics and insights

---

## 👤 Author

**Sreejith Nair**
Data Analytics | Data Science 

---

## 📝 Notes

This project demonstrates a shift from static RFM-based analysis to **dynamic behavioral modeling**, enabling more accurate and proactive retention strategies.
