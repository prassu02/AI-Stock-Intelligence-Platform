🚀 AI Stock Intelligence Platform

An end-to-end AI-powered stock prediction system using Deep Learning (LSTM, GRU, Transformer) with a FastAPI backend and Streamlit frontend dashboard, deployed on Render + Streamlit Cloud.
---
🌐 Live Deployments
🔗 Backend API: AI Stock Backend (Render)
🎨 Frontend App: AI Stock Streamlit App
📌 Project Overview
---
This system predicts stock prices and market signals using multiple deep learning models and provides:

📈 Stock price prediction
⚖️ Buy / Sell / Hold signals
🤖 AI model selection (LSTM / GRU / Transformer / Ensemble)
📊 Interactive dashboards
📂 Dataset upload & analysis
📉 Real-time visualizations
----
🏗️ Project Architecture
Frontend (Streamlit)
        ↓
FastAPI Backend (Render)
        ↓
ML Models (LSTM / GRU / Transformer)
        ↓
Preprocessing + Indicators
        ↓
Stock Prediction Output
---
📂 Folder Structure
stock-ai-platform/
│
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── indicators.py
│   ├── train.py
│   ├── config.py
│   ├── requirements_backend.txt
│   └── __init__.py
│
├── frontend/
│   ├── streamlit_app.py
│   ├── utils.py
│   ├── requirements_frontend.txt
│   └── __init__.py
│
├── models/
│   ├── gru_model.keras
│   ├── lstm_model.keras
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
├── requirements.txt
├── Procfile
└── README.md-
---
⚙️ Backend (FastAPI)
Features
REST API for predictions
Stock preprocessing pipeline
Technical indicators (RSI, MA, EMA)
Model inference engine
Run locally
cd backend
pip install -r requirements_backend.txt
uvicorn app:app --reload
API Endpoints
🔮 Predict Stock
GET /predict/{ticker}
📂 Upload Dataset
POST /upload-file
🎨 Frontend (Streamlit)
Features
Stock prediction dashboard
Interactive charts (Plotly)
Dataset upload & analysis
Model selection UI
Real-time API integration
Run locally
cd frontend
pip install -r requirements_frontend.txt
streamlit run streamlit_app.py
🤖 AI Models Used
Model	Type	Purpose
LSTM	RNN	Time-series forecasting
GRU	RNN	Fast sequence learning
Transformer	Attention	Advanced pattern learning
Ensemble	Hybrid	Best accuracy output
📊 Features
--
✔ AI-powered stock prediction
✔ Deep learning models (LSTM, GRU, Transformer)
✔ FastAPI backend architecture
✔ Streamlit interactive dashboard
✔ Real-time API communication
✔ Candlestick + Line charts
✔ Dataset upload (CSV/XLSX)
✔ Technical indicators
✔ Docker support
✔ Render + Streamlit deployment ready
--
🚀 Deployment
Backend (Render)
Build: Dockerfile.backend
Start: uvicorn app:app --host 0.0.0.0 --port 10000
Frontend (Streamlit Cloud)
Entry file: streamlit_app.py
Hosted on Streamlit Cloud
🧪 Testing
pytest tests/
📦 Requirements
Backend
fastapi
uvicorn
numpy
pandas
tensorflow
scikit-learn
Frontend
streamlit
requests
pandas
plotly
--
🔥 Key Highlights
Production-ready ML system
Clean modular architecture
Real-time API integration
Scalable deployment (Docker + Render)
Interactive AI dashboard
---
👨‍💻 Author

Prasanna Kumar
AI / Data Science Engineer
Machine Learning | Deep Learning | Full Stack AI Systems
--

📜 License

This project is licensed under the MIT License.
