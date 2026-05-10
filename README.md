# Telangana-PDS-Analytics-Multi-Dimensional-Shop-Performance-Clustering-and-Anomaly-Profiling
# Telangana PDS Analytics Dashboard

## 📌 Project Title
Telangana PDS Analytics: Multi-Dimensional Shop Performance Clustering and Anomaly Profiling

---

## 🎯 Objective
To analyze Fair Price Shop (FPS) performance in Telangana using transactional, card status, and location data to:
- Identify shop performance patterns
- Detect anomalies (fraud or unusual behavior)
- Segment shops using machine learning
- Build an interactive Streamlit dashboard

---

## 📊 Dataset Used
- Transactions Data (2024–2025 monthly records)
- Card Status Data (ration card details)
- FPS Location Data (latitude & longitude, shop info)

---

## 🧠 Techniques Used
- Data Cleaning & Merging
- Feature Engineering
- K-Means Clustering
- DBSCAN (Anomaly Detection)
- PCA (Dimensionality Reduction)

---

## 📈 Features Engineered
- utilization_ratio
- portability_ratio
- transaction_gap

---

## 🤖 Machine Learning Models
- KMeans → Shop clustering (behavior groups)
- DBSCAN → Anomaly detection (-1 clusters)
- PCA → Visualization of high-dimensional data

---

## 📊 Dashboard Features (Streamlit)
- Cluster distribution chart
- PCA visualization
- Interactive shop map
- Shop search by shop number
- Anomaly detection view

---

## 🚀 How to Run Project

```bash
pip install -r requirements.txt
streamlit run telangana_ration.py
