import yfinance as yf
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from preprocessing import create_sequences, scale_data


def build_gru(input_shape):
    model = tf.keras.Sequential([
        layers.GRU(64, return_sequences=True, input_shape=input_shape),
        layers.GRU(32),
        layers.Dense(16, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    return model


def build_lstm(input_shape):
    model = tf.keras.Sequential([
        layers.LSTM(64, return_sequences=True, input_shape=input_shape),
        layers.LSTM(32),
        layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    return model


def build_transformer(input_shape):

    inputs = tf.keras.Input(shape=input_shape)

    x = layers.MultiHeadAttention(num_heads=4, key_dim=16)(inputs, inputs)
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dense(32, activation='relu')(x)
    outputs = layers.Dense(1)(x)

    model = tf.keras.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mse')

    return model


def train_models():

    df = yf.download("AAPL", period="5y")

    close = df['Close'].values

    scaled, scaler = scale_data(close)

    X, y = create_sequences(scaled)

    X = X.reshape(X.shape[0], X.shape[1], 1)

    gru_model = build_gru((X.shape[1], 1))
    lstm_model = build_lstm((X.shape[1], 1))
    transformer_model = build_transformer((X.shape[1], 1))

    gru_model.fit(X, y, epochs=3, batch_size=32)
    lstm_model.fit(X, y, epochs=3, batch_size=32)
    transformer_model.fit(X, y, epochs=3, batch_size=32)

    gru_model.save("models/gru_model.keras")
    lstm_model.save("models/lstm_model.keras")
    transformer_model.save("models/transformer_model.keras")

    print("Models trained and saved successfully")


if __name__ == "__main__":
    train_models()