# 🚀 AI Stock Intelligence Platform

An **end-to-end AI-powered stock prediction system** leveraging **Deep Learning (LSTM, GRU, Transformer)** with a **FastAPI backend** and **interactive Streamlit dashboard**, deployed on **Render and Streamlit Cloud**.

---

## 🌐 Live Deployments

* 🔗 **Backend API:** [https://ai-stock-intelligence-backend1.onrender.com](https://ai-stock-intelligence-backend1.onrender.com)
* 🎨 **Frontend App:** [https://ai-stock-intelligence-platform-2vamvenawyivsbkzmo5ufe.streamlit.app/](https://ai-stock-intelligence-platform-2vamvenawyivsbkzmo5ufe.streamlit.app/)

---

## 📌 Project Overview

A production-grade **AI financial analytics system** designed to forecast stock prices and generate actionable trading signals using multiple deep learning architectures.

The platform provides **end-to-end ML pipeline automation**, from data ingestion to prediction and visualization.

---

## 🔥 Key Capabilities

* 📈 Stock price forecasting using deep learning models
* ⚖️ Automated Buy / Sell / Hold signal generation
* 🤖 Multi-model AI system (LSTM, GRU, Transformer, Ensemble)
* 📊 Interactive financial analytics dashboard
* 📂 CSV/XLSX dataset upload and real-time processing
* 📉 Live visualization of prediction trends and indicators

---

## 🏗️ System Architecture
CI/CD pipeline (GitHub)
↓
Frontend (Streamlit UI)
↓
FastAPI Backend (Render)
↓
Data Preprocessing & Feature Engineering
↓
Deep Learning Models (LSTM / GRU / Transformer)
↓
Prediction Engine
↓
Output Layer (Forecast + Signals + Metrics)

---

## 📂 Project Structure

```
stock-ai-platform/
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── indicators.py
│   ├── train.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   ├── utils.py
│   └── requirements.txt
│
├── models/
│   ├── lstm_model.keras
│   ├── gru_model.keras
│   └── transformer_model.keras
│
├── data/
│   └── sample_stock_data.csv
│
├── tests/
│   ├── test_api.py
│   └── test_model.py
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── render.yaml
└── README.md
```

---

## ⚙️ Backend (FastAPI)

### 🚀 Capabilities

* REST APIs for stock prediction
* Technical indicator computation (RSI, SMA, EMA)
* Deep learning inference pipeline
* Dataset upload and processing

### ▶️ Run Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

### 📡 API Endpoints

* `GET /predict/{ticker}` → Stock price prediction
* `POST /upload-file` → Dataset ingestion

---

## 🎨 Frontend (Streamlit)

### 🚀 Capabilities

* Real-time AI stock prediction dashboard
* Interactive Plotly-based financial charts
* Dataset upload and analysis
* Model selection and comparison
* Live API integration

### ▶️ Run Locally

```bash
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 🤖 AI Models

| Model       | Type      | Use Case                      |
| ----------- | --------- | ----------------------------- |
| LSTM        | RNN       | Time-series forecasting       |
| GRU         | RNN       | Efficient sequence learning   |
| Transformer | Attention | Pattern recognition           |
| Ensemble    | Hybrid    | Final prediction optimization |

---

## 📊 Key Features

✔ End-to-end stock prediction pipeline
✔ Multi-deep learning architecture system
✔ FastAPI production backend
✔ Streamlit interactive dashboard
✔ Real-time API communication
✔ Technical indicators (RSI, EMA, SMA)
✔ Dataset upload support (CSV/XLSX)
✔ Docker-ready deployment
✔ Cloud deployment (Render + Streamlit Cloud)

---

## 🚀 Deployment

### Backend (Render)

* Containerized using Docker
* Hosted FastAPI service

### Frontend (Streamlit Cloud)

* Connected to backend API
* Live interactive dashboard

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🔥 Key Highlights (Recruiter Focus)

* Production-ready AI system with full MLOps pipeline
* Deep learning-based financial forecasting system
* Real-time API-driven architecture
* Scalable cloud deployment with Docker support
* End-to-end ML lifecycle implementation

---

## 👨‍💻 Author

**Prasanna Kumar**
AI/ML Engineer | Deep Learning | Generative AI | MLOps

---

## 📜 License

MIT License
