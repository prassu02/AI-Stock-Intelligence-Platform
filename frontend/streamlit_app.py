import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from io import BytesIO

# ==============================
# THEME FIX (IMPORTANT)
# ==============================
pio.templates.default = "plotly_dark"

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="AI Stock Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

BACKEND_URL = "https://ai-stock-intelligence-backend1.onrender.com"

# ==============================
# CLEAN UI CSS
# ==============================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

/* Metrics FIX */
[data-testid="metric-container"] {
    background-color: #111827;
    border-radius: 12px;
    padding: 14px;
    border: 1px solid #374151;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 24px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #9CA3AF !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0F172A;
}

/* Inputs */
input, textarea {
    background-color: #111827 !important;
    color: #FFFFFF !important;
    border: 1px solid #374151 !important;
    border-radius: 10px !important;
}

/* Buttons */
.stButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 10px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.title("🚀 AI Stock Intelligence Platform")
st.markdown("### Deep Learning + FastAPI + Streamlit + Real-Time Analytics")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.header("⚙️ Controls")
if st.sidebar.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# STOCK LIST
ticker = st.sidebar.selectbox(
    "📈 Select Stock",
    ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "META", "NVDA"]
)

model_choice = st.sidebar.selectbox(
    "🤖 AI Model",
    ["Ensemble", "LSTM", "GRU", "Transformer"]
)

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Dataset",
    type=["csv", "xlsx"]
)

run_btn = st.sidebar.button("🚀 Run Analysis")

# ==============================
# API CALL (SAFE)
# ==============================
@st.cache_data(ttl=60)
def get_prediction(ticker):
    try:
        res = requests.get(
            f"{BACKEND_URL}/predict/{ticker}",
            timeout=10
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}

# ==============================
# STOCK ANALYSIS
# ==============================
if run_btn:

    with st.spinner("Running AI Models..."):

        data = get_prediction(ticker)

        if "error" in data:
            st.error(data["error"])
            st.stop()

        st.subheader("📊 Prediction Results")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Ticker", data.get("ticker", "N/A"))
        col2.metric("Price", f"${data.get('predicted_price', 0)}")
        col3.metric("Signal", data.get("signal", "N/A"))
        confidence = data.get("confidence")

        if confidence is None:
            confidence = 85  # fallback only if backend not sending
            
        col4.metric("Confidence", f"{confidence}%")

        signal = data.get("signal", "HOLD").upper()

        if signal == "BUY":
            st.success("📈 Strong Bullish Signal")
        elif signal == "SELL":
            st.error("📉 Bearish Signal")
        else:
            st.warning(f"⚖️ Market Signal: {signal}")

        # ==========================
        # TREND CHART
        # ==========================
        st.subheader("🧠 AI Explanation")

        st.info(
           data.get(
               "reason",
               "AI model predicts based on historical trend, volatility and momentum."
           )
        )
        st.subheader("📈 Price Trend")

        df = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "Price": [180, 185, 183, 190, data.get("predicted_price", 190)]
        })

        fig = px.line(df, x="Day", y="Price", markers=True)
        st.plotly_chart(fig, use_container_width=True)

        # ==========================
        # CANDLESTICK
        # ==========================
        st.subheader("🕯️ Candlestick Chart")

        candle = pd.DataFrame({
            "Date": pd.date_range("2025-01-01", periods=5),
            "Open": [180, 182, 184, 183, 188],
            "High": [185, 186, 188, 190, 193],
            "Low": [178, 180, 182, 181, 186],
            "Close": [182, 184, 183, 188, 190]
        })

        fig2 = go.Figure(data=[
            go.Candlestick(
                x=candle["Date"],
                open=candle["Open"],
                high=candle["High"],
                low=candle["Low"],
                close=candle["Close"]
            )
        ])

        st.plotly_chart(fig2, use_container_width=True)

        fi = data.get("feature_importance")

        if fi:
            st.subheader("📊 Feature Importance")
            st.bar_chart(pd.DataFrame(fi))
       
        with st.expander("Raw Response"):
            st.json(data)

# ==============================
# FILE UPLOAD
# ==============================
if uploaded_file:

    st.subheader("📂 Dataset Analysis")

    try:
        file_bytes = uploaded_file.getvalue()

        res = requests.post(
            f"{BACKEND_URL}/upload-file",
            files={"file": (uploaded_file.name, file_bytes)},
            timeout=20
        )

        file_data = res.json()

        st.success("File Uploaded")

        col1, col2 = st.columns(2)
        col1.metric("Rows", file_data.get("rows", 0))
        col2.metric("Columns", len(file_data.get("columns", [])))

        st.write(file_data.get("columns", []))

        df = pd.read_csv(BytesIO(file_bytes)) if uploaded_file.name.endswith(".csv") else pd.read_excel(BytesIO(file_bytes))

        st.dataframe(df.head(), use_container_width=True)

        numeric = df.select_dtypes(include="number").columns

        if len(numeric) > 0:
            col = st.selectbox("Select Column", numeric)

            chart = st.radio("Chart", ["Line", "Histogram", "Box"], horizontal=True)

            if chart == "Line":
                fig = px.line(df, y=col)
            elif chart == "Histogram":
                fig = px.histogram(df, x=col)
            else:
                fig = px.box(df, y=col)

            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"File Error: {e}")

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("🚀 Built with ❤️ FastAPI + Streamlit + Deep Learning + Plotly")
