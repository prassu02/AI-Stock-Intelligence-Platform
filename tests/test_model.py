import sys
import os

sys.path.append(os.path.abspath("."))

from backend.model import predict_ensemble

def test_model():
    result = predict_ensemble("AAPL")
    assert result is not None