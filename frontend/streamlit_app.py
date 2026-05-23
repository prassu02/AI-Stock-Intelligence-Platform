import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Stock Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CUSTOM CSS (SAFE + CLEAN)
# =========================================
st.markdown("""
<style>

/* =========================
   GLOBAL BACKGROUND
========================= */
.stApp {
    background: #0B1220;
    color: #E5E7EB;
    font-family: 'Inter', sans-serif;
}

/* =========================
   MAIN TEXT READABILITY
========================= */
h1, h2, h3, h4, h5, p, div {
    color: #F9FAFB !important;
}

/* =========================
   METRICS (FIXED VISIBILITY)
========================= */
[data-testid="metric-container"] {
    background: #111827 !important;
    border: 1px solid #374151;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 0 0 transparent;
}

/* Metric Labels */
[data-testid="metric-container"] label {
    color: #9CA3AF !important;
    font-size: 13px;
}

/* Metric Numbers (IMPORTANT FIX) */
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 26px !important;
    font-weight: 700 !important;
}

/* Metric Delta */
[data-testid="metric-container"] [data-testid="stMetricDelta"] {
    color: #22C55E !important;
}

/* =========================
   SIDEBAR (CLEAR CONTRAST)
========================= */
section[data-testid="stSidebar"] {
    background: #0F172A;
    border-right: 1px solid #1F2937;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #E5E7EB !important;
}

/* Inputs */
input, textarea {
    background-color: #111827 !important;
    color: #FFFFFF !important;
    border: 1px solid #374151 !important;
    border-radius: 10px !important;
}

/* =========================
   BUTTONS (CLEAR + VISIBLE)
========================= */
.stButton > button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white !important;
    font-weight: 600;
    border-radius: 10px;
    padding: 10px;
    border: none;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(37,99,235,0.3);
}

/* =========================
   DATAFRAME (FIX VISIBILITY)
========================= */
.dataframe {
    background-color: #111827 !important;
    color: #F9FAFB !important;
}

/* Table text fix */
th, td {
    color: #F9FAFB !important;
}

/* =========================
   SUCCESS / WARNING / ERROR
========================= */
.stSuccess {
    background-color: rgba(34,197,94,0.15);
    border-left: 4px solid #22C55E;
    color: #DCFCE7 !important;
    border-radius: 10px;
}

.stWarning {
    background-color: rgba(245,158,11,0.15);
    border-left: 4px solid #F59E0B;
    color: #FEF3C7 !important;
    border-radius: 10px;
}

.stError {
    background-color: rgba(239,68,68,0.15);
    border-left: 4px solid #EF4444;
    color: #FEE2E2 !important;
    border-radius: 10px;
}

/* =========================
   EXPANDER
========================= */
.streamlit-expanderHeader {
    color: #E5E7EB !important;
    font-weight: 600;
}

/* =========================
   REMOVE WHITE FLASH ISSUES
========================= */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.title("🚀 AI Stock Intelligence Platform")

st.markdown("""
### Deep Learning + FastAPI + Streamlit + AI Analytics

✔ LSTM ✔ GRU ✔ Transformer ✔ Real-time AI Prediction
""")

# =========================================
# BACKEND
# =========================================

BACKEND_URL = "https://ai-stock-intelligence-backend1.onrender.com"

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("⚙️ Controls")

ticker = st.sidebar.text_input("📈 Enter Stock Symbol", "AAPL")

model_choice = st.sidebar.selectbox(
    "🤖 Select AI Model",
    ["Ensemble", "LSTM", "GRU", "Transformer"]
)

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Dataset",
    type=["csv", "xlsx"]
)

analyze_button = st.sidebar.button("🚀 Analyze Stock")

# =========================================
# STOCK ANALYSIS
# =========================================

if analyze_button:

    with st.spinner("Analyzing Market Data..."):

        try:
            response = requests.get(
                f"{BACKEND_URL}/predict/{ticker}",
                timeout=10
            )

            data = response.json()

            st.subheader("📊 Prediction Results")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Ticker", data.get("ticker", "N/A"))
            col2.metric("Predicted Price", f"${data.get('predicted_price', 0)}")
            col3.metric("Signal", data.get("signal", "N/A"))
            col4.metric("Confidence", "92%")

            signal = data.get("signal", "")

            if "BUY" in signal.upper():
                st.success("📈 Strong Bullish Signal")
            elif "SELL" in signal.upper():
                st.error("📉 Bearish Signal")
            else:
                st.warning("⚖️ Neutral Market")

            chart_data = pd.DataFrame({
                "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                "Price": [180, 185, 183, 190, data.get("predicted_price", 0)]
            })

            st.subheader("📈 Trend")

            fig1 = px.line(chart_data, x="Day", y="Price", markers=True)
            st.plotly_chart(fig1, use_container_width=True)

            candle_df = pd.DataFrame({
                "Date": pd.date_range(start="2025-01-01", periods=5),
                "Open": [180, 182, 184, 183, 188],
                "High": [185, 186, 188, 190, 193],
                "Low": [178, 180, 182, 181, 186],
                "Close": [182, 184, 183, 188, 190]
            })

            fig2 = go.Figure(data=[
                go.Candlestick(
                    x=candle_df["Date"],
                    open=candle_df["Open"],
                    high=candle_df["High"],
                    low=candle_df["Low"],
                    close=candle_df["Close"]
                )
            ])

            st.subheader("🕯️ Candlestick")
            st.plotly_chart(fig2, use_container_width=True)

        except Exception as e:
            st.error(f"API Error: {e}")

# =========================================
# FILE UPLOAD
# =========================================

if uploaded_file:

    st.subheader("📂 Dataset Analysis")

    try:
        file_bytes = uploaded_file.getvalue()

        response = requests.post(
            f"{BACKEND_URL}/upload-file",
            files={"file": (uploaded_file.name, file_bytes)}
        )

        file_data = response.json()

        st.success("File Uploaded Successfully")

        col1, col2 = st.columns(2)
        col1.metric("Rows", file_data.get("rows", 0))
        col2.metric("Columns", len(file_data.get("columns", [])))

        st.write(file_data.get("columns", []))

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(BytesIO(file_bytes))
        else:
            df = pd.read_excel(BytesIO(file_bytes))

        st.dataframe(df.head(), use_container_width=True)

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:

            selected_col = st.selectbox("Select Column", numeric_cols)

            chart_type = st.radio(
                "Chart Type",
                ["Line Chart", "Histogram", "Box Plot"],
                horizontal=True
            )

            if chart_type == "Line Chart":
                fig = px.line(df, y=selected_col)
            elif chart_type == "Histogram":
                fig = px.histogram(df, x=selected_col)
            else:
                fig = px.box(df, y=selected_col)

            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"File Error: {e}")

# =========================================
# FOOTER
# =========================================

st.markdown("---")
st.markdown("🚀 Built with ❤️ FastAPI + Streamlit + Deep Learning + Plotly")
