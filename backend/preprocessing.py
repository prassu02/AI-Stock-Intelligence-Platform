import numpy as np
from sklearn.preprocessing import MinMaxScaler


def create_sequences(data, seq_length=60):
    X = []
    y = []

    for i in range(seq_length, len(data)):
        X.append(data[i-seq_length:i])
        y.append(data[i])

    return np.array(X), np.array(y)


def scale_data(data):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data.reshape(-1, 1))
    return scaled, scaler