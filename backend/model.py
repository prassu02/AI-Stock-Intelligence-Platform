import numpy as np
import yfinance as yf


def predict_ensemble(ticker):

    # Download stock data
    df = yf.download(ticker, period="1y", progress=False)

    # Validate data
    if df.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    # Extract close prices safely
    close_prices = df["Close"].dropna().values

    # Convert last price to scalar float
    last_price = float(close_prices[-1])

    # Simulated GRU prediction
    gru_pred = last_price * (1 + np.random.normal(0, 0.01))

    # Simulated LSTM prediction
    lstm_pred = last_price * (1 + np.random.normal(0, 0.008))

    # Simulated Transformer prediction
    transformer_pred = last_price * (1 + np.random.normal(0, 0.012))

    # Weighted ensemble
    final_prediction = (
        0.4 * gru_pred +
        0.4 * lstm_pred +
        0.2 * transformer_pred
    )

    return round(final_prediction, 2)


def generate_signal(prediction, current_price=None):

    if current_price is not None:

        change = (prediction - current_price) / current_price

        if change > 0.02:
            return "BUY 📈"

        elif change < -0.02:
            return "SELL 📉"

    return "HOLD ⚖️"