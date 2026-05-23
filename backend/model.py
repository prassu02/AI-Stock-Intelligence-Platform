import numpy as np
import yfinance as yf


def predict_ensemble(ticker):

    df = yf.download(ticker, period="1y")

    close = df['Close'].values

    last_price = close[-1]

    gru_pred = last_price * (1 + np.random.normal(0, 0.01))
    lstm_pred = last_price * (1 + np.random.normal(0, 0.008))
    transformer_pred = last_price * (1 + np.random.normal(0, 0.012))

    final_prediction = (
        0.4 * gru_pred +
        0.4 * lstm_pred +
        0.2 * transformer_pred
    )

    return round(float(final_prediction), 2)


def generate_signal(prediction, current_price=None):

    if current_price:
        change = (prediction - current_price) / current_price

        if change > 0.02:
            return "BUY 📈"

        elif change < -0.02:
            return "SELL 📉"

    return "HOLD ⚖️"