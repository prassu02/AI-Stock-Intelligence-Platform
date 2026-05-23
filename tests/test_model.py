from backend.model import predict_ensemble


def test_prediction():
    result = predict_ensemble("AAPL")
    assert result > 0