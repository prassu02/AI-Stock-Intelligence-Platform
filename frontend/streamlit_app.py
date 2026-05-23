import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="AI Stock Intelligence Platform",
    page_icon="🚀",
    layout="wide"
)

BACKEND_URL = "https://ai-stock-intelligence-backend1.onrender.com"

# ==============================
# CSS (CLEAN + MODERN UI)
# ==============================
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.stMetric {
    background-color: #1E1E1E;
    padding: 14px;
    border-radius: 12px;
    border: 1px solid #333;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.title("🚀 AI Stock Intelligence Platform")
st.markdown("### Deep Learning + FastAPI + Streamlit + Real-time Analytics")

# ==============================
# SIDEBAR CONTROLS
# ==============================
st.sidebar.header("⚙️ Controls")

ticker = st.sidebar.text_input("📈 Stock Symbol", "AAPL")

model_choice = st.sidebar.selectbox(
    "🤖 Model",
    ["Ensemble", "LSTM", "GRU", "Transformer"]
)

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Dataset",
    type=["csv", "xlsx"]
)

run_btn = st.sidebar.button("🚀 Run Analysis")

# ==============================
# SAFE API CALL (CACHED)
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
# MAIN ANALYSIS
# ==============================
if run_btn:

    with st.spinner("🔄 Running AI Models..."):

        data = get_prediction(ticker)

        if "error" in data:
            st.error(f"API Error: {data['error']}")
            st.stop()

        # ==========================
        # METRICS
        # ==========================
        st.subheader("📊 Prediction Results")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Ticker", data.get("ticker", "N/A"))
        col2.metric("Price", f"${data.get('predicted_price', 0)}")
        col3.metric("Signal", data.get("signal", "N/A"))

        confidence = data.get("confidence", "N/A")
        col4.metric("Confidence", f"{confidence}")

        # ==========================
        # SIGNAL UI
        # ==========================
        signal = data.get("signal", "")

        if "BUY" in signal:
            st.success("📈 Strong Bullish Signal")
        elif "SELL" in signal:
            st.error("📉 Bearish Signal")
        else:
            st.warning("⚖️ Neutral / Hold Market")

        # ==========================
        # MODEL INFO
        # ==========================
        colA, colB = st.columns(2)
        colA.info(f"Selected Model: {model_choice}")
        colB.info("Prediction Window: Next Session")

        # ==========================
        # TREND CHART
        # ==========================
        st.subheader("📈 Price Trend")

        chart_df = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "Price": [180, 185, 183, 190, data.get("predicted_price", 190)]
        })

        fig = px.line(chart_df, x="Day", y="Price", markers=True)
        st.plotly_chart(fig, use_container_width=True)

        # ==========================
        # CANDLESTICK
        # ==========================
        st.subheader("🕯️ Candlestick Chart")

        candle_df = pd.DataFrame({
            "Date": pd.date_range("2025-01-01", periods=5),
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

        st.plotly_chart(fig2, use_container_width=True)

        # ==========================
        # RAW JSON
        # ==========================
        with st.expander("🔍 Raw API Response"):
            st.json(data)

# ==============================
# FILE UPLOAD
# ==============================
if uploaded_file:

    st.subheader("📂 Dataset Analysis")

    try:
        file_bytes = uploaded_file.getvalue()

        with st.spinner("Uploading file..."):
            response = requests.post(
                f"{BACKEND_URL}/upload-file",
                files={"file": (uploaded_file.name, file_bytes)},
                timeout=20
            )
            file_data = response.json()

        st.success("File uploaded successfully")

        col1, col2 = st.columns(2)
        col1.metric("Rows", file_data.get("rows", 0))
        col2.metric("Columns", len(file_data.get("columns", [])))

        st.write("### Columns")
        st.write(file_data.get("columns", []))

        # Load DataFrame
        df = pd.read_csv(BytesIO(file_bytes)) if uploaded_file.name.endswith(".csv") else pd.read_excel(BytesIO(file_bytes))

        st.subheader("📊 Preview")
        st.dataframe(df.head(), use_container_width=True)

        st.subheader("📋 Info")
        c1, c2 = st.columns(2)
        c1.write(f"Shape: {df.shape}")
        c2.write(f"Missing: {df.isnull().sum().sum()}")

        # Visualization
        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:
            st.subheader("📈 Visualization")

            col = st.selectbox("Select Column", numeric_cols)
            chart = st.radio("Chart Type", ["Line", "Histogram", "Box"], horizontal=True)

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
st.markdown("### 🚀 AI Stock Intelligence Platform")
st.markdown("✔ FastAPI + Streamlit + Deep Learning + Real-time Analytics")
st.markdown("---")
st.markdown("Built with ❤️ using AI + ML + Streamlit")
